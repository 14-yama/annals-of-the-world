#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 06 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: south-america, asia, americas, oceania, latin-america,
          antarctica, taras-fedorovych, ildibad
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-06-may2026"

ENRICHMENTS = {

"south-america": {
  "filepath": "data/appwrite-export/entities/410-Class-410/410south-america.json",
  "slug": "south-america",
  "data": {
    "summary": "South America is the world's fourth-largest continent — a 17.8 million km² landmass running from the tropical equatorial forests of the Amazon basin in the north to the wind-swept sub-Antarctic tip of Tierra del Fuego in the south. Home to approximately 430 million people across 12 sovereign nations and two territories, the continent encompasses some of the most ecologically distinct environments on Earth: the Amazon rainforest (5.5 million km², 10% of all species on the planet), the Atacama Desert (the driest non-polar desert on Earth), the Andes mountain chain (the world's longest continental mountain range at 7,000 km), and the Patagonian steppe. Its cultural geography is dominated by the legacies of Andean civilisation, Iberian colonialism, African enslavement, and 20th-century political radicalism.\n\nThe deep human history of South America extends at least 15,000 years, with the Monte Verde site in Chile (14,500 years old) providing some of the earliest evidence of human settlement in the Americas. The continent's pre-Columbian civilisations reached their climax in the Inca Empire (Tawantinsuyu), which at its height around 1500 CE administered 12 million people across 2 million km² from modern Colombia to Chile, using a sophisticated system of roads, relay messengers (chasquis), and knotted recording devices (quipu) without a writing system. The Spanish conquest of the Inca Empire (1532–1572) under Francisco Pizarro was one of the most consequential and devastating episodes of the early modern period, bringing epidemic disease, forced labour, and cultural destruction that reduced the indigenous population by an estimated 80–95%.\n\nThe 19th century saw the independence of all South American Spanish colonies between 1810 and 1825, shaped by Simón Bolívar's vision of a unified continental republic and José de San Martín's military campaigns in the south. The 20th century brought cycles of economic nationalism (Brazilian industrialisation under Vargas, Argentine Perónism), military dictatorship (Argentina 1976–1983, Chile 1973–1990, Brazil 1964–1985), and in the 21st century, the 'Pink Tide' of left-wing governments including Lula's Brazil, Chávez's Venezuela, Morales's Bolivia, and Correa's Ecuador. Brazil, with 215 million people and the 9th-largest economy, dominates the continent's political economy.",
    "causes": [
      "The Gondwana breakup (c. 80 million years ago) separated South America from Africa, creating the continent's extraordinary biodiversity through 50+ million years of evolutionary isolation before the land bridge reconnection with North America (the Great American Biotic Interchange, c. 3 million years ago).",
      "The Spanish and Portuguese colonisation (1492–1830) imposed plantation economies, extractive silver mining (Potosí), and the Atlantic slave trade on the continent — the colonial economic structures whose legacies continue to shape South American inequality.",
      "The 19th-century independence movements (1810–1825) broke the Iberian colonial framework but largely preserved colonial social hierarchies — mestizo and criollo elites replacing Spanish administrators without fundamental redistribution of land, wealth, or political power."
    ],
    "effects": [
      "South America's Amazon rainforest is the largest terrestrial carbon sink on Earth and the primary regulatory system for South American and global rainfall patterns — its ongoing deforestation (17% lost since 1970, accelerating under Bolsonaro 2019–2022) is a primary driver of both regional climate disruption and global greenhouse gas emissions.",
      "The continent's resource geography — oil (Venezuela, Brazil), copper (Chile, Peru), soybeans and beef (Brazil, Argentina), lithium (Bolivia, Argentina, Chile in the 'Lithium Triangle') — has made it the primary arena for 21st-century resource geopolitics as the energy transition drives demand for critical minerals.",
      "South American political experiments — from socialist Chile under Allende, to Cuba-influenced guerrilla movements, to Bolívar's Pan-Americanism — have been among the most influential laboratories of 20th-century political thought, shaping both leftist theory and the counter-revolutionary doctrine that produced the CIA-backed coups of the 1970s."
    ],
    "relationships": [
      {"sourceSlug": "south-america", "sourceName": "South America", "verb": "CONTAINS", "targetSlug": "inca-empire", "targetName": "Inca Empire", "context": "The Inca Empire (Tawantinsuyu) was South America's largest pre-Columbian civilisation, administering 2 million km² from Colombia to Chile before the Spanish conquest of 1532."},
      {"sourceSlug": "south-america", "sourceName": "South America", "verb": "CONTAINS", "targetSlug": "amazon-rainforest", "targetName": "Amazon Rainforest", "context": "The Amazon basin, covering 5.5 million km² across Brazil, Peru, Colombia, and six other countries, is the world's largest tropical forest and a primary global carbon sink."},
      {"sourceSlug": "spanish-empire", "sourceName": "Spanish Empire", "verb": "TRANSFORMS", "targetSlug": "south-america", "targetName": "South America", "context": "Spanish colonialism (1492–1825) imposed plantation economies, silver extraction, and the Atlantic slave trade on South America, creating the colonial social structures whose legacies define contemporary inequality."},
      {"sourceSlug": "simon-bolivar", "sourceName": "Simón Bolívar", "verb": "TRANSFORMS", "targetSlug": "south-america", "targetName": "South America", "context": "Bolívar's liberation campaigns (1810–1825) created six independent republics in northern South America and established the vision of Hispano-American unity that continues to shape regional identity and politics."}
    ],
    "places": [
      {"name": "Amazon Basin, Brazil/Peru/Colombia", "role": "Core ecological zone — the world's largest rainforest covering 40% of South America and regulating regional and global climate"},
      {"name": "Andes Mountains", "role": "The world's longest continental mountain range (7,000 km) — defining the western edge of the continent and hosting the core of Andean civilisation"},
      {"name": "Potosí, Bolivia", "role": "Site of the world's richest silver mine under the Spanish Empire — the engine of colonial extraction that financed the Spanish state and shaped global monetary history"}
    ],
    "subjects": ["Geography", "World History", "Colonial History", "Indigenous History", "Environment", "Political History", "Latin America", "Global History"],
    "frameworks": ["WORLD_SYSTEMS", "POSTCOLONIAL_ANALYSIS", "ENVIRONMENTAL_HISTORY", "LONGUE_DUREE"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "South America is one of humanity's primary living spaces — home to the world's largest rainforest, the Andean civilisational tradition, the Spanish colonial silver economy that financed early modern European history, and the 20th century's most significant experiments in socialist and liberation politics. Its Amazon basin is the single most important terrestrial ecosystem for global climate stability.",
      "significanceCategory": "world-changing"
    }
  }
},

"asia": {
  "filepath": "data/appwrite-export/entities/410-Class-410/410asia.json",
  "slug": "asia",
  "data": {
    "summary": "Asia is the world's largest and most populous continent — 44.6 million km² (30% of Earth's total land area) and home to 4.7 billion people (60% of the global population). It spans from the Bosphorus and the Ural Mountains in the west to the Pacific coast in the east, from the Arctic tundra in the north to the tropical islands of Southeast Asia in the south. Asia contains the world's highest mountains (the Himalayas, with Everest at 8,849 m), the world's deepest lake (Baikal, 1,642 m), the largest inland sea (Caspian Sea), and the two most populous nations in human history (China and India, each with over 1 billion people). All three major Abrahamic religions — Judaism, Christianity, and Islam — and all major Eastern religions — Hinduism, Buddhism, Confucianism, Daoism, Sikhism — originated on the Asian continent.\n\nAsia was the cradle of the world's earliest civilisations: Mesopotamia (Sumer, c. 3500 BCE), the Indus Valley civilisation (c. 2600 BCE), the Yellow River civilisation in China (c. 2000 BCE), and the cradle of all major world religions. The Silk Road — the overland and maritime trade network connecting China to the Mediterranean — was Asia's most consequential contribution to global history: for 1,500 years (roughly 200 BCE to 1450 CE) it transmitted silk, spices, paper, gunpowder, the compass, and the bubonic plague between the civilisations of East Asia, Central Asia, South Asia, the Middle East, and Europe. The Mongol Empire (1206–1368), which originated in Central Asia and conquered territory from Korea to Hungary, was the largest contiguous land empire in history and the most comprehensive engine of Eurasian connectivity before the age of European colonialism.\n\nThe 19th and 20th centuries saw Asia's transformation from the primary object of European colonial extraction to the primary engine of global economic growth. The Japanese Meiji Restoration (1868), the Chinese Communist Revolution (1949), and the 'Four Asian Tigers' (South Korea, Taiwan, Hong Kong, Singapore) industrial takeoffs of the 1960s–1980s demonstrated different pathways of industrialisation that cumulatively shifted the global economic centre of gravity back toward Asia. China's GDP surpassed Japan's in 2010 and is projected to surpass the United States' by the 2030s, marking what some scholars call 'the Asian century'.",
    "causes": [
      "Asia's exceptional ecological diversity — from Arctic tundra to tropical rainforest, from the world's highest mountains to the Ganges-Brahmaputra-Mekong river systems — created the wide range of domesticable plants and animals (wheat, rice, millet, cattle, horses) that enabled the independent emergence of agriculture and civilisation in multiple Asian regions.",
      "The Eurasian landmass's east-west orientation (unlike the Americas' north-south axis) allowed the horizontal diffusion of crops, technologies, and diseases along similar climate zones — the primary geographic factor, as Jared Diamond argues, enabling Eurasian civilisations to develop complex societies, metallurgy, and ultimately pandemic disease exposure.",
      "Asia's geographic centrality in the Eastern Hemisphere — positioned between the Mediterranean, sub-Saharan Africa, and the Pacific — made it the natural hub of the Silk Road trading system that for millennia was the primary mechanism of trans-civilisational exchange."
    ],
    "effects": [
      "The major inventions originating in Asia — paper (China, 105 CE), printing (China, 1040 CE), gunpowder (China, 9th century), the compass (China, 11th century), steel production (India, 6th century BCE), Hindu-Arabic numerals (India, 5th–7th century CE) — were transmitted to Europe via the Islamic world and fundamentally enabled the European Scientific Revolution and the Industrial Revolution.",
      "The Asian religious systems — Hinduism, Buddhism, Islam, Confucianism, Daoism — collectively provide the religious and philosophical frameworks for over 60% of the global population, making Asia the primary source of human spiritual and ethical tradition.",
      "The 21st-century Asian economic rise — China as the world's manufacturing hub, India as the world's services outsourcing centre, and the ASEAN economies as intermediate manufacturing centres — represents the most significant shift in global economic geography since the European Industrial Revolution, with profound implications for geopolitics, climate policy, and global governance."
    ],
    "relationships": [
      {"sourceSlug": "asia", "sourceName": "Asia", "verb": "PRODUCES", "targetSlug": "silk-road", "targetName": "Silk Road", "context": "The Silk Road — Asia's primary contribution to global connectivity — transmitted goods, technologies, religions, and diseases between Asian, Middle Eastern, and European civilisations for 1,500 years."},
      {"sourceSlug": "asia", "sourceName": "Asia", "verb": "PRODUCES", "targetSlug": "mongol-empire", "targetName": "Mongol Empire", "context": "The Mongol Empire (1206–1368), originating in Central Asia, became the largest contiguous land empire in history and the most comprehensive engine of Eurasian connectivity before the European maritime age."},
      {"sourceSlug": "asia", "sourceName": "Asia", "verb": "PRODUCES", "targetSlug": "four-asian-tigers", "targetName": "Four Asian Tigers", "context": "The East Asian economic miracle — South Korea, Taiwan, Hong Kong, Singapore — demonstrated that non-Western industrialisation was possible, paving the way for China's rise and the concept of 'the Asian century'."}
    ],
    "places": [
      {"name": "Mesopotamia, Iraq", "role": "Location of the world's earliest urban civilisations (Sumer, Babylon, Assyria) — the origin of writing, law codes, and the urban state form"},
      {"name": "Himalayas, Nepal/Tibet/India", "role": "The world's highest mountain range — the geographic spine separating South Asia from Central Asia and defining the monsoon system that sustains 1.5 billion people"},
      {"name": "Chang'an (Xi'an), China", "role": "Eastern terminus of the Silk Road and capital of the Tang Dynasty — the most cosmopolitan city in the world at its 7th-century peak"}
    ],
    "subjects": ["Geography", "World History", "Civilisation", "Global History", "Religion", "Economics", "Silk Road", "East Asia"],
    "frameworks": ["WORLD_SYSTEMS", "LONGUE_DUREE", "STRUCTURAL_ANALYSIS", "COMPARATIVE_HISTORY"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Asia is the world's largest and most populous continent — the origin of all major world religions, the cradle of the earliest civilisations, the birthplace of paper, printing, gunpowder, and the compass, and the hub of the Silk Road trading system that connected Eurasia for 1,500 years. In the 21st century, Asia's economic rise is the most significant shift in global power since the European Industrial Revolution.",
      "significanceCategory": "world-changing"
    }
  }
},

"americas": {
  "filepath": "data/appwrite-export/entities/410-Class-410/410americas.json",
  "slug": "americas",
  "data": {
    "summary": "The Americas — comprising North America, Central America, the Caribbean, and South America — form a 42.5 million km² contiguous landmass that extends from the Arctic Ocean in the north to Cape Horn at 55°S, making it the longest continuous landmass on Earth at approximately 15,000 km from tip to tip. Home to 1.05 billion people across 35 sovereign nations, the Americas represent one of the last major landmasses to be settled by Homo sapiens (the earliest confirmed human presence at Monte Verde, Chile, dates to c. 14,500 BCE) and the most profoundly transformed by European colonialism in the 15th–19th centuries. The concept of 'the Americas' as a single geographic entity derives from the 1507 Waldseemüller map, which named the southern continent 'America' after Amerigo Vespucci's accounts of Gonçalo Coelho's 1501–1502 Brazilian voyage.\n\nThe pre-Columbian Americas supported some of the world's most sophisticated civilisations. Mesoamerica produced the Maya (200–900 CE classical period), with their independently developed writing, calendar systems, and astronomical knowledge; the Aztec Triple Alliance (1428–1521), which organised a tribute empire of 5–6 million in central Mexico; and the Classic Teotihuacan (100–600 CE), with a planned urban centre of 100,000–200,000 people. In South America, the Inca Empire (1438–1532) administered 12 million people across 2 million km² using roads, relay stations, and sophisticated administrative quipu. The Mississippi-based Cahokia (c. 1050–1350 CE) in North America reached a population of 10,000–20,000 — larger than contemporary London.\n\nThe Columbian Exchange that followed 1492 — the mutual transfer of plants, animals, diseases, and peoples between the Americas and the Old World — was the most consequential ecological event in human history since the domestication of agriculture. American crops (potato, maize, tomato, sweet potato, cacao, tobacco) transformed the diet and demographics of Europe, Africa, and Asia; Old World diseases (smallpox, measles, influenza) killed an estimated 50–90% of the indigenous American population within a century of contact. The Atlantic slave trade (1500–1865) brought approximately 12.5 million enslaved Africans to the Americas, creating the diaspora population and the plantation economy whose legacies continue to shape American societies.",
    "causes": [
      "The Bering land bridge crossing (c. 15,000–20,000 BCE) brought the first human populations to the Americas via Siberia, initiating the colonisation of the only major landmass that had been free of modern humans until the Late Pleistocene.",
      "The Americas' north-south orientation — unlike Eurasia's east-west axis — created barriers to the latitudinal diffusion of crops and domesticated animals across climate zones, potentially explaining the slower development of large-scale agriculture and pandemic disease immunity compared to Eurasian civilisations.",
      "The Columbian contact after 1492 introduced the American continent to the most consequential network of exchange in human history: the combination of European pathogens, animal domesticates, and the Atlantic trade system — the Columbian Exchange — fundamentally transformed both the Americas and the Old World."
    ],
    "effects": [
      "American crops — particularly the potato (Andean origin), maize (Mesoamerican origin), and the sweet potato (South American origin) — are credited with enabling the European population expansion of the 18th–19th centuries and with fundamentally transforming Asian and African diets, making the Americas the primary source of global caloric surplus.",
      "The United States, founded on the western hemisphere's largest contiguous territory with the world's most navigable inland waterway system (Mississippi-Missouri-Ohio), became the world's largest economy by 1890 and its primary geopolitical power by 1945 — a position whose roots lie in the geographic advantages Diamond and others identify with the Americas' specific ecology.",
      "The 19th–20th century independence of the American republics created the first post-colonial political order in the world — establishing the templates of republican government, popular sovereignty, and national self-determination that the 20th century's decolonisation movements drew upon."
    ],
    "relationships": [
      {"sourceSlug": "americas", "sourceName": "The Americas", "verb": "CONTAINS", "targetSlug": "columbian-exchange", "targetName": "Columbian Exchange", "context": "The Columbian Exchange — the transfer of biota between the Americas and the Old World after 1492 — was the most consequential ecological event in the post-Pleistocene world, transforming global demography, agriculture, and disease."},
      {"sourceSlug": "americas", "sourceName": "The Americas", "verb": "CONTAINS", "targetSlug": "aztec-empire", "targetName": "Aztec Empire", "context": "The Aztec Triple Alliance (1428–1521) was the Americas' largest Mesoamerican empire at the time of Spanish contact — governing 5–6 million people through a sophisticated tribute network."},
      {"sourceSlug": "christopher-columbus", "sourceName": "Christopher Columbus", "verb": "CONNECTS", "targetSlug": "americas", "targetName": "The Americas", "context": "Columbus's 1492 voyage initiated the sustained contact between the Americas and the Old World that transformed both hemispheres — triggering the Columbian Exchange and the colonial era."}
    ],
    "places": [
      {"name": "Monte Verde, Chile", "role": "Site of the earliest confirmed human presence in the Americas (c. 14,500 BCE) — evidence of the Paleo-Indian colonisation that populated the hemisphere from Alaska to Tierra del Fuego"},
      {"name": "Tenochtitlan (Mexico City), Mexico", "role": "Capital of the Aztec Empire and, at its peak (c. 1500 CE), one of the five largest cities in the world with 200,000–400,000 inhabitants"},
      {"name": "Mississippi River, United States", "role": "Core of North America's inland waterway system — the geographic infrastructure that enabled American agricultural and industrial development"}
    ],
    "subjects": ["Geography", "World History", "Pre-Columbian History", "Colonial History", "Columbian Exchange", "Indigenous History", "Global History"],
    "frameworks": ["WORLD_SYSTEMS", "LONGUE_DUREE", "POSTCOLONIAL_ANALYSIS", "ENVIRONMENTAL_HISTORY"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Americas were the last major landmass settled by humans and the most profoundly transformed by the Columbian Exchange — the transfer of plants, animals, diseases, and people that reshaped global demography, agriculture, and power after 1492. American crops (potato, maize, tomato) fed the world's population explosion. The United States became the 20th century's dominant power from within the Americas' geographic base.",
      "significanceCategory": "world-changing"
    }
  }
},

"oceania": {
  "filepath": "data/appwrite-export/entities/420-Class-420/420oceania.json",
  "slug": "oceania",
  "data": {
    "summary": "Oceania is the world's smallest 'continent' (or the largest geographic region of islands) — a vast expanse of the Pacific Ocean encompassing Australia (7.7 million km²), Melanesia, Micronesia, Polynesia, and New Zealand, totalling approximately 8.5 million km² of land spread across 165 million km² of ocean. With approximately 44 million people, it is the least densely populated inhabited region on Earth. Despite its physical marginality in global terms, Oceania is the setting for one of history's most extraordinary achievements: the Polynesian settlement of the Pacific, one of the greatest navigational accomplishments in human prehistory, and the location of Australia — a continent that achieved total geographic isolation for 45 million years and whose First Peoples have the world's oldest continuous living cultural tradition.\n\nThe Polynesian settlement of the Pacific represents the culmination of the Austronesian expansion — the most geographically ambitious migration in human prehistory. Beginning from Taiwan around 5,000 years ago, Austronesian-speaking peoples spread across the Pacific, reaching Fiji around 1000 BCE, Samoa by 800 BCE, Hawaii by 600 CE, New Zealand by 1250–1300 CE, and Easter Island by 900 CE — navigating 60 million km² of open ocean using star navigation, wave-pattern reading, and outrigger canoe technology without written records, metal tools, or navigational instruments. The settlement of Hawaii at 21° North and New Zealand at 46° South from the same Polynesian homeland represents an 8,000 km latitudinal range of ocean colonisation with no parallel in human history.\n\nEuropean contact with Oceania (from Magellan's 1521 Pacific crossing through Cook's three voyages 1768–1779) precipitated the most rapid demographic collapse in human history outside the Americas: the Aboriginal Australian population fell from an estimated 750,000 in 1788 to approximately 117,000 by 1901 — an 84% decline in 113 years from disease, violence, and dispossession. The 20th century saw the independence of most Pacific Island nations (Papua New Guinea 1975, Solomon Islands 1978, Vanuatu 1980, Kiribati 1979) and Australia's transformation from a British settler colony into a multicultural state and major regional power. In the 21st century, Pacific Island nations face existential threat from sea-level rise due to climate change.",
    "causes": [
      "The Austronesian expansion from Taiwan (c. 3000 BCE) provided the population, technology (double-outrigger canoes), and navigational knowledge that enabled the Polynesian settlement of the vast Pacific — arguably the most ambitious human migration project in prehistory.",
      "Australia's 45-million-year tectonic isolation from Gondwana created the continent's unique marsupial megafauna, endemic flora, and biological exceptionalism — the ecological context that shaped Aboriginal Australian culture over 65,000 years of occupation.",
      "European colonialism's 18th-19th century expansion — motivated by Pacific trade routes, strategic positioning, and the resource value of Australian wool, gold, and agricultural land — imposed the settler-colonial order that defines the political geography of contemporary Oceania."
    ],
    "effects": [
      "The Aboriginal Australian cultural tradition — with continuous occupation of the continent dating to at least 65,000 BP and sophisticated knowledge systems of ecology, astronomy, and land management — represents the world's longest continuous cultural record and a primary data source for human deep prehistory.",
      "Australian gold rushes (1851–1861) attracted 600,000 migrants and transformed the continent into a prosperous settler society that would federate in 1901 as the world's first country founded on the principle of democratic federation — a constitutional model that influenced subsequent nation-building.",
      "Pacific Island nations' 21st-century climate vulnerability — Kiribati, Tuvalu, and Marshall Islands face total inundation from sea-level rise within decades — makes Oceania the first inhabited region to face displacement from anthropogenic climate change, making it central to global climate justice discourse."
    ],
    "relationships": [
      {"sourceSlug": "oceania", "sourceName": "Oceania", "verb": "CONTAINS", "targetSlug": "polynesian-navigation", "targetName": "Polynesian Navigation", "context": "The Polynesian navigation tradition — star charts, wave patterns, bird flight — enabled the settlement of every habitable Pacific island across 8,000 km of ocean, the most ambitious human migration project in prehistory."},
      {"sourceSlug": "oceania", "sourceName": "Oceania", "verb": "CONTAINS", "targetSlug": "aboriginal-australians", "targetName": "Aboriginal Australians", "context": "Aboriginal Australians have the world's oldest continuous cultural tradition — at least 65,000 years of occupation — representing an unbroken link to the first human settlement of Australia."},
      {"sourceSlug": "james-cook", "sourceName": "James Cook", "verb": "TRANSFORMS", "targetSlug": "oceania", "targetName": "Oceania", "context": "Cook's three Pacific voyages (1768–1779) comprehensively mapped Oceania for European knowledge and initiated the colonisation that would transform the region within a century."}
    ],
    "places": [
      {"name": "Australia", "role": "The largest land area of Oceania — a continent with 65,000 years of continuous human occupation, unique marsupial biodiversity, and the world's largest per-capita land mass for a developed nation"},
      {"name": "Hawaii, Pacific Ocean", "role": "The northernmost extremity of Polynesian settlement (600 CE) — the most geographically isolated inhabited archipelago on Earth, reached by Polynesian navigators crossing 3,200 km of open ocean"},
      {"name": "Easter Island (Rapa Nui), Pacific Ocean", "role": "The most remote inhabited island on Earth and site of the famous Moai statues — testimony to the extraordinary Polynesian achievement of settling the far corners of the Pacific"}
    ],
    "subjects": ["Geography", "Pacific History", "Indigenous History", "Navigation", "Environment", "Colonial History", "Climate Change", "Oceania"],
    "frameworks": ["LONGUE_DUREE", "POSTCOLONIAL_ANALYSIS", "ENVIRONMENTAL_HISTORY", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Oceania is the setting of the Polynesian navigation achievement — the most ambitious human migration in prehistory — and the home of Aboriginal Australians, who have the world's oldest continuous cultural tradition. In the 21st century, Pacific Island nations face the first existential displacement from anthropogenic climate change, making Oceania the frontline of the defining environmental crisis of our era.",
      "significanceCategory": "highly-significant"
    }
  }
},

"latin-america": {
  "filepath": "data/appwrite-export/entities/420-Class-420/420latin-america.json",
  "slug": "latin-america",
  "data": {
    "summary": "Latin America — loosely defined as the countries of the American continents where Spanish or Portuguese (Romance/Latin-derived) languages predominate — encompasses 20 nations from Mexico in the north to Argentina in the south, plus the Caribbean nations of Cuba, the Dominican Republic, Haiti, and others. Covering approximately 19.2 million km² with a population of 660 million, it is the world's most urbanised developing region (80% urban) and the most unequal region in terms of income distribution, with a Gini coefficient that consistently tops global rankings. The concept of 'Latin America' was popularised in the mid-19th century — partly as a French geopolitical formulation (under Napoleon III) to claim cultural kinship with the region against Anglo-Saxon American dominance.\n\nThe region's historical arc runs from the extraordinary pre-Columbian civilisations — Maya, Aztec, Inca, and dozens of smaller polities — through the Spanish and Portuguese colonial system (1492–1826) that was the primary site of the Atlantic slave trade (approximately 10 million enslaved Africans brought to Latin America, versus 400,000 to North America), to the 19th-century independence movements led by Bolívar, San Martín, Hidalgo, and Toussaint Louverture (Haiti, 1804 — the only successful slave revolt in history to produce an independent state). The 20th century saw Latin America as the primary arena of US Cold War interventionism: CIA-backed coups removed elected leaders in Guatemala (1954), Brazil (1964), Chile (1973), and supported authoritarian regimes across the region that collectively killed or 'disappeared' tens of thousands.\n\nThe 21st century brought the 'Pink Tide' — a wave of left-wing governments (Lula in Brazil 2002–2010 and 2022–present, Morales in Bolivia 2006–2019, Chávez in Venezuela 1999–2013, Correa in Ecuador 2007–2017, Kirchner in Argentina 2003–2015) — followed by a conservative backlash and then a second wave of left-wing victories. The region's ongoing challenges: extreme inequality (the richest 10% hold 55% of income), organised crime and drug cartel violence (Mexico, Central American Northern Triangle), climate vulnerability (Amazon deforestation, Caribbean hurricane intensification), and the legacy of colonial racial hierarchy.",
    "causes": [
      "Iberian colonialism's plantation and extractive economy — silver mining at Potosí, sugar at Saint-Domingue, cattle ranching in the Rio de la Plata — created the colonial structures of extreme inequality between white landowners, mixed-race intermediaries, Indigenous labourers, and enslaved Africans that persist in 21st-century Latin American class structure.",
      "The Monroe Doctrine (1823) and its 20th-century interventionist corollaries (the Platt Amendment, the Roosevelt Corollary) established the framework of US hegemony that shaped Latin American political history throughout the Cold War period.",
      "Latin America's extraordinary geographic diversity — tropical rainforest, Andean highlands, subtropical pampas, Caribbean islands — created the ecological base for the diversity of agricultural commodities (coffee, sugar, bananas, soybeans) that made the region the primary supplier of commodity agriculture to the global market."
    ],
    "effects": [
      "The Haitian Revolution (1791–1804) — the only successful slave revolt in history — created the world's first Black republic and inspired antislavery movements globally, while simultaneously generating a century of economic blockade and political isolation that locked Haiti into the perpetual poverty it continues to experience.",
      "The narcotics trade — cocaine (Colombia, Peru, Bolivia), marijuana and methamphetamine (Mexico) — routed through Latin America to the United States and Europe, has generated armed conflicts, state capture, and social violence that have killed hundreds of thousands and displaced millions, constituting the primary security challenge in the region.",
      "Lula's conditional cash transfer programme (Bolsa Família) in Brazil (2003–2010) lifted 28 million people out of poverty and became the global model for social protection programmes, demonstrating that economic growth and social inclusion could be achieved simultaneously in a developing economy."
    ],
    "relationships": [
      {"sourceSlug": "latin-america", "sourceName": "Latin America", "verb": "PRODUCES", "targetSlug": "haitian-revolution", "targetName": "Haitian Revolution", "context": "The Haitian Revolution (1791–1804) was the only successful slave revolt in history — creating the world's first Black republic and inspiring antislavery movements globally from within the Latin American colonial system."},
      {"sourceSlug": "simon-bolivar", "sourceName": "Simón Bolívar", "verb": "TRANSFORMS", "targetSlug": "latin-america", "targetName": "Latin America", "context": "Bolívar's liberation campaigns (1810–1825) created six independent republics and established the vision of Pan-American unity that remains a recurring political aspiration in the region."},
      {"sourceSlug": "latin-america", "sourceName": "Latin America", "verb": "INFLUENCES", "targetSlug": "liberation-theology", "targetName": "Liberation Theology", "context": "Liberation theology — the Catholic theological movement articulating God's 'preferential option for the poor' — emerged from Latin America's combination of extreme inequality, radical Catholic communities, and the influence of Vatican II."}
    ],
    "places": [
      {"name": "Mexico City, Mexico (Tenochtitlan)", "role": "Built on the site of the Aztec capital, Mexico City is Latin America's largest metropolitan area (22 million) and the cultural capital of Mexican and Mesoamerican civilisation"},
      {"name": "São Paulo, Brazil", "role": "Latin America's largest city (22 million) and economic engine — the hub of Brazilian industrialisation and the region's most complex multicultural society"},
      {"name": "Potosí, Bolivia", "role": "The colonial silver mining city that was, in the 16th–17th centuries, one of the world's largest cities — the engine of Spanish Empire wealth and the symbol of colonial extraction"}
    ],
    "subjects": ["Latin America", "Geography", "Colonial History", "Political History", "Indigenous History", "Economics", "Global History", "Caribbean"],
    "frameworks": ["POSTCOLONIAL_ANALYSIS", "WORLD_SYSTEMS", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Latin America is the world's most unequal region and the primary site of Iberian colonialism's long-term legacies — from the Atlantic slave trade to the plantation economy to 20th-century US Cold War interventionism. It produced the only successful slave revolution in history (Haiti 1804), the most significant 21st-century social-democratic governance experiments, and liberation theology — arguably the most influential 20th-century theological movement.",
      "significanceCategory": "world-changing"
    }
  }
},

"antarctica": {
  "filepath": "data/appwrite-export/entities/410-Class-410/410antarctica.json",
  "slug": "antarctica",
  "data": {
    "summary": "Antarctica is the world's fifth-largest continent — 14.2 million km² of land (98% covered by ice averaging 2.1 km deep), containing 70% of the world's fresh water in frozen form. The coldest, driest, and windiest continent on Earth, it is the only continent without a permanent human population and without any indigenous human history: no Homo sapiens ever reached Antarctica before the early 19th century, and the last continent to be discovered (the first confirmed sighting was in 1820). The Antarctic ice sheet, if fully melted, would raise global sea levels by approximately 60 metres — making it the most consequential ice mass for the future of human civilisation in a warming world.\n\nAntarctica's human history begins with the 'Heroic Age' of polar exploration (1897–1922): the Belgian Belgica expedition (1897), the British Discovery expedition under Robert Falcon Scott (1901–1904), Ernest Shackleton's Nimrod expedition (1907–1909) and his legendary Endurance voyage (1914–1917), and Roald Amundsen's Norwegian team reaching the South Pole on 14 December 1911 — thirty-four days before Scott's team, which perished on the return journey. The race to the South Pole was one of the defining episodes of early 20th-century nationalism and heroism, and Shackleton's Endurance survival — his entire crew of 28 rescued without a single fatality after 634 days stranded — remains the greatest survival story in exploration history.\n\nThe Antarctic Treaty System (1959, in force 1961) is one of the most successful international agreements in history: 54 nations have signed, and the treaty designates Antarctica as a scientific preserve, bans military activity and mineral extraction, and suspends all territorial claims for the treaty's duration. In the 21st century, Antarctica has become the primary site for climate science: ice core records provide a 800,000-year climate archive (the oldest continuous climate record on Earth), and the rate of Antarctic ice mass loss — accelerating dramatically since 2000 — is the most alarming leading indicator of the global climate crisis.",
    "causes": [
      "The Gondwana breakup (c. 34 million years ago) isolated Antarctica from the other southern continents, allowing the development of the Antarctic Circumpolar Current — the most powerful ocean current on Earth — which thermally isolated the continent and caused the formation of the permanent ice sheet.",
      "The late 19th-century imperial competition for geographic 'firsts' and territorial claims created the geopolitical pressure that motivated the Heroic Age expeditions — the race to the South Pole was inseparable from the nationalist competition among Britain, Norway, Germany, Belgium, and France.",
      "The post-World War II International Geophysical Year (1957–1958) — the first major international scientific collaboration of the Cold War — used Antarctica as its primary focus, generating the scientific community and international goodwill that enabled the Antarctic Treaty System."
    ],
    "effects": [
      "The Antarctic Treaty System (1959) established the principle of international governance of a non-sovereign territory for exclusively peaceful and scientific purposes — a model of multilateral resource management that has been applied to outer space (Outer Space Treaty, 1967) and the deep seabed.",
      "Antarctica's ice cores provide the most important archive of Earth's climate history: Vostok and EPICA ice cores record 800,000 years of CO₂ concentrations, temperature, and volcanic activity, providing the primary evidence base for understanding the relationship between greenhouse gases and global temperature.",
      "The accelerating loss of Antarctic ice mass — the West Antarctic Ice Sheet is considered potentially unstable at current warming levels — is the primary driver of worst-case sea level rise projections: a full collapse would raise global sea levels by 5–6 metres over centuries, threatening the majority of the world's coastal cities."
    ],
    "relationships": [
      {"sourceSlug": "antarctica", "sourceName": "Antarctica", "verb": "ENABLES", "targetSlug": "antarctic-treaty-system", "targetName": "Antarctic Treaty System", "context": "The Antarctic Treaty (1959) designated Antarctica as an international scientific preserve — the most successful multilateral governance agreement for a non-sovereign territory in history."},
      {"sourceSlug": "roald-amundsen", "sourceName": "Roald Amundsen", "verb": "OCCURS_IN", "targetSlug": "antarctica", "targetName": "Antarctica", "context": "Amundsen's Norwegian team reached the South Pole on 14 December 1911, beating Scott's British expedition by 34 days — the climax of the Heroic Age of Antarctic exploration."},
      {"sourceSlug": "antarctica", "sourceName": "Antarctica", "verb": "ENABLES", "targetSlug": "climate-science", "targetName": "Climate Science", "context": "Antarctica's 800,000-year ice core climate record is the primary evidence base for understanding the relationship between greenhouse gas concentrations and global temperature — the foundation of modern climate science."}
    ],
    "places": [
      {"name": "South Pole, Antarctica", "role": "Geographic destination of the Amundsen-Scott race (1911) and site of the Amundsen-Scott South Pole Station — the most remote continuously staffed research station on Earth"},
      {"name": "Vostok Station, East Antarctica", "role": "Soviet/Russian research station and site of the world's coldest recorded temperature (−89.2°C) and the EPICA/Vostok ice core drilling that provided 800,000 years of climate data"},
      {"name": "Elephant Island, Antarctica", "role": "Site of Shackleton's Endurance crew's survival camp (1916) — where 22 men waited 128 days while Shackleton crossed the Southern Ocean to South Georgia in an open boat to organise rescue"}
    ],
    "subjects": ["Geography", "Climate Science", "Exploration", "International Law", "Environment", "Polar History", "Science", "Global History"],
    "frameworks": ["ENVIRONMENTAL_HISTORY", "LONGUE_DUREE", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Antarctica is the world's last continent — discovered in 1820, with no human history before that. Its ice cores provide the primary 800,000-year climate record that underpins modern climate science. Its Antarctic Treaty System (1959) is the most successful international scientific governance agreement in history. And the future fate of its ice sheet is the primary variable in worst-case sea level rise projections that could reshape the world's coastlines.",
      "significanceCategory": "highly-significant"
    }
  }
},

"taras-fedorovych": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220taras-fedorovych.json",
  "slug": "taras-fedorovych",
  "data": {
    "summary": "Taras Fedorovych (died c. 1636), also known as Tryasyla ('Shaker'), was a Zaporozhian Cossack hetman who led the most militarily successful Cossack uprising against Polish-Lithuanian Commonwealth rule in the decade before the better-known Khmelnytsky Rebellion — an uprising that demonstrated the Cossacks' capacity to inflict serious military defeats on one of Europe's most powerful states and that further radicalised the Cossack community toward the full-scale revolt that would come under Bohdan Khmelnytsky in 1648. Fedorovych emerges from the historical record primarily in connection with the Cossack revolt of 1630, which he led after being passed over for registration in the official Cossack register — the formal Polish system of enrolling and compensating Cossack warriors — a grievance that encapsulated the broader Cossack political and social conflict with the Polish nobility.\n\nFedorovych's 1630 uprising achieved remarkable success: his Cossack forces defeated the Polish Crown Army at the Battle of Pereiaslav (April 1630), capturing the Polish hetman and demonstrating that the Cossacks, when united, could defeat the Commonwealth's regular forces in the field. The subsequent negotiations produced the Pereiaslav Agreement (June 1630), which temporarily expanded the Cossack register and acknowledged some Cossack demands — a significant concession from the Polish side and a precedent for the negotiations that would define Cossack-Polish relations for the next two decades. Fedorovych then served in the Commonwealth military against the Ottomans before disappearing from the historical record — likely dying in the early 1630s.\n\nFedorovych is a transitional figure in Cossack history: less celebrated than the earlier Sahaidachny or the later Khmelnytsky, but occupying the crucial middle ground of the 1620s–1630s when the Cossack movement was consolidating its military capacity, sharpening its political demands, and building the tradition of resistance that Khmelnytsky would channel into the Cossack-Polish War of 1648–1657.",
    "causes": [
      "The Polish-Lithuanian Commonwealth's Cossack register policy — which formally enrolled and paid only a limited number of Cossacks, leaving thousands of registered fighters outside the official system — created permanent structural grievance that fuelled recurring Cossack revolts throughout the first half of the 17th century.",
      "Fedorovych's personal exclusion from the register, combined with his military reputation and leadership qualities, gave him both the motivation and the following to launch the 1630 uprising — a pattern typical of Cossack revolt leadership where personal grievance combined with structural tension.",
      "The Ottoman-Polish conflict and the ongoing struggle with Crimean Tatars provided Cossack commanders like Fedorovych with military experience and tactical knowledge that made them genuinely formidable opponents of the Polish Crown Army."
    ],
    "effects": [
      "Fedorovych's 1630 military victory at Pereiaslav demonstrated that the Cossacks could defeat the Polish Crown Army in the field — a precedent that emboldened subsequent Cossack resistance and contributed to the growing sense among Cossack commanders that military autonomy was achievable.",
      "The Pereiaslav Agreement of 1630 temporarily expanded the Cossack register and acknowledged some Cossack political demands, establishing the pattern of post-revolt negotiation and partial concession that characterised Polish-Cossack relations until Khmelnytsky's revolt shattered the framework entirely.",
      "Fedorovych's revolt contributed to the radicalisation of the Cossack political consciousness in the 1630s — the decade in which the next generation of Cossack leaders (including the young Khmelnytsky) were forming their political outlook and military experience."
    ],
    "relationships": [
      {"sourceSlug": "taras-fedorovych", "sourceName": "Taras Fedorovych", "verb": "RESISTS", "targetSlug": "polish-lithuanian-commonwealth", "targetName": "Polish-Lithuanian Commonwealth", "context": "Fedorovych led the 1630 Cossack uprising against the Commonwealth — defeating the Crown Army at Pereiaslav and extracting the Pereiaslav Agreement expanding the Cossack register."},
      {"sourceSlug": "taras-fedorovych", "sourceName": "Taras Fedorovych", "verb": "PRECEDES", "targetSlug": "bohdan-khmelnytsky", "targetName": "Bohdan Khmelnytsky", "context": "Fedorovych's 1630 revolt was one of the major precedents that established the Cossack tradition of military resistance and negotiated autonomy that Khmelnytsky would radicalise into full-scale revolt in 1648."},
      {"sourceSlug": "cossack-hetmanate", "sourceName": "Cossack Hetmanate", "verb": "PRODUCES", "targetSlug": "taras-fedorovych", "targetName": "Taras Fedorovych", "context": "The Zaporozhian Host's political and military structure — including the hetman election and the register system — was the institutional framework within which Fedorovych's career and revolt were embedded."}
    ],
    "places": [
      {"name": "Pereiaslav, Ukraine", "role": "Site of Fedorovych's 1630 military victory over the Polish Crown Army — and the subsequent Pereiaslav Agreement that temporarily resolved the uprising"},
      {"name": "Zaporozhia, Ukraine", "role": "Heartland of the Zaporozhian Cossack Host that Fedorovych commanded — the semi-autonomous military frontier community below the Dnieper rapids"}
    ],
    "subjects": ["Early Modern History", "Ukraine", "Cossack History", "Poland", "Military History", "Early Modern Era", "Eastern Europe", "Political History"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "MILITARY_HISTORY"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Taras Fedorovych was the Cossack hetman whose 1630 victory at Pereiaslav demonstrated the Cossacks' capacity to defeat the Polish Crown Army — a military precedent that contributed to the radicalisation leading to Khmelnytsky's full-scale revolt of 1648 and the eventual creation of the Cossack Hetmanate. He represents the crucial transitional generation of Cossack military leadership.",
      "significanceCategory": "regional"
    }
  }
},

"ildibad": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221ildibad.json",
  "slug": "ildibad",
  "data": {
    "summary": "Ildibad (died 541 CE) was an Ostrogothic king of Italy who reigned for approximately one year (540–541 CE) during the most critical phase of the Byzantine-Gothic War — succeeding the captured Witigis as the Ostrogoths' military leader in the immediate aftermath of Justinian's general Belisarius's recapture of Ravenna. A nephew by marriage of the Visigothic king Theudis, Ildibad was a military commander of considerable ability who revived Ostrogothic resistance after the apparently decisive Byzantine victory, beginning the second phase of the Gothic War that would last another decade and devastate the Italian peninsula.\n\nIldibad's brief reign (roughly May 540 to May 541) accomplished more militarily than his limited time suggests. He defeated a Byzantine force at Treviso in early 541, demonstrating that Ostrogothic military capacity had survived Belisarius's campaigns and that Italy was far from pacified. This victory helped consolidate Gothic support around his leadership, reversing the demoralisation that had followed Witigis's surrender and setting the military foundation for his successor and nephew Totila's remarkable decade-long revival. Had Ildibad not been murdered by a Gothic chieftain (in a dispute over a personal slight, according to Procopius), he might have prosecuted the Gothic recovery that Totila accomplished.\n\nIldibad occupies an important structural position in the history of the Gothic Wars: the man who prevented the Ostrogothic collapse in the critical window between Witigis's fall and Totila's rise. Without Ildibad's one year of military stabilisation — winning the first Gothic victory over Justinian's forces since the war began — Totila might never have had a viable military base from which to launch his extraordinary counter-offensive. Ildibad thus represents the hidden hinge figure whose brief tenure enabled the decade of resistance that made the Byzantine reconquest of Italy the most destructive military campaign in the history of the peninsula before the 20th century.",
    "causes": [
      "Belisarius's recapture of Ravenna in May 540 and the capture of King Witigis created a leadership vacuum in the Ostrogothic resistance — Ildibad was chosen as king by the surviving Gothic military commanders in northern Italy who refused to accept Byzantine rule despite the fall of their capital.",
      "Ildibad's military reputation as a capable commander and his family connection to the Visigothic king Theudis gave him the political standing among the Goths to secure election as king at a moment when Ostrogothic morale and military capacity were at their nadir.",
      "Justinian's decision to recall Belisarius from Italy in 541 — partly due to court politics in Constantinople — removed the most capable Byzantine commander just as Ildibad was rebuilding Gothic resistance, creating the military opportunity that Ildibad and then Totila exploited."
    ],
    "effects": [
      "Ildibad's victory at Treviso (541) was the first Gothic military success since the war's early stages — demonstrating to the remaining Gothic warriors that Byzantine forces could be beaten and providing the military morale that enabled the subsequent Gothic revival under Totila.",
      "The continuity Ildibad maintained between Witigis's leadership and Totila's allowed the Ostrogothic resistance to survive the critical transition period — Totila succeeded Ildibad's brief successor Eraric and built directly on the military position Ildibad had reconstructed.",
      "Ildibad's brief reign, followed by Totila's decade-long counter-offensive (541–552), extended the Gothic Wars by an additional twelve years — transforming what appeared to be a rapid Byzantine reconquest into a twenty-year conflict that devastated the Italian population, destroyed the senatorial aristocracy, and broke the economic and demographic base of Italy for generations."
    ],
    "relationships": [
      {"sourceSlug": "ildibad", "sourceName": "Ildibad", "verb": "PRECEDES", "targetSlug": "totila", "targetName": "Totila", "context": "Ildibad's one-year kingship stabilised Ostrogothic resistance after Witigis's fall, providing the military foundation on which Totila built his remarkable ten-year counter-offensive against Byzantine Italy."},
      {"sourceSlug": "belisarius", "sourceName": "Belisarius", "verb": "CREATES", "targetSlug": "ildibad", "targetName": "Ildibad", "context": "Belisarius's capture of Ravenna and King Witigis in 540 created the leadership vacuum that produced Ildibad's election — the Gothic military commanders choosing a new king rather than accepting Byzantine rule."},
      {"sourceSlug": "gothic-wars", "sourceName": "Gothic Wars (535–554)", "verb": "CONTAINS", "targetSlug": "ildibad", "targetName": "Ildibad", "context": "Ildibad reigned during the pivotal transition phase of the Gothic Wars — the year between Belisarius's apparent victory (540) and Totila's counter-offensive (541) that extended the conflict by a decade."}
    ],
    "places": [
      {"name": "Northern Italy (Veneto)", "role": "Theatre of Ildibad's military activity — his Treviso victory demonstrated Gothic resilience after Belisarius's campaigns and initiated the second phase of the Gothic Wars"},
      {"name": "Ravenna, Italy", "role": "The Ostrogothic capital fallen to Belisarius in 540 — the loss that precipitated the Gothic crisis from which Ildibad was elected to lead recovery"}
    ],
    "subjects": ["Late Antiquity", "Byzantine History", "Gothic History", "Italy", "Military History", "Classical Era", "Ostrogoths", "Migration Period"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "MILITARY_HISTORY"],
    "historicalSignificance": {
      "significanceScore": 5,
      "significanceNarrative": "Ildibad was the transitional Ostrogothic king whose brief one-year reign (540–541) stabilised Gothic resistance after Belisarius's apparent final victory, enabling the Totila counter-offensive that extended the Gothic Wars by a decade. He is the hidden hinge figure who prevented Ostrogothic collapse in the critical window between Witigis's fall and Totila's rise.",
      "significanceCategory": "regional"
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
