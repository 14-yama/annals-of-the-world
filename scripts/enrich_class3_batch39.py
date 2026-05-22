#!/usr/bin/env python3
"""
Batch 39 — 8 entities (Class 373): Major International NGOs & Civil Society Organisations
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/373-Class-373"
FILE_PREFIX = "373"


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

    ("amnesty-international", {
        "summary": (
            "Amnesty International (est. 1961, London — founded by Peter Benenson) is the world's largest and most influential human rights organisation — the NGO that invented the concept of the 'prisoner of conscience', established human rights documentation as a professional discipline, and created the global campaign model that has freed thousands of political prisoners and shaped international human rights law for 60 years. Amnesty International has 10 million+ members in 160 countries, publishes the definitive annual State of the World's Human Rights report, and was awarded the Nobel Peace Prize (1977).\n\n"
            "Peter Benenson founded Amnesty International on 28 May 1961 — after reading a newspaper article about two Portuguese students imprisoned for toasting freedom — with a letter to The Observer titled 'The Forgotten Prisoners'. The founding innovation was the 'prisoner of conscience' concept: the idea that a person imprisoned solely for their beliefs, regardless of the political system imprisoning them, deserved international support. Benenson's original campaign asked readers to write letters to governments on behalf of individual prisoners — establishing the letter-writing campaign as Amnesty's primary advocacy tool.\n\n"
            "Amnesty's key innovations include the candlelit barbed wire logo (designed 1961), the 'Urgent Action Network' (mobilising global letter-writers within 24 hours for prisoners at immediate risk), and the systematic country-by-country human rights documentation that became the gold standard for international human rights monitoring. Amnesty's 1984 'Stop Torture' campaign was the first international campaign to document and oppose systematic torture as a government practice."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's largest and most influential human rights organisation (est. 28 May 1961, Peter Benenson); invented 'prisoner of conscience' concept; 10 million+ members, 160 countries; Nobel Peace Prize (1977); letter-writing campaign model; Urgent Action Network; annual State of the World's Human Rights report (definitive); 'Stop Torture' campaign (1984); established human rights documentation as professional discipline; candlelit barbed wire logo (1961); shaped international human rights law.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Peter Benenson's personal outrage at the imprisonment of two Portuguese students for toasting freedom under Salazar's dictatorship — and his intuition that individual human stories, widely communicated, could generate international moral pressure on governments — drove the founding of Amnesty International",
            "The post-WWII development of the Universal Declaration of Human Rights (1948) — establishing individual rights as a category of international law — created the legal and moral framework within which Amnesty could advocate, giving human rights campaigning a normative foundation that transcended political ideology",
            "The Cold War's polarisation of global human rights advocacy — in which Western governments condemned Soviet abuses while ignoring US-allied abuses, and vice versa — created the demand for a politically impartial human rights organisation that Benenson's principle of equal condemnation regardless of political system was designed to answer"
        ],
        "effects": [
            "The 'prisoner of conscience' concept — Amnesty's founding idea that any person imprisoned solely for their beliefs deserved international support — created the moral category that has been adopted into international human rights law and diplomacy, making political prisoners a recognised class requiring special international attention",
            "Amnesty's letter-writing campaign model — mobilising ordinary citizens to write to governments about individual prisoners — democratised human rights advocacy, making it accessible to people without legal training or political connections, and creating the mass civil society movement that is Amnesty's primary political asset",
            "Amnesty's annual State of the World's Human Rights report — documenting abuses in 150+ countries without political favour — established systematic human rights documentation as a credible professional discipline, creating the evidentiary standard that courts, governments, and UN bodies use in assessing human rights situations",
            "Amnesty International's Nobel Peace Prize (1977) — awarded for its 'defence of human dignity against torture, execution, and other forms of brutality' — legitimised the role of non-governmental organisations in international peace and security, establishing NGOs as recognised actors in the international system alongside governments"
        ],
        "relationships": [
            {"entity": "Peter Benenson (founder, 'The Forgotten Prisoners' 1961)", "relationship": "FOUNDED_BY", "note": "Benenson's 1961 Observer letter — 'The Forgotten Prisoners' — and his invention of the 'prisoner of conscience' concept established Amnesty's founding innovation"},
            {"entity": "Nobel Peace Prize (1977)", "relationship": "AWARDED_THE", "note": "The 1977 Nobel Peace Prize legitimised NGOs as recognised actors in international peace and security alongside governments"},
            {"entity": "Universal Declaration of Human Rights (1948, normative foundation)", "relationship": "OPERATES_WITHIN_THE_FRAMEWORK_OF_THE", "note": "The UDHR — establishing individual rights in international law — provided the moral and legal framework within which Amnesty's advocacy operates"},
            {"entity": "Prisoner of conscience (Amnesty's founding concept)", "relationship": "INVENTED_THE_INTERNATIONAL_HUMAN_RIGHTS_CONCEPT_OF_THE", "note": "The 'prisoner of conscience' concept — adopted into international human rights law and diplomacy — is Amnesty's most lasting intellectual contribution"},
            {"entity": "Amnesty's letter-writing campaign model", "relationship": "PIONEERED_THE", "note": "Amnesty's letter-writing model — mobilising ordinary citizens to pressure governments — democratised human rights advocacy and created the mass civil society movement template"}
        ],
    }),

    ("doctors-without-borders-international", {
        "summary": (
            "Médecins Sans Frontières (MSF, Doctors Without Borders, est. 1971, Paris — founded by Bernard Kouchner and a group of French doctors) is the world's leading independent medical humanitarian organisation — the NGO that established the principle that medical aid must transcend political neutrality, pioneered témoignage (bearing witness and speaking out about human rights abuses while providing medical care), and provides emergency medical care to 10 million+ patients annually in 70+ countries in conflict zones, epidemic zones, and natural disaster areas. MSF was awarded the Nobel Peace Prize (1999).\n\n"
            "MSF was founded in December 1971 — by a group of French doctors who had worked in the Red Cross mission to Biafra (1969) and been frustrated by the Red Cross's neutrality requirement that prevented them from speaking out about the Nigerian government's use of starvation as a weapon of war. Bernard Kouchner's founding principle — that doctors have an obligation not merely to treat patients but to bear witness to the human rights abuses that create medical emergencies — was a direct challenge to the Red Cross model of political neutrality as a precondition for medical access.\n\n"
            "MSF's landmark operations include the Ethiopian famine response (1984–1985), the Rwanda genocide medical response (1994), the West Africa Ebola crisis (2014–2016, when MSF was the primary responder for the first six months), and the ongoing Syria conflict medical operations. MSF's annual International Activity Report and its publication of treatment protocols — which are freely available — have established the gold standard for humanitarian medical practice."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's leading independent medical humanitarian organisation (est. December 1971, Bernard Kouchner); témoignage principle — doctors must bear witness to human rights abuses; 10 million+ patients annually, 70+ countries; Nobel Peace Prize (1999); West Africa Ebola crisis (2014–2016, primary responder for first six months); Rwanda genocide medical response (1994); Ethiopian famine response (1984–1985); Syria conflict operations; challenges Red Cross neutrality model; freely published treatment protocols — gold standard for humanitarian medicine.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The founding doctors' experience in Biafra (1969) — where they were prevented by Red Cross neutrality from speaking out about the Nigerian government's deliberate starvation of the Igbo civilian population — drove the founding of MSF as an organisation that would combine medical care with public témoignage",
            "Bernard Kouchner's philosophical conviction — that doctors have an obligation to bear witness to human rights abuses, not merely to treat patients in political silence — challenged the fundamental principle of the Red Cross model and created the MSF model as an alternative vision of medical humanitarianism",
            "The 1970s expansion of global conflict zones, political violence, and natural disasters — and the inadequacy of existing international medical response capacities — created the operational demand for an independent, rapidly deployable medical organisation that could reach conflict zones faster than governmental or UN systems"
        ],
        "effects": [
            "MSF's témoignage principle — speaking out about human rights abuses while providing medical care — has fundamentally changed the humanitarian NGO landscape, with most major humanitarian organisations now combining advocacy with service delivery in ways that the Red Cross model of strict neutrality was designed to prevent",
            "MSF's response to the West Africa Ebola crisis (2014–2016) — providing the primary medical response for the first six months while government and UN systems organised — demonstrated the unique operational value of a rapidly deployable independent medical organisation and its capacity to respond faster than any government system",
            "MSF's free publication of humanitarian medical treatment protocols — covering tropical diseases, malnutrition, conflict surgery, and epidemic response — has established the global standard for humanitarian medicine and made MSF's clinical expertise freely available to health workers in the world's most medically under-resourced environments",
            "MSF's campaigns against pharmaceutical company patent protections (Access to Essential Medicines campaign) — challenging the patenting of HIV drugs at prices that made treatment in Africa impossible — were instrumental in the 2001 Doha Declaration on TRIPS and Public Health, which established governments' right to issue compulsory licences for life-saving medicines"
        ],
        "relationships": [
            {"entity": "Bernard Kouchner (co-founder, témoignage principle)", "relationship": "FOUNDED_AND_PHILOSOPHICAL_PRINCIPLE_ESTABLISHED_BY", "note": "Kouchner's témoignage principle — doctors must bear witness to human rights abuses — was the founding innovation that distinguished MSF from the Red Cross neutrality model"},
            {"entity": "Biafra crisis (1969, founding catalyst — Red Cross neutrality)", "relationship": "FOUNDED_AS_DIRECT_RESPONSE_TO_FRUSTRATIONS_OF", "note": "The Biafra experience — where doctors were prevented from speaking out about deliberate starvation — drove the founding of MSF as an alternative to the Red Cross neutrality model"},
            {"entity": "Nobel Peace Prize (1999)", "relationship": "AWARDED_THE", "note": "MSF's 1999 Nobel Prize recognised its decades of emergency medical work in conflict zones and its campaigns for access to essential medicines"},
            {"entity": "West Africa Ebola crisis (2014–2016, MSF primary responder)", "relationship": "PRIMARY_FIRST-RESPONDER_ORGANISATION_IN_THE", "note": "MSF was the primary medical responder in the first six months of the West Africa Ebola crisis — demonstrating its unique capacity to respond faster than any government or UN system"},
            {"entity": "Doha Declaration on TRIPS and Public Health (2001)", "relationship": "ACCESS_TO_MEDICINES_CAMPAIGNS_CONTRIBUTED_TO_THE", "note": "MSF's Access to Essential Medicines campaigns — challenging HIV drug patents — were instrumental in the 2001 Doha Declaration establishing governments' right to compulsory licences for life-saving medicines"}
        ],
    }),

    ("international-olympic-committee", {
        "summary": (
            "The International Olympic Committee (IOC, est. 23 June 1894, Paris — founded by Pierre de Coubertin at the Sorbonne) is the governing body of the modern Olympic Games — the organisation that organises the world's largest peacetime international gathering (10,000+ athletes from 200+ countries every four years), manages one of the world's most recognised brands (the five-ring Olympic symbol), and exercises more cultural and political influence over international sport than any other institution. The modern Olympic Games are the primary global ritual of international peace, shared humanity, and competitive excellence.\n\n"
            "Pierre de Coubertin convened the International Athletic Congress at the Sorbonne on 23 June 1894 — and proposed reviving the ancient Greek Olympic Games as a modern international competition — motivated by his belief that sport could foster international understanding and peace, and that the competitive ethos of ancient Greece could be revived as a force for moral education. The first modern Olympic Games were held in Athens in 1896, with 241 athletes from 14 nations competing in 43 events.\n\n"
            "The Olympic Games have been the site of some of the 20th century's most politically significant sporting moments: Jesse Owens's four gold medals at the 1936 Berlin Games (confounding Nazi racial ideology); the Black Power salute by Tommie Smith and John Carlos at the 1968 Mexico City Games; the Munich Massacre (1972); the US boycott of Moscow (1980) and Soviet boycott of Los Angeles (1984). The IOC's management of these crises has established the Olympics as a uniquely powerful intersection of sport and global politics."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Governing body of modern Olympic Games (est. 23 June 1894, Pierre de Coubertin, Sorbonne); 10,000+ athletes from 200+ countries every four years; five-ring Olympic symbol — one of world's most recognised brands; first modern Olympics (Athens 1896, 241 athletes from 14 nations, 43 events); Jesse Owens (1936 Berlin, four gold medals, Nazi racial ideology); Black Power salute (1968 Mexico City); Munich Massacre (1972); US boycott Moscow (1980); world's largest peacetime international gathering; primary global ritual of international peace and competitive excellence.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Pierre de Coubertin's idealistic conviction — that international sporting competition could foster peace and understanding between nations, and that the ancient Greek competitive ideal could be revived as a force for moral education in the modern world — drove the founding of the IOC and the revival of the Olympic Games",
            "The late 19th century's nationalist tensions — and the search for peaceful alternatives to the military competition that had produced the Franco-Prussian War (1870) and threatened further conflict — gave Coubertin's Olympic idea political resonance with governments and aristocrats who formed the IOC's founding membership",
            "The development of international amateur sport in the late 19th century — with the formation of national athletics federations, cycling clubs, and football associations — created the organisational infrastructure and competitive culture that the Olympic Games could aggregate and celebrate"
        ],
        "effects": [
            "The modern Olympic Games — held continuously since 1896 (except for wartime suspensions in 1916, 1940, and 1944) — have become the world's most watched sporting event and the primary global ritual of international peace, with the Olympic opening ceremony providing the world's most significant annual display of national diversity and shared humanity",
            "Jesse Owens's four gold medals at the 1936 Berlin Games — under the eyes of Adolf Hitler and a global audience — was the most powerful single sporting rebuttal of racial ideology in history, demonstrating sport's capacity to contradict political propaganda and inspire oppressed populations worldwide",
            "The IOC's management of the Olympic brand — protecting the five-ring symbol, managing broadcast rights that generate $1.8 billion per cycle, and distributing 90%+ of revenues to national Olympic committees and sports federations — has made the Olympics the most financially significant international sporting organisation in history",
            "The Olympic 'truce' tradition — the ancient Greek ekecheiria (ceasefire during the Games) revived by the UN General Assembly in 1993 on IOC proposal — has been invoked in contemporary conflicts, demonstrating the Olympic ideal's continuing moral authority as a symbol of peace even when its practical impact is limited"
        ],
        "relationships": [
            {"entity": "Pierre de Coubertin (founder, Sorbonne 1894)", "relationship": "FOUNDED_BY", "note": "Coubertin's 1894 Sorbonne congress — proposing the revival of the ancient Olympic Games — was driven by his conviction that international sport could foster peace and understanding"},
            {"entity": "First modern Olympics (Athens 1896, 241 athletes, 14 nations)", "relationship": "ORGANISED_THE", "note": "The Athens 1896 Games — 241 athletes from 14 nations in 43 events — inaugurated the modern Olympic tradition that has continued for 130 years"},
            {"entity": "Jesse Owens (1936 Berlin, four gold medals)", "relationship": "HOSTED_THE_MOST_POWERFUL_SINGLE_SPORTING_REBUTTAL_OF_RACIAL_IDEOLOGY_IN_HISTORY_AT_THE", "note": "Owens's four gold medals at Berlin 1936 — under Hitler's gaze — demonstrated sport's capacity to contradict political propaganda"},
            {"entity": "Munich Massacre (1972, PLO attack on Israeli athletes)", "relationship": "FORCED_TO_MANAGE_THE_SECURITY_CRISIS_OF_THE", "note": "The 1972 Munich Massacre — PLO attack killing 11 Israeli athletes — forced the IOC to integrate security, politics, and sporting neutrality in ways that shaped all subsequent Olympics planning"},
            {"entity": "UN General Assembly Olympic Truce (1993)", "relationship": "PARTNERED_WITH_THE_UN_TO_REVIVE_THE", "note": "The IOC's successful proposal to revive the ancient Olympic truce — adopted by the UN General Assembly in 1993 — demonstrates the moral authority of the Olympic ideal in global peace politics"}
        ],
    }),

    ("oxfam", {
        "summary": (
            "Oxfam (Oxford Committee for Famine Relief, est. 5 October 1942, Oxford — founded during the Greek famine crisis caused by the British naval blockade of Nazi-occupied Greece) is the world's most influential anti-poverty organisation — the NGO that pioneered the emergency food relief, sustainable development, and global inequality advocacy model that has influenced development policy for 80 years. Oxfam's annual Inequality Report — which documents that the world's richest 1% own more wealth than the rest of humanity combined — is the most cited document in global inequality debates and has directly influenced the policy debates at Davos, the G7, and the UN.\n\n"
            "Oxfam was founded on 5 October 1942 in Oxford — during WWII — by a group of Quakers, social activists, and academics who were outraged that the British naval blockade of Nazi-occupied Greece was causing mass starvation of Greek civilians. The founding group petitioned the government to allow food through the blockade (a campaign that partially succeeded) and established the model of emergency food relief combined with advocacy. After WWII, Oxfam expanded into development work in Asia, Africa, and Latin America.\n\n"
            "Oxfam's innovations include the 'twin-track approach' (combining emergency relief with long-term development), Fair Trade (Oxfam co-founded the fair trade movement), and the Inequality Report (since 2014). Oxfam International — a confederation of 21 independent national organisations — is the world's third largest development INGO by budget."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's most influential anti-poverty organisation (est. 5 October 1942, Oxford, Quakers and academics); founded during Greek famine from British naval blockade of Nazi-occupied Greece; emergency food relief + advocacy model; Fair Trade co-founder; Inequality Report (since 2014) — world's richest 1% own more than rest of humanity combined; most cited document in global inequality debates; influences Davos, G7, UN; twin-track approach (emergency relief + long-term development); 21-organisation confederation; world's third largest development INGO.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Greek famine of 1941–1944 — caused by the combination of Nazi occupation and the British naval blockade that prevented food imports — created the immediate humanitarian crisis that drove Oxfam's founding, with the founders' outrage that the British government's strategic decision was causing civilian mass starvation",
            "The Quaker and social activist tradition of the founders — who combined moral outrage at injustice with practical organisational capacity and a tradition of pacifist advocacy — shaped Oxfam's distinctive combination of emergency relief, long-term development, and political advocacy",
            "The post-WWII decolonisation process — which left newly independent countries without the economic infrastructure to address endemic poverty, famine, and underdevelopment — created the field of international development in which Oxfam became a primary institutional actor"
        ],
        "effects": [
            "Oxfam's twin-track approach — combining emergency food relief (treating the symptoms of poverty) with long-term development support (addressing structural causes) — established the development NGO model that distinguishes sustainable development work from simple charity, influencing the design of development programmes worldwide",
            "The Fair Trade movement — which Oxfam co-founded — has grown to $12 billion in annual certified sales, ensuring that 1.7 million farmers and workers in 75 countries receive fair prices for their products, demonstrating that consumer behaviour can be channelled to support global economic justice",
            "Oxfam's annual Inequality Report — most recently documenting that the world's 8 richest individuals own as much wealth as the bottom 50% of humanity — has been the primary agenda-setting document for the global inequality debate, directly influencing policy discussions at Davos, the G7, and the UN General Assembly",
            "Oxfam's advocacy campaigns — including the Jubilee 2000 debt relief campaign (which resulted in $100 billion of debt cancellation for 35 developing countries), the Make Poverty History campaign, and ongoing trade justice campaigns — have been among the most successful civil society advocacy campaigns in history by measurable policy impact"
        ],
        "relationships": [
            {"entity": "Greek famine 1941–1944 (founding catalyst — British naval blockade)", "relationship": "FOUNDED_IN_RESPONSE_TO_THE", "note": "The Greek famine — caused by Nazi occupation and British naval blockade — drove Oxfam's founding and its distinctive combination of emergency relief and government advocacy"},
            {"entity": "Fair Trade movement (Oxfam co-founder)", "relationship": "CO-FOUNDED_THE", "note": "Oxfam co-founded the Fair Trade movement — now $12 billion in annual certified sales — demonstrating that consumer behaviour can support global economic justice"},
            {"entity": "Oxfam Inequality Report (since 2014, 1% vs rest)", "relationship": "PUBLISHES_THE_PRIMARY_AGENDA-SETTING_DOCUMENT_OF_THE", "note": "Oxfam's Inequality Report — documenting extreme wealth concentration — is the most cited document in global inequality debates, influencing Davos, G7, and UN policy discussions"},
            {"entity": "Jubilee 2000 debt relief campaign ($100 billion cancelled)", "relationship": "CO-LED_THE", "note": "Oxfam's co-leadership of Jubilee 2000 — resulting in $100 billion debt cancellation for 35 developing countries — is among the most successful civil society advocacy campaigns by measurable policy impact"},
            {"entity": "Twin-track approach (emergency relief + long-term development model)", "relationship": "PIONEERED_THE", "note": "Oxfam's twin-track approach established the development NGO model that combines emergency relief with structural development — influencing development programme design worldwide"}
        ],
    }),

    ("human-rights-watch", {
        "summary": (
            "Human Rights Watch (HRW, est. 1978, New York — founded as Helsinki Watch to monitor Soviet compliance with the Helsinki Accords) is the world's second largest international human rights organisation — the NGO that pioneered the 'naming and shaming' model of human rights documentation and advocacy, producing the detailed investigative reports that governments, courts, and media use to assess human rights situations in 100+ countries. HRW's reports on civilian harm in conflicts, systematic documentation of torture and arbitrary detention, and investigation of government-sponsored violence have shaped international humanitarian law and the doctrine of the Responsibility to Protect.\n\n"
            "Human Rights Watch was founded in 1978 as Helsinki Watch — specifically to monitor Soviet and Eastern Bloc compliance with the human rights provisions of the Helsinki Final Act (1975) — by the Ford Foundation, Robert Bernstein, and Jeri Laber. The founding innovation was systematic documentation: collecting testimony from victims, witnesses, and defectors, cross-referencing accounts, and producing detailed reports that could withstand government denial. Helsinki Watch merged with Americas Watch (1981), Asia Watch (1985), and Middle East Watch (1989) to form Human Rights Watch in 1988.\n\n"
            "HRW's most consequential reports include the documentation of the My Lai-style El Mozote massacre (El Salvador, 1982), which challenged US government denials and contributed to the Congressional investigations into the Reagan administration's El Salvador policy; the documentation of chemical weapons use against Kurdish civilians in Halabja (Iraq, 1988); and the ongoing documentation of Israeli settlements, Saudi Arabia's Yemen campaign, and Chinese Xinjiang detention camps."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's second largest international human rights organisation (est. 1978 as Helsinki Watch); pioneered 'naming and shaming' documentation model; systematic victim testimony collection + government denial challenge; Helsinki Final Act compliance monitoring; El Mozote massacre documentation (El Salvador 1982); chemical weapons against Kurds Halabja (Iraq 1988); Chinese Xinjiang camps; Saudi Arabia Yemen campaign; 100+ countries; shaped Responsibility to Protect doctrine; Ford Foundation, Robert Bernstein, Jeri Laber founding.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Helsinki Final Act (1975) — in which the Soviet Union and Eastern Bloc governments committed to respect human rights as part of the broader Helsinki process — created both the legal obligation and the monitoring rationale that Helsinki Watch was designed to exploit, using the USSR's own commitments as the standard against which to document violations",
            "The Ford Foundation's recognition — and Robert Bernstein's conviction — that systematic, professionally documented human rights reporting could be more politically effective than moral condemnation, by creating evidence records that governments could not simply deny, drove the founding of the 'naming and shaming' investigative model",
            "The Cold War's creation of proxy conflicts — in Central America, Southeast Asia, and Africa — in which US and Soviet-backed governments committed human rights abuses that their superpower patrons were reluctant to acknowledge, created the political demand for independent documentation that couldn't be dismissed as communist or anti-communist propaganda"
        ],
        "effects": [
            "HRW's 'naming and shaming' model — producing detailed, sourced investigative reports that governments, courts, and media can use to assess human rights situations — has been adopted by virtually every subsequent human rights organisation, establishing systematic documentation as the professional standard for human rights advocacy",
            "HRW's documentation of the El Mozote massacre (1982) — produced by Raymond Bonner and Alma Guillermoprieto and supported by HRW research — challenged the Reagan administration's denials and contributed to the Congressional investigations that constrained US El Salvador policy, demonstrating that accurate documentation could affect Cold War policy",
            "HRW's documentation of chemical weapons use against Kurdish civilians at Halabja (Iraq, 1988) — which the Reagan administration initially attempted to attribute to Iranian forces — established the evidential record that was used in Saddam Hussein's trial and in the international debate about chemical weapons use in subsequent conflicts",
            "The Responsibility to Protect (R2P) doctrine — adopted by the UN World Summit (2005) — was shaped by HRW's documentation of systematic civilian atrocities in Rwanda and Bosnia that existing international law had been unable to prevent, establishing the principle that the international community has a responsibility to intervene when a state fails to protect its population"
        ],
        "relationships": [
            {"entity": "Helsinki Final Act (1975, founding rationale)", "relationship": "FOUNDED_TO_MONITOR_COMPLIANCE_WITH_THE", "note": "The Helsinki Final Act — in which the USSR committed to human rights — created the monitoring rationale for Helsinki Watch: using the USSR's own commitments as documentation standards"},
            {"entity": "Ford Foundation and Robert Bernstein (founding institutions and leaders)", "relationship": "FOUNDED_BY", "note": "The Ford Foundation and Bernstein's 'naming and shaming' conviction drove the founding of the systematic documentation model that made HRW more politically effective than moral advocacy alone"},
            {"entity": "El Mozote massacre documentation (El Salvador 1982)", "relationship": "PRODUCED_THE_DOCUMENTATION_THAT_CHALLENGED_US_GOVERNMENT_DENIALS_OF_THE", "note": "HRW-supported documentation of El Mozote (1982) challenged Reagan administration denials and contributed to Congressional investigations that constrained US El Salvador policy"},
            {"entity": "Responsibility to Protect doctrine (R2P, UN 2005)", "relationship": "DOCUMENTATION_CONTRIBUTED_TO_THE_DEVELOPMENT_OF_THE", "note": "HRW's Rwanda and Bosnia documentation contributed to the R2P doctrine — establishing the international community's responsibility to intervene when states fail to protect their populations"},
            {"entity": "Halabja chemical attack documentation (Iraq, Kurdish civilians 1988)", "relationship": "PRODUCED_THE_PRIMARY_DOCUMENTATION_OF_THE", "note": "HRW's documentation of Halabja — establishing chemical weapons use against Kurdish civilians — was used in Saddam Hussein's trial and shaped the international debate about chemical weapons use"}
        ],
    }),

    ("action-against-hunger", {
        "summary": (
            "Action Against Hunger (Action contre la Faim / ACF, est. 1979, Paris — founded by a group of French intellectuals including Alfred Kastler, Marek Halter, and Bernard-Henri Lévy in response to the Cambodian genocide and resulting famine) is one of the world's leading emergency food security and nutrition organisations — the NGO that pioneered ready-to-use therapeutic food (RUTF) programmes for severe acute malnutrition, operates in 55+ countries with 8,000+ staff, and treats 20 million+ people annually for hunger-related conditions. ACF's specific technical contribution to global nutrition — the development and scaling of RUTF (Plumpy'Nut) protocols — has saved millions of children from death by severe acute malnutrition.\n\n"
            "Action Against Hunger was founded in 1979 by a group of French intellectuals and academics outraged at the international community's failure to respond adequately to the Cambodian genocide (1975–1979) and the resulting famine among Cambodian refugees. The founders — who included Nobel Prize winner Alfred Kastler — created ACF on the principle that fighting hunger was not merely charitable but a matter of fundamental justice, requiring both emergency response and the advocacy to address the political causes of hunger.\n\n"
            "ACF's most significant technical innovation is its development and scaling of Ready-to-Use Therapeutic Food (RUTF) programmes — particularly Plumpy'Nut, a peanut-butter-based high-energy paste that requires no cooking, no clean water, and can be administered by mothers at home — which has transformed the treatment of severe acute malnutrition from a hospital-based procedure to a community-based programme achievable at low cost in the most resource-poor settings."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Leading emergency food security and nutrition organisation (est. 1979, Paris, Alfred Kastler, Marek Halter, Bernard-Henri Lévy); founded in response to Cambodian genocide famine; pioneered ready-to-use therapeutic food (RUTF) — Plumpy'Nut; 55+ countries, 8,000+ staff, 20 million+ people annually treated; RUTF transformed severe acute malnutrition treatment from hospital-based to community-based; justice principle — fighting hunger as political act, not mere charity.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Cambodian genocide (1975–1979) and the resulting refugee famine — and the intellectual outrage of French left-wing academics at the international community's failure to respond adequately — drove the founding of ACF as an organisation committed to emergency response and political advocacy against hunger",
            "The recognition by Alfred Kastler and the founding intellectuals that hunger was not merely a natural disaster but a product of political choices — wars, poor governance, economic exploitation — gave ACF its distinctive combination of emergency relief and political advocacy",
            "The development of nutritional science in the 1970s–1980s — which established the specific metabolic requirements for recovery from severe acute malnutrition and identified the window of opportunity for treatment in children under five — created the scientific foundation for RUTF development"
        ],
        "effects": [
            "ACF's development and scaling of RUTF/Plumpy'Nut protocols — which transformed severe acute malnutrition treatment from a hospital-based to a community-based programme — has been adopted by UNICEF, WHO, and WFP as the standard treatment protocol, saving an estimated 1–2 million children annually who would previously have died from severe acute malnutrition",
            "ACF's integrated nutrition programming — combining treatment of acute malnutrition with prevention of chronic malnutrition, food security, water and sanitation, and mental health support — established the comprehensive nutrition security model that has been adopted by the global humanitarian system",
            "ACF's political advocacy on the right to food — framing hunger as a political failure requiring political accountability rather than merely a technical challenge requiring technical solutions — has contributed to the development of international food security policy and the Sustainable Development Goal 2 (Zero Hunger) framework",
            "ACF's emergency nutrition response in major crises — including South Sudan, Yemen, Sahel, and Rohingya refugee camps — has provided critical nutrition services in environments where government health systems have collapsed, demonstrating the irreplaceable role of independent humanitarian organisations in extreme food security crises"
        ],
        "relationships": [
            {"entity": "Cambodian genocide (1975–1979, founding catalyst)", "relationship": "FOUNDED_IN_RESPONSE_TO_THE_HUMANITARIAN_FAILURE_FOLLOWING_THE", "note": "The Cambodian genocide's famine and the international community's inadequate response drove ACF's founding by French intellectuals committed to both emergency response and political advocacy"},
            {"entity": "Alfred Kastler (Nobel Prize winner, co-founder)", "relationship": "CO-FOUNDED_BY_NOBEL_LAUREATE", "note": "Kastler's Nobel Prize stature gave ACF initial credibility and reflected the intellectual seriousness of its founding — framing hunger as a matter of justice, not mere charity"},
            {"entity": "Ready-to-Use Therapeutic Food (RUTF / Plumpy'Nut)", "relationship": "PIONEERED_THE_DEVELOPMENT_AND_SCALING_OF", "note": "ACF's RUTF development — transforming malnutrition treatment from hospital-based to community-based — has been adopted as the global standard, saving millions of children annually"},
            {"entity": "UNICEF, WHO, WFP (adopted ACF RUTF protocols)", "relationship": "ACF_PROTOCOLS_ADOPTED_AS_GLOBAL_STANDARDS_BY", "note": "UNICEF, WHO, and WFP adopted ACF's RUTF treatment protocols as the global standard for severe acute malnutrition — demonstrating ACF's technical leadership in global nutrition"},
            {"entity": "Sustainable Development Goal 2 (Zero Hunger)", "relationship": "CONTRIBUTED_TO_THE_POLITICAL_FRAMING_AND_ADVOCACY_FOUNDATION_OF", "note": "ACF's political framing of hunger as a justice issue — requiring political accountability — contributed to the advocacy foundation for SDG 2 Zero Hunger"}
        ],
    }),

    ("alcoholics-anonymous", {
        "summary": (
            "Alcoholics Anonymous (AA, est. 10 June 1935, Akron, Ohio — founded by Bill Wilson and Dr. Bob Smith at their first meeting in Bob's home) is the world's most influential peer mutual aid organisation — the institution that invented the 12-step recovery model that has been adapted for treatment of addiction, eating disorders, gambling, sex addiction, and dozens of other compulsive behaviours, and that currently has 2 million+ members in 180 countries meeting in 120,000+ groups. AA's foundational insight — that recovery from addiction requires community, not willpower alone — transformed the understanding and treatment of alcoholism from a moral failure to a medical and spiritual condition amenable to peer support.\n\n"
            "Alcoholics Anonymous was founded on 10 June 1935 — the date Bill Wilson (a Wall Street stockbroker) had his last drink — after Wilson met Robert Smith (an Akron surgeon) through the Oxford Group, a non-denominational Christian fellowship. Their first meeting established the foundational AA principle: alcoholics could recover by sharing their experiences with each other. Wilson and Smith published 'Alcoholics Anonymous' (the 'Big Book') in 1939, which articulated the 12 Steps and the 12 Traditions that became AA's governing principles.\n\n"
            "AA's 12-step model has been adapted into Narcotics Anonymous (NA), Al-Anon, Overeaters Anonymous, Gamblers Anonymous, and 200+ other fellowships, making AA the foundational institution of the global peer mutual aid movement. The 12 Steps' combination of personal accountability, spiritual surrender, and community support has influenced psychiatric treatment, addiction medicine, and the philosophy of recovery worldwide."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's most influential peer mutual aid organisation (est. 10 June 1935, Akron, Ohio); founded by Bill Wilson and Dr. Bob Smith; invented 12-step recovery model; 2 million+ members, 180 countries, 120,000+ groups; 'Alcoholics Anonymous' Big Book (1939, 12 Steps and 12 Traditions); transformed alcoholism from moral failure to medical and spiritual condition amenable to peer support; adapted into Narcotics Anonymous, Al-Anon, Gamblers Anonymous, 200+ fellowships; influenced psychiatric treatment and addiction medicine worldwide.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Bill Wilson's personal experience of alcoholism — and his sudden spiritual experience during hospitalisation (1934) that ended his drinking — combined with his Wall Street background's pragmatic problem-solving orientation to create the AA model's unique combination of spiritual surrender and practical programme of action",
            "The failure of 1930s medical and psychiatric treatment for alcoholism — which had no effective pharmaceutical treatment, and which framed alcoholism primarily as a moral failing requiring willpower — created the opening for the peer-based mutual aid model that AA pioneered",
            "The Oxford Group's Christian fellowship model — which Wilson and Smith initially worked within — provided both the community structure (small-group meetings, personal testimony, accountability) and the spiritual framework (surrender to a higher power) that became the foundation of AA's 12-step approach"
        ],
        "effects": [
            "AA's 12-step model has been adapted into 200+ fellowships — Narcotics Anonymous, Al-Anon, Overeaters Anonymous, Gamblers Anonymous, Sex Addicts Anonymous, and many others — creating the global peer mutual aid movement that is estimated to help more people with addictive and compulsive behaviours than any other treatment modality",
            "AA's re-framing of alcoholism as a disease rather than a moral failing — which was embedded in the Big Book's insistence that alcoholics could not recover through willpower alone, but required a spiritual and community programme — contributed to the medical and psychiatric recognition of alcoholism as a disease (American Medical Association, 1956) that fundamentally changed treatment approaches",
            "AA's anonymity principle — which prevents members from associating AA's name with public figures or endorsing anything outside AA — was a governance innovation that protected AA from the organisational and political pressures that destroy most large membership organisations, creating the 'leaderless' peer fellowship model that many subsequent organisations have attempted to replicate",
            "The Bill Wilson and Bob Smith friendship — which established AA's foundational principle that alcoholics recover through sharing with other alcoholics — demonstrated that peer support could achieve what professional treatment had failed to accomplish, establishing the evidence base for peer recovery support services that are now integrated into addiction treatment systems worldwide"
        ],
        "relationships": [
            {"entity": "Bill Wilson and Dr. Bob Smith (co-founders, 10 June 1935)", "relationship": "FOUNDED_BY", "note": "Wilson and Smith's first meeting (10 June 1935) established the foundational AA principle: alcoholics recover through sharing experiences with each other — the peer mutual aid model"},
            {"entity": "'Alcoholics Anonymous' Big Book (1939, 12 Steps and 12 Traditions)", "relationship": "FOUNDATIONAL_TEXT_AND_PROGRAMME_ARTICULATED_IN_THE", "note": "The Big Book (1939) — articulating the 12 Steps and 12 Traditions — gave AA its governing principles and became one of the most widely distributed books in history"},
            {"entity": "Narcotics Anonymous, Al-Anon, Gamblers Anonymous (200+ adapted fellowships)", "relationship": "FOUNDATIONAL_MODEL_FOR_THE", "note": "AA's 12-step model has been adapted into 200+ fellowships helping people with addiction, eating disorders, gambling, and compulsive behaviours — creating the global peer mutual aid movement"},
            {"entity": "American Medical Association alcoholism-as-disease recognition (1956)", "relationship": "EVIDENCE_BASE_AND_ADVOCACY_FOUNDATION_FOR_THE", "note": "AA's re-framing of alcoholism as a condition requiring peer support rather than willpower contributed to the AMA's 1956 recognition of alcoholism as a disease — transforming medical treatment approaches"},
            {"entity": "Oxford Group (Christian fellowship, founding influence)", "relationship": "SPIRITUAL_AND_COMMUNITY_STRUCTURE_MODEL_DERIVED_FROM_THE", "note": "The Oxford Group's small-group meeting model, personal testimony, and surrender framework provided the structural and spiritual foundation that AA adapted into the 12-step programme"}
        ],
    }),

    ("alexander-von-humboldt-foundation", {
        "summary": (
            "The Alexander von Humboldt Foundation (AvH, est. 1953, Bonn — refounded by the Federal Republic of Germany, originally est. 1860) is Germany's most prestigious scientific exchange organisation — the institution that funds 700+ international research fellowships per year at German universities, has supported 30,000+ researchers from 140 countries over its 70-year history, and whose alumni network includes 55 Nobel Prize winners. The Foundation's explicit mission — to rebuild Germany's scientific reputation after the devastation of National Socialism and WWII, and to restore Germany to the international scientific community through personal research exchange — made it one of the most consequential instruments of West German foreign cultural policy.\n\n"
            "Named after Alexander von Humboldt (1769–1859) — the Prussian naturalist and explorer whose concept of scientific universalism (the idea that all natural phenomena are interconnected and that science is a common human enterprise transcending national boundaries) embodied the values the Foundation sought to represent — the AvH refounded in 1953 was explicitly designed to counter the image of Germany as a nation of scientists who had participated in Nazi crimes.\n\n"
            "The Humboldt Foundation's alumna network — which includes physicists, chemists, biologists, social scientists, and humanities scholars — has maintained Germany's position as one of the world's leading research destinations, with German universities receiving approximately 5% of all international research fellows worldwide. The Foundation's Humboldt Prize (awarded to distinguished foreign researchers) and the Sofja Kovalevskaja Award (for exceptional young international researchers) are among the most prestigious international science awards."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Germany's most prestigious scientific exchange organisation (est. 1953, Bonn, Federal Republic of Germany); 700+ fellowships/year, 30,000+ researchers from 140 countries; 55 Nobel Prize winners in alumni network; named after Alexander von Humboldt (1769–1859, scientific universalism); refounded 1953 to rebuild Germany's post-Nazi scientific reputation; primary instrument of West German foreign cultural policy; Humboldt Prize, Sofja Kovalevskaja Award; 5% of all international research fellows worldwide at German universities.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The devastation of German science under National Socialism — the expulsion and murder of Jewish scientists, the ideological distortion of research, and Germany's post-WWII international isolation — created the urgent political need to restore Germany's scientific reputation and relationships with the international research community",
            "The Federal Republic of Germany's strategic commitment — backed by permanent government funding — to using scientific exchange as a primary instrument of foreign cultural policy, on the theory that personal research relationships would rebuild trust more effectively than political diplomacy",
            "Alexander von Humboldt's intellectual legacy — his concept that science is a common human enterprise transcending national boundaries, and his personal scientific journeys across Europe and the Americas that embodied international research collaboration — provided the ideal symbolic foundation for an organisation dedicated to international scientific exchange"
        ],
        "effects": [
            "The Humboldt Foundation's 30,000+ fellowships have maintained Germany's position as a leading research destination, attracting top international researchers to German universities and building the alumni networks that generate collaborative research partnerships lasting for decades after the original fellowship",
            "The 55 Nobel Prize winners in the AvH alumni network — who typically maintain strong connections to German science after their Humboldt fellowship — reflect the Foundation's success in attracting the researchers who go on to make the most consequential contributions to their fields",
            "The AvH's contribution to West Germany's rehabilitation as an international scientific partner — by demonstrating that the Federal Republic was committed to international scientific collaboration, anti-nationalist scientific ethics, and investment in the human capital of global science — was a significant element of West Germany's post-war foreign policy success",
            "The Humboldt Foundation's model — government-funded international research fellowships as a foreign policy instrument — has been adopted by many countries, from the US Fulbright Program to the UK Newton Fund, establishing international research exchange as a recognised instrument of scientific diplomacy"
        ],
        "relationships": [
            {"entity": "Alexander von Humboldt (1769–1859, scientific universalism, namesake)", "relationship": "NAMED_AFTER_AND_EMBODIES_THE_SCIENTIFIC_VALUES_OF", "note": "Humboldt's scientific universalism — science as a common human enterprise transcending national boundaries — provided the ideal symbolic foundation for Germany's post-WWII scientific exchange organisation"},
            {"entity": "Federal Republic of Germany (funder and strategic principal)", "relationship": "PERMANENTLY_FUNDED_BY_AND_FOREIGN_CULTURAL_POLICY_INSTRUMENT_OF_THE", "note": "The FRG's commitment to government-funded scientific exchange as a primary foreign cultural policy instrument drove the AvH's mission of rebuilding Germany's post-Nazi scientific reputation"},
            {"entity": "55 Nobel Prize winners (AvH alumni network)", "relationship": "ALUMNI_NETWORK_INCLUDES", "note": "55 Nobel Prize winners in the AvH network reflect the Foundation's success in attracting the researchers who make the most consequential scientific contributions"},
            {"entity": "Fulbright Program, Newton Fund (Humboldt model adoptees)", "relationship": "FOUNDATIONAL_MODEL_FOR_THE", "note": "The Humboldt Foundation's government-funded international fellowship model has been adopted by the US Fulbright Program and UK Newton Fund — establishing scientific diplomacy as a recognised foreign policy instrument"},
            {"entity": "Humboldt Prize, Sofja Kovalevskaja Award", "relationship": "AWARDS_TWO_OF_THE_MOST_PRESTIGIOUS_INTERNATIONAL_SCIENCE_PRIZES_THROUGH_THE", "note": "The Humboldt Prize (distinguished foreign researchers) and Sofja Kovalevskaja Award (exceptional young international researchers) are among the most prestigious international science prizes"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 39 — {len(ENTITIES)} entities (Class 373: Major International NGOs)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
