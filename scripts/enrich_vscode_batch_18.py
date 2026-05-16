#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 18 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: vikings, shapur-i-shahrvaraz, donnchad-mac-briain, demetrius-iii,
          saint-fergus, lazarus-spengler, theatre-art, galaxy
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-18-may2026"

ENRICHMENTS = {

"vikings": {
  "filepath": "data/appwrite-export/entities/110-Class-110/110vikings.json",
  "slug": "vikings",
  "data": {
    "summary": "The Vikings were the Norse seafaring peoples of Scandinavia (modern Denmark, Norway, and Sweden) who, during the Viking Age (c. 793–1066 CE), undertook an extraordinary period of exploration, raiding, trading, colonisation, and political expansion that brought them into contact with — and frequently transformed — civilisations from Newfoundland in the west to Constantinople and Baghdad in the east. The term 'Viking' (Old Norse víkingr) originally referred specifically to raiders and pirates, though in modern usage it has come to describe the entirety of the Norse culture of the period. The Vikings were not a unified people or polity but rather a diverse set of communities sharing language, material culture, and religious traditions (Old Norse religion, later gradually replaced by Christianity), who operated across an enormous geographic range.\n\nThe Viking Age is conventionally dated from the raid on the monastery of Lindisfarne (793 CE) — the first major recorded Norse raid on Britain — through the Norman Conquest of England by William the Conqueror (1066 CE), a Norman whose lineage traced back to the Viking Rollo who had been granted Normandy by the French king in 911 CE. During this period, Norse peoples settled Iceland (c. 874 CE), Greenland (c. 985 CE), and briefly Vinland (L'Anse aux Meadows, Newfoundland, c. 1000 CE) — the first European settlements in the Americas. In the east, the Varangians (Norse traders and warriors who penetrated Russia via the river systems) founded the Kievan Rus' state, served as the elite Varangian Guard of the Byzantine emperors, and reached Constantinople and Baghdad. In England, the Danelaw established Norse political control over northern and eastern England. In France, Normans founded a duchy that would eventually conquer England and establish a kingdom in southern Italy.\n\nThe Vikings' legacy is deeply ambivalent: they were raiders and slavers who terrorised coastal and riverside communities across Europe, but also skilled craftsmen, traders who connected the Baltic to the Mediterranean and the Islamic world, pioneering navigators who mastered open-ocean sailing by stars and the sun, and settlers who populated the North Atlantic islands. Norse mythology and literature — the Eddas, the sagas — represent a sophisticated literary and religious tradition.",
    "causes": [
      "Population growth in Scandinavia combined with the inheritance system (primogeniture in Norway — only the eldest son inherited land) and the fragmented political landscape of the Viking Age drove younger sons and ambitious men to seek fortune abroad through raiding, trading, or mercenary service.",
      "The development of the Viking longship — a shallow-draught, highly manoeuvrable vessel capable of both open-ocean sailing and river navigation, and able to be beached directly on coastlines — provided the technological foundation for the Vikings' extraordinary range and gave them a decisive tactical advantage in surprise raids.",
      "The weakness and political fragmentation of the Carolingian Empire after Charlemagne's death (814 CE) — the civil wars, the partition of the empire, and the inability of Frankish rulers to mount effective coastal defences — created the political vulnerability that Viking raiders exploited most intensively in western Europe."
    ],
    "effects": [
      "The Vikings permanently shaped the political map of Europe: the Norman Conquest of England (1066) replaced the Anglo-Saxon kingdom with a French-speaking Norman aristocracy that transformed English culture, language, and institutions; the Varangian founding of Kievan Rus' created the political entity from which Russia, Ukraine, and Belarus trace their medieval origins; and the Norman Kingdom of Sicily produced one of the most sophisticated multicultural states of the medieval Mediterranean.",
      "Viking trade networks — connecting Scandinavia via the Baltic and Russian rivers to Byzantium and the Abbasid caliphate — were crucial conduits for the flow of silver (Arabic dirhams) from the Islamic world into northern Europe, facilitating the monetisation of the northern European economy and the development of the early medieval trading towns (emporia) of the Baltic and North Sea.",
      "The Norse settlement of Iceland, Greenland, and Vinland made the Vikings the first Europeans to reach and temporarily settle the Americas (c. 1000 CE) — 500 years before Columbus — an achievement confirmed by archaeology at L'Anse aux Meadows, Newfoundland, and representing the furthest extent of Old World exploratory reach before the Portuguese voyages of the 15th century."
    ],
    "relationships": [
      {"sourceSlug": "vikings", "sourceName": "Vikings", "verb": "FOUND", "targetSlug": "kievan-rus", "targetName": "Kievan Rus'", "context": "Varangian (Norse) traders and warriors penetrating Russia via its river systems founded the trading state that became Kievan Rus' — the political predecessor of Russia, Ukraine, and Belarus."},
      {"sourceSlug": "vikings", "sourceName": "Vikings", "verb": "SETTLE", "targetSlug": "normandy", "targetName": "Normandy (and Norman civilisation)", "context": "Viking chieftain Rollo was granted Normandy by the Frankish king Charles the Simple in 911 CE — the Norse settlement that produced the Norman civilisation whose Conquest of England (1066) transformed medieval Europe."},
      {"sourceSlug": "vikings", "sourceName": "Vikings", "verb": "DISCOVER", "targetSlug": "vinland", "targetName": "Vinland (North America, c. 1000 CE)", "context": "Norse explorers — Leif Eriksson and others — established the first European settlement in the Americas at L'Anse aux Meadows, Newfoundland (c. 1000 CE), 500 years before Columbus."}
    ],
    "places": [
      {"name": "Scandinavia (Denmark, Norway, Sweden)", "role": "The origin point of the Viking peoples — the societies whose population pressure, political culture, and maritime technology produced the Viking Age"},
      {"name": "North Atlantic, British Isles, France, Russia, Byzantium, North America", "role": "The full geographic range of Viking activity — from Newfoundland to Baghdad, the most extensive exploratory and raiding range of any medieval people"}
    ],
    "subjects": ["Viking Age", "Medieval History", "Classical Era", "Scandinavia", "Medieval Europe", "Exploration", "Norse Culture", "Migration"],
    "frameworks": ["WORLD_SYSTEMS", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Vikings were one of the most consequential peoples of the medieval world — their raids, trade, colonisation, and political foundations transformed European history from Britain to Russia, produced the first European settlement in the Americas (c. 1000 CE), and connected northern Europe to the economies of Byzantium and the Islamic world. Their Norman descendants conquered England (1066), Sicily, and the Holy Land, making Viking civilisation's ultimate impact extend far beyond the Viking Age itself.",
      "significanceCategory": "world-changing"
    }
  }
},

"shapur-i-shahrvaraz": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221shapur-i-shahrvaraz.json",
  "slug": "shapur-i-shahrvaraz",
  "data": {
    "summary": "Shapur-i Shahrvaraz (died 630 CE) was a brief and turbulent Sasanian Persian king — one of the last rulers of the Sasanian Empire before the Arab Islamic conquest — who reigned for only a matter of months in 630 CE during the catastrophic collapse of Sasanian power following the Byzantine-Sasanian wars and the internal political breakdown of the Persian state. He was the son of Shahrbaraz, the great Sasanian military commander who had conquered Egypt, Palestine, and Syria for Persia, and who himself briefly seized the throne before being overthrown.\n\nShapur-i Shahrvaraz's brief reign falls in one of the most dramatic periods of ancient Near Eastern history: the years immediately following the Byzantine Emperor Heraclius's decisive victory over the Sasanian Empire in the series of campaigns (622–628 CE) that reversed the previous Persian conquests of Egypt, Syria, and Anatolia, recovered the True Cross captured from Jerusalem, and forced Persia to restore all conquered territories. The Sasanian defeat led to the assassination of the war-emperor Khosrow II (628 CE) by his own nobles, triggering a succession crisis in which multiple claimants — including Kavad II (son of Khosrow II), Ardashir III, Shahrbaraz (Shapur-i Shahrvaraz's father), Boran, Azarmidokht, and finally Yazdegerd III — seized and lost the Persian throne in rapid succession between 628 and 634 CE.\n\nThis period of Sasanian internal collapse — in which Shapur-i Shahrvaraz was one of multiple short-lived rulers — was the direct precondition for the Arab Islamic conquest of Persia. When the Arab armies began their campaigns against Persia in 633–634 CE, they confronted an empire exhausted by three decades of war with Byzantium, drained of treasure and manpower, and politically fragmented by the succession crisis. The Sasanian Empire — once one of the most powerful states in the world — fell to the Arabs with remarkable speed, with its last emperor Yazdegerd III dying a fugitive in 651 CE.",
    "causes": [
      "The catastrophic Sasanian defeat in the Byzantine-Sasanian War (622–628 CE) — Heraclius's reversal of all Persian conquests, the loss of the Persian treasury captured from Ctesiphon, and the humiliating peace — destabilised Khosrow II's position and triggered the succession crisis that created the chaotic conditions in which Shapur-i Shahrvaraz briefly claimed the throne.",
      "The assassination of Khosrow II (628 CE) by Persian nobles who blamed him for the war's catastrophic outcome — and the subsequent rapid succession of multiple claimants, none able to consolidate power — created the political vacuum within which Shahrbaraz and his son Shapur-i Shahrvaraz could attempt to seize the throne.",
      "The structural weaknesses of the late Sasanian state — the overmighty nobles (the dehqans and great houses), the military's dependence on these nobles' resources, and the lack of a clear succession mechanism — made the post-war political collapse extremely difficult to arrest, as each attempted usurpation triggered further instability."
    ],
    "effects": [
      "Shapur-i Shahrvaraz's brief reign was one episode in the catastrophic Sasanian succession crisis of 628–634 CE — a period of political disintegration that left the Persian Empire unable to resist the Arab Muslim armies that invaded from 633 CE, leading to the complete collapse of Sasanian power by 651 CE.",
      "The fall of the Sasanian Empire — the political context within which Shapur-i Shahrvaraz's brief claim occurred — produced the Islamisation of Iran, one of the most consequential civilisational transformations in world history: the replacement of Zoroastrian Persian culture with Islamic Arab culture that created the Iranian Islamic civilisation.",
      "The speed and completeness of the Arab conquest of Persia — facilitated by the Sasanian succession crisis — demonstrated the catastrophic vulnerability of centralised empires to simultaneous internal political collapse and external military pressure, a pattern observed repeatedly in world history."
    ],
    "relationships": [
      {"sourceSlug": "shapur-i-shahrvaraz", "sourceName": "Shapur-i Shahrvaraz", "verb": "SON_OF", "targetSlug": "shahrbaraz", "targetName": "Shahrbaraz (Sasanian general and king)", "context": "Shapur-i Shahrvaraz was the son of the great Sasanian general Shahrbaraz — who had conquered Egypt and Palestine before himself briefly seizing the Persian throne in 629 CE."},
      {"sourceSlug": "sasanian-empire", "sourceName": "Sasanian Empire", "verb": "COLLAPSES_DURING", "targetSlug": "shapur-i-shahrvaraz", "targetName": "Shapur-i Shahrvaraz (and succession crisis)", "context": "Shapur-i Shahrvaraz's reign was part of the catastrophic Sasanian succession crisis of 628–634 CE — the internal collapse that made Persia unable to resist the Arab Islamic conquest."},
      {"sourceSlug": "arab-islamic-conquest-of-persia", "sourceName": "Arab Islamic Conquest of Persia (633–651 CE)", "verb": "EXPLOITS", "targetSlug": "shapur-i-shahrvaraz", "targetName": "Sasanian Succession Crisis (including Shapur-i Shahrvaraz)", "context": "The Arab Muslim armies invaded a Persia weakened and fragmented by the succession crisis — the political collapse that had included Shapur-i Shahrvaraz's brief reign — and rapidly conquered the exhausted empire."}
    ],
    "places": [
      {"name": "Ctesiphon (Iraq), Sasanian Empire", "role": "The capital of the Sasanian Empire — the political centre of the collapsing empire within which Shapur-i Shahrvaraz's brief claim to the throne took place"},
      {"name": "Greater Iran (Persia)", "role": "The geographic core of the Sasanian state whose political fragmentation and Arab conquest followed the succession crisis in which Shapur-i Shahrvaraz was one claimant"}
    ],
    "subjects": ["Sasanian Empire", "Persian History", "Classical Era", "Late Antiquity", "Islamic Conquest", "Ancient Near East", "Byzantine-Persian Wars", "7th Century CE"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 3,
      "significanceNarrative": "Shapur-i Shahrvaraz (died 630 CE) was a brief Sasanian claimant during the catastrophic succession crisis (628–634 CE) that followed Persia's defeat by Heraclius. His reign was one episode in the political disintegration that left the Sasanian Empire unable to resist the Arab Islamic conquest — one of the most consequential civilisational transformations in world history.",
      "significanceCategory": "local"
    }
  }
},

"donnchad-mac-briain": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221donnchad-mac-briain.json",
  "slug": "donnchad-mac-briain",
  "data": {
    "summary": "Donnchad mac Briain (died 1064 CE) was an Irish king — one of the sons of Brian Boru, the High King of Ireland who died at the Battle of Clontarf (1014 CE) — who served as King of Munster for a period and whose stormy career illustrates the persistent political instability of Irish kingship in the 11th century. He was the son of the greatest figure in early medieval Irish history, and his life was defined by the shadow of his father's achievement and by the factional conflicts among the Dal Cais (Dál Cais) dynasty — Brian Boru's family — that prevented any of Brian's sons or grandsons from consolidating the pan-Irish supremacy that Brian had briefly achieved.\n\nDonnchad's political career was characterised by violent competition with his brothers and his nephew Toirdelbach for control of Munster and the wider claim to the Irish high kingship. He served as king of Munster from 1014 (following Brian Boru's death at Clontarf) through various periods of conflict and displacement. His reign saw the continuation of the factional violence that had marked Irish politics before Brian Boru's rise — the competing claims of Munster, Leinster, Connacht, and Ulster for supremacy — without the ability of any single figure to replicate Brian Boru's achievement.\n\nDonnchad's later life took a remarkable turn: he undertook a pilgrimage to Rome (c. 1063–1064 CE) and died on the journey or shortly after reaching Rome in 1064 CE — an act of pious pilgrimage that was both a genuine expression of medieval Christian devotion and, given his political difficulties at home, perhaps also a pragmatic withdrawal from the violent factional conflicts that had consumed his kingship. His pilgrimage is recorded in the Irish annals and represents the broader pattern of Irish royal and ecclesiastical pilgrimages to Rome that connected Ireland to the wider Latin Christian world.",
    "causes": [
      "Brian Boru's extraordinary achievement at Clontarf (1014 CE) — eliminating the Viking power in Ireland and briefly asserting pan-Irish supremacy — created both the dynastic legacy that Donnchad inherited and the impossibly high standard against which his own kingship was measured.",
      "The structural instability of the Irish kingship system — in which the king of a provincial dynasty like Munster had to continuously demonstrate military dominance over rivals, and in which succession was contested among all members of the royal kin-group rather than passing automatically to a single heir — made Donnchad's hold on power perpetually vulnerable.",
      "The internecine conflict within the Dal Cais dynasty following Brian Boru's death — multiple sons and nephews competing for the Munster kingship and the wider high-kingship claim — was the immediate cause of the political turbulence that defined Donnchad's reign and that eventually drove him to pilgrimage."
    ],
    "effects": [
      "Donnchad's failure to consolidate the pan-Irish supremacy his father had achieved contributed to the continuation of the fragmented multi-kingdom political system of Ireland — the decentralised structure that would make Ireland vulnerable to Norman intervention when Diarmait Mac Murchada invited the Normans in 1169 CE.",
      "Donnchad's pilgrimage to Rome (c. 1063–1064 CE) — whatever its personal motivations — was part of the broader pattern of Irish royal and ecclesiastical engagement with Rome that integrated Ireland into the reforming Latin Christian world of the 11th century, contributing to the Gregorian Reform's eventual impact on the Irish church.",
      "The struggles of Brian Boru's sons — including Donnchad — to hold the position their father had created demonstrated the structural limits of 11th-century Irish political institutions: without the bureaucratic infrastructure of centralised kingship, even the greatest military achievement could not create stable dynastic succession."
    ],
    "relationships": [
      {"sourceSlug": "donnchad-mac-briain", "sourceName": "Donnchad mac Briain", "verb": "SON_OF", "targetSlug": "brian-boru", "targetName": "Brian Boru (High King of Ireland)", "context": "Donnchad was the son of Brian Boru — the greatest figure in medieval Irish history — whose death at Clontarf (1014 CE) left his sons competing for the legacy of his briefly achieved pan-Irish supremacy."},
      {"sourceSlug": "donnchad-mac-briain", "sourceName": "Donnchad mac Briain", "verb": "RULES", "targetSlug": "kingdom-of-munster", "targetName": "Kingdom of Munster", "context": "Donnchad served as King of Munster from 1014 CE — the southern Irish province that was the Dal Cais base — through years of factional conflict with his brothers and nephew."},
      {"sourceSlug": "battle-of-clontarf", "sourceName": "Battle of Clontarf (1014 CE)", "verb": "SHAPES", "targetSlug": "donnchad-mac-briain", "targetName": "Donnchad mac Briain", "context": "Brian Boru's death at Clontarf and the removal of his central unifying authority shaped the entire political context of Donnchad's reign — the sons' inability to replicate his achievement was the defining failure of the Dal Cais dynasty."}
    ],
    "places": [
      {"name": "Munster, Ireland", "role": "Donnchad's kingdom — the southern Irish province and Dal Cais heartland that he contested and ruled through the tumultuous decades after Clontarf"},
      {"name": "Rome (Italy)", "role": "The destination of Donnchad's final pilgrimage (c. 1063–1064 CE) — where he died, an act of both piety and political withdrawal from the factional conflicts of Irish kingship"}
    ],
    "subjects": ["Irish History", "Medieval Ireland", "Classical Era", "Viking Age", "Celtic History", "Medieval History", "High Kingship of Ireland", "11th Century"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 4,
      "significanceNarrative": "Donnchad mac Briain (died 1064 CE) was a son of Brian Boru and King of Munster — one of the claimants to Brian's legacy who failed to consolidate his father's pan-Irish supremacy. His stormy reign illustrates the structural instability of 11th-century Irish kingship, and his pilgrimage to Rome (where he died) reflects the integration of Irish royal culture with the wider Latin Christian world.",
      "significanceCategory": "regional"
    }
  }
},

"demetrius-iii": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221demetrius-iii.json",
  "slug": "demetrius-iii",
  "data": {
    "summary": "Demetrius III Aniketos (Greek: Δημήτριος Ἀνίκητος; 'the invincible'; fl. c. 100–80 BCE) was an Indo-Greek king who ruled portions of the Indo-Greek kingdom — the fascinating political entity created by the successors of Alexander the Great's eastern conquests in the region of Bactria and northwestern India (modern Afghanistan and Pakistan). He was one of numerous Indo-Greek rulers who issued coins with both Greek and Kharoshthi (Indian) legends, demonstrating the hybrid Hellenistic-Indian culture of his kingdom.\n\nThe Indo-Greek Kingdom (c. 200–10 BCE) was one of the most remarkable political entities of the ancient world: a Greek-speaking dynasty ruling over populations of Indian, Iranian, and Hellenistic descent in the frontier zone between the Greek world and the Indian subcontinent. Its kings — many known primarily through their coins — issued bilingual and biscript currency combining Greek imagery and text with Indian Kharoshthi script, reflecting the multicultural reality of their realm. The most famous Indo-Greek ruler was Menander I (Milinda; c. 165–130 BCE), who is the subject of the Buddhist philosophical dialogue the Milindapanha ('Questions of Milinda'), suggesting that some Indo-Greek rulers converted to Buddhism.\n\nDemetrius III's specific historical record is almost entirely numismatic — his existence and the general outline of his reign are known primarily through coins bearing his name and portrait. He is associated with the period of increasing fragmentation of the Indo-Greek kingdom in the late 2nd–early 1st centuries BCE, as the kingdom splintered into multiple competing sub-kingdoms and as pressure from the Scythian (Saka) peoples from the north and west gradually displaced the Indo-Greek rulers from their territories. His epithet 'Aniketos' ('invincible') suggests a ruler who wished to project military strength in a period of increasing difficulty.",
    "causes": [
      "The fragmentation of the Indo-Greek kingdom in the late 2nd–1st century BCE — following the death of the great king Menander I — produced the conditions in which multiple competing kings like Demetrius III controlled different portions of the former unified kingdom.",
      "The Scythian (Saka) and Parthian pressures from the northwest — nomadic and semi-nomadic peoples who were progressively displacing the Indo-Greek rulers from their Bactrian and northwestern Indian territories — created the military and political challenges within which Demetrius III's reign unfolded.",
      "The multicultural character of the Indo-Greek kingdom — combining Greek political forms with Indian religious traditions, producing the bilingual coins and the possible conversion of some rulers to Buddhism — reflected the creative synthesis that resulted from Alexander's eastern conquests and the subsequent interactions of Hellenistic and Indian civilisations."
    ],
    "effects": [
      "Demetrius III's coinage — bilingual Greek-Kharoshthi coins bearing his portrait — provides direct evidence for the Indo-Greek kingdom's remarkable cultural synthesis and is one of the primary sources for reconstructing the political history of this poorly documented but fascinating ancient state.",
      "The Indo-Greek kingdom of which Demetrius III was part left an enduring artistic legacy in the Buddhist art of the Gandhara region — the Greco-Buddhist artistic style that depicted the Buddha in Greek-influenced figurative forms and that spread Buddhist art across Central and East Asia, making the Indo-Greek synthesis one of the most consequential cultural encounters of the ancient world.",
      "The eventual displacement of the Indo-Greek kings by Scythian, Parthian, and Kushan rulers — the process within which Demetrius III's reign falls — completed the transition of northwestern India from a zone of Hellenistic influence to one dominated by Iranian-nomadic cultures, representing the final retreat of Alexander's eastern legacy."
    ],
    "relationships": [
      {"sourceSlug": "demetrius-iii", "sourceName": "Demetrius III Aniketos", "verb": "RULES", "targetSlug": "indo-greek-kingdom", "targetName": "Indo-Greek Kingdom", "context": "Demetrius III was one of the later kings of the fragmented Indo-Greek kingdom — his bilingual coins are almost the only evidence for his reign."},
      {"sourceSlug": "indo-greek-kingdom", "sourceName": "Indo-Greek Kingdom", "verb": "PRODUCES", "targetSlug": "greco-buddhist-art", "targetName": "Greco-Buddhist Art (Gandhara)", "context": "The Indo-Greek kingdom's multicultural synthesis produced Greco-Buddhist art — the fusion of Greek figurative style with Buddhist iconography that created the first Buddha images and influenced Buddhist art across Asia."},
      {"sourceSlug": "scythian-saka-peoples", "sourceName": "Scythian (Saka) Peoples", "verb": "DISPLACES", "targetSlug": "demetrius-iii", "targetName": "Indo-Greek Kings (including Demetrius III)", "context": "The Saka pressure from the northwest was gradually displacing Indo-Greek rulers from their territories in the period of Demetrius III's reign — the process that would end the Indo-Greek kingdom by c. 10 BCE."}
    ],
    "places": [
      {"name": "Bactria and Northwestern India (modern Afghanistan/Pakistan)", "role": "The territory of the Indo-Greek kingdom — the Hellenistic-Indian frontier zone where Demetrius III ruled"},
      {"name": "Gandhara (modern northwestern Pakistan/eastern Afghanistan)", "role": "The cultural heartland of the Indo-Greek synthesis — the region where Greco-Buddhist art developed and from which it spread across Asia"}
    ],
    "subjects": ["Hellenistic History", "Ancient India", "Classical Era", "Indo-Greek Kingdom", "Buddhism", "Ancient History", "Numismatics", "Central Asia"],
    "frameworks": ["WORLD_SYSTEMS", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 4,
      "significanceNarrative": "Demetrius III Aniketos was a ruler of the fragmented Indo-Greek kingdom (c. 100–80 BCE) — one of the remarkable Hellenistic-Indian hybrid monarchies whose bilingual coins are almost the only evidence for his reign. His kingdom's cultural legacy — Greco-Buddhist art — was one of the most consequential artistic syntheses of the ancient world, producing the first Buddha images and influencing Buddhist iconography across Asia.",
      "significanceCategory": "regional"
    }
  }
},

"saint-fergus": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250saint-fergus.json",
  "slug": "saint-fergus",
  "data": {
    "summary": "Saint Fergus (also Fergustian or Fergustianus; died c. 730 CE) was an Irish bishop-missionary who brought Christianity from Ireland to Scotland — specifically to the region of Pictland in the northeast of Scotland — and is venerated as the patron saint of the Scottish town of Forfar and several other parishes in Angus and Aberdeenshire. He is one of the Irish peregrini ('wanderers for Christ') — the Irish missionary monks who, following the tradition of Columba (521–597 CE), voluntarily exiled themselves from Ireland to bring Christianity to pagan peoples in Scotland, England, and continental Europe.\n\nFergus is believed to have worked in the Pictish kingdom of northeastern Scotland in the early 8th century, establishing churches and communities in the region that would eventually become the county of Angus (Forfarshire). The Pictish church — the Christianity of the ancient Pictish people who inhabited Scotland north of the Forth-Clyde line before the Gaelic kingdoms absorbed them — was largely a product of Irish missionary activity, and Fergus represents one of the Irish missionaries who extended this evangelisation into the northeastern corners of Scotland. His feast day is 18 November.\n\nThe historical documentation for Fergus is almost entirely hagiographic — the medieval church records and local traditions that preserved his memory — and the details of his life must be reconstructed from these sources with appropriate caution. He is represented in the iconography of medieval Scottish church art (notably in the cathedral of Dundee), and churches dedicated to him in multiple Scottish parishes testify to the geographic spread of his missionary activity. His story exemplifies the remarkable phenomenon of Irish monastic Christianity — the penitential pilgrimage tradition in which Irish monks sought spiritual merit through voluntary exile and missionary activity in foreign lands.",
    "causes": [
      "The Irish monastic tradition of voluntary exile for Christ (peregrinatio pro Christo) — the spirituality of voluntary exile as a form of ascetic devotion that had already produced Columba's Iona mission and Columbanus's continental missions — motivated Fergus's departure from Ireland to Pictland.",
      "The Pictish kingdom's partial Christianisation through earlier Irish and Northumbrian missions (Columba's work, Aidan's Northumbrian missions) — and the continuing need for deeper evangelisation in remote northeastern areas — created the missionary opportunity that Fergus's journey addressed.",
      "The early 8th century context of increasing integration between the Irish church and the Pictish and Northumbrian churches — including the Pictish church's adoption of the Roman Easter calculation and its closer alignment with continental practices — provided the broader ecclesiastical context for Fergus's activity."
    ],
    "effects": [
      "Fergus's missionary activity in the Angus region established churches and communities that became part of the Pictish church's network — contributing to the Christianisation of northeastern Scotland and to the religious infrastructure that survived the eventual absorption of the Pictish kingdom by the Gaelic Dál Riata to form the Kingdom of Scotland.",
      "The cult of Fergus — centred on the churches dedicated to him in Angus and Aberdeenshire — provided these Scottish communities with a patron saint whose Irish origin connected the local church to the broader Celtic Christian tradition, embedding the memory of the Irish mission within Scottish local religious identity.",
      "Saint Fergus represents the broader phenomenon of Irish missionary Christianity — the peregrini who were instrumental in the Christianisation of Scotland, northern England, and continental Europe, and whose tradition of scholarly monasticism was a major force in the preservation and transmission of classical learning through the early medieval period."
    ],
    "relationships": [
      {"sourceSlug": "saint-fergus", "sourceName": "Saint Fergus", "verb": "EVANGELISES", "targetSlug": "pictish-kingdom", "targetName": "Pictish Kingdom (northeastern Scotland)", "context": "Fergus was an Irish missionary bishop who brought Christianity to the Pictish regions of Angus and Aberdeenshire in northeastern Scotland, establishing churches that became part of the Pictish church network."},
      {"sourceSlug": "irish-monastic-tradition", "sourceName": "Irish Monastic Tradition (peregrinatio)", "verb": "PRODUCES", "targetSlug": "saint-fergus", "targetName": "Saint Fergus", "context": "Fergus was a product of the Irish peregrini tradition — the voluntary exile for Christ that sent Irish monks as missionaries to Scotland, England, and the continent."},
      {"sourceSlug": "columba", "sourceName": "Columba (521–597 CE)", "verb": "INSPIRES", "targetSlug": "saint-fergus", "targetName": "Saint Fergus", "context": "Columba's Iona mission — the foundational Irish Christian mission to Scotland — established the model and tradition within which Fergus's subsequent missionary work in Pictland followed."}
    ],
    "places": [
      {"name": "Angus (Forfarshire), Scotland", "role": "The primary region of Fergus's missionary activity — the northeastern Scottish area where he established churches and communities and where his cult was centred"},
      {"name": "Ireland (origin)", "role": "Fergus's homeland — the Irish monastic culture that shaped his formation and from which he departed as a peregrinus to Pictland"}
    ],
    "subjects": ["Early Christianity", "Scottish History", "Classical Era", "Celtic Christianity", "Missionary Activity", "Medieval History", "Saints", "Pictish Kingdom"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 3,
      "significanceNarrative": "Saint Fergus (died c. 730 CE) was an Irish missionary bishop who brought Christianity to northeastern Scotland — one of the Irish peregrini whose voluntary exile missions were instrumental in the Christianisation of the British Isles. His cult, centred on churches in Angus and Aberdeenshire, made him the patron saint of Forfar and embedded the memory of the Irish mission within Scottish local religious identity.",
      "significanceCategory": "local"
    }
  }
},

"lazarus-spengler": {
  "filepath": "data/appwrite-export/entities/252-Class-252/252lazarus-spengler.json",
  "slug": "lazarus-spengler",
  "data": {
    "summary": "Lazarus Spengler (1479–7 September 1534) was a German humanist, jurist, and city councillor of Nuremberg — one of the most important early lay supporters of Martin Luther's Reformation and a key figure in the implementation of Lutheranism in Nuremberg, the most significant imperial free city to adopt the Reformation in the early 1520s. He served as the secretary (Ratsschreiber) and later as a senior official of the Nuremberg city council, where he became the most influential lay advocate for the Lutheran cause in a city whose support was crucial to the early success of the Reformation.\n\nSpengler was one of the first educated German laymen to publicly embrace Luther's theology — he composed one of the earliest vernacular defences of Luther ('Schutzrede,' 1519) and was named alongside Luther and Ulrich von Hutten in the papal bull 'Exsurge Domine' (1520) that threatened Luther with excommunication. His position in Nuremberg's city government allowed him to influence the council's religious policy, and when Nuremberg officially adopted Lutheranism in 1525 — becoming the first major German imperial city to do so — Spengler's work had been central to that outcome. He was closely associated with the Nuremberg humanist circle (which included Albrecht Dürer, Willibald Pirckheimer, and Christoph Scheurl) and with the Saxon-Nuremberg axis that was crucial to early Lutheranism's survival.\n\nNuremberg's adoption of the Reformation in 1525 was a pivotal moment: as a major centre of printing, commerce, and Imperial politics — and as the city that hosted the Imperial Diet more frequently than any other — its Lutheran turn gave the Reformation institutional and economic resources that greatly enhanced its survival prospects. Spengler's role as the council's religious policy architect made him the lay embodiment of how humanist civic culture and Lutheran theology could be fused into a new Protestant urban identity.",
    "causes": [
      "Spengler's formation in Nuremberg's humanist culture — his connections to the Pirckheimer circle, his legal and classical education, and his engagement with the humanist critique of ecclesiastical corruption — prepared him to recognise Luther's theological challenge as the fulfilment of the reform agenda that humanists had long desired.",
      "Luther's theological breakthrough — particularly his attack on indulgences (1517), his defence of scripture as the sole authority (sola scriptura), and his challenge to papal jurisdiction — resonated with Spengler's humanist concerns about church corruption and provided the theological foundation for a reform he was willing to publicly support.",
      "Nuremberg's unique position as an imperial free city with a tradition of asserting civic authority over church affairs — and with a literate, commercially successful patriciate that valued reform and had the institutional capacity to implement religious change — made it the ideal environment for Spengler's lay Reformation advocacy."
    ],
    "effects": [
      "Spengler's advocacy and the Nuremberg city council's adoption of Lutheranism (1525) made Nuremberg the model for the Protestant imperial city — demonstrating how humanist civic culture, Protestant theology, and republican self-governance could be combined into a durable urban Reformation. The Nuremberg model was influential for other German cities contemplating the Reformation.",
      "Spengler's inclusion in 'Exsurge Domine' (1520) alongside Luther showed the papacy's recognition that lay intellectuals — not just clergy — were central to the Lutheran movement, a recognition that shaped the papal strategy of condemning the broader circle of reformers rather than focusing only on Luther.",
      "Nuremberg's printing industry — enhanced by the city's Lutheran turn and the demand for Protestant literature — became one of the most important centres for the production and distribution of Protestant tracts, sermons, and Bibles, making Spengler's city a crucial node in the information network that spread the Reformation across Germany."
    ],
    "relationships": [
      {"sourceSlug": "lazarus-spengler", "sourceName": "Lazarus Spengler", "verb": "SUPPORTS", "targetSlug": "martin-luther", "targetName": "Martin Luther", "context": "Spengler was one of the earliest and most important lay supporters of Luther — named alongside Luther in the papal bull Exsurge Domine (1520) and central to Nuremberg's adoption of Lutheranism in 1525."},
      {"sourceSlug": "lazarus-spengler", "sourceName": "Lazarus Spengler", "verb": "IMPLEMENTS", "targetSlug": "nuremberg-reformation", "targetName": "Nuremberg Reformation (1525)", "context": "As Nuremberg's senior city council official, Spengler was the architect of the council's religious policy — his advocacy was central to Nuremberg becoming the first major German imperial city to officially adopt Lutheranism."},
      {"sourceSlug": "nuremberg-humanist-circle", "sourceName": "Nuremberg Humanist Circle (Dürer, Pirckheimer)", "verb": "SHAPES", "targetSlug": "lazarus-spengler", "targetName": "Lazarus Spengler", "context": "Spengler was embedded in Nuremberg's humanist culture — his connections to Dürer, Pirckheimer, and Scheurl gave him the intellectual formation that made him receptive to Lutheran reform and capable of articulating it in civic terms."}
    ],
    "places": [
      {"name": "Nuremberg, Holy Roman Empire (Germany)", "role": "Spengler's city and the stage of his most important work — the imperial free city whose adoption of Lutheranism (1525) he helped engineer and whose model became influential for the Protestant Reformation's urban development"},
      {"name": "Wittenberg, Saxony", "role": "Luther's base and the intellectual centre of early Lutheranism — the theological source from which Spengler drew his religious ideas and with which Nuremberg maintained the crucial Saxon-Nuremberg alliance"}
    ],
    "subjects": ["Protestant Reformation", "German History", "Medieval Era", "Nuremberg", "Humanism", "Early Modern History", "Lutheran Reformation", "16th Century"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Lazarus Spengler (1479–1534) was the key lay architect of the Nuremberg Reformation — the city council official whose advocacy made Nuremberg the first major German imperial city to adopt Lutheranism (1525) and the model for Protestant urban governance. Named alongside Luther in the papal bull Exsurge Domine (1520), his career demonstrates how humanist civic culture and Lutheran theology fused into the Protestant urban identity that shaped Reformation Germany.",
      "significanceCategory": "significant"
    }
  }
},

"theatre-art": {
  "filepath": "data/appwrite-export/entities/130-Class-130/130theatre-art.json",
  "slug": "theatre-art",
  "data": {
    "summary": "Theatre is one of the oldest and most universal forms of human performance art — the staged enactment of narrative, character, and dramatic conflict before an audience, using the combined arts of acting, speech, movement, music, visual design, and storytelling in a shared physical or virtual space. Theatre's origins are ancient and multiple: the religious drama of ancient Athens (from Dionysian festivals to the tragedies of Aeschylus, Sophocles, and Euripides, c. 5th century BCE), the Sanskrit drama of ancient India (Natyashastra, c. 200 BCE), Chinese theatre forms (from court entertainment to the elaborately codified Peking Opera), and ritual performance traditions in cultures across every continent all represent independent points of theatrical origin.\n\nThe Greek tragic and comic drama of the 5th century BCE is the foundation of the Western theatrical tradition — Aeschylus's Oresteia, Sophocles's Oedipus Rex and Antigone, Euripides's Medea and Bacchae, and Aristophanes's comic plays established the dramatic forms, character types, and thematic concerns that influenced every subsequent Western playwright. Aristotle's Poetics (c. 335 BCE) — analysing tragedy's structure, the function of catharsis, and the elements of plot and character — became the theoretical foundation of Western dramatic criticism. Through Rome (Plautus, Terence, Seneca), the medieval mystery and morality plays, the Renaissance revival of classical drama, and the development of national theatrical traditions from the Elizabethan stage (Shakespeare) to the French classical theatre (Corneille, Racine, Molière) to the 18th-century bourgeois drama, theatre was continuously central to European cultural life.\n\nThe 19th and 20th centuries saw a revolutionary diversification of theatrical form: the realist drama of Ibsen and Chekhov, Brecht's epic theatre (designed to provoke critical thought rather than emotional identification), Stanislavski's acting method that influenced Hollywood, the absurdist theatre of Beckett and Ionesco, and the explosion of experimental, political, and postmodern theatre forms. In the 21st century, theatre coexists with film, television, and digital performance while maintaining its unique quality as a live, unrepeatable, embodied art form — the only performing art in which the human presence of performer and audience sharing a physical space remains irreplaceable.",
    "causes": [
      "The universal human cognitive disposition toward narrative and role-playing — the ability to simulate alternative realities, embody other perspectives, and explore social situations through pretend — created the psychological foundation from which theatrical performance emerged independently in multiple human cultures.",
      "Religious ritual as the matrix of early theatre: the Dionysian festivals that gave rise to Greek tragedy, the Sanskrit theatrical tradition's roots in Vedic ritual, and the medieval Christian mystery plays that dramatised Scripture all demonstrate how theatrical performance emerged from the ritual need to make sacred narratives present and vivid for communities.",
      "The development of urban civic life — the Greek polis's outdoor theatre as a democratic institution, the Roman amphitheatre, the Elizabethan public playhouse — created the institutional infrastructure and the paying audience that enabled theatre to develop as both an art form and a commercial enterprise."
    ],
    "effects": [
      "The Greek tragic and comic tradition — mediated through Roman drama, Renaissance revival, and continuous development — created the foundational forms (tragedy, comedy, and their subgenres) and the theoretical vocabulary (plot, character, catharsis) of Western literary culture, influencing not only drama but narrative fiction and film.",
      "Theatre has historically served as one of the primary means by which societies process, debate, and represent their central conflicts and values — from Athenian tragedy's engagement with hubris and fate to Shakespeare's explorations of power and identity to Brecht's political theatre to contemporary activist performance. Theatre's capacity to stage difficult truths has made it both a vehicle of social criticism and a target of censorship.",
      "The acting traditions developed in theatre — from the Greek mask-performance to Stanislavski's psychological realism — have shaped the theory and practice of performance across every medium. Stanislavski's 'Method' (developed for the Moscow Art Theatre) became the dominant acting approach in Hollywood and American theatre, making the theatre-trained actor the model for performance in film and television."
    ],
    "relationships": [
      {"sourceSlug": "theatre-art", "sourceName": "Theatre", "verb": "ORIGINATES_IN", "targetSlug": "greek-drama", "targetName": "Greek Drama (Aeschylus, Sophocles, Euripides)", "context": "The Greek tragic and comic drama of the 5th century BCE is the foundation of the Western theatrical tradition — establishing the dramatic forms, character types, and thematic concerns that influenced every subsequent playwright."},
      {"sourceSlug": "shakespeare", "sourceName": "William Shakespeare (1564–1616)", "verb": "SHAPES", "targetSlug": "theatre-art", "targetName": "Theatre (Western tradition)", "context": "Shakespeare's plays — written for the Elizabethan public stage — are the pinnacle of the Western theatrical tradition and the most performed dramatic works in world history."},
      {"sourceSlug": "theatre-art", "sourceName": "Theatre", "verb": "INFLUENCES", "targetSlug": "cinema", "targetName": "Cinema and Television", "context": "Theatre's acting traditions (especially Stanislavski's Method), narrative structures, and dramatic conventions are the foundational inheritance of cinema and television — the newer performance media that developed from and in dialogue with theatrical tradition."}
    ],
    "places": [
      {"name": "Athens, Greece (5th century BCE)", "role": "The birthplace of Western theatre — the Athenian polis whose Dionysian festivals produced the tragedies and comedies that are the foundation of Western dramatic tradition"},
      {"name": "Global (universal — Greece, India, China, Japan, Europe, Americas)", "role": "The universal scope of theatrical tradition — independent theatrical forms developed in multiple world cultures, making theatre one of the most globally distributed art forms"}
    ],
    "subjects": ["Performing Arts", "Art Forms", "Classical Era", "Drama", "Cultural History", "Ancient Greece", "Theatre History", "World Culture"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Theatre is one of the oldest and most universal art forms — from the Dionysian festivals of ancient Athens and the Sanskrit Natyashastra to Shakespeare's Globe and Brecht's epic theatre, theatrical performance has been central to how human societies process their conflicts, values, and experience. The Greek tragic tradition, codified by Aristotle's Poetics, created the foundational forms and theoretical vocabulary of Western literary culture, and theatre's acting traditions shaped cinema and television.",
      "significanceCategory": "world-changing"
    }
  }
},

"galaxy": {
  "filepath": "data/appwrite-export/entities/140-Class-140/140galaxy.json",
  "slug": "galaxy",
  "data": {
    "summary": "A galaxy is a gravitationally bound system of stars, stellar remnants, interstellar gas, dust, and dark matter — the fundamental large-scale structural unit of the visible universe. Galaxies range in size from dwarf galaxies containing a few hundred million stars to giant elliptical galaxies containing tens of trillions of stars, and they exist in an enormous variety of morphological types: spiral galaxies (like our own Milky Way and the Andromeda Galaxy), elliptical galaxies, lenticular galaxies, and irregular galaxies. The observable universe contains an estimated two trillion (2×10¹²) galaxies, distributed in a cosmic web of clusters, superclusters, filaments, and voids that represents the large-scale structure of the universe on the grandest scales.\n\nThe scientific understanding of galaxies has undergone revolutionary development in the 20th century. Before Edwin Hubble's observations in 1923–1924 — which used Cepheid variable stars to demonstrate that the Andromeda 'nebula' (M31) was far beyond the boundaries of the Milky Way — the nature of the 'spiral nebulae' observed by astronomers was hotly debated in the 'Great Debate' (1920) between Harlow Shapley (who argued they were within the Milky Way) and Heber Curtis (who argued they were separate galaxies). Hubble's resolution of the debate revealed that the universe consists of billions of galaxies, each itself containing billions of stars — a discovery that fundamentally transformed humanity's understanding of the scale and structure of the cosmos.\n\nModern galaxy science has revealed the central role of supermassive black holes in galactic structure and evolution — virtually every large galaxy contains a supermassive black hole at its centre (our Milky Way's is Sagittarius A*, mass ~4 million solar masses), and the feedback between black hole activity and star formation is now understood to be a central driver of galactic evolution. Dark matter — a form of matter that interacts gravitationally but not electromagnetically, and therefore invisible to telescopes — constitutes approximately 85% of all matter in the universe and provides the gravitational scaffolding within which galaxies form and maintain their structure. The James Webb Space Telescope (launched 2021) has revealed galaxies forming less than 300 million years after the Big Bang, providing new constraints on our models of galaxy formation and cosmic evolution.",
    "causes": [
      "The Big Bang (c. 13.8 billion years ago) and the subsequent gravitational collapse of small density fluctuations in the early universe — amplified by the gravitational pull of dark matter halos — produced the first galaxies approximately 200–400 million years after the Big Bang, initiating the process of hierarchical structure formation that built the cosmic web of galaxies observable today.",
      "Dark matter's gravitational dominance in the early universe provided the scaffolding within which ordinary (baryonic) matter condensed — without dark matter halos, galaxies could not have formed as quickly as observations show they did, and the large-scale structure of the universe would be radically different.",
      "The emergence of astronomy as an empirical science — from Galileo's telescope (1609) through 19th-century spectroscopy to 20th-century radio, X-ray, and infrared telescopes — progressively revealed the structure of the universe and enabled the understanding of galaxies as the fundamental large-scale building blocks of the cosmos."
    ],
    "effects": [
      "Hubble's 1923–1924 discovery that the Andromeda 'nebula' was a separate galaxy — revealing that the universe contains billions of galaxies, not just the Milky Way — was one of the most consequential scientific discoveries in history, transforming humanity's conception of the scale of the cosmos and inaugurating the modern era of extragalactic astronomy.",
      "The study of galaxies revealed the expansion of the universe (Hubble's Law, 1929 — more distant galaxies recede faster) and provided the observational evidence for the Big Bang cosmology, establishing the scientific picture of a universe that began in a hot, dense state and has been expanding and cooling for 13.8 billion years.",
      "The discovery that galaxies host supermassive black holes and that their evolution is shaped by dark matter — invisible components of the universe that together (dark matter plus dark energy) constitute 95% of the universe's total energy content — revealed that ordinary visible matter is a minor constituent of the cosmos, profoundly challenging any naive human-centred view of the universe."
    ],
    "relationships": [
      {"sourceSlug": "galaxy", "sourceName": "Galaxy", "verb": "DISCOVERED_BY", "targetSlug": "edwin-hubble", "targetName": "Edwin Hubble (1923–1924)", "context": "Hubble's use of Cepheid variables to demonstrate that Andromeda was a separate galaxy — not a nebula within the Milky Way — revealed the true scale of the universe and inaugurated extragalactic astronomy."},
      {"sourceSlug": "dark-matter", "sourceName": "Dark Matter", "verb": "STRUCTURES", "targetSlug": "galaxy", "targetName": "Galaxies", "context": "Dark matter provides the gravitational scaffolding within which galaxies form and maintain their structure — without dark matter halos, the observed pattern of galaxy formation could not be explained."},
      {"sourceSlug": "galaxy", "sourceName": "Galaxy", "verb": "CONTAINS", "targetSlug": "supermassive-black-hole", "targetName": "Supermassive Black Holes", "context": "Virtually every large galaxy contains a supermassive black hole at its centre — the feedback between black hole activity and star formation is now understood to be a central driver of galactic evolution."}
    ],
    "places": [
      {"name": "Observable Universe (universal)", "role": "The scale on which galaxies are distributed — the ~93 billion light-year observable universe containing an estimated 2 trillion galaxies organised in the cosmic web of clusters, filaments, and voids"},
      {"name": "Milky Way (our galaxy)", "role": "Humanity's home galaxy — the barred spiral galaxy containing our Solar System, approximately 100,000 light-years in diameter and containing 100–400 billion stars"}
    ],
    "subjects": ["Astronomy", "Cosmology", "Classical Era", "Astrophysics", "Natural Sciences", "Space", "Universe", "Modern Science"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Galaxies are the fundamental large-scale structural units of the observable universe — gravitationally bound systems of billions of stars, dark matter, gas, and dust. The scientific discovery that the universe contains two trillion galaxies (Hubble, 1923–1924) was one of the most consequential revolutions in human cosmology, and the subsequent understanding of galaxy formation, dark matter, supermassive black holes, and cosmic expansion has established the modern scientific picture of the universe's 13.8-billion-year history.",
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
