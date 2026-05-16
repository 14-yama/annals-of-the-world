#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 33 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: fundamento-de-esperanto, covenant-of-the-league-of-nations,
          apologie, capitalism-and-freedom-friedman-1962,
          daredevils-of-sassoun, bibliotheca,
          a-scandal-in-bohemia, atlas-shrugged
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-33-may2026"

ENRICHMENTS = {

"fundamento-de-esperanto": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780fundamento-de-esperanto.json",
  "slug": "fundamento-de-esperanto",
  "data": {
    "summary": "The Fundamento de Esperanto (Foundation of Esperanto) is the normative reference work of the Esperanto language, published in 1905 by the language's creator, Ludwig Lazarus Zamenhof (1859–1917), a Polish Jewish ophthalmologist from Białystok — and accepted by the First World Congress of Esperanto (Boulogne-sur-Mer, 1905) as the inviolable basis of the language. The Fundamento consists of three parts: the Antaŭparolo (preface), the Gramatiko (a 16-rule grammar that defines the morphological structure of Esperanto in its entirety), and the Ekzercaro (a set of exercises demonstrating the language in use), along with a vocabulary of approximately 900 root words in multiple languages. Zamenhof's preface declares that the Fundamento is to be considered the immutable foundation of Esperanto — no authority, including Zamenhof himself, may alter it — a declaration that established the principle of democratic linguistic governance that distinguishes Esperanto from other constructed languages.\n\nEsperanto was first published in 1887 in Zamenhof's Unua Libro ('First Book'), but the Fundamento of 1905 is the definitive normative text that fixed the language's grammar and core vocabulary. Zamenhof designed Esperanto as a politically neutral international auxiliary language that would enable communication across linguistic, national, and ethnic barriers — his Białystok childhood, in a city divided between Russians, Poles, Germans, and Jews with no common language, was the direct inspiration for the project. The 16 grammatical rules of the Fundamento — which cover all the morphological regularities of Esperanto in less than a page — are designed to be learnable in hours, in contrast to the years required for natural languages.\n\nEsperanto is the most successful constructed language in history — with estimates of 1–2 million speakers worldwide, a rich literary and cultural tradition, UNESCO recognition, and a global community of native speakers (the Denaskuloj, children raised with Esperanto as a first language). The Fundamento remains the normative basis of the language after 120 years, and Zamenhof's vision of a politically neutral international auxiliary language as the foundation of international communication has influenced all subsequent thinking about language planning and linguistic human rights.",
    "causes": [
      "Zamenhof's Białystok childhood — growing up in a city divided between Russian, Polish, German, and Yiddish speakers with no common language, experiencing the role of linguistic division in ethnic conflict and mutual incomprehension — gave him the direct inspiration for Esperanto: a politically neutral auxiliary language that would enable communication across linguistic and ethnic boundaries without displacing any existing language.",
      "The 19th-century European language planning movement — the recognition that linguistic diversity was a barrier to international communication, trade, and peace, and the various proposals for international auxiliary languages (Volapük, 1879; Esperanto, 1887; Ido, 1907) — provided the intellectual and political context for Zamenhof's project and the international community that adopted it.",
      "The First World Congress of Esperanto (Boulogne-sur-Mer, 1905) — which brought together several hundred Esperantists and adopted the Fundamento as the inviolable basis of the language — provided the community governance that transformed Esperanto from a language proposal into a living language with an institutionalised normative framework and a global community of speakers."
    ],
    "effects": [
      "The Fundamento's 16-rule grammar — learnable in hours — established Esperanto as the most widely studied constructed language in history and validated Zamenhof's claim that a regular, morphologically transparent language could be acquired far more rapidly than natural languages. This claim has influenced subsequent research in second-language acquisition and language planning.",
      "The Esperanto movement's development of a global speaker community — a culture with its own literature, music, journalism, and a network of annual congresses (the Universala Kongreso, held annually since 1905) — demonstrated that a constructed language could develop an authentic living culture, not merely a linguistic system.",
      "Zamenhof's model of democratic linguistic governance — the principle that no authority may alter the Fundamento, and that the language belongs to its speakers collectively — influenced subsequent thinking about language planning, linguistic rights, and the governance of international communication, and remains the normative framework that distinguishes Esperanto from competitor constructed languages."
    ],
    "relationships": [
      {"sourceSlug": "ludwik-zamenhof", "sourceName": "Ludwig Lazarus Zamenhof (1859–1917)", "verb": "AUTHORS", "targetSlug": "fundamento-de-esperanto", "targetName": "Fundamento de Esperanto (1905)", "context": "Zamenhof published the Fundamento in 1905 as the normative reference of Esperanto — the inviolable foundation of grammar and vocabulary adopted by the First World Congress of Esperanto at Boulogne-sur-Mer in 1905."},
      {"sourceSlug": "fundamento-de-esperanto", "sourceName": "Fundamento de Esperanto (16-rule grammar)", "verb": "FOUNDS", "targetSlug": "esperanto-language", "targetName": "Esperanto language (1 million+ speakers worldwide)", "context": "The Fundamento's 16-rule grammar and core vocabulary established the normative basis of Esperanto — the most successful constructed language in history, with 1–2 million speakers and a living culture after 120 years."},
      {"sourceSlug": "fundamento-de-esperanto", "sourceName": "Esperanto (Zamenhof, 1905)", "verb": "INSPIRES", "targetSlug": "language-planning", "targetName": "Language planning and international auxiliary language movement", "context": "Esperanto's success and Zamenhof's model of democratic linguistic governance have influenced all subsequent thinking about language planning, international auxiliary languages, and linguistic human rights."}
    ],
    "places": [
      {"name": "Białystok, Russian Empire (now Poland, Zamenhof's birthplace and inspiration)", "role": "Zamenhof's Białystok childhood — in a multilingual city divided by ethnic and linguistic barriers — was the direct inspiration for Esperanto, and the city is the acknowledged origin of the language"},
      {"name": "Boulogne-sur-Mer, France (First World Congress of Esperanto, August 1905)", "role": "The First World Congress of Esperanto (1905) adopted the Fundamento as the inviolable basis of the language — the founding moment of the international Esperanto community as a self-governing linguistic institution"}
    ],
    "subjects": ["Constructed Language", "Modern Era", "Zamenhof", "Esperanto", "Language Planning", "International Communication", "Jewish History", "Linguistics"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Fundamento de Esperanto (Zamenhof, 1905) is the normative basis of the most successful constructed language in history — with 1–2 million speakers worldwide and a living culture after 120 years. Zamenhof's vision of a politically neutral international auxiliary language and his model of democratic linguistic governance have influenced language planning and international communication. The Esperanto movement demonstrates that a constructed language can develop into a living culture.",
      "significanceCategory": "significant"
    }
  }
},

"covenant-of-the-league-of-nations": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781covenant-of-the-league-of-nations.json",
  "slug": "covenant-of-the-league-of-nations",
  "data": {
    "summary": "The Covenant of the League of Nations is the foundational charter of the League of Nations — the first permanent intergovernmental organisation for collective security and international cooperation — incorporated as Part I of the Treaty of Versailles (signed 28 June 1919) and entering into force on 10 January 1920. The Covenant consists of 26 articles establishing the institutional structure of the League (the Assembly, the Council, the Secretariat), the obligations of member states (to submit disputes to peaceful arbitration before resorting to war), the Mandate System (administering former German and Ottoman colonial territories), and the provisions for the creation of the International Labour Organisation and the Permanent Court of International Justice. Drafted primarily under the direction of President Woodrow Wilson, the Covenant embodied Wilson's Fourteen Points programme — particularly the Fourteenth Point, which called for 'a general association of nations must be formed under specific covenants for the purpose of affording mutual guarantees of political independence and territorial integrity to great and small states alike.'\n\nThe League of Nations (1920–1946) was the first attempt in history to create a permanent institutional framework for collective security — the idea that war could be prevented through binding obligations to submit disputes to peaceful resolution, collective defence against aggression, and a standing international forum for diplomatic engagement. The League achieved significant successes in arbitrating minor disputes, establishing the Mandate System (which administered former German colonies in Africa and the Pacific and former Ottoman territories in the Middle East), coordinating refugee assistance (Nansen passports), and pioneering international health, labour, and communications standards.\n\nThe Covenant's failure — most dramatically the League's inability to respond effectively to Japanese aggression in Manchuria (1931), Italian aggression in Ethiopia (1935–1936), and German remilitarisation and expansion (1936–1939) — stemmed partly from the absence of the United States (whose Senate refused to ratify the Treaty of Versailles), partly from the defection of major powers, and partly from the Covenant's structural weakness (requiring unanimous Council decisions for enforcement). The League was dissolved in 1946 and replaced by the United Nations — whose Charter incorporated many of the Covenant's institutional innovations but attempted to address its structural weaknesses.",
    "causes": [
      "Woodrow Wilson's Fourteen Points programme — particularly his Fourteenth Point calling for a 'general association of nations' — was the primary political and ideological driver of the Covenant, and Wilson's personal insistence on including the League Covenant in the Treaty of Versailles made it the centrepiece of the post-war settlement and of his vision for a new world order based on collective security and democratic self-determination.",
      "The unprecedented scale of destruction of the First World War (10 million dead, 21 million wounded, the physical and financial devastation of Europe) created the political will in 1919 for the most ambitious experiment in international institution-building in history — the recognition that the pre-war system of bilateral alliances and balance of power had failed catastrophically gave the League its political mandate.",
      "The 19th-century peace movement and international arbitration tradition — the Hague Peace Conferences of 1899 and 1907 (which established the Permanent Court of Arbitration and the laws of war), the Inter-Parliamentary Union, and the International Peace Bureau — provided the institutional precedents and the networks of internationalist activists on which the League's designers drew."
    ],
    "effects": [
      "The Covenant of the League of Nations established the institutional framework for modern international organisations — its Assembly (universal membership), Council (great power veto), Secretariat (permanent bureaucracy), and specialised agencies (ILO, PCIJ) were the templates from which the United Nations system was designed in 1945, making the Covenant the direct ancestor of the entire post-war international institutional order.",
      "The League's Mandate System — which placed former German and Ottoman colonial territories under League supervision, requiring mandatory powers to report on their administration and pursue the 'development' of the territories toward eventual self-government — was the first institutionalised attempt at international accountability for colonial administration and established the principle of international trusteeship that became the UN Trusteeship System.",
      "The League's failures — particularly the inability to stop Japanese, Italian, and German aggression in the 1930s — provided the negative lessons that shaped the UN Charter's design: the UN Security Council's mandatory enforcement powers, the veto system, and the distinction between Chapter VI (peaceful settlement) and Chapter VII (enforcement) all reflect the attempt to avoid the Covenant's structural weaknesses."
    ],
    "relationships": [
      {"sourceSlug": "woodrow-wilson", "sourceName": "Woodrow Wilson (1856–1924)", "verb": "AUTHORS", "targetSlug": "covenant-of-the-league-of-nations", "targetName": "Covenant of the League of Nations (1919)", "context": "Wilson was the primary architect of the Covenant — his Fourteenth Point called for the League, and he personally insisted on its inclusion in the Treaty of Versailles, sacrificing other American objectives to secure the League's establishment."},
      {"sourceSlug": "covenant-of-the-league-of-nations", "sourceName": "Covenant of the League of Nations", "verb": "FOUNDS", "targetSlug": "league-of-nations", "targetName": "League of Nations (1920–1946)", "context": "The Covenant is the constitutional basis of the League — establishing its institutional structure (Assembly, Council, Secretariat), its obligations (peaceful settlement, collective defence), and the Mandate System that governed former colonial territories."},
      {"sourceSlug": "covenant-of-the-league-of-nations", "sourceName": "League of Nations Covenant (institutional model)", "verb": "INSPIRES", "targetSlug": "un-charter", "targetName": "United Nations Charter (1945)", "context": "The UN Charter — drafted at the San Francisco Conference (1945) — drew directly on the Covenant's institutional innovations while attempting to address its structural weaknesses, making the Covenant the direct ancestor of the post-war international order."}
    ],
    "places": [
      {"name": "Paris (Versailles, 1919, Covenant drafting and Treaty signing)", "role": "The Covenant was drafted at the Paris Peace Conference (January–June 1919) and signed as Part I of the Treaty of Versailles at the Hall of Mirrors on 28 June 1919 — the centrepiece of the post-WWI settlement"},
      {"name": "Geneva (League of Nations headquarters, 1920–1946)", "role": "The League of Nations was headquartered in Geneva, Switzerland — the Palais des Nations (built 1929–1938) became the symbol of the first experiment in permanent international organisation and was transferred to the United Nations in 1946"}
    ],
    "subjects": ["International Law", "Modern Era", "World War I", "League of Nations", "Woodrow Wilson", "Collective Security", "International Organizations", "Treaty of Versailles"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Covenant of the League of Nations (1919) established the first permanent international organisation for collective security — the institutional template for the entire post-war international order, including the United Nations. Its Mandate System was the first institutionalised international accountability for colonial administration. Its failures shaped the UN Charter's design. The Covenant is the founding document of modern international institutional law.",
      "significanceCategory": "world-changing"
    }
  }
},

"apologie": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781apologie.json",
  "slug": "apologie",
  "data": {
    "summary": "The Apologie of William the Silent (Dutch: Apologie van Willem van Oranje; also known as the 'Justification', Dutch: Verantwoordinge) is the political tract published on 13 December 1581 by William I, Prince of Orange (1533–1584), in response to the Spanish King Philip II's ban (proscription) of July 1580 — which had offered a reward of 25,000 gold crowns for William's assassination and declared him an outlaw, traitor, and 'pest of all Christianity.' William's Apologie — published in French, Dutch, English, and German — was the most widely distributed and politically significant political manifesto of the early modern Dutch Revolt (the Eighty Years' War, 1568–1648), defending his actions, attacking Philip II's tyranny, and articulating the case for the Dutch right to resist illegitimate royal authority.\n\nThe Apologie was drafted primarily by William's secretary and political adviser Pieter de Villiers and published simultaneously with the Act of Abjuration (Plakkaat van Verlatinghe, 26 July 1581) — the formal declaration by the States-General of the United Provinces that Philip II had forfeited his right to rule by tyranny, equivalent to the social contract theory later articulated by Locke and Rousseau. The Apologie makes both a personal defence (refuting Philip's accusations of treachery, heresy, and private vice) and a political argument: that a king who violates his fundamental obligations to his subjects (protection, justice, respect for their liberties) forfeits his authority, and that resistance to tyranny is a legitimate and Christian obligation. William presents himself as the defender of Dutch liberties, Calvinist religious freedom, and constitutional government against Spanish despotism.\n\nThe Apologie is a foundational document of the early modern right of resistance tradition — alongside the Huguenot monarchomach writings (Vindiciae contra Tyrannos, 1579) and the Scottish reformers' political theology, it established the theoretical framework of contractarian political resistance that fed into the English Civil War, the Glorious Revolution, and eventually the American and French revolutionary traditions.",
    "causes": [
      "Philip II's proscription of William of Orange (July 1580) — declaring him an outlaw and offering a reward for his assassination, a declaration of the monarch's personal authority against an individual subject — forced William to defend himself publicly and to articulate a counter-theory of political legitimacy that challenged the divine right of monarchy.",
      "The Act of Abjuration (26 July 1581) — the formal declaration by the States-General of the United Provinces that Philip II had forfeited his royal authority by tyranny — was the political context in which the Apologie appeared, and the two documents together constitute the theoretical and legal framework of Dutch independence: the Apologie providing the personal and philosophical defence; the Act of Abjuration providing the formal constitutional declaration.",
      "The early modern right of resistance tradition — the Protestant political theology developed by the Calvinist monarchomachs (Beza, Hotman, the anonymous Vindiciae contra Tyrannos) in response to the St Bartholomew's Day Massacre (1572), which argued that resistance to tyrants was legitimate under natural law and Christian obligation — provided the intellectual framework from which William's Apologie drew its political arguments."
    ],
    "effects": [
      "The Apologie articulated the contractarian theory of political legitimacy — the claim that a king who violates his obligations to his subjects forfeits his authority — in the context of the Dutch Revolt, providing the theoretical framework that influenced subsequent early modern resistance theory and ultimately the Lockean theory of government that justified the Glorious Revolution and the American Revolution.",
      "The wide international distribution of the Apologie (in French, Dutch, English, and German) made it one of the most influential political pamphlets of the 16th century — it shaped European Protestant political thought in the 1580s, influenced Scottish and English resistance theory, and contributed to the broader early modern tradition of arguing for constitutional limits on royal authority.",
      "William the Silent's assassination on 10 July 1584 — just over two years after the Apologie's publication, by Balthasar Gérard, who had been motivated by Philip's proscription — transformed William into the martyred 'Father of the Fatherland' of Dutch national identity, and the Apologie retroactively became the founding political testament of Dutch independence."
    ],
    "relationships": [
      {"sourceSlug": "william-of-orange", "sourceName": "William I, Prince of Orange (1533–1584)", "verb": "AUTHORS", "targetSlug": "apologie", "targetName": "Apologie (1581)", "context": "William published the Apologie in December 1581 in response to Philip II's proscription — simultaneously a personal defence and a political manifesto for the legitimacy of the Dutch Revolt."},
      {"sourceSlug": "apologie", "sourceName": "Apologie (William of Orange, 1581)", "verb": "CONTEMPORARY_WITH", "targetSlug": "act-of-abjuration-1581", "targetName": "Act of Abjuration (Plakkaat van Verlatinghe, 26 July 1581)", "context": "The Apologie appeared alongside the Act of Abjuration — together the two documents constitute the theoretical and legal framework of Dutch independence from Spanish rule."},
      {"sourceSlug": "apologie", "sourceName": "Apologie (right of resistance, 1581)", "verb": "INFLUENCES", "targetSlug": "early-modern-resistance-theory", "targetName": "Early modern contractarian resistance theory (Locke, Glorious Revolution)", "context": "The Apologie's articulation of the contractarian theory of political legitimacy — a king who violates his obligations forfeits his authority — contributed to the early modern right of resistance tradition that fed into the English Civil War, the Glorious Revolution, and the American Revolution."}
    ],
    "places": [
      {"name": "Dutch Republic (Low Countries, 1581, publication context)", "role": "The Apologie was published at the height of the Dutch Revolt — the Eighty Years' War for independence from Spain — and was distributed across the United Provinces and internationally in four languages"},
      {"name": "Delft (William of Orange's residence and assassination site, 1584)", "role": "William was assassinated at his residence in Delft on 10 July 1584 — two and a half years after the Apologie's publication — by Balthasar Gérard, motivated by Philip's proscription, transforming William into the martyred Father of the Dutch Fatherland"}
    ],
    "subjects": ["Dutch History", "Early Modern Era", "William of Orange", "Dutch Revolt", "Political Theory", "Resistance Theory", "Early Modern Europe", "Eighty Years War"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Apologie of William of Orange (1581) is the foundational political manifesto of Dutch independence and one of the most significant early modern statements of contractarian political legitimacy — its articulation of the right to resist tyrannical rulers contributed to the tradition of resistance theory that influenced the Glorious Revolution, the American Revolution, and ultimately Lockean liberal political philosophy. Together with the Act of Abjuration, it constitutes the theoretical framework of Dutch national independence.",
      "significanceCategory": "highly-significant"
    }
  }
},

"capitalism-and-freedom-friedman-1962": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781capitalism-and-freedom-friedman-1962.json",
  "slug": "capitalism-and-freedom-friedman-1962",
  "data": {
    "summary": "Capitalism and Freedom is the work of political economy by Milton Friedman (1912–2006), professor of economics at the University of Chicago and the leading theorist of free-market liberalism, published by the University of Chicago Press in 1962 — the most accessible and widely read statement of Friedman's argument that economic freedom (free markets, free prices, minimal government intervention) is both instrumentally necessary for and conceptually inseparable from political freedom. The book argues against the Keynesian consensus of the post-war decades (government management of aggregate demand, the welfare state, progressive taxation) and in favour of a classical liberal economic framework: the competitive market as the primary mechanism of economic coordination, the floating exchange rate as the appropriate currency regime, monetarism as the appropriate framework for macroeconomic policy, the negative income tax as a superior alternative to the welfare bureaucracy, school vouchers as a market mechanism for educational reform, and the abolition of occupational licensing.\n\nCapitalism and Freedom develops the Chicago School's central claim that the market is not merely efficient but freedom-preserving: in Friedman's analysis, economic power dispersed across millions of market participants cannot become the basis of political coercion in the way that concentrated government economic power can, and the historical record shows that political freedom has never existed without a substantial degree of economic freedom. The book's most famous claim — 'there is one and only one social responsibility of business — to use its resources and engage in activities designed to increase its profits' — prefigured his 1970 New York Times Magazine essay 'The Social Responsibility of Business is to Increase Its Profits', which became the canonical statement of shareholder primacy in corporate governance.\n\nCapitalism and Freedom sold over half a million copies by 2002 and has been translated into 18 languages. Its influence on economic policy — through its arguments for floating exchange rates, monetarism, school choice, and supply-side economics — was enormous in the 1970s–1980s: Friedman's ideas were directly influential on the economic policies of the Pinochet government in Chile (through the 'Chicago Boys'), the Reagan administration, and Margaret Thatcher's government, making Capitalism and Freedom one of the most practically consequential works of economic theory in the 20th century.",
    "causes": [
      "The post-war Keynesian consensus — the dominance of Keynesian macroeconomic policy (active fiscal management of aggregate demand), the welfare state, and progressive taxation in Western economies after 1945 — provided both the intellectual target that Friedman attacked and the political context of expanding government economic intervention against which Capitalism and Freedom was a deliberate counter-manifesto.",
      "The Chicago School's intellectual tradition — the price theory of Frank Knight, the monetarism being developed by Friedman and Anna Schwartz (A Monetary History of the United States was published in 1963), and the foundational arguments of Friedrich Hayek's The Road to Serfdom (1944) about the connection between economic and political freedom — provided the intellectual framework from which Capitalism and Freedom was built.",
      "Friedman's 1956 lecture series at Wabash College — which became the basis of the book — and the broader Cold War context (the comparison between free-market capitalism and Soviet central planning as a contest between freedom and unfreedom) gave Capitalism and Freedom its ideological urgency: the argument that free markets and political freedom are inseparable was simultaneously an economic argument and a Cold War political argument."
    ],
    "effects": [
      "Capitalism and Freedom's intellectual influence on the Reagan and Thatcher economic revolutions of the 1980s was substantial — Friedman's arguments for monetarism (controlling inflation through money supply rather than interest rates), deregulation, floating exchange rates, privatisation, and supply-side taxation were the intellectual framework of the neoliberal policy agenda that reshaped Western economies after 1979.",
      "The 'Chicago Boys' — Chilean economists trained at the University of Chicago, many directly by Friedman — implemented a radical free-market reform programme in Chile after Pinochet's 1973 coup, making Chile the first real-world laboratory for the economic policy agenda of Capitalism and Freedom and establishing the template for subsequent neoliberal economic reform programmes worldwide.",
      "Friedman's argument for school vouchers — the proposal that government education funding should follow students to schools of their choice rather than funding state monopoly schools — introduced the market mechanism of consumer choice into educational policy and became the intellectual basis of the school choice movement in the United States, which has fundamentally reshaped educational policy debates since the 1980s."
    ],
    "relationships": [
      {"sourceSlug": "milton-friedman", "sourceName": "Milton Friedman (1912–2006)", "verb": "AUTHORS", "targetSlug": "capitalism-and-freedom-friedman-1962", "targetName": "Capitalism and Freedom (1962)", "context": "Friedman wrote Capitalism and Freedom as the accessible statement of his free-market liberalism — drawing on his Chicago lectures to argue that economic freedom is both instrumentally necessary for and conceptually inseparable from political freedom."},
      {"sourceSlug": "capitalism-and-freedom-friedman-1962", "sourceName": "Capitalism and Freedom (1962)", "verb": "INFLUENCES", "targetSlug": "neoliberal-economic-policy", "targetName": "Neoliberal economic policy (Reagan, Thatcher, Chile)", "context": "Friedman's arguments for monetarism, deregulation, floating exchange rates, and school choice were the intellectual framework of the neoliberal policy revolution of the 1980s — influencing Reagan, Thatcher, and the 'Chicago Boys' in Chile."},
      {"sourceSlug": "capitalism-and-freedom-friedman-1962", "sourceName": "Capitalism and Freedom", "verb": "CONTEMPORARY_WITH", "targetSlug": "road-to-serfdom-hayek", "targetName": "The Road to Serfdom (Hayek, 1944)", "context": "Capitalism and Freedom built on Hayek's The Road to Serfdom — sharing the central argument that economic and political freedom are inseparable — and together they constitute the two foundational texts of 20th-century free-market liberalism."}
    ],
    "places": [
      {"name": "Chicago, USA (University of Chicago, Friedman's academic base)", "role": "The University of Chicago was Friedman's academic home and the centre of the Chicago School of economics — the intellectual environment in which the price theory and monetarism underlying Capitalism and Freedom were developed"},
      {"name": "Chile (1973–1989, first large-scale policy application)", "role": "The 'Chicago Boys' implementation of Capitalism and Freedom's policy agenda in Pinochet's Chile made the country the first real-world laboratory for Friedman's free-market programme — the results were deeply controversial but enormously influential on subsequent neoliberal reform programmes"}
    ],
    "subjects": ["Economics", "Modern Era", "Milton Friedman", "Free Market", "Neoliberalism", "Chicago School", "Political Economy", "20th Century"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Capitalism and Freedom (Friedman, 1962) is the most practically influential work of economic theory in the 20th century — the intellectual foundation of the neoliberal economic revolution that reshaped Western economies under Reagan and Thatcher, and the framework for the 'Chicago Boys' reform programme in Chile. Its arguments for monetarism, school vouchers, and deregulation shaped economic policy worldwide. Together with Hayek's Road to Serfdom, it constitutes the foundational text of 20th-century free-market liberalism.",
      "significanceCategory": "world-changing"
    }
  }
},

"daredevils-of-sassoun": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782daredevils-of-sassoun.json",
  "slug": "daredevils-of-sassoun",
  "data": {
    "summary": "The Daredevils of Sassoun (Armenian: Սասնա Ծռեր, Sasna Tsṙer, 'The Crazies/Daredevils of Sassoun'; also known as David of Sassoun) is the Armenian national epic, composed orally over centuries and first recorded in written form in the 19th century — the central monument of Armenian oral literature and the primary embodiment of Armenian national identity, cultural resistance, and heroic virtue. The epic follows four generations of heroes from the legendary Armenian region of Sassoun (in what is now eastern Turkey): Sanasar and Bagdasar (the founders), Mher the Elder, David of Sassoun (the central hero, the most beloved figure in Armenian literary tradition), and Mher the Younger. The narrative is organised around the recurrent theme of resistance against foreign oppression — the heroes defend their people against Arab, Byzantine, and Kurdish overlordship — and around the heroic virtues of loyalty, courage, supernatural strength, and love.\n\nDavid of Sassoun (Dawit' Sasneci) is the epic's dominant hero — a giant of superhuman strength wielding the magical sword Tsor-Tsor (Lightning) and riding his magical horse Jalali — who defeats the Arab Caliph Melik in single combat and frees Sassoun from tribute. David's story has the deepest roots in Armenian folk tradition and the widest cultural resonance: his image is the most common heroic representation in Armenian visual art, and his statue stands in Yerevan's central Sasuntsi Davit Square (by sculptor Yervand Kochar, 1959), one of the most iconic monuments of modern Armenia.\n\nThe Daredevils of Sassoun was first written down from oral dictation in 1873 by the scholar Garegin Srvandztiants — whose transcription revealed the epic's full scope and inaugurated the scholarly study of Armenian oral literature. It has been performed by ashughs (Armenian folk poets and bards) across Armenian communities worldwide, and its themes of resistance against overwhelming oppression took on particular resonance after the Armenian Genocide of 1915, making the epic a symbol of Armenian survival and cultural continuity.",
    "causes": [
      "The historical experience of Armenian resistance — the centuries of Armenian resistance to Arab, Byzantine, Seljuk, Mongol, and Ottoman overlordship, particularly the semi-legendary resistance of the Sassoun region (in the Armenian highlands of Anatolia) — provided the historical substrate from which the epic's narrative themes and heroic figures crystallised over centuries of oral transmission.",
      "The Armenian oral tradition — the culture of the ashugh (folk poet and bard) who transmitted heroic narratives in performance across Armenian communities in the Near East and Caucasus — sustained the Daredevils of Sassoun as a living oral tradition for centuries before its first written transcription, accumulating regional variants and expansions as it was performed across the Armenian diaspora.",
      "The 19th-century Armenian national awakening (Zartonk) — the development of a self-conscious Armenian national and cultural identity in response to the constraints of Ottoman and Russian rule — created the intellectual and political context for the scholarly recovery and valorisation of the Daredevils of Sassoun as a national monument comparable to the Iliad or the Nibelungenlied."
    ],
    "effects": [
      "The Daredevils of Sassoun became the primary monument of Armenian national identity — David of Sassoun's heroic resistance against foreign oppression was the central image through which Armenians understood their own history of resistance and survival, especially after the Armenian Genocide of 1915 gave the epic's themes of resistance and survival an intensely contemporary resonance.",
      "The epic's 1000th anniversary celebration (1939) in Soviet Armenia — which produced a critical scholarly edition, artistic events, and the recognition of the epic as the foundation of Armenian national literature — made the Daredevils of Sassoun the cornerstone of Soviet Armenian cultural policy and the vehicle for the expression of Armenian national identity within the Soviet framework.",
      "The statue of Sasuntsi David (Yervand Kochar, 1959) in Yerevan — the most iconic public monument in Armenia — transformed the epic's hero into the embodiment of modern Armenian national identity: the heroic defender of the homeland whose image continues to represent Armenian resistance and cultural pride in the post-Soviet period."
    ],
    "relationships": [
      {"sourceSlug": "daredevils-of-sassoun", "sourceName": "Daredevils of Sassoun (Sasna Tsṙer, oral tradition)", "verb": "EMBODIES", "targetSlug": "armenian-national-identity", "targetName": "Armenian national identity and cultural resistance", "context": "The Daredevils of Sassoun is the central monument of Armenian national identity — David of Sassoun's heroic resistance against foreign oppression is the primary image through which Armenians understand their history, especially after the 1915 Genocide."},
      {"sourceSlug": "daredevils-of-sassoun", "sourceName": "Daredevils of Sassoun (first written transcription, 1873)", "verb": "TRANSCRIBED_BY", "targetSlug": "garegin-srvandztiants", "targetName": "Garegin Srvandztiants (Armenian scholar, 1873)", "context": "Srvandztiants first wrote down the Daredevils of Sassoun from oral dictation in 1873, inaugurating the scholarly study of Armenian oral literature and revealing the epic's full scope."},
      {"sourceSlug": "daredevils-of-sassoun", "sourceName": "Daredevils of Sassoun (David's statue, 1959)", "verb": "COMMEMORATED_BY", "targetSlug": "sasuntsi-david-statue", "targetName": "Sasuntsi David statue, Yerevan (Yervand Kochar, 1959)", "context": "The iconic statue of Sasuntsi David in Yerevan — the most recognisable monument of modern Armenia — is the physical embodiment of the epic's heroic tradition and the central symbol of Armenian national identity."}
    ],
    "places": [
      {"name": "Sassoun region, historical Armenia (now eastern Turkey, narrative setting)", "role": "The Sassoun region of the Armenian highlands — a semi-legendary landscape of mountains and fortresses — is the setting of the epic and the symbol of Armenian resistance to foreign rule"},
      {"name": "Armenia and Armenian diaspora (worldwide transmission)", "role": "The Daredevils of Sassoun has been performed and transmitted across the Armenian diaspora — from historic Armenia through the Caucasus, Anatolia, and the diaspora communities of the Middle East, Europe, and Americas"}
    ],
    "subjects": ["Armenian Literature", "Medieval Era", "Armenian Epic", "Oral Tradition", "National Identity", "Armenian History", "Cultural Heritage", "Heroic Poetry"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Daredevils of Sassoun is the Armenian national epic — the primary monument of Armenian cultural identity, whose themes of resistance against overwhelming foreign oppression took on profound resonance after the Armenian Genocide of 1915. David of Sassoun's heroic image is embodied in Yerevan's central monument and remains the most powerful symbol of Armenian national identity. The epic sustains a literary tradition across one of the world's oldest Christian civilisations.",
      "significanceCategory": "highly-significant"
    }
  }
},

"bibliotheca": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782bibliotheca.json",
  "slug": "bibliotheca",
  "data": {
    "summary": "The Bibliotheca (Greek: Βιβλιοθήκη, 'Library') — also known as the Myriobiblion ('Ten Thousand Books') — is the vast reading journal and literary encyclopedia compiled by Photius I, Patriarch of Constantinople (c. 810–893 CE), one of the greatest scholars of the Byzantine Empire and of the 9th-century intellectual world. The Bibliotheca consists of 280 codices (numbered reviews or summaries) of books that Photius had read, covering approximately 386 distinct works across theology, history, philosophy, rhetoric, medicine, and natural science. Each codex includes a summary of the work's content, judgements on its literary style, and (crucially) extensive quotations — making the Bibliotheca the primary source for the survival of numerous ancient Greek and Byzantine texts that are otherwise lost. Photius's scholarly range is extraordinary: his codices cover classical Greek historians (Diodorus Siculus, Ctesias of Cnidus, Theopompus), early Christian theological controversies (Nestorius's Bazaar of Heracleides), medical writers, and Byzantine chroniclers.\n\nThe Bibliotheca is one of the most important works for the preservation of ancient literature — several texts that exist only in fragments or are known almost entirely through Photius's summaries would be lost without his work: the historical writings of Ctesias of Cnidus (on Persian and Indian history), the lost novels of Iamblichus and Antonio Diogenes, the theological works of Nestorius, and numerous Byzantine chroniclers. For classical scholars and historians of Byzantine literature, the Bibliotheca is an indispensable reference and a window into the library of a 9th-century Byzantine polymath.\n\nPhotius was also a central figure in the Byzantine-Carolingian scholarly network and in the Photian Schism (863–867 CE) — the dispute between the Roman and Constantinopolitan churches over church jurisdiction in Bulgaria, papal authority, and the addition of the Filioque to the Nicene Creed, which inaugurated the formal process of divergence between Eastern and Western Christianity that culminated in the Great Schism of 1054. The Bibliotheca reflects the extraordinary breadth of learning available in 9th-century Constantinople — the city that served as the primary custodian of ancient Greek learning during the period when most of Western Europe had lost access to the classical tradition.",
    "causes": [
      "Photius's personal scholarly project — his ambition to record, summarise, and evaluate the enormous range of books he had read in a systematic reading journal — gave the Bibliotheca its specific form: a personalised encyclopedia of reading that combined summary, quotation, and critical evaluation in a format unique in ancient and medieval literature.",
      "The Byzantine intellectual tradition of encyclopedism — the 9th–10th century Byzantine 'encyclopaedic movement' (including the encyclopaedias of Constantine VII Porphyrogennetos and the Suda lexicon) that sought to preserve and organise the accumulated knowledge of antiquity — gave the Bibliotheca its cultural context: Photius was the pioneer of the systematic preservation and evaluation of ancient texts in the Byzantine tradition.",
      "The survival of ancient Greek books in Constantinople — the city's great libraries (including the Patriarchal Library and the imperial libraries) had preserved texts that were unknown or inaccessible in Western Europe — gave Photius access to an extraordinary range of ancient and late antique literature that was otherwise unavailable to scholars and that the Bibliotheca helped preserve for posterity."
    ],
    "effects": [
      "The Bibliotheca preserved extensive summaries and quotations of texts that are otherwise lost — including the historical writings of Ctesias of Cnidus (on Persian and Indian history), lost Byzantine novels, and numerous theological and historical works — making Photius's reading journal an essential source for classical and Byzantine scholarship.",
      "The Bibliotheca's critical evaluations of ancient authors' literary style — Photius's judgements on the clarity, complexity, vocabulary, and rhetorical quality of the authors he read — constitute a significant contribution to Byzantine literary criticism and provide insights into 9th-century Byzantine scholarly aesthetic values.",
      "Photius's Bibliotheca, together with the 10th-century Byzantine encyclopaedic movement under Constantine VII, preserved the classical Greek literary tradition through the most critical period of its survival — the interval between the fragility of ancient manuscript survival and the Renaissance recovery of ancient texts — making Constantinople the indispensable bridge between ancient Greek literature and the Western Renaissance."
    ],
    "relationships": [
      {"sourceSlug": "photius-i", "sourceName": "Photius I, Patriarch of Constantinople (c. 810–893 CE)", "verb": "AUTHORS", "targetSlug": "bibliotheca", "targetName": "Bibliotheca (Myriobiblion, c. 855 CE)", "context": "Photius compiled the Bibliotheca as a personal reading journal — summaries and evaluations of 280 codices covering approximately 386 works — preserving extensive quotations from texts that would otherwise be lost."},
      {"sourceSlug": "bibliotheca", "sourceName": "Bibliotheca (Photius)", "verb": "PRESERVES", "targetSlug": "ancient-greek-texts", "targetName": "Lost or fragmentary ancient Greek texts (Ctesias, Iamblichus, etc.)", "context": "The Bibliotheca preserves extensive summaries and quotations of texts otherwise lost — including Ctesias of Cnidus on Persia and India, Byzantine novels, and theological works — making it an irreplaceable source for classical and Byzantine scholarship."},
      {"sourceSlug": "bibliotheca", "sourceName": "Bibliotheca and Byzantine learning", "verb": "PART_OF", "targetSlug": "byzantine-encyclopaedic-movement", "targetName": "Byzantine encyclopaedic movement (9th–10th century)", "context": "The Bibliotheca was the pioneering work of the Byzantine encyclopaedic movement — the systematic preservation and organisation of ancient learning in Constantinople that served as the bridge between ancient Greek literature and the Western Renaissance."}
    ],
    "places": [
      {"name": "Constantinople (9th century, Photius's scholarly context)", "role": "Constantinople — the capital of the Byzantine Empire and the primary custodian of ancient Greek learning during the early medieval period — is the context for Photius's extraordinary scholarly access to an extensive library of ancient and Byzantine texts"},
      {"name": "Patriarchal Library, Constantinople (primary resource)", "role": "The Patriarchal Library of Constantinople — one of the great libraries of the ancient and medieval world — was Photius's primary scholarly resource, and its remarkable collection of ancient texts made the Bibliotheca possible"}
    ],
    "subjects": ["Byzantine Literature", "Medieval Era", "Photius", "Literary Criticism", "Byzantine Scholarship", "Ancient Greek Literature", "Encyclopaedism", "Manuscript Tradition"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Bibliotheca of Photius (c. 855 CE) is one of the most important works for the preservation of ancient literature — its extensive summaries and quotations preserve texts otherwise lost, including Ctesias of Cnidus on Persia and India. As the pioneering work of the Byzantine encyclopaedic movement, the Bibliotheca helped bridge ancient Greek literary tradition to the Western Renaissance. Photius himself was the central Byzantine scholar of the 9th century and a key figure in the Photian Schism.",
      "significanceCategory": "highly-significant"
    }
  }
},

"a-scandal-in-bohemia": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783a-scandal-in-bohemia.json",
  "slug": "a-scandal-in-bohemia",
  "data": {
    "summary": "'A Scandal in Bohemia' is the short story by Arthur Conan Doyle (1859–1930), first published in The Strand Magazine in July 1891 — the first of the 56 Sherlock Holmes short stories (following two novels: A Study in Scarlet, 1887, and The Sign of Four, 1890), and arguably the most famous Sherlock Holmes story after The Hound of the Baskervilles. It is significant in the Holmes canon primarily for introducing Irene Adler — the opera singer, adventuress, and former King of Bohemia's lover — who becomes the only person ever to outwit Sherlock Holmes, and whom Holmes thereafter refers to simply as 'the woman.' The story established Irene Adler as the most iconic female figure in detective fiction and as the model of feminine intelligence and resourcefulness that has been endlessly reinterpreted in subsequent Holmes adaptations.\n\nThe story follows Holmes and Watson as they are engaged by a Bohemian King to recover compromising photographs showing him with Irene Adler, who threatens to use them to prevent his upcoming royal marriage. Holmes deploys a series of ingenious stratagems to locate the photographs — staging a fake fire in her house to discover where she hides her valuables — only to find that Adler, having recognised Holmes in disguise, has already fled with the photographs, leaving only a note and her own photograph as a souvenir. The story's conclusion — in which Holmes has been defeated by a woman's intelligence and initiative — is the most striking reversal in the Holmes canon, and Doyle's characterisation of Adler (Holmes's tribute: 'To Sherlock Holmes she is always the woman') established her as the one adversary Holmes considered his intellectual equal.\n\n'A Scandal in Bohemia' was the story that established the Strand Magazine as the primary vehicle for the Holmes stories — its combination of Conan Doyle's prose, Sidney Paget's illustrations (including the iconic deerstalker and pipe), and the serial format created the publishing phenomenon that made Sherlock Holmes the most famous fictional character in the world. The Strand's circulation doubled with the publication of the Holmes stories, and the combination of magazine, illustration, and detective fiction defined the Victorian popular literary market.",
    "causes": [
      "The development of the illustrated popular magazine — exemplified by The Strand Magazine (founded January 1891) — created the publishing format perfectly suited to Conan Doyle's self-contained Holmes short stories: each issue contained a complete Holmes case with Sidney Paget's illustrations, creating a regular, accessible, illustrated detective fiction that was novel in Victorian popular literature.",
      "Conan Doyle's invention of the short detective story format — in contrast to the detective novel (of which he had written two), the short story allowed a single self-contained puzzle to be presented and resolved within a single magazine reading, creating a format of perfect narrative economy that the Strand Magazine made popular and that defined the golden age detective fiction tradition.",
      "The character of Irene Adler — Conan Doyle's creation of a woman who is Holmes's intellectual equal and who defeats him through her own intelligence and initiative — gave 'A Scandal in Bohemia' its distinctive place in the Holmes canon: the reversal of the expected detective story resolution (Holmes outwits everyone) created the story's lasting fascination."
    ],
    "effects": [
      "Irene Adler's establishment as 'the woman' — the only person who ever outwitted Holmes — made her the model for the resourceful, intelligent female antagonist/equal in detective fiction and popular culture, and she has been reinterpreted in virtually every Sherlock Holmes adaptation from Conan Doyle's own stage play through the BBC's Sherlock (Rachel McAdams, Lara Pulver) to countless pastiche novels.",
      "The Strand Magazine's publishing success with the Holmes short stories — circulation doubled; newsboys sold out within hours of publication — created the Victorian popular fiction market and established the template of the illustrated monthly detective story that defined popular fiction publishing for the following decades.",
      "Conan Doyle's development of the short detective story format — the self-contained case with a single puzzle, fair presentation of clues, and satisfying resolution — established the formal conventions of detective short fiction that were subsequently adopted by Edgar Wallace, Agatha Christie, Dorothy L. Sayers, and the entire golden age tradition."
    ],
    "relationships": [
      {"sourceSlug": "arthur-conan-doyle", "sourceName": "Arthur Conan Doyle (1859–1930)", "verb": "AUTHORS", "targetSlug": "a-scandal-in-bohemia", "targetName": "'A Scandal in Bohemia' (The Strand, July 1891)", "context": "Conan Doyle published 'A Scandal in Bohemia' as the first of the Holmes short stories in The Strand Magazine — establishing the publishing format, the illustrated short detective story, that made Holmes the most famous fictional character in the world."},
      {"sourceSlug": "a-scandal-in-bohemia", "sourceName": "'A Scandal in Bohemia' (Irene Adler)", "verb": "INTRODUCES", "targetSlug": "irene-adler", "targetName": "Irene Adler ('the woman', the only one to outwit Holmes)", "context": "The story introduced Irene Adler — the opera singer who outwits Holmes — making her the most iconic female figure in detective fiction and the model of feminine intelligence that has been endlessly reinterpreted in Holmes adaptations."},
      {"sourceSlug": "a-scandal-in-bohemia", "sourceName": "'A Scandal in Bohemia' (Strand Magazine, 1891)", "verb": "ESTABLISHES", "targetSlug": "strand-magazine", "targetName": "The Strand Magazine as the vehicle for Holmes short stories", "context": "The publication of 'A Scandal in Bohemia' in The Strand Magazine created the publishing phenomenon of the illustrated detective short story — the Strand's circulation doubled with the Holmes stories, establishing the template for Victorian popular fiction publishing."}
    ],
    "places": [
      {"name": "London, England (Baker Street setting, Strand Magazine publication)", "role": "The Baker Street of Sherlock Holmes — the symbolic address of detective fiction — is the domestic setting from which Holmes operates in 'A Scandal in Bohemia', and London is the context of the Strand Magazine's publication and the Victorian popular fiction market"},
      {"name": "The Strand Magazine offices, London (July 1891 publication)", "role": "The Strand Magazine — the vehicle for the Holmes short stories — was published from London's Strand district; its combination of Conan Doyle's prose, Paget's illustrations, and serial format created the most successful popular fiction publishing phenomenon of the Victorian era"}
    ],
    "subjects": ["Detective Fiction", "Victorian Era", "Sherlock Holmes", "Arthur Conan Doyle", "English Literature", "Victorian Literature", "Short Story", "Popular Fiction"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "'A Scandal in Bohemia' (Conan Doyle, 1891) is the founding story of the Sherlock Holmes short fiction canon — the first Strand Magazine Holmes story that created the Victorian popular fiction publishing phenomenon, and the story that introduced Irene Adler ('the woman'), the only person ever to outwit Holmes. Its establishment of the illustrated detective short story format shaped the golden age detective fiction tradition and made the Strand Magazine the defining Victorian popular fiction venue.",
      "significanceCategory": "highly-significant"
    }
  }
},

"atlas-shrugged": {
  "filepath": "data/appwrite-export/entities/784-Class-784/784atlas-shrugged.json",
  "slug": "atlas-shrugged",
  "data": {
    "summary": "Atlas Shrugged is the novel by Ayn Rand (born Alisa Zinovyevna Rosenbaum, 1905–1982), published in October 1957 by Random House — the most comprehensive fictional statement of Rand's philosophy of Objectivism and one of the most commercially successful and politically influential novels in American history, with over 30 million copies sold and consistent polling that places it among the most influential books read by Americans after the Bible. Set in a dystopian near-future America in which the economy is collapsing under the weight of government regulation, taxation, and the resentment of mediocrity toward productive achievement, Atlas Shrugged follows Dagny Taggart (railroad executive), Hank Rearden (steel magnate), and ultimately John Galt — the mysterious figure who is leading the 'strike of the mind', persuading the most productive people in society to withdraw from the parasitic world that exploits their achievement, retreating to a hidden valley ('Galt's Gulch') until the collectivist world collapses.\n\nAtlas Shrugged is the fullest fictional expression of Rand's Objectivist philosophy — a systematic rejection of altruism, collectivism, and religion in favour of rational self-interest, individual achievement, and laissez-faire capitalism as the only social system consistent with human nature and the requirements of a rational life. The novel's climax is John Galt's 60-page radio speech — a systematic philosophical manifesto of Objectivism that Rand considered the fullest expression of her thought — which articulates the moral case for rational egoism: the claim that the pursuit of one's own rational self-interest is the highest moral standard and that the sacrifice of the productive to the needs of the unproductive (whether by individual altruism or by government redistribution) is the primary source of social decline.\n\nAtlas Shrugged has had enormous political influence in the American conservative and libertarian tradition — it is the most cited book in surveys of the reading habits of Republican politicians, libertarian activists, and Tea Party supporters, and the phrase 'going Galt' (withdrawing productive effort from a society that over-taxes and over-regulates it) has become a standard idiom of American conservative political rhetoric. Its influence on the Libertarian Party, on Objectivist think tanks, and on figures like Alan Greenspan (a member of Rand's circle in the 1950s–60s and Federal Reserve chairman 1987–2006) has been substantial.",
    "causes": [
      "Rand's personal experience of Soviet Russia — she was born in St. Petersburg in 1905, witnessed the Bolshevik Revolution and the Stalinist period, and emigrated to the United States in 1926 — gave Atlas Shrugged its visceral rejection of collectivism and state control: the dystopian America of the novel is deliberately designed to make visible the processes that Rand saw as the inevitable outcome of any system that subordinates individual achievement to collective welfare.",
      "The New Deal and post-war American liberalism — the expansion of federal regulation, progressive taxation, labour law, and social provision under Roosevelt and Truman that Rand experienced as an attack on the productive individual and on the free market — provided the specific American political context against which Atlas Shrugged was directed: the novel is a sustained polemic against the direction of American economic policy in the 1930s–1950s.",
      "Rand's Objectivist philosophical system — developed across her essays, her earlier novel The Fountainhead (1943), and the Objectivist circles she led in New York — gave Atlas Shrugged its ambitious philosophical scope: the novel is simultaneously a work of fiction and a comprehensive philosophical argument, making it unique in the American literary tradition as the fullest fictional embodiment of a systematic philosophical programme."
    ],
    "effects": [
      "Atlas Shrugged's influence on American conservative and libertarian politics has been extraordinary — consistently cited as the most influential book read by Republican politicians, libertarian activists, and Tea Party supporters after the Bible, and the source of the political idiom 'going Galt' — making Rand's novel one of the most practically consequential works of fiction in American political history.",
      "Alan Greenspan's membership in Rand's inner circle (the 'Collective') in the 1950s–60s — and his subsequent appointment as Federal Reserve chairman — made Atlas Shrugged's philosophical framework directly relevant to 20-year US monetary and regulatory policy: Greenspan acknowledged Rand's influence on his views about financial market self-regulation, contributing to the policies that enabled the 2008 financial crisis.",
      "Atlas Shrugged's 30 million+ copies sold and its persistent influence on surveys of American reading habits demonstrate its extraordinary commercial durability — sustained not primarily by literary critics (who have generally been dismissive) but by a devoted readership that finds in the novel a comprehensive philosophical framework for understanding capitalism, government, and individual achievement."
    ],
    "relationships": [
      {"sourceSlug": "ayn-rand", "sourceName": "Ayn Rand (1905–1982)", "verb": "AUTHORS", "targetSlug": "atlas-shrugged", "targetName": "Atlas Shrugged (1957)", "context": "Rand wrote Atlas Shrugged as the fullest fictional expression of Objectivism — 12 years in composition, including John Galt's 60-page philosophical speech, which she considered the most complete statement of her philosophical system."},
      {"sourceSlug": "atlas-shrugged", "sourceName": "Atlas Shrugged (Objectivism)", "verb": "INFLUENCES", "targetSlug": "american-libertarianism", "targetName": "American libertarian and conservative politics", "context": "Atlas Shrugged is the most cited book in surveys of Republican and libertarian political reading — its influence on the Libertarian Party, Tea Party, and individual politicians (including Alan Greenspan) has made it one of the most practically consequential works of American fiction."},
      {"sourceSlug": "atlas-shrugged", "sourceName": "Atlas Shrugged (1957)", "verb": "FOLLOWS", "targetSlug": "the-fountainhead-rand", "targetName": "The Fountainhead (Rand, 1943)", "context": "Atlas Shrugged followed The Fountainhead (1943) as the culminating statement of Rand's Objectivism — while The Fountainhead established Rand's reputation and introduced her themes, Atlas Shrugged provided the comprehensive philosophical system (including John Galt's 60-page speech) that Rand considered her definitive work."}
    ],
    "places": [
      {"name": "United States (fictional near-future setting and publication context, 1957)", "role": "Atlas Shrugged is set in a dystopian near-future America in which collectivist economic policy has produced economic collapse — the American setting makes it a direct political commentary on New Deal liberalism and the direction of mid-20th century American economic policy"},
      {"name": "New York City (Rand's residence and Objectivist circle)", "role": "New York — where Rand lived and led her Objectivist circle (the 'Collective', including Alan Greenspan) from the 1950s — is the centre of the Objectivist movement that Atlas Shrugged created and sustained"}
    ],
    "subjects": ["American Literature", "Modern Era", "Ayn Rand", "Objectivism", "Libertarianism", "Political Fiction", "20th Century", "American Politics"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Atlas Shrugged (Rand, 1957) is one of the most politically influential novels in American history — with over 30 million copies sold, it is consistently cited as the most influential book read by American conservatives and libertarians after the Bible. Its influence on the Libertarian Party, Tea Party politics, and Alan Greenspan's Federal Reserve policy has been substantial. John Galt's philosophical speech remains the fullest fictional articulation of radical free-market individualism in the American literary tradition.",
      "significanceCategory": "highly-significant"
    }
  }
}

}  # end ENRICHMENTS


def get_entity(filepath, slug):
    with open(filepath) as f:
        data = json.load(f)
    for e in data.get("entities", []):
        if e.get("slug") == slug:
            return e, data
    return None, data

def apply_enrichment(filepath, slug, enrichment_data, dry_run=False):
    entity, data = get_entity(filepath, slug)
    if entity is None:
        print(f"  ERROR: slug '{slug}' not found in {filepath}")
        return False
    raw = entity.get("detailsJson", "{}")
    details = raw if isinstance(raw, dict) else json.loads(raw or "{}")
    old_len = len(details.get("summary", "") or "")
    if old_len >= 800:
        print(f"  SKIP — already enriched ({old_len}c)")
        return False
    if dry_run:
        print(f"  DRY RUN — would enrich {old_len}c → {len(enrichment_data.get('summary',''))}c")
        return True
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    for k, v in enrichment_data.items():
        details[k] = v
    edit_log = details.get("_editLog", [])
    edit_log.append({"field": "summary", "editorId": EDITOR_ID, "sessionId": SESSION_ID,
                     "timestamp": now, "oldValue": "", "newValue": enrichment_data.get("summary","")[:200] + "…"})
    details["_editLog"] = edit_log
    entity["detailsJson"] = details
    entity["_unsyncedEdits"] = True
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  ENRICHED — {old_len}c → {len(enrichment_data.get('summary',''))}c")
    return True

def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("** DRY RUN **\n")
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    enriched = skipped = errors = 0
    for slug, spec in ENRICHMENTS.items():
        fp = os.path.join(repo_root, spec["filepath"])
        print(f"\n[{slug}]")
        if not os.path.exists(fp):
            print(f"  ERROR: not found: {fp}")
            errors += 1
            continue
        ok = apply_enrichment(fp, slug, spec["data"], dry_run=dry_run)
        if ok: enriched += 1
        else: skipped += 1
    print(f"\n{'='*60}\nRESULTS: {enriched} enriched, {skipped} skipped, {errors} errors")

if __name__ == "__main__":
    main()
