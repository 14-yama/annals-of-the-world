#!/usr/bin/env python3
"""
Batch 44 — 8 entities (Class 394): Military Alliances
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/394-Class-394"
FILE_PREFIX = "394"


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

    ("nato", {
        "summary": (
            "The North Atlantic Treaty Organization (NATO, est. 4 April 1949, Washington D.C. — founded by 12 Western democracies as a collective defence alliance against Soviet expansion, currently 32 members) is the most successful military alliance in history — maintaining the security architecture of the Western world for 75 years without a single Article 5 collective defence obligation being triggered against a member state. NATO's founding principle — that 'an attack on one is an attack on all' (Article 5) — created the mutual security guarantee that underpinned the post-war liberal democratic order and deterred Soviet military aggression against Western Europe throughout the Cold War.\n\n"
            "NATO was founded in 1949 in direct response to the Soviet coup in Czechoslovakia (February 1948) and the Berlin Blockade (June 1948–May 1949) — which demonstrated that the Soviet Union was willing to use coercion to expand its sphere of influence. The North Atlantic Treaty (4 April 1949) — signed by the United States, Canada, the United Kingdom, France, Belgium, the Netherlands, Luxembourg, Norway, Denmark, Iceland, Italy, and Portugal — committed all signatories to the collective defence of any member attacked by an external power.\n\n"
            "Article 5 was invoked only once in NATO's history — on 12 September 2001, the day after the 9/11 attacks, when the Alliance determined that the attacks on the United States were an attack on all members. NATO's post-Cold War expansion — from 12 original members to 32 (2024, following Sweden's accession) — has been the most consequential change in European security architecture since 1945, with Russia's February 2022 invasion of Ukraine accelerating both Finland's (2023) and Sweden's (2024) accession."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Most successful military alliance in history (est. 4 April 1949, Washington D.C., 12 founding members, now 32); collective defence underpinned Western post-war liberal democratic order; deterred Soviet military aggression throughout Cold War; Article 5 invoked only once (September 12, 2001, post-9/11); post-Cold War expansion 12→32 members; Finland (2023) and Sweden (2024) accession accelerated by Russia's Ukraine invasion (2022); founding: Soviet coup Czechoslovakia (1948) and Berlin Blockade (1948–1949) as triggers.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Soviet coup in Czechoslovakia (February 1948) and the Berlin Blockade (June 1948–May 1949) — which demonstrated Soviet willingness to use coercion against European democracies — created the immediate political urgency for a formal mutual defence treaty, overcoming US Senate resistance to peacetime military alliances",
            "The Vandenberg Resolution (June 1948) — in which the US Senate authorised the United States to join peacetime collective security organisations — provided the constitutional basis for US participation in NATO, overcoming the isolationist tradition that had prevented US membership in the League of Nations",
            "The British and European recognition that US security guarantees were essential for Western European defence — given the devastation of WWII and the Soviet threat — drove the intense diplomatic effort to persuade the United States to commit formally to European defence, culminating in Article 5's mutual defence guarantee"
        ],
        "effects": [
            "NATO's collective defence guarantee — deterring Soviet military aggression against Western Europe throughout the Cold War — is the primary reason that no NATO member state was ever attacked by Soviet or Warsaw Pact forces, preserving the liberal democratic order in Western Europe for 40 years",
            "NATO's post-Cold War expansion — admitting Central and Eastern European states (Poland, Czech Republic, Hungary in 1999; Baltic states in 2004; Romania, Bulgaria in 2004) — extended the liberal democratic security architecture into the former Soviet sphere, permanently changing the European security map and provoking growing Russian hostility that culminated in the Ukraine invasion",
            "Russia's invasion of Ukraine (February 2022) — which was partly justified by Vladimir Putin as a response to NATO expansion — paradoxically drove Finland and Sweden to abandon their traditional military non-alignment and apply for NATO membership, adding two militarily significant members and extending NATO's Arctic flank",
            "NATO's only Article 5 invocation (September 12, 2001) — following the 9/11 attacks — led to the ISAF mission in Afghanistan (2001–2021), NATO's first out-of-area combat operation, demonstrating that the Alliance could operate beyond its treaty area while also revealing the limits of collective action in counter-insurgency"
        ],
        "relationships": [
            {"entity": "Berlin Blockade (1948–1949, Soviet coercion, NATO founding trigger)", "relationship": "IMMEDIATE_POLITICAL_CATALYST_FOR_THE_FOUNDING_OF", "note": "The Berlin Blockade — Soviet coercion against a Western-occupied city — created the urgency that overcame US Senate resistance to the peacetime military alliance"},
            {"entity": "Article 5 collective defence (invoked September 12, 2001, 9/11)", "relationship": "COLLECTIVE_SECURITY_ARCHITECTURE_DEFINED_BY", "note": "Article 5's mutual defence guarantee — invoked only once, post-9/11 — is the foundational principle that has deterred military aggression against NATO members for 75 years"},
            {"entity": "Russia's invasion of Ukraine (February 2022, NATO expansion paradox)", "relationship": "EXPANSION_ACCELERATED_BY_THE", "note": "Russia's Ukraine invasion — justified partly as response to NATO expansion — paradoxically drove Finland and Sweden to join, extending NATO's Arctic flank"},
            {"entity": "Cold War (deterrence of Soviet military aggression, 40 years)", "relationship": "PRIMARY_WESTERN_MILITARY_SECURITY_ARCHITECTURE_THROUGHOUT_THE", "note": "NATO's 40-year deterrence of Soviet aggression against Western Europe is the primary reason no NATO member was attacked during the Cold War"},
            {"entity": "ISAF Afghanistan mission (2001–2021, first out-of-area NATO operation)", "relationship": "CONDUCTED_THE_FIRST_OUT-OF-AREA_COMBAT_OPERATION", "note": "The ISAF mission — NATO's response to the Article 5 invocation after 9/11 — was the Alliance's first out-of-area operation, revealing limits of collective action in counter-insurgency"}
        ],
    }),

    ("axis-powers", {
        "summary": (
            "The Axis Powers (1936–1945 — the alliance of Nazi Germany, Fascist Italy, and Imperial Japan, formally constituted by the Berlin-Rome-Tokyo Axis) were the principal adversaries of the Allied nations in World War II and the most destructive military alliance in human history — responsible for the deaths of 70–85 million people (the deadliest conflict in history), the Holocaust (6 million Jews, 5–6 million others), and the systematic devastation of three continents. The Axis alliance was ideologically unified by fascism, ultranationalism, and opposition to liberal democracy and Soviet communism, but operationally fragmented by geography, competing strategic interests, and the inability to coordinate a genuinely unified military strategy.\n\n"
            "The Axis began with the Rome-Berlin Pact (October 1936) and the Anti-Comintern Pact between Germany and Japan (November 1936) — forming the framework for an anti-Soviet ideological alignment that Italy joined in 1937. The Tripartite Pact (September 27, 1940) formally constituted the three-power Axis and created the mutual defence framework that would theoretically commit each to war if the others were attacked. The Axis was subsequently joined by Hungary, Romania, Bulgaria, Slovakia, Croatia, and other satellite states.\n\n"
            "The Axis powers' simultaneous defeat — Germany's unconditional surrender (8 May 1945) and Japan's surrender (2 September 1945) after the atomic bombings of Hiroshima and Nagasaki — was the foundational moment of the post-war international order, leading directly to the creation of the United Nations, the Nuremberg trials, the decolonisation movement, and the Cold War."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Principal adversaries of Allies in WWII (1936–1945); Nazi Germany, Fascist Italy, Imperial Japan; 70–85 million deaths (deadliest conflict in history); Holocaust (6M Jews, 5–6M others); Rome-Berlin Pact (1936), Anti-Comintern Pact (1936), Tripartite Pact (1940); ideologically unified by fascism/ultranationalism, operationally fragmented; defeat led to UN founding, Nuremberg trials, decolonisation, Cold War; most destructive military alliance in human history.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Great Depression's political destabilisation of European democracies — enabling the rise of fascist movements in Italy (Mussolini, 1922), Germany (Hitler, 1933), and ultranationalist military government in Japan — created the ideological and political conditions for an alignment of authoritarian regimes opposed to liberal democracy and the Versailles order",
            "The Treaty of Versailles's perceived injustices — particularly against Germany (war guilt clause, reparations, territorial losses) and Italy (denied expected territorial gains despite wartime contribution) — created the nationalist grievances that fascist leaders exploited to justify revision of the post-WWI order by force",
            "The Western democracies' appeasement policy — culminating in the Munich Agreement (September 1938), which sacrificed Czechoslovakia to Hitler's demands — demonstrated that democratic governments would not resist fascist expansion until it directly threatened vital interests, emboldening Hitler's strategic gambles and enabling the Axis to prepare for a larger war"
        ],
        "effects": [
            "The Axis's defeat and the Nuremberg trials (1945–1946) — the first international tribunal for war crimes and crimes against humanity — established the principles of individual criminal accountability for state-sponsored atrocities that became the foundation of international humanitarian law, the Genocide Convention (1948), and eventually the International Criminal Court (2002)",
            "The Axis powers' territorial ambitions and military aggression — destroying the pre-war European order — paradoxically accelerated decolonisation by weakening the European imperial powers, demonstrating that European military superiority was not invincible, and creating the moral contradiction between Allied claims to fight for freedom and the maintenance of colonial empires",
            "The Holocaust — the Axis's genocide of 6 million Jews and 5–6 million others (Roma, disabled persons, political prisoners, Soviet POWs) — transformed Jewish political consciousness and international Jewish community support for a Jewish state, directly enabling the founding of Israel (1948) and shaping the human rights architecture of the post-war international order",
            "The Axis alliance's operational failures — Germany and Japan never coordinated strategy against the Soviet Union and the United States, and Germany's defeat at Stalingrad (1943) removed any possibility of a Japanese-German strategic linkup — demonstrated that ideological affinity cannot substitute for genuine operational coordination, making the Axis a historically significant study in alliance failure"
        ],
        "relationships": [
            {"entity": "Holocaust (6 million Jews, 5-6 million others, Nazi Germany)", "relationship": "PERPETRATED_BY_THE_PRIMARY_MEMBER_OF_THE", "note": "The Holocaust — the Axis's genocide — transformed post-war international human rights law and directly enabled Israel's founding"},
            {"entity": "Tripartite Pact (September 27, 1940, formal Axis constitution)", "relationship": "FORMALLY_CONSTITUTED_BY_THE", "note": "The 1940 Tripartite Pact formally bound Germany, Italy, and Japan in a mutual defence framework that defined the Axis alliance"},
            {"entity": "Nuremberg trials (1945–1946, individual criminal accountability for war crimes)", "relationship": "DEFEAT_PRODUCED_THE_FOUNDATIONAL_ACCOUNTABILITY_MECHANISM_OF_THE", "note": "The Nuremberg trials — establishing individual accountability for war crimes — were a direct consequence of Axis defeat and atrocities"},
            {"entity": "Munich Agreement (1938, appeasement, Western democracies)", "relationship": "EMBOLDENED_BY_THE_APPEASEMENT_POLICY_CULMINATING_IN_THE", "note": "Western appeasement — demonstrated by Munich — convinced Hitler that democratic governments would not resist expansion, enabling Axis strategic gambles"},
            {"entity": "World War II (70–85 million deaths, Axis-Allied conflict)", "relationship": "PRIMARY_ADVERSARY_COALITION_IN_THE", "note": "The Axis's 1936–1945 military campaign — responsible for 70–85 million deaths — was the defining causative factor of WWII's destructiveness"}
        ],
    }),

    ("allies-of-world-war-ii", {
        "summary": (
            "The Allies of World War II (1939–1945 — the coalition of nations that opposed the Axis powers, led by the United States, the United Kingdom, the Soviet Union, and the Republic of China — the 'Big Four') were the victorious military alliance in history's deadliest conflict, winning the war at a cost of 70–85 million lives and reshaping the entire global political order. The Allies were an ideologically heterogeneous coalition — combining liberal democracies, a communist superpower, colonial empires, and dozens of smaller states — unified by the immediate necessity of defeating fascism rather than by shared long-term political values.\n\n"
            "The Allied coalition evolved over the war's course: Britain fought alone from the fall of France (June 1940) to the Nazi invasion of the Soviet Union (June 1941); the Soviet Union joined after Operation Barbarossa (22 June 1941); the United States after Pearl Harbor (7 December 1941). The full Allied coalition — formalised by the Declaration by United Nations (1 January 1942), signed by 26 nations — created the institutional precursor to the United Nations and committed all signatories to the Atlantic Charter's principles.\n\n"
            "The Allies' wartime conferences — Tehran (1943), Yalta (February 1945), and Potsdam (July–August 1945) — were the forums in which the post-war world order was designed, with the United States, Britain, and the Soviet Union dividing spheres of influence, agreeing the occupation of Germany, planning the United Nations, and setting the conditions for the Cold War that divided the victorious coalition almost immediately after Japan's surrender."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Victorious coalition of WWII (1939–1945); US, UK, Soviet Union, China — 'Big Four'; Declaration by United Nations (1 January 1942, 26 nations) — precursor to UN; ideologically heterogeneous (liberal democracies + communist superpower + colonial empires); Tehran (1943), Yalta (February 1945), Potsdam (July-August 1945) conferences designed the post-war world order; won at 70–85 million lives; United Nations founding (1945); Cold War emerged immediately after victory; most consequential military coalition in history.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Nazi Germany's military aggression — invading Poland (September 1939), France (May 1940), and the Soviet Union (June 1941) — forced nations with deeply incompatible political systems into a coalition of necessity, uniting liberal democracies with the Soviet Union in the common cause of military survival",
            "The Atlantic Charter (August 1941) — agreed by Roosevelt and Churchill before US entry into the war — established the ideological framework for Allied war aims: self-determination, free trade, collective security, and the prohibition of territorial aggrandisement, creating the moral foundation for the Allied cause and the basis for the post-war liberal international order",
            "The Japanese attack on Pearl Harbor (7 December 1941) — bringing the United States into the war — completed the Allied coalition by adding the world's largest industrial economy, transforming what had been a European conflict into a genuinely global war and ensuring that Axis defeat was ultimately inevitable given the Allied powers' combined industrial and demographic superiority"
        ],
        "effects": [
            "The Allied victory — and the Declaration by United Nations (1942) which evolved into the United Nations Charter (1945) — created the post-war multilateral institutional architecture: the United Nations, the International Monetary Fund, the World Bank, and GATT (later WTO), establishing the rules-based international order that has governed global affairs since 1945",
            "The Allied wartime conferences — Yalta (February 1945) in particular, where Roosevelt, Churchill, and Stalin divided Europe into spheres of influence, agreed German occupation zones, and established the basis for the UN Security Council's veto system — designed the post-war world in ways that created both the institutional framework of the liberal order and the spheres of influence that generated the Cold War",
            "The Allied prosecution of the Nuremberg and Tokyo war crimes trials — establishing that national leaders could be held individually accountable for crimes against humanity and war crimes — created the international criminal law framework that eventually produced the International Criminal Court (2002) and represents the most significant expansion of international law in the 20th century",
            "The Allied coalition's post-war fragmentation — with the wartime US-Soviet alliance collapsing almost immediately into the Cold War — demonstrated that strategic necessity can temporarily unite ideologically incompatible partners but cannot sustain an alliance once the unifying threat is removed"
        ],
        "relationships": [
            {"entity": "United Nations (1945 founding, Declaration by United Nations 1942 precursor)", "relationship": "DIRECT_INSTITUTIONAL_PRECURSOR_OF_THE", "note": "The Declaration by United Nations (1942) — binding 26 Allied nations — was the direct precursor to the UN Charter (1945) and the post-war institutional order"},
            {"entity": "Atlantic Charter (1941, Roosevelt-Churchill, war aims and post-war vision)", "relationship": "IDEOLOGICAL_FRAMEWORK_FOR_ALLIED_WAR_AIMS_ESTABLISHED_BY_THE", "note": "The Atlantic Charter's principles — self-determination, free trade, collective security — defined the Allied cause and the basis for the post-war liberal international order"},
            {"entity": "Yalta Conference (February 1945, Roosevelt-Churchill-Stalin, post-war world design)", "relationship": "POST-WAR_WORLD_ORDER_DESIGNED_AT_THE", "note": "Yalta — dividing Europe into spheres, agreeing German occupation, planning UN veto structure — created both the institutional framework and the Cold War geopolitical fault lines"},
            {"entity": "Nuremberg trials (1945–1946, individual accountability, international criminal law)", "relationship": "PROSECUTED_THE_LANDMARK_WAR_CRIMES_TRIALS_OF_THE", "note": "The Allied war crimes prosecution established individual accountability for crimes against humanity — the most significant expansion of international law in the 20th century"},
            {"entity": "Pearl Harbor (7 December 1941, US entry into war, coalition completion)", "relationship": "FINAL_COALITION_MEMBER_JOINED_AFTER_THE", "note": "Japan's Pearl Harbor attack completed the Allied coalition by bringing US industrial power into the war, ensuring that Axis defeat was ultimately inevitable"}
        ],
    }),

    ("central-powers", {
        "summary": (
            "The Central Powers (1914–1918 — the military alliance of Germany, Austria-Hungary, the Ottoman Empire, and Bulgaria in World War I) were the adversaries of the Entente (Allied) powers in the first genuinely industrialised global war — responsible for 9 million military deaths and the destabilisation of four empires that would collapse before the war's end. The Central Powers' defeat in November 1918 produced the most consequential political reorganisation in European history: the dissolution of the German Empire, the Austro-Hungarian Empire, the Ottoman Empire, and the Russian Empire, creating the successor states that defined 20th-century European and Middle Eastern politics.\n\n"
            "The Central Powers alliance evolved from the pre-war Triple Alliance (Germany, Austria-Hungary, Italy — though Italy remained neutral in 1914) into the wartime coalition. The Austro-Hungarian ultimatum to Serbia (July 1914) — following the assassination of Archduke Franz Ferdinand — triggered the alliance mechanisms that produced the war, with Germany's Blank Check to Austria-Hungary (5 July 1914) being the critical decision that made a general European war probable.\n\n"
            "The Central Powers' strategic situation — fighting a two-front war against the Entente in the West and Russia in the East — was ultimately insurmountable, but Germany's military genius produced a series of near-victories: the Schlieffen Plan's near-success in 1914, the Brest-Litovsk peace with Russia (March 1918) that freed the Eastern Front, and the Spring Offensive (March–July 1918) that came close to breaking the Western Front before American reinforcements and German exhaustion ended the last offensive."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "WWI military alliance (1914–1918): Germany, Austria-Hungary, Ottoman Empire, Bulgaria; 9 million military deaths; defeat produced most consequential political reorganisation in European history; collapse of German Empire, Austro-Hungarian Empire, Ottoman Empire, Russian Empire; Blank Check to Austria-Hungary (5 July 1914); Brest-Litovsk peace with Russia (March 1918); Spring Offensive (1918) near-success; successor states defined 20th-century European and Middle Eastern politics; Treaty of Versailles consequences drove WWII.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Triple Alliance (Germany, Austria-Hungary, Italy — 1882) and the Anglo-French-Russian Entente created the interlocking alliance systems that transformed the localised Austro-Serbian conflict into a general European war, with Germany's Blank Check to Austria-Hungary (5 July 1914) removing the last constraint on Austro-Hungarian escalation",
            "Germany's strategic doctrine of preventive war — the Schlieffen Plan's requirement for a rapid Western victory before Russian mobilisation could threaten the Eastern Front — created the military logic that made escalation, once begun, almost impossible to stop, as each day of delay reduced Germany's strategic margin",
            "The Ottoman Empire's entry into the war (October 1914) on the Central Powers' side — driven by German naval support (the transfer of the Goeben and Breslau) and Ottoman desire to recover lost territories — extended the war to the Middle East, creating the conditions for the Gallipoli campaign, the Arab Revolt, and ultimately the Sykes-Picot partition of the Ottoman Empire"
        ],
        "effects": [
            "The Central Powers' defeat and the subsequent peace treaties — Versailles (Germany), Saint-Germain (Austria), Trianon (Hungary), Sèvres/Lausanne (Ottoman), and Neuilly (Bulgaria) — dissolved four empires and created the map of Europe and the Middle East that defined 20th-century politics, with the successor states' instability contributing to WWII",
            "The Ottoman Empire's dissolution — accelerated by its defeat with the Central Powers — produced the Sykes-Picot partition of the Middle East (1916), the Balfour Declaration (1917), and the eventual creation of the mandate territories that became Israel, Palestine, Iraq, Syria, Lebanon, and Jordan, shaping the Middle East's modern political conflicts",
            "Germany's defeat at the Central Powers — and the 'stab-in-the-back' myth (Dolchstoßlegende) that blamed the German defeat on internal betrayal rather than military failure — created the political narrative that Nazi propaganda exploited to undermine the Weimar Republic and justify WWII as a war of national restoration",
            "The Treaty of Brest-Litovsk (March 1918) — Germany's peace treaty with the new Bolshevik government, imposing harsh terms on Russia — was the template for the victorious Allies' Versailles Treaty with Germany, demonstrating that great power peace treaties can embed the grievances that generate the next conflict"
        ],
        "relationships": [
            {"entity": "Germany's Blank Check to Austria-Hungary (5 July 1914, war decision)", "relationship": "CRITICAL_DECISION_ENABLING_THE_FORMATION_OF_THE", "note": "The Blank Check — Germany's unconditional support for Austria-Hungary against Serbia — was the decision that made a general European war probable and activated the Central Powers alliance"},
            {"entity": "Schlieffen Plan (German two-front war strategy, near-success 1914)", "relationship": "PRIMARY_STRATEGIC_DOCTRINE_OF_THE_DOMINANT_MEMBER_OF_THE", "note": "The Schlieffen Plan's logic — rapid Western victory before Russian mobilisation — drove the Central Powers' opening strategy and failed to produce the decisive result needed"},
            {"entity": "Treaty of Brest-Litovsk (March 1918, Russia-Germany peace, Eastern Front freed)", "relationship": "MOST_CONSEQUENTIAL_WARTIME_DIPLOMATIC_SUCCESS_OF_THE", "note": "Brest-Litovsk freed Germany's Eastern Front — but too late and too costly to change the Western Front outcome"},
            {"entity": "Dissolution of Ottoman Empire (Sykes-Picot, Balfour, Middle East partition)", "relationship": "DEFEAT_DIRECTLY_PRODUCED_THE_CONDITIONS_FOR_THE", "note": "Ottoman defeat with the Central Powers produced Sykes-Picot, the Balfour Declaration, and the Middle East mandate system that shaped modern regional conflicts"},
            {"entity": "Dolchstoßlegende ('stab-in-the-back' myth, Weimar Republic undermining, Nazi exploitation)", "relationship": "DEFEAT_GENERATED_THE_POLITICAL_NARRATIVE_OF_THE", "note": "The stab-in-the-back myth — attributing Central Powers defeat to internal betrayal — was the foundational lie that Nazi propaganda used to undermine Weimar democracy"}
        ],
    }),

    ("holy-alliance", {
        "summary": (
            "The Holy Alliance (26 September 1815 — the conservative political-religious alliance of Russia (Tsar Alexander I), Austria (Emperor Francis I), and Prussia (King Frederick William III), proposed by Alexander I after Napoleon's final defeat at Waterloo) was the foundational instrument of the post-Napoleonic conservative international order — the mechanism through which the three Eastern monarchies suppressed liberal nationalism and constitutionalism in Europe from 1815 to 1848, and the first modern attempt to create a rule-based international order on explicitly conservative-religious principles. The Holy Alliance was both a cynical exercise of great-power dominance and a genuine expression of the monarchs' conviction that Christian fraternity should govern international relations.\n\n"
            "Tsar Alexander I's proposal — that the three monarchs pledge to govern their states and conduct their foreign relations according to 'the precepts of holy religion, namely the precepts of Justice, Christian Charity, and Peace' — was widely mocked by Metternich (who called it 'a high-sounding nothing') and Castlereagh ('a piece of sublime mysticism and nonsense') but was accepted as politically harmless. In practice, the Holy Alliance framework was used to justify intervention against constitutional movements in Italy (1821), Spain (1823), and the Greek War of Independence.\n\n"
            "The Congress System — the series of great-power conferences (Aix-la-Chapelle 1818, Troppau 1820, Laibach 1821, Verona 1822) that implemented the Holy Alliance's conservative agenda — was the first modern system of collective great-power management of European affairs, and the historical precursor to the Concert of Europe and ultimately the League of Nations."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Post-Napoleonic conservative international order (26 September 1815); Russia-Austria-Prussia; Tsar Alexander I proposal — Christian fraternity governing international relations; suppressed liberal nationalism 1815–1848 (Italian constitutionalism 1821, Spanish constitutionalism 1823, Greek War of Independence); Metternich called it 'a piece of sublime mysticism and nonsense' but used it cynically; Congress System (Aix-la-Chapelle, Troppau, Laibach, Verona) — first modern collective great-power management; precursor to Concert of Europe and League of Nations.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Napoleon's final defeat (Waterloo, June 1815) — and the conservative monarchies' determination to prevent the recurrence of revolutionary or Napoleonic disruption of the European order — drove the Holy Alliance's founding as a mechanism for collective great-power management of European politics",
            "Tsar Alexander I's religious mysticism — intensified by his experience of Napoleon's invasion of Russia (1812) and the burning of Moscow — produced the genuinely idealistic proposal that Christian fraternity should govern relations between monarchs, creating the religious-conservative framework that distinguished the Holy Alliance from a conventional defensive treaty",
            "Metternich's recognition that the Holy Alliance's religious rhetoric — however meaningless in itself — could be used to justify intervention against constitutionalist movements in Austria's sphere of influence, particularly in Italy and Germany, drove his pragmatic exploitation of Alexander's idealistic proposal"
        ],
        "effects": [
            "The Holy Alliance/Congress System's suppression of liberal constitutionalism — authorising Austrian intervention against the Neapolitan (1821) and Piedmontese (1821) constitutional movements, and the French intervention against the Spanish constitutionalists (1823) — preserved the absolute monarchy order in Southern Europe for a generation, delaying but not preventing the constitutional revolutions of 1848",
            "The Congress System's breakdown over Greece — where British and Russian support for Greek independence (Greek War of Independence, 1821–1829) created a conflict between the Holy Alliance's conservative principle of legitimacy (supporting the Ottoman Empire) and national/religious sympathies — demonstrated that collective great-power management had inherent limits when the interests of major powers diverged",
            "The Holy Alliance's legacy as the model for both the Concert of Europe (1815–1914) and the League of Nations (1919–1946) — attempts to manage international relations through collective great-power agreement rather than bilateral balancing — made it the foundational historical reference for all subsequent collective security discussions",
            "The 'Holy Alliance' concept — as a shorthand for conservative great-power cooperation to suppress liberal movements — became a powerful rhetorical weapon in 19th-century liberal discourse, used to mobilise public opinion against intervention and in support of national liberation movements across Europe"
        ],
        "relationships": [
            {"entity": "Tsar Alexander I (Russian founder, religious mysticism, Napoleonic trauma)", "relationship": "PROPOSED_AND_FOUNDED_BY", "note": "Alexander's religious mysticism — shaped by the Napoleonic invasion — produced the Holy Alliance's Christian fraternity framework that distinguished it from a conventional defensive treaty"},
            {"entity": "Metternich (Austrian chancellor, cynical exploitation of Holy Alliance framework)", "relationship": "INSTITUTIONALLY_EXPLOITED_TO_JUSTIFY_CONSERVATIVE_INTERVENTION_BY", "note": "Metternich used the Holy Alliance's conservative legitimacy principle to justify Austrian intervention against constitutionalist movements in Italy"},
            {"entity": "Congress System (Aix-la-Chapelle 1818, Troppau, Laibach, Verona — collective great-power management)", "relationship": "OPERATIONAL_MECHANISM_OF_THE", "note": "The Congress System — implementing the Holy Alliance's conservative agenda through great-power conferences — was the first modern system of collective management of European affairs"},
            {"entity": "Concert of Europe (1815–1914, collective great-power management precursor)", "relationship": "DIRECT_PRECURSOR_FRAMEWORK_OF_THE", "note": "The Holy Alliance/Congress System was the direct institutional precursor of the Concert of Europe that managed European affairs for a century"},
            {"entity": "Greek War of Independence (1821–1829, Holy Alliance breakdown over national liberation)", "relationship": "COHERENCE_FIRST_BROKEN_BY_CONFLICTING_GREAT-POWER_RESPONSES_TO_THE", "note": "The Greek independence war — where British and Russian sympathies conflicted with the Holy Alliance's legitimist support for the Ottoman Empire — revealed the limits of collective conservative management"}
        ],
    }),

    ("anglo-portuguese-alliance", {
        "summary": (
            "The Anglo-Portuguese Alliance (est. 1373 — the oldest active alliance in the world, originally constituted by the Treaty of London between England and Portugal, renewed by the Treaty of Windsor, 1386, and continuously maintained to the present day) is the world's longest-standing bilateral diplomatic alliance — spanning 651 years, three Portuguese dynasties, the dissolution of the Portuguese and British empires, and two world wars. The alliance has been invoked in both World Wars, and its continuing formal existence makes it the most durable bilateral agreement in the history of international relations.\n\n"
            "The Treaty of London (1373) — agreed between King Edward III of England and King Fernando I of Portugal — created a perpetual alliance of friendship, mutual aid, and solidarity, establishing the framework that would be renewed and strengthened by the Treaty of Windsor (1386, between King John I of Portugal and King Richard II of England), which extended the alliance to cover personal as well as national relationships and remains the foundational document. The Windsor treaty was sealed by the marriage of King John I to Philippa of Lancaster (daughter of John of Gaunt), creating a dynastic as well as diplomatic bond.\n\n"
            "The alliance's most consequential applications were: the Methuen Treaty (1703), which created the preferential trade arrangement that gave Portugal English manufactured goods in exchange for wine access, integrating Portugal into Britain's informal economic empire; Britain's Peninsular War alliance with Portugal (1808–1814) against Napoleon; and the WWII agreement allowing the Allies to use the Azores as a naval base (1943), which was critical for the Battle of the Atlantic."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "World's oldest active alliance (est. 1373, Treaty of London; Treaty of Windsor 1386 — 651+ years); England/Britain and Portugal; Treaty of Windsor — sealed by John I of Portugal and Philippa of Lancaster marriage; Methuen Treaty (1703, wine-manufactures trade, informal economic integration); Peninsular War alliance (1808–1814, Wellington, Lisbon base); WWII Azores agreement (1943, Atlantic convoy protection); most durable bilateral agreement in history of international relations; formally still active today.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Portugal's strategic vulnerability — as a small Atlantic state on the Iberian Peninsula threatened by Castilian ambitions for Iberian unification — drove its consistent need for an external ally to guarantee independence, with England/Britain being the most accessible and commercially compatible partner",
            "England's Atlantic commercial and later imperial interests — which made Portuguese ports (Lisbon, Porto) and the Azores critical staging points for Atlantic navigation — created the strategic complementarity that sustained the alliance across changing political circumstances",
            "The Methuen Treaty's (1703) creation of a preferential wine-manufactures trade relationship — giving Portugal privileged access to the British market for port wine in exchange for British cloth — created economic interdependence that gave both countries ongoing material interests in maintaining the alliance"
        ],
        "effects": [
            "The Peninsular War alliance (1808–1814) — in which Wellington used Lisbon as the base for his operations against Napoleon's forces in Iberia — was one of the most consequential applications of the Anglo-Portuguese Alliance, providing the strategic platform that eventually led to Napoleon's Spanish disaster and contributed to his final defeat",
            "The Azores agreement (1943) — Britain invoking the alliance to request Azores basing rights for convoy protection against German U-boats — was critical for the Battle of the Atlantic, enabling Allied aircraft to close the mid-Atlantic gap where U-boats had operated beyond air cover, decisively shifting the battle against the U-boat threat",
            "The Alliance's survival through the dissolution of both the British and Portuguese empires — through Portugal's Estado Novo dictatorship (1933–1974), the transition to democracy (Carnation Revolution, 1974), and both countries' NATO membership — demonstrates how a bilateral treaty can outlast all the political, economic, and imperial conditions that originally sustained it",
            "Portugal's admission to the European Community (1986) — facilitated partly by British support in recognition of the alliance — demonstrates how the oldest diplomatic relationship in history can still generate practical political benefits in the context of modern multilateral institutions"
        ],
        "relationships": [
            {"entity": "Treaty of Windsor (1386, John I of Portugal, Richard II of England, Philippa of Lancaster)", "relationship": "FOUNDATIONAL_TREATY_RENEWING_AND_STRENGTHENING_THE", "note": "The Treaty of Windsor — sealed by the dynastic marriage of John I and Philippa of Lancaster — is the foundational document of the world's oldest active alliance"},
            {"entity": "Methuen Treaty (1703, port wine-British cloth, economic interdependence)", "relationship": "ECONOMIC_DIMENSION_INSTITUTIONALISED_BY_THE", "note": "The Methuen Treaty's wine-manufactures trade — giving Portugal privileged British market access — created the economic interdependence that sustained the alliance"},
            {"entity": "Peninsular War (1808–1814, Wellington, Lisbon base, Napoleon's Iberian disaster)", "relationship": "STRATEGIC_PLATFORM_PROVIDED_TO_WELLINGTON'S_CAMPAIGN_BY_THE", "note": "Wellington's use of Lisbon as his Peninsular War base — enabled by the alliance — contributed directly to Napoleon's Spanish disaster"},
            {"entity": "Azores basing agreement (1943, Battle of the Atlantic, mid-Atlantic gap closure)", "relationship": "INVOKED_TO_SECURE_THE_CRITICAL_ATLANTIC_WAR_BASING_RIGHTS_OF_THE", "note": "The 1943 Azores agreement — Britain invoking the oldest alliance to close the mid-Atlantic U-boat gap — was one of the alliance's most consequential modern applications"},
            {"entity": "NATO (both UK and Portugal members, alliance context)", "relationship": "BILATERAL_RELATIONSHIP_EMBEDDED_WITHIN_THE_MULTILATERAL_FRAMEWORK_OF", "note": "Both UK and Portugal's NATO membership embeds the world's oldest bilateral alliance within a modern multilateral security framework"}
        ],
    }),

    ("grand-alliance", {
        "summary": (
            "The Grand Alliance (1689–1697 — the coalition of England, the Dutch Republic, the Holy Roman Empire, Spain, Savoy, and the League of Augsburg against Louis XIV's France, formed after William III's Glorious Revolution brought England into the continental coalition) was the pivotal military alliance that halted French hegemonic expansion in the Nine Years' War, established the principle that European great powers would collectively resist any single state's bid for continental dominance, and transferred financial and military power from France to Britain-Dutch combination in a shift whose consequences shaped the 18th century. A second Grand Alliance (1701–1714) fought the War of the Spanish Succession.\n\n"
            "The Grand Alliance emerged from the League of Augsburg (1686) — formed by the Emperor Leopold I, the Dutch Republic, Spain, Sweden, and German princes in response to Louis XIV's Reunion policy (annexing territories through legal proceedings) and his Revocation of the Edict of Nantes (1685). William III of Orange's accession to the English throne (1689 Glorious Revolution) was the critical development that brought England and its naval power into the coalition, transforming it from a continental defensive alliance into a grand strategic challenge to French hegemony.\n\n"
            "The Nine Years' War (1688–1697) ended with the Treaty of Ryswick (1697), which forced France to return most of its Reunion conquests and recognize William III as King of England — a decisive check on French expansion that established the Grand Alliance's pattern of European coalitional resistance to French hegemony, which would be refined in the War of the Spanish Succession (1701–1714) and the wars of the 18th century."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Coalition against Louis XIV's France (1689–1697); England, Dutch Republic, Holy Roman Empire, Spain, Savoy; Nine Years' War — halted French hegemonic expansion; William III of Orange (Glorious Revolution, England brought into coalition); Treaty of Ryswick (1697) — France returned Reunion conquests, recognized William III; established principle of European collective resistance to single-state hegemony; War of the Spanish Succession (Second Grand Alliance, 1701–1714); shifted financial-military power from France to Britain-Dutch combination; Marlborough's military campaigns; foundational for 18th-century balance-of-power politics.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Louis XIV's Reunion policy (1680s) — using French courts to claim sovereign rights over territories adjacent to French borders — and his Revocation of the Edict of Nantes (1685), which expelled 400,000 Protestant Huguenots and alarmed Protestant European powers, drove the formation of the League of Augsburg as a defensive coalition against French expansion",
            "William III's Glorious Revolution (1688) — his successful invasion of England and accession to the throne — was the pivotal event that brought England and its naval power into the continental coalition, transforming the League of Augsburg into the Grand Alliance and giving France's opponents the financial and naval resources needed for a sustained war",
            "The Dutch Republic's financial innovation — the creation of the Bank of Amsterdam and the Dutch funding system that enabled sustained military expenditure — combined with England's post-Glorious Revolution financial revolution (Bank of England, 1694) to give the Grand Alliance the fiscal-military capacity to sustain a decade-long war against the wealthiest state in Europe"
        ],
        "effects": [
            "The Grand Alliance's successful resistance to French hegemony in the Nine Years' War — forcing France to accept the Treaty of Ryswick and cede most of its Reunion gains — established the balance-of-power principle that no single state should be allowed to achieve hegemonic dominance in Europe, which governed European diplomacy for the next 250 years",
            "The financial innovations enabled by the Grand Alliance — particularly the Bank of England (1694), created to fund war against France — transformed England from a second-rate military power into a fiscal-military state capable of sustaining global warfare, setting the trajectory for British hegemony in the 18th and 19th centuries",
            "The military partnership between England and the Dutch Republic — creating the combined Dutch-English force under Marlborough that won the battles of Blenheim, Ramillies, Oudenarde, and Malplaquet in the War of the Spanish Succession — was the foundational military alliance of the 18th-century European order",
            "The Grand Alliance's pattern — European great powers combining against any state that threatened hegemony — became the template for subsequent European coalitions against Napoleon (1793–1815), creating the recurring diplomatic pattern that defined European power politics until the 20th century"
        ],
        "relationships": [
            {"entity": "William III of Orange (Glorious Revolution, England into Grand Alliance)", "relationship": "PIVOTAL_EXPANSION_INTO_FULL_GRAND_ALLIANCE_DRIVEN_BY_THE_ACCESSION_OF", "note": "William III's 1688 accession — bringing England and its naval power into the coalition — was the critical development that transformed the League of Augsburg into the Grand Alliance"},
            {"entity": "Louis XIV of France (French hegemonic expansion, Grand Alliance target)", "relationship": "FORMED_TO_RESIST_THE_HEGEMONIC_AMBITIONS_OF", "note": "Louis XIV's Reunion policy and religious persecution of Protestants created the coalition of European powers that checked French dominance"},
            {"entity": "Bank of England (1694, financial innovation enabling sustained Grand Alliance warfare)", "relationship": "FINANCIAL_INFRASTRUCTURE_OF_SUSTAINED_WARFARE_CREATED_TO_FUND_THE", "note": "The Bank of England — created to fund the Grand Alliance wars — transformed England into a fiscal-military state capable of sustaining global warfare"},
            {"entity": "Treaty of Ryswick (1697, Nine Years' War end, French Reunion concessions)", "relationship": "ACHIEVED_THE_STRATEGIC_OBJECTIVE_OF_FORCING_THE", "note": "Ryswick forced France to return most Reunion conquests — the Alliance's decisive check on French hegemony"},
            {"entity": "Duke of Marlborough (Grand Alliance military commander, Blenheim, Ramillies)", "relationship": "MILITARY_GENIUS_OF_THE_COMBINED_FORCES_OF_THE", "note": "Marlborough's victories at Blenheim, Ramillies, Oudenarde, and Malplaquet made the Grand Alliance's military campaign the most successful in early modern European history"}
        ],
    }),

    ("balkan-league", {
        "summary": (
            "The Balkan League (1912–1913 — the alliance of Bulgaria, Serbia, Greece, and Montenegro, formed under the auspices of Russian diplomacy to coordinate military action against the Ottoman Empire in Macedonia and Thrace) was the offensive coalition that fought the First Balkan War (October 1912–May 1913), expelling the Ottoman Empire from most of its remaining European territories in a remarkably rapid and decisive campaign. The Balkan League's military success — reducing Ottoman Europe from 169,000 km² to approximately 26,000 km² in a single war — was simultaneously the League's greatest achievement and the immediate cause of its dissolution in the Second Balkan War.\n\n"
            "The Balkan League was formed through Russian-mediated bilateral treaties — the Serbian-Bulgarian alliance (March 1912) and the Greek-Bulgarian alliance (May 1912), followed by Montenegro's association — that committed the allied states to coordinated action against the Ottoman Empire while secretly dividing anticipated territorial gains. Russia's support for the League — as a tool for weakening the Ottoman Empire and expanding Russian influence in the Balkans — was critical to the alliance's formation but also introduced conflicting interests about post-war territorial distribution.\n\n"
            "The First Balkan War's speed and decisiveness — with Bulgarian forces reaching the Chataldja defensive lines outside Constantinople before the Armistice (December 1912), and Greek forces capturing Thessaloniki — shocked both the Ottoman Empire and the European great powers, demonstrating that the 'sick man of Europe' was far weaker militarily than European diplomatic calculations had assumed, and creating the territorial ambiguities that produced the Second Balkan War."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "First Balkan War coalition (1912–1913); Bulgaria, Serbia, Greece, Montenegro; Russian-mediated formation (Serbian-Bulgarian March 1912, Greek-Bulgarian May 1912); expelledOttoman Empire from most European territories (169,000 km² → 26,000 km²); Bulgarian forces reached Chataldja lines outside Constantinople; Thessaloniki captured by Greece; League's success immediate cause of dissolution → Second Balkan War (1913); 'sick man of Europe' militarily weaker than assumed; precipitated conditions for WWI (Balkan Wars → Serbian expansionism → Austro-Hungarian alarm → Sarajevo 1914).",
            "significanceCategory": "continental"
        },
        "causes": [
            "Russia's diplomatic cultivation of a Balkan anti-Ottoman coalition — as part of its broader strategy of weakening Ottoman power and expanding Russian influence over the Straits — drove the Russian-mediated Serbian-Bulgarian and Greek-Bulgarian alliance negotiations that formed the Balkan League",
            "The Young Turk Revolution (1908) and the subsequent Ottoman political instability — combined with the Italian-Turkish War (1911–1912) that demonstrated Ottoman military weakness in Africa — created both the opportunity and the urgency for Balkan states to act before the Ottoman military could modernise under Young Turk direction",
            "The unresolved status of Macedonia and Thrace — where Bulgarian, Serbian, Greek, and Ottoman populations overlapped in contested territories — created both the territorial objective and the national grievances that motivated all four Balkan League members to prioritise war against the Ottoman Empire above their mutual rivalries"
        ],
        "effects": [
            "The First Balkan War's expulsion of the Ottoman Empire from most of its European territories — reducing Ottoman Europe by 85% — was the most rapid territorial transformation in European history since the Napoleonic Wars, fundamentally changing the demographic and political map of Southeastern Europe",
            "The Second Balkan War (June–August 1913) — caused by Bulgaria's attack on its former allies over the partition of Macedonia — expanded the territorial settlement to include Romanian and Ottoman territorial gains at Bulgaria's expense, creating a deeply resentful Bulgaria that subsequently allied with the Central Powers in WWI",
            "The Balkan Wars' territorial settlements — creating an enlarged Serbia (doubly enlarged, gaining Macedonia and part of the Sandžak) and a Greece extended into northern Greece — intensified Austro-Hungarian alarm at Serbian expansion, directly contributing to the Austro-Hungarian decision to crush Serbian ambition in 1914 after the Sarajevo assassination",
            "The Balkan League's rapid dissolution — from triumphant military alliance to fratricidal Second Balkan War in months — demonstrated that alliances formed for specific offensive purposes dissolve once the objective is achieved if the allies have conflicting interests over the division of gains, a lesson in alliance management with broad applicability"
        ],
        "relationships": [
            {"entity": "First Balkan War (October 1912–May 1913, Ottoman expulsion from Europe)", "relationship": "MILITARY_COALITION_THAT_FOUGHT_THE", "note": "The First Balkan War — expelling the Ottoman Empire from 85% of its European territories — was the Balkan League's defining military achievement and immediate cause of dissolution"},
            {"entity": "Russian diplomatic mediation (Serbian-Bulgarian, Greek-Bulgarian alliance formation)", "relationship": "FORMED_THROUGH_THE_DIPLOMATIC_AUSPICES_OF", "note": "Russia's mediation of the Serbian-Bulgarian and Greek-Bulgarian alliances was critical to the League's formation — driven by Russian strategic interest in weakening the Ottoman Empire"},
            {"entity": "Second Balkan War (1913, Bulgaria attacks former allies, Macedonia partition)", "relationship": "ALLIANCE_DISSOLVED_INTO_THE_FRATRICIDAL", "note": "Bulgaria's attack on Serbia and Greece over Macedonia's partition transformed the victorious Balkan League into the destructive Second Balkan War within months"},
            {"entity": "Austro-Hungarian alarm at Serbian expansion (→ Sarajevo 1914, WWI trigger)", "relationship": "TERRITORIAL_OUTCOMES_HEIGHTENED_THE_AUSTRO-HUNGARIAN_CONCERN_THAT_TRIGGERED_THE_CONDITIONS_FOR", "note": "The Balkan Wars' enlargement of Serbia alarmed Austria-Hungary — directly contributing to the chain of events leading to the 1914 Sarajevo assassination and WWI"},
            {"entity": "Young Turk Revolution (1908, Ottoman instability, Balkan League opportunity)", "relationship": "OPPORTUNE_MOMENT_FOR_FORMATION_CREATED_BY_THE_OTTOMAN_INSTABILITY_OF_THE", "note": "The Young Turk Revolution and subsequent Ottoman political instability — combined with the Italian-Turkish War (1911–1912) — created the opportunity the Balkan League exploited"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 44 — {len(ENTITIES)} entities (Class 394: Military Alliances)")
    for slug, data in ENTITIES:
        print(f"\n\u2192 {slug}")
        enrich_entity(slug, data)
    print("\n\u2713 Done")
