#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 23 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: leviathan-hobbes-1651, book-of-job, book-of-revelation, beatitudes,
          beowulf, alexiad, anabasis-of-alexander-arrian, al-kutub-al-sittah
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-23-may2026"

ENRICHMENTS = {

"leviathan-hobbes-1651": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785leviathan-hobbes-1651.json",
  "slug": "leviathan-hobbes-1651",
  "data": {
    "summary": "Leviathan, or The Matter, Forme and Power of a Common-Wealth Ecclesiasticall and Civill is the masterwork of English philosopher Thomas Hobbes (1588–1679), published in London in 1651 — the founding text of modern political philosophy and social contract theory. Written during the English Civil War while Hobbes was in exile in Paris, Leviathan constructs from materialist first principles a theory of human nature, the state of nature, and the necessity of absolute sovereign power — the 'Leviathan' of the title, named after the biblical sea monster — that became one of the most controversial and influential works in the Western political tradition, simultaneously founding modern political science and provoking fundamental objections that drove the development of liberalism, republicanism, and democratic theory.\n\nHobbes's argument proceeds systematically from his materialist conception of human beings as physical organisms driven by appetite and aversion, to his account of human reason as the calculation of consequences, to his famous description of the natural condition of mankind — without political authority — as a 'war of all against all' in which life is 'solitary, poor, nasty, brutish, and short'. From this 'state of nature' analysis, Hobbes deduces the social contract: rational individuals agree to transfer their natural right to self-governance to a single sovereign authority (whether a monarch or assembly) in exchange for the security of civil order. The sovereign's authority, once granted, is absolute and indivisible — Hobbes resists any limitation or division of sovereign power as the path back to civil war — and subjects have no right to rebellion except in the direct case of the sovereign threatening their lives.\n\nLeviathan's immediate context was the English Civil War — and its argument for sovereign authority over the church (the book's second half attacks the political claims of both the Catholic Church and the Presbyterian model) scandalised contemporaries who saw it as atheism and absolutism in equal measure. But its long-term influence was enormous: John Locke's Two Treatises (1689) were written as a systematic refutation of Hobbes; Rousseau's Social Contract reworks Hobbes's framework; and the tradition of social contract theory in Rawls, Gauthier, and contemporary political philosophy all grapple directly with Hobbes's challenge.",
    "causes": [
      "The English Civil War (1642–1651) — the struggle between Parliament and Charles I that overthrew the monarchy and threatened to dissolve all political authority — was the immediate context of Leviathan, and Hobbes's terrifying state-of-nature analysis reflects his visceral horror at the dissolution of civil order he was witnessing.",
      "Hobbes's encounter with the new mechanical philosophy of Galileo and Descartes — and his determination to apply the same materialist, mathematical method to the study of politics and human nature that Galileo had applied to physics — gave Leviathan its systematic, deductive structure and its philosophical ambition.",
      "The collapse of traditional religious and political authority — the Reformation's fragmentation of Christian unity, the challenge to monarchical divine right, the competing claims of Parliament, church, and king — created the political-philosophical vacuum that Hobbes sought to fill with a new, secular theory of political authority based on human reason alone."
    ],
    "effects": [
      "Leviathan founded the modern tradition of social contract theory — the analytical framework that derives political authority from a hypothetical agreement between rational individuals — that runs through Locke (1689), Rousseau (1762), Kant (1797), Rawls (A Theory of Justice, 1971), and remains the dominant framework of contemporary political philosophy.",
      "Hobbes's argument for the absolute sovereignty of the civil power over religion — his systematic subordination of church authority to the state — was one of the most powerful early arguments for secular government and the separation of church and state, contributing to the Enlightenment's programme of limiting religious power over political life.",
      "The reaction against Hobbes's absolutism — particularly Locke's Two Treatises of Government (1689), written in explicit refutation of Hobbesian sovereignty — was one of the principal drivers of liberal political theory, shaping the political philosophy of the American and French revolutions and the tradition of constitutional limited government."
    ],
    "relationships": [
      {"sourceSlug": "thomas-hobbes", "sourceName": "Thomas Hobbes (1588–1679)", "verb": "AUTHORS", "targetSlug": "leviathan-hobbes-1651", "targetName": "Leviathan (1651)", "context": "Hobbes wrote Leviathan in Paris during his exile from the English Civil War — the work's argument for absolute sovereignty was shaped by his horror at the breakdown of political order."},
      {"sourceSlug": "leviathan-hobbes-1651", "sourceName": "Leviathan (1651)", "verb": "PROMPTS_RESPONSE_FROM", "targetSlug": "john-locke", "targetName": "John Locke (Two Treatises of Government, 1689)", "context": "Locke's Two Treatises were written as a systematic refutation of Hobbesian sovereignty — Locke accepted the social contract framework but rejected absolute sovereignty in favour of limited, constitutional government."},
      {"sourceSlug": "english-civil-war", "sourceName": "English Civil War (1642–1651)", "verb": "CONTEXTUALISES", "targetSlug": "leviathan-hobbes-1651", "targetName": "Leviathan (1651)", "context": "The English Civil War — the dissolution of political authority that Hobbes experienced as exile — provided the immediate political context for Leviathan's terrifying state-of-nature analysis and its argument for absolute sovereign power."}
    ],
    "places": [
      {"name": "Paris (exile) and London (publication, 1651)", "role": "Hobbes wrote Leviathan in Paris while in exile during the English Civil War, and published it in London in 1651 as the war was concluding"},
      {"name": "Western political tradition (global influence)", "role": "Leviathan's social contract framework shaped political philosophy throughout the Western tradition — from Locke and Rousseau through Rawls and contemporary political philosophy"}
    ],
    "subjects": ["Political Philosophy", "Early Modern Era", "Social Contract", "Sovereignty", "English History", "Political Theory", "Materialism", "Natural Law"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Leviathan (Hobbes, 1651) is the founding text of modern political philosophy — its social contract framework, state-of-nature analysis, and theory of sovereign authority established the terms of debate within which all subsequent Western political philosophy (Locke, Rousseau, Kant, Rawls) has operated. Written during the English Civil War, it simultaneously justified absolute sovereignty and, by provoking Locke's systematic refutation, launched the tradition of liberal constitutional theory that shaped the American and French revolutions.",
      "significanceCategory": "world-changing"
    }
  }
},

"book-of-job": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780book-of-job.json",
  "slug": "book-of-job",
  "data": {
    "summary": "The Book of Job is one of the most profound and philosophically complex texts of the Hebrew Bible — a poetic dialogue exploring the problem of innocent suffering (theodicy), the nature of the covenant relationship between God and humanity, and the limits of human understanding of divine purpose. Placed in the Ketuvim ('Writings') section of the Hebrew Bible and the Old Testament wisdom tradition, it tells the story of Job, a righteous man of 'the land of Uz' (of uncertain location, probably Edom) whose prosperity, family, and health are destroyed through a wager between God and the 'Adversary' (Hebrew: הַשָּׂטָן, ha-Satan, 'the Accuser'). The Book's date of composition is debated (ranging from the 10th to 3rd century BCE), but it draws on ancient Near Eastern wisdom traditions and represents one of the earliest systematic philosophical engagements with the problem of evil.\n\nThe Book of Job consists of a prose frame narrative (Job 1–2, 42:7–17) surrounding a long central poetic dialogue in which Job debates the causes of his suffering with three friends (Eliphaz, Bildad, Zophar) and eventually with a fourth interlocutor (Elihu). The friends argue the traditional position of retributive theology: suffering is God's punishment for sin, so Job must have sinned. Job passionately rejects this — he maintains his innocence, demands an audience with God, and challenges the justice of his suffering. God then appears in a whirlwind (the 'Voice from the Whirlwind', Job 38–41) and delivers a breathtaking speech cataloguing the wonders of creation — but never directly answering Job's question about the justice of his suffering. God vindicates Job over his friends, restores his prosperity, and the frame narrative ends happily — leaving the philosophical question of innocent suffering deliberately unresolved.\n\nThe Book of Job's influence on Western literature, theology, and philosophy has been enormous: its theodicy problem — how to reconcile divine goodness and omnipotence with the existence of innocent suffering — is one of the central questions of Western religious philosophy, engaging thinkers from Augustine and Aquinas through Leibniz, Kant, and Dostoevsky to 20th-century theology in the wake of the Holocaust.",
    "causes": [
      "The ancient Near Eastern wisdom tradition — including the Babylonian 'Job' (I Will Praise the Lord of Wisdom, c. 1700 BCE) and the Dialogue of a Man with His God — provided the intellectual context within which the Book of Job was composed, addressing the persistent problem of the righteous sufferer in polytheistic and monotheistic religious cultures.",
      "The Hebrew Bible's prophetic tradition and its covenantal theology — the relationship between Israel's faithfulness and divine blessing/punishment — created the orthodox position that Job's friends articulate and the Book challenges, setting up the central tension between traditional retributive theology and the reality of innocent suffering.",
      "The development of wisdom literature in the ancient Near East — texts that stepped back from national history and covenant to ask universal philosophical questions about human nature, suffering, justice, and the cosmos — provided the genre within which Job's radical philosophical questioning of divine justice was given literary form."
    ],
    "effects": [
      "The Book of Job established the theodicy problem — the philosophical question of how a good and omnipotent God permits innocent suffering — as one of the central questions of Western religious philosophy, engaging Jewish, Christian, and Islamic thinkers from the rabbis through Augustine, Aquinas, Leibniz, and Kant to 20th-century responses to the Holocaust.",
      "Job's poetic and dramatic form — the figure of the righteous sufferer who challenges God directly, the voice from the whirlwind that overwhelms human questioning with divine sublimity — became one of the archetypal patterns of Western literature, influencing Milton's Paradise Lost, Blake's Illustrations of the Book of Job, Dostoevsky's Brothers Karamazov, and Kafka's The Trial.",
      "The Book of Job's conclusion — God vindicates Job's honesty over his friends' orthodoxy, and the philosophical question is left without a simple answer — established a tradition of authentic theological questioning that values honesty about human experience over doctrinal tidiness, influencing Jewish theology after the Holocaust and Christian liberation theology."
    ],
    "relationships": [
      {"sourceSlug": "book-of-job", "sourceName": "Book of Job", "verb": "ADDRESSES", "targetSlug": "theodicy", "targetName": "Theodicy (problem of evil in theology)", "context": "The Book of Job is the paradigmatic treatment of the theodicy problem in Western religion — the philosophical question of how to reconcile divine goodness and omnipotence with innocent suffering."},
      {"sourceSlug": "book-of-job", "sourceName": "Book of Job", "verb": "INFLUENCES", "targetSlug": "dostoevsky", "targetName": "Fyodor Dostoevsky (1821–1881)", "context": "Dostoevsky's engagement with the theodicy problem — particularly Ivan Karamazov's rebellion against God in The Brothers Karamazov — draws directly on the Job tradition of honest protest against innocent suffering."},
      {"sourceSlug": "book-of-job", "sourceName": "Book of Job", "verb": "PART_OF", "targetSlug": "hebrew-bible", "targetName": "Hebrew Bible (Tanakh)", "context": "Job is placed in the Ketuvim (Writings) section of the Hebrew Bible — the third section after the Torah and Prophets — and represents the wisdom literature tradition."}
    ],
    "places": [
      {"name": "Ancient Near East (Land of Uz, c. 10th–3rd century BCE)", "role": "The setting and context of composition — Job is set in the Land of Uz (probably Edom, outside Israel), reflecting the wisdom literature's universalist perspective that transcends national boundaries"},
      {"name": "Western religious and literary tradition (global influence)", "role": "The sphere of the Book of Job's influence — its theodicy problem has engaged Jewish, Christian, and Islamic thinkers across two millennia, and its literary form has shaped Western literature from Milton to Kafka"}
    ],
    "subjects": ["Hebrew Bible", "Religious Philosophy", "Classical Era", "Theodicy", "Wisdom Literature", "Ancient Near East", "Judaism", "Christianity"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Book of Job (Hebrew Bible, c. 10th–3rd century BCE) is the paradigmatic treatment of the theodicy problem in Western religion — the question of how divine goodness and omnipotence are compatible with innocent suffering. Its poetic dialogue between Job and his friends, climaxing in God's sublime speech from the whirlwind, has shaped Jewish, Christian, and Islamic religious philosophy across two millennia, and its influence on Western literature — from Milton and Blake to Dostoevsky and Kafka — is profound.",
      "significanceCategory": "world-changing"
    }
  }
},

"book-of-revelation": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780book-of-revelation.json",
  "slug": "book-of-revelation",
  "data": {
    "summary": "The Book of Revelation (Greek: Ἀποκάλυψις, Apokalypsis, 'Apocalypse' or 'Unveiling') is the final book of the Christian New Testament — an apocalyptic prophetic text attributed to 'John of Patmos' (traditionally identified with the apostle John, though modern scholarship distinguishes several possible authors) and composed c. 95 CE during the reign of the Roman Emperor Domitian. Written in a highly symbolic and visionary register drawing on Hebrew prophetic literature (particularly Ezekiel, Daniel, and Zechariah), it addresses seven churches of Asia Minor, describes a series of heavenly visions of cosmic war between good and evil, the defeat of Rome (figured as 'Babylon, the great whore'), the Last Judgment, and the establishment of a New Jerusalem — the eternal kingdom of God on earth. The most contested and variously interpreted text in the New Testament, Revelation has exercised an influence on Christian theology, art, literature, and political imagination that is disproportionate to its late and disputed canonical status.\n\nRevelation's key images and narrative sequences — the Four Horsemen of the Apocalypse (War, Famine, Death, Conquest), the Beast of 666, the Whore of Babylon, the Millennium (1,000-year reign of Christ), Armageddon, the New Jerusalem — have become so deeply embedded in Western culture that they shape imagination far beyond explicitly religious contexts. The text was used by early Christians as a coded resistance document against Roman imperial persecution; by medieval millenarian movements (the Cathars, the Joachimites, the Taborites) as prophecy of imminent divine revolution; by the Reformation's radical wing as a critique of papal Rome; by Puritan colonists in America who saw themselves as the New Jerusalem; and by 20th–21st century evangelical Protestantism (particularly the Left Behind series and dispensationalist theology) as a literal prophecy of the End Times.\n\nRevelation's political theology — its depiction of earthly empire as demonic, its promise of divine vindication for the persecuted, its vision of history moving toward a cosmic resolution — has made it both a resource for revolutionary resistance (liberation theology, abolitionism) and, in its more literal interpretations, a potential driver of apocalyptic politics.",
    "causes": [
      "The Roman persecution of Christians under Domitian (c. 81–96 CE) — including the exile of John of Patmos to the island of Patmos — created the context of crisis and persecution within which Revelation's coded critique of Roman imperial power (Rome as 'Babylon', the Emperor as the Beast) was written as a message of resistance and hope.",
      "The Hebrew prophetic and apocalyptic tradition — particularly the Books of Daniel, Ezekiel, Isaiah, and Zechariah, with their visions of cosmic war, divine judgment, and the establishment of God's kingdom on earth — provided the literary forms, symbols, and theological framework within which Revelation was composed.",
      "The early Christian community's urgent expectation of the imminent return of Christ (parousia) and the end of the current age — which had not materialised as expected by the second generation — created the theological pressure to which Revelation's reaffirmation of ultimate divine victory and cosmic renewal was a pastoral response."
    ],
    "effects": [
      "Revelation provided the founding images and narrative of Christian eschatology — the theology of the Last Things (death, judgment, heaven, hell, the End of History) — that shaped Christian thought, art, and culture across two millennia, from the Harrowing of Hell in medieval mystery plays through Michelangelo's Last Judgment to contemporary evangelical dispensationalism.",
      "The millenarian movements that drew on Revelation's thousand-year kingdom prophecy — from the medieval Joachimite movements and the radical wing of the Reformation (Münster 1534) through the American Great Awakenings and 20th-century evangelical millennialism — have been significant social and political forces, driving movements of revolution, reform, and radical community formation.",
      "Revelation's symbolic vocabulary — the Beast, 666, Armageddon, the Whore of Babylon, the New Jerusalem — has so thoroughly permeated Western culture that its imagery appears in contexts ranging from medieval cathedral iconography and Renaissance painting (Dürer's Four Horsemen, 1498) through William Blake and D.H. Lawrence to contemporary popular culture, politics, and environmental eschatology."
    ],
    "relationships": [
      {"sourceSlug": "john-of-patmos", "sourceName": "John of Patmos (c. 95 CE)", "verb": "AUTHORS", "targetSlug": "book-of-revelation", "targetName": "Book of Revelation (c. 95 CE)", "context": "The Book of Revelation is attributed to 'John', writing in exile on Patmos during the Domitianic persecution — whether the author was the apostle John, John the Elder, or another John is disputed by scholarship."},
      {"sourceSlug": "book-of-revelation", "sourceName": "Book of Revelation", "verb": "CRITIQUES", "targetSlug": "roman-empire", "targetName": "Roman Empire (specifically Domitianic Rome)", "context": "Revelation's portrayal of Rome as 'Babylon the Great Whore' and the Emperor as the Beast of 666 is a coded critique of Roman imperial power written during the Domitianic persecution of Christians."},
      {"sourceSlug": "book-of-revelation", "sourceName": "Book of Revelation", "verb": "INFLUENCES", "targetSlug": "millenarianism", "targetName": "Christian Millenarianism", "context": "Revelation's prophecy of the Millennium — the thousand-year reign of Christ — is the foundational text of Christian millenarianism, the tradition of movements expecting an imminent divine transformation of the world."}
    ],
    "places": [
      {"name": "Patmos, Asia Minor (c. 95 CE)", "role": "The place of composition — John wrote Revelation while in exile on the island of Patmos during Domitian's persecution of Christians"},
      {"name": "Seven Churches of Asia Minor (Ephesus, Smyrna, Pergamon, Thyatira, Sardis, Philadelphia, Laodicea)", "role": "The immediate addressees of Revelation — the seven churches to whom the letters at the beginning of the book are addressed"}
    ],
    "subjects": ["New Testament", "Christian Theology", "Classical Era", "Apocalyptic Literature", "Eschatology", "Early Christianity", "Roman Empire", "World Literature"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Book of Revelation (c. 95 CE) is the paradigmatic apocalyptic text of Western culture — its images (Four Horsemen, Beast of 666, Armageddon, New Jerusalem) have shaped Christian eschatology, medieval and Renaissance art, millenarian political movements from the Reformation to American evangelicalism, and Western cultural imagination for nearly two millennia. Its coded critique of Roman imperial power, promise of divine vindication for the persecuted, and vision of cosmic renovation have made it a resource for both revolutionary hope and apocalyptic politics.",
      "significanceCategory": "world-changing"
    }
  }
},

"beatitudes": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780beatitudes.json",
  "slug": "beatitudes",
  "data": {
    "summary": "The Beatitudes (from Latin: beati, 'blessed' or 'happy') are the opening declarations of the Sermon on the Mount — the extended teaching attributed to Jesus of Nazareth in the Gospel of Matthew (chapters 5–7) and its shorter parallel in Luke 6:20–23 (the Sermon on the Plain). The Matthean Beatitudes (Matthew 5:3–12) comprise eight or nine blessings — 'Blessed are the poor in spirit, for theirs is the kingdom of heaven; Blessed are those who mourn, for they will be comforted; Blessed are the meek, for they will inherit the earth...' — that articulate a radical inversion of conventional worldly values: the poor, the meek, the persecuted, those who hunger and thirst for righteousness are declared the recipients of divine blessing and the inheritors of the Kingdom of God. The Beatitudes form the programmatic opening of Jesus's most comprehensive surviving discourse, and the Sermon on the Mount as a whole is considered by many Christians the definitive statement of Christian ethics.\n\nThe Beatitudes' social and ethical radicalism — their blessing of the poor, the mournful, and the persecuted rather than the powerful, the prosperous, and the celebrated — has made them one of the most contested and transformative passages in Western history. Medieval Catholic interpretation generally spiritualised them (the 'poor in spirit' as the spiritually humble rather than the materially poor), while Francis of Assisi's movement found in them a mandate for voluntary poverty, and the liberation theology movement of the 20th century returned to a more literal reading of Jesus's blessing of the poor as a critique of economic inequality. Tolstoy, Gandhi, and Martin Luther King each drew on the Beatitudes' non-violent ethic ('Blessed are the peacemakers') in their programmes of civil resistance.\n\nThe Sermon on the Mount, of which the Beatitudes are the opening, also contains the Lord's Prayer, the Golden Rule ('Do to others as you would have them do to you', Matthew 7:12), and the antitheses ('You have heard it said... but I say to you') that intensify the Torah's moral demands. Together they constitute the clearest surviving statement of Jesus's ethical teaching and have shaped Christian moral theology, social ethics, and political thought across two millennia.",
    "causes": [
      "Jesus of Nazareth's teaching ministry in Galilee (c. 28–30 CE) — addressed primarily to the rural poor of Roman-occupied Judea — provided the social context for the Beatitudes' inversion of conventional values: the blessing of the poor, marginalised, and persecuted resonated with an audience experiencing Roman occupation and the social displacement of the Herodian economy.",
      "The Hebrew prophetic tradition's preferential concern for the poor and oppressed — the tradition of Isaiah 61 ('The Spirit of the Lord is upon me, because he has anointed me to bring good news to the poor'), Amos, and Micah — provided Jesus with the scriptural and theological framework for the Beatitudes' radical social ethics.",
      "The context of early Christian community formation — the compilation of the Gospel of Matthew (c. 80–90 CE), addressed to a Jewish-Christian community experiencing persecution and the aftermath of the Jewish-Roman war — shaped the Sermon on the Mount's final form, giving the Beatitudes' blessing of the persecuted ('Blessed are those who are persecuted for righteousness' sake') particular pastoral urgency."
    ],
    "effects": [
      "The Beatitudes established the programmatic ethical vision of Christianity — the radical inversion of worldly values, the preferential option for the poor, the non-violent response to persecution — that has been the source of both the most radical and the most conventional Christian social ethics across two millennia.",
      "The Beatitudes inspired the Franciscan movement — Francis of Assisi's literal embrace of evangelical poverty, directly drawn from Matthew 5:3 ('Blessed are the poor in spirit') and the Sermon on the Mount generally — which became the most significant lay religious movement of medieval Christianity.",
      "The Sermon on the Mount's non-violent ethic — 'Blessed are the meek'; 'Do not resist an evil-doer'; 'Love your enemies' (Matthew 5:38–44) — was the explicit basis of Tolstoy's religious anarchism, Gandhi's ahimsa and satyagraha, and Martin Luther King's civil rights programme, making the Beatitudes a foundational text of 20th-century non-violent political resistance."
    ],
    "relationships": [
      {"sourceSlug": "jesus-of-nazareth", "sourceName": "Jesus of Nazareth (c. 4 BCE–30 CE)", "verb": "DELIVERS", "targetSlug": "beatitudes", "targetName": "Beatitudes (Sermon on the Mount)", "context": "The Beatitudes are attributed to Jesus in the Gospels of Matthew and Luke — forming the opening of the Sermon on the Mount, the most comprehensive surviving collection of Jesus's ethical teaching."},
      {"sourceSlug": "beatitudes", "sourceName": "Beatitudes", "verb": "INSPIRES", "targetSlug": "francis-of-assisi", "targetName": "Francis of Assisi (1181–1226)", "context": "Francis of Assisi's movement of voluntary poverty and evangelical simplicity was directly inspired by the Beatitudes and the Sermon on the Mount — particularly Jesus's blessing of the poor and his call to sell possessions and follow him."},
      {"sourceSlug": "beatitudes", "sourceName": "Beatitudes", "verb": "INFLUENCES", "targetSlug": "mahatma-gandhi", "targetName": "Mahatma Gandhi (non-violent resistance)", "context": "Gandhi explicitly acknowledged the Sermon on the Mount's influence on his philosophy of non-violent resistance (ahimsa, satyagraha) — particularly the Beatitudes' blessing of the meek and the instruction to love enemies."}
    ],
    "places": [
      {"name": "Galilee, Roman Palestine (c. 28–30 CE)", "role": "The setting of Jesus's Sermon on the Mount — though the specific location ('a mountain') is not identified, Galilee was the primary setting of his ministry and the audience the rural poor of Roman-occupied Judea"},
      {"name": "Global Christian world (2+ millennium influence)", "role": "The Beatitudes' sphere of influence — shaping Christian ethics, social movements, art, literature, and political thought across the entire history of Christianity and beyond"}
    ],
    "subjects": ["New Testament", "Christian Ethics", "Classical Era", "Jesus of Nazareth", "Sermon on the Mount", "Christianity", "Non-Violence", "Liberation Theology"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Beatitudes (Gospel of Matthew 5:3–12, c. 80–90 CE) — the opening declarations of the Sermon on the Mount — established the programmatic ethical vision of Christianity: the radical inversion of worldly values, the blessing of the poor and persecuted, and the non-violent ethic that shaped Christian moral theology across two millennia. Directly inspiring Francis of Assisi's evangelical poverty movement and, in the 20th century, Gandhi's and Martin Luther King's programmes of non-violent resistance, they are among the most historically consequential ethical statements in world history.",
      "significanceCategory": "world-changing"
    }
  }
},

"beowulf": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782beowulf.json",
  "slug": "beowulf",
  "data": {
    "summary": "Beowulf is the longest surviving Old English poem — 3,182 alliterative lines preserved in a single manuscript (the Nowell Codex, c. 1000 CE) in the British Library — and the most important work of Old English literature. Set in the legendary Scandinavian past of the 5th–6th centuries and composed (in its surviving form) between the late 7th and early 11th centuries, it narrates the career of the Geat hero Beowulf, who crosses the sea to the Danish court of King Hrothgar to rid his meadhall (Heorot) of the monster Grendel, then kills Grendel's mother in her underwater lair, and finally, as an aged king, dies fighting a dragon that has been awakened by the theft of its treasure hoard — leaving his kingdom without a protector. One of the foundational texts of English literature and the defining work of the Germanic heroic tradition, Beowulf has been studied, translated, and imitated continuously since its rediscovery in the 19th century.\n\nBeowulf's literary world combines the heroic values of the Germanic warrior culture (loyalty to the lord, courage in battle, the winning of fame, the sharing of treasure in the meadhall) with a Christian spiritual overlay — the poem is composed by a Christian poet looking back at pagan ancestors, and Grendel and his mother are described as descendants of Cain, the biblical fratricidal outcast. The tension between the heroic code (which demands the pursuit of glory and vengeance) and the Christian values that shadow the narrative (wisdom, humility, the transience of earthly glory) gives the poem its particular reflective and elegiac quality.\n\nJ.R.R. Tolkien's 1936 essay 'Beowulf: The Monsters and the Critics' transformed Beowulf scholarship — arguing that the poem should be read as literature rather than historical document, and that the monsters (Grendel, the dragon) were its thematic heart, not peripheral curiosities. Tolkien drew directly on Beowulf in constructing Middle-earth (particularly the Rohirrim's culture, the language Old English elements in Tolkien's invented languages, and the dragon Smaug), and his translation (published posthumously 2014) remains widely read.",
    "causes": [
      "The Anglo-Saxon warrior culture and its value system — loyalty to the lord (comitatus), courage in battle, the winning of lasting fame (lof, dom), the meadhall as the centre of community — provided the heroic world within which Beowulf's narrative is set and from which its values derive.",
      "The Christianisation of the Anglo-Saxon world (7th–8th centuries CE) — and the particular moment of a Christian poet looking back at the pagan Germanic past — created the retrospective, elegiac perspective of Beowulf, in which heroic values are celebrated but framed within a Christian awareness of transience and divine sovereignty.",
      "The tradition of oral Germanic heroic poetry — transmitted through the figure of the scop (court poet) and performed in the meadhall — provided the compositional conventions (alliterative metre, kennings, formulaic expressions, the elegiac tone) within which Beowulf was composed and within which it would originally have been performed."
    ],
    "effects": [
      "Beowulf established the literary tradition of Old English poetry — the alliterative metre, the kenning tradition ('whale-road' for the sea, 'ring-giver' for the king, 'light-of-battle' for the sword), the elegiac tone — that influenced Middle English poetry and, through the scholarly rediscovery in the 19th century, the modern tradition of medievalism.",
      "J.R.R. Tolkien's engagement with Beowulf — his 1936 essay, his translation, and the direct borrowings in The Lord of the Rings (the Rohirrim's culture, Smaug the dragon, the Ring as cursed treasure) — made the Old English poem a foundational source for modern fantasy literature, shaping the genre's conventions worldwide.",
      "Seamus Heaney's translation (1999) — which won the Whitbread Book of the Year and became the most widely read English version — brought Beowulf to a global popular audience in the late 20th century, demonstrating the poem's continuing vitality and its capacity to speak across languages and cultures."
    ],
    "relationships": [
      {"sourceSlug": "beowulf", "sourceName": "Beowulf (poem, c. 700–1000 CE)", "verb": "INFLUENCES", "targetSlug": "j-r-r-tolkien", "targetName": "J.R.R. Tolkien (The Lord of the Rings)", "context": "Tolkien's 1936 essay transformed Beowulf scholarship, and the poem directly shaped The Lord of the Rings — the Rohirrim's culture, Smaug the dragon, and the One Ring as cursed treasure all derive from Beowulf's imagery."},
      {"sourceSlug": "beowulf", "sourceName": "Beowulf", "verb": "REPRESENTS", "targetSlug": "old-english-literature", "targetName": "Old English literature", "context": "Beowulf is the longest and most important surviving work of Old English literature — the primary monument of the Anglo-Saxon literary tradition."},
      {"sourceSlug": "beowulf", "sourceName": "Beowulf", "verb": "TRANSLATED_BY", "targetSlug": "seamus-heaney", "targetName": "Seamus Heaney (translation, 1999)", "context": "Heaney's 1999 translation brought Beowulf to a global popular audience — winning the Whitbread Book of the Year and becoming the most widely read English-language version."}
    ],
    "places": [
      {"name": "Anglo-Saxon England (c. 700–1000 CE, composition)", "role": "The context of composition — Beowulf was composed in England by an Anglo-Saxon Christian poet, preserved in a single manuscript of c. 1000 CE"},
      {"name": "Legendary Scandinavia (Denmark and Geatland, 5th–6th century setting)", "role": "The poem's narrative setting — the Danish court of King Hrothgar and the Geat homeland of the hero Beowulf, set in a legendary Germanic heroic past"}
    ],
    "subjects": ["Old English Literature", "Medieval Literature", "Medieval Era", "Germanic Culture", "Heroic Poetry", "Anglo-Saxon England", "World Literature", "Fantasy"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Beowulf (c. 700–1000 CE) is the defining work of Old English literature and the primary monument of the Germanic heroic tradition — a 3,182-line alliterative epic that shaped medieval English literary culture. Tolkien's 1936 essay transformed its scholarly reception and the poem directly inspired The Lord of the Rings, making it a foundational source for modern fantasy literature. Seamus Heaney's 1999 translation brought it to a global popular audience.",
      "significanceCategory": "highly-significant"
    }
  }
},

"alexiad": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781alexiad.json",
  "slug": "alexiad",
  "data": {
    "summary": "The Alexiad (Greek: Ἀλεξιάς, Alexias) is a Byzantine historical chronicle written by Princess Anna Komnene (1083–c. 1153) — the daughter of Emperor Alexios I Komnenos (r. 1081–1118) — covering the reign of her father from his accession to his death. Composed in Greek in an elevated classical style consciously modelled on Thucydides and Homer, the Alexiad is one of the most important historical sources for Byzantine history in the late 11th and early 12th centuries and for the First Crusade (1095–1099) — described from the Byzantine perspective as the disruptive arrival of Latin Christian armies that complicated Alexios's efforts to recover lost Anatolian territory from the Seljuk Turks. Anna Komnene is widely regarded as the first woman historian in the Western tradition, and the Alexiad as a rare example of a medieval historical work written by a woman.\n\nAnna was the first-born child of Alexios I, educated in Greek classical literature, philosophy, and medicine at a level unprecedented for women of her era, and she expected to inherit the throne — a hope dashed by the birth of her brother John and dashed again by her unsuccessful attempt to seize power after her father's death. She retired to a convent, where she wrote the Alexiad as a memorial to her father and (she implies) a sublimation of her frustrated political ambitions. The work is a fascinating combination of filial piety and historical sophistication — her portrait of Alexios is idealised but detailed, and her descriptions of the First Crusade, the Norman invasions, and the Bogomil heresy are primary sources of exceptional value.\n\nThe Alexiad is particularly notable for its account of the First Crusade — Anna's perspective is distinctly Byzantine and Greek-educated, viewing the Latin crusaders with a mixture of admiration for their military prowess, contempt for their barbarity and bad faith, and concern for their impact on Byzantine imperial interests. Her description of Peter the Hermit's People's Crusade, the arrival of the crusading princes, and the negotiations between Alexios and the crusade leaders is an irreplaceable counterpoint to the Latin crusade chronicles.",
    "causes": [
      "Anna Komnene's retirement to a convent (c. 1118–1153) after the failure of her attempt to seize the throne — her brother John II's successful accession — gave her the time and the scholarly environment in which to write the Alexiad as a monument to her father and a compensation for her frustrated political career.",
      "The Byzantine imperial tradition of court historiography — the production of polished Greek prose chronicles celebrating and commemorating emperors — provided the literary model within which Anna was working, though her gender and her personal relationship with her subject give the Alexiad a distinctive character within the tradition.",
      "The reign of Alexios I (1081–1118) — which included the reconsolidation of Byzantine power after the catastrophic defeat at Manzikert (1071), the successful management of the First Crusade's passage through Byzantine territory, and the defeat of the Norman invasions — provided the historical material for a genuinely significant and complex work of history."
    ],
    "effects": [
      "The Alexiad is the primary source for Byzantine history during the reign of Alexios I — its detailed account of the First Crusade from the Byzantine perspective, the Norman invasions of Alexios's reign, and the Bogomil heresy provides irreplaceable primary source material that supplements and complicates the Latin crusade chronicles.",
      "Anna Komnene's authorship of the Alexiad established her as the first woman historian in the Western tradition — and a figure of particular fascination in the history of women's intellectual life, combining exceptional classical education, political ambition, frustrated power, and extraordinary literary achievement.",
      "The Alexiad's portrait of the First Crusade from the Byzantine perspective — viewing the crusaders as simultaneously useful allies and dangerous, uncontrollable barbarians — has significantly shaped modern historians' understanding of the complex relationship between Byzantium and the crusader states, and the fundamental divergence of Eastern and Western Christian cultures."
    ],
    "relationships": [
      {"sourceSlug": "anna-komnene", "sourceName": "Anna Komnene (1083–c. 1153)", "verb": "AUTHORS", "targetSlug": "alexiad", "targetName": "Alexiad (c. 1143–1153)", "context": "Anna Komnene wrote the Alexiad in her retirement in a Constantinople convent — the daughter of the emperor she is memorialising, writing in the elevated Greek classical style of Thucydides."},
      {"sourceSlug": "alexios-i-komnenos", "sourceName": "Alexios I Komnenos (r. 1081–1118)", "verb": "SUBJECT_OF", "targetSlug": "alexiad", "targetName": "Alexiad", "context": "The Alexiad chronicles the reign of Anna's father Alexios I — covering his accession, the Norman invasions, the First Crusade, and the Bogomil heresy."},
      {"sourceSlug": "alexiad", "sourceName": "Alexiad", "verb": "DESCRIBES", "targetSlug": "first-crusade", "targetName": "First Crusade (1095–1099)", "context": "The Alexiad is the primary Byzantine account of the First Crusade — describing the arrival of the Latin crusaders from the perspective of the Byzantine court that hosted and negotiated with them."}
    ],
    "places": [
      {"name": "Constantinople, Byzantine Empire (c. 1143–1153 CE, composition)", "role": "The place of composition — Anna wrote the Alexiad in a Constantinople convent after her retirement from political life"},
      {"name": "Byzantine Empire and Norman Kingdom (reign of Alexios I, 1081–1118)", "role": "The historical setting of the Alexiad — the Byzantine Empire under Alexios I, threatened by Norman invasions and transformed by the First Crusade's passage through its territory"}
    ],
    "subjects": ["Byzantine History", "Medieval Literature", "Medieval Era", "First Crusade", "Byzantine Empire", "Women's History", "Greek Literature", "Historiography"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Alexiad (Anna Komnene, c. 1143–1153) is the primary Byzantine source for the reign of Alexios I Komnenos and for the First Crusade from the Greek perspective — an irreplaceable counterpoint to the Latin crusade chronicles. As the work of the first woman historian in the Western tradition, written by the emperor's daughter who had expected to inherit the throne, it combines exceptional scholarship with personal stakes and political complexity unique in medieval historiography.",
      "significanceCategory": "highly-significant"
    }
  }
},

"anabasis-of-alexander-arrian": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781anabasis-of-alexander-arrian.json",
  "slug": "anabasis-of-alexander-arrian",
  "data": {
    "summary": "The Anabasis of Alexander (Greek: Ἀλεξάνδρου Ἀνάβασις, Alexandrou Anabasis, literally 'Alexander's Upward March') is the historical account of Alexander the Great's campaigns written by Arrian (Lucius Flavius Arrianus, c. 86–160 CE) — a Greek-speaking Roman senator and governor from Nicomedia in Bithynia who wrote the Anabasis as both a historical and literary monument to Alexander, using as his primary sources the lost eyewitness accounts of Ptolemy (later King of Egypt) and Aristobulus (a military engineer who served on the campaign). Written in a deliberately elevated Attic Greek style modelled on Xenophon's earlier Anabasis (the account of the Ten Thousand), it is the most detailed and reliable surviving ancient account of Alexander's campaigns from the crossing of the Hellespont (334 BCE) to his death in Babylon (323 BCE), and the primary modern source for the military history of Alexander's conquest of the Persian Empire, Egypt, Central Asia, and northern India.\n\nArrian wrote the Anabasis (c. 130–140 CE) some four and a half centuries after Alexander's campaigns, but his use of Ptolemy's eyewitness account — Ptolemy was a close companion of Alexander who had every reason to accurately record major military events, though also every reason to glorify his own role — gives it a measure of documentary authority that the other surviving Alexander sources (Diodorus, Curtius Rufus, Plutarch, Justin) generally lack. The Anabasis covers the seven books of Alexander's campaigns in systematic detail: the conquest of Asia Minor and Egypt, the great battles of the Granicus, Issus, and Gaugamela, the destruction of Persepolis, the campaigns in Bactria and Sogdiana (modern Afghanistan and Uzbekistan), the Indian campaign and the mutiny at the Hyphasis, the disastrous return march through Gedrosia, and Alexander's death.\n\nArrian's Anabasis has been the foundational modern source for Alexander since its revival in the Renaissance, and virtually every major modern biography of Alexander (Tarn, Bosworth, Green, Lane Fox) is primarily constructed from and in dialogue with Arrian's text. Its portrait of Alexander — brilliant, ruthless, driven by the desire to outdo Achilles and to reach the limits of the world — remains the most vivid and detailed ancient account of history's most celebrated conqueror.",
    "causes": [
      "Arrian's admiration for Alexander — and his explicit dissatisfaction with the existing Alexander historians he had read (Cleitarchus, the 'vulgate' tradition) for their sensationalism and inaccuracy — drove his decision to write a new history based on the more reliable primary sources of Ptolemy and Aristobulus.",
      "The Roman imperial literary culture of the 2nd century CE — the Hadrianic and Antonine 'Second Sophistic' movement of Greek literary revival, in which Greek-educated Romans wrote in elevated Attic Greek as a mark of cultural prestige — provided the literary context within which Arrian modelled himself on Xenophon and wrote the Anabasis as a self-conscious literary monument.",
      "The continuing fascination of the Roman imperial ruling class with Alexander the Great — who was the model figure of heroic kingship for Roman emperors from Caesar and Augustus through Trajan and Hadrian — gave Arrian's historical project cultural relevance: Alexander was not an antiquarian subject but the living model for imperial ambition."
    ],
    "effects": [
      "The Anabasis became the primary modern source for Alexander's campaigns — its systematic, detailed account of the military history, based on eyewitness Ptolemy, gave it an authority that the more dramatic but less reliable 'vulgate' tradition (Cleitarchus, Curtius, Diodorus) lacked, and virtually all modern Alexander biographies are built primarily on Arrian's framework.",
      "Arrian's portrait of Alexander — the combination of military genius, philosophical aspiration, increasing megalomania, and the tragic death in Babylon — shaped the Western and global image of Alexander the Great, making the Anabasis an indirect source for the Alexander legend that has fascinated rulers and conquerors from Julius Caesar and Augustus through Napoleon.",
      "The Anabasis inspired the tradition of 'following Alexander' — the physical retracing of Alexander's route — that runs from medieval pilgrims through 19th-century explorers and archaeologists (Alexander Burnes in Afghanistan) to Robin Lane Fox's modern Alexander biography (whose author participated in the filming of Oliver Stone's Alexander on horseback)."
    ],
    "relationships": [
      {"sourceSlug": "arrian", "sourceName": "Arrian (c. 86–160 CE)", "verb": "AUTHORS", "targetSlug": "anabasis-of-alexander-arrian", "targetName": "Anabasis of Alexander (c. 130–140 CE)", "context": "Arrian wrote the Anabasis using the lost eyewitness accounts of Ptolemy and Aristobulus as his primary sources — a deliberate choice to base his history on the most reliable available evidence."},
      {"sourceSlug": "anabasis-of-alexander-arrian", "sourceName": "Anabasis of Alexander", "verb": "CHRONICLES", "targetSlug": "alexander-the-great", "targetName": "Alexander the Great (356–323 BCE)", "context": "The Anabasis is the most detailed and reliable surviving ancient account of Alexander's campaigns — covering his conquests from the crossing of the Hellespont to his death in Babylon."},
      {"sourceSlug": "ptolemy-i-soter", "sourceName": "Ptolemy I Soter (c. 367–282 BCE)", "verb": "PRIMARY_SOURCE_FOR", "targetSlug": "anabasis-of-alexander-arrian", "targetName": "Anabasis of Alexander", "context": "Arrian's primary source was the lost eyewitness history of Ptolemy — Alexander's companion who later became King of Egypt — whose account gave the Anabasis a documentary authority the other Alexander sources lack."}
    ],
    "places": [
      {"name": "Roman Empire (c. 130–140 CE, composition)", "role": "The context of composition — Arrian wrote the Anabasis as a Roman senator and governor, in the literary culture of the 2nd-century CE Second Sophistic"},
      {"name": "Persian Empire, Egypt, Central Asia, and India (334–323 BCE, subject)", "role": "The geographic scope of Alexander's campaigns — from the Hellespont through Anatolia, Egypt, Persia, Bactria/Sogdiana, and to the Hyphasis river at the boundary of the known world"}
    ],
    "subjects": ["Greek History", "Classical Era", "Alexander the Great", "Military History", "Ancient Greece", "Hellenism", "Historiography", "Ancient Persia"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Anabasis of Alexander (Arrian, c. 130–140 CE) is the primary modern source for Alexander the Great's campaigns — the most detailed and reliable surviving ancient account, based on the lost eyewitness history of Ptolemy. Every major modern Alexander biography is constructed primarily from and in dialogue with Arrian's text, making it the foundational source for the historical record of one of history's most consequential conquerors.",
      "significanceCategory": "highly-significant"
    }
  }
},

"al-kutub-al-sittah": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780al-kutub-al-sittah.json",
  "slug": "al-kutub-al-sittah",
  "data": {
    "summary": "Al-Kutub al-Sittah (Arabic: الكتب الستة, 'The Six Books') are the six canonical collections of Hadith — the recorded sayings, actions, and tacit approvals of the Prophet Muhammad — recognised as authoritative by Sunni Islam. Compiled in the 9th century CE (approximately 200–270 AH), they are: Sahih al-Bukhari (compiled by Muhammad al-Bukhari, d. 870 CE), Sahih Muslim (Muslim ibn al-Hajjaj, d. 875 CE), Sunan al-Nasai, Sunan Abu Dawud, Sunan al-Tirmidhi, and Sunan Ibn Majah. Together with the Quran, the Six Books constitute the foundational sources of Sunni Islamic law (sharia) and theology, providing the prophetic precedents (Sunnah) that supplement the Quran's direct revelation in guiding Islamic practice across all domains of life — prayer, fasting, pilgrimage, marriage, inheritance, commerce, and governance.\n\nThe project of Hadith collection was a massive scholarly enterprise undertaken over several generations after the Prophet's death (632 CE) — the compilers travelled thousands of miles across the Islamic world interviewing transmitters, evaluating chains of transmission (isnad), and applying rigorous criteria to distinguish authentic reports from fabrications. Al-Bukhari's Sahih — widely regarded as the most authoritative Hadith collection in Sunni Islam, second only to the Quran itself — is said to have been compiled by al-Bukhari from approximately 600,000 examined Hadith, of which he accepted only 7,275 as meeting his stringent criteria of authenticity. The systematic science of Hadith criticism (ilm al-rijal, 'science of men' — evaluating the biographies and characters of transmitters) that the compilation of the Six Books required was one of the most sophisticated historical-critical enterprises of the medieval world.\n\nThe Six Books are the foundation of Islamic jurisprudence (fiqh) across all four major Sunni law schools (Hanafi, Maliki, Shafi'i, Hanbali) — providing the prophetic precedents that the jurists use to derive legal rulings. Their interpretation and the ongoing scholarly debate about the authenticity and application of specific Hadith remains one of the central intellectual activities of Islamic scholarship in the modern world, with significant implications for Muslim practice and law across the globe.",
    "causes": [
      "The death of the Prophet Muhammad (632 CE) and the rapid geographic expansion of Islam across the Middle East, North Africa, Persia, and Central Asia created an urgent need for reliable records of the Prophet's practice and sayings (Sunnah) to guide the rapidly growing Muslim community in matters where the Quran did not provide explicit guidance.",
      "The proliferation of fabricated Hadith — reports invented to support sectarian, political, or theological positions in the first two Islamic centuries — created the scholarly crisis that drove the systematic project of Hadith collection and verification, and the development of the sophisticated methodological apparatus (isnad criticism, biography of transmitters) that the Six Books represent.",
      "The institutionalisation of Islamic law in the Abbasid period (8th–9th centuries CE) — and the need for reliable prophetic precedents to ground the emerging legal schools' rulings — gave the project of canonical Hadith compilation its institutional support and urgency: the legal schools needed authoritative collections of Sunnah to anchor their jurisprudence."
    ],
    "effects": [
      "The Six Books became the foundational sources of Sunni Islamic jurisprudence — the prophetic precedents that the four major Sunni law schools draw on to derive legal rulings across all domains of Islamic life, making them the practical foundation of sharia law for approximately 1.5 billion Sunni Muslims worldwide.",
      "The science of Hadith criticism developed in the process of compiling the Six Books — the elaborate methodology of isnad analysis, transmitter biography (ilm al-rijal), and authenticity criteria — became one of the most sophisticated systems of historical-critical source evaluation in the medieval world, applied not just to religious texts but influencing Islamic historical methodology generally.",
      "The ongoing scholarly debate about the authenticity, interpretation, and contemporary application of Hadith in the Six Books — with reformist scholars questioning the binding authority of specific Hadith and traditionalist scholars defending the canonical collections — remains one of the most significant intellectual controversies in contemporary Islam, with direct implications for Muslim legal and political practice worldwide."
    ],
    "relationships": [
      {"sourceSlug": "muhammad-al-bukhari", "sourceName": "Muhammad al-Bukhari (810–870 CE)", "verb": "COMPILES", "targetSlug": "al-kutub-al-sittah", "targetName": "Al-Kutub al-Sittah (the Six Books)", "context": "Al-Bukhari's Sahih is the most authoritative of the Six Books — widely regarded as second only to the Quran in Sunni Islamic authority, compiled after examining approximately 600,000 Hadith."},
      {"sourceSlug": "al-kutub-al-sittah", "sourceName": "Al-Kutub al-Sittah", "verb": "GROUNDS", "targetSlug": "sunni-islam", "targetName": "Sunni Islamic jurisprudence (fiqh)", "context": "The Six Books provide the prophetic precedents (Sunnah) that ground Sunni Islamic law — the four major law schools (Hanafi, Maliki, Shafi'i, Hanbali) derive their legal rulings from the Quran and the Six Books."},
      {"sourceSlug": "al-kutub-al-sittah", "sourceName": "Al-Kutub al-Sittah", "verb": "COMPLEMENTS", "targetSlug": "quran", "targetName": "Quran", "context": "Together with the Quran, the Six Books constitute the two foundational sources of Sunni Islamic law and theology — the Quran as direct revelation and the Six Books as the record of prophetic practice (Sunnah)."}
    ],
    "places": [
      {"name": "Islamic world (9th century CE, Khorasan, Iraq, Arabia)", "role": "The geographic context of compilation — the Hadith scholars travelled across the Islamic world from Khorasan to Arabia to Iraq, collecting and verifying reports from transmitters"},
      {"name": "Global Sunni Islam (ongoing influence)", "role": "The sphere of the Six Books' authority — as the foundational Hadith collections of Sunni Islam, they guide the practice of approximately 1.5 billion Sunni Muslims worldwide"}
    ],
    "subjects": ["Islam", "Islamic Law", "Classical Era", "Hadith", "Sunni Islam", "Islamic Scholarship", "Religious Texts", "Middle East"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Al-Kutub al-Sittah (the Six Books of Hadith, compiled 9th century CE) are the foundational collections of prophetic practice for Sunni Islam — second only to the Quran as sources of Islamic law and theology. As the ground of sharia jurisprudence for approximately 1.5 billion Sunni Muslims, they are among the most practically consequential religious texts in world history. The sophisticated historical-critical methodology developed for Hadith evaluation was one of the most advanced source-critical systems in the medieval world.",
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
