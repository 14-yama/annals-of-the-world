#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 10 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: bachelors-degree, venezuela, sweden, gil-eanes, pacian,
          pietro-pileo-di-prata, fulk-of-reims, vitello
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-10-may2026"

ENRICHMENTS = {

"bachelors-degree": {
  "filepath": "data/appwrite-export/entities/576-Class-576/576bachelors-degree.json",
  "slug": "bachelors-degree",
  "data": {
    "summary": "The Bachelor's Degree is the foundational first degree of the Western university system — a qualification that emerged in the medieval European universities of the 12th–13th centuries and has become the world's most widely recognised academic credential. The term derives from the Latin 'baccalaureus' (the etymology is disputed — possibly from 'bacca lauri', laurel berry, as a symbol of learning; or from 'baccalarius', a young knight or farm apprentice; or from later folk-etymological conflation). The degree system emerged at the Universities of Bologna, Paris, and Oxford in the 12th–13th centuries as a formal credential distinguishing students who had completed the introductory curriculum of the liberal arts (the trivium: grammar, rhetoric, logic; and quadrivium: arithmetic, geometry, music, astronomy) from those who had progressed to the higher faculties (theology, law, medicine).\n\nIn the medieval system, the bachelor's degree was not a terminal qualification but a stage in a cursus studiorum leading to the master's or doctor's degree. A bachelor was licensed to teach under supervision — similar to the position of a journeyman in the craft guilds — before proceeding to full mastership. The degree structure reflected the guild-craft model that medieval universities consciously adopted: master (magister), journeyman (baccalaureus), and apprentice. The disputations, lectures, and examinations that constituted the bachelor's degree programme were designed to train students in formal argumentation — the scholastic method that was the intellectual technology of medieval university education.\n\nThe bachelor's degree underwent fundamental transformation in the 19th–20th centuries: from a minority qualification of the learned elite to a mass-market credential that by the early 21st century is held by over a quarter of the adult population in developed countries. This transformation — driven by industrial-era credentialism, the expansion of the state sector, and the 'degree inflation' of post-WWII economic expansion — has made the bachelor's degree simultaneously the global standard of educational attainment and the subject of persistent debates about its value, cost, and accessibility.",
    "causes": [
      "The foundation of the medieval universities (Bologna c. 1088, Paris c. 1150, Oxford c. 1167) and their adoption of the guild-craft model of organisation — in which progression from apprentice to journeyman to master required formal assessment — created the institutional framework within which the bachelor's degree emerged as a recognised stage of learning.",
      "The medieval church's need for trained administrators, lawyers, and theologians — and the resulting demand for a standardised certification of educational attainment — drove the formalisation of degree requirements that made the bachelor's qualification a transferable credential across different universities and employers.",
      "The 19th–20th century expansion of state bureaucracies, professional licensing systems, and industrial economies requiring technically trained workforces transformed the bachelor's degree from an elite scholarly qualification into a mass credential — the 'credentialism revolution' that redefined educational attainment as a prerequisite for professional employment."
    ],
    "effects": [
      "The bachelor's degree became the foundational credential of the Western professional class — a qualification whose recognition spread globally through colonialism and educational transfer, making it the de facto international standard for tertiary education by the 20th century.",
      "The medieval liberal arts curriculum embedded in the bachelor's degree — the trivium and quadrivium — shaped the content of Western education for centuries, with its emphasis on logic, rhetoric, and mathematical reasoning surviving in modified forms in modern general education requirements.",
      "The 20th–21st century mass expansion of bachelor's degree programmes has generated persistent debates about credential inflation, student debt, and the relationship between formal education and economic value — debates that reflect the tension between the degree's medieval origins as an elite scholarly qualification and its current role as a near-universal entry credential for professional employment."
    ],
    "relationships": [
      {"sourceSlug": "bachelors-degree", "sourceName": "Bachelor's Degree", "verb": "EMERGES_FROM", "targetSlug": "university-of-paris", "targetName": "University of Paris", "context": "The University of Paris was one of the founding institutions of the medieval degree system — the bachelor's qualification emerged from the formal curriculum and examination structures of the great 12th-13th century universities."},
      {"sourceSlug": "bachelors-degree", "sourceName": "Bachelor's Degree", "verb": "REFLECTS", "targetSlug": "scholasticism", "targetName": "Scholasticism", "context": "The bachelor's degree curriculum — centred on the liberal arts, formal disputation, and logical argumentation — embodied the scholastic method that was the intellectual technology of medieval university education."},
      {"sourceSlug": "bachelors-degree", "sourceName": "Bachelor's Degree", "verb": "SHAPES", "targetSlug": "modern-higher-education", "targetName": "Modern Higher Education", "context": "The bachelor's degree became the structural foundation of modern university education — its three/four-year structure, liberal arts core, and graduation requirements are the global template for tertiary education."}
    ],
    "places": [
      {"name": "Bologna, Italy", "role": "Home of the University of Bologna (c. 1088) — the first Western university and one of the founding institutions of the degree system"},
      {"name": "Paris, France", "role": "Home of the University of Paris (c. 1150) — whose arts faculty was the model for the liberal arts bachelor's curriculum adopted across medieval European universities"},
      {"name": "Oxford, England", "role": "Home of the University of Oxford (c. 1167) — which developed the bachelor's degree system that became the model for English-language universities worldwide"}
    ],
    "subjects": ["Higher Education", "Medieval History", "Academic Credentials", "Classical Era", "University History", "Medieval Era", "Education", "Intellectual History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The bachelor's degree is one of the most consequential institutional innovations of the medieval university system — a qualification that emerged from the 12th-century liberal arts curriculum and has become the world's most widely recognised academic credential. Its evolution from elite medieval qualification to mass-market 21st-century credential reflects the transformation of education from a social distinction to an economic prerequisite.",
      "significanceCategory": "world-changing"
    }
  }
},

"venezuela": {
  "filepath": "data/appwrite-export/entities/430-Class-430/430venezuela.json",
  "slug": "venezuela",
  "data": {
    "summary": "Venezuela (Bolivarian Republic of Venezuela) is a South American nation occupying the northern coast of the continent on the Caribbean Sea, bordered by Colombia to the west, Brazil to the south, and Guyana to the east. With an area of 916,445 km² and a population of approximately 32 million, Venezuela possesses some of the world's largest proven oil reserves (the largest by conventional crude estimates as of the early 21st century, largely in the Orinoco Belt) and a landscape of extraordinary natural diversity: the Andes in the west, the llanos (vast tropical grasslands) of the interior, the Amazon rainforest in the south, the Guiana Highlands (home to the world's highest waterfall, Angel Falls/Salto Ángel), and 2,800 km of Caribbean coastline.\n\nVenezuela was colonised by Spain from the early 16th century, with the first permanent European settlement at Coro (1527). The indigenous population — comprising diverse peoples including the Carib, Arawak, and various Andean and Amazonian groups — was devastated by disease, enslavement, and displacement. Venezuela was among the first South American territories to declare independence from Spain: Francisco de Miranda's 1811 declaration and Simón Bolívar's subsequent military campaigns led to formal independence in 1821. Bolívar himself was born in Caracas (1783), making Venezuela the birthplace of the 'Liberator' whose military campaigns freed most of northern South America.\n\nVenezuela's modern history has been dominated by oil — discovered in commercial quantities at Lake Maracaibo in 1914 and rapidly transforming the country's economy and politics. The 'sowing the oil' (sembrar el petróleo) dream — using oil revenues to diversify and develop the economy — was never fully realised, and Venezuela's political history has oscillated between democratic and authoritarian governments. The Bolivarian Revolution of Hugo Chávez (1999–2013) and its continuation under Nicolás Maduro produced a severe economic and humanitarian crisis in the 2010s–2020s, with the world's largest recorded hyperinflation and a massive emigration of over 7 million Venezuelans.",
    "causes": [
      "Spanish colonisation of the Caribbean and South American coast from the 1490s–1530s brought Venezuela within the colonial system, establishing the hacienda economy and African slave trade that shaped the country's social structure — the colonial legacy of racial stratification and economic dependence that persists in Venezuelan society.",
      "Venezuela's extraordinary oil endowment — concentrated in the Lake Maracaibo basin and the Orinoco Heavy Oil Belt — created a rentier economy in the 20th century in which oil revenues generated both enormous wealth and deep structural dependency, making Venezuela vulnerable to commodity price cycles and resistant to economic diversification.",
      "The Bolivarian political tradition — the cult of Simón Bolívar as national hero and the recurring appeal to 'Bolivarian' ideology by Venezuelan political movements, culminating in Hugo Chávez's Bolivarian Revolution — shaped Venezuelan political culture in ways that both mobilised popular nationalism and justified authoritarian concentration of power."
    ],
    "effects": [
      "Venezuela's oil wealth made it one of the richest countries in Latin America through much of the 20th century, funding urbanisation, education, and infrastructure — but also creating the 'resource curse' dynamics of institutional weakness, corruption, and economic volatility that contributed to the crises of the 21st century.",
      "The Bolivarian Revolution of Chávez and Maduro became a significant reference point in 21st-century Latin American politics — alternately celebrated as a model of social investment and anti-imperialism, and condemned as a model of authoritarian populism — influencing political movements across the region.",
      "The Venezuelan migration crisis of the 2010s–2020s — producing over 7 million emigrants, the largest displacement in Latin American history — had significant political and demographic effects across Colombia, Peru, Ecuador, Chile, and Brazil, reshaping migration politics in the entire region."
    ],
    "relationships": [
      {"sourceSlug": "venezuela", "sourceName": "Venezuela", "verb": "BIRTHPLACE_OF", "targetSlug": "simón-bolívar", "targetName": "Simón Bolívar", "context": "Caracas, Venezuela, was the birthplace of Simón Bolívar (1783) — the Liberator whose military campaigns freed Venezuela, Colombia, Ecuador, Peru, and Bolivia from Spanish rule."},
      {"sourceSlug": "venezuela", "sourceName": "Venezuela", "verb": "PRODUCES", "targetSlug": "bolivarian-revolution", "targetName": "Bolivarian Revolution", "context": "Venezuela was the site of Hugo Chávez's Bolivarian Revolution (1999) — the leftist political movement that dominated Venezuelan politics and became a major reference point in 21st-century Latin American politics."},
      {"sourceSlug": "spanish-colonialism", "sourceName": "Spanish Colonialism", "verb": "SHAPES", "targetSlug": "venezuela", "targetName": "Venezuela", "context": "Spanish colonisation from the 1520s established the colonial social structure, language, and Catholic religion that shaped Venezuelan society — the colonial legacy that independence (1821) transformed but did not erase."}
    ],
    "places": [
      {"name": "Caracas, Venezuela", "role": "Venezuela's capital and largest city — the birthplace of Simón Bolívar and the centre of Venezuelan political and economic life"},
      {"name": "Lake Maracaibo, Venezuela", "role": "The site of Venezuela's first major oil discoveries (1914) — the geological formation that made Venezuela one of the world's leading petroleum exporters"},
      {"name": "Orinoco River Basin, Venezuela", "role": "The heartland of the Venezuelan llanos and the location of the Orinoco Heavy Oil Belt — the world's largest heavy oil deposit"}
    ],
    "subjects": ["South America", "Venezuelan History", "Modern Era", "Latin America", "Oil Politics", "Contemporary Era", "Independence Movements", "Political History"],
    "frameworks": ["WORLD_SYSTEMS", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Venezuela is the birthplace of Simón Bolívar, the liberator of South America, and holds the world's largest proven oil reserves — a natural endowment that has both defined and cursed its modern history. The Bolivarian Revolution of Hugo Chávez (1999) became a defining reference in 21st-century Latin American politics, and Venezuela's subsequent economic collapse and mass emigration (7+ million people) have had transformative effects across the continent.",
      "significanceCategory": "world-changing"
    }
  }
},

"sweden": {
  "filepath": "data/appwrite-export/entities/430-Class-430/430sweden.json",
  "slug": "sweden",
  "data": {
    "summary": "Sweden (Kingdom of Sweden) is a Scandinavian nation in northern Europe occupying the eastern part of the Scandinavian Peninsula, bordered by Norway to the west, Finland to the northeast, and separated from Denmark by the Øresund strait. With an area of 450,295 km² — making it the largest Nordic country and the fifth largest in Europe — and a population of approximately 10.5 million, Sweden is one of the world's most developed and egalitarian societies, consistently ranking among the top nations in human development, press freedom, gender equality, and quality of life indicators.\n\nSweden's history spans from Viking-era Scandinavian kingship (9th–11th centuries) through medieval statehood, the Swedish Empire's brief 17th-century status as a major European power, and the long peace since 1814 that has shaped the modern Swedish model. Swedish Vikings (Varangians) were among the founders of the medieval Rus' state and established trading networks from the Baltic to Byzantium and the Caspian Sea. The medieval Swedish kingdom, nominally unified by the 12th century, experienced the Nordic competition of the Kalmar Union (1397–1523) before Gustav Vasa's rebellion established an independent Swedish monarchy. The Age of Greatness (Stormaktstiden, 1611–1718) saw Sweden become the dominant power of northern Europe — controlling the Baltic coast from Finland to Prussia — before the catastrophic losses of the Great Northern War (1700–1721) ended Swedish great-power ambitions.\n\nModern Sweden's distinctive character was shaped by industrialisation (1870–1930), the 'Swedish Model' of social democracy (1930s onward), and the welfare state built by the Social Democratic Party's long dominance (1932–1976). Sweden maintained strict neutrality in both World Wars, allowing it to emerge from WWII with its industrial capacity intact and its welfare state building boom uninterrupted. By the late 20th century, Sweden was internationally recognised as the model of social democracy — combining market economics with comprehensive welfare provision, strong labour rights, and active government.",
    "causes": [
      "Sweden's geographic position on the Baltic Sea — with access to Baltic trade routes, abundant forest and iron resources, and a defensible peninsula — enabled Viking-era commercial expansion and provided the natural and human resources for Sweden's subsequent medieval and early modern state-building.",
      "The Protestant Reformation in Sweden (officially adopted 1527 under Gustav Vasa, who used the confiscation of church property to finance the Swedish state) was a decisive state-building moment — the fusion of Lutheran church and Swedish national identity that shaped Swedish culture and politics for centuries.",
      "Sweden's traumatic defeat in the Great Northern War (1700–1721) — losing Finland to Russia and its Baltic empire — ended Swedish great-power pretensions and redirected national energy toward internal development, ultimately contributing to the political stability that enabled 19th–20th century economic modernisation."
    ],
    "effects": [
      "Swedish industrial-era innovations — in ball bearings (SKF), dynamite (Alfred Nobel, whose fortune created the Nobel Prizes), telecommunications (Ericsson), and forest products — gave Sweden a disproportionate global technological influence relative to its population size.",
      "The Swedish social democratic model — the 'Nordic Model' combining generous welfare state, strong labour rights, high taxes, and open market economy — became an internationally influential template for progressive governance, studied and debated across the political spectrum globally from the 1960s onward.",
      "Alfred Nobel's establishment of the Nobel Prizes (1895, awarded from 1901) created the world's most prestigious academic and humanitarian awards — an institution that has given Sweden cultural influence far exceeding its geographic or population weight in global affairs."
    ],
    "relationships": [
      {"sourceSlug": "sweden", "sourceName": "Sweden", "verb": "PRODUCES", "targetSlug": "alfred-nobel", "targetName": "Alfred Nobel", "context": "Alfred Nobel — Swedish inventor of dynamite and founder of the Nobel Prizes — is Sweden's most globally influential individual, whose prizes have shaped international science, literature, and peace recognition since 1901."},
      {"sourceSlug": "sweden", "sourceName": "Sweden", "verb": "SHAPES", "targetSlug": "nordic-model", "targetName": "Nordic Model of Social Democracy", "context": "Sweden's Social Democratic welfare state — built from the 1930s under decades of Social Democratic governance — became the internationally recognised 'Nordic Model' of progressive political economy."},
      {"sourceSlug": "great-northern-war", "sourceName": "Great Northern War (1700–1721)", "verb": "TRANSFORMS", "targetSlug": "sweden", "targetName": "Sweden", "context": "The Great Northern War's catastrophic losses ended Swedish great-power status and redirected Swedish national development toward the internal modernisation that eventually produced the modern welfare state."}
    ],
    "places": [
      {"name": "Stockholm, Sweden", "role": "Sweden's capital since the 13th century — the political, economic, and cultural centre of the Swedish state and the site of the Nobel Prize ceremonies"},
      {"name": "Baltic Sea", "role": "The maritime space that defined Swedish economic and strategic geography — from Viking-era trade routes to the 17th-century Baltic empire to modern shipping"},
      {"name": "Scandinavia", "role": "Sweden's broader regional context — its relationships with Norway, Denmark, and Finland have been the primary framework of Swedish diplomacy and identity formation"}
    ],
    "subjects": ["Swedish History", "Nordic History", "Medieval Era", "Scandinavia", "Social Democracy", "Medieval History", "Modern Era", "Viking Age"],
    "frameworks": ["WORLD_SYSTEMS", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Sweden is one of Europe's most historically significant northern nations — home to Viking-era Varangian expansion, the 17th-century Baltic empire, Alfred Nobel's dynamite and Nobel Prizes, and the internationally influential Nordic Model of social democracy. Its 200-year peace since 1814 (the longest in Europe) and its welfare state model have made Sweden a global reference for progressive governance.",
      "significanceCategory": "world-changing"
    }
  }
},

"gil-eanes": {
  "filepath": "data/appwrite-export/entities/290-Class-290/290gil-eanes.json",
  "slug": "gil-eanes",
  "data": {
    "summary": "Gil Eanes (fl. 1430s–1440s; died c. 1500) was a Portuguese navigator who in 1434 became the first European recorded to have successfully rounded Cape Bojador — a geographical and psychological barrier on the West African coast that had blocked European Atlantic exploration for over a decade and that represented one of the most significant navigational milestones in the history of exploration. Cape Bojador (modern Boujdour, Western Sahara) was located at approximately 26°N latitude on the Moroccan/Saharan coast — not a particularly challenging cape by modern standards, but one whose combination of shallow reefs, strong currents, unusual atmospheric conditions, and powerful mythological reputation had caused every Portuguese attempt to round it to fail or turn back. Twelve expeditions sponsored by Prince Henry the Navigator had been launched since the 1420s without success.\n\nThe psychological barrier was at least as significant as the physical one: Cape Bojador was associated with ancient legends of a 'Sea of Darkness' beyond which lay boiling seas, sea monsters, and magnetic rocks that would pull the iron fastenings from ships. The extreme fear of the unknown that had paralysed Portuguese exploration was as much a product of inherited classical and medieval cosmographical traditions as of actual navigational difficulty. When Gil Eanes finally rounded the cape in 1434 — on his second attempt, after failing the first year — his success demonstrated that the barrier was psychological as much as physical, and opened the entire West African coast to exploration.\n\nGil Eanes's rounding of Cape Bojador is considered one of the decisive moments of the Age of Discovery — a first step that made all subsequent Portuguese exploration of West Africa, the route to India, and the circumnavigation of the globe possible. The chronicler Gomes Eanes de Zurara described Prince Henry's joy at the news and the significance assigned to the achievement — the barrier had been 'the frontier of the world' and its crossing opened a new era.",
    "causes": [
      "Prince Henry the Navigator's systematic programme of maritime exploration — funding annual expeditions down the West African coast from his court at Sagres from the 1420s — provided the institutional support and repeated attempts that eventually produced Gil Eanes's successful rounding.",
      "Portuguese improvements in naval technology — the development of the caravel (lateen-rigged, shallow-drafted, able to sail closer to the wind) — gave Eanes a vessel better suited to coastal exploration than the earlier square-rigged vessels, enabling the tack away from the coast and back that allowed him to round the cape.",
      "The accumulated navigational experience of twelve failed expeditions — each adding to Portuguese knowledge of the currents, winds, and coastal conditions south of Morocco — provided Eanes with the practical information and psychological framework to attempt a different approach."
    ],
    "effects": [
      "The rounding of Cape Bojador (1434) opened the entire West African coast to Portuguese exploration — a process that within 50 years led to Bartolomeu Dias's rounding of the Cape of Good Hope (1488) and Vasco da Gama's establishment of the sea route to India (1498), transforming global trade.",
      "Gil Eanes's success demonstrated that the ancient geographical limits — the 'frontier of the world' myths — were psychological and cultural constructs rather than physical realities, breaking the ideological barrier that had made Atlantic exploration seem impossible and encouraging the systematic expansion of European geographical knowledge.",
      "The Portuguese model of systematic state-sponsored exploration — of which Gil Eanes's repeated attempts (funded and directed by Prince Henry) were the paradigmatic example — established the template for the Age of Discovery that Spain, England, France, and the Netherlands subsequently adopted."
    ],
    "relationships": [
      {"sourceSlug": "gil-eanes", "sourceName": "Gil Eanes", "verb": "ENABLES", "targetSlug": "portuguese-exploration", "targetName": "Portuguese Age of Discovery", "context": "Gil Eanes's rounding of Cape Bojador (1434) was the critical breakthrough that opened West Africa to Portuguese exploration — the first step toward the sea routes to India and the Americas."},
      {"sourceSlug": "henry-the-navigator", "sourceName": "Prince Henry the Navigator", "verb": "SPONSORS", "targetSlug": "gil-eanes", "targetName": "Gil Eanes", "context": "Henry the Navigator funded and directed the repeated expeditions to round Cape Bojador — including Gil Eanes's successful 1434 attempt — making him the institutional patron of the breakthrough."},
      {"sourceSlug": "cape-bojador", "sourceName": "Cape Bojador", "verb": "BLOCKS", "targetSlug": "gil-eanes", "targetName": "Gil Eanes", "context": "Cape Bojador — the 'frontier of the world' — was the physical and psychological barrier that Eanes overcame in 1434, breaking the block that had stopped European Atlantic exploration for over a decade."}
    ],
    "places": [
      {"name": "Cape Bojador (Boujdour), Western Sahara", "role": "The cape Eanes successfully rounded in 1434 — the geographical barrier whose crossing opened West Africa to Portuguese exploration"},
      {"name": "Lagos/Sagres, Portugal", "role": "Henry the Navigator's court at Sagres — the institutional base from which the Portuguese exploration programme was directed and from which Eanes's expeditions departed"}
    ],
    "subjects": ["Age of Discovery", "Portuguese Exploration", "Classical Era", "Navigation", "West Africa", "Medieval Era", "Atlantic History", "Exploration"],
    "frameworks": ["CAUSE_AND_EFFECT", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Gil Eanes was the Portuguese navigator who in 1434 rounded Cape Bojador — breaking the decade-long barrier that had blocked European Atlantic exploration and opening the West African coast to the Portuguese expeditions that eventually produced the sea route to India (1498) and transformed global trade. His achievement is one of the decisive moments of the Age of Discovery — the breakthrough that made all subsequent Atlantic and Indian Ocean exploration possible.",
      "significanceCategory": "world-changing"
    }
  }
},

"pacian": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250pacian.json",
  "slug": "pacian",
  "data": {
    "summary": "Pacian of Barcelona (c. 310–390 CE) was a 4th-century Spanish bishop — Bishop of Barcelona from around 365 CE until his death — and one of the most significant early Christian writers from the Iberian Peninsula. He is notable both for his theological and pastoral writings and for his famous dictum — preserved by his admiring correspondent Jerome — 'Christianus mihi nomen est, Catholicus vero cognomen' ('Christian is my name, Catholic my surname'): a formulation that expressed the early church's claim that 'Catholic' (universal) was the proper designation of orthodox Christianity, as opposed to the various schismatic and heretical groups (Novatianists, Montanists, Donatists) that also claimed the name Christian.\n\nPacian's surviving works include three letters against the Novatianists (a rigorist schismatic group that refused to readmit those who had lapsed during persecutions), a short treatise 'Paraenesis sive Exhortatorius libellus' (an exhortation against certain pagan customs that had infiltrated Christian communities — specifically the practice of the 'Cervulus', a New Year masquerade in which people dressed as deer, a pagan festivity), and a treatise on baptism. His anti-Novatianist writings are significant as evidence for the ongoing debates in the 4th-century Western church about the boundaries of penance, reconciliation, and the church's authority to readmit the lapsed — debates directly connected to the rigorist-laxist controversies that had produced the Donatist schism in Africa.\n\nPacian's Barcelona episcopate places him in the context of the 4th-century Hispano-Roman church's rapid development: the Iberian Peninsula had produced the Priscillianist heresy (condemned 380 CE), the proto-Gnostic movement that was the first Christian heresy to result in execution by Christian secular authorities. Pacian's pastoral works reflect the concerns of a bishop managing the interface between lingering pagan customs and the newly dominant Christian culture of the post-Constantinian empire.",
    "causes": [
      "The Novatianist schism — the rigorist movement that denied the church's authority to readmit those who had apostasised under persecution — created the theological controversy to which Pacian's letters were a response, positioning him as a defender of the more moderate Catholic position on penance and reconciliation.",
      "The rapid Christianisation of the Roman Empire after Constantine (313 CE) and the resulting influx of nominally Christian converts who retained pagan customs — such as the Cervulus masquerade — created the pastoral challenge that Pacian's exhortatory treatise addressed.",
      "Barcelona's position as an important Hispano-Roman city on the Mediterranean coast gave Pacian access to the theological debates circulating through the broader Latin church, and his contacts with Jerome (who praised him in 'De Viris Illustribus') placed him in the network of the 4th-century Latin church's intellectual elite."
    ],
    "effects": [
      "Pacian's formulation 'Christianus mihi nomen est, Catholicus vero cognomen' became one of the most quoted early expressions of the Catholic church's self-definition — a formulation that distinguished orthodox Christianity from schismatic groups and that remained a touchstone in later controversies about church unity.",
      "His anti-Novatianist letters contributed to the 4th-century Latin tradition of pastoral theology on penance and reconciliation — a tradition whose development led to the formal sacramental theology of penance that became a standard feature of Catholic practice.",
      "Pacian's 'Paraenesis' against the Cervulus masquerade is one of the earliest Christian condemnations of pagan popular customs still surviving in Christianised society — a genre of episcopal literature that became increasingly important in the 4th–6th centuries as the church worked to suppress or redirect pagan festive practices."
    ],
    "relationships": [
      {"sourceSlug": "pacian", "sourceName": "Pacian of Barcelona", "verb": "OPPOSES", "targetSlug": "novatianism", "targetName": "Novatianism", "context": "Pacian's three letters against the Novatianists defended the Catholic church's authority to readmit the lapsed — a position central to the 4th-century debates about penance and church unity."},
      {"sourceSlug": "jerome", "sourceName": "Saint Jerome", "verb": "COMMEMORATES", "targetSlug": "pacian", "targetName": "Pacian of Barcelona", "context": "Jerome preserved and praised Pacian's works in his 'De Viris Illustribus' — the primary source for much of what we know about Pacian's life, works, and his famous Christian/Catholic formulation."},
      {"sourceSlug": "pacian", "sourceName": "Pacian of Barcelona", "verb": "SHAPES", "targetSlug": "catholic-identity", "targetName": "Catholic Identity", "context": "Pacian's formulation 'Christianus mihi nomen est, Catholicus vero cognomen' became one of the most quoted early expressions of the Catholic church's claim to universal orthodox Christian identity."}
    ],
    "places": [
      {"name": "Barcelona, Hispania (modern Spain)", "role": "Pacian's diocese — the Hispano-Roman city whose bishop he was for approximately 25 years, managing the pastoral challenges of the post-Constantinian Christianisation"},
      {"name": "Iberian Peninsula (Hispania)", "role": "The broader regional context of Pacian's episcopate — 4th-century Hispania was the site of major Christian controversies including Priscillianism and the rapid transformation of pagan Roman culture"}
    ],
    "subjects": ["Early Christianity", "Church History", "Classical Era", "Spain", "Catholic Identity", "Patristics", "4th Century", "Ancient History"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Pacian of Barcelona was the 4th-century Spanish bishop whose famous dictum — 'Christian is my name, Catholic my surname' — became one of the earliest and most-quoted expressions of Catholic self-definition. His anti-Novatianist writings contributed to the Latin tradition of penance theology, and his condemnation of the Cervulus masquerade is among the earliest episcopal attacks on pagan popular customs in the Christianised empire.",
      "significanceCategory": "regional"
    }
  }
},

"pietro-pileo-di-prata": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220pietro-pileo-di-prata.json",
  "slug": "pietro-pileo-di-prata",
  "data": {
    "summary": "Pietro Pileo di Prata (c. 1333–1401) was a Venetian cardinal and ecclesiastical diplomat who played a significant role in the Western Schism (1378–1417) — the crisis in which two (and later three) competing claimants held the papacy simultaneously, dividing the Latin church and producing one of the most serious institutional crises in medieval Catholicism. As Archbishop of Ravenna (1370–1378) and later a cardinal, Pileo di Prata initially supported Urban VI (the Roman pope) but subsequently shifted to the Avignon obedience under Clement VII — a switch that illustrated the political complexity of allegiance during the Schism and that made him a significant figure in the negotiations for reunion.\n\nPileo di Prata's most important role came in his later career when he worked as a mediator and diplomat attempting to resolve the Schism. He was involved in the negotiations leading to the Council of Pisa (1409) — the council convened by cardinals from both obediences in an attempt to end the Schism by deposing both claimants and electing a new pope (Alexander V). While the Council of Pisa paradoxically worsened the Schism by creating a third claimant rather than resolving the division, it was an important step toward the eventual resolution at the Council of Constance (1414–1418). Pileo died in 1401, before the final resolution, but his diplomatic career represented the growing consensus among senior clergy that conciliar action was the only way to end the crisis.\n\nPileo di Prata's career illustrates the profound institutional and theological crisis that the Western Schism created for the medieval church: cardinals, bishops, and theologians were forced to choose between competing legitimacies, sometimes switching allegiance as political circumstances changed, and to develop the theoretical frameworks (conciliarism) that would eventually provide a mechanism for resolving the crisis at Constance.",
    "causes": [
      "The contested election of Urban VI (1378) — whose erratic and abusive behaviour caused the cardinals who had elected him to reverse their support and elect Clement VII at Avignon — created the Western Schism that divided the Latin church for nearly 40 years and forced senior clergy like Pileo di Prata to choose between competing obediences.",
      "The political interests of European monarchies — France supporting the Avignon papacy, England and the Holy Roman Empire initially supporting Rome — shaped the ecclesiastical allegiances of bishops and cardinals in ways that made the Schism a proxy conflict for secular political rivalries.",
      "The growing conciliarist movement — the theological argument that a general council of the church had authority superior to any individual pope, and could therefore resolve a disputed papal succession — provided the intellectual framework for the diplomatic efforts in which Pileo di Prata participated."
    ],
    "effects": [
      "Pileo di Prata's diplomacy contributed to the growing consensus for conciliar action that eventually produced the Council of Pisa (1409) and the Council of Constance (1414–1418) — the conciliarist solution to the Western Schism that established the principle that a general council could depose popes.",
      "His career as a cardinal who switched obediences illustrates the political and moral complexity of the Schism — the way in which clerics at the highest level were forced to navigate competing legitimacies, producing the institutional flexibility and the pragmatic conciliarism that eventually enabled resolution.",
      "The Western Schism crisis that shaped Pileo di Prata's career contributed to the broader 15th-century conciliarist movement — the political and theological tradition that influenced the later critique of papal monarchy and provided some of the intellectual groundwork for the Protestant Reformation."
    ],
    "relationships": [
      {"sourceSlug": "pietro-pileo-di-prata", "sourceName": "Pietro Pileo di Prata", "verb": "PARTICIPATES_IN", "targetSlug": "western-schism", "targetName": "Western Schism (1378–1417)", "context": "Pileo di Prata was a senior cardinal whose career spanned the Western Schism — switching from Urban VI to Clement VII and later working toward the conciliar solution."},
      {"sourceSlug": "council-of-pisa", "sourceName": "Council of Pisa (1409)", "verb": "INFLUENCES", "targetSlug": "pietro-pileo-di-prata", "targetName": "Pietro Pileo di Prata", "context": "Pileo di Prata's diplomatic work contributed to the movement toward the Council of Pisa — the conciliarist attempt to end the Schism by deposing both papal claimants."},
      {"sourceSlug": "western-schism", "sourceName": "Western Schism", "verb": "SHAPES", "targetSlug": "conciliarism", "targetName": "Conciliarism", "context": "The Western Schism's crisis of divided legitimacy drove the development of conciliarist theology — the argument that a general council could override papal authority — in which figures like Pileo di Prata were important participants."}
    ],
    "places": [
      {"name": "Ravenna, Italy", "role": "Where Pileo di Prata served as Archbishop (1370–1378) — the ancient Adriatic city whose archbishopric was one of the most prestigious in northern Italy"},
      {"name": "Rome and Avignon", "role": "The competing centres of the Western Schism — the two (and later three) rival papal courts to which Pileo di Prata successively gave and shifted his allegiance"}
    ],
    "subjects": ["Medieval Catholicism", "Church History", "Medieval History", "Medieval Era", "Italy", "Western Schism", "Conciliarism", "Ecclesiastical Diplomacy"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Pietro Pileo di Prata was a Venetian cardinal whose career spanned the Western Schism — the 40-year crisis of divided papal legitimacy. His switching of allegiance from Urban VI to Clement VII and his diplomatic work toward conciliar resolution illustrated the institutional complexity of the Schism and contributed to the conciliarist movement that eventually resolved it at the Council of Constance (1418).",
      "significanceCategory": "regional"
    }
  }
},

"fulk-of-reims": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250fulk-of-reims.json",
  "slug": "fulk-of-reims",
  "data": {
    "summary": "Fulk of Reims (also Foulques; c. 845–900 CE) was Archbishop of Reims from 882 CE until his assassination in 900 CE — one of the most politically active and influential prelates of the Carolingian twilight and the beginning of the Capetian era in France. His archiepiscopate coincided with the catastrophic collapse of Carolingian central authority in the West Frankish kingdom — the period of Viking invasions, competing Carolingian claimants, and the rise of the territorial aristocracy that would eventually produce the feudal kingdom of medieval France. As Archbishop of Reims — the most prestigious ecclesiastical see in the West Frankish kingdom, whose archbishop crowned the king of France — Fulk was not merely a bishop but a major political actor in the succession struggles of the late Carolingian period.\n\nFulk was among the most energetic correspondents of his era: his letters survive and show him in active communication with Pope Stephen V, with Anglo-Saxon England (he corresponded with Archbishop Plegmund of Canterbury and was instrumental in persuading King Alfred the Great to send scholarly talent to help reform the English church), and with Carolingian political figures. He played a central role in the education and promotion of the monk Remigius of Auxerre — one of the great Carolingian scholars — and Reims under Fulk was an important centre of the Carolingian renaissance's final phase.\n\nFulk's political career was defined by his role in the Carolingian succession struggles: he initially supported Charles the Fat, then played a role in the elevation of Odo of Paris (a non-Carolingian) as king (888 CE), and later became a strong supporter of Charles the Simple — the last significant Carolingian — against Odo's successor Robert I. His assassination in 900 CE by Baldwin II of Flanders (in a dispute over monastic property) was a symptom of the violence and political instability of the late Carolingian world.",
    "causes": [
      "The Viking invasions of the West Frankish kingdom (beginning intensively from the 840s) and the failure of the Carolingian state to provide effective military protection created the political vacuum in which powerful ecclesiastics like Fulk could exercise quasi-regal authority and negotiate directly with rival secular powers.",
      "The collapse of Carolingian central authority after Louis the Stammerer (879 CE) and the competing claims of multiple Carolingian and non-Carolingian claimants forced the Archbishop of Reims — as the kingdom's crown-bestower — into an unavoidably political role in legitimating royal authority.",
      "Fulk's personal energy, political skill, and scholarly networks — including his connections to Pope Stephen V, Alfred the Great's England, and the Carolingian intellectual tradition — gave him an exceptional capacity to exercise the political power that the institutional position of Archbishop of Reims made possible."
    ],
    "effects": [
      "Fulk's role in the election of Odo of Paris (888 CE) — the first non-Carolingian king of the West Franks — was a pivotal moment in the transition from the Carolingian to the Capetian kingdom: his willingness to crown a non-Carolingian broke the dynastic principle that had sustained Carolingian legitimacy.",
      "Fulk's correspondence with Alfred the Great's England — and his role in sending scholars to help reform the English church — contributed to the Anglo-Saxon scholarly renaissance of the late 9th century that produced Alfred's translation programme and the eventual flowering of Old English literature.",
      "Fulk's assassination by Baldwin II of Flanders in 900 CE — a murder of an archbishop over monastic property — illustrated the violence and institutional breakdown of the late Carolingian world, and was a harbinger of the feudal anarchy that the 10th century would bring to the West Frankish kingdom."
    ],
    "relationships": [
      {"sourceSlug": "fulk-of-reims", "sourceName": "Fulk of Reims", "verb": "CROWNS", "targetSlug": "odo-of-paris", "targetName": "Odo of Paris", "context": "Fulk's coronation of Odo (888 CE) — the first non-Carolingian king of the West Franks — was a pivotal political act that broke the Carolingian dynastic principle and began the transition to Capetian rule."},
      {"sourceSlug": "fulk-of-reims", "sourceName": "Fulk of Reims", "verb": "CORRESPONDS_WITH", "targetSlug": "alfred-the-great", "targetName": "Alfred the Great", "context": "Fulk's correspondence with Alfred and his role in sending scholars to England contributed to the late 9th-century Anglo-Saxon scholarly renaissance that produced Alfred's translation programme."},
      {"sourceSlug": "carolingian-decline", "sourceName": "Carolingian Decline", "verb": "SHAPES", "targetSlug": "fulk-of-reims", "targetName": "Fulk of Reims", "context": "The collapse of Carolingian central authority and the Viking invasions made Fulk's archiepiscopate a period of intense political engagement — forcing the Archbishop of Reims to become a major actor in the succession struggles of the late Carolingian kingdom."}
    ],
    "places": [
      {"name": "Reims, France", "role": "Fulk's archiepiscopal see — the most prestigious ecclesiastical centre in the West Frankish kingdom, whose archbishop crowned the kings of France"},
      {"name": "Anglo-Saxon England", "role": "The destination of Fulk's scholarly correspondence and scholars — his connections to Alfred the Great's court were part of the late Carolingian scholarly network"}
    ],
    "subjects": ["Medieval Church", "Carolingian History", "Medieval Era", "France", "Frankish History", "Medieval History", "Archbishop", "Political History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Fulk of Reims was the politically active Archbishop of Reims (882–900) during the Carolingian collapse — the archbishop who crowned the first non-Carolingian king (Odo, 888), corresponded with Alfred the Great, and was assassinated by a Count of Flanders. His career marks the transition from Carolingian to Capetian France and the emergence of the feudal political order that replaced it.",
      "significanceCategory": "significant"
    }
  }
},

"vitello": {
  "filepath": "data/appwrite-export/entities/210-Class-210/210vitello.json",
  "slug": "vitello",
  "data": {
    "summary": "Vitello (also Witelo, Vitellio; c. 1230–c. 1275) was a medieval Polish-Silesian mathematician and natural philosopher — one of the most important optical scientists of the 13th century — whose massive Latin treatise 'Perspectiva' (c. 1270–1278) became the standard European textbook on optics for over three centuries. Born in Silesia (in the region that is now southwestern Poland and northeastern Czech Republic), Vitello studied in Paris and Padua and was working in Viterbo (near Rome) when he composed the 'Perspectiva', which he dedicated to William of Moerbeke (the great Flemish translator of Greek scientific texts who was also in Viterbo at the papal court).\n\nVitello's 'Perspectiva' was a systematic, mathematically rigorous synthesis of all earlier optical knowledge — drawing primarily on the Arabic scientist Ibn al-Haytham's revolutionary 'Kitab al-Manazir' (Book of Optics, c. 1015), which had transformed the science of optics by demonstrating that vision occurred through rays entering the eye from luminous objects rather than rays emitted from the eye. Vitello's work organised and extended Ibn al-Haytham's findings, added geometric proofs, and transmitted the Arabic optical tradition to the Latin West in a form that became the primary reference for European optics. The 'Perspectiva' consisted of ten books covering reflection, refraction, the anatomy of the eye, the psychology of visual perception, and the behaviour of lenses and mirrors.\n\nVitello's influence on subsequent European science was substantial: Roger Bacon's optical work drew on similar sources; John Pecham's 'Perspectiva Communis' simplified Vitello's material for a wider audience; and most significantly, Johannes Kepler — working in the early 17th century — titled his foundational work 'Ad Vitellionem Paralipomena' (Additions to Vitello, 1604), directly positioning his revolutionary theory of the retinal image as a supplement and correction to Vitello's framework. This means Vitello's 'Perspectiva' was the technical baseline from which Kepler launched the modern science of optics.",
    "causes": [
      "The Latin translation of Ibn al-Haytham's 'Kitab al-Manazir' — the revolutionary Arabic optical treatise that transformed the science of vision — provided Vitello with the intellectual foundation for his 'Perspectiva', transmitting the most advanced optical science of the medieval Islamic world to the Latin West.",
      "Vitello's access to William of Moerbeke at the papal court in Viterbo — who was actively translating Greek scientific texts — placed him at the centre of the 13th-century translation movement that was making Greek and Arabic science available to Latin scholars, providing both intellectual stimulus and scholarly community.",
      "The 13th-century expansion of European universities — and the curriculum of the quadrivium that included mathematics and natural philosophy — created both the educational demand for a comprehensive Latin optics textbook and the scholarly infrastructure within which Vitello's work could be produced and disseminated."
    ],
    "effects": [
      "Vitello's 'Perspectiva' was the standard European optics textbook for over three centuries — printed in Basel in 1535 (with Ibn al-Haytham's work), it was the form in which European scholars encountered the mathematical science of light, vision, and optics until Kepler's revolution.",
      "Kepler's direct engagement with Vitello's 'Perspectiva' in his 'Ad Vitellionem Paralipomena' (1604) — the work in which Kepler first explained retinal image formation and laid the foundations of modern optics — makes Vitello a direct intellectual ancestor of the Scientific Revolution's optical achievements.",
      "Vitello's synthesis of Arabic and Greek optical science in a Latin framework was a paradigmatic example of the 13th-century translation and synthesis movement — the intellectual process by which medieval European scholarship absorbed, organised, and extended the achievements of Islamic science."
    ],
    "relationships": [
      {"sourceSlug": "vitello", "sourceName": "Vitello (Witelo)", "verb": "TRANSMITS", "targetSlug": "ibn-al-haytham", "targetName": "Ibn al-Haytham", "context": "Vitello's 'Perspectiva' was the primary vehicle through which Ibn al-Haytham's revolutionary optics (the intromission theory of vision) reached Latin European science — making him the crucial intermediary between Islamic and European optical traditions."},
      {"sourceSlug": "johannes-kepler", "sourceName": "Johannes Kepler", "verb": "BUILDS_ON", "targetSlug": "vitello", "targetName": "Vitello", "context": "Kepler's foundational optical work 'Ad Vitellionem Paralipomena' (1604) — which introduced the modern theory of retinal image formation — was explicitly titled as a supplement and correction to Vitello's 'Perspectiva'."},
      {"sourceSlug": "william-of-moerbeke", "sourceName": "William of Moerbeke", "verb": "COLLABORATES_WITH", "targetSlug": "vitello", "targetName": "Vitello", "context": "Vitello dedicated his 'Perspectiva' to William of Moerbeke — the great translator of Greek scientific texts at the papal court in Viterbo — reflecting the collaborative scholarly milieu that produced the work."}
    ],
    "places": [
      {"name": "Silesia (Poland/Czech Republic)", "role": "Vitello's homeland — the region whose intellectual culture shaped his early education and whose name is reflected in the 'Silesian' identification in medieval sources"},
      {"name": "Viterbo, Italy (papal court)", "role": "Where Vitello composed the 'Perspectiva' and where he had access to William of Moerbeke — the papal court as a centre of 13th-century scientific scholarship"}
    ],
    "subjects": ["Medieval Science", "Optics", "Medieval History", "Medieval Era", "Poland", "Mathematics", "Natural Philosophy", "Islamic-European Transfer"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "CULTURAL_TRANSMISSION"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Vitello was the 13th-century Polish-Silesian mathematician whose 'Perspectiva' (c. 1270–1278) became the standard European optics textbook for three centuries — the primary vehicle transmitting Ibn al-Haytham's revolutionary optical science to the Latin West. Kepler's foundational 'Ad Vitellionem Paralipomena' (1604) was titled as a direct supplement to Vitello's work, making Vitello the baseline from which modern optics was launched — a direct intellectual ancestor of the Scientific Revolution.",
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
