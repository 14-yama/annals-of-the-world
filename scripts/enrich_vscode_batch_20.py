#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 20 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: khosrau-the-usurper, uurad, ariapeithes, atheism, president,
          gratus-of-aosta, polyxenos-epiphanes-soter, astronomy
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-20-may2026"

ENRICHMENTS = {

"khosrau-the-usurper": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221khosrau-the-usurper.json",
  "slug": "khosrau-the-usurper",
  "data": {
    "summary": "Khosrau the Usurper (died c. 500 CE) was a claimant to the Sasanian Persian throne in the late 5th century — a member of the Sasanian royal family who seized power briefly during the turbulent period of dynastic instability that followed the death of Peroz I (r. 459–484 CE) and the catastrophic Sasanian defeat at the Battle of Herat (484 CE), in which Peroz and much of the Sasanian nobility were killed by the Hephthalite Huns. This military disaster created a severe succession crisis and a period of Hephthalite dominance over Persia that lasted for several decades.\n\nThe Battle of Herat (484 CE) was one of the worst military disasters in Sasanian history: the Emperor Peroz I and a large portion of the Persian army were killed in battle against the Hephthalites (the eastern Iranian nomadic power that dominated Central Asia), and Persia was subsequently forced to pay annual tribute to the Hephthalites, severely weakening its prestige and finances. The succession that followed was contested, with multiple claimants vying for the throne. In this unstable context, Khosrau briefly seized or claimed the throne — whether as a legitimate heir or as a rebellious general — before being defeated and killed by Kavad I (who reigned 488–531 CE, with a period of exile in 496–498 CE).\n\nKhosrau's usurpation is one of several contested throne claims in the period between Peroz's death (484 CE) and Kavad I's consolidation of power — a period that also included the reigns of Balash (484–488 CE), Kavad's first reign, his temporary overthrow by Jamasp (496–498 CE), and Kavad's restoration. This era of Sasanian instability, occurring simultaneously with the Hephthalite domination and the internal religious upheaval of the Mazdakite movement, was one of the most difficult periods in Sasanian history before Khosrow I's great reforms in the mid-6th century.",
    "causes": [
      "The catastrophic Battle of Herat (484 CE) — in which Peroz I and much of the Sasanian army were killed by the Hephthalites — created a succession vacuum and a period of severe state weakness that made throne claims by members of the royal house both more tempting and more feasible.",
      "The Hephthalite domination of Persia following the Battle of Herat — including the imposition of annual tribute payments — weakened central Sasanian authority and emboldened internal rivals, creating the conditions in which claimants like Khosrau could attempt to seize power.",
      "The structural dynamics of the Sasanian succession system — in which there was no clear primogeniture rule and multiple members of the royal family could claim the throne — meant that periods of central weakness regularly produced competing claimants and usurpations."
    ],
    "effects": [
      "Khosrau the Usurper's failure and death — likely at the hands of Kavad I or his supporters — contributed to Kavad's eventual consolidation of power and the beginning of the process that would, under Khosrow I (531–579 CE), restore and greatly enhance Sasanian imperial power.",
      "The series of contested successions in which Khosrau's claim was one episode delayed the administrative and military reforms that the Sasanian state needed, prolonging the period of Hephthalite dominance and internal weakness before Kavad I's later alliance with the Hephthalites paradoxically enabled his own consolidation.",
      "Khosrau's usurpation illustrates the recurrent pattern of Sasanian succession crises — the gap between the empire's often extraordinary external power and its internal dynastic vulnerability — that would eventually prove fatal in the 7th-century crisis that allowed the Arab Islamic conquest."
    ],
    "relationships": [
      {"sourceSlug": "khosrau-the-usurper", "sourceName": "Khosrau the Usurper", "verb": "CHALLENGES", "targetSlug": "kavad-i", "targetName": "Kavad I (Sasanian Emperor, 488–531 CE)", "context": "Khosrau's usurpation was likely suppressed by Kavad I — the Sasanian king who eventually consolidated power after the turbulent succession crisis following Peroz's death."},
      {"sourceSlug": "battle-of-herat", "sourceName": "Battle of Herat (484 CE)", "verb": "CREATES", "targetSlug": "khosrau-the-usurper", "targetName": "Khosrau's Usurpation", "context": "The catastrophic Battle of Herat — in which Peroz I was killed — created the succession vacuum and state weakness that enabled Khosrau's usurpation attempt."},
      {"sourceSlug": "hephthalite-empire", "sourceName": "Hephthalite Empire", "verb": "WEAKENS", "targetSlug": "khosrau-the-usurper", "targetName": "Sasanian Succession (including Khosrau)", "context": "Hephthalite dominance of Persia after 484 CE — including tribute payments — severely weakened Sasanian central authority, creating the environment in which internal claimants like Khosrau could contest the throne."}
    ],
    "places": [
      {"name": "Sasanian Empire (Greater Iran)", "role": "The political arena of Khosrau's usurpation — the Sasanian Persian state in its most difficult decades, weakened by Hephthalite defeat and internal succession conflicts"},
      {"name": "Ctesiphon (Iraq)", "role": "The Sasanian capital — the centre of the political power that Khosrau and other claimants were contesting in the turbulent post-Herat succession crisis"}
    ],
    "subjects": ["Sasanian Empire", "Persian History", "Classical Era", "Late Antiquity", "Hephthalites", "Ancient Near East", "5th Century CE", "Succession Crisis"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 2,
      "significanceNarrative": "Khosrau the Usurper (died c. 500 CE) was a minor claimant to the Sasanian throne during the turbulent succession crisis that followed the catastrophic Battle of Herat (484 CE) and Peroz I's death. His usurpation represents one episode in the period of Sasanian weakness and Hephthalite domination that preceded Kavad I's consolidation of power.",
      "significanceCategory": "local"
    }
  }
},

"uurad": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221uurad.json",
  "slug": "uurad",
  "data": {
    "summary": "Uurad (fl. 840s CE; died 842 CE) was a Pictish king — ruler of the ancient Pictish people of northeastern Scotland — who reigned briefly in the final, turbulent years of the Pictish kingdom before its effective end and absorption into the Scottish (Dál Riatan) kingdom under Kenneth MacAlpin (Cináed mac Ailpín, reigned 843–858 CE). He is listed in the Pictish king lists as one of the last kings of the Picts, his reign occurring in the extraordinarily turbulent decade in which the previously dominant Pictish kingdom was definitively overcome.\n\nThe Picts were the indigenous people of Scotland north of the Firth of Forth — a people who had successfully resisted Roman conquest (the Antonine Wall, Hadrian's Wall, and the Severan campaigns all failed to subdue them), developed a distinctive art (the carved symbol stones of northeastern Scotland), and built a powerful kingdom that had, at its height, been the dominant political force in northern Britain. The Pictish kingdom's origins are obscure, but it was a major power in the 7th–8th centuries CE, and Pictish kings had occasionally dominated large parts of Scotland. However, by the 840s, decades of Viking raiding had devastated coastal and island communities, and the Pictish and Dál Riatan kingdoms were increasingly under pressure.\n\nUurad's reign and death (842 CE) coincide with the critical years of Kenneth MacAlpin's rise to power — the tradition (later and possibly legendary) that MacAlpin massacred the Pictish nobility at a feast and seized the combined kingdom. Whether this tradition preserves historical reality or is later invention, Kenneth MacAlpin did effectively unite the Pictish and Dál Riatan kingdoms into what would become the Kingdom of Scotland, and Uurad's reign represents the last moment of independent Pictish royal authority before this transformation.",
    "causes": [
      "The prolonged Viking raids and settlements from the late 8th century onwards — devastating the western and northern Scottish islands and coasts, killing leaders, and disrupting political structures — weakened both the Pictish and Dál Riatan kingdoms and created the political conditions in which their merger became feasible.",
      "The dynastic and political instability of the Pictish kingdom in the 9th century — reflected in the rapid succession of kings in the Pictish king lists — created the weakness that enabled Kenneth MacAlpin's successful seizure of power, with Uurad's short reign being part of this pattern of instability.",
      "The gradual cultural and dynastic integration between the Pictish and Dál Riatan (Scottish/Irish) kingdoms over the preceding centuries — through intermarriage, shared Christianity, and political alliances — created the conditions in which a merger of the two kingdoms under a leader who could claim descent from both royal lines was politically possible."
    ],
    "effects": [
      "Uurad's death (842 CE) and the end of the independent Pictish monarchy immediately preceded Kenneth MacAlpin's effective unification of the Pictish and Dál Riatan kingdoms (843 CE) — creating the Kingdom of Alba (Scotland) that would develop into the medieval Scottish kingdom.",
      "The end of the Pictish kingdom and the absorption of the Picts into the broader Scottish/Gaelic cultural sphere resulted in the gradual disappearance of the Pictish language — a loss that remains one of the great unsolved puzzles of linguistics, as the Pictish language (whose relationship to Celtic is debated) left only fragmentary evidence.",
      "The Pictish cultural legacy — particularly the extraordinary carved symbol stones of northeastern Scotland — survived the political absorption, and modern Scottish identity draws on the Pictish heritage as one of the foundational elements of Scotland's pre-medieval past."
    ],
    "relationships": [
      {"sourceSlug": "uurad", "sourceName": "Uurad", "verb": "PRECEDED_BY_REIGN", "targetSlug": "kenneth-macalpin", "targetName": "Kenneth MacAlpin (Kenneth I of Scotland)", "context": "Uurad was one of the last Pictish kings before Kenneth MacAlpin united the Pictish and Dál Riatan kingdoms — Uurad's death (842 CE) immediately preceded Kenneth's creation of the Kingdom of Alba."},
      {"sourceSlug": "pictish-kingdom", "sourceName": "Pictish Kingdom", "verb": "ENDS_WITH", "targetSlug": "uurad", "targetName": "Uurad (one of last Pictish kings)", "context": "Uurad's reign represents one of the final moments of independent Pictish kingship — the culmination of the kingdom's gradual decline that ended with Kenneth MacAlpin's unification."},
      {"sourceSlug": "viking-raids-scotland", "sourceName": "Viking Raids on Scotland (late 8th–9th century)", "verb": "WEAKENS", "targetSlug": "uurad", "targetName": "Pictish Kingdom under Uurad", "context": "Viking raiding devastated Scottish coastal communities and weakened both the Pictish and Dál Riatan kingdoms — contributing to the political instability that made Kenneth MacAlpin's absorption of the Pictish throne possible."}
    ],
    "places": [
      {"name": "Pictland (northeastern Scotland)", "role": "Uurad's kingdom — the Pictish realm of northeastern Scotland, north of the Firth of Forth, whose independent existence ended in the years after his reign"},
      {"name": "Scotland (early medieval)", "role": "The broader context — the emerging Kingdom of Alba that arose from the merger of the Pictish and Dál Riatan kingdoms in which Uurad's death was a turning point"}
    ],
    "subjects": ["Pictish History", "Scottish History", "Classical Era", "Viking Age", "Medieval Scotland", "Celtic History", "Early Medieval History", "9th Century CE"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 3,
      "significanceNarrative": "Uurad (died 842 CE) was one of the last kings of the ancient Pictish people of northeastern Scotland — his reign immediately preceded Kenneth MacAlpin's unification of the Pictish and Dál Riatan kingdoms that created the Kingdom of Alba (Scotland). His death marks the effective end of independent Pictish political existence and the beginning of the political entity that would become medieval Scotland.",
      "significanceCategory": "regional"
    }
  }
},

"ariapeithes": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221ariapeithes.json",
  "slug": "ariapeithes",
  "data": {
    "summary": "Ariapeithes (Greek: Ἀριάπειθης; fl. c. 5th century BCE) was a Scythian king — ruler of the Scythians of the Pontic steppe (the vast grassland north of the Black Sea, in modern Ukraine and southern Russia) — whose political career is documented primarily by the historian Herodotus in his Histories. He was the father of Scyles and Octamasades, whose dynastic rivalry illustrated the tensions within Scythian society between those who adopted Greek culture and those who fiercely defended traditional Scythian customs.\n\nAccording to Herodotus (Histories 4.76–80), Ariapeithes was a powerful Scythian ruler who had multiple wives — including a Greek woman from the city of Istria (on the Black Sea coast) who was the mother of Scyles. The story of Scyles — Ariapeithes's son who was raised with Greek language and culture, who repeatedly slipped away from his Scythian subjects to participate in Greek religious rites at the city of Olbia (the major Greek colony on the northern Black Sea), and who was eventually executed by his own brother Octamasades when his Hellenisation was revealed — is one of Herodotus's most vivid illustrations of the tension between Scythian cultural conservatism and the appeal of Greek civilisation to Scythian elites.\n\nAriapeithes himself was killed by Spargapeithes, king of the Agathyrsi (a neighbouring Iranian/steppe people), creating the succession crisis between Scyles and Octamasades. His career represents the complex political world of the Pontic steppe in the 5th century BCE — the interaction between the dominant Scythian nomadic empire, the Greek Black Sea colonies, and the neighbouring steppe peoples — that Herodotus observed and recorded during his travels in the Black Sea region.",
    "causes": [
      "The geopolitical position of the Scythian kingdom on the Pontic steppe — between the Greek colonies of the northern Black Sea coast (Olbia, Chersonesus, Panticapaeum) and the neighbouring steppe peoples (Agathyrsi, Sauromatae) — created the diplomatic and military relationships within which Ariapeithes operated, including his marriage to a Greek woman from Istria.",
      "The Scythian elite's exposure to Greek culture through their extensive contact with the Black Sea colonies — Greek luxury goods, religious ideas, and artistic styles penetrated Scythian culture, creating the cultural hybridity that Ariapeithes's son Scyles represented and that Scythian traditionalists violently rejected.",
      "The competitive dynastic politics of the steppe — in which Scythian kings maintained their position through military success, tribute collection, and diplomatic marriages with multiple peoples — created the rivalries that led to Ariapeithes's death at the hands of the Agathyrsi king Spargapeithes."
    ],
    "effects": [
      "Ariapeithes's death at the hands of Spargapeithes and the subsequent succession crisis between his sons Scyles and Octamasades illustrated the internal divisions within Scythian society over cultural identity — the conflict between Hellenised and traditionally-minded Scythian leaders that Herodotus used to explore the theme of cultural boundaries and taboos.",
      "Scyles's execution by his brother Octamasades — the direct consequence of Ariapeithes's dynastic legacy — became one of Herodotus's key ethnographic examples of Scythian cultural conservatism: the Scythians' exceptional hostility to adopting foreign customs, which Herodotus connected to their response to Anacharsis's Greek-style religious practices.",
      "Ariapeithes's political relationships — particularly his marriage alliances with Greek and neighbouring steppe communities — illustrate the sophisticated diplomatic world of the Pontic steppe in the 5th century BCE, demonstrating that Scythian kings were not isolated nomads but active participants in a complex network of political relationships with the Greek and Iranian worlds."
    ],
    "relationships": [
      {"sourceSlug": "ariapeithes", "sourceName": "Ariapeithes", "verb": "FATHER_OF", "targetSlug": "scyles", "targetName": "Scyles (Scythian king, Herodotus 4.78–80)", "context": "Ariapeithes was the father of Scyles — the Hellenised Scythian king whose execution by his brother Octamasades is one of Herodotus's most vivid ethnographic narratives about Scythian cultural conservatism."},
      {"sourceSlug": "herodotus", "sourceName": "Herodotus", "verb": "RECORDS", "targetSlug": "ariapeithes", "targetName": "Ariapeithes (Scythian king)", "context": "Herodotus is the primary source for Ariapeithes — his Histories' ethnographic account of the Scythians includes the story of Ariapeithes and his sons as an illustration of Scythian cultural identity."},
      {"sourceSlug": "spargapeithes", "sourceName": "Spargapeithes (king of the Agathyrsi)", "verb": "KILLS", "targetSlug": "ariapeithes", "targetName": "Ariapeithes (Scythian king)", "context": "Ariapeithes was killed by Spargapeithes, king of the Agathyrsi — creating the succession crisis in which his son Scyles's Hellenisation became the fatal fault line."}
    ],
    "places": [
      {"name": "Pontic Steppe (modern Ukraine/southern Russia)", "role": "Ariapeithes's kingdom — the vast grassland north of the Black Sea that was the heartland of the Scythian nomadic empire"},
      {"name": "Olbia and the northern Black Sea colonies (Greek colonies)", "role": "The cultural frontier context — the Greek colonies of the northern Black Sea coast whose proximity to the Scythians created the cultural hybridity that shaped Ariapeithes's world and his sons' fates"}
    ],
    "subjects": ["Scythian History", "Ancient Greece", "Classical Era", "Steppe Peoples", "Black Sea", "Ancient History", "Herodotus", "5th Century BCE"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 4,
      "significanceNarrative": "Ariapeithes (fl. c. 5th century BCE) was a Scythian king of the Pontic steppe whose career and death are recorded by Herodotus — primarily as the father of Scyles, the Hellenised Scythian king whose execution by his brother illustrated Scythian cultural conservatism. His political world represents the complex intersection of the Scythian nomadic empire, the Greek Black Sea colonies, and the neighbouring steppe peoples that Herodotus documented.",
      "significanceCategory": "regional"
    }
  }
},

"atheism": {
  "filepath": "data/appwrite-export/entities/145-Class-145/145atheism.json",
  "slug": "atheism",
  "data": {
    "summary": "Atheism — from the Greek atheos ('without god', from a- 'without' + theos 'god') — is the absence of belief in the existence of gods or the positive assertion that no gods exist. As a philosophical position, explicit atheism has a history dating to ancient Greece (Theodorus of Cyrene, Diagoras of Melos, c. 5th–4th century BCE) and ancient India (the Cārvāka materialist school, c. 6th century BCE); as a widespread social phenomenon in the modern West, it became significant primarily in the 18th century Enlightenment and accelerated dramatically through the 19th–21st centuries, to the point where atheists and the non-religious now constitute a substantial portion of the populations of many developed societies.\n\nThe term 'atheism' has historically been used both as a self-description and as an accusation — in ancient Greece, Christians were called atheists by their pagan contemporaries because they rejected the traditional gods; in early modern Europe, atheism was a serious charge that could result in execution; and the philosophical defence and development of atheism as a reasoned position — through figures like Baron d'Holbach (Système de la nature, 1770), David Hume (Dialogues Concerning Natural Religion, 1779), Ludwig Feuerbach, Karl Marx, Friedrich Nietzsche, and Bertrand Russell — represents one of the major intellectual developments of modern Western philosophy. The 20th century produced both state atheism (Soviet communism's militant anti-religion, the Chinese Cultural Revolution's destruction of religious practice) and the 'New Atheism' of the early 21st century (Dawkins, Hitchens, Harris, Dennett).\n\nPhilosophically, atheism is typically distinguished from agnosticism (the position that the existence of god is unknown or unknowable) and from strong atheism (the positive assertion that no gods exist) versus weak atheism (the mere absence of theistic belief). The arguments for and against theism — the cosmological argument, the ontological argument, the argument from evil, the argument from design — constitute one of the oldest and most sustained debates in the history of philosophy.",
    "causes": [
      "The development of natural philosophy and scientific explanation from ancient Greece onwards provided increasingly powerful accounts of natural phenomena that did not require divine intervention — from Democritus's atomism through Newton's mechanics to Darwin's evolution and the Big Bang cosmology — gradually reducing the explanatory role of supernatural agency.",
      "The internal critiques of religious institutions — the corruption, persecution, and hypocrisy that religious critics from Erasmus to Voltaire to Marx documented — created the social motivation for rejecting not just specific institutional forms of religion but the theological foundations that supported them.",
      "The Enlightenment's elevation of reason, empirical evidence, and critical inquiry as the standards of truth — its systematic application to all claims including religious ones — created the intellectual framework within which explicit atheism could be articulated, defended, and eventually widely accepted."
    ],
    "effects": [
      "The 19th–20th century spread of atheism and secularism in Western societies produced the separation of church and state, the secularisation of law, education, and medicine, and the decline of religious practice across much of Europe — a transformation of the relationship between religion and public life that was among the most significant social changes of the modern period.",
      "Marx's analysis of religion as 'the opium of the people' — ideological superstructure that legitimated class exploitation — shaped the explicitly atheist character of communist states (Soviet Union, China, Cuba), which conducted systematic campaigns against religious practice and produced the only large-scale state enforcement of atheism in modern history.",
      "The persistence of atheism as a minority philosophical position throughout human history — and its dramatic growth in the 20th–21st centuries — has forced sustained theological and philosophical engagement with the question of justification for religious belief, producing sophisticated modern defences of theism (Plantinga, Swinburne) and atheism (Mackie, Oppy) that constitute the current state of philosophy of religion."
    ],
    "relationships": [
      {"sourceSlug": "atheism", "sourceName": "Atheism", "verb": "OPPOSED_BY", "targetSlug": "theism", "targetName": "Theism (religious belief systems)", "context": "Atheism is defined by its rejection of theism — the belief in the existence of gods — and its relationship to theism (whether as its negation or as simply its absence) is the fundamental philosophical question in defining the concept."},
      {"sourceSlug": "darwinian-evolution", "sourceName": "Darwinian Evolution (1859)", "verb": "STRENGTHENS", "targetSlug": "atheism", "targetName": "Atheism (naturalist argument)", "context": "Darwin's theory of evolution by natural selection provided a naturalistic explanation for the apparent design in living organisms — removing what had been the strongest argument for theism (the argument from design) and greatly strengthening the intellectual case for atheism."},
      {"sourceSlug": "enlightenment", "sourceName": "The Enlightenment (18th century)", "verb": "ENABLES", "targetSlug": "atheism", "targetName": "Modern Atheism", "context": "The Enlightenment's elevation of reason and critical inquiry as standards of truth created the intellectual framework within which modern philosophical atheism was articulated and defended — with figures like Hume and d'Holbach providing its foundational texts."}
    ],
    "places": [
      {"name": "Ancient Greece and India (early philosophical atheism)", "role": "The ancient intellectual contexts — the Greek philosophical tradition and the Indian Cārvāka school — where explicit philosophical rejection of divine existence was first systematically articulated"},
      {"name": "Europe and Global (modern secularisation)", "role": "The contemporary geographic spread of atheism — now substantial in much of Europe, East Asia, and the English-speaking world, representing one of the major demographic shifts in global religious identity"}
    ],
    "subjects": ["Philosophy", "Religion", "Classical Era", "Secularism", "History of Ideas", "Enlightenment", "Philosophical Thought", "Modern History"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Atheism — the rejection of belief in gods — is one of the most consequential philosophical positions in human intellectual history, with ancient roots (Greek, Indian) but its most dramatic social impact in the modern era. The Enlightenment's rationalisation of knowledge, Darwin's evolution, and Marx's materialism progressively strengthened atheism's intellectual foundations, and the 20th–21st centuries have seen the non-religious become a significant portion of many developed societies — one of the major transformations in human religious demography.",
      "significanceCategory": "highly-significant"
    }
  }
},

"president": {
  "filepath": "data/appwrite-export/entities/574-Class-574/574president.json",
  "slug": "president",
  "data": {
    "summary": "President is a title for the head of state or head of government of a republic or other organisation — one of the most important political titles in the modern world, used in various forms by the leaders of over 130 countries. The title derives from the Latin praesidens ('presiding over', from praesidere, 'to sit before or in front of') and was first used in the political context of the presiding officer of deliberative bodies — the President of the Continental Congress in the American Revolution, and then the President of the United States (established by the Constitution of 1787) — before spreading globally as the standard republican alternative to monarchical titles.\n\nThe American presidency — established by the Constitution of 1787 and first held by George Washington (inaugurated 1789) — was the foundational model for presidential government: an executive head of state directly elected by the people (or by an electoral college), invested with executive power, serving a fixed term, and subject to constitutional limits and legislative oversight. The American model influenced the presidential systems adopted by the Latin American republics that emerged from Spanish colonial rule in the early 19th century (beginning with Simón Bolívar's South American republics), by France (the French Fifth Republic's strong presidency under de Gaulle, 1958), and by many postcolonial states in the 20th century.\n\nPresidential systems are distinguished from parliamentary systems (where the head of government — prime minister — derives authority from the legislature rather than direct election) and from semi-presidential systems (where power is shared between a directly elected president and a prime minister). The concentration of executive power in a single directly elected individual makes the presidency both a powerful vehicle for democratic leadership and a potential pathway to authoritarian consolidation — a tension illustrated by the careers of presidents from Lincoln and Roosevelt to Putin and Orbán.",
    "causes": [
      "The American Revolution's rejection of monarchy and hereditary privilege — the founding principle that government derives its just powers from the consent of the governed — created the intellectual and political context in which a new form of executive office (the president) was invented as the republican alternative to the king.",
      "The Constitutional Convention of 1787's practical problem of creating a strong enough executive to govern effectively while preventing tyranny — solved by the 'separated powers' system with an independently elected president, a bicameral legislature, and an independent judiciary — produced the specific design of the presidential office that became the global model.",
      "The post-colonial drive for republican self-governance — in Latin America (1810–1825), in Europe (1848 revolutions, Third French Republic), and in the post-1945 decolonisation of Asia and Africa — spread the presidential title globally as the standard designation for the head of state of a republic."
    ],
    "effects": [
      "The spread of presidential republics across the globe — particularly in Latin America and postcolonial Africa and Asia — made the presidency one of the most common forms of executive government in the world, with over 130 countries using the title for their head of state or government.",
      "The American model of a strong, independently elected executive with defined powers and term limits became the reference point for constitutional design globally — both as a model to emulate (many constitutions explicitly drew on American precedents) and as a warning (the risks of presidential authoritarianism in many Latin American and postcolonial states).",
      "The presidency's combination of democratic mandate (popular election) and concentrated executive power made it both a vehicle for transformative leadership (Lincoln, Roosevelt, Mandela) and a potential instrument of democratic erosion — the 21st century has seen 'democratic backsliding' through the actions of elected presidents who gradually dismantled constitutional constraints."
    ],
    "relationships": [
      {"sourceSlug": "president", "sourceName": "President (office)", "verb": "ORIGINATED_WITH", "targetSlug": "george-washington", "targetName": "George Washington (first US President, 1789)", "context": "Washington's acceptance and definition of the presidential office — particularly his voluntary resignation after two terms — established the norms and precedents that shaped the American presidency and its global influence."},
      {"sourceSlug": "united-states-constitution", "sourceName": "United States Constitution (1787)", "verb": "CREATES", "targetSlug": "president", "targetName": "President (office of)", "context": "The Constitutional Convention of 1787 invented the modern presidency — designing an independently elected executive with defined powers that became the global template for republican executive government."},
      {"sourceSlug": "president", "sourceName": "Presidency", "verb": "SPREADS_TO", "targetSlug": "latin-american-republics", "targetName": "Latin American Republics (19th century)", "context": "The American presidential model spread first to the Latin American republics that emerged from Spanish colonial rule (1810–1825), making the presidency the standard form of executive government across the Western Hemisphere."}
    ],
    "places": [
      {"name": "United States of America (origin)", "role": "The birthplace of the modern presidential office — Philadelphia 1787, where the Constitutional Convention designed the presidency that became the global model"},
      {"name": "Global (130+ countries)", "role": "The contemporary geographic spread — the worldwide adoption of the presidential title as the standard designation for the republican head of state"}
    ],
    "subjects": ["Political History", "Government", "Classical Era", "American History", "Democracy", "Constitutional Law", "Modern History", "Political Science"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The presidency — invented by the American Constitutional Convention of 1787 and first embodied by George Washington — became the global template for republican executive government, used in various forms by over 130 countries. The design of the presidency (independently elected, fixed term, constitutionally limited executive power) was one of the most consequential political innovations of the modern era, shaping the form of government for much of the world and serving as both a model for democratic leadership and a potential pathway to authoritarian consolidation.",
      "significanceCategory": "world-changing"
    }
  }
},

"gratus-of-aosta": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250gratus-of-aosta.json",
  "slug": "gratus-of-aosta",
  "data": {
    "summary": "Gratus of Aosta (died 8 September 470 CE) was an early Christian bishop of Aosta (ancient Augusta Praetoria Salassorum) in the Aosta Valley of northwestern Italy — the Alpine valley at the head of the Great St. Bernard Pass, which was one of the most important mountain crossing points between Italy and the trans-Alpine regions (modern Switzerland and France). He is venerated as a saint in the Catholic Church with his feast day on 7 September, and he is the patron saint of Aosta. His episcopate falls in the late Roman and early sub-Roman period — the decades of the Western Roman Empire's final political collapse (Romulus Augustulus deposed 476 CE) and the establishment of Germanic successor kingdoms.\n\nGratus is associated in hagiographic tradition with the discovery of the head of John the Baptist — a relic tradition that connected Aosta to one of the most important relics in the Christian world and greatly enhanced the prestige of the local church. According to the legend, Gratus discovered the relic at Jerusalem during a pilgrimage and brought it back to Aosta, where it became the centrepiece of the local cult. This relic tradition, whether historically accurate or hagiographically constructed, was enormously important for establishing Aosta's ecclesiastical significance and for the subsequent development of pilgrimage to the cathedral.\n\nAosta's strategic position on the Via Francigena and the Great St. Bernard Pass made it an important node in the communications network between Rome and the trans-Alpine world — a significance that its bishop inherited and which gave the episcopal see of Aosta a prominence beyond its small size. Gratus represents the typical late antique bishop-saint whose cultus embedded a city's Christian identity in apostolic-era relic traditions, giving medieval Aosta its sacred foundations.",
    "causes": [
      "The Christianisation of the Alpine communities in the 4th–5th centuries CE — part of the broader post-Constantinian spread of episcopal organisation into the smaller cities and strategic locations of the Western Roman Empire — created the institutional context for Gratus's episcopate in Aosta.",
      "Aosta's strategic position on the Great St. Bernard Pass — one of the most important Alpine crossing points between Italy and trans-Alpine Europe — gave its bishop a prominence and a set of relationships (with travellers, pilgrims, and the flow of goods and people across the Alps) that exceeded what the town's size would otherwise warrant.",
      "The late antique tradition of relic acquisition and translation — the bringing of holy relics from the Holy Land and the major centres of Christian martyrdom to the smaller churches of the Western Empire — provided the mechanism through which Gratus could acquire the John the Baptist relic tradition that became central to his cultus."
    ],
    "effects": [
      "The relic of John the Baptist's head — attributed to Gratus's discovery and translation — became the centrepiece of the religious life of Aosta's cathedral, attracting pilgrims and enhancing the city's ecclesiastical prestige far beyond its administrative importance.",
      "Gratus's cult as patron saint of Aosta embedded the city's Christian identity in a sacred narrative connecting it to the apostolic era — the typical mechanism by which late antique cities established their place in the sacred geography of Latin Christendom.",
      "The cathedral of Aosta, dedicated to Gratus, became a significant stop on the Via Francigena pilgrimage route to Rome — the Alpine crossing that made Aosta's religious life intimately connected to the broader patterns of medieval pilgrimage and trans-Alpine communication."
    ],
    "relationships": [
      {"sourceSlug": "gratus-of-aosta", "sourceName": "Gratus of Aosta", "verb": "FOUNDS", "targetSlug": "diocese-of-aosta", "targetName": "Diocese of Aosta", "context": "Gratus was a founding bishop of Aosta — establishing the Christian community in this strategic Alpine city and becoming its patron saint."},
      {"sourceSlug": "gratus-of-aosta", "sourceName": "Gratus of Aosta", "verb": "ASSOCIATED_WITH", "targetSlug": "relic-of-john-the-baptist", "targetName": "Relic of John the Baptist's Head", "context": "Hagiographic tradition associates Gratus with the discovery and translation of John the Baptist's head — a relic that became central to Aosta's religious identity and pilgrimage significance."},
      {"sourceSlug": "via-francigena", "sourceName": "Via Francigena (pilgrimage route)", "verb": "CONNECTS", "targetSlug": "gratus-of-aosta", "targetName": "Gratus of Aosta (and Aosta's cult)", "context": "Aosta's position on the Via Francigena — the major pilgrimage and trans-Alpine route — made Gratus's cathedral an important stop in the medieval pilgrimage network from northern Europe to Rome."}
    ],
    "places": [
      {"name": "Aosta (Augusta Praetoria Salassorum), Aosta Valley, Italy", "role": "Gratus's episcopal city — the strategic Alpine city whose patron saint he became and whose religious identity he helped establish through the John the Baptist relic tradition"},
      {"name": "Great St. Bernard Pass, Alps", "role": "The strategic context — the most important Alpine crossing point that gave Aosta its significance as a node in trans-Alpine communications and pilgrimage"}
    ],
    "subjects": ["Early Christianity", "Late Roman Church", "Classical Era", "Italy", "Saints", "Alpine History", "Late Antiquity", "5th Century CE"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 3,
      "significanceNarrative": "Gratus of Aosta (died 470 CE) was the founding bishop and patron saint of Aosta in the Alpine Aosta Valley — associated in tradition with the discovery of John the Baptist's head, a relic that became central to the city's religious identity. His cult and Aosta's position on the Via Francigena made the cathedral a significant stop in medieval pilgrimage, giving this small Alpine city an ecclesiastical importance beyond its size.",
      "significanceCategory": "local"
    }
  }
},

"polyxenos-epiphanes-soter": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221polyxenos-epiphanes-soter.json",
  "slug": "polyxenos-epiphanes-soter",
  "data": {
    "summary": "Polyxenos Epiphanes Soter (Greek: Πολύξενος Ἐπιφανής Σωτήρ; 'the Illustrious Saviour'; died c. 160 BCE) was an Indo-Greek king — one of the rulers of the remarkable Indo-Greek kingdom that controlled portions of Bactria (modern Afghanistan) and northwestern India (modern Pakistan) following the Mauryan Empire's decline and in the wake of the Greco-Bactrian kingdom's fragmentation. Like many Indo-Greek rulers, his existence is known almost entirely through his coins — bilingual issues with Greek on one side and Kharoshthi (Indian script) on the other, and biscript legends that reflect the kingdom's hybrid Hellenistic-Indian cultural character.\n\nThe Indo-Greek kingdom (c. 200–10 BCE) was one of the most remarkable political phenomena of the ancient world: a series of Greek-speaking kings who ruled over mixed populations of Greek, Iranian, and Indian descent in the cultural and geographic frontier zone between the Hellenistic world and the Indian subcontinent. These kings issued the most sophisticated coinage of the ancient world — bilingual, biscript, and often of extraordinary artistic quality — demonstrating both the technical refinement of Hellenistic numismatic art and the administrative necessity of communicating with both Greek and Indian-language-speaking subjects. Some Indo-Greek rulers are known to have converted to Buddhism, and the Gandhara artistic tradition that produced the first Buddha images drew directly on Greek sculptural forms.\n\nPolyxenos's epithet 'Soter' ('Saviour') was a common Hellenistic royal title claiming divine protection and military victory. 'Epiphanes' ('the Illustrious' or 'the Manifest') was similarly a standard Hellenistic epithet. These Greek royal epithets — combined with the Kharoshthi legends and the eastern provenance of his coins — place Polyxenos squarely in the hybrid cultural world of the Indo-Greek frontier: a Hellenistic ruler who had adapted to the political and cultural conventions of the Indian subcontinent.",
    "causes": [
      "The fragmentation of the Greco-Bactrian kingdom following the death of Eucratides I (c. 145 BCE) and the pressure of the Scythian (Saka) and Parthian peoples from the northwest created the conditions in which multiple competing Indo-Greek kings controlled small territories — Polyxenos being one of these localised successors.",
      "The multicultural character of the Indo-Greek realm — Greek cities, Indian villages, Iranian herdsmen, Buddhist monasteries, and Zoroastrian communities coexisting in a frontier zone — required the bilingual administration reflected in Indo-Greek coinage, including Polyxenos's biscript issues.",
      "The Greek tradition of royal epithets and numismatic self-presentation — the elaborate coin portraits and titles through which Hellenistic kings projected authority and divine favour — was maintained by Indo-Greek rulers like Polyxenos even as they adapted to their Indian context."
    ],
    "effects": [
      "Polyxenos's coinage — the primary evidence for his reign — contributes to the numismatic record of the Indo-Greek kingdom, providing historians and archaeologists with evidence for the geographic extent of his authority and the artistic conventions of his court.",
      "The Indo-Greek kingdom of which Polyxenos was part left an enduring legacy in the Greco-Buddhist art of the Gandhara region — the synthesis of Greek sculptural forms with Buddhist iconography that created the first anthropomorphic Buddha images and influenced Buddhist art across Central and East Asia for centuries.",
      "The progressive displacement of Indo-Greek rulers by Saka, Parthian, and Kushan successors — the process within which Polyxenos's reign falls — eventually ended Greek political presence in the Indian subcontinent but left a lasting artistic and cultural legacy in the Gandhara tradition."
    ],
    "relationships": [
      {"sourceSlug": "polyxenos-epiphanes-soter", "sourceName": "Polyxenos Epiphanes Soter", "verb": "RULES", "targetSlug": "indo-greek-kingdom", "targetName": "Indo-Greek Kingdom (c. 200–10 BCE)", "context": "Polyxenos was an Indo-Greek king — one of the rulers of the remarkable Hellenistic-Indian hybrid kingdom of Bactria and northwestern India, known primarily through his bilingual coinage."},
      {"sourceSlug": "greco-buddhist-art", "sourceName": "Greco-Buddhist Art (Gandhara)", "verb": "EMERGES_FROM", "targetSlug": "polyxenos-epiphanes-soter", "targetName": "Indo-Greek Kingdom (including Polyxenos)", "context": "The Indo-Greek cultural synthesis — of which Polyxenos's reign was a part — produced the Greco-Buddhist artistic tradition that created the first Buddha images and influenced Buddhist iconography across Asia."},
      {"sourceSlug": "scythian-saka-peoples", "sourceName": "Scythian (Saka) Peoples", "verb": "DISPLACES", "targetSlug": "polyxenos-epiphanes-soter", "targetName": "Indo-Greek Kings including Polyxenos", "context": "The progressive Saka displacement of Indo-Greek rulers — the process that ended the Indo-Greek kingdom by c. 10 BCE — was already underway in Polyxenos's era, as the Scythian pressure from the northwest gradually reduced the Indo-Greek territories."}
    ],
    "places": [
      {"name": "Bactria and northwestern India (modern Afghanistan/Pakistan)", "role": "The territory of Polyxenos's kingdom — the Hellenistic-Indian frontier zone where the Indo-Greek kings ruled"},
      {"name": "Gandhara (modern northwestern Pakistan/eastern Afghanistan)", "role": "The cultural heartland of the Indo-Greek synthesis — the region where Greco-Buddhist art developed and from which it spread across Asia"}
    ],
    "subjects": ["Indo-Greek Kingdom", "Hellenistic History", "Classical Era", "Ancient India", "Numismatics", "Central Asia", "Buddhism", "Ancient History"],
    "frameworks": ["WORLD_SYSTEMS", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 3,
      "significanceNarrative": "Polyxenos Epiphanes Soter (died c. 160 BCE) was an Indo-Greek king of Bactria and northwestern India — one of the many rulers of the remarkable Hellenistic-Indian hybrid kingdom known almost entirely through bilingual coinage. His reign was part of the broader Indo-Greek cultural synthesis that produced Greco-Buddhist art — one of the most consequential artistic encounters of the ancient world, creating the first Buddha images and influencing Buddhist iconography across Asia.",
      "significanceCategory": "local"
    }
  }
},

"astronomy": {
  "filepath": "data/appwrite-export/entities/130-Class-130/130astronomy.json",
  "slug": "astronomy",
  "data": {
    "summary": "Astronomy is the natural science of celestial objects — stars, planets, moons, comets, asteroids, galaxies, and the universe as a whole — studying their positions, motions, physical properties, chemical composition, and origins through observation and theoretical analysis. It is the oldest of the natural sciences, with its roots in the naked-eye sky observations of ancient Mesopotamia, Egypt, Greece, India, China, and the pre-Columbian Americas, all of which developed systematic astronomical records and calendrical calculations thousands of years before the telescope existed. The regularity and grandeur of celestial phenomena — the seasonal cycle, the lunar calendar, the rising and setting of planets, the predictability of eclipses — made astronomy both practically essential (for agriculture, navigation, and timekeeping) and the paradigmatic domain of human attempts to understand the mathematical order of the cosmos.\n\nThe astronomical revolution of the 16th–17th centuries was one of the most consequential transformations in intellectual history: Copernicus's heliocentric model (De Revolutionibus, 1543) displaced the Earth from the centre of the cosmos; Brahe's precise naked-eye observations provided the data; Kepler's laws of planetary motion (1609–1619) described the elliptical orbits; Galileo's telescopic observations (1609) confirmed the Copernican system; and Newton's Principia Mathematica (1687) provided the gravitational mechanics that explained why planets move as they do. This sequence — the Copernican Revolution — is the archetypal scientific revolution, the model for how paradigms shift, and the event that established the authority of mathematical-empirical natural science over traditional theological cosmology.\n\nModern astronomy encompasses a vast range of sub-disciplines — planetary astronomy, stellar astronomy, galactic astronomy, cosmology, astrobiology — and observes the universe across the entire electromagnetic spectrum (radio, infrared, visible, ultraviolet, X-ray, gamma-ray) as well as through gravitational wave detection (LIGO, 2015) and neutrino astronomy. The James Webb Space Telescope (launched 2021), with its infrared sensitivity, has revealed galaxies forming within 300 million years of the Big Bang, pushing the observational frontier to the universe's earliest epochs.",
    "causes": [
      "The universal human observation of the regular cycles of the sky — day and night, the lunar month, the solar year, the predictable rising of constellations — and their intimate connection to agriculture, navigation, and ritual created the practical and spiritual motivation for systematic astronomical record-keeping in virtually every ancient culture.",
      "The development of mathematics — particularly geometry (Greece) and arithmetic (Babylonia, India, China) — provided the computational tools necessary to model and predict celestial motions, transforming observation into quantitative astronomy and enabling the prediction of eclipses, planetary positions, and other celestial events.",
      "The invention of the telescope (Lippershey, 1608; Galileo's astronomical use, 1609) and the development of spectroscopy (Fraunhofer, 1814; Kirchhoff and Bunsen, 1859) gave astronomers the technological means to observe celestial phenomena beyond naked-eye capability and to determine the chemical composition of stars and galaxies — expanding astronomy from positional to astrophysical science."
    ],
    "effects": [
      "The Copernican Revolution — astronomy's replacement of the Earth-centred cosmos with the Sun-centred solar system, and ultimately with the infinite, directionless universe of modern cosmology — was one of the most consequential intellectual transformations in human history, dethroning humanity from its assumed central position in the cosmos and establishing the authority of mathematical-empirical science over theological tradition.",
      "Practical astronomy — navigation, calendrical calculation, timekeeping — was essential to the European Age of Discovery: the celestial navigation methods that enabled Portuguese, Spanish, and later Dutch and English ships to sail across oceans and find their way back were the direct practical application of the astronomical knowledge accumulated since ancient times.",
      "Modern cosmological astronomy — the Big Bang model, dark matter and dark energy, the cosmic microwave background, gravitational waves — has established the scientific picture of a universe 13.8 billion years old, containing two trillion galaxies, expanding from a hot dense state, and composed primarily of forms of matter and energy invisible to normal observation, profoundly challenging any naive human-centred cosmology."
    ],
    "relationships": [
      {"sourceSlug": "astronomy", "sourceName": "Astronomy", "verb": "REVOLUTIONISED_BY", "targetSlug": "nicolaus-copernicus", "targetName": "Nicolaus Copernicus (De Revolutionibus, 1543)", "context": "Copernicus's heliocentric model — placing the Sun rather than the Earth at the centre of the solar system — initiated the Copernican Revolution that transformed astronomy, philosophy, and humanity's self-understanding."},
      {"sourceSlug": "galileo-galilei", "sourceName": "Galileo Galilei (1564–1642)", "verb": "TRANSFORMS", "targetSlug": "astronomy", "targetName": "Astronomy (telescopic revolution)", "context": "Galileo's use of the telescope to observe the moons of Jupiter, the phases of Venus, and the mountains of the Moon provided the first observational confirmation of the Copernican system and inaugurated telescopic astronomy."},
      {"sourceSlug": "astronomy", "sourceName": "Astronomy", "verb": "ENABLES", "targetSlug": "age-of-discovery", "targetName": "European Age of Discovery (15th–17th centuries)", "context": "Celestial navigation — the practical application of astronomical knowledge to determine position at sea — was essential to the European maritime exploration that transformed the world in the 15th–17th centuries."}
    ],
    "places": [
      {"name": "Global (universal — Mesopotamia, Egypt, Greece, India, China, Americas)", "role": "The universal scope of astronomical observation — present in every ancient civilisation as a practical and intellectual necessity, with multiple independent traditions of systematic sky-watching"},
      {"name": "Europe (16th–17th century revolution) and Global (modern telescopes)", "role": "The geographic centre of the Copernican Revolution and modern astronomy — European observatories and subsequently global telescope networks and space observatories"}
    ],
    "subjects": ["Astronomy", "Natural Sciences", "Classical Era", "Cosmology", "History of Science", "Scientific Revolution", "Astrophysics", "Mathematics"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Astronomy is the oldest natural science — present in every ancient civilisation — whose transformation in the Copernican Revolution (Copernicus 1543, Galileo, Kepler, Newton) was one of the most consequential intellectual events in human history: dethroning Earth from the centre of the cosmos, establishing the authority of mathematical-empirical science, and enabling the celestial navigation of the Age of Discovery. Modern astronomy has revealed a universe 13.8 billion years old, containing two trillion galaxies — a cosmological picture that continues to transform human self-understanding.",
      "significanceCategory": "world-changing"
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
