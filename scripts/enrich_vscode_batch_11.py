#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 11 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: pomponio-cecci, johannes-despauterius, benin, quintus-minucius-thermus,
          vima-takto, association-of-southeast-asian-nations,
          ʻabd-al-wahhāb-ibn-ʻabd-al-raḥman, rudravarman
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-11-may2026"

ENRICHMENTS = {

"pomponio-cecci": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250pomponio-cecci.json",
  "slug": "pomponio-cecci",
  "data": {
    "summary": "Pomponio Cecci (c. 1480–1542) was an Italian Catholic preacher and ecclesiastic of the early 16th century — a religious figure active in Rome during the turbulent decades of the Italian Reformation and the pre-Tridentine church reform debates. Active in the period between the Fifth Lateran Council (1512–1517) and the Council of Trent (opened 1545), Pomponio Cecci represented the tradition of Italian Catholic preaching that attempted to address the spiritual and institutional crisis of the church from within — the current of Catholic reform that included figures like Gian Matteo Giberti, Gasparo Contarini, and the Oratory of Divine Love.\n\nThe early 16th-century Italian church that Pomponio Cecci inhabited was one of the most complex and contested religious environments in Christian history: Martin Luther's challenge (1517) had polarised the Latin church, the Sack of Rome (1527) had deeply shaken the papacy's prestige and confidence, and a generation of Italian clergy were confronting the question of whether Lutheranism's success reflected fundamental failures of Catholic pastoral care, preaching, and doctrine. The tradition of Catholic reform preaching — exemplified by figures associated with the reform circles of Venice, Brescia, and Rome — sought to address these concerns through evangelical poverty, doctrinal clarity, and improved preaching standards.\n\nCecci's career falls in the category of those Roman ecclesiastics who responded to the Reformation challenge by intensifying rather than abandoning the Catholic sacramental and institutional tradition. The preaching ministry — long the primary medium of popular religious education — was being transformed in the early 16th century by the printing press, which allowed sermons to circulate beyond their immediate audience, and by the challenge of Protestant preaching that used vernacular scripture as its primary instrument.",
    "causes": [
      "The crisis of the Roman church in the early 16th century — the Protestant Reformation's challenge to Catholic doctrine and practice, combined with the institutional scandals of the Borgia and Julius II papacies — created the urgent pastoral context in which preachers like Cecci operated, responding to the demand for renewed Catholic spiritual leadership.",
      "The tradition of mendicant preaching (Franciscan and Dominican) that had been the primary medium of popular Catholic religious instruction for three centuries provided the institutional and rhetorical framework within which Cecci's preaching ministry was conducted.",
      "Rome's role as the centre of Catholic institutional life in the early 16th century — attracting ecclesiastics, scholars, and reformers from across Italy and Europe — gave Cecci access to the reform networks and debates that shaped the Catholic response to Lutheranism."
    ],
    "effects": [
      "Pomponio Cecci was part of the generation of Italian Catholic preachers and reformers whose work contributed to the intellectual and spiritual foundations of the Counter-Reformation — the renewal of Catholic pastoral care, preaching standards, and doctrinal clarity that culminated in the Council of Trent (1545–1563).",
      "His religious activity in pre-Tridentine Rome contributed to the culture of Catholic reform preaching that sought to address the spiritual failures that had allowed Lutheranism to spread — the emphasis on pastoral care, doctrinal catechesis, and improved clerical standards.",
      "As a figure in the Roman Catholic ecclesiastical world of the 1510s–1540s, Cecci's career illustrates the diversity of Catholic responses to the Reformation challenge — the range of positions between full reform and rigid traditionalism that characterised Italian Catholic thought before Trent."
    ],
    "relationships": [
      {"sourceSlug": "pomponio-cecci", "sourceName": "Pomponio Cecci", "verb": "REPRESENTS", "targetSlug": "counter-reformation", "targetName": "Counter-Reformation", "context": "Cecci was part of the pre-Tridentine Italian Catholic reform movement — preachers and ecclesiastics whose work contributed to the intellectual foundations of the Counter-Reformation."},
      {"sourceSlug": "protestant-reformation", "sourceName": "Protestant Reformation", "verb": "CHALLENGES", "targetSlug": "pomponio-cecci", "targetName": "Pomponio Cecci", "context": "The Protestant Reformation's challenge to Catholic practice and doctrine created the pastoral crisis that Cecci's preaching ministry addressed — a representative of Catholic responses to the Lutheran challenge."},
      {"sourceSlug": "pomponio-cecci", "sourceName": "Pomponio Cecci", "verb": "ACTIVE_IN", "targetSlug": "rome-ecclesiastical-culture", "targetName": "Roman Ecclesiastical Culture", "context": "Cecci's career was centred in Rome — the institutional heart of Catholicism where the debates about church reform, doctrinal response to Protestantism, and preaching standards were most intensely contested."}
    ],
    "places": [
      {"name": "Rome, Italy", "role": "The centre of Cecci's ecclesiastical career — the hub of Catholic institutional life where the most intense debates about church reform and Protestant challenge were conducted"},
      {"name": "Italian Peninsula", "role": "The broader context of Cecci's religious world — early 16th-century Italy was the site of both the most sophisticated Catholic reform movements and the most acute vulnerability to Protestant ideas"}
    ],
    "subjects": ["Italian Church History", "Counter-Reformation", "Medieval Era", "Catholic Reform", "Italy", "Early Modern Religion", "Preaching", "Renaissance Religion"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 5,
      "significanceNarrative": "Pomponio Cecci was an Italian Catholic preacher active in pre-Tridentine Rome during the critical decades of the Reformation challenge (c. 1510–1542). His career represents the tradition of Catholic reform preaching that sought to address the spiritual failures exposed by Lutheranism — a tradition that contributed to the intellectual foundations of the Counter-Reformation and the Council of Trent.",
      "significanceCategory": "local"
    }
  }
},

"johannes-despauterius": {
  "filepath": "data/appwrite-export/entities/252-Class-252/252johannes-despauterius.json",
  "slug": "johannes-despauterius",
  "data": {
    "summary": "Johannes Despauterius (Jan van Pauteren; c. 1460–1520) was a Flemish humanist grammarian and educational reformer — one of the most influential Latin grammar textbook writers of the 16th century and one of the founding figures of humanist Latin education in northern Europe. His 'Commentarii Grammatici' (published in parts 1509–1514) became the standard Latin grammar reference in schools across the Low Countries, France, and the British Isles for much of the 16th century, replacing the medieval scholastic Latin grammars (particularly Alexander de Villedieu's 'Doctrinale', a 13th-century verse grammar) with a humanist text based on the usage of classical authors.\n\nDespauterius was born in Ninove (modern Belgium) and spent much of his career in Comines (modern Franco-Belgian border), where he was a schoolmaster. He corresponded with Erasmus — whose educational programme for reformed Latin learning ('De Copia', 'Colloquia') he shared — and his grammars were explicitly designed to replace the medieval Latin tradition with humanist classical standards. His works included not only the 'Commentarii Grammatici' but also 'De Arte Versificatoria' (on Latin prosody and verse composition), 'Syntaxis', and a collection of Latin epigrams and poems that served as models for students.\n\nDespauterius's significance in the history of education is substantial: his grammars were the primary vehicle through which the humanist reform of Latin instruction penetrated northern European schools in the first half of the 16th century. Erasmus praised his work; it was used in the schools of the Low Countries, in French colleges, and in English grammar schools (it was used at Eton and elsewhere in England). The pedagogical programme embodied in Despauterius — Latin learned from classical authors rather than medieval compilations, combined with systematic grammatical instruction — shaped the formal education of several generations of the northern European elite.",
    "causes": [
      "The northern European humanist movement — centred in the Low Countries and the Rhineland — created the demand for reformed Latin textbooks that would replace the medieval scholastic tradition with classical humanist standards, providing the intellectual context within which Despauterius produced his grammars.",
      "Erasmus's programme of educational reform — promoting classical Latin, improving textbook quality, and connecting grammar instruction to the reading of good Latin authors — created a receptive environment for Despauterius's humanist grammars, and Erasmus's praise was crucial to the rapid diffusion of Despauterius's work.",
      "The printing press's availability in the Low Countries by the early 16th century allowed Despauterius's grammars to be produced, reproduced, and distributed at scale across northern Europe — transforming what might have been a local schoolmaster's work into a major educational publication with continental reach."
    ],
    "effects": [
      "Despauterius's 'Commentarii Grammatici' displaced the medieval Latin grammars (particularly the 'Doctrinale' of Alexander de Villedieu) in northern European schools — replacing scholastic, verse-form grammar instruction with a humanist prose grammar based on classical usage.",
      "The generation of scholars educated on Despauterius's grammars — including many who received their formal Latin training in Low Countries schools, French colleges, and English grammar schools in the first half of the 16th century — had their foundational intellectual formation shaped by his humanist classical standard.",
      "Despauterius contributed to the broader humanist educational revolution that transformed European schooling in the 16th century — the shift from medieval scholastic Latin to classical humanist Latin that was the educational parallel to the theological and artistic transformations of the Renaissance."
    ],
    "relationships": [
      {"sourceSlug": "johannes-despauterius", "sourceName": "Johannes Despauterius", "verb": "REFORMS", "targetSlug": "latin-education", "targetName": "Latin Grammar Education", "context": "Despauterius's grammars replaced the medieval scholastic Latin tradition in northern European schools — the 'Commentarii Grammatici' became the standard humanist Latin grammar of the early 16th century."},
      {"sourceSlug": "erasmus", "sourceName": "Erasmus of Rotterdam", "verb": "SUPPORTS", "targetSlug": "johannes-despauterius", "targetName": "Johannes Despauterius", "context": "Erasmus praised Despauterius's grammatical work as part of the humanist reform of Latin education — an endorsement that significantly increased the diffusion and prestige of Despauterius's grammars."},
      {"sourceSlug": "northern-humanism", "sourceName": "Northern Renaissance Humanism", "verb": "PRODUCES", "targetSlug": "johannes-despauterius", "targetName": "Johannes Despauterius", "context": "Despauterius was a product of the northern European humanist movement — the reform of education, letters, and Latin culture that centred in the Low Countries, Rhineland, and northern France in the late 15th–early 16th centuries."}
    ],
    "places": [
      {"name": "Ninove, Flanders (modern Belgium)", "role": "Despauterius's birthplace — the Flemish intellectual milieu that produced many of the northern humanist scholars of the late 15th century"},
      {"name": "Comines (modern Franco-Belgian border)", "role": "Where Despauterius spent most of his career as a schoolmaster — the site of the practical pedagogical work that produced the grammars"}
    ],
    "subjects": ["Humanism", "Renaissance Education", "Medieval Era", "Latin Grammar", "Low Countries", "Northern Renaissance", "Early Modern Education", "Textbooks"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "CULTURAL_TRANSMISSION"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Johannes Despauterius was the Flemish humanist whose 'Commentarii Grammatici' (1509–1514) became the standard Latin grammar textbook in schools across the Low Countries, France, and England for much of the 16th century — replacing the medieval scholastic tradition with humanist classical standards. Praised by Erasmus and used at Eton, his grammars shaped the foundational Latin education of generations of the northern European intellectual elite.",
      "significanceCategory": "significant"
    }
  }
},

"benin": {
  "filepath": "data/appwrite-export/entities/430-Class-430/430benin.json",
  "slug": "benin",
  "data": {
    "summary": "Benin (Republic of Benin; formerly Dahomey) is a small West African nation on the Gulf of Guinea, bordered by Togo to the west, Nigeria to the east, and Burkina Faso and Niger to the north — with a narrow southern coastline on the Bight of Benin (part of the Gulf of Guinea). With an area of 114,763 km² and a population of approximately 13 million, Benin is one of West Africa's most historically significant small nations: the homeland of the ancient Kingdom of Dahomey, a major site of the transatlantic slave trade, the origin point of Vodun (Voodoo) religion that spread across the Atlantic to the Americas, and one of sub-Saharan Africa's significant democratic transitions of the post-Cold War era.\n\nThe territory of modern Benin was home to several pre-colonial kingdoms, most significantly the Kingdom of Dahomey (founded c. 1600, centred at Abomey), which became a significant regional power in the 17th–19th centuries. Dahomey was notable for its highly organised military, its corps of female warriors (the Agojie — source of the 'Dahomey Amazons' legend, a subject of modern popular culture), and its active participation in the transatlantic slave trade: the Kingdom of Dahomey was among West Africa's most significant suppliers of enslaved people to European slavers, raiding neighbouring peoples and selling captives at the coast. This history makes Dahomey a central site for understanding the African dimensions of the slave trade — not only as victim but as participant.\n\nFrance colonised the territory as 'Dahomey' in the 1890s–1900s (the defeat of the Dahomey Kingdom came in 1894). Independent as 'Dahomey' from 1960, the country renamed itself 'Benin' in 1975 (after the Bight of Benin). Benin's post-independence history included a period of socialist one-party rule (1972–1990) under Mathieu Kérékou before its celebrated democratic transition — the 1990 National Conference that produced a peaceful democratic constitution — which was a model for democratic transitions across sub-Saharan Africa in the early 1990s.",
    "causes": [
      "The geographic position of the Dahomey territory — on the coastal plain of the Gulf of Guinea, between the forest zone (suitable for agriculture and dense settlement) and the coast (providing access to Atlantic trade) — created the conditions for the Kingdom of Dahomey's emergence as a regional military and commercial power.",
      "The transatlantic slave trade's demand for African captives (17th–19th centuries) fundamentally shaped the Kingdom of Dahomey's political economy — the kingdom became one of West Africa's most active slave-trading states, building its military power partly on the proceeds of selling captives to European slavers.",
      "France's colonial conquest of Dahomey (1892–1894) — defeating the kingdom's military resistance including its famous female warriors — imposed the colonial administrative structure that became the framework of the modern Beninese state."
    ],
    "effects": [
      "The Kingdom of Dahomey's participation in the transatlantic slave trade was a significant factor in the forced migration of enslaved Africans to the Americas — particularly to Haiti, Brazil, and the Caribbean — and Vodun religion (which originated in the Dahomey region) spread with these enslaved populations to become a major religious tradition in the African diaspora.",
      "Benin's 1990 National Conference — a peaceful transition from single-party Marxist rule to multi-party democracy, engineered through a sovereign national conference model — became an influential template for democratic transitions across francophone Africa in the early 1990s.",
      "The Dahomey Amazons (Agojie) — the Kingdom of Dahomey's all-female military corps — became a subject of significant 21st-century popular and scholarly interest, particularly through the 2022 film 'The Woman King', contributing to global awareness of Benin's pre-colonial history."
    ],
    "relationships": [
      {"sourceSlug": "benin", "sourceName": "Benin (Republic)", "verb": "SUCCESSOR_TO", "targetSlug": "kingdom-of-dahomey", "targetName": "Kingdom of Dahomey", "context": "The modern Republic of Benin is the successor state to the Kingdom of Dahomey — the 17th–19th century West African kingdom whose history of slave trading and military culture defines much of modern Benin's historical significance."},
      {"sourceSlug": "transatlantic-slave-trade", "sourceName": "Transatlantic Slave Trade", "verb": "SHAPES", "targetSlug": "benin", "targetName": "Benin (Dahomey)", "context": "The Kingdom of Dahomey was one of West Africa's most active slave-trading states — its political economy was significantly built on the trade in enslaved captives sold to European slavers on the Slave Coast."},
      {"sourceSlug": "benin", "sourceName": "Benin (Republic)", "verb": "ORIGINATES", "targetSlug": "vodun-religion", "targetName": "Vodun (Voodoo) Religion", "context": "The Vodun religious tradition originated in the Dahomey/Benin region — spread across the Atlantic by enslaved Africans, it became a major religious tradition in Haiti, Brazil, and the African diaspora."}
    ],
    "places": [
      {"name": "Abomey, Benin", "role": "The capital of the historic Kingdom of Dahomey — the royal city whose palace complex (now a UNESCO World Heritage Site) represents the kingdom's pre-colonial civilisation"},
      {"name": "Cotonou, Benin", "role": "Benin's largest city and economic capital — the port city through which the slave trade passed and through which modern Beninese commercial life is organised"},
      {"name": "Gulf of Guinea / Bight of Benin", "role": "The coastal geography that defined Dahomey's Atlantic connection — the 'Slave Coast' where European slavers collected their human cargo"}
    ],
    "subjects": ["West Africa", "Dahomey History", "Contemporary Era", "Africa", "Atlantic Slavery", "Contemporary History", "African Diaspora", "Democratic Transition"],
    "frameworks": ["WORLD_SYSTEMS", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Benin (formerly Dahomey) is the successor state to the Kingdom of Dahomey — one of West Africa's most powerful pre-colonial kingdoms, a major participant in the transatlantic slave trade, the origin point of Vodun (Voodoo) religion, and notable for its Agojie female warrior corps. The modern Republic of Benin's 1990 democratic transition was an influential model for sub-Saharan Africa, and Dahomey's history has become a major subject of global interest through the lens of the African diaspora.",
      "significanceCategory": "significant"
    }
  }
},

"quintus-minucius-thermus": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220quintus-minucius-thermus.json",
  "slug": "quintus-minucius-thermus",
  "data": {
    "summary": "Quintus Minucius Thermus (fl. 200s BCE; consul 193 BCE; died c. 186 BCE) was a Roman Republican politician and military commander of the early 2nd century BCE — a praetor, consul, and general who participated in the Roman military campaigns of the Ligurian Wars and post-Hannibalic consolidation that extended Roman control over northern Italy. His career falls in the critical period of Roman expansion following the Second Punic War (218–201 BCE), when Rome was simultaneously absorbing the territories won from Carthage and Hannibal's Italian allies, pushing northward against the Ligurians of the Apennines and the Gallic tribes of the Po valley, and projecting power eastward into the Greek world (the Macedonian and Syrian Wars).\n\nQuintus Minucius Thermus served as praetor (probably c. 196 BCE) and was elected consul for the year 193 BCE — one of the two men who, according to Roman constitutional convention, held supreme civil and military authority in the Roman Republic. During his consulship he was assigned the province of Liguria, where the Roman legions were engaged in a prolonged pacification campaign against the Ligurian peoples of the northwestern Apennines — a low-intensity but persistent conflict that occupied numerous consuls throughout the first decades of the 2nd century BCE. His military operations in Liguria secured him a minor but recognised place in the Roman military record.\n\nAlthough Quintus Minucius Thermus is not among the major figures of Roman Republican history — his career lacks the dramatic scale of contemporaries like Scipio Africanus, Flamininus, or Marcus Porcius Cato — he represents the typical senior magistrate of the period: a member of the Roman political elite who moved through the standard career progression (cursus honorum), held military command in the active frontier zones, and contributed to the incremental expansion and consolidation of Roman power in northern Italy.",
    "causes": [
      "The Second Punic War's aftermath — the need to consolidate Roman control over northern Italy, subdue Hannibal's former Gallic and Ligurian allies, and absorb the territory seized from Carthage's supporters — created the military and political context in which Quintus Minucius Thermus's career unfolded.",
      "The Roman Republican cursus honorum — the standardised ladder of magistracies (quaestor, aedile, praetor, consul) through which the Roman political elite progressed — provided the institutional framework for Thermus's career, as for all Roman republican politicians of his generation.",
      "The Ligurian Wars — the prolonged conflict between Rome and the Ligurian peoples of the northwestern Apennines that continued through much of the 2nd century BCE — provided the theatre of military operations where Thermus exercised his consular military command."
    ],
    "effects": [
      "Quintus Minucius Thermus's consular military operations in Liguria (193 BCE) contributed to the incremental Roman pacification of northwestern Italy — a process that over several decades of successive consular campaigns transformed the Ligurian highlands from an active military frontier into a region integrated into the Roman system.",
      "His career is documented in Livy's 'Ab Urbe Condita' and other Roman annalistic sources, contributing to the historical record of the early 2nd century BCE Roman Republic — the period of rapid Mediterranean expansion whose documentation is essential for understanding Roman imperialism.",
      "As consul in 193 BCE, Thermus participated in the Roman governance of the post-Hannibalic period — the generation of Roman politicians who administered the expanding Republic during the critical decades of its transformation from Italian hegemon to Mediterranean superpower."
    ],
    "relationships": [
      {"sourceSlug": "quintus-minucius-thermus", "sourceName": "Quintus Minucius Thermus", "verb": "PARTICIPATES_IN", "targetSlug": "roman-republic", "targetName": "Roman Republic", "context": "Thermus was a consul of the Roman Republic (193 BCE) — one of the annual holders of supreme civil and military authority in the Republican constitutional system during the period of Roman Mediterranean expansion."},
      {"sourceSlug": "ligurian-wars", "sourceName": "Ligurian Wars", "verb": "SHAPES", "targetSlug": "quintus-minucius-thermus", "targetName": "Quintus Minucius Thermus", "context": "The prolonged Roman campaigns against the Ligurians of the northwestern Apennines provided the theatre of Thermus's consular military command in 193 BCE."},
      {"sourceSlug": "quintus-minucius-thermus", "sourceName": "Quintus Minucius Thermus", "verb": "REPRESENTS", "targetSlug": "roman-expansion-italy", "targetName": "Roman Expansion in Northern Italy", "context": "Thermus's consular campaigns in Liguria were part of the systematic Roman military pacification of northern Italy — the incremental extension of Roman control that followed the Second Punic War."}
    ],
    "places": [
      {"name": "Rome, Roman Republic", "role": "The political centre of Thermus's career — Rome where he held his magistracies, including the consulship of 193 BCE"},
      {"name": "Liguria, northern Italy", "role": "The theatre of Thermus's consular military command — the northwestern Apennine zone where Rome was conducting its prolonged pacification of the Ligurian peoples"}
    ],
    "subjects": ["Roman Republic", "Ancient Rome", "Classical Era", "Roman Military", "Italy", "2nd Century BCE", "Republican Rome", "Roman History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 4,
      "significanceNarrative": "Quintus Minucius Thermus was a Roman consul (193 BCE) who commanded Roman forces in the Ligurian Wars — a typical senior magistrate of the middle Roman Republic who participated in the incremental military consolidation of northern Italy. While not a major figure, his career is documented in Livy and represents the standard Roman consular military command of the post-Hannibalic period.",
      "significanceCategory": "local"
    }
  }
},

"vima-takto": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221vima-takto.json",
  "slug": "vima-takto",
  "data": {
    "summary": "Vima Takto (also Vema Taktu; fl. c. 80–100 CE) was an early Kushan Emperor — one of the rulers of the Kushan Empire during its formative period of consolidation in Bactria and northwestern India. He is attested primarily through coinage and, more significantly, through the Rabatak inscription (discovered 1993 near Rabatak, Afghanistan), a trilingual royal inscription issued by the Kushan emperor Kanishka I in which the genealogy of the Kushan royal house is recorded — naming Vima Takto as one of Kanishka's ancestors and predecessors.\n\nThe Rabatak inscription's genealogical evidence suggests that Vima Takto ruled the Kushan Empire approximately three to four generations before Kanishka I (whose reign is usually dated to c. 127–150 CE), placing Vima Takto's reign approximately in the late 1st century CE. His reign appears to have been a period of Kushan territorial expansion and consolidation — particularly the Kushan push into northwestern India (modern Pakistan and Afghanistan), which would characterise the reigns of his successors Vima Kadphises and Kanishka I. Coins attributed to Vima Takto show iconographic elements that indicate a ruler positioned at the cultural crossroads of Central Asian, Iranian, and Indian traditions — a characteristic feature of Kushan royal culture.\n\nThe Kushan Empire that Vima Takto helped to build and consolidate was one of the great crossroads empires of the ancient world — controlling the Silk Road routes between China, India, and the Mediterranean, patronising Buddhist art and architecture, and facilitating the transmission of Gandharan Buddhism northward into Central Asia and eventually to China. Vima Takto's reign, though poorly documented compared to Kanishka's, was part of the foundational Kushan state-building that made this cultural transmission possible.",
    "causes": [
      "The collapse of the Greco-Bactrian Kingdom (c. 120–135 BCE) and the subsequent migration of the Yuezhi peoples (of which the Kushans were one group) from the steppes into Bactria created the political vacuum that the Kushan clan gradually filled — Vima Takto's reign was part of the century-long process by which the Kushans consolidated control over Bactria and northwestern India.",
      "The Silk Road's commercial significance — making control of the Bactrian corridor an enormous economic asset — provided both the resources and the strategic incentive for the Kushan expansion that Vima Takto's reign advanced.",
      "The cultural pluralism of the Kushan ruling class — drawing on Greco-Bactrian, Iranian, and Indian cultural traditions simultaneously — allowed the Kushan kings to rule a diverse empire through flexible cultural and religious patronage, a policy Vima Takto embodied and continued."
    ],
    "effects": [
      "Vima Takto's consolidation of Kushan power in Bactria and northwestern India laid the territorial and institutional foundations for the great reigns of Vima Kadphises and Kanishka I — the rulers under whom the Kushan Empire reached its maximum extent and its greatest cultural and artistic achievements.",
      "The Kushan state-building process that Vima Takto's reign advanced ultimately created the political and commercial conditions for the Silk Road's peak functioning — the period of intense trade and cultural exchange between Rome, Persia, India, and China that characterised the 1st–3rd centuries CE.",
      "The Rabatak inscription's preservation of Vima Takto's name and genealogical position has been crucial for modern historians' reconstruction of early Kushan dynastic history — a rare documentary source in a period where Kushan chronology remains significantly contested."
    ],
    "relationships": [
      {"sourceSlug": "vima-takto", "sourceName": "Vima Takto", "verb": "PRECEDES", "targetSlug": "kanishka-i", "targetName": "Kanishka I", "context": "The Rabatak inscription issued by Kanishka I lists Vima Takto as one of his royal predecessors — placing Vima Takto approximately 3-4 generations before Kanishka in the Kushan dynastic succession."},
      {"sourceSlug": "vima-takto", "sourceName": "Vima Takto", "verb": "RULES", "targetSlug": "kushan-empire", "targetName": "Kushan Empire", "context": "Vima Takto was one of the formative rulers of the Kushan Empire — an early emperor whose reign was part of the Kushan expansion from Bactria into northwestern India."},
      {"sourceSlug": "silk-road", "sourceName": "Silk Road", "verb": "ENABLES", "targetSlug": "vima-takto", "targetName": "Vima Takto", "context": "The Silk Road's commercial routes through Bactria and northwestern India were the economic foundation of Kushan imperial power — the trade revenues that funded Vima Takto's court and military expansion."}
    ],
    "places": [
      {"name": "Bactria (modern Afghanistan/Uzbekistan/Tajikistan)", "role": "The heartland of the Kushan Empire and the base of Vima Takto's power — the ancient Bactrian plain that had been the cultural crossroads of Greek, Iranian, and Indian civilisations"},
      {"name": "Rabatak, Afghanistan", "role": "The site of the Rabatak inscription discovery — the crucial epigraphic source that names Vima Takto in the Kushan royal genealogy"}
    ],
    "subjects": ["Kushan Empire", "Central Asian History", "Classical Era", "Silk Road", "Ancient History", "Afghanistan", "Central Asia", "Ancient Empires"],
    "frameworks": ["WORLD_SYSTEMS", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Vima Takto was an early Kushan Emperor (c. 80–100 CE) whose reign was part of the foundational Kushan state-building that created the conditions for Kanishka I's great empire — the Silk Road crossroads power that facilitated the transmission of Gandharan Buddhism to China. He is primarily attested through the Rabatak inscription (discovered 1993), which placed him in the Kushan royal genealogy as a predecessor of Kanishka.",
      "significanceCategory": "regional"
    }
  }
},

"association-of-southeast-asian-nations": {
  "filepath": "data/appwrite-export/entities/010-Class-010/010association-of-southeast-asian-nations.json",
  "slug": "association-of-southeast-asian-nations",
  "data": {
    "summary": "The Association of Southeast Asian Nations (ASEAN) is a regional intergovernmental organisation founded on 8 August 1967 in Bangkok, Thailand — established by the Bangkok Declaration, signed by the five founding members: Indonesia, Malaysia, the Philippines, Singapore, and Thailand. As of 2024, ASEAN has ten member states (adding Brunei, Vietnam, Laos, Myanmar, and Cambodia over subsequent decades), with a combined population of approximately 680 million and a collective GDP of approximately $3.6 trillion — making it the third-largest economy in Asia and the fifth-largest in the world. ASEAN operates under the principle of non-interference in members' internal affairs and consensus-based decision-making — principles that reflect both Southeast Asian diplomatic traditions and the Cold War context of its founding.\n\nASEAN was founded in the context of the Cold War — specifically in the aftermath of the Indonesian communist coup attempt of 1965 (the September 30th Movement), the ongoing Vietnam War, and the general concern among non-communist Southeast Asian governments about regional stability and communist expansion. The founding members were all non-communist, and the organisation was partly designed to provide a framework for cooperation among the non-communist states of the region. However, ASEAN's explicit focus on economic cooperation and non-interference in political affairs distinguished it from more overtly political Cold War alliances like SEATO (Southeast Asia Treaty Organisation), which it effectively outlasted.\n\nOver its five decades, ASEAN has evolved from a modest Cold War regional arrangement into one of the world's most significant regional organisations — institutionalising the 'ASEAN Way' of dialogue and consensus, establishing the ASEAN Free Trade Area (AFTA, 1992), developing the ASEAN Community framework (political-security, economic, and socio-cultural pillars), and launching the Regional Comprehensive Economic Partnership (RCEP, 2022) — the world's largest free trade agreement by population and GDP covered. ASEAN has also become the nucleus of the broader 'ASEAN+3' framework engaging China, Japan, and South Korea, and the East Asia Summit engaging the major Indo-Pacific powers.",
    "causes": [
      "The Cold War's geopolitical pressures on Southeast Asia — particularly the Vietnam War, the 1965 Indonesian communist coup attempt, and the general threat of communist expansion — provided the immediate political context that brought five non-communist Southeast Asian governments together to establish ASEAN as a framework for regional stability and cooperation.",
      "The decolonisation of Southeast Asia (1945–1965) had created a set of newly independent states with urgent needs for economic development, political stabilisation, and the management of colonial-era border disputes — needs that ASEAN's regional cooperation framework was designed to address.",
      "The failure of earlier Southeast Asian regional organisations (particularly SEATO, which was explicitly Cold War and militarily oriented) to provide a durable framework for regional cooperation demonstrated the need for a more inclusive, non-interventionist organisation that could eventually accommodate all Southeast Asian states regardless of political system."
    ],
    "effects": [
      "ASEAN's 'ASEAN Way' — the principles of non-interference, consensus, and incremental dialogue — became the distinctive diplomatic style of Southeast Asian multilateralism, shaping how member states manage disputes and differences and creating a regional norm of peaceful conflict resolution.",
      "ASEAN's economic integration — from the ASEAN Free Trade Area (1992) through the ASEAN Economic Community (2015) to the Regional Comprehensive Economic Partnership (2022) — has been a significant driver of regional economic growth and integration, with Southeast Asia's combined economy becoming one of the world's largest.",
      "ASEAN's institutional development over 50+ years has created the frameworks (ASEAN+3, East Asia Summit, RCEP) that are the primary vehicles for broader Indo-Pacific regional architecture — making ASEAN 'centrality' a key concept in the geopolitics of the Asia-Pacific, particularly in the context of US-China competition."
    ],
    "relationships": [
      {"sourceSlug": "association-of-southeast-asian-nations", "sourceName": "ASEAN", "verb": "EMERGES_FROM", "targetSlug": "cold-war", "targetName": "Cold War", "context": "ASEAN was founded (1967) in direct response to Cold War pressures — particularly the Vietnam War and communist expansion concerns — providing a non-communist Southeast Asian regional framework."},
      {"sourceSlug": "association-of-southeast-asian-nations", "sourceName": "ASEAN", "verb": "ENABLES", "targetSlug": "asean-free-trade-area", "targetName": "ASEAN Free Trade Area (AFTA)", "context": "ASEAN's institutional development produced the ASEAN Free Trade Area (1992) — the first major step in Southeast Asian economic integration that has evolved into the ASEAN Economic Community and RCEP."},
      {"sourceSlug": "association-of-southeast-asian-nations", "sourceName": "ASEAN", "verb": "SHAPES", "targetSlug": "indo-pacific-geopolitics", "targetName": "Indo-Pacific Regional Architecture", "context": "ASEAN centrality — the principle that ASEAN is the hub of broader regional multilateral frameworks — has made ASEAN the organisational core of the Indo-Pacific regional architecture, including ASEAN+3, East Asia Summit, and RCEP."}
    ],
    "places": [
      {"name": "Bangkok, Thailand", "role": "The founding site of ASEAN (Bangkok Declaration, 8 August 1967) and the city whose name is associated with the organisation's establishment"},
      {"name": "Southeast Asia", "role": "ASEAN's geographic remit — the region whose ten sovereign states are ASEAN members and whose collective economic and political development ASEAN has shaped"},
      {"name": "Jakarta, Indonesia", "role": "Home of the ASEAN Secretariat — Indonesia is the largest ASEAN member and Jakarta has been the de facto centre of ASEAN institutional life since 1976"}
    ],
    "subjects": ["Southeast Asia", "Regional Organisation", "Contemporary Era", "Geopolitics", "East Asia", "Cold War", "Economic Integration", "International Relations"],
    "frameworks": ["WORLD_SYSTEMS", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "ASEAN is one of the world's most successful regional organisations — founded in 1967 amid Cold War pressures, it has evolved into the institutional hub of Southeast Asian and Indo-Pacific cooperation, with 680 million people and a $3.6 trillion economy. Its 'ASEAN Way' of non-interference and consensus has kept the peace among diverse member states, and its frameworks (AFTA, ASEAN Community, RCEP) have driven Southeast Asia's economic transformation into one of the world's fastest-growing regions.",
      "significanceCategory": "world-changing"
    }
  }
},

"ʻabd-al-wahhāb-ibn-ʻabd-al-raḥman": {
  "filepath": "data/appwrite-export/entities/204-Class-204/204ʻabd-al-wahhāb-ibn-ʻabd-al-raḥman.json",
  "slug": "ʻabd-al-wahhāb-ibn-ʻabd-al-raḥman",
  "data": {
    "summary": "ʻAbd al-Wahhāb ibn ʻAbd al-Raḥmān ibn Rustum (fl. late 8th century; died c. 784 CE) was the second imam of the Rustamid dynasty — the Ibadi Muslim imamate that ruled Tahert (modern Tiaret, Algeria) from approximately 776 CE until its destruction by the Fatimid Ismaili forces in 909 CE. The Rustamid imamate was one of the most important political expressions of Ibadi Islam — the surviving moderate branch of the Kharijite movement, which had rejected both the Umayyad and Alid claims to the caliphate and maintained that leadership of the Muslim community should be based on piety and community consent rather than tribal lineage or dynastic descent.\n\nThe Rustamid imamate was founded by ʻAbd al-Wahhāb's father, ʻAbd al-Raḥmān ibn Rustum, a Persian convert who had studied Ibadi theology in Basra (the centre of early Ibadi scholarship) and had come to North Africa as a scholar-teacher. After his father's death, ʻAbd al-Wahhāb inherited the imamate and governed the Rustamid state for approximately three decades — consolidating the administration, supporting Ibadi scholarly life, and maintaining the state's position amid the complex politics of post-Umayyad North Africa (where Aghlabid emirs ruled Tunisia on behalf of the Abbasid caliphate to the east, and the Idrisid kingdom controlled Morocco to the west).\n\nʻAbd al-Wahhāb's Rustamid imamate is historically significant as one of the few stable political expressions of Ibadi Islam in history — demonstrating that the Ibadi tradition of piety-based, non-dynastic governance could be institutionalised into a functioning state. The Rustamid period is celebrated in Ibadi tradition (particularly among the Ibadis of Oman and the Mzab valley of Algeria) as a golden age of Ibadi scholarship and governance. The imamate's destruction by the Fatimids in 909 CE ended the first phase of Ibadi political history in North Africa, but the Ibadi communities of the Mzab valley have preserved the Rustamid tradition into the present.",
    "causes": [
      "The Ibadi movement's theological commitment to non-dynastic governance — the principle that the imam should be chosen for piety and learning, not lineage — drove the establishment of the Rustamid imamate as an alternative to both Umayyad dynastic rule and the Alid claims that would produce Fatimid Shiism.",
      "The political fragmentation of the Maghreb in the late 8th century — following the collapse of effective Umayyad authority in North Africa and the emergence of multiple independent or semi-independent polities — created the space within which the Rustamid imamate could establish itself in the Algerian highlands.",
      "ʻAbd al-Wahhāb's personal scholarly prestige and administrative capability — the qualities that Ibadi theology required of a legitimate imam — enabled him to consolidate and govern the state that his father had founded, maintaining Rustamid authority amid the competing pressures of Aghlabid and Idrisid neighbours."
    ],
    "effects": [
      "ʻAbd al-Wahhāb's Rustamid imamate preserved and developed Ibadi scholarship in North Africa — creating an intellectual environment in which Ibadi law, theology, and history were systematised in ways that remain foundational for Ibadi communities in Oman, Zanzibar, and the Mzab valley today.",
      "The Rustamid state's relative stability and justice (as celebrated in Ibadi tradition) provided a model of Ibadi governance — the practical demonstration that a state organised on Ibadi principles of piety-based, non-dynastic rule could function effectively — that has remained an important reference in Ibadi political thought.",
      "The eventual destruction of the Rustamid imamate by the Fatimids (909 CE) contributed to the dispersal of North African Ibadi communities into the Mzab valley and the Jebel Nafusa of Libya, creating the isolated Ibadi communities that have preserved the tradition to the present."
    ],
    "relationships": [
      {"sourceSlug": "ʻabd-al-wahhāb-ibn-ʻabd-al-raḥman", "sourceName": "ʻAbd al-Wahhāb ibn ʻAbd al-Raḥmān", "verb": "LEADS", "targetSlug": "rustamid-imamate", "targetName": "Rustamid Imamate of Tahert", "context": "ʻAbd al-Wahhāb was the second imam of the Rustamid state (Tahert, Algeria) — the Ibadi imamate that he consolidated and governed for approximately three decades after his father's founding reign."},
      {"sourceSlug": "ibadi-islam", "sourceName": "Ibadi Islam", "verb": "PRODUCES", "targetSlug": "ʻabd-al-wahhāb-ibn-ʻabd-al-raḥman", "targetName": "ʻAbd al-Wahhāb", "context": "The Ibadi theological tradition — the moderate surviving branch of early Kharijism — produced the Rustamid imamate and its scholar-imam rulers, of whom ʻAbd al-Wahhāb was the paradigmatic example."},
      {"sourceSlug": "fatimid-caliphate", "sourceName": "Fatimid Caliphate", "verb": "DESTROYS", "targetSlug": "rustamid-imamate", "targetName": "Rustamid Imamate", "context": "The Fatimid Ismaili army destroyed the Rustamid imamate in 909 CE — ending the first phase of Ibadi political history in North Africa and dispersing the Ibadi communities into the Mzab and Jebel Nafusa."}
    ],
    "places": [
      {"name": "Tahert (modern Tiaret, Algeria)", "role": "Capital of the Rustamid imamate — the highland city that was the seat of ʻAbd al-Wahhāb's government and the centre of 8th–9th century Ibadi scholarship in North Africa"},
      {"name": "North Africa (Maghreb)", "role": "The broader context of the Rustamid imamate — the post-Umayyad Maghreb where multiple independent Muslim polities competed for regional dominance"}
    ],
    "subjects": ["Ibadi Islam", "North Africa", "Medieval Era", "Islamic History", "Algeria", "Medieval History", "Kharijite Movements", "Medieval Islamic States"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "ʻAbd al-Wahhāb ibn ʻAbd al-Raḥmān was the second imam of the Rustamid imamate (Tahert, Algeria) — one of the most important political expressions of Ibadi Islam, whose century-long existence (776–909 CE) preserved and developed Ibadi scholarship in North Africa. The Rustamid period is celebrated in Ibadi tradition as a golden age of governance and learning, and ʻAbd al-Wahhāb's consolidation of his father's state was central to that achievement.",
      "significanceCategory": "regional"
    }
  }
},

"rudravarman": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221rudravarman.json",
  "slug": "rudravarman",
  "data": {
    "summary": "Rudravarman (reigned c. 514–550 CE) was the last king of Funan — the ancient Southeast Asian kingdom that had dominated the Mekong delta region and the maritime trade routes of the Gulf of Thailand from approximately the 1st century CE until its absorption by the Khmer polity of Chenla in the mid-6th century. As the final ruler of what Chinese sources called 'Funan' (a Chinese transcription of a Mon-Khmer word for 'mountain', referring to the territory's sacred peak), Rudravarman presided over the decline and eventual transformation of the first major state in Southeast Asian history — a kingdom that had been one of the most significant maritime trading polities in the ancient Indian Ocean world.\n\nFunan's significance in Southeast Asian history derives from its role as the earliest documented state in mainland Southeast Asia — an Indianised kingdom that adopted Hindu and Buddhist religious traditions, Sanskrit language and epigraphy, and Indian commercial and administrative practices while remaining distinctively Southeast Asian in culture. From its capital at Vyadhapura (near modern Phnom Penh, Cambodia), Funan controlled the lucrative entrepôt trade between India and China — collecting port duties, hosting merchants, and serving as the commercial and cultural interface between the two great civilisations of Asia.\n\nRudravarman came to power through usurpation — according to Chinese sources, he killed his father Jayavarman II to seize the throne — and his reign was marked by increasing pressure from the rising Chenla kingdom to the north. He sent embassies to the Chinese emperor (535, 539 CE) seeking diplomatic recognition and support, and Chinese sources record his court as still functioning in Hindu-Buddhist syncretism characteristic of Funanese culture. By approximately 550 CE, Chenla had absorbed or supplanted Funan, and the kingdom that Rudravarman had ruled effectively disappeared as a political entity — though Funanese cultural and religious traditions survived in the Khmer civilisation that succeeded it.",
    "causes": [
      "The rise of the Chenla polity to the north of Funan — a Khmer-speaking kingdom that had been a vassal of Funan before asserting independence — created the primary political pressure that ended Funanese dominance of the Mekong delta region and ultimately absorbed Funan under or shortly after Rudravarman's reign.",
      "Rudravarman's contested succession — his usurpation of the throne by killing his father Jayavarman II — likely weakened the Funanese state by creating internal dynastic tensions and undermining the legitimacy of the royal line at precisely the moment when Chenla's challenge required maximum political cohesion.",
      "The long-term economic and demographic changes in the Mekong delta region — including shifts in maritime trade routes and the relative rise of the lower Mekong Khmer peoples — contributed to the structural weakening of Funanese power that made Rudravarman's kingdom vulnerable to the Chenla expansion."
    ],
    "effects": [
      "Rudravarman's reign as last king of Funan marked the end of the first major phase of mainland Southeast Asian state history — the disappearance of the Funanese political entity that had defined the region's international character for five centuries was replaced by the Khmer Chenla polity that eventually produced Angkor.",
      "Funanese cultural and religious traditions — Hindu-Buddhist syncretism, Sanskrit epigraphy, Indianised court culture — survived the political transition to Chenla and became foundational elements of Khmer civilisation, shaping the culture that produced the Angkor complex.",
      "Chinese diplomatic records of Rudravarman's embassies (535, 539 CE) are important sources for the history of late Funan — providing the primary evidence for the final phase of Funanese political life and contributing to historians' understanding of the transition from Funan to Chenla."
    ],
    "relationships": [
      {"sourceSlug": "rudravarman", "sourceName": "Rudravarman", "verb": "RULES", "targetSlug": "kingdom-of-funan", "targetName": "Kingdom of Funan", "context": "Rudravarman was the last king of Funan — the final ruler of the ancient Mekong delta kingdom before its absorption by the Khmer Chenla polity in the mid-6th century."},
      {"sourceSlug": "chenla", "sourceName": "Chenla (Khmer Kingdom)", "verb": "ABSORBS", "targetSlug": "rudravarman", "targetName": "Rudravarman's Funan", "context": "Chenla — the rising Khmer polity to the north of Funan — absorbed or supplanted Funan during or shortly after Rudravarman's reign, ending the first major phase of Southeast Asian state history."},
      {"sourceSlug": "rudravarman", "sourceName": "Rudravarman", "verb": "REPRESENTS", "targetSlug": "indianisation-southeast-asia", "targetName": "Indianisation of Southeast Asia", "context": "Funan under Rudravarman represented the mature Indianised court culture of early mainland Southeast Asia — Hindu-Buddhist syncretism, Sanskrit, and Indian administrative traditions adapted to the Mekong delta environment."}
    ],
    "places": [
      {"name": "Vyadhapura (near modern Phnom Penh, Cambodia)", "role": "The capital of the Kingdom of Funan — the sacred centre from which Rudravarman and his predecessors ruled the Mekong delta and its maritime trade routes"},
      {"name": "Mekong Delta, Southeast Asia", "role": "The heartland of Funanese power — the agricultural and commercial base of the kingdom whose control over the Gulf of Thailand and Mekong delta made it the dominant power of early mainland Southeast Asia"}
    ],
    "subjects": ["Funan Kingdom", "Southeast Asian History", "Classical Era", "Cambodia", "Khmer History", "Ancient History", "Mekong History", "Indianisation"],
    "frameworks": ["WORLD_SYSTEMS", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Rudravarman was the last king of Funan — the first major state in mainland Southeast Asian history, which had dominated the Mekong delta and Gulf of Thailand maritime trade for five centuries. His reign marked the end of the Funanese political entity as Chenla absorbed or supplanted it (c. 550 CE), but the Funanese cultural traditions of Hindu-Buddhist syncretism and Indianised court culture survived to shape Khmer civilisation and the Angkor complex.",
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
