#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 15 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: java, prehistory, harald-klak, syrus-of-genoa,
          sociology, eannatum-ii, tiberius-julius-sauromates-i, zidanta-ii
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-15-may2026"

ENRICHMENTS = {

"java": {
  "filepath": "data/appwrite-export/entities/136-Class-136/136java.json",
  "slug": "java",
  "data": {
    "summary": "Java is a high-level, general-purpose, object-oriented programming language developed by Sun Microsystems — primarily by James Gosling — with its first public release in 1995. Java was designed around the principle of 'Write Once, Run Anywhere' (WORA): Java source code is compiled to bytecode that runs on the Java Virtual Machine (JVM), an abstract computing machine that can be implemented on any hardware or operating system, making Java programmes inherently portable across platforms. This design philosophy — and Java's combination of object-oriented structure, memory safety (automatic garbage collection), strong typing, and large standard library — made Java one of the most widely adopted programming languages in the world, and it dominated enterprise software development and server-side programming for over two decades.\n\nJava's trajectory after its 1995 release was shaped by several key moments: its adoption for web browser applets (which briefly made Java the primary client-side web technology before being superseded by JavaScript), its use as the primary language for Android mobile application development (announced 2008, which gave Java a second era of massive adoption), its central role in enterprise server-side development through Java EE (now Jakarta EE) and frameworks like Spring and Hibernate, and its acquisition by Oracle through the purchase of Sun Microsystems in 2010. The Oracle acquisition led to the Java vs. Google lawsuit (Oracle v. Google) — a decade-long legal dispute over whether Google's use of Java APIs in Android constituted copyright infringement, ultimately resolved in Google's favour by the US Supreme Court in 2021.\n\nJava's influence on the broader programming ecosystem has been immense: it popularised object-oriented programming and design patterns for a generation of developers, its JVM became the platform for numerous other languages (Kotlin, Scala, Clojure, Groovy), and its ecosystem of tools, frameworks, and libraries set the standard for enterprise software development. By the 2020s, Java had been joined by Kotlin (the preferred Android language since Google's 2017 designation) and Python as dominant general-purpose languages, but remained one of the most widely used languages worldwide.",
    "causes": [
      "Sun Microsystems' 'Green Project' (1991), initiated to develop software for consumer electronics and cable TV set-top boxes, created the technical and design requirements — portability, reliability, security — that shaped Java's architecture; the project was redirected toward internet applications as the World Wide Web's commercial potential became clear.",
      "The explosion of the World Wide Web in 1994–1995 — and the internet's need for platform-independent, network-capable, safe code that could be distributed across diverse hardware — created the perfect market for Java's 'Write Once, Run Anywhere' design philosophy.",
      "Sun Microsystems' deliberate strategy of making Java free to use and developing it as an open standard (though with Sun retaining control of the specification) — combined with aggressive marketing of Java as the solution to the fragmented computing landscape — drove the rapid adoption that made Java dominant in enterprise computing by the late 1990s."
    ],
    "effects": [
      "Java's WORA principle and its popularisation of object-oriented programming fundamentally shaped software engineering practice for two decades — its design patterns book (1994 Gang of Four) and its enterprise frameworks (Spring, Hibernate, EJB) defined how large-scale software systems were designed, tested, and deployed from the late 1990s through the 2010s.",
      "Java's adoption as the primary Android development language (2008) gave it a second major wave of adoption that extended its relevance into the mobile era — making Java-based Android development the dominant mobile programming environment until Kotlin's rise in the 2017–2020 period.",
      "The Oracle v. Google lawsuit — centred on Java API copyright — became one of the most consequential intellectual property cases in software history, with the US Supreme Court's 2021 ruling in Google's favour establishing important precedents for software interoperability and the limits of API copyright protection."
    ],
    "relationships": [
      {"sourceSlug": "java", "sourceName": "Java (programming language)", "verb": "ENABLES", "targetSlug": "android-platform", "targetName": "Android Mobile Platform", "context": "Java was the primary programming language for Android app development (2008–2017) — Google's choice of Java for Android gave it a massive second wave of adoption in the mobile era."},
      {"sourceSlug": "java", "sourceName": "Java (programming language)", "verb": "INSPIRES", "targetSlug": "jvm-languages", "targetName": "JVM Languages (Kotlin, Scala, Clojure)", "context": "Java's JVM became the platform for numerous other programming languages — Kotlin (Android preferred language since 2017), Scala, Clojure, and Groovy all run on the JVM and were shaped by Java's design."},
      {"sourceSlug": "oracle-corporation", "sourceName": "Oracle Corporation", "verb": "ACQUIRES", "targetSlug": "java", "targetName": "Java (via Sun Microsystems acquisition 2010)", "context": "Oracle's acquisition of Sun Microsystems in 2010 transferred Java's stewardship to Oracle, leading to the Oracle v. Google lawsuit that became a landmark software copyright case."}
    ],
    "places": [
      {"name": "Silicon Valley, California, USA", "role": "The birthplace of Java — Sun Microsystems was headquartered in Santa Clara, California, and the Java language was developed there"},
      {"name": "Global Internet / Enterprise Computing", "role": "The operational environment of Java — the worldwide web and enterprise computing infrastructure on which Java became the dominant server-side and application language"}
    ],
    "subjects": ["Programming Languages", "Computer Science", "Contemporary Era", "Software Engineering", "Technology", "Internet History", "Object-Oriented Programming", "Enterprise Software"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Java is one of the most influential programming languages in the history of computing — its 'Write Once, Run Anywhere' design philosophy, popularisation of object-oriented programming, dominance in enterprise server-side development, and role as the primary Android language have shaped software engineering for 30 years. Its JVM became the platform for multiple languages and its ecosystem defined how large-scale software is built.",
      "significanceCategory": "world-changing"
    }
  }
},

"prehistory": {
  "filepath": "data/appwrite-export/entities/910-Class-910/910prehistory.json",
  "slug": "prehistory",
  "data": {
    "summary": "Prehistory is the term for the period of human existence before the invention of writing — the vast majority of human history, spanning from the emergence of the genus Homo (c. 2.5 million years ago) to the development of writing systems in different regions at different times (c. 3200 BCE in Mesopotamia, c. 3000 BCE in Egypt, c. 2600 BCE in the Indus Valley, c. 1200 BCE in China, c. 900 BCE in Mesoamerica). The term 'prehistory' itself is a historiographical construct: since written records are the conventional definition of 'history', prehistory is defined by its absence — it is the period known only through the physical evidence of archaeology, palaeontology, genetics, and related sciences rather than through written testimony.\n\nPrehistory encompasses the overwhelming bulk of human experience: the Palaeolithic period (Old Stone Age, c. 3.3 million–10,000 BCE), during which anatomically modern humans (Homo sapiens) evolved in Africa (c. 300,000 years ago), mastered fire, developed language, created art (the cave paintings of Lascaux and Altamira, the Venus figurines), and spread across every continent except Antarctica; the Mesolithic period (c. 10,000–5,000 BCE in many regions), characterised by the transition from purely hunter-gatherer economies toward more complex subsistence strategies; and the Neolithic period (c. 10,000–3,000 BCE), during which the agricultural revolution transformed human society — the domestication of plants and animals, the development of permanent settlements, and the beginnings of social complexity that eventually produced the first states and writing systems.\n\nThe study of prehistory has been revolutionised in the late 20th and early 21st centuries by the development of new scientific methods: radiocarbon dating (from 1949), dendrochronology, archaeogenomics (ancient DNA analysis), and isotope analysis have allowed prehistorians to reconstruct human migrations, population histories, diet, and social organisation with precision impossible for earlier generations. The ancient DNA revolution in particular — associated with the work of Svante Pääbo (Nobel Prize 2022) — has transformed understanding of early human migrations, the interbreeding of Homo sapiens with Neanderthals and Denisovans, and the complex genetic history of the first populations to settle every region of the world.",
    "causes": [
      "The biological evolution of the genus Homo over 2.5 million years — the development of larger brains, bipedalism, manual dexterity, and language — produced the cognitive and social capabilities that enabled prehistoric human populations to spread across the globe, develop culture, and eventually create the conditions for the agricultural revolution and the origins of writing.",
      "The development of agriculture (the Neolithic Revolution, c. 10,000 BCE in the Fertile Crescent, independently in multiple world regions) was the transformative economic transition that enabled population growth, social stratification, specialisation of labour, and eventually the urban complexity that produced writing — ending prehistory and beginning history.",
      "The climate stabilisation of the Holocene epoch (c. 11,700 years ago) — following the end of the last glacial period — provided the relatively stable and warm environmental conditions that made sedentary agriculture possible and drove the Neolithic demographic and economic transformation."
    ],
    "effects": [
      "The prehistoric development of agriculture, settled communities, and social complexity — the Neolithic revolution — produced the population densities, economic surpluses, and social structures that led to the first cities, states, and writing systems, ending prehistory and creating the conditions for recorded history.",
      "The prehistoric dispersal of Homo sapiens out of Africa (c. 70,000–50,000 years ago) and across every continent produced the global human population whose genetic, linguistic, and cultural diversity is the foundation of all subsequent human history — prehistoric migrations are the ultimate explanation for the distribution of world languages, genetic haplogroups, and cultural traditions.",
      "Prehistoric technological innovations — the mastery of fire, the development of stone tools (lithic technology), the invention of pottery, metallurgy, and the wheel — created the cumulative technological foundation on which all subsequent civilisational development was built."
    ],
    "relationships": [
      {"sourceSlug": "prehistory", "sourceName": "Prehistory", "verb": "PRECEDES", "targetSlug": "ancient-civilisations", "targetName": "Ancient Civilisations (First Writing Cultures)", "context": "Prehistory ends with the invention of writing in different world regions — the transition that marks the beginning of recorded human history and the first civilisations of Mesopotamia, Egypt, and China."},
      {"sourceSlug": "neolithic-revolution", "sourceName": "Neolithic Revolution (c. 10,000 BCE)", "verb": "TRANSFORMS", "targetSlug": "prehistory", "targetName": "Late Prehistory", "context": "The Neolithic agricultural revolution was the defining transformation of late prehistory — the domestication of plants and animals that produced the population growth and social complexity ending in the first cities and writing."},
      {"sourceSlug": "homo-sapiens", "sourceName": "Homo sapiens (anatomically modern humans)", "verb": "CREATES", "targetSlug": "prehistory", "targetName": "Human Prehistory", "context": "Prehistoric human culture — from the earliest Palaeolithic tools to cave art to agricultural settlements — was created by Homo sapiens, whose cognitive revolution c. 50,000 years ago produced the symbolic and cultural richness of the archaeological record."}
    ],
    "places": [
      {"name": "Africa (cradle of Homo sapiens)", "role": "The continent of human evolutionary origins — where anatomically modern humans evolved c. 300,000 years ago and from which they dispersed across the globe"},
      {"name": "Fertile Crescent (Middle East)", "role": "The region of the first agricultural revolution (c. 10,000 BCE) — the origin point of Neolithic farming that ended prehistory for the Near East and transformed human civilisation"},
      {"name": "Global (all continents except Antarctica)", "role": "The geographic scope of prehistoric human habitation — Homo sapiens settled every continent before the invention of writing"}
    ],
    "subjects": ["Prehistory", "Human Evolution", "Prehistoric Era", "Archaeology", "Ancient History", "Palaeolithic", "Neolithic", "Human Origins"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Prehistory — the 2.5 million years of human existence before writing — encompasses the overwhelming bulk of human experience: the evolution and global dispersal of Homo sapiens, the mastery of fire and tool-making, the creation of art, and the Neolithic agricultural revolution that produced the first cities and writing. It is the foundational period from which all subsequent history emerged.",
      "significanceCategory": "world-changing"
    }
  }
},

"harald-klak": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221harald-klak.json",
  "slug": "harald-klak",
  "data": {
    "summary": "Harald Klak (c. 785–852 CE) was a Danish Viking king who became the first Scandinavian ruler to be baptised as a Christian — an event of enormous symbolic and practical significance for the subsequent Christianisation of Scandinavia. Harald was baptised at Mainz in 826 CE along with his wife and entourage, at the court of the Frankish emperor Louis the Pious. The ceremony was a state affair: Harald received Louis as his godfather, was given rich gifts and the duchy of Rüstringen in Frisia as his base, and was provided with the Frankish missionary Ansgar — the 'Apostle of the North' — as a companion to accompany him back to Denmark and begin the Christianisation of Scandinavia.\n\nHarald Klak's political career was dominated by the instability of Danish royal succession in the early 9th century — a period of persistent civil war between multiple claimants to the Danish throne. Harald was expelled from Denmark multiple times and returned with Frankish support; his conversion to Christianity was as much a political act — cementing his alliance with the Frankish Empire — as a religious one. He spent much of his later career as a Frankish vassal based in Frisia, ruling the island base of Walcheren and conducting Viking raids on behalf of Frankish interests as well as his own.\n\nDespite his political failures in Denmark (he never permanently consolidated the Danish throne and his attempted Christianisation of Denmark did not immediately succeed), Harald Klak's baptism and his partnership with Ansgar initiated the missionary enterprise that would eventually Christianise Scandinavia. Ansgar's subsequent missions to Denmark and Sweden — partially enabled by his association with Harald — laid the groundwork for the eventual conversion of the Scandinavian peoples, which was substantially complete by c. 1000 CE (Norway under Olaf Tryggvason and Olaf Haraldsson, Denmark under Harald Bluetooth, Sweden somewhat later).",
    "causes": [
      "The instability of Danish royal succession in the early 9th century — the persistent competition between Harald Klak and the Horik dynasty for control of the Danish throne — drove Harald to seek Frankish imperial support, creating the political context for his baptism as a symbolic act of alliance with Louis the Pious.",
      "The Frankish Empire's interest in pacifying and eventually Christianising the Viking neighbours on its northern border — the missionary ambition that led Louis the Pious to sponsor Harald's baptism and send Ansgar as a missionary companion — created the imperial context for Harald's conversion.",
      "The Viking Age's political dynamics — in which successful leaders needed both military strength and powerful patron-allies — made the Frankish connection (sealed by baptism and imperial godparenthood) an attractive political strategy for Harald despite his subsequent failures in Denmark."
    ],
    "effects": [
      "Harald Klak's baptism (826 CE) and his bringing of the missionary Ansgar to Scandinavia initiated the Christianisation process that would transform Scandinavian societies over the following two centuries — the first concrete step in the missionary enterprise that eventually produced Christian Denmark, Norway, and Sweden.",
      "Ansgar's missionary journeys to Denmark and Sweden — enabled by his connection with Harald — established the first Christian churches and communities in Scandinavia, creating an institutional foothold for subsequent evangelisation even though Ansgar's immediate results were limited.",
      "The model of Viking rulers converting to Christianity as a means of gaining access to Frankish imperial patronage, territory, and support — exemplified by Harald Klak — was repeated by subsequent Viking leaders (including Rollo of Normandy in 911 CE) and became a standard mechanism of Viking integration into the Carolingian political world."
    ],
    "relationships": [
      {"sourceSlug": "harald-klak", "sourceName": "Harald Klak", "verb": "ACCEPTS_BAPTISM_FROM", "targetSlug": "louis-the-pious", "targetName": "Louis the Pious (Emperor)", "context": "Harald Klak's baptism at Mainz in 826 CE — with Louis the Pious as his godfather — was the first Christian baptism of a Danish ruler and the political seal of the Frankish-Danish alliance."},
      {"sourceSlug": "ansgar", "sourceName": "Ansgar (Apostle of the North)", "verb": "ACCOMPANIES", "targetSlug": "harald-klak", "targetName": "Harald Klak", "context": "Ansgar accompanied Harald Klak back to Denmark in 826 CE as a missionary — his subsequent missions to Denmark and Sweden (made possible by the Harald connection) initiated the Christianisation of Scandinavia."},
      {"sourceSlug": "christianisation-of-scandinavia", "sourceName": "Christianisation of Scandinavia", "verb": "BEGINS_WITH", "targetSlug": "harald-klak", "targetName": "Harald Klak", "context": "Harald Klak's baptism was the symbolic beginning of Scandinavian Christianisation — the first step in a centuries-long process that was substantially complete by c. 1000 CE."}
    ],
    "places": [
      {"name": "Mainz, Frankish Empire (Germany)", "role": "The site of Harald Klak's baptism (826 CE) — Louis the Pious's court at Mainz where the state ceremony was held"},
      {"name": "Denmark", "role": "Harald's native kingdom — the target of his political ambitions and the initial objective of Ansgar's missionary work, which Harald's conversion inaugurated"},
      {"name": "Frisia (Netherlands/Germany coast)", "role": "Harald's Frankish vassal base — the territory granted to him by Louis the Pious as his operational base after his baptism"}
    ],
    "subjects": ["Viking Age", "Christianisation", "Classical Era", "Scandinavia", "Frankish Empire", "Medieval History", "Denmark", "Early Medieval"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Harald Klak was the first Danish king baptised as a Christian (Mainz, 826 CE) — an event that initiated the Christianisation of Scandinavia. His political alliance with Louis the Pious and his bringing of Ansgar to Denmark set in motion the missionary process that converted the Viking world over the following two centuries. Though Harald himself never permanently held the Danish throne, his baptism was the first concrete step in the transformation of Scandinavian religious culture.",
      "significanceCategory": "significant"
    }
  }
},

"syrus-of-genoa": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250syrus-of-genoa.json",
  "slug": "syrus-of-genoa",
  "data": {
    "summary": "Syrus of Genoa (died 29 June 381 CE) was the first Bishop of Genoa — a founding figure of the Christian church in the Ligurian coastal city of Genua (Roman Genoa, modern Genoa in northwestern Italy) — venerated as a saint in the Catholic Church with feast day on 29 June. He is credited with the establishment of the Christian episcopal community in Genoa during the reign of the Emperor Constantius II or, by some traditions, earlier. The evidence for his life is entirely hagiographic and liturgical — the traditions preserved in the church of Genoa about its founding bishop, which place him in the 4th century and identify him as the organiser of the earliest Christian community in the city.\n\nGenoa's position on the Ligurian coast — strategically located on the western Ligurian sea between the Alpine passes and the Mediterranean — made it a significant port city in the late Roman Empire, and its Christianisation was part of the broader pattern of episcopal organisation that transformed the cities of northern Italy into Christian communities under the influence of the Milanese church (under Ambrose of Milan, 374–397 CE). Like Felix of Como (contemporaneous first bishop of Como), Syrus of Genoa represents the founding figures of the northern Italian diocesan network whose memory was preserved primarily through their churches' liturgical tradition.\n\nThe cult of Syrus at Genoa was perpetuated through the cathedral dedicated to him — the Cattedrale di San Siro (later replaced by the Cathedral of San Lorenzo as Genoa's primary church) — and through the liturgical calendar of the Genoese church. The medieval commune of Genoa, which became one of the great maritime republics of medieval Italy, inherited the civic Christian identity whose institutional foundation was laid by the episcopates of Syrus and his successors.",
    "causes": [
      "The post-Constantinian reorganisation of the western church — the systematic establishment of episcopal sees in the major cities of the empire following Constantine's conversion (312 CE) and the Edict of Milan (313 CE) — provided the institutional context for the establishment of a bishop at the strategically important port of Genoa.",
      "Genoa's commercial importance as a Ligurian port city — its role in the maritime trade of the western Mediterranean and its connection to the Po plain via the Ligurian passes — made it a natural site for an episcopal see as the church organised itself in the cities of northern Italy.",
      "Ambrose of Milan's dominant influence over the northern Italian church — his organisation of suffragen sees throughout the Milanese metropolitan province — provided the specific ecclesiastical context in which the Genoese diocese was organised and Syrus was appointed."
    ],
    "effects": [
      "Syrus's establishment of the Genoese diocese created the institutional foundation for the Christian community of Genoa — the church that would persist through the fall of the Western Roman Empire, the Lombard invasion of northern Italy, and the emergence of medieval Genoa as one of the great maritime republics.",
      "The cult of Syrus at Genoa — centred on the church dedicated to him (later Cathedral of San Siro) — provided the civic religious identity of early medieval Genoa and was maintained through the subsequent centuries of the city's growth to maritime prominence.",
      "The northern Italian diocesan network of which Syrus's Genoese see was a part — established under Ambrosian influence in the late 4th century — provided the ecclesiastical infrastructure through which the Christianisation of the Ligurian coast and the Alpine foothills proceeded in the 5th–6th centuries."
    ],
    "relationships": [
      {"sourceSlug": "syrus-of-genoa", "sourceName": "Syrus of Genoa", "verb": "FOUNDS", "targetSlug": "diocese-of-genoa", "targetName": "Diocese of Genoa", "context": "Syrus was the founding bishop of Genoa — establishing the diocese that became the institutional foundation of the Christian community in this strategically important Ligurian port city."},
      {"sourceSlug": "ambrose-of-milan", "sourceName": "Ambrose of Milan", "verb": "INFLUENCES", "targetSlug": "syrus-of-genoa", "targetName": "Syrus of Genoa", "context": "The Milanese church under Ambrose of Milan (374–397 CE) provided the dominant influence on the northern Italian diocesan network within which Syrus's episcopate at Genoa was established."},
      {"sourceSlug": "late-roman-church", "sourceName": "Late Roman Church (4th Century)", "verb": "PRODUCES", "targetSlug": "syrus-of-genoa", "targetName": "Syrus of Genoa", "context": "Syrus was a product of the post-Constantinian church's systematic episcopal organisation — the transformation of Christianity from persecuted minority to state institution that created the network of city bishops across the western empire."}
    ],
    "places": [
      {"name": "Genoa (Genua), Liguria, Italy", "role": "Syrus's episcopal city — the Ligurian port whose Christian community he founded and whose cathedral bore his name for centuries"},
      {"name": "Northwestern Italy / Liguria", "role": "The regional context of Syrus's diocese — the coastal zone between the Alps and the Ligurian Sea where Genoa's strategic and commercial importance made episcopal organisation essential"}
    ],
    "subjects": ["Early Christianity", "Late Roman Church", "Classical Era", "Italy", "Church Organisation", "4th Century CE", "Genoa", "Saints"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 3,
      "significanceNarrative": "Syrus of Genoa was the founding bishop of Genoa (died 381 CE) — establishing the diocese in the strategically important Ligurian port city during the post-Constantinian organisation of the northern Italian church. His cult was perpetuated through the Cathedral of San Siro (Genoa's first cathedral), and he represents the founding figures of the northern Italian diocesan network established under Ambrosian influence.",
      "significanceCategory": "local"
    }
  }
},

"sociology": {
  "filepath": "data/appwrite-export/entities/120-Class-120/120sociology.json",
  "slug": "sociology",
  "data": {
    "summary": "Sociology is the scientific study of human social life, groups, organisations, and societies — the academic discipline that emerged in the 19th century as a systematic attempt to apply scientific methods to the study of the social world. The term was coined by Auguste Comte (1798–1857), who proposed sociology as the queen of the sciences — the discipline that would synthesise all knowledge about human affairs and provide a scientific basis for social reform and the organisation of modern industrial society. Comte's positivism — the programme of applying empirical scientific method to social phenomena — laid the philosophical foundation for sociology's ambition to be a science of society analogous to the natural sciences.\n\nThe classical period of sociological theory (c. 1840–1920) produced the discipline's foundational frameworks: Émile Durkheim (1858–1917) demonstrated the power of sociological explanation through his studies of suicide, religion, and the division of labour — arguing that social facts (such as suicide rates) could not be reduced to individual psychology and required specifically sociological explanation. Max Weber (1864–1920) developed interpretive sociology and the concepts of social action, bureaucracy, rationalisation, and the Protestant Ethic and the Spirit of Capitalism — his thesis that Protestant Calvinist culture promoted capitalist economic attitudes becoming one of the most debated propositions in modern social science. Karl Marx's historical materialism — the theory that the material organisation of production determines social structure and ideology — was another founding framework, though Marx himself was not primarily a sociologist.\n\nIn the 20th century, sociology diversified into numerous sub-fields and theoretical schools: structural functionalism (Talcott Parsons), conflict theory, symbolic interactionism, ethnomethodology, feminist sociology, critical theory (the Frankfurt School), and postmodern sociology (Bourdieu, Giddens, Foucault as interlocutors). Sociological methods expanded from survey research and statistical analysis to ethnography, interviews, discourse analysis, and computational social science, making sociology one of the most methodologically diverse disciplines in the social sciences.",
    "causes": [
      "The Industrial Revolution and the social dislocations of 19th-century urbanisation, class conflict, and the disruption of traditional communities — the 'social question' of how to understand and manage the new industrial society — created the intellectual demand for a scientific study of social life that sociology was designed to meet.",
      "The Enlightenment tradition of applying reason and empirical method to understanding the natural world — and its extension to social institutions by thinkers like Montesquieu, Condorcet, and Saint-Simon — provided the intellectual precedents for Comte's positivist programme of a science of society.",
      "The institutional development of the modern university in the 19th century — and the creation of academic disciplines with their own journals, professional associations, and curricula — provided the institutional infrastructure within which sociology could establish itself as an academic field."
    ],
    "effects": [
      "Sociology's development of theoretical frameworks — Durkheim's social facts, Weber's rationalism and bureaucracy, Marx's class analysis — provided the conceptual tools that shaped how modern societies understand themselves, their institutions, and their problems; these frameworks influenced policy, law, education, and political thought across the 20th century.",
      "The sociological concept of social structure — the idea that human behaviour is shaped by patterns of social organisation, norms, institutions, and inequalities that exist independently of individual will — has become a fundamental presupposition of modern social science, politics, and policy, shaping how modern states approach poverty, crime, education, and health.",
      "Sociology's sub-disciplines — medical sociology, criminology, urban sociology, the sociology of education, organisational sociology, gender and race studies — have produced empirical research and theoretical frameworks that directly inform professional practice, policy-making, and social reform in every domain of modern life."
    ],
    "relationships": [
      {"sourceSlug": "sociology", "sourceName": "Sociology", "verb": "FOUNDED_BY", "targetSlug": "auguste-comte", "targetName": "Auguste Comte", "context": "Comte coined the term 'sociology' and proposed it as the capstone science of human affairs — his positivist programme of applying scientific method to social life laid the philosophical foundation for the discipline."},
      {"sourceSlug": "emile-durkheim", "sourceName": "Émile Durkheim", "verb": "SHAPES", "targetSlug": "sociology", "targetName": "Sociology", "context": "Durkheim's empirical studies of suicide, religion, and the division of labour established the canonical methods and central concepts of academic sociology — his social facts approach defined sociology's explanatory distinctiveness from psychology."},
      {"sourceSlug": "max-weber", "sourceName": "Max Weber", "verb": "SHAPES", "targetSlug": "sociology", "targetName": "Sociology", "context": "Weber's interpretive sociology, his concepts of bureaucracy, rationalisation, and social action, and his Protestant Ethic thesis are foundational to sociology's theoretical heritage — his approach to social explanation remains one of the discipline's central methodological traditions."}
    ],
    "places": [
      {"name": "France (Paris), Germany, United States", "role": "The primary national centres of early sociology's development — Comte and Durkheim in France, Weber and Simmel in Germany, Chicago School in the USA"},
      {"name": "Industrial Europe", "role": "The social context that generated sociology — the Industrial Revolution's urban dislocations, class conflicts, and moral questions that made a science of society seem both possible and necessary"}
    ],
    "subjects": ["Social Science", "Academic Disciplines", "Modern Era", "Sociology", "Social Theory", "Intellectual History", "19th Century", "Social Science History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Sociology is one of the foundational social sciences — coined by Auguste Comte in the 19th century and developed by Durkheim, Weber, and Marx into a discipline whose theoretical frameworks (social structure, bureaucracy, class, rationalisation) have shaped how modern societies understand themselves and their problems. Its concepts permeate policy, law, education, and political thought across the 20th–21st centuries.",
      "significanceCategory": "world-changing"
    }
  }
},

"eannatum-ii": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221eannatum-ii.json",
  "slug": "eannatum-ii",
  "data": {
    "summary": "Enannatum II (also Eannatum II; fl. c. 2350 BCE) was a ruler (ensi) of the Sumerian city-state of Lagash — one of the kings in the sequence of Lagashite rulers of the Early Dynastic III period of ancient Sumer, documented in the Sumerian King List and in inscriptions from Lagash. He should be distinguished from the more famous Eannatum I (c. 2454–2425 BCE), who was one of Lagash's greatest military kings and the creator of the 'Stele of the Vultures' — the earliest surviving detailed war monument in human history, commemorating the defeat of the rival city-state Umma. Enannatum II was a later ruler in the Lagashite dynasty, appearing after the reign of Eannatum I and his successors in the dynastic sequence.\n\nThe specific historical record for Enannatum II is thin: he appears in royal inscriptions and the king list as part of the Lagashite sequence, but without the detailed military narratives that make Eannatum I and other Lagashite kings (like Uruinimgina) more fully documented. His reign falls in the complex late Early Dynastic III period when the power of individual Sumerian city-states was being challenged by the growing supremacy of Akkad — a process that would culminate in Sargon of Akkad's conquests (c. 2334 BCE) and the creation of the first Mesopotamian empire. Enannatum II's Lagash was still engaged in the recurring conflict with Umma (the border dispute that had defined Lagashite history since the time of Ush of Umma centuries earlier) and in the internal political tensions that preceded the reform period of Uruinimgina.\n\nLagash's significance in the broader context of Sumerian history lies partly in the exceptional quality of its archaeological record: the excavations at Telloh (ancient Girsu, Lagash's principal city) produced an extraordinary corpus of cuneiform inscriptions, including the 'Lagashite King List' that is one of the primary sources for Early Dynastic chronology and for the Lagash-Umma border conflict.",
    "causes": [
      "The Early Dynastic III period's political structure — the competing city-state system of Sumer in which Lagash, Umma, Uruk, Kish, and other cities vied for regional supremacy — created the political environment within which Enannatum II's reign unfolded.",
      "The ongoing Lagash-Umma border conflict — the recurring competition over the Gu-edena boundary zone that had been initiated by Ush of Umma and that Eannatum I had temporarily resolved through military victory — provided the persistent external challenge that defined Lagashite royal activity in this period.",
      "The internal dynamics of Lagashite succession and royal authority — the traditions of the ensi office and the economic and political power of the great Lagashite temples — shaped the context within which Enannatum II exercised his authority."
    ],
    "effects": [
      "Enannatum II's reign contributed to the continuity of Lagashite political power during the late Early Dynastic period — maintaining the dynasty that would end with Uruinimgina's reform reign and the subsequent Akkadian conquest.",
      "The Lagashite king list and royal inscriptions of which Enannatum II is a part constitute one of the most valuable documentary records of Early Dynastic Sumer — providing historians with the chronological framework for understanding the political sequence of the period before the Akkadian empire.",
      "Lagash's continued resistance to Umma throughout the reigns of rulers like Enannatum II sustained the centuries-long border conflict that is one of the best-documented instances of interstate warfare in the ancient world, illustrating the geopolitical dynamics of the city-state system."
    ],
    "relationships": [
      {"sourceSlug": "eannatum-ii", "sourceName": "Enannatum II", "verb": "RULES", "targetSlug": "lagash", "targetName": "Lagash (Sumerian City-State)", "context": "Enannatum II was an ensi (ruler) of Lagash — one of the late Early Dynastic rulers in the Lagashite dynasty documented in the king list and royal inscriptions."},
      {"sourceSlug": "lagash-umma-wars", "sourceName": "Lagash-Umma Wars", "verb": "SHAPES", "targetSlug": "eannatum-ii", "targetName": "Enannatum II", "context": "The recurring Lagash-Umma border conflict — the defining geopolitical challenge of Lagashite history — continued through Enannatum II's reign as part of the centuries-long dispute over the Gu-edena boundary zone."},
      {"sourceSlug": "early-dynastic-sumer", "sourceName": "Early Dynastic Sumer", "verb": "PRODUCES", "targetSlug": "eannatum-ii", "targetName": "Enannatum II", "context": "Enannatum II was a ruler of the Early Dynastic III period — the competitive city-state era of ancient Sumer whose military and diplomatic conflicts are recorded in the earliest surviving historical inscriptions."}
    ],
    "places": [
      {"name": "Lagash (Telloh/Girsu), southern Iraq", "role": "Enannatum II's city-state — the Sumerian polity whose royal inscriptions and king list are among the most important documents of Early Dynastic history"},
      {"name": "Southern Mesopotamia (Sumer)", "role": "The broader geographic context — the alluvial plain of southern Iraq where the Sumerian city-state system produced the earliest complex civilisations"}
    ],
    "subjects": ["Ancient Sumer", "Mesopotamian History", "Classical Era", "Ancient Near East", "Early Civilisation", "Ancient History", "City-States", "Lagash"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 3,
      "significanceNarrative": "Enannatum II was a ruler of the Sumerian city-state of Lagash (c. 2350 BCE) — documented in the Lagashite king list and royal inscriptions as part of the late Early Dynastic dynasty. His significance is primarily as an entry in the remarkable Lagashite documentary record that provides the most detailed picture of Early Dynastic Sumerian political history.",
      "significanceCategory": "local"
    }
  }
},

"tiberius-julius-sauromates-i": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221tiberius-julius-sauromates-i.json",
  "slug": "tiberius-julius-sauromates-i",
  "data": {
    "summary": "Tiberius Julius Sauromates I (died c. 123 CE) was King of the Bosporan Kingdom — the client state of Rome centred on the Crimean peninsula and the Taman peninsula (the region around the Cimmerian Bosporus, the modern Kerch Strait separating Crimea from Russia) — who ruled from approximately 92/93 CE until his death c. 123 CE. The Bosporan Kingdom was one of the most remarkable of Rome's client states: a Hellenised Greek-Scythian-Sarmatian monarchy that had maintained a close alliance with Rome (in various forms) since the 1st century BCE, trading grain and fish from the Black Sea region for Roman manufactured goods, military support, and diplomatic recognition.\n\nSauromates I's reign represents the mature phase of the Bosporan Kingdom's Roman client relationship — a period when the kingdom was fully integrated into the Roman imperial system as a loyal buffer state on the northern Black Sea frontier. The Bosporan kings of this period (the Tiberii Julii dynasty) bore Roman names reflecting their client status and their Roman citizenship; the 'Tiberius Julius' praenomen and nomen were adopted by the dynasty when they received Roman citizenship under the early Julio-Claudian emperors. Sauromates I maintained the dynasty's characteristic dual cultural identity — issuing coins with Greek legends and imagery, conducting diplomacy in both the Greek and Roman traditions, and governing a kingdom whose population included Greek colonists, indigenous Scythian and Sarmatian peoples, and various other Black Sea communities.\n\nSauromates I is documented primarily through coins bearing his image and name and through brief references in Roman sources. His reign — coinciding with the reigns of Trajan (98–117 CE) and the early Hadrian (117–138 CE) — falls in the high period of Pax Romana, a phase of relative stability on Rome's northern frontier when the client state system was functioning effectively.",
    "causes": [
      "The establishment of the Roman client state system in the Black Sea region — going back to Mithridates of Pontus's defeat by Pompey (63 BCE) and the subsequent integration of the Bosporan Kingdom into the Roman imperial system — created the political framework within which Sauromates I's dynasty exercised its kingship.",
      "The Bosporan Kingdom's strategic economic importance to Rome — as the primary source of the grain and fish that fed the Roman provinces of Asia Minor and the Aegean, and as a buffer against nomadic peoples (Scythians, Sarmatians, later Alans) beyond Rome's direct control — gave Rome strong reasons to maintain and support the Bosporan client kings.",
      "The Tiberii Julii dynasty's adoption of Roman cultural markers (Roman names, Latin inscriptions alongside Greek, coins modelled on Roman prototypes) reflected their deliberate strategy of integrating into the Roman imperial system while maintaining their identity as Greek-Scythian Hellenistic monarchs."
    ],
    "effects": [
      "Sauromates I's stable long reign contributed to the continuity of the Bosporan Kingdom as Rome's most durable northern Black Sea client state — a continuity that allowed the kingdom to maintain its commercial and strategic role through the 1st and 2nd centuries CE.",
      "The Bosporan Kingdom's coinage tradition — of which Sauromates I's coins are a significant part — provides one of the most continuous numismatic records of any client state in the Roman imperial system, offering valuable evidence for dating, portraiture, and the kingdom's political history.",
      "The Bosporan Kingdom's survival and stability under rulers like Sauromates I demonstrated the effectiveness of the Roman client state model in managing peripheral regions — maintaining Roman interests in the Black Sea grain trade without the costs of direct Roman military occupation."
    ],
    "relationships": [
      {"sourceSlug": "tiberius-julius-sauromates-i", "sourceName": "Tiberius Julius Sauromates I", "verb": "RULES", "targetSlug": "bosporan-kingdom", "targetName": "Bosporan Kingdom (Crimea)", "context": "Sauromates I was King of the Bosporan Kingdom (c. 92–123 CE) — Rome's client state on the northern Black Sea, which he governed as part of the Tiberii Julii dynasty."},
      {"sourceSlug": "roman-empire", "sourceName": "Roman Empire", "verb": "SUPPORTS", "targetSlug": "tiberius-julius-sauromates-i", "targetName": "Tiberius Julius Sauromates I", "context": "Rome maintained Sauromates I's Bosporan kingdom as a loyal client state — supplying diplomatic recognition, occasional military support, and the imperial patronage that legitimated the Bosporan monarchy's authority."},
      {"sourceSlug": "bosporan-kingdom", "sourceName": "Bosporan Kingdom", "verb": "EXPORTS", "targetSlug": "roman-black-sea-trade", "targetName": "Roman Black Sea Grain Trade", "context": "The Bosporan Kingdom's primary economic role in the Roman world was as a source of grain and fish for the Roman provinces — trade that Sauromates I's stable rule helped to maintain."}
    ],
    "places": [
      {"name": "Panticapaeum (modern Kerch, Crimea)", "role": "Capital of the Bosporan Kingdom — the Greek city on the Cimmerian Bosporus (Kerch Strait) that was the political centre of Sauromates I's kingdom"},
      {"name": "Cimmerian Bosporus (Kerch Strait, Black Sea)", "role": "The strategic waterway controlling the entrance to the Sea of Azov — the geographic key to the Bosporan Kingdom's commercial and strategic importance"}
    ],
    "subjects": ["Roman Client States", "Black Sea History", "Classical Era", "Crimea", "Ancient Rome", "Ancient History", "Hellenistic States", "Roman Empire"],
    "frameworks": ["WORLD_SYSTEMS", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 4,
      "significanceNarrative": "Tiberius Julius Sauromates I was King of the Bosporan Kingdom (c. 92–123 CE) — Rome's durable client state in the Crimea that controlled the Black Sea grain trade. His stable reign during the reigns of Trajan and Hadrian exemplifies the mature Roman client state system, and his coinage provides important numismatic evidence for the kingdom's history.",
      "significanceCategory": "local"
    }
  }
},

"zidanta-ii": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221zidanta-ii.json",
  "slug": "zidanta-ii",
  "data": {
    "summary": "Zidanta II (also Zidanta; fl. c. 1450 BCE) was a Hittite king — a ruler of the Hittite Old Kingdom (c. 1650–1400 BCE) whose reign is documented in the fragmentary records of the early Hittite state. The Hittites were an ancient Anatolian people who created one of the most powerful states of the Bronze Age Near East — eventually competing as equals with Egypt and Assyria as one of the major powers of the Late Bronze Age. Zidanta II's reign falls in the transitional period between the Hittite Old Kingdom and the later period of Hittite imperial expansion.\n\nThe historical record for Zidanta II is fragmentary and relies primarily on later Hittite texts, including the Hittite royal succession lists and royal annals that preserve records of early Hittite kings. He is associated in the sources with the persistent political instability of the Hittite Old Kingdom — a period characterised by repeated coups, assassinations, and dynastic upheavals that weakened the state and preceded the reforms and consolidation of the later Hittite empire. The Hittite Old Kingdom was notable for a distinctive tradition of royal succession disputes in which sons, brothers, and other relatives competed violently for the throne, leading Telipinu (c. 1525–1500 BCE) to issue the 'Telipinu Edict' — an attempt to regulate succession and end the cycle of dynastic violence.\n\nZidanta II's position in the Hittite succession sequence — he appears in the royal succession narratives in connection with the troubled period before or after the Telipinu reforms — illustrates the instability that characterised early Hittite royal history. The Hittite state's achievement, despite this instability, of eventually becoming a great power that challenged Egypt for supremacy in the Near East (the Battle of Kadesh, 1274 BCE) makes even its early turbulent kings significant as participants in the civilisational development of one of antiquity's most important cultures.",
    "causes": [
      "The Hittite Old Kingdom's persistent succession instability — the culture of dynastic violence and coup-making that repeatedly disrupted Hittite political continuity — created the environment of insecurity and contested authority within which Zidanta II's reign unfolded.",
      "The Hittite state's gradual development of its administrative and military institutions — the creation of the bureaucratic, legal, and military structures that would eventually support Hittite imperial expansion — provided the institutional context within which early kings like Zidanta II operated.",
      "The Bronze Age Near East's competitive multipower environment — the ongoing rivalries and conflicts between Hittites, Hurrians, Egyptians, Kassites, and other powers — shaped the external strategic challenges facing Hittite kings of the Old Kingdom period."
    ],
    "effects": [
      "Zidanta II's reign contributed to (or was affected by) the pattern of dynastic instability that eventually prompted the Telipinu Edict's attempt to regularise Hittite succession — the first known attempt to legislate royal succession in any ancient state.",
      "The early Hittite state's survival through the turbulent Old Kingdom period — including the reigns of kings like Zidanta II — created the institutional foundation for the later Hittite empire's rise to great power status, making the Old Kingdom a necessary, if turbulent, precursor to Hittite imperial achievement.",
      "The Hittite documentary tradition that preserves Zidanta II's name — the royal succession texts, annals, and administrative records of Hattusa — is one of the most important archives of the Bronze Age Near East, and Zidanta II's record is one entry in the corpus that illuminates early Anatolian political history."
    ],
    "relationships": [
      {"sourceSlug": "zidanta-ii", "sourceName": "Zidanta II", "verb": "RULES", "targetSlug": "hittite-old-kingdom", "targetName": "Hittite Old Kingdom", "context": "Zidanta II was a king of the Hittite Old Kingdom — one of the rulers of the early Hittite state in the turbulent period preceding the Telipinu reforms and the later Hittite imperial expansion."},
      {"sourceSlug": "telipinu-edict", "sourceName": "Telipinu Edict (c. 1525–1500 BCE)", "verb": "RESPONDS_TO", "targetSlug": "zidanta-ii", "targetName": "Zidanta II (and Old Kingdom instability)", "context": "The Telipinu Edict — the first known attempt to legislate royal succession — was a direct response to the dynastic violence of the Old Kingdom period in which Zidanta II participated."},
      {"sourceSlug": "hittite-empire", "sourceName": "Hittite Empire (New Kingdom)", "verb": "BUILDS_ON", "targetSlug": "zidanta-ii", "targetName": "Zidanta II (and Old Kingdom)", "context": "The later Hittite imperial expansion that made Hatti a great power equal to Egypt built on the institutional foundations laid during the turbulent Old Kingdom period, including the reigns of early kings like Zidanta II."}
    ],
    "places": [
      {"name": "Hattusa (modern Boğazkoy, Turkey)", "role": "Capital of the Hittite state — the central Anatolian city that was the political and religious centre of the Hittite kingdom throughout its history"},
      {"name": "Anatolia (modern Turkey)", "role": "The core territory of the Hittite state — the Anatolian plateau from which the Hittite Old Kingdom expanded to eventually become one of the major powers of the Bronze Age Near East"}
    ],
    "subjects": ["Hittite History", "Bronze Age", "Classical Era", "Anatolia", "Ancient Near East", "Ancient History", "Bronze Age Kingdoms", "Hittite Old Kingdom"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 3,
      "significanceNarrative": "Zidanta II was a Hittite king of the Old Kingdom (c. 1450 BCE) — one of the early rulers of the Anatolian civilisation that would eventually become a great power challenging Egypt. His reign contributed to or exemplified the dynastic instability that prompted the Telipinu Edict and that made the Old Kingdom a turbulent but foundational phase of Hittite history.",
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
