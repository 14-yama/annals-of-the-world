#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 17 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: medicine, william-of-paris, donatus-of-arezzo, john-helou,
          saadia-gaon, gaius-claudius-centho, exuperantius-of-cingoli, poetry
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-17-may2026"

ENRICHMENTS = {

"medicine": {
  "filepath": "data/appwrite-export/entities/126-Class-126/126medicine.json",
  "slug": "medicine",
  "data": {
    "summary": "Medicine is the science and practice of diagnosing, treating, preventing, and understanding disease and injury — one of the oldest and most consequential domains of human knowledge, with deep roots in all ancient civilisations and a transformative history of scientific development that has fundamentally altered human health, longevity, and demographic structure. Medicine encompasses both the empirical biological sciences (anatomy, physiology, pharmacology, microbiology, genetics) and the practical clinical arts of diagnosis and treatment, operating at the intersection of natural science, social institution, and ethical practice.\n\nThe history of medicine spans from the earliest human societies' use of medicinal plants and ritual healing to the systematic medical traditions of ancient Egypt (Ebers Papyrus, c. 1550 BCE), Mesopotamia, China (Huangdi Neijing, Yellow Emperor's Classic of Medicine, c. 300 BCE), India (Ayurveda, Sushruta's surgical treatise), and Greece — particularly the Hippocratic tradition (c. 400 BCE), which established the empirical-observational approach to disease, the importance of patient history, and the ethical framework encoded in the Hippocratic Oath. Islamic medicine (Avicenna's Canon of Medicine, c. 1025 CE) preserved and advanced Greek medical knowledge through the European Dark Ages, while the European Scientific Revolution produced the foundational discoveries that transformed medicine: William Harvey's discovery of blood circulation (1628), the microscope and germ theory (Leeuwenhoek, 1670s; Pasteur and Koch, 1860s–1880s), anaesthesia (Morton, 1846), antisepsis (Lister, 1867), and vaccination (Jenner, 1796).\n\nThe 20th century witnessed the most dramatic acceleration in medical history: the discovery of antibiotics (Fleming's penicillin, 1928; clinical use from 1940s), the eradication of smallpox (declared 1980), the double helix and the genetic revolution (Watson and Crick, 1953), organ transplantation (Barnard's first heart transplant, 1967), and the Human Genome Project (completed 2003). These advances transformed life expectancy from the global average of c. 30–35 years in 1900 to c. 72 years by 2020 — one of the most rapid and consequential changes in human biology in recorded history.",
    "causes": [
      "The universal human vulnerability to disease, injury, and suffering — and the consequent universal human motivation to develop effective responses — made the development of medical knowledge one of the oldest and most persistent intellectual projects in human history.",
      "The Scientific Revolution of the 17th century and its application to biological questions — Harvey's anatomical discoveries, the invention of the microscope, the Enlightenment's programme of systematic empirical observation — created the foundation on which modern scientific medicine was built, replacing humoral and supernatural models of disease with mechanistic and microbiological ones.",
      "The industrial and demographic pressures of the 19th century — urban overcrowding, epidemic diseases (cholera, typhoid, tuberculosis), and the scale of military medicine in the Napoleonic and Civil wars — created the practical urgency that drove the critical discoveries of germ theory, antisepsis, and anaesthesia that launched scientific clinical medicine."
    ],
    "effects": [
      "Modern medicine's most transformative impact has been on human longevity and demographic structure: the control of infectious disease through vaccination, antibiotics, and public health measures; the reduction of infant and maternal mortality; and surgical advances have raised global life expectancy from c. 35 years in 1900 to c. 72 years in 2020, adding an unprecedented number of human life-years to the global total and fundamentally restructuring the age composition of populations.",
      "The pharmaceutical and biotechnology industries — direct outgrowths of medical research — have become among the largest economic sectors in the world, generating trillions of dollars annually and creating the incentive structures, patents, and regulatory systems that shape how medical innovation is funded, distributed, and accessed globally.",
      "Medicine's globalisation — through the World Health Organisation (established 1948), international vaccination programmes, global disease surveillance networks, and the COVID-19 pandemic's acceleration of international health governance — has made health one of the central domains of global politics, international development, and human rights."
    ],
    "relationships": [
      {"sourceSlug": "medicine", "sourceName": "Medicine", "verb": "TRANSFORMED_BY", "targetSlug": "germ-theory", "targetName": "Germ Theory (Pasteur, Koch, 1860s–1880s)", "context": "Germ theory — the demonstration that infectious diseases are caused by microorganisms — was the most transformative single conceptual advance in medicine, replacing centuries of humoral theory and enabling the targeted development of vaccines, antibiotics, and aseptic surgery."},
      {"sourceSlug": "hippocrates", "sourceName": "Hippocrates (c. 460–370 BCE)", "verb": "FOUNDS", "targetSlug": "medicine", "targetName": "Western Clinical Medicine", "context": "The Hippocratic tradition established the empirical-observational approach to disease, the importance of prognosis and patient history, and the ethical framework (Hippocratic Oath) that remained foundational to Western medical practice for two millennia."},
      {"sourceSlug": "medicine", "sourceName": "Medicine", "verb": "PRODUCES", "targetSlug": "global-health", "targetName": "Global Health and Human Longevity Revolution", "context": "Modern medicine's advances in vaccination, antibiotics, and surgical technique produced the global health revolution of the 20th century — raising life expectancy by more than 30 years and fundamentally altering human demography."}
    ],
    "places": [
      {"name": "Ancient Greece (Cos, Alexandria), Islamic World, Europe (London, Paris, Berlin), Global", "role": "The successive geographic centres of medical advance — from Hippocratic Greece through Islamic synthesis to European scientific medicine to global health institutions"},
      {"name": "Global (universal)", "role": "Medicine's operational scope — as a universal human practice present in every culture and, in its modern scientific form, institutionalised globally through hospitals, medical schools, and international health organisations"}
    ],
    "subjects": ["Science", "Medicine", "Classical Era", "History of Science", "Public Health", "Biology", "Human Biology", "Modern History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Medicine is one of the most consequential domains of human knowledge — a universal practice whose scientific transformation since the 17th century has raised global life expectancy by more than 30 years, eradicated smallpox, and fundamentally altered human demography. From Hippocratic empiricism to germ theory to the genetic revolution, medicine's development represents one of the most sustained and impactful intellectual achievements in human history.",
      "significanceCategory": "world-changing"
    }
  }
},

"william-of-paris": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250william-of-paris.json",
  "slug": "william-of-paris",
  "data": {
    "summary": "William of Paris (died 1314), also known as Guillaume de Paris, was a French Dominican friar, theologian, and Inquisitor who served as the confessor and adviser of King Philip IV of France ('Philip the Fair') and who played a central role in one of the most dramatic and controversial episodes of medieval history: the suppression of the Order of the Knights Templar (1307–1312). As the royal confessor with royal authority to act as inquisitor, William of Paris conducted the initial interrogations of the arrested Templars following their sudden arrest on Friday 13 October 1307 — an event that has resonated in Western culture ever since, including as the claimed origin of the superstition around Friday the 13th.\n\nWilliam of Paris's role in the Templar affair was to extract confessions from the arrested Knights under torture — the standard inquisitorial procedure of the period — obtaining admissions of heresy (denial of Christ, obscene rituals, sodomy) that Philip IV used to justify the mass arrest and that formed the basis of the subsequent trials. Pope Clement V (the Avignon pope, himself under French political pressure) initially suspended the inquisition but eventually authorised a formal Church trial at the Council of Vienne (1311–1312), at which the Order was dissolved. The grand master Jacques de Molay and three other Templar leaders were burned at the stake in Paris in 1314.\n\nBeyond the Templar affair, William of Paris was a significant figure in late medieval Dominican intellectual and institutional life — a theologian who participated in the vigorous scholastic debates of the early 14th century and who represented the fusion of royal confessor, inquisitor, and Dominican friar that characterised the relationship between the Capetian monarchy and the mendicant orders. His career illustrates the intimate connection between French royal power, the Dominican inquisition, and the Avignon papacy in the early 14th century.",
    "causes": [
      "Philip IV's financial desperation — the enormous debts accumulated through wars with England and Flanders, and the appeal of seizing the Templars' vast wealth — provided the political motivation for the sudden arrest of 13 October 1307, which William of Paris executed as the king's inquisitorial agent.",
      "The Dominican Order's role as the primary instrument of papal inquisition in France — and the close relationship between the Dominican friars and the Capetian court through the institution of royal confessor — gave William of Paris both the authority and the institutional position to act as the lead interrogator of the arrested Templars.",
      "The theological vulnerability of the Templars to heresy charges — their secretive initiation rituals, their wealth, their perceived pride, and the broader late medieval anxiety about heterodox practices — provided the material from which William of Paris and Philip IV constructed the case for suppression."
    ],
    "effects": [
      "William of Paris's inquisitorial interrogations produced the confessions that justified the Templar suppression — confessions later repudiated by many Templars, including Grand Master Jacques de Molay at his death. The affair ended the most powerful military order of the crusading era, redistributed enormous wealth primarily to the Hospitallers and the French crown, and became one of the defining episodes of medieval injustice in popular and historical memory.",
      "The arrest of the Templars on Friday 13 October 1307 — ordered by Philip IV and executed by William of Paris — entered cultural memory as a harbinger of disaster and is one of the proposed origins of the Western superstition about Friday the 13th.",
      "The Templar affair and William of Paris's role in it exemplified the dangerous fusion of royal power and inquisitorial authority — the use of religious legal mechanisms to achieve purely political and financial objectives — that would recur in subsequent monarchical attacks on wealthy and independent institutions."
    ],
    "relationships": [
      {"sourceSlug": "william-of-paris", "sourceName": "William of Paris", "verb": "SERVES", "targetSlug": "philip-iv-of-france", "targetName": "Philip IV of France (Philip the Fair)", "context": "William of Paris was the royal confessor and trusted agent of Philip IV — his inquisitorial authority to interrogate the Templars came from his position as both Dominican inquisitor and royal confidant."},
      {"sourceSlug": "william-of-paris", "sourceName": "William of Paris", "verb": "INTERROGATES", "targetSlug": "knights-templar", "targetName": "Knights Templar", "context": "William of Paris conducted the initial inquisitorial interrogations of the arrested Templars following the mass arrest of 13 October 1307 — extracting the confessions of heresy that Philip IV used to justify the suppression."},
      {"sourceSlug": "suppression-of-knights-templar", "sourceName": "Suppression of the Knights Templar (1307–1312)", "verb": "INVOLVES", "targetSlug": "william-of-paris", "targetName": "William of Paris", "context": "The Templar suppression — one of the most dramatic events of medieval history — was executed with William of Paris as the key inquisitorial agent who obtained the confessions on which the trial was built."}
    ],
    "places": [
      {"name": "Paris, France (Capetian Kingdom)", "role": "The centre of William of Paris's activities — the royal court where he served as confessor and the city where the Templars were arrested, tried, and executed"},
      {"name": "France (Kingdom of the Capetians)", "role": "The broader context of William's career — the Capetian kingdom in its most powerful Valois-era phase, whose royal-Dominican alliance shaped both the Templar suppression and the Avignon papacy"}
    ],
    "subjects": ["Medieval France", "Dominican Order", "Classical Era", "Inquisition", "Knights Templar", "Medieval Church", "Medieval History", "Capetian France"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "William of Paris (died 1314) was the Dominican inquisitor and royal confessor who conducted the interrogations that produced the Templar confessions — a central agent in the suppression of the Knights Templar (1307–1312), one of the most consequential and controversial events of medieval history. His career exemplifies the fusion of royal power and inquisitorial authority that defined the Capetian monarchy's relationship with the mendicant orders.",
      "significanceCategory": "significant"
    }
  }
},

"donatus-of-arezzo": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250donatus-of-arezzo.json",
  "slug": "donatus-of-arezzo",
  "data": {
    "summary": "Donatus of Arezzo (died 9 August 362 CE) was an early Christian bishop of the Italian city of Arezzo (ancient Arretium) in Tuscany — venerated as a saint and martyr in both the Roman Catholic and Eastern Orthodox churches, with his feast day observed on 7 August (Eastern) and 9 August (Western). He is one of the founding figures of the Christian church in the Etruscan heartland of central Italy, and his martyrdom (according to tradition) occurred during the persecution of Christians under the Emperor Julian the Apostate (361–363 CE) — the last pagan Roman emperor, whose effort to reverse the Christianisation of the empire made him the target of the emerging Christian tradition of martyrdom narratives.\n\nAccording to hagiographic sources, Donatus was accompanied by the Irish monk Hilarianus (who is sometimes identified as his teacher), and the two worked together to spread Christianity in the region around Arezzo. The tradition records that Donatus restored a broken chalice during a liturgy — the scattered pieces reassembling miraculously — which became the miracle most associated with his cult. He was arrested under Julian's anti-Christian measures and executed, earning the crown of martyrdom that made him the patron saint of Arezzo.\n\nDonatus's cult was centred on the Cathedral of Arezzo (the Cattedrale dei Santi Donato e Hilarianus), which bears both his name and that of his companion, and which has preserved his relics. The city of Arezzo, which would become significant in medieval Italy as a Tuscan commune, maintained Donatus as its patron saint throughout the medieval period. His story is representative of the pattern of late antique Christian bishop-martyrs whose cults became the founding myths of Italian city-church identities — local traditions that embedded Christian origins in Roman imperial history and gave medieval cities their sacred genealogy.",
    "causes": [
      "The Emperor Julian the Apostate's programme of reversing the Christianisation of the Roman Empire (361–363 CE) — his promotion of traditional Roman paganism, withdrawal of privileges from the Christian church, and measures that put pressure on Christian communities — created the context of persecution within which Donatus's martyrdom is located.",
      "The post-Constantinian expansion of Christianity into the cities of central Italy — the establishment of episcopal sees in the towns of Etruria and Umbria following the Edict of Milan (313 CE) — created the institutional framework within which Donatus's bishopric of Arezzo was established.",
      "The developing tradition of Christian hagiography and the cult of saints in the 4th century — the growing practice of venerating martyrs, preserving their relics, and constructing narratives of their deaths as models of Christian courage — created the cultural context in which Donatus's story was preserved and transmitted."
    ],
    "effects": [
      "Donatus's cult as patron saint of Arezzo embedded the city's Christian identity in a narrative of apostolic-era martyrdom — giving the medieval commune of Arezzo a sacred foundation that legitimated its religious culture and provided a patron saint for civic devotion.",
      "The Cathedral of Arezzo — dedicated to Donatus and Hilarianus — became the architectural and liturgical centre of the city's religious life, a monument whose foundation in a martyr's cult connected medieval Arezzo to the history of early Christian Tuscany.",
      "Donatus's veneration as a martyr under Julian the Apostate contributed to the widespread Christian portrayal of Julian as a persecutor — reinforcing the narrative of Julian's reign as an attempted anti-Christian reaction that strengthened the church's martyrological tradition."
    ],
    "relationships": [
      {"sourceSlug": "donatus-of-arezzo", "sourceName": "Donatus of Arezzo", "verb": "FOUNDS", "targetSlug": "diocese-of-arezzo", "targetName": "Diocese of Arezzo", "context": "Donatus was the founding bishop of Arezzo — establishing the Christian community in this Tuscan city and becoming its patron saint."},
      {"sourceSlug": "julian-the-apostate", "sourceName": "Julian the Apostate (Emperor, 361–363 CE)", "verb": "MARTYRS", "targetSlug": "donatus-of-arezzo", "targetName": "Donatus of Arezzo", "context": "Donatus's martyrdom is traditionally attributed to the persecution under Julian the Apostate — the last pagan Roman emperor whose anti-Christian measures claimed Donatus as one of their victims."},
      {"sourceSlug": "arezzo", "sourceName": "Arezzo (Arretium), Tuscany", "verb": "VENERATES", "targetSlug": "donatus-of-arezzo", "targetName": "Donatus of Arezzo (patron saint)", "context": "Donatus became the patron saint of Arezzo — his cult centred on the cathedral bearing his name, which preserved his relics and provided the sacred foundation for the medieval Tuscan commune."}
    ],
    "places": [
      {"name": "Arezzo (Arretium), Tuscany, Italy", "role": "Donatus's episcopal city — the Tuscan city where he served as bishop, was martyred, and whose patron saint he became"},
      {"name": "Central Italy (Etruria/Tuscany)", "role": "The regional context of Donatus's mission — the former Etruscan heartland of Tuscany that was being Christianised in the post-Constantinian period"}
    ],
    "subjects": ["Early Christianity", "Late Roman Church", "Classical Era", "Italy", "Saints", "Martyrs", "4th Century CE", "Tuscany"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 3,
      "significanceNarrative": "Donatus of Arezzo (died 362 CE) was the founding bishop and patron saint of Arezzo in Tuscany — martyred (by tradition) under Julian the Apostate and venerated in both Western and Eastern churches. His cult, centred on the Cathedral of Arezzo, gave this important Tuscan city its sacred Christian foundation and represents the broader pattern of late antique bishop-martyrs who became the founding figures of Italian civic Christianity.",
      "significanceCategory": "local"
    }
  }
},

"john-helou": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250john-helou.json",
  "slug": "john-helou",
  "data": {
    "summary": "John Helou (Arabic: يوحنا حلو; died 12 May 1823) was a Lebanese Maronite Catholic bishop — serving as the Bishop of Batroun (a diocese in northern Lebanon) — who participated in the ecclesiastical and political life of Mount Lebanon during the Ottoman period of the late 18th and early 19th centuries. He was an ecclesiastical figure of the Maronite Church, the ancient Eastern Catholic church of Lebanon that had entered into full communion with Rome in 1736 at the Synod of Mount Lebanon while maintaining its distinctive Syriac liturgical tradition.\n\nJohn Helou's episcopal career falls in one of the most turbulent and consequential periods of Lebanese and Levantine history: the era of the Lebanese feudal dynasties (the Shihab emirs), Ottoman suzerainty over Mount Lebanon, and the beginning of the pressures from European powers and missionary activity that would transform the region in the 19th century. The Maronite bishops of this period played crucial roles not only as religious leaders but as political mediators, tax collectors, and intermediaries between the Ottoman authorities, the feudal emirs, and the European Catholic powers (particularly France, which had maintained a special relationship of protection over the Maronites since the Crusades).\n\nThe Diocese of Batroun, which John Helou headed, was one of the Maronite dioceses serving the northern Lebanese coast and the mountains behind it — a region of significant agricultural and commercial activity, dense Maronite settlement, and important monastic communities. Helou's tenure as bishop represents the Maronite Church's continued maintenance of its ecclesiastical structure and its community's identity through the late Ottoman period, contributing to the preservation of Maronite culture and political consciousness that would eventually contribute to the formation of the Lebanese national identity in the 20th century.",
    "causes": [
      "The Maronite Church's unique institutional position in Ottoman Mount Lebanon — recognised by the Ottomans as the religious and communal representative of the Maronite community, and protected by France as part of the Capitulations system — gave its bishops like Helou both religious and political authority that shaped their role in Lebanese society.",
      "The Synod of Mount Lebanon (1736) — which formalised the Maronite Church's relationship with Rome and reorganised its ecclesiastical structure — established the diocesan system within which Helou served as Bishop of Batroun, giving the Maronite hierarchy a more regularised canonical structure.",
      "The political instability of Ottoman Mount Lebanon in the late 18th and early 19th centuries — factional conflicts among the Shihab emirs, sectarian tensions, and the growing intervention of European powers — created the demanding environment within which Maronite bishops had to navigate between Ottoman, feudal, and European interests."
    ],
    "effects": [
      "John Helou's episcopal service contributed to the continuity of the Maronite Church's institutional presence in northern Lebanon — maintaining the ecclesiastical infrastructure of community life, education, and religious practice that preserved Maronite identity through the Ottoman period.",
      "The Diocese of Batroun under bishops like Helou remained a significant centre of Maronite monastic and educational activity — contributing to the community's relatively high literacy rates and the preservation of Syriac liturgical traditions.",
      "The Maronite bishops of this period — through their role as community intermediaries and their relationships with French consular protection — helped maintain the political consciousness and communal cohesion that would eventually underpin Lebanon's formation as a distinct political entity."
    ],
    "relationships": [
      {"sourceSlug": "john-helou", "sourceName": "John Helou", "verb": "LEADS", "targetSlug": "diocese-of-batroun", "targetName": "Diocese of Batroun (Maronite)", "context": "John Helou served as Bishop of Batroun — the Maronite diocese of northern Lebanon whose community he led during the turbulent late Ottoman period."},
      {"sourceSlug": "maronite-church", "sourceName": "Maronite Catholic Church", "verb": "EMPLOYS", "targetSlug": "john-helou", "targetName": "John Helou (Bishop)", "context": "John Helou was a Maronite Catholic bishop — a member of the ancient Lebanese church that maintained full communion with Rome while preserving its Syriac liturgical tradition under Ottoman suzerainty."},
      {"sourceSlug": "ottoman-mount-lebanon", "sourceName": "Ottoman Mount Lebanon (18th–19th century)", "verb": "CONTEXTUALISES", "targetSlug": "john-helou", "targetName": "John Helou", "context": "Helou's episcopal career unfolded in the politically complex Mount Lebanon of the late Ottoman period — between the Shihab emirs, Ottoman authorities, and European Catholic powers."}
    ],
    "places": [
      {"name": "Batroun, northern Lebanon", "role": "The diocese John Helou led — the northern Lebanese coastal city and its mountain hinterland, a region of dense Maronite settlement"},
      {"name": "Mount Lebanon, Ottoman Empire", "role": "The broader geographic and political context — the semi-autonomous mountain region under Ottoman suzerainty where the Maronite community maintained its distinctive religious and political identity"}
    ],
    "subjects": ["Maronite Church", "Lebanese History", "Classical Era", "Ottoman Empire", "Eastern Christianity", "Lebanon", "Middle Eastern History", "18th–19th Century"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 3,
      "significanceNarrative": "John Helou (died 1823) was a Maronite Catholic Bishop of Batroun in northern Lebanon — one of the ecclesiastical leaders who maintained Maronite institutional life and communal identity through the turbulent late Ottoman period. His significance lies in his contribution to the continuity of Maronite community structures that contributed to Lebanon's eventual formation as a distinct national entity.",
      "significanceCategory": "local"
    }
  }
},

"saadia-gaon": {
  "filepath": "data/appwrite-export/entities/210-Class-210/210saadia-gaon.json",
  "slug": "saadia-gaon",
  "data": {
    "summary": "Saadia Gaon (Hebrew: רַב סַעַדְיָה גָּאוֹן; Arabic: سعيد بن يوسف الفيومي; born 882/892 CE, Egypt; died 21 May 942 CE, Sura) was one of the most influential Jewish scholars of the medieval period — the Gaon (head) of the great Talmudic academy of Sura in Babylonia (modern Iraq), a prolific author in Hebrew and Arabic, and the founding figure of medieval Jewish philosophy and biblical scholarship. He is considered the first major Jewish philosopher of the medieval era and one of the most important figures in the entire history of Jewish thought, scholarship, and religious identity.\n\nBorn in the Fayyum region of Egypt, Saadia emerged as a prodigy in the fractious Jewish world of the early 10th century, first gaining prominence for his fierce polemics against the Karaite movement — a sect that rejected the Oral Torah (Talmud) and accepted only the written Hebrew Bible. His anti-Karaite polemics helped define the boundaries of Rabbinic Judaism at a critical moment of sectarian challenge. In 928 CE, the exilarch David ben Zakkai appointed him Gaon of Sura — the most prestigious position in Jewish intellectual life — though his tenure was marked by a bitter personal conflict with the exilarch that temporarily removed him from office. His restoration to the gaonate and continued scholarship until his death demonstrated the depth of respect he commanded in the broader Jewish world.\n\nSaadia's intellectual output was extraordinary in breadth and depth: his Arabic translation and commentary on the entire Hebrew Bible (the Tafsir) made Scripture accessible to the Arabic-speaking Jewish communities of the Abbasid caliphate; his philosophical masterwork 'Emunot ve-De'ot' (Book of Beliefs and Opinions, 933 CE) was the first systematic Jewish philosophy, applying kalam (Islamic scholastic theology) and Aristotelian logic to Jewish theological questions; and his works on Hebrew grammar, liturgical poetry (piyyutim), and Jewish law established him as a comprehensive reformer of Jewish intellectual life.",
    "causes": [
      "The Karaite schism — the 8th-century movement founded by Anan ben David that rejected the Oral Torah and threatened to split medieval Jewry — created the urgent intellectual challenge that propelled Saadia's early career as the most effective Rabbinic polemicist against Karaite claims, giving him his first wide reputation.",
      "The cultural and linguistic environment of the Abbasid caliphate — in which Arabic was the language of scholarship, philosophy, and intellectual life for Jews, Christians, and Muslims alike — shaped Saadia's methodology: his use of Arabic philosophical methods, his Arabic Bible translation, and his dialogue with Islamic kalam theology all reflected the creative synthesis possible in the multicultural Abbasid world.",
      "The political structure of Babylonian Jewry under the Abbasid caliphate — with the gaonate of Sura as the pre-eminent position of rabbinic scholarship and the exilarch as the political representative of the Jewish community — provided the institutional platform from which Saadia exercised his extraordinary intellectual influence."
    ],
    "effects": [
      "Saadia's 'Emunot ve-De'ot' (Book of Beliefs and Opinions, 933 CE) inaugurated the tradition of Jewish philosophical theology — applying Greek-Aristotelian and Islamic scholastic methods to Jewish theological questions — a tradition that would continue through Bahya ibn Paquda, Judah Halevi, and culminate in Maimonides' 'Guide for the Perplexed' (1190 CE). Saadia established that faith and reason were compatible and that Jewish theology could engage the philosophical challenges of the age.",
      "Saadia's Arabic translation of the Hebrew Bible (the Tafsir) — making Scripture accessible to the Arabic-speaking Jewish diaspora — became the standard Bible translation used by Jewish communities in the Arab world for centuries, shaping their understanding of Scripture and their engagement with Islamic theological arguments.",
      "Saadia's polemics against Karaism helped consolidate Rabbinic Judaism as the dominant form of Jewish religious practice — by intellectually defeating Karaite challenges and defending the authority of the Talmud with philosophical rigour, he contributed to the resilience of mainstream rabbinism at a critical moment of sectarian challenge."
    ],
    "relationships": [
      {"sourceSlug": "saadia-gaon", "sourceName": "Saadia Gaon", "verb": "PRODUCES", "targetSlug": "emunot-ve-deot", "targetName": "Emunot ve-De'ot (Book of Beliefs and Opinions)", "context": "Saadia's 'Emunot ve-De'ot' (933 CE) was the first systematic Jewish philosophical theology — inaugurating the tradition of rationalist Jewish thought that would culminate in Maimonides."},
      {"sourceSlug": "saadia-gaon", "sourceName": "Saadia Gaon", "verb": "OPPOSES", "targetSlug": "karaism", "targetName": "Karaite Judaism", "context": "Saadia's fierce polemics against Karaism — which rejected the Oral Torah — were instrumental in defending Rabbinic Judaism and consolidating its intellectual authority against the most significant medieval Jewish sectarian challenge."},
      {"sourceSlug": "maimonides", "sourceName": "Maimonides (1138–1204 CE)", "verb": "BUILDS_ON", "targetSlug": "saadia-gaon", "targetName": "Saadia Gaon's Philosophical Method", "context": "Maimonides' 'Guide for the Perplexed' — the pinnacle of medieval Jewish philosophy — built on the tradition of rationalist Jewish theology that Saadia had inaugurated, applying similar methods of philosophical synthesis to Jewish belief."}
    ],
    "places": [
      {"name": "Sura, Babylonia (Iraq)", "role": "The great Talmudic academy of which Saadia was Gaon — the most prestigious centre of rabbinic scholarship in the Jewish world and the base of his intellectual activity"},
      {"name": "Egypt (Fayyum)", "role": "Saadia's birthplace — the Egyptian Jewish community from which this prodigy emerged before moving to Babylonia to become the era's pre-eminent Jewish intellectual"}
    ],
    "subjects": ["Jewish History", "Medieval Judaism", "Medieval Era", "Jewish Philosophy", "Islamic Golden Age", "Medieval Scholarship", "Religious Thought", "Abbasid Caliphate"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Saadia Gaon (882–942 CE) was the founding figure of medieval Jewish philosophy — his 'Emunot ve-De'ot' (933 CE) was the first systematic philosophical theology in Jewish history, his Arabic Bible translation shaped Jewish communities across the Arab world, and his anti-Karaite polemics helped consolidate Rabbinic Judaism against its most serious medieval sectarian challenge. He inaugurated the tradition of rationalist Jewish thought that culminated in Maimonides.",
      "significanceCategory": "highly-significant"
    }
  }
},

"gaius-claudius-centho": {
  "filepath": "data/appwrite-export/entities/280-Class-280/280gaius-claudius-centho.json",
  "slug": "gaius-claudius-centho",
  "data": {
    "summary": "Gaius Claudius Centho (fl. c. 250 BCE) was a Roman politician and military commander of the mid-Republican period — a member of the patrician Claudian family, one of the most distinguished gentes (clans) of the Roman Republic, which had produced consuls, censors, and dictators since the earliest days of the Republic. He served as consul in 240 BCE, the year after the end of the First Punic War (264–241 BCE), placing him in the immediate aftermath of Rome's successful but exhausting first major overseas conflict — the war against Carthage for Sicily that ended with the Treaty of Lutatius and established Rome as a significant Mediterranean naval power.\n\nThe Claudian family's history in the Roman Republic was marked by a distinctive tradition of aristocratic pride, political prominence, and occasionally controversial behaviour — the Claudii were notorious for their hauteur and their readiness to challenge popular sentiment. Gaius Claudius Centho's specific historical record is limited — he appears in the Roman consular lists (the fasti) for 240 BCE and in the records of the Claudian family's political activities in this period, but without the detailed narrative treatment of the period's major military and political events.\n\nHis consulship falls in a period of Roman consolidation following the First Punic War: the pacification of Sardinia and Corsica (seized from Carthage in 238 BCE, despite the terms of the treaty), the beginning of Rome's expansion in northern Italy against the Gauls, and the preparations for what would become the Illyrian Wars and the eventually the Second Punic War. The decades following his consulship would see Rome transform from a peninsular power into the dominant force in the Western Mediterranean — a transformation in which the Claudian family's members continued to play significant roles.",
    "causes": [
      "The Roman Republican system of annual magistracies — the rotation of consuls, praetors, and other office-holders through the patrician and plebeian elite — created the institutional framework within which Gaius Claudius Centho's consulship occurred as part of the normal aristocratic cursus honorum.",
      "The Claudian family's centuries of prominence in Roman politics — their connections, client networks, wealth, and family prestige — provided the social capital that enabled Gaius Claudius Centho to reach the consulship in 240 BCE.",
      "The post-First Punic War context — Rome's need for experienced political and military leadership to manage the pacification of the newly acquired Sicilian province and the ongoing challenges from Gauls and Illyrians — shaped the political environment of Centho's consulship."
    ],
    "effects": [
      "Gaius Claudius Centho's consulship contributed to the governance of the Roman Republic in the critical decade following the First Punic War — a period of territorial consolidation, treaty revision, and preparation for Rome's next phase of Mediterranean expansion.",
      "His tenure as consul is preserved in the Roman fasti — the official list of magistrates that provides the chronological backbone of Roman Republican history — making his name part of the documentary record that allows historians to date events and trace the careers of the Roman aristocracy.",
      "The Claudian family's continued prominence through multiple generations — of which Centho's consulship was one instance — contributed to the clan's role in shaping Roman policy in the 3rd–2nd centuries BCE, including subsequent members who would be involved in major events of the Punic Wars."
    ],
    "relationships": [
      {"sourceSlug": "gaius-claudius-centho", "sourceName": "Gaius Claudius Centho", "verb": "MEMBER_OF", "targetSlug": "claudian-family", "targetName": "Claudian Family (gens Claudia)", "context": "Gaius Claudius Centho was a member of the patrician Claudian family — one of the most distinguished gentes of the Roman Republic — and his consulship is one entry in the family's long record of political prominence."},
      {"sourceSlug": "roman-republic", "sourceName": "Roman Republic", "verb": "ELECTS", "targetSlug": "gaius-claudius-centho", "targetName": "Gaius Claudius Centho (consul 240 BCE)", "context": "Gaius Claudius Centho served as Roman consul in 240 BCE — the year after the end of the First Punic War — as part of the Republican system of annual aristocratic magistracies."},
      {"sourceSlug": "first-punic-war", "sourceName": "First Punic War (264–241 BCE)", "verb": "PRECEDES", "targetSlug": "gaius-claudius-centho", "targetName": "Gaius Claudius Centho (consulship)", "context": "Centho's consulship in 240 BCE occurred in the immediate aftermath of Rome's First Punic War victory — the period of consolidation and expansion that followed Rome's emergence as a major Mediterranean power."}
    ],
    "places": [
      {"name": "Rome (Roman Republic)", "role": "The political centre of Centho's career — the city-state whose consulship he held in 240 BCE and whose expanding Mediterranean empire he helped govern"},
      {"name": "Mediterranean Basin (post-First Punic War)", "role": "The broader strategic context — the Western Mediterranean sphere in which Rome was establishing itself as the dominant power in the decades following Centho's consulship"}
    ],
    "subjects": ["Roman Republic", "Ancient Rome", "Classical Era", "Roman Politics", "Ancient History", "Roman Aristocracy", "3rd Century BCE", "Roman Magistrates"],
    "frameworks": ["STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 2,
      "significanceNarrative": "Gaius Claudius Centho was a Roman Republican consul (240 BCE) — a member of the distinguished Claudian family whose consulship in the year after the First Punic War is preserved in the Roman fasti. His significance is primarily as an entry in the Roman consular records and an example of the Claudian family's continuous prominence in the Republican period.",
      "significanceCategory": "local"
    }
  }
},

"exuperantius-of-cingoli": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250exuperantius-of-cingoli.json",
  "slug": "exuperantius-of-cingoli",
  "data": {
    "summary": "Exuperantius of Cingoli (died c. 500 CE) was an early Christian bishop — traditionally identified as the first bishop of the Italian city of Cingoli in the Marche region of central-eastern Italy, near the Adriatic coast — venerated as a saint in the Catholic Church with his feast day observed on 24 May. He is one of numerous bishop-saints of the late antique and early medieval period who served as the founding figures of local Italian dioceses and whose cults became the foundation of civic Christian identity in the cities of the Italian peninsula.\n\nCingoli — known in Roman times as Cingulum — was a small but historically notable hill-town in the Piceno region of ancient Italy: it was founded or refounded as a Roman town by Julius Caesar's father-in-law Lucius Calpurnius Piso Caesoninus, and played a role in the Social War (91–87 BCE). By the late Roman period, the town had become part of the Christianising network of dioceses being established across central Italy under the influence of the Roman and Ravennate churches. Exuperantius's episcopate — placing the establishment of Cingoli's diocese in the late 5th or early 6th century — falls in the tumultuous transition from the Western Roman Empire to Ostrogothic rule in Italy (Odoacer's deposition of Romulus Augustulus in 476 CE; Theodoric the Great's Ostrogothic kingdom, 493–526 CE).\n\nThe historical documentation for Exuperantius is almost entirely hagiographic — the traditions preserved in the local church of Cingoli about its founding bishop. His name (Exuperantius, 'surpassing' or 'outstanding') is a common late antique Christian name. The preservation of his memory through his feast day, the local cathedral, and the hagiographic tradition represents the typical mechanism by which the Christian identity of Italian cities was rooted in founding bishop-saint narratives.",
    "causes": [
      "The late antique Christianisation of the Italian countryside — the extension of the episcopal network from major cities to smaller towns like Cingoli in the 5th–6th centuries, driven by the Roman church's systematic organisation of suffragen sees — created the institutional context for Exuperantius's episcopate.",
      "The political disruption of the Western Roman Empire's collapse (476 CE) and its replacement by the Ostrogothic kingdom — a transition that placed the Italian church in a complex position between Roman aristocratic culture, Gothic rule, and Byzantine imperial claims — shaped the challenging environment within which late 5th-century bishops like Exuperantius operated.",
      "The local community's need for religious leadership, institutional organisation, and a patron saint to anchor the city's Christian identity — the universal demand that drove the proliferation of bishop-saint cults across late antique and early medieval Italy — provided the context for the creation of Exuperantius's cult."
    ],
    "effects": [
      "Exuperantius's identification as the founding bishop of Cingoli established the city's ecclesiastical lineage — providing the diocese with an apostolic origin narrative and a patron saint that anchored its Christian identity through the medieval period.",
      "The cathedral of Cingoli — dedicated to Exuperantius and preserving his memory — served as the institutional and spiritual centre of the city's religious life through the medieval period, maintaining the cult of the founding bishop within the broader Marchigian episcopal network.",
      "Exuperantius's episcopate represents the broader late antique pattern of diocesan foundation in the smaller cities of central Italy — the extension of the ecclesiastical network that was completing the Christianisation of the Italian peninsula and creating the bishop-saint cults that would anchor Italian civic religious identity throughout the medieval period."
    ],
    "relationships": [
      {"sourceSlug": "exuperantius-of-cingoli", "sourceName": "Exuperantius of Cingoli", "verb": "FOUNDS", "targetSlug": "diocese-of-cingoli", "targetName": "Diocese of Cingoli", "context": "Exuperantius was the founding bishop of Cingoli — establishing the diocese in this central Italian hill-town and becoming its patron saint."},
      {"sourceSlug": "late-roman-church", "sourceName": "Late Roman Church (5th Century)", "verb": "PRODUCES", "targetSlug": "exuperantius-of-cingoli", "targetName": "Exuperantius of Cingoli", "context": "Exuperantius was a product of the late Roman church's systematic extension of the episcopal network to smaller Italian towns — a founding bishop in the generation that completed Italy's diocesan organisation."},
      {"sourceSlug": "ostrogothic-italy", "sourceName": "Ostrogothic Italy (476–526 CE)", "verb": "CONTEXTUALISES", "targetSlug": "exuperantius-of-cingoli", "targetName": "Exuperantius of Cingoli", "context": "Exuperantius's episcopate coincided with the transition from Roman to Ostrogothic rule in Italy — the period of political transformation within which the Italian church maintained institutional continuity as the Germanic kingdoms took over Roman political structures."}
    ],
    "places": [
      {"name": "Cingoli (Cingulum), Marche, Italy", "role": "Exuperantius's episcopal city — the Adriatic hill-town in the Marche region where he established the diocese and whose patron saint he became"},
      {"name": "Central-Eastern Italy (Marche/Piceno)", "role": "The regional context of Exuperantius's mission — the Marchigian hill-country that was completing its Christianisation in the late Roman to Ostrogothic transitional period"}
    ],
    "subjects": ["Early Christianity", "Late Roman Church", "Classical Era", "Italy", "Saints", "Early Medieval History", "5th–6th Century CE", "Marche Region"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 2,
      "significanceNarrative": "Exuperantius of Cingoli (died c. 500 CE) was the founding bishop of the Adriatic hill-town of Cingoli in central Italy — one of many late antique bishop-saints whose cults became the foundation of Italian civic Christian identity. His significance is primarily local: as the patron saint of Cingoli whose memory anchored the city's ecclesiastical lineage through the medieval period.",
      "significanceCategory": "local"
    }
  }
},

"poetry": {
  "filepath": "data/appwrite-export/entities/130-Class-130/130poetry.json",
  "slug": "poetry",
  "data": {
    "summary": "Poetry is one of the oldest and most universal forms of human artistic expression — the use of language in structured, rhythmically organised, or aesthetically heightened ways to evoke emotion, communicate experience, encode cultural memory, and explore the limits of meaning. Poetry predates writing: the earliest human cultures used rhythmic, formulaic, and mnemonic oral verse for religious ritual, mythology, history, and wisdom literature — from the Vedic hymns of ancient India (c. 1500 BCE in written form, but far older in oral tradition) to the Homeric epics of ancient Greece (c. 800 BCE written form) to the Psalms of ancient Israel. The impulse to shape language into something beyond prose — to select, compress, intensify, and pattern — appears to be universal across human cultures and epochs.\n\nThe history of world poetry encompasses an extraordinary diversity of forms, traditions, and functions: the epic poetry of Homer's Iliad and Odyssey, Virgil's Aeneid, and the Sanskrit Mahabharata and Ramayana; the lyric poetry of Sappho, Horace, Li Bai, Hafez, and Shakespeare's sonnets; the devotional poetry of the Psalms, Rumi's Masnavi, and St. John of the Cross; the satirical poetry of Juvenal and Dryden; the Romantic poetry of Keats, Shelley, and Byron; the modernist revolution of Eliot's 'The Waste Land' (1922), which fragmented traditional form to reflect the dislocations of modernity; and the contemporary global proliferation of poetic forms that crosses linguistic, cultural, and digital boundaries. Each tradition has developed its own formal conventions — the Chinese regulated verse (lüshi), the Japanese haiku, the Persian ghazal, the Italian sonnet, the English blank verse — that represent millennia of accumulated aesthetic wisdom about how language can be shaped to achieve particular effects.\n\nPoetry's social functions have been as diverse as its forms: as the primary vehicle of cultural memory before writing; as liturgical language in religious ritual; as political propaganda (in Homer's Iliad to Soviet-era odes); as a vehicle of romantic love, grief, and celebration; as a medium of philosophical and scientific instruction (Lucretius's 'De Rerum Natura', Hesiod's 'Works and Days'); and as the most compressed and intense form of aesthetic experience available in language.",
    "causes": [
      "The cognitive and social functions of rhythmic, patterned language — its power to aid memory, to create communal experience, to intensify emotional expression, and to mark the sacred from the ordinary — made poetry one of the earliest and most persistent forms of human linguistic creativity.",
      "The social function of epic poetry as the primary vehicle of cultural memory in pre-literate societies — encoding the history, mythology, values, and social norms of communities in a form that could be transmitted across generations through oral performance — drove the development of sophisticated poetic traditions before writing was invented.",
      "The development of literacy and writing in different civilisations, while creating new possibilities for prose narrative and philosophy, also enabled the fixation and transmission of poetic traditions across time and space — allowing poetic innovation to build on inherited forms and for the dialogue between poets across centuries and cultures that is one of poetry's defining characteristics."
    ],
    "effects": [
      "Poetry's role as the primary vehicle of cultural memory in ancient and medieval societies — the Homeric epics, the Vedas, the Psalms, the Norse Eddas, the Quran's extraordinary Arabic verse — shaped the religious, ethical, and social imaginations of the civilisations that inherited them, encoding the values and narratives that defined cultural identity across millennia.",
      "The formal innovations of poetry — from the invention of blank verse by Surrey and Wyatt in the English Renaissance through Whitman's free verse to the modernist fragmentation of Eliot and Pound — have continuously renewed literary possibility and influenced the development of prose, creating a dialogue between the formal and the free that has driven literary culture forward.",
      "Poetry's persistence as a living art form in the digital age — through slam poetry, spoken word performance, social media verse, and global translation — demonstrates its continued capacity to meet human needs for intense linguistic experience, communal performance, and the compression of complex emotion into memorable form."
    ],
    "relationships": [
      {"sourceSlug": "poetry", "sourceName": "Poetry", "verb": "PRECEDES", "targetSlug": "prose-literature", "targetName": "Prose Literature", "context": "Poetry predates prose as a literary form — the earliest written literatures in every culture are poetic, and prose narrative developed from and in dialogue with the older tradition of verse."},
      {"sourceSlug": "homer", "sourceName": "Homer (c. 800 BCE)", "verb": "SHAPES", "targetSlug": "poetry", "targetName": "Western Poetic Tradition", "context": "Homer's Iliad and Odyssey established the epic tradition that was foundational to Western literary culture — the model of heroic poetry that influenced every subsequent generation of European poets and shaped the concept of what poetry could achieve."},
      {"sourceSlug": "poetry", "sourceName": "Poetry", "verb": "ENCODES", "targetSlug": "cultural-memory", "targetName": "Cultural Memory (oral and written traditions)", "context": "Poetry has served as the primary vehicle of cultural memory across human history — from pre-literate societies' oral epic traditions to the Psalms to modern national anthems, using rhythm and heightened language to fix and transmit the values, stories, and experiences that define communities."}
    ],
    "places": [
      {"name": "Global (all cultures and languages)", "role": "The universal scope of poetry — present in every human culture and language, in oral and written forms, as one of the most fundamental and universal expressions of human linguistic creativity"},
      {"name": "Ancient Greece, India, China, Arabia, Persia (early centres)", "role": "The ancient civilisational centres where the most influential poetic traditions were first developed and codified — the Homeric, Vedic, classical Chinese, Arabic, and Persian traditions that have shaped world literature"}
    ],
    "subjects": ["Literature", "Art Forms", "Classical Era", "Aesthetics", "Cultural History", "Oral Tradition", "Language", "World Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Poetry is one of the oldest, most universal, and most consequential forms of human artistic expression — predating writing, encoding cultural memory, shaping religious and national identity across millennia, and serving as the primary vehicle for the most intense forms of linguistic experience. From the Vedas to Homer to Rumi to Shakespeare to Eliot, poetry has been at the centre of every great literary civilisation and remains a living art form in the digital age.",
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
