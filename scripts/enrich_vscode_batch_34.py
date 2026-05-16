#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 34 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: gospel-of-mary, being-digital-negroponte, cranmers-recantations-1556,
          albanian-songs-of-the-frontier-warriors, amir-arsalan,
          a-song-of-ice-and-fire, delphi-method, life-cycle-assessment
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-34-may2026"

ENRICHMENTS = {

"gospel-of-mary": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780gospel-of-mary.json",
  "slug": "gospel-of-mary",
  "data": {
    "summary": "The Gospel of Mary is a Gnostic text attributed to Mary Magdalene, discovered in fragmentary Coptic and Greek manuscripts — most importantly the Berlin Gnostic Codex (Papyrus Berolinensis 8502), purchased in Cairo in 1896 and published in full in 1955 — and dated by scholars to the 2nd century CE. Only portions survive: the extant Coptic text (chapters 7–10) contains a dialogue between Mary Magdalene and the other disciples, in which Mary reports a vision of the Risen Jesus and his secret teaching about the ascent of the soul through hostile spiritual powers. The second half of the text is a dispute in which Peter and Andrew question whether Jesus could have communicated a teaching privately to a woman that he did not share with his male disciples — a challenge that is defended by Levi (Matthew), who affirms that Jesus 'knew her very well' and 'loved her more than us.'\n\nThe Gospel of Mary is the only surviving early Christian text explicitly attributed to a female disciple, and its dispute about Mary Magdalene's authority is the most direct ancient evidence for debates within early Christianity about women's leadership and spiritual authority. The text's presentation of Mary as the recipient of a private revelation from Jesus — and as having to defend this against male disciples' scepticism — has made it a central text in feminist theology and in the scholarly reassessment of women's roles in early Christianity. Elaine Pagels's scholarly work and Karen King's The Gospel of Mary of Magdala (2003) brought the text to wide scholarly and popular attention.\n\nThe Gospel of Mary's theological content — the description of the soul's ascent through seven hostile spiritual powers (Darkness, Desire, Ignorance, Death-wish, Fleshly Kingdom, Foolish Fleshly Wisdom, and Wrathful Wisdom) — is characteristic of Gnostic cosmology, presenting the spiritual journey as an ascent through cosmic obstacles toward the divine realm. The text's fragmentary state (the first six and part of the middle chapters are lost) makes it tantalising rather than fully interpretable, but its existence demonstrates the variety of early Christian traditions about Mary Magdalene's special relationship with Jesus.",
    "causes": [
      "The Gnostic Christian tradition's emphasis on spiritual knowledge (gnosis) received through private revelation — and its openness to female spiritual authority, reflecting the broader Gnostic view that the divine spark transcends gendered distinctions — created the context in which a Gospel attributed to Mary Magdalene could be composed and circulated, presenting her as a superior spiritual authority to the male apostles.",
      "The historical role of Mary Magdalene in early Christianity — described in all four canonical Gospels as the first witness to the Resurrection (John 20:1–18), a prominent female patron of Jesus's ministry, and a figure of particular significance in the Syrian and Egyptian Christian traditions — provided the basis for a literary and spiritual tradition that expanded her role in extra-canonical texts.",
      "The discovery and publication of the Berlin Gnostic Codex (1896, published 1955) and its subsequent scholarly interpretation — particularly by feminist theologians like Elaine Pagels and Karen King in the 1970s–2000s — created the modern academic and popular interest in the Gospel of Mary as a primary text for the study of gender, authority, and diversity in early Christianity."
    ],
    "effects": [
      "The Gospel of Mary became the central text in feminist theological arguments for women's spiritual authority in early Christianity — its presentation of Mary Magdalene as the recipient of special revelation and as having to defend her authority against male apostles' scepticism is the most direct ancient evidence for debates about women's leadership in the early Christian movement.",
      "The popular and scholarly attention given to the Gospel of Mary — through Karen King's The Gospel of Mary of Magdala (2003), Elaine Pagels's work, and the popular impact of The Da Vinci Code (2003, which drew on Gnostic traditions about Mary Magdalene's relationship with Jesus) — significantly raised public awareness of the diversity of early Christianity and the role of women in the movement.",
      "The Gospel of Mary, together with the Gospel of Thomas and the Gospel of Judas, forms part of the modern scholarly and popular reassessment of early Christian diversity — demonstrating that the canonical New Testament's marginalisation of women's spiritual authority represented the victory of one tradition over several competing alternatives."
    ],
    "relationships": [
      {"sourceSlug": "gospel-of-mary", "sourceName": "Gospel of Mary (c. 2nd century CE)", "verb": "ATTRIBUTES_TO", "targetSlug": "mary-magdalene", "targetName": "Mary Magdalene (disciple, first resurrection witness)", "context": "The Gospel of Mary is the only early Christian text explicitly attributed to a female disciple — presenting Mary Magdalene as the recipient of special revelation from Jesus and as having to defend her authority against the male apostles' scepticism."},
      {"sourceSlug": "gospel-of-mary", "sourceName": "Gospel of Mary (Berlin Gnostic Codex)", "verb": "PART_OF", "targetSlug": "gnostic-christianity", "targetName": "Gnostic Christian literary tradition (Berlin Codex, Nag Hammadi)", "context": "The Gospel of Mary is part of the Gnostic Christian literary tradition — discovered in the Berlin Gnostic Codex (1896) and published in full in 1955 — reflecting Gnostic theology's openness to female spiritual authority."},
      {"sourceSlug": "gospel-of-mary", "sourceName": "Gospel of Mary (feminist theology)", "verb": "INFLUENCES", "targetSlug": "feminist-theology", "targetName": "Feminist theology and women's leadership in early Christianity", "context": "The Gospel of Mary became a central text in feminist theological arguments for women's spiritual authority — its ancient dispute between Mary and Peter about the validity of female revelation is the most direct early Christian evidence for debates about women's leadership."}
    ],
    "places": [
      {"name": "Egypt (Berlin Gnostic Codex, purchased Cairo 1896)", "role": "The Berlin Gnostic Codex was purchased in Cairo in 1896 — Egypt has preserved the most significant Gnostic texts in their Coptic translations, including the Gospel of Mary, the Gospel of Thomas, and the Nag Hammadi library"},
      {"name": "Berlin (Papyrus Berolinensis 8502, published 1955)", "role": "The Berlin Codex has been housed in the Egyptian Museum in Berlin since its purchase in 1896 — Carl Schmidt's planned publication was delayed by World War II and eventually published in 1955"}
    ],
    "subjects": ["Gnostic Christianity", "Classical Era", "Mary Magdalene", "Early Christianity", "Feminist Theology", "New Testament Apocrypha", "Women in Christianity", "Biblical Scholarship"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Gospel of Mary (c. 2nd century CE, published 1955) is the only early Christian text attributed to a female disciple — its presentation of Mary Magdalene as a recipient of special revelation and its dispute about women's spiritual authority make it the most direct ancient evidence for debates about women's leadership in early Christianity. A central text in feminist theology and the popular reassessment of early Christian diversity.",
      "significanceCategory": "significant"
    }
  }
},

"being-digital-negroponte": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781being-digital-negroponte.json",
  "slug": "being-digital-negroponte",
  "data": {
    "summary": "Being Digital is the work of media technology forecasting by Nicholas Negroponte (born 1943), founder of the MIT Media Lab, published in January 1995 by Alfred A. Knopf — based on his 'Bits' column in Wired magazine — one of the most widely read and prescient accounts of the coming digital revolution and its cultural, social, and economic consequences. The book's central distinction — between 'atoms' (physical matter, the basis of the industrial economy of manufactured goods) and 'bits' (digital information, the basis of the emerging information economy) — provided the conceptual framework for understanding the digital transformation of media, entertainment, commerce, and communication that was beginning in 1995 with the early World Wide Web. Being Digital was translated into 40 languages and sold over 1 million copies in its first year.\n\nNegroponte's predictions in Being Digital covered the transformation of newspapers, television, telephony, and retail commerce by digital distribution — he predicted personalised news delivered to individual preferences ('Daily Me'), interactive television, the convergence of computing and communication, the decline of physical media (CDs, videotapes), e-commerce, and the decentralisation of cultural production enabled by digital networks. Many of his predictions proved accurate within a decade: the MP3 revolution, streaming video, Amazon, Google, social media, and the smartphone all embodied forces he had identified. Some predictions (the 'Daily Me' personalised newspaper) took longer than expected but arrived in the form of algorithmic news feeds on Facebook and Twitter.\n\nBeing Digital was influential not only as a technology forecast but as a cultural manifesto — its optimistic vision of digital technology as a force for individual empowerment, decentralisation, and cultural democratisation was the dominant technology ideology of the 1990s, and Negroponte's Wired column and public advocacy helped shape the 'California ideology' of Silicon Valley techno-optimism that drove the dot-com boom. The MIT Media Lab — which Negroponte co-founded in 1985 — became the institutional embodiment of the approach to technology as creative cultural transformation that Being Digital articulated.",
    "causes": [
      "The emergence of the World Wide Web (Tim Berners-Lee's web browser Mosaic was released in 1993) and the first wave of commercial internet services — CompuServe, AOL, the early e-commerce experiments — created the empirical basis for Negroponte's predictions: he was writing at the inflection point when digital networks were becoming commercially and culturally significant for the first time.",
      "Negroponte's founding of the MIT Media Lab (1985) — a research institution explicitly dedicated to the intersection of computing, communication, and culture — gave him the institutional vantage point from which to synthesise research across computing, media, design, and education, and the academic credibility from which to make sweeping claims about the digital future.",
      "The Wired magazine environment of the early 1990s — the journal that articulated the cultural politics of the early digital revolution, combining technology forecasting with aesthetic avant-gardism and libertarian political theory — gave Negroponte his initial audience and shaped the 'California ideology' frame in which Being Digital's predictions were made and received."
    ],
    "effects": [
      "Being Digital's atoms-vs-bits framework became the canonical conceptual vocabulary for discussing the digital transformation of the economy — the distinction between physical goods (atoms) and information goods (bits) structured discussions of intellectual property, e-commerce, media disruption, and the economics of digital goods throughout the 1990s and 2000s.",
      "Negroponte's predictions about the convergence of computing and communication — the transformation of telephone, television, and publishing into digital services — proved broadly accurate and helped shape the strategic thinking of media companies, technology investors, and policymakers in the 1990s, contributing to the wave of digital media investment and transformation.",
      "Being Digital's optimistic vision of digital technology as a force for individual empowerment, cultural democratisation, and decentralisation was the dominant technology ideology of the 1990s dot-com era — and the subsequent disillusionment with this vision (privacy surveillance, algorithmic polarisation, platform monopolisation) has made Being Digital a historical document of the techno-optimist worldview before its complications became apparent."
    ],
    "relationships": [
      {"sourceSlug": "nicholas-negroponte", "sourceName": "Nicholas Negroponte (born 1943)", "verb": "AUTHORS", "targetSlug": "being-digital-negroponte", "targetName": "Being Digital (1995)", "context": "Negroponte wrote Being Digital from his Wired column, synthesising MIT Media Lab research to forecast the digital transformation of media, commerce, and communication — one of the most widely read technology forecasting books of the 1990s."},
      {"sourceSlug": "being-digital-negroponte", "sourceName": "Being Digital (atoms vs bits framework)", "verb": "INFLUENCES", "targetSlug": "digital-economy-theory", "targetName": "Digital economy theory and technology forecasting", "context": "The atoms-vs-bits distinction became the canonical conceptual vocabulary for discussing digital transformation — structuring discussions of e-commerce, intellectual property, media disruption, and the economics of digital goods throughout the 1990s and 2000s."},
      {"sourceSlug": "being-digital-negroponte", "sourceName": "Being Digital (1995, MIT Media Lab)", "verb": "REFLECTS", "targetSlug": "california-ideology", "targetName": "'California ideology' of Silicon Valley techno-optimism", "context": "Being Digital was a primary articulation of the Silicon Valley techno-optimist ideology — the belief that digital technology would inherently be a force for individual empowerment, decentralisation, and cultural democratisation — which drove the dot-com boom and shaped 1990s technology culture."}
    ],
    "places": [
      {"name": "MIT Media Lab, Cambridge, Massachusetts (founding context, 1985–1995)", "role": "The MIT Media Lab — co-founded by Negroponte in 1985 — was the institutional basis for Being Digital's synthesis of research across computing, media, design, and education"},
      {"name": "Global (40 languages, 1 million+ copies sold in first year)", "role": "Being Digital was translated into 40 languages and sold over a million copies in its first year — its global reach made it the canonical popular account of the coming digital transformation for international audiences"}
    ],
    "subjects": ["Technology", "Modern Era", "Nicholas Negroponte", "Digital Revolution", "Internet", "Media Theory", "MIT Media Lab", "Wired Magazine"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Being Digital (Negroponte, 1995) is one of the most widely read technology forecasting books of the 1990s — its atoms-vs-bits framework became canonical for discussing digital transformation, and many of its predictions (MP3, streaming, e-commerce, convergence) proved accurate within a decade. It is an important historical document of the techno-optimist 'California ideology' that drove the dot-com era, and a foundational text for the study of digital media theory.",
      "significanceCategory": "significant"
    }
  }
},

"cranmers-recantations-1556": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781cranmers-recantations-1556.json",
  "slug": "cranmers-recantations-1556",
  "data": {
    "summary": "Thomas Cranmer's Recantations and Final Speech (1556) refer to the series of documents in which Archbishop Thomas Cranmer (1489–1556), the architect of the English Reformation and principal author of the Book of Common Prayer, signed six recantations of Protestant doctrine under pressure of interrogation and imminent execution during Queen Mary I's Catholic restoration — before dramatically repudiating all his recantations at the stake at Oxford on 21 March 1556, dying as a Protestant martyr. Cranmer's end is among the most theatrically and morally dramatic moments in English religious history: having recanted to avoid the burning he feared, he recanted his recantations in his final speech, declaring that since his hand had 'signed to the contrary of what I believed in my heart,' he would thrust his right hand first into the flames, holding it steadfast in the fire until it burned to ash.\n\nCranmer's recantations and repudiation are documents of profound psychological and theological significance. The six signed recantations — in which Cranmer submitted to papal authority, acknowledged the Real Presence in the Eucharist, and condemned the Protestant heresies he had championed — were the product of months of imprisonment, interrogation, and the gradual erosion of resistance by skilled Catholic interrogators. Cranmer signed them in the expectation that his submission would win him reprieve; when Mary I refused mercy despite his recantations and ordered him burned anyway, Cranmer recovered his Protestant faith at the moment of his death and repudiated everything he had signed.\n\nCranmer's martyrdom — documented immediately in contemporary accounts and later canonised in John Foxe's Acts and Monuments (Foxe's Book of Martyrs, 1563) — became one of the most powerful narratives of Protestant martyrdom in English history, and his gesture of thrusting his right hand into the flames first ('unworthy hand!') became the iconic image of Protestant witness under persecution. His recantations demonstrate both the psychological vulnerability of even the most committed reformers under coercion and the power of the martyr narrative in early modern confessional culture.",
    "causes": [
      "Queen Mary I's Catholic restoration (1553–1558) — the reversal of the Protestant Reformation of Edward VI's reign, the restoration of papal authority in England, and the heresy trials that burned approximately 284 Protestants (the Marian martyrs) — created the context of Cranmer's imprisonment, interrogation, recantation, and martyrdom.",
      "Cranmer's specific theological vulnerability — his long career as Henry VIII's Archbishop had involved compromises on royal supremacy, the annulment of the King's marriages, and the gradual articulation of Protestant doctrine, making him the most symbolically important target of Mary's Catholic restoration and the subject of particularly determined efforts at recantation by skilled Catholic interrogators.",
      "The practice of obtaining and publishing recantations as propaganda — the Catholic strategy of securing signed confessions from Protestant leaders that could be published and distributed to demonstrate the falseness of heresy — gave Cranmer's recantations their significance as documents: his signed submissions were intended to undermine the Protestant cause and demonstrate the weakness of Reformed doctrine."
    ],
    "effects": [
      "Cranmer's dramatic repudiation of his recantations at the stake — and his deliberate burning of his right hand first — became the most celebrated Protestant martyrdom narrative in English history, immortalised in John Foxe's Acts and Monuments (1563, the 'Book of Martyrs') and shaping the Protestant self-understanding of faith under persecution for generations.",
      "John Foxe's Acts and Monuments — the massive Protestant martyrology first published in 1563, of which the Cranmer narrative is the most dramatic — became the most widely distributed English Protestant text after the Bible, establishing the culture of Protestant martyrdom that shaped English Protestant identity from the Elizabethan period through the 17th century.",
      "Cranmer's theological legacy — the Book of Common Prayer (1549, revised 1552) and the Forty-Two Articles (1553, basis of the Thirty-Nine Articles, 1563) — survived his martyrdom to become the foundational documents of Anglicanism, and his role as the architect of the English Reformation was not diminished by the recantations: the Protestant tradition absorbed his weakness as a human failure redeemed by his final witness."
    ],
    "relationships": [
      {"sourceSlug": "thomas-cranmer", "sourceName": "Thomas Cranmer (1489–1556)", "verb": "REPUDIATES", "targetSlug": "cranmers-recantations-1556", "targetName": "Cranmer's Recantations and Final Speech (1556)", "context": "Cranmer signed six recantations under interrogation and then repudiated all of them at the stake — deliberately burning his right hand first as penance for having signed against his conscience — one of the most dramatic Protestant martyrdom narratives in English history."},
      {"sourceSlug": "cranmers-recantations-1556", "sourceName": "Cranmer's martyrdom (1556)", "verb": "DOCUMENTED_IN", "targetSlug": "acts-and-monuments-foxe", "targetName": "John Foxe's Acts and Monuments ('Book of Martyrs', 1563)", "context": "Foxe's Acts and Monuments — the massive Protestant martyrology first published in 1563 — immortalised Cranmer's death as the supreme example of Protestant witness under Catholic persecution."},
      {"sourceSlug": "cranmers-recantations-1556", "sourceName": "Cranmer's recantations and repudiation", "verb": "SHAPED_BY", "targetSlug": "marian-persecution", "targetName": "Marian persecution (Queen Mary I's Catholic restoration, 1553–1558)", "context": "The Marian persecution — the burning of approximately 284 Protestant martyrs under Mary I — created the context of Cranmer's imprisonment, recantation, and martyrdom, and produced the Protestant martyr tradition that defined English Protestant identity for generations."}
    ],
    "places": [
      {"name": "Oxford, England (21 March 1556, stake at Broad Street)", "role": "Cranmer was burned at the stake in Oxford — at the location now marked by the Martyrs' Memorial — where he famously thrust his right hand into the flames first, fulfilling his pledge that the hand that had signed his recantations would pay the first penalty"},
      {"name": "Tower of London (1553–1556, imprisonment and interrogation)", "role": "Cranmer was imprisoned in the Tower of London from 1553 — where the months of Catholic interrogation gradually produced his six signed recantations — before his final examination and execution at Oxford"}
    ],
    "subjects": ["English Reformation", "Early Modern Era", "Thomas Cranmer", "Protestant Martyrdom", "Mary I", "English History", "Anglicanism", "Religious Persecution"],
    "frameworks": ["CAUSE_AND_EFFECT", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Cranmer's recantations and final speech (1556) are the most dramatic Protestant martyrdom narrative in English history — his repudiation of six signed recantations at the stake, deliberately thrusting his right hand into the flames first, was immortalised in Foxe's Book of Martyrs and shaped English Protestant identity for generations. As the architect of the Book of Common Prayer and the Thirty-Nine Articles, Cranmer's martyrdom represents the full arc of the English Reformation.",
      "significanceCategory": "highly-significant"
    }
  }
},

"albanian-songs-of-the-frontier-warriors": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782albanian-songs-of-the-frontier-warriors.json",
  "slug": "albanian-songs-of-the-frontier-warriors",
  "data": {
    "summary": "The Songs of the Frontier Warriors (Albanian: Këngë kreshnikësh, 'Songs of the Champions/Heroes') — also known as the Albanian Epic Cycle or the Cycle of the Frontier Warriors (Cikli i kreshnikëve) — is the tradition of heroic oral epic poetry of the Albanian-speaking peoples of the Balkans, representing one of the major epic traditions in European oral literature alongside the Greek, South Slavic, and Norse traditions. The cycle centres on the legendary heroes of the Albanian highlands — particularly Mujo (also known as Aga Mujo) and his brother Halil, who guard the frontier between the Albanian/Christian and Ottoman worlds — and covers themes of heroic combat, love and honour, supernatural challenge, and the defence of the community against external threats. The Songs were performed by guslars (bards who accompanied themselves on the one-string gusle fiddle) in the mountain communities of northern Albania and Kosovo.\n\nThe Albanian epic cycle became the subject of international scholarly attention through the work of Milman Parry and Albert Lord — the Harvard scholars whose fieldwork in Yugoslavia (1933–1935) on oral-formulaic composition established the theory that Homer's Iliad and Odyssey were products of an oral tradition, not written compositions. Parry and Lord's comparative study of living South Slavic and Albanian oral epic traditions provided the empirical foundation for the Parry-Lord oral-formulaic theory (Lord's The Singer of Tales, 1960), which transformed the scholarly understanding of Homeric poetry and the nature of oral literature worldwide. The Albanian epics — alongside the South Slavic guslars' performances — thus played an indirect but significant role in the most important development in Homeric scholarship of the 20th century.\n\nThe Songs of the Frontier Warriors reflect the specific historical experience of the Albanian highlands during the long Ottoman period — the semi-autonomous tribal communities of the mountain regions (the Malësia, the highlands of northern Albania and Kosovo) that maintained customary law (the Kanun of Lekë Dukagjini), blood-feud customs, and oral heroic traditions largely outside Ottoman administrative control. The cycle's heroes embody the values of this highland culture: hospitality (besa), honour, martial courage, and the defence of family and community.",
    "causes": [
      "The Albanian highland tribal culture — the semi-autonomous communities of the Malësia (northern Albanian highlands), governed by customary law (the Kanun of Lekë Dukagjini) and maintaining their independence from Ottoman administrative control through the Ottoman period — provided the social context for the performance and transmission of heroic oral epic, a genre suited to communities that valorise martial prowess, honour, and communal defence.",
      "The historical experience of Ottoman-Christian frontier conflicts in the western Balkans — the long period of Ottoman expansion and consolidation in the Balkans (15th–18th centuries), during which Albanian-speaking communities occupied a contested frontier zone — provided the historical substrate for the epic cycle's themes of frontier heroism, Christian/Ottoman tension, and the defence of the community against foreign power.",
      "The oral-formulaic tradition of Balkan epic performance — the culture of the bard (guslar) accompanying himself on the gusle in communal performance, composing each performance anew from traditional formulae and story patterns — sustained the Albanian epic cycle as a living oral tradition that Milman Parry and Albert Lord were able to study in the 20th century."
    ],
    "effects": [
      "The Albanian Songs of the Frontier Warriors, studied by Parry and Lord in the 1930s alongside the South Slavic guslars' tradition, provided the comparative empirical evidence for the Parry-Lord oral-formulaic theory — the most important methodological contribution to Homeric scholarship in the 20th century, which transformed the understanding of how Homer's epics were composed.",
      "The scholarly recovery and publication of the Albanian epic cycle — by Albanian folklorists and international scholars from the 19th century onwards — contributed to the formation of Albanian national literary identity, providing an indigenous heroic tradition comparable to the South Slavic and Greek epics at a crucial period of Albanian national awakening.",
      "The epic cycle's preservation of the values, social structures, and historical memory of the Albanian highland communities — their besa (honour pledge), hospitality customs, blood-feud traditions, and relationship with the Ottoman world — makes it an invaluable ethnographic source for the social and cultural history of the Albanian-speaking communities of the western Balkans."
    ],
    "relationships": [
      {"sourceSlug": "albanian-songs-of-the-frontier-warriors", "sourceName": "Albanian Songs of the Frontier Warriors", "verb": "STUDIED_BY", "targetSlug": "parry-lord-oral-formulaic-theory", "targetName": "Parry-Lord oral-formulaic theory (The Singer of Tales, 1960)", "context": "Milman Parry and Albert Lord's fieldwork on living oral epic traditions — including the Albanian frontier warrior songs — provided the comparative empirical evidence for their oral-formulaic theory, which transformed the scholarly understanding of Homeric poetry."},
      {"sourceSlug": "albanian-songs-of-the-frontier-warriors", "sourceName": "Albanian epic cycle (Mujo and Halil)", "verb": "EMBODIES", "targetSlug": "albanian-highland-culture", "targetName": "Albanian highland culture (besa, Kanun, martial tradition)", "context": "The Songs of the Frontier Warriors preserve the values and social structures of the Albanian highland communities — their honour code, hospitality customs, blood-feud traditions, and martial culture — as an invaluable ethnographic source."},
      {"sourceSlug": "albanian-songs-of-the-frontier-warriors", "sourceName": "Albanian Songs (frontier epic tradition)", "verb": "PARALLELS", "targetSlug": "south-slavic-epic-tradition", "targetName": "South Slavic epic tradition (guslars' oral epic)", "context": "The Albanian and South Slavic epic traditions share the gusle performance tradition, oral-formulaic composition techniques, and frontier heroism themes — their parallel study by Parry and Lord was the empirical foundation of oral-formulaic theory."}
    ],
    "places": [
      {"name": "Northern Albania and Kosovo (Malësia, highland communities, performance context)", "role": "The Albanian highland communities of northern Albania and Kosovo — the Malësia — were the primary context for the performance and transmission of the frontier warrior songs, reflecting the semi-autonomous tribal culture of these mountain regions"},
      {"name": "Yugoslavia/Balkans (1930s Parry-Lord fieldwork)", "role": "Parry and Lord's fieldwork in Yugoslavia in 1933–1935 — recording living oral epic performances by guslars — provided the empirical evidence for oral-formulaic theory, and the Albanian tradition was studied alongside the South Slavic tradition as part of this research"}
    ],
    "subjects": ["Albanian Literature", "Medieval Era", "Oral Epic", "Albanian History", "Balkans", "Oral-Formulaic Theory", "Folk Poetry", "Heroic Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Albanian Songs of the Frontier Warriors is one of Europe's major oral epic traditions — studied by Parry and Lord alongside the South Slavic guslars, it contributed empirical evidence for the oral-formulaic theory that transformed Homeric scholarship. The cycle embodies the values and history of the Albanian highland communities during the Ottoman period and is a monument of Albanian national literary identity. Significant for comparative epic studies and Balkan cultural history.",
      "significanceCategory": "significant"
    }
  }
},

"amir-arsalan": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782amir-arsalan.json",
  "slug": "amir-arsalan",
  "data": {
    "summary": "Amir Arsalan (Persian: امیر ارسلان نامدار, Amīr Arslān-e Nāmdār, 'Prince Arsalan the Renowned') is a romantic epic novel of Persian oral literature, composed in the oral storytelling tradition by Muhammad Ali Naqib al-Mamalik (also known as Mohammad Ali Khan Naqib ol-Mamalik) for Naser al-Din Shah Qajar (r. 1848–1896) at the Persian royal court in the 1880s, and subsequently transcribed and published. It is one of the most beloved works in Persian popular literature and remains widely read in Iran, Afghanistan, and the Persian-speaking diaspora. The narrative follows Prince Amir Arsalan, a Persian hero who embarks on a series of supernatural adventures — encountering jinns, divs (demons), fairy queens, sorcerers, and enchanted cities — in his quest to rescue and marry the beautiful Princess Farrokh-Laqā, the daughter of the Frank (European) King. The story is a fantastical adventure romance combining the themes of heroic quest, divine aid, magic, and love that characterise the masnavi (Persian narrative verse) tradition, here presented in prose.\n\nAmir Arsalan belongs to the tradition of dastan (Persian oral narrative) — the oral storytelling genre of the Persian-speaking world, performed by professional storytellers (naqqāls) in coffeehouses and court settings, that produced narratives of heroic adventure, supernatural wonder, and romantic love. It reflects the Qajar literary culture of the 19th century, which was simultaneously deeply rooted in the classical Persian literary tradition (Ferdowsi's Shahnameh, the romances of Nizami) and open to new narrative forms combining oral performance with written transmission. The work's fantastical geography — its enchanted cities, magical weapons, divine interventions — draws on the conventions of Persian epic and romance while serving the entertainment purposes of Qajar court storytelling.\n\nAmir Arsalan is one of the first major works of Persian prose fiction — its transformation of oral dastan narrative into a written text contributed to the development of Persian prose fiction as a genre in the late 19th and early 20th centuries, alongside the constitutional revolution's stimulation of Persian prose writing. It has been adapted for film and television in Iran multiple times and remains a touchstone of Persian popular literary culture.",
    "causes": [
      "Naser al-Din Shah's cultural patronage — the Qajar monarch's enthusiasm for storytelling and his commission of Naqib al-Mamalik as court storyteller (naqqāl) — created the immediate context for the composition of Amir Arsalan: it was composed as an ongoing oral narrative for royal entertainment, episode by episode, in the tradition of the Thousand and One Nights.",
      "The Persian dastan tradition — the oral narrative genre of the coffeehouses and royal courts, combining heroic adventure, supernatural wonder, romantic love, and moral instruction — provided the literary conventions and the narrative structure from which Amir Arsalan was constructed: its protagonist, quest structure, supernatural helpers, and enchanted obstacles all draw on centuries of dastan narrative convention.",
      "The Qajar literary environment of the late 19th century — the intersection of traditional Persian literary culture with new possibilities of print publication, the Constitutional Revolution's stimulation of vernacular Persian prose, and the growing literacy of the Iranian urban population — created the conditions for the transcription and publication of Amir Arsalan as a popular text accessible beyond the royal court."
    ],
    "effects": [
      "Amir Arsalan contributed to the development of Persian prose fiction as a genre — its transformation of oral dastan narrative into a popular written text helped establish the precedent for Persian prose fiction in the late 19th and early 20th centuries, alongside the Constitutional Revolution's stimulation of vernacular prose writing.",
      "The text's enduring popularity — continuously reprinted in Iran and Afghanistan since its first publication, adapted for film and television, and widely available in the Persian-speaking diaspora — demonstrates its role as a touchstone of Persian popular literary culture, combining classical literary prestige with popular accessibility.",
      "Amir Arsalan's presentation of a Persian hero who traverses a fantastical world that includes European (Frank) elements — engaging with the encounter between Persia and the West — reflects the Qajar cultural moment's negotiation between Persian tradition and the European world that was increasingly impinging on Iran, giving the text a culturally significant subtext beyond its adventure narrative."
    ],
    "relationships": [
      {"sourceSlug": "naqib-al-mamalik", "sourceName": "Mohammad Ali Naqib al-Mamalik (fl. 1880s)", "verb": "AUTHORS", "targetSlug": "amir-arsalan", "targetName": "Amir Arsalan (composed 1880s, transcribed for publication)", "context": "Naqib al-Mamalik composed Amir Arsalan as an oral narrative for Naser al-Din Shah Qajar — the successive episodes performed for royal entertainment and later transcribed and published as one of the most popular works in Persian literature."},
      {"sourceSlug": "amir-arsalan", "sourceName": "Amir Arsalan (Persian dastan)", "verb": "PART_OF", "targetSlug": "persian-oral-narrative-tradition", "targetName": "Persian dastan tradition (oral narrative, coffeehouses, royal courts)", "context": "Amir Arsalan belongs to the Persian dastan tradition — the oral narrative genre of professional storytellers performed in coffeehouses and court settings — and contributed to the development of Persian prose fiction by transforming oral narrative into a popular written text."},
      {"sourceSlug": "amir-arsalan", "sourceName": "Amir Arsalan (Qajar, 1880s)", "verb": "FOLLOWS", "targetSlug": "shahnameh", "targetName": "Ferdowsi's Shahnameh (Persian national epic)", "context": "Amir Arsalan draws on the conventions of Persian epic and romance established by Ferdowsi's Shahnameh and Nizami's romances, continuing the Persian tradition of heroic narrative while adapting it to the Qajar oral storytelling context."}
    ],
    "places": [
      {"name": "Tehran, Qajar Iran (1880s, royal court composition context)", "role": "Amir Arsalan was composed at the Qajar royal court in Tehran — as oral entertainment for Naser al-Din Shah — reflecting the cultural life of the Qajar court at the height of the 19th-century Persian encounter with the modern world"},
      {"name": "Iran and Persian-speaking world (continuous popular reception)", "role": "Amir Arsalan has been continuously popular across the Persian-speaking world — Iran, Afghanistan, and the Persian diaspora — and remains one of the most beloved works in Persian popular literary culture"}
    ],
    "subjects": ["Persian Literature", "Modern Era", "Oral Narrative", "Qajar Iran", "Persian Epic", "Romance", "Iranian Culture", "Dastan"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Amir Arsalan (1880s) is one of the most beloved works in Persian popular literature — composed as oral entertainment at the Qajar court and transcribed as one of the first major works of Persian prose fiction, it contributed to the development of the modern Persian literary novel. Its continuous popularity across the Persian-speaking world and its multiple film/TV adaptations demonstrate its status as a touchstone of Iranian popular cultural identity.",
      "significanceCategory": "significant"
    }
  }
},

"a-song-of-ice-and-fire": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783a-song-of-ice-and-fire.json",
  "slug": "a-song-of-ice-and-fire",
  "data": {
    "summary": "A Song of Ice and Fire is the ongoing series of epic fantasy novels by George R. R. Martin (born 1948), beginning with A Game of Thrones (1996) — one of the best-selling and most culturally influential fantasy series of the late 20th and early 21st centuries, and the basis for the HBO television series Game of Thrones (2011–2019), which became the most watched television drama in history with a peak global audience of approximately 44 million viewers for the final season. The series is set in the fictional continents of Westeros and Essos and follows the political struggles of noble dynasties (the Starks, Lannisters, Targaryens, Baratheons, and others) for control of the Iron Throne of the Seven Kingdoms — against the background of a supernatural threat from the White Walkers (the Others) beyond the Wall in the frozen North, and the arc of Daenerys Targaryen in Essos with her three dragons. Five volumes have been published (through A Dance with Dragons, 2011); two further volumes (The Winds of Winter and A Dream of Spring) remain unfinished.\n\nMartin's series is characterised by its rejection of the high-fantasy conventions of good-versus-evil moral clarity — its morally ambiguous characters (the 'villain' Jaime Lannister is a complex tragic figure; the ostensible 'hero' Ned Stark is killed in the first volume), its willingness to kill off major sympathetic characters (the Red Wedding; the assassination of Jon Snow), and its embedded historical realism (drawing on the Wars of the Roses, the Hundred Years' War, and other medieval conflicts) gave A Song of Ice and Fire a gritty, morally complex quality that distinguished it from Tolkienian high fantasy and attracted readers who had previously avoided the genre. Its political intrigue — the Machiavellian dynamics of the noble houses, the corruption of power, and the question of who deserves to rule — is the most elaborate in the fantasy genre.\n\nThe HBO television adaptation (2011–2019) transformed A Song of Ice and Fire from a beloved but niche fantasy series into one of the most widely known cultural phenomena of the early 21st century — the show's unprecedented production values, its faithfulness to Martin's moral complexity in the early seasons, and its global distribution on HBO and subsequently streaming services made 'Game of Thrones' a shared global cultural experience in a way that few television series have achieved.",
    "causes": [
      "Martin's background in television writing (Beauty and the Beast, The Twilight Zone revival) and his frustration with the visual medium's budget constraints — which limited the epic scale he wanted to achieve — gave him the motivation to return to prose fiction and write an epic fantasy with the cinematic scope that he felt television could not then achieve: the result was A Game of Thrones (1996), the first volume of the series.",
      "The state of fantasy fiction in the early 1990s — dominated by the legacy of Tolkien's high fantasy (clear moral polarities, chosen heroes, good versus evil) and by Robert Jordan's Wheel of Time series (1990) — provided the context against which Martin's morally ambiguous, historically grounded, politically complex approach to fantasy represented a deliberate genre innovation.",
      "The Wars of the Roses — the 15th-century English dynastic conflict between the houses of Lancaster and York for control of the English throne — provided the primary historical model for A Song of Ice and Fire's political conflicts: the Starks mirror the Yorkists, the Lannisters mirror the Lancastrians, and the series' dynastic complexity and its willingness to destroy sympathetic characters reflects the historical Wars of the Roses' moral chaos."
    ],
    "effects": [
      "The HBO television adaptation Game of Thrones (2011–2019) transformed the cultural status of fantasy fiction — demonstrating that epic fantasy, previously considered a niche genre, could attract the largest television audiences in history and achieve the mainstream cultural prestige previously reserved for prestige drama — triggering a wave of major fantasy television and film productions.",
      "A Song of Ice and Fire's rejection of high-fantasy moral conventions — its morally complex characters, its willingness to kill sympathetic protagonists, and its historically grounded realism — influenced the subsequent direction of fantasy fiction, with a generation of fantasy writers following Martin's model of 'grimdark' or morally complex fantasy.",
      "The series' global cultural impact through Game of Thrones — the Red Wedding, the Iron Throne, 'Winter is coming', the Night King, the Mother of Dragons — produced a shared global vocabulary of cultural reference comparable to the Star Wars universe and established fantasy as the defining television genre of the 2010s."
    ],
    "relationships": [
      {"sourceSlug": "george-r-r-martin", "sourceName": "George R. R. Martin (born 1948)", "verb": "AUTHORS", "targetSlug": "a-song-of-ice-and-fire", "targetName": "A Song of Ice and Fire (series, 1996–present)", "context": "Martin began A Song of Ice and Fire with A Game of Thrones (1996) — drawing on the Wars of the Roses and medieval history for his morally complex fantasy world — and has published five of the planned seven volumes."},
      {"sourceSlug": "a-song-of-ice-and-fire", "sourceName": "A Song of Ice and Fire (basis for HBO Game of Thrones)", "verb": "ADAPTED_AS", "targetSlug": "game-of-thrones-hbo", "targetName": "Game of Thrones (HBO, 2011–2019)", "context": "The HBO adaptation of A Song of Ice and Fire became the most watched television drama in history — with a peak global audience of approximately 44 million for the final season — transforming fantasy fiction into mainstream prestige television."},
      {"sourceSlug": "a-song-of-ice-and-fire", "sourceName": "A Song of Ice and Fire (moral complexity)", "verb": "INFLUENCED_BY", "targetSlug": "wars-of-the-roses", "targetName": "Wars of the Roses (15th-century English dynastic conflict)", "context": "The Wars of the Roses provided the primary historical model for A Song of Ice and Fire's political conflicts — the Stark/Lannister dynastic struggle mirrors the York/Lancaster rivalry, and Martin's willingness to destroy sympathetic characters reflects the historical conflict's moral chaos."}
    ],
    "places": [
      {"name": "Westeros and Essos (fictional setting, medieval-inspired geography)", "role": "The fictional continents of Westeros (based loosely on medieval Britain and Europe) and Essos (a vast eastern continent) constitute the world of A Song of Ice and Fire — a world of great geographic and cultural complexity that Martin has built over five volumes"},
      {"name": "United States (Santa Fe, New Mexico, Martin's base)", "role": "Martin writes in Santa Fe, New Mexico — the slow pace of the final two volumes (The Winds of Winter and A Dream of Spring remain unfinished) has become one of the most discussed phenomena in contemporary popular culture"}
    ],
    "subjects": ["Fantasy Fiction", "Modern Era", "George R. R. Martin", "Epic Fantasy", "Television Adaptation", "21st Century", "American Literature", "Medieval History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "A Song of Ice and Fire (Martin, 1996–) is the most culturally impactful fantasy series since Tolkien — its HBO adaptation Game of Thrones became the most watched television drama in history (44 million peak viewers), transforming fantasy fiction into mainstream prestige television. Martin's rejection of Tolkienian moral clarity and his historically grounded political complexity influenced a generation of fantasy writers and established the 'grimdark' subgenre.",
      "significanceCategory": "highly-significant"
    }
  }
},

"delphi-method": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785delphi-method.json",
  "slug": "delphi-method",
  "data": {
    "summary": "The Delphi method is a structured communication and forecasting technique developed by the RAND Corporation in the 1950s–1960s — primarily by Olaf Helmer (1910–2011) and Norman Dalkey (1915–2001) — first described in detail in RAND's classified report 'Use of Experts for the Estimation of Bombing Requirements: A Project DELPHI' (1951) and publicly presented in 'An Experimental Application of the Delphi Method to the Use of Experts' (Helmer and Dalkey, 1963). The technique is a method for structured expert elicitation and consensus-building: a facilitator circulates questionnaires to a panel of experts, collects their responses, provides anonymised summaries to the group (including median responses and ranges of opinion), and repeats the process through multiple rounds — the 'feedback loops' — until the group's judgements converge or stabilise. The anonymity of the process is designed to prevent the distortions of face-to-face group dynamics (dominant personalities, social pressure, anchoring effects).\n\nThe Delphi method was developed in the context of RAND's post-war strategic forecasting work — the question of how to systematically elicit and aggregate expert judgement about complex, uncertain futures in areas like military technology, national security, and economic forecasting where quantitative models were insufficient. RAND's 'Project DELPHI' (named after the Oracle of Delphi, the ancient Greek site of ambiguous prophecy) was initially classified and focused on military applications; when declassified and adapted for commercial, governmental, and academic use in the 1960s–1970s, it became one of the most widely used forecasting and decision-support methods in management consulting, healthcare, technology forecasting, and policy analysis.\n\nThe Delphi method has been applied to an extraordinary range of domains — from forecasting the future of computing technology (the RAND Corporation's own long-range forecasting projects) to healthcare resource allocation, urban planning, environmental policy, and educational curriculum design. Its combination of structured anonymised expert elicitation with iterative feedback and convergence makes it a practical tool for situations where expert knowledge is essential but individual experts are subject to cognitive biases that group process can reduce.",
    "causes": [
      "Post-war RAND Corporation strategic forecasting needs — the Cold War requirement for systematic, rigorous approaches to long-range forecasting in areas like nuclear weapons development, Soviet military capabilities, and technological change, where quantitative models were unavailable and expert intuition was the only resource — drove the development of the Delphi method as a structured approach to aggregating expert judgement.",
      "The recognition of systematic biases in group decision-making — the distortions introduced by dominant personalities, status effects, social conformity pressure, and anchoring in face-to-face expert panels — motivated the Delphi method's design principle of anonymous expert elicitation with iterative feedback: a structured alternative to the committee meeting that could harness expert knowledge while controlling group dynamics.",
      "Olaf Helmer and Norman Dalkey's systematic work on expert judgement at RAND — their interest in developing rigorous scientific methods for areas where formal quantitative models were unavailable — gave the Delphi method its intellectual framework and its claim to be a systematic, replicable procedure for expert forecasting."
    ],
    "effects": [
      "The Delphi method became one of the most widely used structured forecasting and decision-support techniques in the world — applied in healthcare (clinical guideline development, resource allocation), technology forecasting, urban planning, environmental policy, military strategy, and business strategy across dozens of countries and thousands of organisations.",
      "The method's development of structured expert elicitation contributed to the broader field of expert systems and knowledge engineering — the attempt to formalise and replicate expert knowledge in decision-support systems — and influenced the design of other deliberative forecasting methods (nominal group technique, prediction markets, structured analogies).",
      "The Delphi method's application to technology forecasting — from RAND's own long-range forecasting of computing and communications technology to Japan's national technology foresight exercises (used to guide government R&D investment from the 1970s) — demonstrates its role in shaping national and corporate technology strategy in the post-war period."
    ],
    "relationships": [
      {"sourceSlug": "olaf-helmer", "sourceName": "Olaf Helmer (1910–2011) and Norman Dalkey (1915–2001)", "verb": "AUTHORS", "targetSlug": "delphi-method", "targetName": "Delphi method (RAND Corporation, 1951–1963)", "context": "Helmer and Dalkey developed the Delphi method at RAND as a structured approach to expert elicitation and consensus-building — first described in classified form in 1951 and publicly presented in 1963."},
      {"sourceSlug": "delphi-method", "sourceName": "Delphi method", "verb": "DEVELOPED_AT", "targetSlug": "rand-corporation", "targetName": "RAND Corporation (Cold War strategic research)", "context": "The Delphi method was developed at RAND in the context of Cold War strategic forecasting — the need for rigorous methods of aggregating expert judgement about military technology, nuclear strategy, and long-range futures where quantitative models were unavailable."},
      {"sourceSlug": "delphi-method", "sourceName": "Delphi method (expert elicitation)", "verb": "INFLUENCES", "targetSlug": "structured-decision-making", "targetName": "Structured decision-making and expert elicitation methods", "context": "The Delphi method is the foundational technique of structured expert elicitation — widely applied in healthcare, technology forecasting, urban planning, and policy analysis — and influenced the design of related deliberative forecasting methods (nominal group technique, prediction markets)."}
    ],
    "places": [
      {"name": "RAND Corporation, Santa Monica, California (1950s–1960s, development context)", "role": "RAND Corporation — the Cold War strategic research organisation — was the institutional home of the Delphi method's development, reflecting the post-war need for rigorous methods of strategic forecasting under uncertainty"},
      {"name": "Global (widespread application, 1970s–present)", "role": "The Delphi method has been applied worldwide in healthcare, technology forecasting, urban planning, environmental policy, and business strategy — one of the most widely used structured decision-support techniques in the world"}
    ],
    "subjects": ["Operations Research", "Modern Era", "RAND Corporation", "Forecasting", "Expert Systems", "Decision Theory", "Cold War", "Technology Forecasting"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Delphi method (Helmer and Dalkey, RAND Corporation, 1951–1963) is one of the most widely used structured forecasting and decision-support techniques in the world — applied in healthcare, technology forecasting, urban planning, and policy analysis across dozens of countries. Developed in the Cold War context of RAND's strategic forecasting work, it introduced systematic anonymous expert elicitation with iterative feedback as an alternative to the distortions of face-to-face group decision-making.",
      "significanceCategory": "significant"
    }
  }
},

"life-cycle-assessment": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785life-cycle-assessment.json",
  "slug": "life-cycle-assessment",
  "data": {
    "summary": "Life Cycle Assessment (LCA) is the systematic methodology for evaluating the environmental impacts of a product, process, or service throughout its entire life cycle — from raw material extraction ('cradle') through manufacturing, distribution, use, and final disposal ('grave') — developed as a rigorous analytical framework primarily through the work of the Society of Environmental Toxicology and Chemistry (SETAC) from the late 1980s and subsequently standardised in the ISO 14040 series (1997, revised 2006). The methodology has four stages: goal and scope definition, inventory analysis (quantification of material and energy flows), impact assessment (translation of inventory data into environmental impact categories such as climate change, ozone depletion, acidification, eutrophication, and human toxicity), and interpretation. LCA provides a comprehensive, quantitative basis for comparing the environmental performance of competing products, identifying improvement priorities, and avoiding burden-shifting (reducing impact in one life cycle stage while inadvertently increasing it in another).\n\nLife Cycle Assessment grew from parallel research streams in the 1960s–1970s: the energy analysis work associated with the 1973 oil crisis (which motivated systematic analysis of the energy requirements of product systems), the pollution prevention movement's need for quantitative environmental accounting, and early 'resource and environmental profile analysis' studies (including Coca-Cola's 1969 internal study of beverage container alternatives — now considered the first LCA). The methodology was standardised through SETAC workshops (1991–1993, the Code of Practice), UNEP guidance, and ultimately the ISO 14040 series, achieving the international standardisation that made LCA a legitimate tool for eco-labelling, product environmental declarations, and regulatory compliance.\n\nLCA is now a standard tool in environmental engineering, sustainable product design, corporate sustainability reporting, green procurement, and environmental policy — used by manufacturers to optimise product designs, by retailers to compare supplier products, by governments to evaluate policy options, and by researchers to compare the environmental performance of energy systems (the LCA of fossil fuels vs. renewables is central to energy policy analysis). The methodology has been particularly influential in the debate about the environmental performance of biofuels, electric vehicles, and renewable energy technologies.",
    "causes": [
      "The 1973 oil crisis — which focused attention on the energy requirements of product systems and motivated the development of energy analysis methodologies — was a primary driver of early life cycle thinking: the need to understand the full energy chain from resource extraction to end use drove the development of inventory analysis methods that formed the basis of LCA.",
      "The pollution prevention movement of the 1970s–1980s — the shift from end-of-pipe pollution control to prevention-oriented environmental management — created the demand for quantitative environmental accounting methods that could identify pollution prevention opportunities throughout the product system, not just at the point of emission.",
      "SETAC's standardisation work (1991–1993) and the ISO 14040 series (1997) — which provided internationally agreed definitions, procedures, and reporting requirements for LCA — transformed it from a set of disparate methods into a rigorous, replicable, internationally standardised methodology that could be used for eco-labelling, environmental declarations, and regulatory purposes."
    ],
    "effects": [
      "Life Cycle Assessment became the standard quantitative tool for comparative environmental performance analysis — used in eco-labelling schemes (the EU Ecolabel), environmental product declarations (EPDs), corporate sustainability reporting, green procurement standards, and environmental impact assessments, enabling quantitative comparison of products and processes on a common basis.",
      "LCA's contribution to the renewable energy debate — systematic life cycle analyses of solar, wind, and other renewable energy technologies demonstrating their substantially lower life cycle greenhouse gas emissions compared to fossil fuels — provided crucial quantitative evidence for energy policy decisions and has been central to arguments for accelerating the energy transition.",
      "The methodological framework of LCA — particularly its inventory analysis of material and energy flows across complex product systems — influenced the development of related environmental accounting methods (material flow analysis, environmental input-output analysis, carbon footprinting, water footprinting) that together constitute the toolkit of industrial ecology."
    ],
    "relationships": [
      {"sourceSlug": "setac", "sourceName": "Society of Environmental Toxicology and Chemistry (SETAC)", "verb": "STANDARDISES", "targetSlug": "life-cycle-assessment", "targetName": "Life Cycle Assessment (methodology, 1991–2006 ISO 14040)", "context": "SETAC workshops (1991–1993) and the subsequent ISO 14040 series standardised LCA as an international methodology — transforming diverse approaches into a rigorous, replicable tool for environmental impact analysis."},
      {"sourceSlug": "life-cycle-assessment", "sourceName": "Life Cycle Assessment (LCA)", "verb": "INFORMS", "targetSlug": "renewable-energy-policy", "targetName": "Renewable energy environmental performance analysis", "context": "LCA's systematic analysis of life cycle greenhouse gas emissions from solar, wind, and other renewable technologies — demonstrating their substantially lower impacts compared to fossil fuels — has been central to arguments for the energy transition in climate policy."},
      {"sourceSlug": "life-cycle-assessment", "sourceName": "Life Cycle Assessment (industrial ecology)", "verb": "PART_OF", "targetSlug": "industrial-ecology", "targetName": "Industrial ecology (material flow analysis, carbon footprinting)", "context": "LCA's inventory analysis framework influenced the development of related methods — material flow analysis, carbon footprinting, water footprinting — that together constitute the toolkit of industrial ecology, the science of environmental sustainability in industrial systems."}
    ],
    "places": [
      {"name": "Global (ISO 14040 standardisation, international application)", "role": "LCA is applied globally — standardised through ISO 14040 and used in eco-labelling, corporate sustainability reporting, green procurement, and environmental policy worldwide"},
      {"name": "United States (Coca-Cola study, 1969; SETAC, Pensacola, Florida)", "role": "Coca-Cola's 1969 internal study of beverage container alternatives is now considered the first LCA; SETAC — headquartered in Pensacola, Florida — organised the workshops that standardised the methodology in 1991–1993"}
    ],
    "subjects": ["Environmental Science", "Modern Era", "Sustainability", "Industrial Ecology", "Environmental Policy", "Green Technology", "ISO Standards", "Product Design"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Life Cycle Assessment (LCA, standardised 1991–2006) is the standard international methodology for quantitative environmental performance analysis — used in eco-labelling, corporate sustainability reporting, green procurement, and energy policy analysis worldwide. Its systematic comparison of the life cycle environmental impacts of renewable and fossil energy technologies has been central to the energy transition debate, and its framework influenced the development of industrial ecology as a discipline.",
      "significanceCategory": "significant"
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
