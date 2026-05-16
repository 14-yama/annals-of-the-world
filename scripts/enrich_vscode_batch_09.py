#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 09 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: mansuy-of-toul, publius-acilius-attianus, melaine, victor-of-capua,
          georg-heinrich-von-görtz, peter-the-iberian, arame-of-urartu, aeschines
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-09-may2026"

ENRICHMENTS = {

"mansuy-of-toul": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250mansuy-of-toul.json",
  "slug": "mansuy-of-toul",
  "data": {
    "summary": "Saint Mansuy of Toul (also Mansuetus; died c. 375 CE) was according to hagiographic tradition the first bishop of Toul in Lorraine (northeastern France) and one of the Frankish church's founding episcopal figures — part of the wave of early Christian missionaries who established the episcopal structure of Gaul in the 3rd and 4th centuries. The legend of Mansuy presents him as a Roman Christian sent from Rome (some traditions link him to a papal mission under Pope Clement I, though this would be chronologically impossible — suggesting the tradition is largely symbolic) who arrived in the region of Toul, converted the local population, and established the see that would become the Diocese of Toul, one of the ancient suffragan sees of the Archdiocese of Trier.\n\nToul (Tullum Leucorum) was a significant Roman city on the Moselle road in Gallia Belgica — a garrison and administrative centre whose strategic position on the route between Metz and Langres made it an important node in the Roman communication network of northeastern Gaul. The establishment of a Christian episcopal community at Toul in the mid-to-late 4th century (the historically plausible range for Mansuy's episcopate) fits the broader pattern of Christianity spreading through the urban centres of Roman Gaul in the period of Constantine and his successors, when Christianity rapidly became the dominant religion of the Roman Empire's governing classes.\n\nMansuy's cult became central to the religious and civic identity of the city of Toul throughout the medieval period. His relics were venerated at the Cathedral of Saint-Étienne in Toul (a Romanesque and Gothic masterpiece), and his feast day (3 September) was observed throughout the diocese. As patron saint of Toul, Mansuy's memory connected the medieval city to an apostolic foundation narrative — the claim of direct apostolic or near-apostolic origin that was politically important for episcopal sees competing for prestige and jurisdictional authority in the medieval church.",
    "causes": [
      "The Constantinian transformation of the Roman Empire (313 CE Edict of Milan, 380 CE Edict of Thessalonica) created the political and social conditions for rapid Christianisation of Roman urban centres in Gaul, giving episcopal missionaries like Mansuy both freedom and imperial encouragement to establish Christian communities.",
      "The Roman administrative infrastructure of northeastern Gaul — the road network, the urban centres, and the military-civilian population of the Rhine frontier — provided both the audience for early Christian missionaries and the physical spaces (converted temples, wealthy patrons' houses) for early churches.",
      "The prestige competition among medieval episcopal sees for apostolic or near-apostolic foundation narratives created the hagiographic tradition that linked Mansuy to an implausibly early founding — a common pattern in which medieval bishops claimed founding fathers to strengthen their see's jurisdiction and authority."
    ],
    "effects": [
      "Mansuy's establishment of the Diocese of Toul created one of the enduring episcopal structures of northeastern France — a see that played a significant role in the ecclesiastical politics of the Carolingian and Ottonian empires and that produced several notable medieval bishops.",
      "The cathedral complex of Toul — built around Mansuy's relics and dedicated to both Saint-Étienne and Saint Mansuy — became one of the major pilgrimage and architectural achievements of medieval Lorraine, representing the deep integration of a founding bishop's cult into civic identity.",
      "Mansuy is one of the many 'founding bishop' saints of Gallic dioceses whose cults collectively provided the medieval French church with its dense network of local sacred geography — the episcopal patron saints whose feast days, relic shrines, and foundation legends structured local religious life throughout the Middle Ages."
    ],
    "relationships": [
      {"sourceSlug": "mansuy-of-toul", "sourceName": "Saint Mansuy of Toul", "verb": "FOUNDS", "targetSlug": "diocese-of-toul", "targetName": "Diocese of Toul", "context": "Mansuy is venerated as the founding bishop of Toul — the establishment of the see that would become a significant ecclesiastical centre of northeastern France and the Lorraine region."},
      {"sourceSlug": "roman-gaul", "sourceName": "Roman Gaul", "verb": "ENABLES", "targetSlug": "mansuy-of-toul", "targetName": "Saint Mansuy of Toul", "context": "Toul's position as a Roman administrative and military centre in Gallia Belgica provided the urban infrastructure and population within which early Christian bishops like Mansuy built their communities."}
    ],
    "places": [
      {"name": "Toul, Lorraine, France", "role": "The city where Mansuy founded the diocese, was venerated as patron saint, and whose Cathedral of Saint-Étienne preserves his cult"},
      {"name": "Rome, Italy", "role": "Traditional origin of Mansuy's mission — the hagiographic narrative (probably legendary) of a Roman bishop sent to evangelise northeastern Gaul"}
    ],
    "subjects": ["Early Christianity", "Church History", "Medieval France", "Classical Era", "Lorraine", "Hagiography", "Medieval Era", "Episcopal History"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 5,
      "significanceNarrative": "Saint Mansuy of Toul was the legendary founding bishop of the Diocese of Toul in Lorraine — one of many 4th-century episcopal founder-saints whose cults provided the medieval French church with its local sacred geography. His relics at the Cathedral of Saint-Étienne anchored Toul's civic and religious identity throughout the Middle Ages.",
      "significanceCategory": "local"
    }
  }
},

"publius-acilius-attianus": {
  "filepath": "data/appwrite-export/entities/280-Class-280/280publius-acilius-attianus.json",
  "slug": "publius-acilius-attianus",
  "data": {
    "summary": "Publius Acilius Attianus (fl. late 1st–early 2nd century CE) was a Roman equestrian official and the guardian of the future Emperor Hadrian — one of the most powerful figures of the Trajanic-Hadrianic transition period and a key actor in the succession crisis of 117 CE. As the co-guardian (with Trajan's relative Ulpius Sabinus) of the young Hadrian after the death of his father, Attianus played a formative role in Hadrian's upbringing. When Trajan died in August 117 CE at Selinus in Cilicia without having formally designated a successor, it was Attianus — then serving as praetorian prefect — who managed the crisis: he announced Hadrian's adoption by Trajan (claimed on the basis of a deathbed communication, the authenticity of which was widely doubted in antiquity), arranged the army's acclamation of Hadrian, and administered affairs in Rome while Hadrian was with the eastern armies.\n\nAttianus's position as praetorian prefect in 117 CE made him one of the two most powerful men in Rome during the transition. He took decisive and controversial action in the first year of Hadrian's reign: together with Hadrian (though Hadrian later denied personal involvement), he orchestrated the execution of four ex-consuls — Lusius Quietus, Avidius Nigrinus, Cornelius Palma, and Publius Celsus — who were alleged to be plotting against the new emperor. This act — the killing of four distinguished senators without trial at the very outset of Hadrian's reign — was the most controversial event of Hadrian's early principate. The Senate was outraged, and Hadrian took the calculated step of relieving Attianus of the praetorian prefecture shortly afterwards, placing the political blame on his former guardian while rewarding him with consular ornamenta.\n\nAttianus's career illustrates the critical importance of the praetorian prefecture in managing imperial transitions — the office that, in moments of dynastic uncertainty, was the key institutional mechanism for maintaining power and managing succession.",
    "causes": [
      "Hadrian's status as a ward of Attianus — following the death of his father when Hadrian was about 10 years old — created the personal bond and legal relationship that made Attianus both Hadrian's protector and his political patron throughout Trajan's reign.",
      "Trajan's failure to formally designate a successor before his death in 117 CE created a succession vacuum that required the praetorian prefect to act decisively — Attianus's institutional position and personal connection to Hadrian made him the key figure in managing the dangerous transition.",
      "The culture of the early Principate's court politics — in which the praetorian prefecture was the key buffer between the emperor and political threats — meant that the first year of a new reign often required decisive, violent action against potential rivals: Attianus's execution of the four ex-consuls was a calculated pre-emption of a real or perceived aristocratic challenge."
    ],
    "effects": [
      "Attianus's management of the 117 CE succession — announcing Hadrian's adoption, securing the army's acclamation, and eliminating potential rivals — was decisive in establishing Hadrian's reign and preventing the civil war that might otherwise have accompanied Trajan's ambiguous death.",
      "The execution of the four ex-consuls created a permanent stain on the beginning of Hadrian's reign that coloured the Senate's relationship with the new emperor for years — and produced a lasting historiographic debate about whether Attianus acted on Hadrian's instruction or independently.",
      "Attianus's removal from the praetorian prefecture shortly after the executions was a model of how emperors used their subordinates as political scapegoats — accepting the benefit of decisive action while denying personal responsibility, a mechanism Hadrian used again with other subordinates."
    ],
    "relationships": [
      {"sourceSlug": "publius-acilius-attianus", "sourceName": "Publius Acilius Attianus", "verb": "ENABLES", "targetSlug": "hadrian", "targetName": "Emperor Hadrian", "context": "As Hadrian's guardian and praetorian prefect, Attianus was the decisive figure in securing Hadrian's succession in 117 CE — managing the army's acclamation and eliminating rival claimants."},
      {"sourceSlug": "publius-acilius-attianus", "sourceName": "Publius Acilius Attianus", "verb": "SHAPES", "targetSlug": "hadrianic-succession-117", "targetName": "Hadrianic Succession Crisis (117 CE)", "context": "Attianus's management of Trajan's death and Hadrian's accession — including the controversial execution of four ex-consuls — was the central political event of the 117 CE transition."},
      {"sourceSlug": "roman-praetorian-guard", "sourceName": "Roman Praetorian Guard", "verb": "ENABLES", "targetSlug": "publius-acilius-attianus", "targetName": "Publius Acilius Attianus", "context": "The praetorian prefecture provided Attianus with the institutional power to manage the 117 CE succession — controlling the elite guard that was essential for any emperor's security."}
    ],
    "places": [
      {"name": "Rome, Italy", "role": "Where Attianus held the praetorian prefecture and managed affairs during the transition to Hadrian's reign"},
      {"name": "Selinus, Cilicia (modern Turkey)", "role": "Where Trajan died in 117 CE — Attianus managed Rome's response to the succession crisis from a distance while Hadrian was with the eastern armies"}
    ],
    "subjects": ["Roman Empire", "Classical Rome", "Political History", "Classical Era", "Hadrianic Period", "Imperial Administration", "Succession", "Ancient History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Publius Acilius Attianus was Hadrian's guardian and praetorian prefect — the decisive figure in managing the 117 CE succession crisis that secured Hadrian's reign. His orchestration of the army's acclamation and his controversial execution of four ex-consuls shaped the beginning of one of Rome's greatest reigns, while his subsequent removal illustrated the political mechanics of imperial scapegoating.",
      "significanceCategory": "significant"
    }
  }
},

"melaine": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250melaine.json",
  "slug": "melaine",
  "data": {
    "summary": "Saint Melaine of Rennes (also Melanius; c. 450–530 CE) was a 6th-century Breton bishop and significant figure in the early ecclesiastical history of Brittany — a region undergoing simultaneous Christianisation and ethnic transformation as Brythonic Celtic migrants from Britain (fleeing Anglo-Saxon encroachments) settled in Armorica and created what would become Bretagne (Brittany). Bishop of Rennes from around 490 CE until his death (c. 501–530 CE), Melaine navigated the complex intersection of the remnant Gallo-Roman Christian establishment, the incoming Brythonic Christian migrants (who brought their own monastic church traditions from Britain and Ireland), and the Frankish overlordship that was extending itself over the region following Clovis's conquest of the Kingdom of Soissons (486 CE).\n\nMelaine had a significant relationship with the Frankish king Clovis I — he is mentioned in the famous letter from Remigius of Reims (Clovis's baptiser) to Melaine and other Gallic bishops following Clovis's baptism (c. 508 CE), a document that shows Melaine was regarded as a major figure in the Gallic episcopal network. He is also credited with writing to the Frankish court opposing the practice of wandering priests celebrating private masses at tables in private houses without a proper altar — an early disciplinary document of the Frankish church. His feast day is 6 January.\n\nMelaine represents the transitional generation of bishops who shaped Brittany's distinctive ecclesiastical culture — poised between the Roman episcopal model of Gallo-Roman Christianity and the monastic network model brought by the British migrants, between Frankish political authority and the semi-independent social structures of the incoming Brythonic settlers. This transitional role made him an important figure in the formation of Breton Christianity, which retained distinctively Celtic characteristics well into the medieval period.",
    "causes": [
      "The migration of Brythonic peoples from southwestern Britain (Cornwall, Wales, Dumnonia) to Armorica in the 5th–6th centuries — fleeing Anglo-Saxon expansion — transformed the demographic and cultural character of the region, creating the need for bishops who could bridge the Gallo-Roman and Brythonic-Celtic Christian traditions.",
      "Clovis I's conquest of the Kingdom of Soissons (486 CE) and his subsequent Frankish expansion over northern Gaul extended Frankish political authority over Brittany's bishops, requiring local ecclesiastics like Melaine to negotiate a relationship with the new Frankish overlordship.",
      "The letter of Remigius of Reims following Clovis's baptism — addressed to Melaine and other bishops — reflects the network of Gallic episcopal authority being reconstructed under Frankish patronage, in which Melaine was identified as a significant regional power."
    ],
    "effects": [
      "Melaine's episcopal career contributed to the formation of Breton Christianity's distinctive culture — a synthesis of Gallo-Roman episcopal structures and Brythonic-Celtic monastic Christianity that would produce the unique 'Celtic Christianity' of medieval Brittany.",
      "His disciplinary letter opposing wandering priests and improper masses is one of the early documents of Frankish ecclesiastical reform — reflecting the church-building efforts of the post-Clovis Frankish church that would eventually produce the Carolingian reforms.",
      "Melaine's cult as patron of Rennes — centred on the Cathedral of Rennes and his monastery foundation — provided the city with its foundational sacred identity throughout the medieval period, connecting Rennes to the apostolic-era Christianisation narrative that was politically valuable for episcopal authority."
    ],
    "relationships": [
      {"sourceSlug": "melaine", "sourceName": "Saint Melaine of Rennes", "verb": "CORRESPONDS_WITH", "targetSlug": "clovis-i", "targetName": "Clovis I", "context": "Melaine was among the Gallic bishops addressed by Remigius of Reims following Clovis's baptism — a network of episcopal recognition that placed him in the inner circle of the Frankish church's post-conversion establishment."},
      {"sourceSlug": "melaine", "sourceName": "Saint Melaine of Rennes", "verb": "SHAPES", "targetSlug": "breton-christianity", "targetName": "Breton Christianity", "context": "Melaine's episcopate in the transitional period of Brythonic settlement shaped Brittany's distinctive Christian culture — a synthesis of Roman episcopal and Celtic monastic traditions."},
      {"sourceSlug": "remigius-of-reims", "sourceName": "Remigius of Reims", "verb": "CORRESPONDS_WITH", "targetSlug": "melaine", "targetName": "Saint Melaine", "context": "Remigius's letter to Melaine and other Gallic bishops following Clovis's baptism identifies Melaine as a significant figure in the post-Clovis Gallic episcopal network."}
    ],
    "places": [
      {"name": "Rennes, Brittany, France", "role": "Where Melaine served as bishop — the Gallo-Roman city at the interface of Frankish authority and Brythonic settlement that he navigated as bishop"},
      {"name": "Brittany (Armorica), France", "role": "The broader region undergoing transformation through Brythonic migration and Frankish conquest — the ecclesiastical context of Melaine's career"}
    ],
    "subjects": ["Early Christianity", "Church History", "Medieval France", "Classical Era", "Brittany", "Frankish History", "Celtic Christianity", "Medieval Era"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Saint Melaine of Rennes was a 6th-century bishop who shaped the early ecclesiastical culture of Brittany during its transformation through Brythonic migration and Frankish conquest. His correspondence with Remigius of Reims following Clovis's baptism places him in the inner circle of the post-Clovis Gallic church, and his disciplinary letters are early documents of Frankish ecclesiastical reform.",
      "significanceCategory": "regional"
    }
  }
},

"victor-of-capua": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250victor-of-capua.json",
  "slug": "victor-of-capua",
  "data": {
    "summary": "Victor of Capua (died 554 CE) was a 6th-century Italian bishop and biblical scholar — Bishop of Capua in Campania — who is primarily known for a significant contribution to biblical textual history: he is associated with the 'Fuldensis Gospel Harmony', a Latin revision of Tatian's Diatessaron (the famous 2nd-century Gospel harmony compiled by the Syriac Christian scholar Tatian) that Victor commissioned or composed. The Codex Fuldensis — a 6th-century Latin New Testament manuscript housed at the Abbey of Fulda (from which it takes its name) — includes a Latin version of a Gospel harmony that Victor prepared in 545 CE, with a preface explaining his editorial work: he noted that he had discovered a Latin Diatessaron that had been poorly rendered and had revised and reorganised it to align with the canonical four-gospel structure.\n\nVictor's Gospel harmony is significant for several reasons in biblical scholarship: it preserves elements of an ancient Gospel harmony tradition (Tatian's Diatessaron was one of the most widely used Christian texts before the four-gospel canon was fully established, especially in Syriac and Eastern Christianity), it demonstrates the continued interest in Gospel harmonisation in Western Christianity three centuries after Tatian, and it is evidence for the circulation of Diatessaron-related materials in Latin Christianity that had largely moved away from harmonisation toward the canonical four-gospel text.\n\nVictor's scholarly activity places him in the tradition of 6th-century Italian ecclesiastical scholars — the generation that included Cassiodorus, Boethius, and Pope Gregory the Great — who worked to preserve, revise, and transmit the texts of the Christian tradition during the turbulent period of Ostrogothic rule and the Byzantine reconquest. His work on the Gospel text shows a bishop engaged in active literary and textual scholarship at a time when the institutional structures for such work were under stress from military and political disruption.",
    "causes": [
      "The survival of a Latin Diatessaron tradition in Italy — preserving elements of Tatian's 2nd-century Gospel harmony that circulated in the Latin-speaking West despite the increasing dominance of the canonical four-gospel format — provided Victor with the textual material for his revision.",
      "The 6th-century Italian intellectual climate — characterised by scholars like Cassiodorus and Boethius working to preserve classical and Christian learning during the Ostrogothic period — created the context for Victor's scholarly engagement with Gospel texts.",
      "The institutional resources of the Campanian church — a wealthy and ancient Christian community with access to manuscripts, scriptoria, and clerical scholars — enabled Victor to undertake the textual revision work that produced the Fuldensis harmony."
    ],
    "effects": [
      "Victor's Gospel harmony (preserved in the Codex Fuldensis, c. 546 CE) became one of the primary textual sources through which the Diatessaron tradition was partially preserved in Latin Christianity — a transmission that has been important for modern scholars studying the early harmony tradition and the pre-canonical Gospel text.",
      "The Codex Fuldensis — which Victor's work helped create — became one of the most important Latin biblical manuscripts of the early medieval period, preserved at Fulda and used by scholars including Boniface of Mainz in his missionary work among the Germans.",
      "Victor's scholarly activity as a bishop contributed to the 6th-century Italian tradition of episcopal biblical scholarship that was the immediate precursor of the Carolingian scriptorial culture — the monastic and episcopal centres that preserved and copied biblical texts throughout the early medieval period."
    ],
    "relationships": [
      {"sourceSlug": "victor-of-capua", "sourceName": "Victor of Capua", "verb": "REVISES", "targetSlug": "diatessaron", "targetName": "Tatian's Diatessaron", "context": "Victor prepared a revised Latin version of the Diatessaron Gospel harmony in 545 CE — the work preserved in the Codex Fuldensis that is the primary Latin witness to the Diatessaron tradition."},
      {"sourceSlug": "codex-fuldensis", "sourceName": "Codex Fuldensis", "verb": "PRESERVES", "targetSlug": "victor-of-capua", "targetName": "Victor of Capua's Gospel Harmony", "context": "The Codex Fuldensis (c. 546 CE), the major 6th-century Latin biblical manuscript, preserves Victor's revised Gospel harmony — making it a primary source for both Victor's work and the Latin Diatessaron tradition."},
      {"sourceSlug": "tatian", "sourceName": "Tatian", "verb": "INFLUENCES", "targetSlug": "victor-of-capua", "targetName": "Victor of Capua", "context": "Tatian's 2nd-century Diatessaron — the most influential early Gospel harmony — was the basis for the Latin text Victor revised and preserved in the Fuldensis, connecting 6th-century Italy to the earliest traditions of Gospel harmonisation."}
    ],
    "places": [
      {"name": "Capua, Campania, Italy", "role": "Victor's diocese — an ancient Campanian city with a wealthy and ancient Christian community that supported his scholarly work"},
      {"name": "Fulda, Germany", "role": "Where the Codex Fuldensis containing Victor's Gospel harmony is preserved — the Abbey of Fulda that became one of the most important centres of early medieval biblical scholarship"}
    ],
    "subjects": ["Biblical Scholarship", "Early Christianity", "Church History", "Classical Era", "Italy", "Biblical Text", "Medieval Era", "6th Century"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Victor of Capua was the 6th-century Italian bishop whose revised Latin Gospel harmony (545 CE), preserved in the Codex Fuldensis, is the primary Latin witness to Tatian's Diatessaron tradition. His work connected the early Christian Gospel harmonisation tradition to the medieval Latin biblical manuscript culture, and the Codex Fuldensis became a significant resource for early medieval biblical scholarship, including Boniface of Mainz's missionary work.",
      "significanceCategory": "significant"
    }
  }
},

"georg-heinrich-von-görtz": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220georg-heinrich-von-görtz.json",
  "slug": "georg-heinrich-von-görtz",
  "data": {
    "summary": "Georg Heinrich von Görtz (1668–1719), also known as Baron Görtz or Count Görtz, was a Swedish-Holstein diplomat and statesman — the most powerful minister of King Charles XII of Sweden in the final years of the Great Northern War (1700–1721) — whose audacious diplomatic manoeuvres and controversial financial policies made him both the architect of Sweden's last hopes for recovery and the symbol of its political recklessness. Born in Holstein (then a duchy under Danish suzerainty with strong connections to the Swedish Crown), Görtz entered Swedish service and rapidly became Charles XII's chief diplomatic operative, given extraordinary powers to negotiate Sweden's way out of the catastrophic military situation following the Battle of Poltava (1709) and the prolonged Swedish defeat.\n\nGörtz's diplomatic strategy was breathtakingly ambitious: he attempted to negotiate a separate peace with Russia's Peter the Great that would end the war on terms Sweden could accept, while simultaneously seeking to redirect Swedish military power toward the Jacobite cause in Britain — backing the Old Pretender James Francis Edward Stuart against the Hanoverian King George I. This would have required Charles XII to invade northern Britain, re-establish the Stuart dynasty, and gain British neutrality or support in exchange. The plan came close to fruition in 1717–1718: Görtz negotiated secretly with Peter the Great at the Åland Congress (1718–1719), and coordinated with Jacobite agents in parallel. The entire scheme collapsed when Charles XII was killed at the Siege of Frederikshald in December 1718 — shot through the head in circumstances that have fuelled conspiracy theories ever since.\n\nWithout Charles XII's protection, Görtz was immediately arrested by the Swedish Riksdag council, tried on charges of treason and financial mismanagement, and executed in Stockholm in February 1719 — a remarkably swift judicial assassination that reflected how thoroughly the Swedish political establishment blamed him for the disasters of Charles XII's final years.",
    "causes": [
      "The catastrophic Swedish defeat at the Battle of Poltava (1709) and Charles XII's subsequent exile in Ottoman Bender (1709–1714) created the strategic desperation that gave Görtz the latitude to pursue extraordinarily radical diplomatic schemes — only a man with nothing to lose would take the risks Görtz accepted.",
      "Charles XII's absolute monarchical style — ruling through personal favourites with minimal institutional constraint — gave Görtz the unchecked ministerial power to conduct secret negotiations, manipulate Swedish finances, and make commitments that the Swedish council would never have authorised.",
      "The fluid multi-player diplomacy of early 18th-century Europe — in which Peter the Great's Russia, the Hanoverian succession in Britain, the Jacobite movement, and the exhausted Northern powers were all simultaneously renegotiating their alignments — provided the diplomatic space for Görtz's complex manoeuvres."
    ],
    "effects": [
      "Görtz's execution in 1719 — the day after Charles XII's sudden death — marked the end of Swedish great-power ambitions in northern Europe and the completion of Sweden's transformation from major military power to secondary state, a transition sealed by the Treaty of Nystad (1721) that formally ended the Great Northern War.",
      "The Jacobite dimension of Görtz's diplomacy represented the last serious possibility of a Stuart restoration backed by a major European power — its collapse with Charles XII's death ended the most credible threat to Hanoverian stability in the years before the 1745 Jacobite rising.",
      "Görtz's financial innovations (including the emergency debased copper coinage and the 'Görtz tokens' used to fund Sweden's continued war effort) were a form of emergency financial engineering that contributed to economic disruption in Sweden — and contributed to the hostility of the Swedish establishment that brought about his execution."
    ],
    "relationships": [
      {"sourceSlug": "georg-heinrich-von-görtz", "sourceName": "Baron Görtz", "verb": "SERVES", "targetSlug": "charles-xii-of-sweden", "targetName": "Charles XII of Sweden", "context": "Görtz was Charles XII's chief diplomatic minister in the final phase of the Great Northern War — given extraordinary powers to negotiate Sweden's recovery from the Poltava disaster."},
      {"sourceSlug": "georg-heinrich-von-görtz", "sourceName": "Baron Görtz", "verb": "NEGOTIATES_WITH", "targetSlug": "peter-the-great", "targetName": "Peter the Great", "context": "Görtz conducted the secret Åland Congress negotiations (1718–1719) with Russia on behalf of Charles XII — an attempt to reach a separate peace that would end the Great Northern War on Sweden's terms."},
      {"sourceSlug": "battle-of-poltava", "sourceName": "Battle of Poltava (1709)", "verb": "ENABLES", "targetSlug": "georg-heinrich-von-görtz", "targetName": "Baron Görtz", "context": "The catastrophic Swedish defeat at Poltava created the strategic desperation that gave Görtz the latitude and necessity to pursue his radical diplomatic schemes on Charles XII's behalf."}
    ],
    "places": [
      {"name": "Stockholm, Sweden", "role": "Where Görtz was arrested, tried, and executed in 1719 — the site of his political downfall immediately following Charles XII's death"},
      {"name": "Åland Islands, Finland/Sweden", "role": "Site of the Åland Congress (1718–1719) — Görtz's secret peace negotiations with Russia that were his most ambitious diplomatic project"},
      {"name": "Holstein, Germany", "role": "Görtz's birthplace — the duchy whose complex political status between Denmark and Sweden shaped his diplomatic career and connections"}
    ],
    "subjects": ["Swedish History", "Early Modern History", "Diplomacy", "Early Modern Era", "Great Northern War", "Northern Europe", "Political History", "Military History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Baron Görtz was Charles XII of Sweden's chief minister and most audacious diplomat — the architect of Sweden's last strategic gamble in the Great Northern War, combining secret peace negotiations with Russia (Åland Congress, 1718) with Jacobite coordination against Hanoverian Britain. His execution in 1719, immediately after Charles XII's death, symbolised the end of Sweden's great-power era. His career touches the major geopolitical transformations of early 18th-century northern Europe.",
      "significanceCategory": "significant"
    }
  }
},

"peter-the-iberian": {
  "filepath": "data/appwrite-export/entities/210-Class-210/210peter-the-iberian.json",
  "slug": "peter-the-iberian",
  "data": {
    "summary": "Peter the Iberian (c. 417–491 CE), born Nabarnugios (also Murvan in Georgian sources), was a Georgian (Kartvelian/Iberian) prince — the son or nephew of King Mithridates V of Kartli/Iberia — who became one of the most remarkable religious and literary figures of 5th-century Christianity. Sent as a political hostage to the court of the Eastern Roman Emperor Theodosius II in Constantinople as a child (c. 423 CE), he was raised in the imperial court alongside the emperor's sister Pulcheria and received a classical Greek and Christian education. Around 423 CE he escaped or was released from the imperial court, converted to ascetic Christianity, and became a monk — spending the rest of his extraordinarily mobile life as a wandering ascetic-scholar across the Byzantine and Eastern Mediterranean world: Palestine, Egypt, Syria, Asia Minor, and his homeland Georgia (Iberia).\n\nPeter the Iberian is significant for two major reasons: first, his life is a primary source for the complex Miaphysite (non-Chalcedonian) theological controversy that dominated 5th-century Christianity. He was a committed opponent of the Council of Chalcedon (451 CE) — which defined Christ as having two natures in one person — supporting instead the Miaphysite position that Christ had one united nature. His connections to Miaphysite theologians and his influence on the theological debates of the eastern Mediterranean make him an important figure in the history of the Chalcedonian schism that ultimately divided Byzantine Christianity from the Egyptian Coptic, Ethiopian, Armenian, and Syriac Orthodox churches.\n\nSecond, Peter the Iberian has been proposed by modern scholars (most notably Cornelia Horn and Robert Phenix) as the actual author — or one of the key figures associated with — the Corpus Dionysiacum: the influential body of mystical theological writings attributed to 'Dionysius the Areopagite' (supposedly a disciple of Saint Paul, 1st century CE) but actually composed in the late 5th–early 6th century. The Corpus Dionysiacum — including the 'Divine Names', 'Mystical Theology', 'Celestial Hierarchy', and 'Ecclesiastical Hierarchy' — was one of the most influential texts in medieval Christian mystical theology.",
    "causes": [
      "The political practice of sending royal children as hostages to the Byzantine court — an instrument of imperial foreign policy toward neighbouring kingdoms — brought Nabarnugios/Peter to Constantinople, giving him access to the highest levels of imperial and ecclesiastical culture.",
      "The Council of Chalcedon (451 CE) and the Miaphysite-Chalcedonian controversy it sparked provided the theological context for Peter's anti-Chalcedonian commitment — a position that put him in tension with imperial orthodoxy but aligned him with the Miaphysite majority in Egypt, Syria, and his homeland Georgia.",
      "Peter's extraordinary mobility across the eastern Mediterranean — moving between Palestine, Egypt, Syria, Georgia, and Asia Minor over several decades — provided the intellectual cross-pollination and the network of Miaphysite theological contacts that shaped his theological work."
    ],
    "effects": [
      "Peter the Iberian's Miaphysite theological activity contributed to the development of Eastern Christian theology in the non-Chalcedonian tradition — a stream that produced the Coptic, Ethiopian, Armenian, and Syriac Orthodox churches that remain distinct from both Chalcedonian Orthodoxy and Latin Christianity.",
      "If the scholarly hypothesis linking Peter to the Pseudo-Dionysian writings is correct, his legacy is one of the most remarkable and unlikely in intellectual history: a Georgian prince-turned-monk who, writing under the pseudonym 'Dionysius the Areopagite', shaped medieval Western mystical theology (Thomas Aquinas, Meister Eckhart, John of the Cross) more profoundly than almost any other single text.",
      "Peter's life as a Georgian prince at the Byzantine court is a primary source for understanding the complex political and cultural relationship between the Caucasian kingdoms and the Byzantine Empire — a frontier zone where Roman, Persian, and Armenian political cultures intersected."
    ],
    "relationships": [
      {"sourceSlug": "peter-the-iberian", "sourceName": "Peter the Iberian", "verb": "OPPOSES", "targetSlug": "council-of-chalcedon", "targetName": "Council of Chalcedon (451 CE)", "context": "Peter was a committed anti-Chalcedonian — his opposition to the Council of Chalcedon's two-nature Christology placed him among the Miaphysite camp that produced the non-Chalcedonian Eastern Christian churches."},
      {"sourceSlug": "peter-the-iberian", "sourceName": "Peter the Iberian", "verb": "POTENTIALLY_AUTHORS", "targetSlug": "corpus-dionysiacum", "targetName": "Pseudo-Dionysian Corpus", "context": "Modern scholars (Horn, Phenix) have proposed Peter the Iberian as a key figure associated with or even the author of the Pseudo-Dionysian writings — one of the most influential bodies of Christian mystical theology."},
      {"sourceSlug": "theodosius-ii", "sourceName": "Emperor Theodosius II", "verb": "SHAPES", "targetSlug": "peter-the-iberian", "targetName": "Peter the Iberian", "context": "The imperial court of Theodosius II in Constantinople — where Peter grew up as a royal hostage — provided his classical Greek education and Christian formation, the intellectual foundation for his later scholarly-theological career."}
    ],
    "places": [
      {"name": "Constantinople, Byzantine Empire", "role": "Where Peter grew up as a royal hostage at the court of Theodosius II — his formative intellectual environment"},
      {"name": "Palestine / Jerusalem", "role": "One of the centres of Peter's monastic life and theological activity — he spent significant periods in the Holy Land engaging with Palestinian monasticism and theology"},
      {"name": "Kartli/Iberia (modern Georgia)", "role": "Peter's homeland — the Caucasian kingdom whose royal family he represented, and to which he returned in his later years"}
    ],
    "subjects": ["Byzantine Christianity", "Early Christianity", "Classical Era", "Georgia", "Miaphysitism", "Mystical Theology", "Ancient History", "Political Hostage"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Peter the Iberian was a Georgian royal hostage at the Byzantine court who became a wandering Miaphysite monk-theologian — and the proposed (by Horn and Phenix) actual author of the Pseudo-Dionysian Corpus, one of the most influential bodies of Christian mystical theology. If this attribution is correct, Peter's influence on medieval Western mysticism (via Thomas Aquinas, Meister Eckhart, John of the Cross) would make him one of the most consequential figures in medieval intellectual history. His life also illuminates Byzantine frontier diplomacy, the Chalcedonian controversy, and the origins of non-Chalcedonian Christianity.",
      "significanceCategory": "highly-significant"
    }
  }
},

"arame-of-urartu": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221arame-of-urartu.json",
  "slug": "arame-of-urartu",
  "data": {
    "summary": "Arame of Urartu (fl. late 9th century BCE) was the first identifiable king of the Kingdom of Urartu (Ararat) — the Urartian state of the ancient Near East centred in the region of Lake Van in modern eastern Turkey, northwestern Iran, and Armenia. Urartu was one of the major powers of the ancient Near East in the 9th–7th centuries BCE, a formidable rival to the Neo-Assyrian Empire whose fortified citadels, bronze metalwork, and horse-breeding culture made it a distinctive and influential civilisation. Arame is the earliest Urartian ruler mentioned by name in Assyrian sources: Assyrian royal inscriptions record that King Shalmaneser III of Assyria (858–824 BCE) conducted military campaigns against 'Aramu' (Arame) and the 'land of Urartu' in his 9th year (850 BCE) and subsequent years, suggesting Arame was the founder or early consolidator of the Urartian kingdom.\n\nThe significance of Arame lies in his position as the first named king at the moment of Urartu's emergence as a coherent political entity capable of resisting Assyrian military pressure. The Urartian kingdom represented the consolidation of a number of confederate Nairi (or Uruatri) tribes that the Assyrians had been raiding and extracting tribute from since the 13th century BCE. Under Arame and his successors, this tribal confederation transformed into a centralised kingdom with a distinctive script (based on cuneiform), a state religion centred on the god Haldi, monumental architectural traditions, and military capacity that challenged Assyrian expansion in the north.\n\nAlthough the Assyrian accounts of Shalmaneser III's campaigns describe repeated raids into Urartian territory, the inability to permanently subjugate Urartu under Arame suggests that even at this early stage the kingdom had sufficient political coherence to survive Assyrian military pressure — laying the foundation for the great Urartian expansion of the 8th century BCE under kings like Sarduri I and Menua.",
    "causes": [
      "The emergence of a more centralised political structure among the Nairi/Uruatri tribes of the Lake Van region — possibly triggered by the threat of Assyrian expansion that required coordinated military response — produced the early Urartian kingdom over which Arame presided.",
      "The geographic advantages of the Lake Van region — high mountain terrain, defensible citadel sites, and a sophisticated irrigation and agricultural base — provided the physical and economic foundation for the kingdom Arame was consolidating against Assyrian pressure.",
      "Shalmaneser III's Assyrian expansion into the northern highlands in the 9th century BCE — driven by the Neo-Assyrian Empire's need for horses, metal, and tribute from the northern peoples — created the military pressure that gave the emerging Urartian kingdom its defining antagonism."
    ],
    "effects": [
      "Arame's resistance to Shalmaneser III's campaigns established the precedent of Urartian military independence from Assyria — a pattern that continued through the 9th–8th centuries and produced the great Urartian expansion of the 8th century BCE that made Urartu one of the Assyrian Empire's most formidable rivals.",
      "The Urartian kingdom Arame founded (or consolidated) became the political ancestor of the Armenian state — the Urartian cultural legacy (language, script, art, architecture) was directly absorbed by the Armenian peoples who replaced Urartu after the Scythian/Median/Babylonian pressures of the late 7th–6th centuries BCE.",
      "The Assyrian inscriptional records of Shalmaneser III's campaigns against Arame are among the earliest direct references to the region that became Armenia — making Arame's kingdom the first historically attested political entity in the Armenian geographical sphere."
    ],
    "relationships": [
      {"sourceSlug": "arame-of-urartu", "sourceName": "Arame of Urartu", "verb": "OPPOSES", "targetSlug": "shalmaneser-iii", "targetName": "Shalmaneser III of Assyria", "context": "Shalmaneser III's Assyrian inscriptions record repeated campaigns against 'Aramu' (Arame) and Urartu — making Arame the first named Urartian king identified through Assyrian military records."},
      {"sourceSlug": "arame-of-urartu", "sourceName": "Arame of Urartu", "verb": "FOUNDS", "targetSlug": "kingdom-of-urartu", "targetName": "Kingdom of Urartu", "context": "Arame is the earliest identifiable king of the emerging Urartian state — the consolidation of Nairi/Uruatri tribes into the centralised kingdom that became one of the major powers of the 9th–7th century BCE Near East."},
      {"sourceSlug": "kingdom-of-urartu", "sourceName": "Kingdom of Urartu", "verb": "PRECEDES", "targetSlug": "ancient-armenia", "targetName": "Ancient Armenia", "context": "The Urartian kingdom — which Arame helped found — was the direct political and cultural predecessor of the Armenian state, whose peoples absorbed the Urartian cultural legacy."}
    ],
    "places": [
      {"name": "Lake Van region, Eastern Turkey / Armenia / Iran", "role": "The geographical heartland of the Urartian kingdom — the high-altitude plateau around Lake Van that provided the defensive terrain and agricultural base of Arame's emerging state"},
      {"name": "Ancient Near East", "role": "The broader context of Arame's kingdom — the competitive state system of Assyria, Urartu, and the Nairi lands in which the early Urartian state was carved out"}
    ],
    "subjects": ["Ancient Near East", "Urartu", "Classical Era", "Armenia", "Ancient History", "Military History", "Neo-Assyrian Empire", "Bronze Age Kingdoms"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Arame of Urartu was the first identifiable king of the Urartian state — the earliest named ruler of the kingdom that became one of the Neo-Assyrian Empire's most formidable rivals and the direct cultural ancestor of Armenian civilisation. His resistance to Shalmaneser III's campaigns established the precedent for Urartian independence that enabled the great 8th-century Urartian expansion, and Assyrian inscriptions recording his name are the earliest historical references to the Armenian geographical sphere.",
      "significanceCategory": "significant"
    }
  }
},

"aeschines": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220aeschines.json",
  "slug": "aeschines",
  "data": {
    "summary": "Aeschines (c. 389–314 BCE) was an Athenian statesman and orator — the third of the canonical 'Ten Attic Orators' in the ancient classification — and the chief rival and nemesis of Demosthenes, the greatest orator of Classical Athens. A self-made man of modest origins (his father ran a grammar school and his mother performed mystery rites), Aeschines rose through his extraordinary talent for improvised speech and his physical presence — he was a trained actor before entering politics, and his theatrical skills gave him a style of oratory that was the antithesis of Demosthenes' laboured, intensely prepared speeches. The personal and political rivalry between Aeschines and Demosthenes, conducted through two decades of lawsuits, counter-accusations, and political manoeuvres, is one of the most fully documented political conflicts of the ancient world.\n\nAeschines represented the pro-Macedonian or 'Philippist' faction in Athens — advocating for accommodation with Philip II of Macedon and later Alexander the Great at a time when Demosthenes was leading the anti-Macedonian resistance. His most famous trial came in 343 BCE when Demosthenes prosecuted him for misconduct during the Peace of Philocrates negotiations (346 BCE) — Aeschines had participated in the embassy to Philip that led to Athens' controversial acceptance of the peace. Aeschines turned the tables and counter-prosecuted (in 343 BCE), but the case ended without conviction. The climactic confrontation came in 330 BCE: Aeschines prosecuted the prominent Athenian Ctesiphon for proposing to award Demosthenes a golden crown for his service to Athens. This produced Demosthenes' masterpiece 'On the Crown' — the greatest speech of ancient oratory — and Aeschines' own 'Against Ctesiphon'. Aeschines lost so decisively (failing to reach even one-fifth of the jury's votes) that he was fined and forced into exile in Rhodes, where he taught rhetoric.\n\nOnly three of Aeschines' speeches survive intact: 'Against Timarchus' (345 BCE), 'On the False Embassy' (343 BCE), and 'Against Ctesiphon' (330 BCE) — primary sources for the turbulent politics of Athens in the era of Macedonian expansion.",
    "causes": [
      "Philip II of Macedon's military expansion into Greece — and Athens' internal debate about how to respond, between active resistance (Demosthenes' position) and pragmatic accommodation (Aeschines' position) — created the political context for the Aeschines-Demosthenes rivalry that defined Athenian politics of the 340s–330s BCE.",
      "Aeschines' theatrical training and natural gifts for improvised oratory gave him the ability to compete with Demosthenes in the assembly and the courts — his different oratorical style (natural, actor-trained, physically expressive) made him a genuine rival rather than a mere foil.",
      "The Athenian democratic legal system — in which political conflicts were routinely fought through prosecutions and counter-prosecutions in the popular courts — provided the arena within which the Aeschines-Demosthenes rivalry was conducted, generating the surviving speeches that are our primary sources."
    ],
    "effects": [
      "Aeschines' defeat by Demosthenes in the 'On the Crown' case (330 BCE) produced the greatest speech in ancient oratory — Demosthenes' defence, which was studied as the model of oratorical excellence throughout the ancient world and remained a canonical text through the Renaissance.",
      "Aeschines' three surviving speeches are primary sources for the political history of Athens in the age of Macedonian expansion — the negotiations with Philip II, the internal debates of Athenian democracy, and the mechanics of the lawcourt as a political arena.",
      "Aeschines' post-exile career as a rhetoric teacher on Rhodes contributed to the transmission of the Attic oratorical tradition into the Hellenistic world — his school was part of the network of rhetorical education that eventually produced Roman oratory."
    ],
    "relationships": [
      {"sourceSlug": "aeschines", "sourceName": "Aeschines", "verb": "OPPOSES", "targetSlug": "demosthenes", "targetName": "Demosthenes", "context": "The rivalry between Aeschines (pro-Macedonian) and Demosthenes (anti-Macedonian) was the defining political and oratorical conflict of classical Athens — culminating in the 'On the Crown' case (330 BCE) that produced Demosthenes' masterpiece."},
      {"sourceSlug": "aeschines", "sourceName": "Aeschines", "verb": "ENABLES", "targetSlug": "peace-of-philocrates", "targetName": "Peace of Philocrates (346 BCE)", "context": "Aeschines' participation in the embassy to Philip II led to the Peace of Philocrates — the controversial accommodation with Macedon that he defended and Demosthenes opposed."},
      {"sourceSlug": "philip-ii-of-macedon", "sourceName": "Philip II of Macedon", "verb": "SHAPES", "targetSlug": "aeschines", "targetName": "Aeschines", "context": "Philip's Macedonian expansion forced Athens to choose between resistance and accommodation — Aeschines' pro-Macedonian position defined his political career and his rivalry with Demosthenes."}
    ],
    "places": [
      {"name": "Athens, Greece", "role": "The democratic polis in which Aeschines' political and oratorical career unfolded — the city whose assembly and lawcourts were the arena for his rivalry with Demosthenes"},
      {"name": "Rhodes, Greece", "role": "Where Aeschines founded a school of rhetoric after his exile following the 'On the Crown' defeat — his teaching at Rhodes contributed to the transmission of Attic oratory into the Hellenistic world"}
    ],
    "subjects": ["Classical Athens", "Greek Oratory", "Classical Era", "Ancient Greece", "Political History", "Ancient History", "Macedonian Expansion", "Democracy"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Aeschines was the chief rival of Demosthenes and the third of the Ten Attic Orators — the pro-Macedonian statesman whose prosecution of Ctesiphon (330 BCE) provoked Demosthenes' 'On the Crown', the greatest speech of ancient oratory. His three surviving speeches are primary sources for Athenian politics in the age of Macedonian expansion, and his defeat in 330 BCE produced one of the canonical texts of ancient rhetoric while defining the parameters of the Macedonian accommodation debate that shaped Greek history.",
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
