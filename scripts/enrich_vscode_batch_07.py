#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 07 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: dong-zhongshu, snorri-thorfinnsson, antonio-joaquín-pérez-martínez,
          juan-margarit-i-pau, zhuansun-shi, justus-of-urgell,
          muḥammad-ibn-yūsuf-al-kindi, lupus-of-sens
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-07-may2026"

ENRICHMENTS = {

"dong-zhongshu": {
  "filepath": "data/appwrite-export/entities/210-Class-210/210dong-zhongshu.json",
  "slug": "dong-zhongshu",
  "data": {
    "summary": "Dong Zhongshu (董仲舒, c. 179–104 BCE) was the Han dynasty Confucian philosopher and political theorist whose memorial to Emperor Wu in 134 BCE resulted in the imperial adoption of Confucianism as the official state ideology of China — arguably the single most consequential act in the history of Chinese intellectual and political culture. A native of Guangchuan in Hebei, Dong Zhongshu studied under the 'Gongyang Commentary' tradition on the Spring and Autumn Annals (Chunqiu) and rose to become the foremost Confucian master of the early Han. His 'Three Recommendations' to Emperor Wu, responding to an imperial inquiry about governance, presented a comprehensive vision of the cosmos, human society, and political order that convinced the emperor to establish official academies (the Taixue) for Confucian learning and to appoint Confucian-trained scholars to bureaucratic positions — creating the examination-based meritocracy that would define Chinese government for two millennia.\n\nDong Zhongshu's philosophical achievement was the creation of a cosmological Confucianism: a synthesis that integrated Confucian ethics with Yin-Yang theory, the Five Phases (wuxing), and Heaven-Earth-Human correlative cosmology into a comprehensive framework in which the moral order of human society was continuous with the natural order of the cosmos. His central concept — that Heaven, Earth, and humanity form a single correlative system (tian-di-ren) — meant that good governance brought natural harmony (fine weather, abundant harvests), while tyranny produced portents and disasters. This 'responsiveness of Heaven to human action' (tianren ganying) gave Confucian scholars the theoretical legitimacy to critique imperial policy by interpreting natural disasters as signs of imperial moral failure — a framework that embedded a subtle check on imperial power within the ideology of imperial legitimacy.\n\nDong Zhongshu's 'Chunqiu Fanlu' ('Luxuriant Dew of the Spring and Autumn Annals') elaborated this cosmological Confucianism in 82 surviving chapters. His institutionalisation of Confucianism through the Han state examination system created the civil service meritocracy that, with modifications, governed China until the abolition of the imperial examination system in 1905 CE — a period of over 2,000 years — and whose echoes persist in the contemporary Chinese civil service examination system (公务员考试).",
    "causes": [
      "Emperor Wu of Han's consolidation of centralised imperial power required an ideological framework that legitimised the emperor's authority while providing a sophisticated administrative philosophy for governing a large agrarian empire — Dong Zhongshu's cosmological Confucianism provided exactly this synthesis.",
      "The Gongyang tradition's emphasis on moral-political interpretation of history (using the Spring and Autumn Annals as a repository of moral judgements rather than merely historical record) gave Dong Zhongshu the hermeneutic framework for his cosmological synthesis.",
      "The competing intellectual schools of the early Han (Huang-Lao Daoism, Legalism, Mohism, diverse Confucian schools) created both the incentive for Emperor Wu to choose an official state ideology and the intellectual competition that drove Dong Zhongshu to develop the most comprehensive and politically sophisticated version of Confucianism."
    ],
    "effects": [
      "Emperor Wu's adoption of Confucianism as state ideology (following Dong Zhongshu's recommendations in 134 BCE) established the principle that government officials should be selected on the basis of classical learning and moral cultivation — the foundation of the examination system that governed China for 2,000 years.",
      "Dong Zhongshu's cosmological framework — that natural disasters signal Heaven's response to imperial moral failure — gave Confucian scholars a theoretical basis for critiquing imperial policy that persisted as a structural feature of Chinese political culture throughout the imperial era.",
      "The state-sponsored Taixue (Imperial Academy) that followed Dong Zhongshu's recommendations became the institutional model for Chinese higher education that produced the trained Confucian literati who staffed the imperial bureaucracy — the class that for two millennia was the most socially prestigious in the world's largest civilisation."
    ],
    "relationships": [
      {"sourceSlug": "dong-zhongshu", "sourceName": "Dong Zhongshu", "verb": "INFLUENCES", "targetSlug": "emperor-wu-of-han", "targetName": "Emperor Wu of Han", "context": "Dong Zhongshu's 134 BCE memorial to Emperor Wu persuaded the emperor to adopt Confucianism as official state ideology — the most consequential act of imperial cultural policy in Chinese history."},
      {"sourceSlug": "dong-zhongshu", "sourceName": "Dong Zhongshu", "verb": "PRODUCES", "targetSlug": "chinese-civil-service-examination", "targetName": "Chinese Civil Service Examination", "context": "Dong Zhongshu's recommendations created the institutional foundation for the state examination system that selected officials by classical Confucian learning — a system that governed China for 2,000 years."},
      {"sourceSlug": "confucius", "sourceName": "Confucius", "verb": "INSPIRES", "targetSlug": "dong-zhongshu", "targetName": "Dong Zhongshu", "context": "Confucius's ethical teachings, interpreted through the Gongyang tradition on the Spring and Autumn Annals, provided the philosophical foundation that Dong Zhongshu developed into state Confucianism."},
      {"sourceSlug": "dong-zhongshu", "sourceName": "Dong Zhongshu", "verb": "DEFINES", "targetSlug": "chinese-confucianism", "targetName": "Chinese State Confucianism", "context": "Dong Zhongshu's cosmological synthesis — integrating Confucian ethics with Yin-Yang correlative cosmology — became the dominant form of Chinese state Confucianism from the Han dynasty through the late imperial period."}
    ],
    "places": [
      {"name": "Chang'an, China (Han capital)", "role": "Imperial capital where Dong Zhongshu presented his Three Recommendations to Emperor Wu and where the Taixue (Imperial Academy) was established"},
      {"name": "Guangchuan, Hebei Province, China", "role": "Dong Zhongshu's birthplace and home region, in the former Zhao kingdom territory of the Yellow River plain"}
    ],
    "subjects": ["Chinese Philosophy", "Confucianism", "Han Dynasty", "Classical Era", "Political Theory", "Education", "China", "Intellectual History"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Dong Zhongshu was the philosopher who institutionalised Confucianism as China's state ideology under Emperor Wu of Han (134 BCE) — the most consequential act of cultural policy in Chinese history. His recommendations created the examination-based civil service meritocracy that governed China for 2,000 years. His cosmological framework shaped Chinese political culture's understanding of the relationship between moral governance and natural order throughout the imperial era.",
      "significanceCategory": "world-changing"
    }
  }
},

"snorri-thorfinnsson": {
  "filepath": "data/appwrite-export/entities/290-Class-290/290snorri-thorfinnsson.json",
  "slug": "snorri-thorfinnsson",
  "data": {
    "summary": "Snorri Thorfinnsson (born c. 1004–1005 CE) was the first known European child born in the Americas — the son of the Norse explorer Thorfinn Karlsefni and Gudrid Thorbjarnardóttir, born during the Norse settlement at Vinland (likely in Newfoundland, Canada) approximately five centuries before Columbus's 1492 voyage. His birth is recorded in both the Saga of the Greenlanders and the Saga of Erik the Red, making him one of the best-documented individuals in the Norse sagas and a historically remarkable figure: the first person of European descent whose birth in the Americas can be attested by literary sources. Snorri's birth symbolises the brief Norse presence in North America that archaeology at L'Anse aux Meadows, Newfoundland (excavated 1960–1968, confirming the Vinland sagas as historically grounded) has corroborated.\n\nSnorri returned to Iceland with his parents after the Vinland settlement was abandoned — driven out by conflict with the indigenous Skraelings (likely Beothuk or Mi'kmaq peoples) and by the practical difficulties of maintaining a viable settlement at such extreme distance from the Norse homelands. He grew up in Iceland, became a respected figure, and according to later tradition was an ancestor of several prominent Icelandic bishops including Bishop Brandr Sæmundarson. The saga record is notably specific about his birth: 'That winter Gudrid gave birth to a boy, and the boy was called Snorri' — a detail that the saga authors preserved because they understood its historical novelty.\n\nSnorri's historical significance lies less in any personal accomplishment than in what his birth represents: the brief Norse engagement with the Americas circa 1000–1025 CE, which preceded permanent European contact by five centuries and which demonstrates that the peoples of the Americas and Europe were not in complete isolation from each other before 1492. The Norse Vinland settlements — however short-lived — represent the first sustained European presence in the Americas and Snorri's birth is the most poignant human detail of that episode.",
    "causes": [
      "Leif Eriksson's accidental sighting of Vinland (c. 1000 CE) and subsequent successful voyage to North America created the knowledge and the precedent that motivated Thorfinn Karlsefni's more ambitious colonisation attempt — the expedition on which Snorri was born.",
      "Gudrid Thorbjarnardóttir's marriage to Thorfinn Karlsefni and her decision to accompany him on the Vinland voyage — an unusual choice for a woman of her social standing — placed her in the right place for Snorri to be born as the first recorded European child in the Americas.",
      "The Norse expansion across the North Atlantic — Iceland (874 CE), Greenland (985 CE), Vinland (c. 1000 CE) — was driven by the combination of Norse navigational technology (the knarr longship), knowledge of Atlantic wind patterns, and the social pressure of land scarcity in Norway, creating the chain that eventually brought Norse settlers to the coast of North America."
    ],
    "effects": [
      "Snorri's birth was recorded in the sagas as a significant event — evidence that the saga authors understood the novelty of European birth in the Americas and preserved it as historically important, contributing to the narrative tradition that eventually (via the sagas' survival in Iceland) provided evidence for the Norse Vinland settlements that archaeology confirmed in the 1960s.",
      "The Vinland settlement's failure — of which Snorri's return to Iceland was a part — represented the Norse withdrawal from North America that left the continent to its indigenous peoples for another five centuries before permanent European contact, fundamentally altering the timeline of the Americas' encounter with Old World civilisation.",
      "Snorri's descendants included several prominent Icelandic bishops, suggesting that his birth in the Americas was remembered and transmitted within Icelandic genealogical tradition as a notable distinction — an early example of transatlantic heritage consciousness."
    ],
    "relationships": [
      {"sourceSlug": "snorri-thorfinnsson", "sourceName": "Snorri Thorfinnsson", "verb": "OCCURS_IN", "targetSlug": "vinland-settlement", "targetName": "Vinland Settlement", "context": "Snorri was born during the Norse Vinland settlement of c. 1004–1005 CE — the Norse attempt to colonise North America that represents the first European presence in the Americas."},
      {"sourceSlug": "thorfinn-karlsefni", "sourceName": "Thorfinn Karlsefni", "verb": "FATHERS", "targetSlug": "snorri-thorfinnsson", "targetName": "Snorri Thorfinnsson", "context": "Thorfinn Karlsefni led the Vinland colonisation expedition and was Snorri's father — the Norse explorer whose voyage provided the setting for the first recorded European birth in the Americas."},
      {"sourceSlug": "gudrid-thorbjarnardottir", "sourceName": "Gudrid Thorbjarnardóttir", "verb": "MOTHERS", "targetSlug": "snorri-thorfinnsson", "targetName": "Snorri Thorfinnsson", "context": "Gudrid, who had previously survived a Greenland winter at Brattahlid, accompanied her husband Thorfinn to Vinland and bore Snorri — one of the most travelled women in early medieval Norse history."},
      {"sourceSlug": "lanse-aux-meadows", "sourceName": "L'Anse aux Meadows", "verb": "DOCUMENTS", "targetSlug": "snorri-thorfinnsson", "targetName": "Snorri Thorfinnsson", "context": "The archaeological site at L'Anse aux Meadows, Newfoundland — excavated by Helge and Anne Stine Ingstad (1960–1968) — corroborated the saga accounts of Vinland, confirming the historical context of Snorri's birth."}
    ],
    "places": [
      {"name": "Vinland (Newfoundland, Canada)", "role": "The Norse settlement where Snorri was born — likely in the L'Anse aux Meadows area of northern Newfoundland, the first recorded European birthplace in the Americas"},
      {"name": "Iceland", "role": "Where Snorri grew up after the Vinland settlement was abandoned — the source of the saga tradition that preserved the record of his American birth"}
    ],
    "subjects": ["Norse History", "Medieval History", "North America", "Exploration", "Medieval Era", "Indigenous History", "Atlantic History", "Sagas"],
    "frameworks": ["CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Snorri Thorfinnsson was the first European known to have been born in the Americas — born at the Norse Vinland settlement c. 1004–1005 CE, nearly five centuries before Columbus. His birth represents the brief but historically significant Norse presence in North America that archaeology confirmed at L'Anse aux Meadows in the 1960s. He is the most humanly vivid detail of the Norse Americas episode.",
      "significanceCategory": "significant"
    }
  }
},

"antonio-joaquín-pérez-martínez": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220antonio-joaquín-pérez-martínez.json",
  "slug": "antonio-joaquín-pérez-martínez",
  "data": {
    "summary": "Antonio Joaquín Pérez Martínez (1763–1829) was a Spanish-born Catholic bishop, delegate to the Spanish Cortes of Cádiz, and one of the signatories of the Mexican Declaration of Independence of 1821 — a man whose career traced one of the most dramatic political arcs of the independence era: from royalist delegate defending Spanish constitutionalism in the Cortes of Cádiz (1810–1814) to bishop who signed Mexico's independence from the Spain he had so recently defended. He served as Bishop of Puebla (the second most important diocese in New Spain) from 1814 to his death, wielding enormous institutional and moral influence over the most populous region of colonial Mexico during the critical decade of the independence wars.\n\nPérez Martínez was a delegate to the Cortes of Cádiz — the liberal-constitutionalist parliamentary assembly convened in 1810 to govern Spain during Napoleon's occupation — representing New Spain (Mexico) in the sessions that produced the Constitution of 1812, one of the most liberal constitutional documents of the early 19th century. His participation placed him within the Ilustrado (Enlightenment) tradition of Spanish liberalism and gave him deep knowledge of constitutional politics. On his return to Mexico as Bishop of Puebla, he initially supported royalist resistance to the insurgency, but by 1821 — as Agustín de Iturbide's Plan of Iguala created the political framework for a consensus independence — Pérez Martínez joined the movement and signed the Solemn Act of the Declaration of Independence of the Mexican Empire on 28 September 1821.\n\nHis significance lies in representing the crucial ecclesiastical legitimation of Mexican independence: a sitting bishop of the most senior diocese signing the declaration carried enormous moral authority in a deeply Catholic society and demonstrated that the Mexican Church — not merely insurgent leaders or creole elites — endorsed independence. His career embodies the transition from the colonial order to the new Mexican state.",
    "causes": [
      "The Cortes of Cádiz (1810–1814) and the Constitution of 1812 created the political formation that shaped Pérez Martínez's constitutionalist thinking — the liberal tradition of Spanish governance that informed his subsequent navigation of New Spain's transition to independence.",
      "The Plan of Iguala (1821), which united royalists, insurgents, and the Church around a conservative independence that would maintain the Church's privileges and social order, provided the political framework within which a conservative bishop like Pérez Martínez could endorse independence without abandoning his institutional interests.",
      "The Mexican Church's strategic calculation — that independence under conservative elites was preferable to continued Spanish rule under the liberal Constitutionalists who had suppressed Church privileges — motivated episcopal support for the Iguala coalition that produced independence."
    ],
    "effects": [
      "Pérez Martínez's signature on the 1821 Mexican Declaration of Independence provided the Catholic Church's institutional legitimation of the new state — crucial in a society where episcopal authority carried enormous moral weight and where the Church controlled 50% of Mexico's productive land.",
      "His subsequent episcopate in Puebla (1821–1829) shaped the early Mexican Church's relationship with the new state — a relationship of uneasy accommodation in which the Church preserved its privileges from the colonial era even as the new republic's political culture moved toward liberalism.",
      "As a representative figure of the criollo and ecclesiastical elite who endorsed independence, Pérez Martínez exemplifies the conservative social character of Mexican independence — an independence that changed political sovereignty without fundamentally altering social hierarchy, setting the stage for the Reform Wars (1858–1861) that would definitively separate Church and state."
    ],
    "relationships": [
      {"sourceSlug": "antonio-joaquín-pérez-martínez", "sourceName": "Antonio Pérez Martínez", "verb": "SIGNS", "targetSlug": "mexican-independence", "targetName": "Mexican Declaration of Independence (1821)", "context": "Pérez Martínez signed the Solemn Act of Mexican Independence on 28 September 1821 — providing crucial ecclesiastical legitimation for the new state in a deeply Catholic society."},
      {"sourceSlug": "antonio-joaquín-pérez-martínez", "sourceName": "Antonio Pérez Martínez", "verb": "OCCURS_IN", "targetSlug": "cortes-of-cadiz", "targetName": "Cortes of Cádiz (1810–1814)", "context": "Pérez Martínez represented New Spain at the liberal Cortes of Cádiz that produced the Spanish Constitution of 1812 — giving him constitutional political formation that shaped his subsequent career."},
      {"sourceSlug": "plan-of-iguala", "sourceName": "Plan of Iguala", "verb": "ENABLES", "targetSlug": "antonio-joaquín-pérez-martínez", "targetName": "Antonio Pérez Martínez", "context": "The Plan of Iguala's guarantee of Church privileges made endorsing independence compatible with Pérez Martínez's institutional interests as Bishop of Puebla."}
    ],
    "places": [
      {"name": "Puebla, Mexico", "role": "Diocese of which Pérez Martínez was bishop (1814–1829) — the second most important Catholic see in New Spain and the base of his enormous institutional influence"},
      {"name": "Cádiz, Spain", "role": "Site of the Cortes where Pérez Martínez served as delegate (1810–1814) — the constitutional assembly that shaped his political formation"}
    ],
    "subjects": ["Mexican Independence", "Early Modern History", "Latin America", "Church History", "Early Modern Era", "Mexico", "Spain", "Constitutional History"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Antonio Pérez Martínez was the Bishop of Puebla who signed Mexico's 1821 Declaration of Independence — providing the Catholic Church's institutional endorsement of the new state at a moment when episcopal authority carried decisive moral weight in Mexican society. His signature exemplifies the conservative social character of Mexican independence: an ecclesiastical elite that changed political sovereignty without transforming social hierarchy.",
      "significanceCategory": "significant"
    }
  }
},

"juan-margarit-i-pau": {
  "filepath": "data/appwrite-export/entities/205-Class-205/205juan-margarit-i-pau.json",
  "slug": "juan-margarit-i-pau",
  "data": {
    "summary": "Juan Margarit i Pau (c. 1422–1484) was a Catalan bishop, humanist scholar, and one of the first significant figures of the Renaissance in the Crown of Aragon — a man who combined an active career in ecclesiastical politics and royal diplomacy with a deep engagement with Italian humanism and a pioneering interest in Spanish antiquity. Born in Girona, Margarit studied canon law and cultivated humanist learning at a time when the Italian Renaissance was beginning to diffuse into the Iberian Peninsula. He served as Bishop of Elna and then Bishop of Girona, and was appointed Cardinal by Pope Innocent VIII in 1483 — one of the first Catalan cardinals and a recognition of his exceptional standing in the Spanish Church.\n\nMargarit's most significant intellectual contribution was his 'Paralipomenon Hispaniae' (c. 1484) — a humanist history of pre-Roman and Roman Spain that was one of the first major works of Spanish historiography in the Renaissance tradition. Drawing on classical sources, epigraphic evidence, and systematic geographical observation, the 'Paralipomenon' attempted to reconstruct the history of Hispania from its earliest inhabitants through the Roman conquest, applying the philological and antiquarian methods of Italian humanism to Spanish history. The work was deeply influenced by his acquaintance with Italian humanist historians and represented a new model of historical scholarship in the Iberian Peninsula — moving from the medieval chronicle tradition toward the humanist 'historia' genre that grounded historical narrative in documentary and material evidence.\n\nMargarit was also a significant political figure in the turbulent politics of Catalonia. He navigated the Catalan Civil War (1462–1472) — in which the Catalan nobility and urban elites rose against King John II of Aragon — with considerable diplomatic skill, maintaining relationships with multiple parties. His relationship with the young Ferdinand (later Ferdinand II of Aragon, the 'Catholic King' who co-founded the Spanish state with Isabella) placed him at the intersection of late medieval Catalan politics and the emerging Spanish monarchy.",
    "causes": [
      "The Italian Renaissance diffusion into the Iberian Peninsula through trade, diplomatic contacts, and the presence of Italian humanists at Aragonese courts created the intellectual environment in which Margarit absorbed and applied humanist methods to Spanish history.",
      "The political turbulence of Catalonia during the reign of John II (including the Catalan Civil War 1462–1472) required the Church to navigate complex loyalties, giving Margarit the diplomatic experience and royal contacts that complemented his scholarly career.",
      "Margarit's proximity to the Aragonese court and later his relationship with Ferdinand allowed him access to resources, political protection, and the network of diplomatic contacts in Italy that facilitated his humanist scholarly programme."
    ],
    "effects": [
      "The 'Paralipomenon Hispaniae' was one of the earliest humanist histories of Spain — it influenced subsequent generations of Spanish antiquarians and historians and represents the first systematic application of humanist philological methods to the reconstruction of pre-Roman Iberian history.",
      "Margarit's cardinalship (1483) raised the profile of Catalan and Spanish Church figures in the Roman curia at a critical moment — just before the establishment of the Spanish Inquisition (1480) and the completion of the Reconquista (1492) transformed the Spanish Church's relationship with Rome.",
      "As a cultural bridge between Italian humanism and the emerging Spanish state, Margarit exemplified the generation of Catalan-Aragonese scholars who began the process of Spanish Renaissance cultural formation — creating the context for the later flowering of Spanish Renaissance scholarship in the 16th century."
    ],
    "relationships": [
      {"sourceSlug": "juan-margarit-i-pau", "sourceName": "Juan Margarit i Pau", "verb": "PRODUCES", "targetSlug": "paralipomenon-hispaniae", "targetName": "Paralipomenon Hispaniae", "context": "Margarit's 'Paralipomenon Hispaniae' (c. 1484) was one of the first humanist histories of Spain — applying Italian Renaissance philological methods to the reconstruction of pre-Roman Iberian history."},
      {"sourceSlug": "italian-renaissance", "sourceName": "Italian Renaissance", "verb": "INFLUENCES", "targetSlug": "juan-margarit-i-pau", "targetName": "Juan Margarit i Pau", "context": "Margarit absorbed humanist methods and the 'historia' genre from Italian Renaissance historiography, applying them to Spanish antiquity and making him a pioneer of Renaissance scholarship on the Iberian Peninsula."},
      {"sourceSlug": "ferdinand-ii-of-aragon", "sourceName": "Ferdinand II of Aragon", "verb": "EMPLOYS", "targetSlug": "juan-margarit-i-pau", "targetName": "Juan Margarit i Pau", "context": "Margarit's relationship with the young Ferdinand of Aragon placed him at the nexus of late medieval Catalan politics and the emerging Spanish monarchy."}
    ],
    "places": [
      {"name": "Girona, Catalonia, Spain", "role": "Margarit's birthplace and episcopal see — the Catalan context of his political and ecclesiastical career"},
      {"name": "Rome, Italy", "role": "Site of the Roman curia where Margarit received the cardinalship (1483) and maintained the Italian humanist contacts that informed his scholarship"}
    ],
    "subjects": ["Renaissance Humanism", "Medieval History", "Spain", "Catalonia", "Historiography", "Medieval Era", "Church History", "Intellectual History"],
    "frameworks": ["CULTURAL_TRANSMISSION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Juan Margarit i Pau was one of the first figures of the Renaissance in the Crown of Aragon — a humanist bishop whose 'Paralipomenon Hispaniae' applied Italian Renaissance philological methods to Spanish antiquity, pioneering humanist historiography on the Iberian Peninsula. His cardinalship and close relationship with Ferdinand of Aragon placed him at the nexus of late medieval Catalan politics and the emerging Spanish state.",
      "significanceCategory": "significant"
    }
  }
},

"zhuansun-shi": {
  "filepath": "data/appwrite-export/entities/210-Class-210/210zhuansun-shi.json",
  "slug": "zhuansun-shi",
  "data": {
    "summary": "Zhuansun Shi (顓孫師, c. 503–450 BCE), better known by his courtesy name Zizhang (子張), was one of Confucius's most prominent disciples and a member of the inner circle of 'Ten Philosophers' (Shi zhe) whose teachings were considered authoritative in the early Confucian tradition. Born in Chen (modern Henan Province) of the state of Chen — one of the smaller Zhou feudal states — Zizhang was drawn to Confucius's circle and became known as one of the most dynamic and socially ambitious of the disciples, with a particular interest in practical official service and the question of how a person of virtue should conduct themselves in public life. Confucius described him as 'biased toward what is excessive' — high praise and mild caution combined — acknowledging both his exceptional qualities and his tendency toward over-extension.\n\nZizhang's recorded conversations in the Analects reveal a disciple primarily interested in the relationship between moral cultivation and social advancement — a fundamentally practical orientation toward Confucian ethics. His famous question 'What must a scholar do to be called distinguished?' provoked Confucius's distinction between genuine virtue (being consistently genuine while adjusting to context) and the mere appearance of virtue (looking virtuous without the substance) — one of the most important Confucian discussions of authenticity versus performance. Zizhang also raised questions about serving rulers of doubtful legitimacy, governance in difficult times, and the relationship between learning and political service — the practical concerns of a man who intended to enter political life.\n\nAfter Confucius's death, Zizhang established his own school — the Zizhang school of Confucianism — which is mentioned in the 'Xunzi' alongside other post-Confucian schools as a recognisable intellectual tradition. The Analects also credit him with the teaching that a gentleman 'holds fast to virtue in the face of danger, thinks of righteousness in the face of gain, thinks of respect in sacrificing, and thinks of grief in mourning' — a formulation that became one of the most quoted Confucian moral maxims. His posthumous recognition as one of the Ten Philosophers placed his image in Confucian temples across East Asia for two thousand years.",
    "causes": [
      "Zizhang's origin in the small feudal state of Chen — caught between the great powers of Qi, Chu, and Jin — gave him the perspective of a man from the political periphery who had learned the importance of virtue and competence as resources that could transcend the limitations of birth and political circumstance.",
      "Confucius's teaching method of responding to individual students' questions according to their particular characters and concerns — what the Analects calls teaching 'according to the student's capacity' — created the distinctive body of individual conversations that defined Zizhang's profile in the canon.",
      "The post-Confucian fragmentation of the school into competing interpretive traditions (the 'eight schools of Confucianism' mentioned in Han sources) provided the context in which Zizhang's distinctive emphasis on practical social conduct developed into an independent intellectual current."
    ],
    "effects": [
      "The Zizhang school of Confucianism — however short-lived as an independent tradition — contributed to the diversity of early Confucian interpretation and preserved a body of conversations that emphasised the practical relationship between virtue and social conduct.",
      "Zizhang's posthumous canonisation as one of the Ten Philosophers placed him among the most venerated figures in the Confucian tradition, with his effigy worshipped in Confucian temples across China, Korea, Japan, and Vietnam throughout the imperial period.",
      "His Analects conversations about the relationship between virtue and appearance contributed to a theme — the gap between genuine moral character and social performance — that became central to both Confucian and Daoist moral philosophy and remained relevant to Chinese intellectual discourse across two millennia."
    ],
    "relationships": [
      {"sourceSlug": "confucius", "sourceName": "Confucius", "verb": "TEACHES", "targetSlug": "zhuansun-shi", "targetName": "Zhuansun Shi (Zizhang)", "context": "Confucius taught Zizhang as one of his Ten Philosophers, describing him as 'biased toward what is excessive' and engaging with his practical questions about virtue, official service, and social conduct."},
      {"sourceSlug": "zhuansun-shi", "sourceName": "Zizhang", "verb": "INFLUENCES", "targetSlug": "confucian-philosophy", "targetName": "Confucian Philosophy", "context": "Zizhang's recorded questions about distinguished conduct, serving difficult rulers, and the distinction between genuine and performative virtue contributed to the core body of Confucian moral discussions."},
      {"sourceSlug": "analects", "sourceName": "Analects of Confucius", "verb": "DOCUMENTS", "targetSlug": "zhuansun-shi", "targetName": "Zizhang", "context": "The Analects preserve Zizhang's most significant conversations with Confucius — particularly his question about distinguished conduct and Confucius's distinction between genuine virtue and its appearance."}
    ],
    "places": [
      {"name": "Chen, China (modern Henan Province)", "role": "Zizhang's home state — a small Zhou feudal principality that was eventually absorbed by Chu in 479 BCE"},
      {"name": "Lu, China (modern Shandong Province)", "role": "Home state of Confucius where Zizhang joined the Confucian school and absorbed the teaching tradition that shaped his subsequent career"}
    ],
    "subjects": ["Confucianism", "Chinese Philosophy", "Classical China", "Classical Era", "Ethics", "Education", "Intellectual History", "Religion"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Zhuansun Shi (Zizhang) was one of Confucius's Ten Philosophers — a disciple whose practical questions about virtue, official service, and the distinction between genuine and performative moral character contributed to the core Confucian canon. His posthumous canonisation placed his image in Confucian temples across East Asia for two millennia, and his school represented one strand of the diverse post-Confucian intellectual tradition.",
      "significanceCategory": "regional"
    }
  }
},

"justus-of-urgell": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250justus-of-urgell.json",
  "slug": "justus-of-urgell",
  "data": {
    "summary": "Justus of Urgell (fl. 6th century CE, died c. 527–565 CE) was a Visigothic bishop of Urgell in the Pyrenees (modern Catalonia, Spain) who composed one of the most influential early medieval biblical commentaries — the 'Explanatio in Cantica Canticorum' (Commentary on the Song of Songs), written around 546 CE. A figure of the transitional period between late antique Christianity and the emerging medieval Visigothic church, Justus produced a commentary that helped establish the allegorical reading of the Song of Songs — as a dialogue between Christ and the Church, or between the divine Word and the human soul — as the dominant interpretive tradition for this biblical book in the medieval West.\n\nJustus's 'Commentary on the Song of Songs' drew on Origen's earlier allegorical interpretation and on the exegetical work of earlier Latin fathers, synthesising their insights into a relatively brief but theologically elegant commentary suited to the educational and pastoral needs of Visigothic Spain's monastic and episcopal culture. The work was widely copied and distributed in medieval scriptoria; it influenced subsequent Spanish commentaries and was known to both Isidore of Seville and Julian of Toledo — figures who shaped Visigothic Christianity's intellectual legacy for the medieval period. Its influence extended beyond Spain: it circulated in Carolingian libraries and contributed to the rich medieval tradition of Song of Songs interpretation that culminated in Bernard of Clairvaux's famous 86 sermons on the book in the 12th century.\n\nJustus participated in the Council of Lleida (546 CE) and the Council of Valencia (549 CE) — Visigothic provincial councils that were establishing the ecclesiastical order of post-Roman Iberia. His episcopate at Urgell placed him at the northern frontier of Visigothic Christianity, a border zone between the Visigothic kingdom and the Frankish kingdoms of Gaul where the transmission of texts and ecclesiastical culture between the two areas passed through his diocese.",
    "causes": [
      "The Visigothic church's need to develop a literate ecclesiastical culture in post-Roman Iberia — maintaining and transmitting the Latin intellectual tradition amid the political disruption of barbarian kingdoms — created the institutional demand for scholarly biblical commentary of the type Justus produced.",
      "The allegory tradition of Song of Songs interpretation — established by Origen in the 3rd century and developed by Ambrose and Jerome in the 4th — provided Justus with both the method and the precedent for his commentary, allowing him to build on an established interpretive framework.",
      "Urgell's position at the Pyrenean frontier between the Visigothic kingdom and the Frankish north made it a significant node in the circulation of texts and ecclesiastical culture, giving Justus access to both Iberian and Frankish Christian intellectual traditions."
    ],
    "effects": [
      "Justus's Song of Songs commentary contributed to the entrenchment of the allegorical reading in the medieval West — a tradition that gave the Song of Songs its ecclesiastical respectability and made it one of the most commented-upon books in the medieval biblical canon.",
      "Isidore of Seville and Julian of Toledo's knowledge of Justus's work placed his interpretation within the chain of Visigothic scholarly transmission that helped preserve late antique intellectual culture through the 7th–8th centuries — the 'Dark Ages' of the European West.",
      "The circulation of Justus's commentary in Carolingian scriptoria meant that Pyrenean 6th-century Visigothic exegesis contributed to the 9th-century Carolingian Renaissance's revival of biblical scholarship — an example of the unexpected pathways through which late antique learning survived in the early medieval West."
    ],
    "relationships": [
      {"sourceSlug": "justus-of-urgell", "sourceName": "Justus of Urgell", "verb": "PRODUCES", "targetSlug": "commentary-on-song-of-songs", "targetName": "Commentary on the Song of Songs (c. 546 CE)", "context": "Justus's 'Explanatio in Cantica Canticorum' was one of the most influential early medieval Song of Songs commentaries — establishing the allegorical Christ-Church reading that shaped medieval biblical interpretation."},
      {"sourceSlug": "origen", "sourceName": "Origen", "verb": "INFLUENCES", "targetSlug": "justus-of-urgell", "targetName": "Justus of Urgell", "context": "Origen's foundational Song of Songs commentary (3rd century) provided the allegorical method that Justus synthesised and transmitted in his more accessible 6th-century version."},
      {"sourceSlug": "justus-of-urgell", "sourceName": "Justus of Urgell", "verb": "INFLUENCES", "targetSlug": "isidore-of-seville", "targetName": "Isidore of Seville", "context": "Isidore of Seville knew Justus's Song of Songs commentary — part of the Visigothic chain of biblical scholarship that Isidore synthesised into his encyclopaedic works."}
    ],
    "places": [
      {"name": "Urgell (La Seu d'Urgell), Catalonia, Spain", "role": "Justus's episcopal see — a Pyrenean diocese at the frontier of the Visigothic kingdom and the primary institutional base of his scholarly and ecclesiastical activity"},
      {"name": "Lleida (Lerida) and Valencia, Spain", "role": "Sites of the 546 and 549 CE councils at which Justus participated — provincial assemblies establishing Visigothic ecclesiastical order"}
    ],
    "subjects": ["Medieval Theology", "Visigothic Spain", "Biblical Commentary", "Classical Era", "Church History", "Spain", "Intellectual History", "Medieval Era"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Justus of Urgell wrote one of the most influential early medieval Song of Songs commentaries — establishing the allegorical Christ-Church reading that shaped medieval biblical interpretation across the Western Church. His work was known to Isidore of Seville, circulated in Carolingian libraries, and contributed to the Song of Songs interpretive tradition that culminated in Bernard of Clairvaux's famous sermons six centuries later.",
      "significanceCategory": "regional"
    }
  }
},

"muḥammad-ibn-yūsuf-al-kindi": {
  "filepath": "data/appwrite-export/entities/205-Class-205/205muḥammad-ibn-yūsuf-al-kindi.json",
  "slug": "muḥammad-ibn-yūsuf-al-kindi",
  "data": {
    "summary": "Muḥammad ibn Yūsuf al-Kindī (897–961 CE) was an Egyptian Islamic scholar and historian whose two major works — 'Wulāt Miṣr' (The Governors of Egypt) and 'Quḍāt Miṣr' (The Judges of Egypt) — are among the most important primary sources for the administrative history of early Islamic Egypt. Not to be confused with the philosopher Yaʿqūb ibn Isḥāq al-Kindī (c. 801–873 CE), who was an Arab philosopher of the Abbasid court in Baghdad, this al-Kindī was a Malikite jurist and scholar based in Egypt who compiled systematic biographical registers of the governors who ruled Egypt from the Arab conquest (639 CE) through his own time, and of the judges who administered Islamic law in the Fustat-Cairo metropolitan area.\n\nThe 'Wulāt Miṣr' (Governors of Egypt) and 'Quḍāt Miṣr' (Judges of Egypt) are works in the Arabic tabaqāt (biographical dictionary) tradition — systematic compilations of biographical data and administrative information organised by subject class. The 'Wulāt' covers the full sequence of Arab governors from ʿAmr ibn al-ʿĀṣ's conquest through the Tulunid and early Ikhshidid periods, providing names, dates, administrative decisions, and anecdotes that are often the only surviving source for the personalities and policies of specific Egyptian governors. The 'Quḍāt' provides equivalent coverage of the qadi tradition — valuable for understanding the development of Malikite jurisprudence in Egypt and the institutional evolution of Islamic justice in the province.\n\nAl-Kindī's works are significant precisely because administrative history of the type he recorded — detailed, bureaucratic, anecdote-rich — is relatively rare in the early Islamic historiographical tradition, which tended toward universal history, biographical dictionaries of hadith transmitters, and religious scholarship. His Egyptian focus makes him the primary source for aspects of early Islamic Egyptian provincial governance that illuminate how the Arab state managed one of its most important and populous provinces during the formative centuries of Islamic civilisation.",
    "causes": [
      "The tabaqāt (biographical dictionary) tradition in early Islamic scholarship — pioneered by Ibn Saʿd's 'Kitāb al-Ṭabaqāt al-Kubrā' for the companions of the Prophet — provided the literary form and scholarly precedent for al-Kindī's systematic compilation of governors and judges.",
      "Al-Kindī's position in 10th-century Egypt, during the period of Ikhshidid rule, gave him access to court archives, administrative records, and the oral tradition of Egyptian official memory that he drew on to compile his biographical dictionaries.",
      "The Malikite legal tradition's emphasis on the continuity of legal practice and the importance of knowing the succession of judicial authorities provided a religious-institutional motivation for preserving systematic records of the judges who had administered Islamic law."
    ],
    "effects": [
      "Al-Kindī's 'Wulāt Miṣr' and 'Quḍāt Miṣr' have been the primary sources for historians of early Islamic Egypt since their rediscovery in the 19th century — they are extensively cited in modern scholarship on Umayyad and Abbasid Egypt and remain irreplaceable for administrative and legal history of the province.",
      "His systematic recording of the governor succession, including detailed notes on individual policies and conflicts, preserved aspects of Egyptian provincial history that would otherwise be entirely unknown — his work fills gaps in the historical record that no other surviving source covers.",
      "As a model of provincial administrative history, al-Kindī's works influenced subsequent Egyptian historical compilations, contributing to the tradition of Egyptian administrative scholarship that produced the great encyclopaedists al-Qalqashandī and al-Maqrīzī in the 14th–15th centuries."
    ],
    "relationships": [
      {"sourceSlug": "muḥammad-ibn-yūsuf-al-kindi", "sourceName": "Muḥammad ibn Yūsuf al-Kindī", "verb": "PRODUCES", "targetSlug": "wulat-misr", "targetName": "Wulāt Miṣr (Governors of Egypt)", "context": "Al-Kindī's 'Governors of Egypt' is the primary source for the sequence of Arab governors from the 639 CE conquest through the 10th century — an irreplaceable administrative history of early Islamic Egypt."},
      {"sourceSlug": "muḥammad-ibn-yūsuf-al-kindi", "sourceName": "Muḥammad ibn Yūsuf al-Kindī", "verb": "DOCUMENTS", "targetSlug": "umayyad-egypt", "targetName": "Umayyad and Abbasid Egypt", "context": "Al-Kindī's biographical dictionaries of governors and judges are the primary surviving sources for the administrative and judicial history of Egypt under Umayyad and Abbasid rule."},
      {"sourceSlug": "ibn-saad", "sourceName": "Ibn Saʿd", "verb": "INFLUENCES", "targetSlug": "muḥammad-ibn-yūsuf-al-kindi", "targetName": "Muḥammad ibn Yūsuf al-Kindī", "context": "The tabaqāt tradition pioneered by Ibn Saʿd provided al-Kindī with the literary form he used for his compilations of Egyptian governors and judges."}
    ],
    "places": [
      {"name": "Fustat (Old Cairo), Egypt", "role": "The first Arab capital of Egypt and centre of al-Kindī's scholarly world — the administrative hub whose governor and judicial succession he documented"},
      {"name": "Egypt", "role": "The province that al-Kindī documented across three centuries from the Arab conquest, making him the primary historical authority for early Islamic Egyptian provincial governance"}
    ],
    "subjects": ["Islamic History", "Medieval History", "Egypt", "Historiography", "Medieval Era", "Administrative History", "North Africa", "Intellectual History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Muḥammad ibn Yūsuf al-Kindī was an Egyptian scholar whose 'Governors of Egypt' and 'Judges of Egypt' are the primary sources for the administrative and legal history of early Islamic Egypt. His systematic biographical dictionaries are irreplaceable for historians of Umayyad and Abbasid provincial governance, filling gaps in the historical record that no other surviving source covers.",
      "significanceCategory": "regional"
    }
  }
},

"lupus-of-sens": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250lupus-of-sens.json",
  "slug": "lupus-of-sens",
  "data": {
    "summary": "Lupus of Sens (died 623 CE), also known as Loup de Sens or Saint Loup, was a Frankish bishop of Sens and one of the more prominent ecclesiastical figures in the Merovingian church of early 7th-century Gaul — a period of intense religious and political turbulence as the Frankish kingdom was torn between rival Merovingian queens (Brunhild and Fredegund) and their royal descendants, and as the Church navigated the competing pressures of royal patronage, Columbanian reform, and episcopal independence. He served as Bishop of Sens for over thirty years (c. 591–623 CE), making him one of the longer-serving prelates of the Merovingian church and a witness to some of the most violent episodes of early medieval Frankish politics.\n\nLupus is primarily known from Merovingian hagiographic tradition and from brief references in Gregory of Tours's 'History of the Franks' and the 'Chronicle of Fredegar'. He was present at several Frankish church councils, including the Council of Paris (614 CE) — one of the most important Merovingian councils, which reaffirmed episcopal election rights and placed limits on royal intervention in Church appointments. His association with Queen Brunhild's court and his subsequent fall from favour (he was briefly exiled, reportedly due to his opposition to the Brunhild faction's church policies) placed him in the complex web of Frankish ecclesiastical politics in which bishops' careers were tightly bound to royal patronage and court faction.\n\nLupus was venerated as a saint after his death, with his feast day on 1 September (in some traditions) and a hagiographic 'Vita' that recorded miracle stories. The veneration of his relics at Sens and the dedication of several churches to him in the Sens region kept his memory alive through the medieval period. He belongs to the important but often overlooked group of Merovingian bishops who maintained the institutional continuity of Roman Christianity through the turbulent 6th–7th centuries, providing the ecclesiastical framework within which Carolingian Christianity would develop.",
    "causes": [
      "The Merovingian church's peculiar combination of episcopal independence (preserved from the late Roman conciliar tradition) and extreme dependence on royal patronage and court faction created the unstable career environment in which Lupus navigated his long episcopate.",
      "Queen Brunhild's domination of the Frankish court in the early 7th century — and her conflicts with rival factions and with the Columbanian reform movement — created the political turbulence that affected Lupus's career, including his brief exile.",
      "The Council of Paris (614 CE) represented the Merovingian church's attempt to codify the relationship between royal authority and episcopal independence — Lupus's participation placed him in the context of these broader institutional negotiations."
    ],
    "effects": [
      "Lupus's long episcopate at Sens contributed to the institutional continuity of one of the oldest and most prestigious Frankish episcopal sees, maintaining the Roman administrative tradition in the important religious province of Lugdunensis IV through the turbulent decades of Merovingian civil war.",
      "His participation in the Council of Paris (614 CE) contributed to the Merovingian church's codification of episcopal rights that provided some of the institutional precedents for the Carolingian church reforms of the 8th century.",
      "The hagiographic cult of Lupus after his death — including miracle stories and church dedications in the Sens region — contributed to the local religious landscape of northeastern France that persisted through the medieval period."
    ],
    "relationships": [
      {"sourceSlug": "lupus-of-sens", "sourceName": "Lupus of Sens", "verb": "OCCURS_IN", "targetSlug": "merovingian-church", "targetName": "Merovingian Church", "context": "Lupus was one of the most prominent Merovingian bishops of the early 7th century, navigating the complex relationship between episcopal independence and royal patronage in Frankish Gaul."},
      {"sourceSlug": "lupus-of-sens", "sourceName": "Lupus of Sens", "verb": "OCCURS_IN", "targetSlug": "council-of-paris-614", "targetName": "Council of Paris (614 CE)", "context": "Lupus participated in the Council of Paris (614 CE) — the major Merovingian council that attempted to codify episcopal election rights and limit royal intervention in Church appointments."},
      {"sourceSlug": "brunhild-of-austrasia", "sourceName": "Queen Brunhild", "verb": "INFLUENCES", "targetSlug": "lupus-of-sens", "targetName": "Lupus of Sens", "context": "Brunhild's court factional politics contributed to Lupus's brief exile — illustrating the vulnerability of Merovingian bishops to royal displeasure regardless of their canonical standing."}
    ],
    "places": [
      {"name": "Sens, France (Roman Agedincum)", "role": "Episcopal see of Lupus for over thirty years — one of the oldest and most prestigious metropolitan sees in Frankish Gaul"},
      {"name": "Paris, France", "role": "Site of the Council of Paris (614 CE) where Lupus participated in the major Merovingian church council that addressed episcopal elections and royal intervention"}
    ],
    "subjects": ["Merovingian History", "Church History", "Medieval History", "France", "Classical Era", "Frankish Gaul", "Hagiography", "Medieval Era"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 5,
      "significanceNarrative": "Lupus of Sens was a long-serving Merovingian bishop whose thirty-year episcopate at one of Gaul's most prestigious sees maintained institutional continuity through the turbulent early 7th century. His participation in the Council of Paris (614 CE) placed him in the Merovingian church's attempt to codify episcopal independence — a precedent for the Carolingian institutional reforms.",
      "significanceCategory": "local"
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
