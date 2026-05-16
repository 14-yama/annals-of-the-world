#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 37 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: hexameter, book-of-discipline,
          alcmeonis, clarel,
          a-feast-for-crows, anarchist-symbolism,
          hedonic-regression, metabolic-control-analysis
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-37-may2026"

ENRICHMENTS = {

"hexameter": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780hexameter.json",
  "slug": "hexameter",
  "data": {
    "summary": "Hexameter (from Greek ἑξάμετρον, 'six measures') is the oldest and most prestigious metrical form in Greek and Latin poetry — a dactylic verse metre consisting of six feet, where each foot is either a dactyl (one long syllable followed by two short syllables, — ∪ ∪) or a spondee (two long syllables, — —), with the fifth foot almost always a dactyl and the sixth foot always a spondee or trochee. Hexameter is the metre of Homer's Iliad and Odyssey (8th century BCE), Hesiod's Theogony and Works and Days, Apollonius of Rhodes's Argonautica, and Virgil's Aeneid and Georgics — the metre in which the foundational epic narratives of Greek and Roman civilisation were composed and transmitted. The specific pattern ∪ ∪ / — ∪ ∪ / — ∪ ∪ / — ∪ ∪ / — ∪ ∪ / — × was known in antiquity as the 'heroic metre' (versus heroicus) because it was identified as the metre of heroic epic narrative.\n\nThe hexameter's origins are disputed — it may derive from an early Greek oral poetic tradition that predates the Linear B script, possibly from a merger of shorter metrical units, or it may have been imported from an early Near Eastern metrical tradition. Its quantitative character — founded on the distinction between long and short syllables rather than the stress-accent patterns of Germanic and modern European prosody — made it fundamentally different from the accentual-syllabic metres that dominate modern European poetry. When Latin poets adapted hexameter (Ennius, c. 239–169 BCE, was the first to use it systematically in Latin), they adapted the quantitative Greek system to the Latin language, creating the tradition of Latin quantitative verse that dominated Roman literary culture and influenced medieval Latin poetry.\n\nHexameter was used not only for epic but for didactic poetry (Hesiod, Lucretius, Virgil's Georgics), hymns (the Homeric Hymns), oracle verse (the Delphic Oracle's responses were traditionally in hexameter), and philosophical poetry (Empedocles, Lucretius). The hexameter's long history — from Homer to Virgil to the medieval Latin tradition, and to ambitious modern adaptations (Longfellow's Evangeline, 1847, in English hexameter) — makes it the most historically consequential metrical form in Western literary tradition.",
    "causes": [
      "The ancient Greek oral poetic tradition — the tradition of professional bards (aoidoi) who composed and performed epic narratives for aristocratic audiences, using the formulaic composition techniques identified by Milman Parry and Albert Lord — required a flexible, long-line metre that could accommodate formulaic phrases of varying length, and hexameter with its dactyl/spondee substitution system provided exactly this flexibility.",
      "The quantitative prosodic system of ancient Greek and Latin — founded on the distinction between long and short syllables (rather than stress accent) — determined the character of hexameter as a quantitative metre: the long/short contrast is the fundamental building block of the dactylic foot and of the entire system of Greek and Latin verse.",
      "The cultural prestige of Homer — whose Iliad and Odyssey were the foundational texts of Greek education, culture, and literary tradition — ensured that hexameter acquired and maintained the highest prestige as the metre of serious literary composition: any poet who wished to write in the tradition of Homer had to use hexameter."
    ],
    "effects": [
      "Hexameter's adoption by Latin poets — beginning with Ennius's Annales (c. 170 BCE) and reaching its highest development in Virgil's Aeneid — created the Roman epic tradition and established hexameter as the prestige metre of Roman literary culture, ensuring its transmission through the medieval Latin tradition to the humanist and neo-Latin poetry of the Renaissance.",
      "The hexameter's role as the metre of the Homeric epics ensured that it was the primary vehicle for the transmission of Homeric narrative to subsequent Greek and Roman culture — the metrical form was inseparable from the content it carried, and the ability to compose in hexameter was a marker of literary education and cultural competence in classical antiquity.",
      "The long hexameter line's structural features — its six-foot length, its rhythmic variety (the dactyl/spondee substitution), its characteristic caesurae (pauses within the line) — provided the templates for the analysis of ancient Greek and Latin prosody, and the comparative study of hexameter across Greek and Latin epic was foundational for the development of classical philology."
    ],
    "relationships": [
      {"sourceSlug": "hexameter", "sourceName": "Dactylic hexameter (Homer, Virgil)", "verb": "USED_IN", "targetSlug": "iliad", "targetName": "Iliad (Homer, c. 750 BCE)", "context": "The Iliad is the primary and oldest surviving major text in dactylic hexameter — the foundational text of the Homeric tradition and the source of hexameter's prestige as the 'heroic metre'."},
      {"sourceSlug": "hexameter", "sourceName": "Dactylic hexameter (Latin adaptation)", "verb": "ADOPTED_BY", "targetSlug": "aeneid", "targetName": "Aeneid (Virgil, 19 BCE)", "context": "Virgil's Aeneid is the supreme achievement of Latin hexameter — the adaptation of the Greek quantitative metre to Latin by Ennius, Lucretius, and Virgil created the Roman epic tradition."},
      {"sourceSlug": "hexameter", "sourceName": "Hexameter (Delphic Oracle verse)", "verb": "USED_IN", "targetSlug": "delphic-oracle", "targetName": "Delphic Oracle (Pythia's prophetic responses)", "context": "The Delphic Oracle's responses were traditionally delivered in hexameter — extending the metre's prestige beyond epic poetry to divine prophecy and establishing it as the metre of elevated religious utterance."}
    ],
    "places": [
      {"name": "Ancient Greece (origin, Homeric tradition, 8th century BCE)", "role": "Hexameter originated in the ancient Greek oral poetic tradition — the dactylic hexameter of Homer's Iliad and Odyssey (c. 750–700 BCE) is the earliest and most prestigious surviving evidence of the metre"},
      {"name": "Rome (Latin adaptation, Ennius, Virgil, 2nd century BCE–1st century BCE)", "role": "Roman poets adapted hexameter to Latin — Ennius (c. 239–169 BCE) first systematised Latin hexameter, and Virgil brought it to its highest development in the Aeneid, ensuring its transmission through the medieval Latin tradition"}
    ],
    "subjects": ["Classical Literature", "Ancient Era", "Greek Poetry", "Latin Poetry", "Prosody", "Homer", "Epic Poetry", "Literary Form"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Dactylic hexameter is the foundational metrical form of Western literary tradition — the metre of Homer's Iliad and Odyssey, Hesiod, Virgil's Aeneid, and Lucretius. Its identification as the 'heroic metre' in antiquity ensured its prestige for over a millennium, and its adaptation by Roman poets (Ennius, Virgil) created the Latin epic tradition transmitted through medieval Latin literature to the Renaissance and beyond.",
      "significanceCategory": "highly-significant"
    }
  }
},

"book-of-discipline": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781book-of-discipline.json",
  "slug": "book-of-discipline",
  "data": {
    "summary": "The Book of Discipline (First Book of Discipline, 1560; Second Book of Discipline, 1578) is a pair of foundational constitutional documents of the Church of Scotland — drafted by a commission of six ministers headed by John Knox (c. 1514–1572) during the Scottish Reformation — that established the doctrine, governance, and social programme of the reformed Church of Scotland. The First Book of Discipline (1560), drafted by Knox and his colleagues immediately after the Scottish Reformation Parliament formally broke with Rome (August 1560), is one of the most ambitious religious-social documents of the Protestant Reformation: it proposed not only a Presbyterian church government (replacing bishops with a system of ministers, superintendents, elders, and deacons) but a comprehensive national programme of education (a school in every parish, a grammar school in every town, a college in every major city, and universities to educate the ministry) and social welfare (provision for the poor from church revenues). While never formally adopted by the Scottish Parliament (the nobility who had seized church lands resisted the proposal to fund education and poor relief from those revenues), the First Book of Discipline was enormously influential in shaping the reformed Church of Scotland's character.\n\nThe Second Book of Discipline (1578), drafted primarily by Andrew Melville (1545–1622) — Knox's successor as the leading Scottish Reformed theologian — went further in establishing the Presbyterian principle of church governance: it articulated the doctrine of the 'two kingdoms' (the spiritual kingdom of Christ, governed by the Church through Scripture, and the civil kingdom, governed by the magistrate through natural law) that became the foundation of Scottish Presbyterian political theology, and it rejected episcopacy (rule by bishops) as contrary to Scripture. The Second Book of Discipline was the foundational document of the Presbyterian church government that the Church of Scotland eventually adopted in 1592.\n\nTogether, the two Books of Discipline represent the most systematic attempt of any Reformed church to establish a comprehensive vision of the Christian society — combining church governance, education, social welfare, and the relationship between church and state into a unified constitutional framework. Their influence extended beyond Scotland to Reformed churches in England (the Puritan tradition) and the Netherlands.",
    "causes": [
      "The Scottish Reformation Parliament's formal break with Rome in August 1560 — which abolished papal authority, forbade the celebration of Mass, and established Protestantism as the national religion — created the immediate need for the constitutional framework of the reformed Church: the First Book of Discipline was drafted within months of the Reformation Parliament to provide this framework.",
      "John Knox's Geneva training under John Calvin — his experience of the Geneva church's disciplined, Reformed social order, which Knox called 'the most perfect school of Christ that ever was in the earth since the days of the Apostles' — provided the model for the First Book of Discipline's vision of a comprehensive Reformed Christian society governed by Scripture.",
      "Andrew Melville's intellectual formation in France and Geneva — his contact with the most advanced Reformed theology of the later 16th century — gave the Second Book of Discipline its more rigorous Presbyterian ecclesiology (the doctrine of the equality of all ministers, the rejection of episcopacy, the two kingdoms doctrine) that shaped the Presbyterian tradition."
    ],
    "effects": [
      "The First Book of Discipline's educational programme — a school in every parish, a grammar school in every town, universities for the ministry — became the aspirational model for Scottish education that, over the following two centuries, produced Scotland's extraordinary rate of literacy and educational participation, contributing to the Scottish Enlightenment and Scotland's reputation as a highly educated society.",
      "The Second Book of Discipline's Presbyterian ecclesiology — the rejection of episcopacy, the doctrine of the two kingdoms, the system of Kirk Sessions, Presbyteries, and General Assembly — became the constitutional framework of the Church of Scotland after 1592, and was transplanted to England through the Puritan movement, where it became the foundation of English Presbyterianism and, via the Westminster Assembly (1643), of the Westminster Confession and Directory.",
      "The Books of Discipline's doctrine of the two kingdoms — the church's independence from civil authority in spiritual matters, and the civil magistrate's obligation to support the true church — became the foundational principle of Scottish Presbyterian political theology, and its assertion of the church's right to discipline and correct the civil magistrate (including the monarch) had profound implications for the development of Scottish political thought and constitutional theory."
    ],
    "relationships": [
      {"sourceSlug": "john-knox", "sourceName": "John Knox (c. 1514–1572)", "verb": "DRAFTS", "targetSlug": "book-of-discipline", "targetName": "First Book of Discipline (1560)", "context": "Knox led the commission that drafted the First Book of Discipline in 1560 — the foundational constitutional document of the reformed Church of Scotland, proposing church governance, a national education system, and poor relief."},
      {"sourceSlug": "book-of-discipline", "sourceName": "Books of Discipline (Scottish Presbyterian ecclesiology)", "verb": "ESTABLISHES", "targetSlug": "presbyterian-church-governance", "targetName": "Presbyterian church governance (Kirk Sessions, Presbyteries, General Assembly)", "context": "The First and Second Books of Discipline established the Presbyterian system of church governance — the hierarchy of minister, elder, deacon, Kirk Session, Presbytery, and General Assembly — that became the constitutional framework of the Church of Scotland."},
      {"sourceSlug": "book-of-discipline", "sourceName": "Book of Discipline (two kingdoms doctrine)", "verb": "INFLUENCES", "targetSlug": "westminster-confession", "targetName": "Westminster Confession (1646)", "context": "The Second Book of Discipline's Presbyterian ecclesiology and two kingdoms doctrine influenced the Westminster Assembly (1643) and the Westminster Confession (1646) — extending the Scottish Presbyterian tradition to English and American Calvinist churches."}
    ],
    "places": [
      {"name": "Edinburgh, Scotland (Scottish Reformation Parliament, August 1560)", "role": "The First Book of Discipline was drafted in Edinburgh immediately after the Scottish Reformation Parliament (August 1560) broke with Rome — the constitutional framework of the reformed Church of Scotland produced at the founding moment of Scottish Protestantism"},
      {"name": "Scotland (national education and church governance programme)", "role": "The Books of Discipline established the constitutional framework for the Church of Scotland across the entire nation — the parish school system, the church courts (Kirk Sessions, Presbyteries, General Assembly), and the social welfare programme"}
    ],
    "subjects": ["Scottish Reformation", "Early Modern Era", "John Knox", "Presbyterian Church", "Scottish History", "Education", "Church Governance", "Protestant Reformation"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Books of Discipline (1560, 1578) are the foundational constitutional documents of the reformed Church of Scotland — proposing a comprehensive vision of the Christian society that combined Presbyterian church governance, a national education system, and social welfare. The First Book of Discipline's educational programme shaped Scotland's high literacy and the Scottish Enlightenment; the Second Book's Presbyterian ecclesiology influenced the Westminster Confession and Calvinist churches worldwide.",
      "significanceCategory": "highly-significant"
    }
  }
},

"alcmeonis": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782alcmeonis.json",
  "slug": "alcmeonis",
  "data": {
    "summary": "The Alcmeonis (Greek: Ἀλκμαιωνίς, Alkmaiōnis) is a lost ancient Greek epic poem dealing with the myth of Alcmaeon — the hero who killed his mother Eriphyle to avenge his father Amphiaraus (the seer who was killed in the battle of the Seven Against Thebes after his wife Eriphyle had bribed to reveal his hiding place) — and is one of the poems of the Greek Epic Cycle, the corpus of epic poems by various ancient Greek authors that supplemented and extended the Homeric narrative of the Trojan War and the myths of the heroic age. The Alcmeonis survives only in fragments — a few lines preserved in quotations by Athenaeus and other ancient authors — and its authorship, date, and exact scope are uncertain, though ancient sources attribute it to Abas or to anonymous Corinthian authorship, and it is generally dated to the 7th or early 6th century BCE.\n\nThe myth of Alcmaeon — the matricide hero, the subsequent madness (Erinyes-driven) visited on him for killing his mother, his wandering in search of purification, and his eventual death — was one of the most important mythological complexes of ancient Greece, explored by Sophocles (his lost Alcmaeon plays), Euripides (Alcmaeon in Psophidis and Alcmaeon in Corinth — the latter the last play he composed before his death), and Callimachus. The story of the Epigoni (the sons of the Seven Against Thebes, who successfully sacked Thebes in the second expedition) and of Alcmaeon's subsequent career as a wandering hero persecuted by the Erinyes for matricide were major subjects of the cyclic epics beyond the Alcmeonis itself.\n\nThe Alcmeonis is significant as evidence for the Greek Epic Cycle's broader scope — the cyclic epics treated not only the Trojan War mythology but the full range of the heroic age myths (Heracles, Theban cycle, Argonautic cycle), demonstrating the comprehensive narrative ambition of the early Greek epic tradition. Its loss, alongside the other cyclic epics (Cypria, Aethiopis, Little Iliad, Iliupersis, Nostoi, Telegony), is one of the major losses of ancient Greek literature.",
    "causes": [
      "The Greek mythological tradition's rich complex of Theban myths — the Seven Against Thebes, the Epigoni, the curse on the house of Oedipus and the linked curse on the house of Amphiaraus — provided the narrative material from which the Alcmeonis was composed: the matricide of Alcmaeon is the culminating act of the Argive/Theban mythological cycle.",
      "The Greek Epic Cycle's tradition of composing supplementary epics to fill the narrative gaps left by Homer — the cyclic poets composed epics treating the full range of the Trojan War and heroic age mythology, from the judgement of Paris to the death of Odysseus — created the literary context for the Alcmeonis as one of the non-Trojan epics that completed the heroic age narrative.",
      "The ancient Greek cultural concern with the moral paradox of the matricide hero — the conflict between the obligation to avenge one's father and the prohibition against killing one's mother, the subsequent pollution and madness, and the quest for purification — gave the Alcmaeon myth its moral and theological depth, making it a major subject for tragic as well as epic treatment."
    ],
    "effects": [
      "The Alcmaeon myth as treated in the Alcmeonis and related cyclic epics provided the narrative material for the tragic treatments of Alcmaeon — Sophocles' and Euripides' Alcmaeon plays (now lost), and Euripides' Alcmaeon in Corinth (his last play) — demonstrating the cyclic epics' role as sources for the Athenian tragic tradition.",
      "The Alcmeonis's preservation in fragments — quoted by Athenaeus and others — is evidence for the broader pattern of ancient Greek text transmission, in which the cyclic epics survived only in fragments while Homer's Iliad and Odyssey were preserved complete, reflecting the educational and cultural prestige of the Homeric texts over the cyclic tradition.",
      "The Alcmeonis and the other cyclic epics represent an irreplaceable loss for our knowledge of ancient Greek literature — their absence means that large sections of the heroic age mythology that were common knowledge in classical Athens survive only in summary (Proclus's Chrestomathia) and scattered quotations, creating significant gaps in the reconstruction of the narrative tradition."
    ],
    "relationships": [
      {"sourceSlug": "alcmeonis", "sourceName": "Alcmeonis (Greek cyclic epic, 7th/6th century BCE)", "verb": "PART_OF", "targetSlug": "greek-epic-cycle", "targetName": "Greek Epic Cycle (cyclic epics beyond Homer)", "context": "The Alcmeonis is one of the non-Trojan epics of the Greek Epic Cycle — treating the Theban mythological tradition (Alcmaeon, the Epigoni) rather than the Trojan War, demonstrating the cycle's comprehensive coverage of the heroic age."},
      {"sourceSlug": "alcmeonis", "sourceName": "Alcmeonis (Alcmaeon matricide myth)", "verb": "PROVIDES_MATERIAL_FOR", "targetSlug": "euripides-alcmaeon", "targetName": "Euripides' Alcmaeon plays (Alcmaeon in Psophidis, Alcmaeon in Corinth)", "context": "The Alcmaeon myth treated in the Alcmeonis provided material for the tragic tradition — Euripides composed two Alcmaeon plays, Alcmaeon in Corinth being his last work, demonstrating the cyclic epics' role as sources for Athenian tragedy."},
      {"sourceSlug": "alcmeonis", "sourceName": "Alcmeonis (lost cyclic epic)", "verb": "SURVIVES_AS", "targetSlug": "greek-epic-cycle-fragments", "targetName": "Fragments of the Greek Epic Cycle", "context": "The Alcmeonis survives only in fragments — a few lines quoted by Athenaeus and others — representing the pattern of cyclic epic loss that left most of the ancient Greek literary tradition accessible only through fragments and summaries."}
    ],
    "places": [
      {"name": "Ancient Greece (Corinthian attribution, 7th/6th century BCE)", "role": "The Alcmeonis is attributed by ancient sources to Corinthian authorship — suggesting its composition in the Corinthian cultural sphere, though the date and authorship are uncertain"},
      {"name": "Athens and the Greek world (tragic tradition, 5th century BCE)", "role": "The Alcmaeon myth treated in the Alcmeonis was well known in classical Athens — Sophocles and Euripides both composed Alcmaeon tragedies — demonstrating the cyclic epics' influence on the Athenian tragic tradition"}
    ],
    "subjects": ["Ancient Greek Literature", "Ancient Era", "Greek Epic Cycle", "Greek Mythology", "Theban Cycle", "Lost Literature", "Classical Greece", "Epic Poetry"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "The Alcmeonis is one of the lost poems of the Greek Epic Cycle — a fragment-surviving ancient Greek epic treating the Alcmaeon/matricide myth of the Theban mythological tradition. Its loss, alongside the other cyclic epics, represents one of the major gaps in ancient Greek literary transmission. It provided material for the tragic tradition (Euripides' Alcmaeon plays) and is evidence for the comprehensive narrative scope of the early Greek epic tradition beyond Homer.",
      "significanceCategory": "regional"
    }
  }
},

"clarel": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782clarel.json",
  "slug": "clarel",
  "data": {
    "summary": "Clarel: A Poem and Pilgrimage in the Holy Land is an epic poem by Herman Melville (1819–1891), published in two volumes by G. P. Putnam's Sons in 1876 — the longest poem in American literary history at approximately 18,000 lines in 150 cantos of short rhyming verse, and one of the most theologically ambitious works in American literature. Clarel is a narrative poem following a young American theological student (Clarel) on a pilgrimage through Palestine and the Middle East — Jerusalem, the Dead Sea, Bethlehem, the Mar Saba monastery — in the company of a diverse group of pilgrims representing the full range of 19th-century attitudes toward faith, doubt, and the meaning of the Holy Land: the Wandering Jew Nehemiah, the disillusioned Rolfe (often read as Melville's self-portrait), the atheist Ungar, the Syrian monk Mortmain, and others.\n\nClarel was composed over a period of sixteen years (1857–1876), following Melville's own journey to the Holy Land in 1857 — a journey undertaken after the commercial and critical failure of his later prose works (Pierre, The Confidence-Man) had left him financially and professionally marginalised. The poem is Melville's sustained meditation on the crisis of faith in the 19th century — the intellectual challenge of Darwinism, the Higher Criticism of the Bible, and the modern scientific worldview to traditional Christian belief — set in the landscape of the Holy Land, where the physical evidence of the Biblical narrative (stripped of its mythological weight by geological and archaeological investigation) generates the poem's central tension between faith and doubt.\n\nClarel was a commercial failure on publication (the edition of 350 copies was largely unsold) and remained obscure for nearly a century — it was not republished until 1960 (the Northwestern-Newberry edition), and critical attention to it developed primarily in the late 20th century. It is now recognised as one of the major American poems of the 19th century — a work of extraordinary intellectual ambition that engages the theological and philosophical crises of the Victorian era in the genre of the long philosophical poem.",
    "causes": [
      "Melville's journey to the Holy Land in January–February 1857 — which he undertook in a state of psychological exhaustion and spiritual crisis following the professional failures of his later prose works — provided the experiential foundation of Clarel: his journals from the journey record the impressions of desolation, barrenness, and disappointed expectation that pervade the poem.",
      "The 19th-century crisis of faith — the intellectual challenge of Darwin's On the Origin of Species (1859), the German Higher Criticism of the Bible (Strauss, Renan), and the growing conflict between scientific materialism and traditional Christian belief — provided the central intellectual content of Clarel: the poem is a sustained dramatic dialogue among different responses to the loss of religious certainty.",
      "The American long poem tradition — particularly the ambition to write a major philosophical epic in the tradition of Milton's Paradise Lost and Dante's Divine Comedy — provided the literary model for Clarel's extraordinary scope: Melville's ambition to write the definitive American meditation on faith and doubt required the epic form."
    ],
    "effects": [
      "Clarel's near-complete commercial failure and obscurity from 1876 to 1960 is itself significant as evidence of the limits of the long philosophical poem in 19th-century American literary culture — the reading public that consumed Longfellow and Tennyson had no appetite for Melville's theologically dense epic, and the poem's rediscovery required the transformation of American literary scholarship.",
      "Clarel's recovery and critical reassessment in the late 20th century — the Northwestern-Newberry edition (1960) and subsequent critical attention — contributed to the broader reassessment of Melville's late career (from the commercial Melville of Typee and Moby-Dick to the reclusive poet of the late period) and to the recognition of his significance as a philosophical poet.",
      "Clarel's sustained engagement with the crisis of faith in the 19th century — its dramatic representation of the full range of responses from orthodox faith to scientific atheism — makes it one of the most comprehensive literary documents of the Victorian intellectual crisis, comparable in its theological depth and range to Tennyson's In Memoriam and Matthew Arnold's Dover Beach."
    ],
    "relationships": [
      {"sourceSlug": "herman-melville", "sourceName": "Herman Melville (1819–1891)", "verb": "AUTHORS", "targetSlug": "clarel", "targetName": "Clarel: A Poem and Pilgrimage in the Holy Land (1876)", "context": "Melville published Clarel in 1876 — the longest poem in American literary history, a 16-year composition composed after his 1857 Holy Land journey, his sustained meditation on the Victorian crisis of faith."},
      {"sourceSlug": "clarel", "sourceName": "Clarel (Holy Land pilgrimage, Victorian faith crisis)", "verb": "ENGAGES_WITH", "targetSlug": "victorian-crisis-of-faith", "targetName": "Victorian crisis of faith (Darwinism, Higher Criticism)", "context": "Clarel is Melville's sustained meditation on the 19th-century crisis of faith — the intellectual challenge of Darwinism, the Higher Criticism of the Bible, and scientific materialism to Christian belief, set in the landscape of the Holy Land."},
      {"sourceSlug": "clarel", "sourceName": "Clarel (philosophical long poem)", "verb": "PART_OF", "targetSlug": "american-long-poem-tradition", "targetName": "American long poem tradition (Whitman, Longfellow, Crane)", "context": "Clarel is Melville's contribution to the tradition of the American long philosophical poem — an 18,000-line meditation on faith and doubt that is the longest poem in American literary history, comparable in ambition to Whitman's Leaves of Grass."}
    ],
    "places": [
      {"name": "Palestine/Holy Land (Jerusalem, Dead Sea, Bethlehem, Mar Saba, pilgrimage setting)", "role": "The Holy Land — Jerusalem, the Dead Sea, the Judean wilderness, the Mar Saba monastery — is the physical and spiritual landscape of Clarel: the barrenness of the landscape embodies the poem's central tension between the promises of the Biblical narrative and the desolation of historical reality"},
      {"name": "New York City (publication 1876, Melville's home)", "role": "Clarel was published by G. P. Putnam's Sons in New York in 1876 — in a first edition of 350 copies, largely unsold, during Melville's obscure final decades as an inspector of customs in New York"}
    ],
    "subjects": ["American Literature", "Modern Era", "Herman Melville", "Epic Poetry", "Victorian Religion", "19th Century", "Pilgrimage", "Crisis of Faith"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Clarel (Melville, 1876) is the longest poem in American literary history — an 18,000-line meditation on the Victorian crisis of faith, set in the Holy Land, that is one of the most theologically ambitious works in American literature. Obscure for nearly a century after its publication, its recovery and reassessment in the late 20th century revealed it as a major document of 19th-century intellectual and spiritual history.",
      "significanceCategory": "significant"
    }
  }
},

"a-feast-for-crows": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783a-feast-for-crows.json",
  "slug": "a-feast-for-crows",
  "data": {
    "summary": "A Feast for Crows is the fourth novel in George R. R. Martin's A Song of Ice and Fire epic fantasy series, published on 17 October 2005 by Bantam Books — after a five-year gap following A Storm of Swords (2000), the longest between volumes in the series to that point. A Feast for Crows covers only half of the characters and storylines from A Storm of Swords (those in Westeros and the immediate vicinity), while its companion volume A Dance with Dragons (2011) covers the parallel timeline of the other characters (Daenerys in Essos, Jon Snow at the Wall, Tyrion's exile). This structural split — necessitated by the manuscript's massive size — resulted in A Feast for Crows focusing primarily on Cersei Lannister's troubled regency in King's Landing, Jaime Lannister's western campaign, Arya Stark's training in Braavos, Sansa Stark's situation in the Vale, and Samwell Tarly's journey to the Citadel.\n\nA Feast for Crows is notable in the series for its psychological depth — particularly its extended, complex portrayal of Cersei Lannister's point-of-view chapters, in which she emerges from a secondary antagonist into one of the most fully realised and morally complex characters in the series. The novel's Cersei chapters — depicting her paranoid misrule of King's Landing, her growing alienation from her allies, her fateful manipulation of the Faith Militant, and her catastrophic miscalculations — provide the most sustained psychological portrait in A Song of Ice and Fire of a character whose downfall is entirely self-generated. The empowerment of the Faith Militant, which Cersei uses as a weapon against her enemies, becomes the instrument of her own humiliation (the Walk of Shame, which concludes the novel).\n\nA Feast for Crows was widely reviewed on publication as slower and less satisfying than A Storm of Swords — its absence of the Jon, Daenerys, and Tyrion characters frustrated readers who expected the narrative momentum of the previous volume. It is better understood as a sustained character study of Westeros in the aftermath of the War of the Five Kings — a landscape of political exhaustion, institutional transformation (the rise of the Faith Militant, the Iron Bank's growing power), and the beginning of the long winter.",
    "causes": [
      "The manuscript's massive size — Martin's fourth volume grew beyond the scope of a single book, requiring the split between A Feast for Crows (covering half the characters) and A Dance with Dragons (covering the other half in a parallel timeline) — creating the structural peculiarity of A Feast for Crows as a volume that tells only half the story of its own period.",
      "The narrative need to develop the aftermath of the War of the Five Kings — the political vacuum left by Joffrey's assassination, Tywin Lannister's death, and Robb Stark's destruction — created the space for A Feast for Crows' focus on the transformation of Westerosi politics: Cersei's misrule, the rise of the Faith Militant, and the Iron Islands succession crisis.",
      "Martin's increasing interest in the psychological complexity of characters previously presented primarily as antagonists — particularly Cersei and Jaime Lannister — drove A Feast for Crows' shift in narrative focus from action-driven plot (the battles and assassinations of A Storm of Swords) to character-driven psychological portraiture."
    ],
    "effects": [
      "A Feast for Crows' Cersei Lannister chapters established her as one of the most complex and fully realised characters in the series — her misrule of King's Landing and her self-destructive manipulation of the Faith Militant culminating in the Walk of Shame (Season 5, one of the most discussed scenes of the HBO series) transformed her from villain to a figure of tragic complexity.",
      "The Faith Militant arc introduced in A Feast for Crows — the resurgence of militant religious zealotry in King's Landing under the High Sparrow — became one of the major storylines of the later HBO series, contributing to the series' sustained exploration of the relationship between religious authority and political power.",
      "A Feast for Crows' five-year publication gap (2000–2005) established the pattern of long waits between A Song of Ice and Fire volumes — A Dance with Dragons (2011) followed another six-year gap — that became one of the defining (and most frequently discussed) features of the series, contributing to the fan culture of speculation and frustration around the unfinished series."
    ],
    "relationships": [
      {"sourceSlug": "george-r-r-martin", "sourceName": "George R. R. Martin (born 1948)", "verb": "AUTHORS", "targetSlug": "a-feast-for-crows", "targetName": "A Feast for Crows (2005)", "context": "Martin published A Feast for Crows in 2005 — five years after A Storm of Swords — covering half the characters and storylines, with the parallel A Dance with Dragons covering the other half in the same timeline."},
      {"sourceSlug": "a-feast-for-crows", "sourceName": "A Feast for Crows (Cersei Lannister focus)", "verb": "PART_OF", "targetSlug": "a-song-of-ice-and-fire", "targetName": "A Song of Ice and Fire (Martin series, 1996–)", "context": "A Feast for Crows is the fourth volume of A Song of Ice and Fire — notable for its psychological depth and its extended portrayal of Cersei Lannister's misrule of King's Landing and the rise of the Faith Militant."},
      {"sourceSlug": "a-feast-for-crows", "sourceName": "A Feast for Crows (Faith Militant, Walk of Shame)", "verb": "ADAPTED_AS", "targetSlug": "game-of-thrones-season-5", "targetName": "Game of Thrones Season 5 (HBO, 2015)", "context": "The Faith Militant arc and Cersei's Walk of Shame were adapted in Game of Thrones Season 5 — the Walk of Shame scene (directed by David Nutter) became one of the most discussed scenes in the series."}
    ],
    "places": [
      {"name": "King's Landing (Cersei's regency, Faith Militant, central focus)", "role": "King's Landing is the primary location of A Feast for Crows — Cersei's misrule of the capital, the empowerment of the Faith Militant, and the Walk of Shame dominate the Westerosi half of the narrative"},
      {"name": "Braavos and the Iron Islands (Arya's training, Kingsmoot)", "role": "Arya Stark's training at the House of Black and White in Braavos and the Iron Islands' Kingsmoot succession crisis are the major secondary storylines of A Feast for Crows outside King's Landing"}
    ],
    "subjects": ["Fantasy Fiction", "Modern Era", "George R. R. Martin", "Epic Fantasy", "21st Century", "American Literature", "Television Adaptation", "Political Fiction"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "A Feast for Crows (Martin, 2005) is the fourth volume of A Song of Ice and Fire — notable for its psychological depth and its establishment of Cersei Lannister as one of the most complex characters in the series. Its five-year publication gap and the structural split with A Dance with Dragons defined the pattern of long waits that became a defining feature of the unfinished series. The Faith Militant arc and the Walk of Shame became major story elements in the HBO adaptation.",
      "significanceCategory": "significant"
    }
  }
},

"anarchist-symbolism": {
  "filepath": "data/appwrite-export/entities/784-Class-784/784anarchist-symbolism.json",
  "slug": "anarchist-symbolism",
  "data": {
    "summary": "Anarchist symbolism encompasses the visual and symbolic tradition of the anarchist political movement — including the circled A (⊕, the most widely recognised anarchist symbol, composed of the letter A inside a circle, representing 'Anarchy is Order', attributed to Pierre-Joseph Proudhon's formulation 'La propriété, c'est le vol' and Mikhail Bakunin's circle); the black flag (the primary symbolic colour of anarchism, representing the negation of state authority, adopted from the Black Banner of the Carbonari and peasant revolts); the red-and-black flag (bicolour of anarcho-syndicalism, combining the red of socialism with the black of anarchism); and associated symbols (the black cat, adopted from the Industrial Workers of the World — the 'sabo-cat' of Emma Goldman and IWW labour action). These symbols have been used by anarchist movements since the mid-19th century as markers of political identity and as tools of agitation and propaganda.\n\nThe circled A — the most universally recognised anarchist symbol — was popularised in the 1960s–1970s, particularly through the punk movement, where it appeared on clothing, album covers (the Sex Pistols' visual identity), and walls worldwide. The punk movement's adoption of anarchist aesthetics (the DIY ethos, the rejection of mainstream culture, the 'anarchy' of the Sex Pistols' 'Anarchy in the U.K.', 1976) transformed the circled A from a specifically political symbol of the anarchist movement into a broader symbol of counter-cultural rebellion, anti-authoritarianism, and youthful resistance to established order — making it one of the most widely reproduced political symbols of the late 20th century.\n\nAnarchist symbolism reflects the broader visual culture of 19th and 20th-century radical politics — alongside the red flag and five-pointed star of socialism, the hammer and sickle of communism, and the raised fist of labour, anarchist symbols represent the visual repertoire of the political left. The circled A's particular capacity to cross from specifically anarchist politics into broader counter-cultural use (punk, graffiti, street art, global justice movement) demonstrates its extraordinary cultural mobility.",
    "causes": [
      "The 19th-century anarchist movement's need for political symbols — Pierre-Joseph Proudhon's first systematic articulation of anarchism (What is Property?, 1840) and the subsequent anarchist movements of Bakunin, Kropotkin, and Goldman required symbolic markers of political identity and distinguishability from socialist and communist movements that shared the red flag tradition.",
      "The Industrial Workers of the World (IWW)'s labour organising tradition — which developed the 'sabo-cat' (black cat) as a symbol of sabotage and direct action in the early 20th century — contributed the black cat to the anarchist symbolic repertoire, embedding anarchist symbols in the American labour movement.",
      "The punk movement's adoption of anarchist aesthetics in the mid-1970s — particularly the Sex Pistols' 'Anarchy in the U.K.' (1976) and the circled A's appearance on punk clothing and album covers — globalised the circled A beyond specifically anarchist political contexts into the broader counter-cultural imagination, making it one of the most reproduced political symbols of the late 20th century."
    ],
    "effects": [
      "The punk movement's adoption and globalisation of the circled A made anarchist symbolism one of the most widely recognised political symbol systems in the world — the circled A appears on walls, clothing, and digital spaces worldwide as a marker of anti-authoritarianism and counter-cultural identity, far exceeding the reach of specifically anarchist political movements.",
      "Anarchist symbolism's presence in global protest movements — the 1999 Seattle WTO protests, the Occupy movement (2011), and subsequent global justice and anti-austerity movements — demonstrates the continued vitality of anarchist symbols as markers of direct-action, anti-institutional politics across different political contexts.",
      "The black flag's adoption as anarchism's primary colour — and its influence on the visual culture of punk, metal, and counter-cultural aesthetics — has made black the colour most associated with anti-authoritarian, counter-cultural, and nihilistic political and aesthetic stances in Western popular culture."
    ],
    "relationships": [
      {"sourceSlug": "anarchist-symbolism", "sourceName": "Anarchist symbolism (circled A, black flag)", "verb": "ASSOCIATED_WITH", "targetSlug": "anarchism", "targetName": "Anarchist political movement (Proudhon, Bakunin, Kropotkin)", "context": "The circled A, black flag, and red-and-black flag are the primary visual symbols of the anarchist political movement — developed from the mid-19th century as markers of anarchist identity distinguishable from socialist and communist movements."},
      {"sourceSlug": "anarchist-symbolism", "sourceName": "Anarchist symbolism (circled A, punk movement)", "verb": "ADOPTED_BY", "targetSlug": "punk-movement", "targetName": "Punk movement (Sex Pistols, 1976)", "context": "The punk movement's adoption of the circled A — particularly through the Sex Pistols' 'Anarchy in the U.K.' and punk visual aesthetics — globalised the symbol beyond specifically anarchist politics into the broader counter-cultural imagination."},
      {"sourceSlug": "anarchist-symbolism", "sourceName": "Anarchist symbolism (black cat, IWW)", "verb": "DEVELOPED_BY", "targetSlug": "industrial-workers-of-the-world", "targetName": "Industrial Workers of the World (IWW, 'sabo-cat')", "context": "The IWW developed the black cat ('sabo-cat') as a symbol of sabotage and direct action in the early 20th century — embedding anarchist symbols in the American labour movement and contributing to the broader anarchist symbolic repertoire."}
    ],
    "places": [
      {"name": "Europe and North America (19th–20th century anarchist movements)", "role": "Anarchist symbolism developed in the context of European and North American anarchist movements — from Proudhon's Paris and Bakunin's Geneva to the IWW's Chicago and the Spanish anarcho-syndicalist movement"},
      {"name": "Global (punk movement globalisation, 1970s–present)", "role": "The punk movement's globalisation of the circled A from the late 1970s onwards — through music, clothing, and street art — made anarchist symbolism a worldwide counter-cultural presence"}
    ],
    "subjects": ["Political Symbolism", "Modern Era", "Anarchism", "Political History", "Visual Culture", "Punk Movement", "Labour History", "Counter-culture"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Anarchist symbolism — the circled A, black flag, red-and-black bicolour — is one of the most widely recognised political symbol systems of the modern era. The punk movement's adoption of the circled A in the 1970s globalised anarchist aesthetics beyond specifically political contexts, making them markers of counter-cultural identity worldwide. Anarchist symbols continue to appear in global protest movements as markers of anti-authoritarian, direct-action politics.",
      "significanceCategory": "significant"
    }
  }
},

"hedonic-regression": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785hedonic-regression.json",
  "slug": "hedonic-regression",
  "data": {
    "summary": "Hedonic regression (also hedonic price method or hedonic pricing model) is an econometric method for measuring the value of specific attributes or characteristics of goods by analysing the prices of differentiated products — based on the hedonic hypothesis (attributed to the economist Andrew Court, 1939, and systematically developed by Zvi Griliches, 1961, and Sherwin Rosen, 1974) that the price of a good is a function of its constituent characteristics, and that the implicit prices of these characteristics can be estimated by regressing the observed market prices on the characteristics. The method was originally developed to create quality-adjusted price indices for automobiles and other differentiated goods, and has been most influentially applied in the measurement of housing prices (decomposing house prices into the values of location, size, construction quality, neighbourhood characteristics, school district quality, and proximity to amenities and disamenities) and technology goods (particularly computers, where rapid quality improvement makes traditional price indices misleading).\n\nThe theoretical foundation of hedonic regression was provided by Sherwin Rosen's 1974 paper 'Hedonic Prices and Implicit Markets: Product Differentiation in Pure Competition' (Journal of Political Economy) — which established the microeconomic theory of hedonic prices as equilibrium outcomes of a two-sided market for differentiated goods, deriving the implicit price functions (hedonic price functions) as equilibrium loci rather than supply or demand curves. Rosen's model showed that the hedonic price regression gives the envelope of consumers' bid functions and producers' offer functions in the market for characteristics, providing the theoretical foundation for welfare analysis of quality change.\n\nHedonic regression is used by statistical agencies worldwide (the US Bureau of Labor Statistics, the UK Office for National Statistics, Eurostat) to construct quality-adjusted price indices for computers, telecommunications equipment, housing, and other goods where rapid quality change would distort traditional fixed-basket price indices. The US national accounts (GDP) use hedonic price indices for computers and software — creating significant adjustments to measured economic growth that have been controversial (critics argue that hedonic adjustment overstates real economic growth by assuming quality improvements are fully valued by consumers) but are now standard practice in national accounting.",
    "causes": [
      "The challenge of measuring price changes for differentiated goods — particularly automobiles (Andrew Court, 1939) and computers (where a personal computer in 1983 and 2003 are both called 'computers' but have radically different capabilities) — motivated the development of hedonic methods for constructing quality-adjusted price indices that could separate genuine price changes from quality improvements.",
      "Sherwin Rosen's theoretical synthesis (1974) — which provided the microeconomic foundation for interpreting hedonic price regression as equilibrium outcomes of markets for characteristics — transformed hedonic regression from an empirical technique into a theoretically grounded economic tool with welfare analysis applications.",
      "The adoption of hedonic price indices by the US Bureau of Labor Statistics and the Bureau of Economic Analysis for computers and software in the 1980s–1990s — following the Boskin Commission's (1996) recommendation that traditional price indices significantly overstated inflation — institutionalised hedonic methods in national accounts and made them central to the measurement of economic growth and productivity."
    ],
    "effects": [
      "Hedonic price indices for computers — showing extremely rapid price declines (adjusted for quality improvement, computer prices fell approximately 20–25% per year in the 1980s–1990s) — contributed substantially to the measured productivity acceleration of the US economy in the 1990s (the 'IT productivity miracle') by increasing measured real investment in information technology.",
      "The hedonic method's application to housing markets — decomposing house prices into the implicit values of location, size, and neighbourhood characteristics — has been one of the most productive applications in applied econometrics, with applications to environmental valuation (the value of clean air, proximity to parks), school quality capitalisation, and urban economics.",
      "The widespread use of hedonic price indices in official statistics has generated methodological controversy — critics argue that hedonic adjustment systematically overstates real economic growth by assuming that measured quality improvements are fully valued by consumers, and that the subjective element in attribute valuation makes hedonic indices non-comparable across time and across countries."
    ],
    "relationships": [
      {"sourceSlug": "hedonic-regression", "sourceName": "Hedonic regression (Rosen 1974, Griliches 1961)", "verb": "THEORISED_BY", "targetSlug": "sherwin-rosen", "targetName": "Sherwin Rosen (1974, hedonic price theory)", "context": "Rosen's 1974 Journal of Political Economy paper provided the microeconomic theory of hedonic prices as equilibrium outcomes of markets for characteristics — establishing the theoretical foundation for hedonic regression as a tool for welfare analysis and quality-adjusted price measurement."},
      {"sourceSlug": "hedonic-regression", "sourceName": "Hedonic regression (quality-adjusted price indices)", "verb": "APPLIED_BY", "targetSlug": "us-bureau-of-labor-statistics", "targetName": "US Bureau of Labor Statistics (CPI, quality adjustment)", "context": "The US BLS and Bureau of Economic Analysis use hedonic price indices for computers, software, and other technology goods — making hedonic methods central to the official measurement of US economic growth and the Consumer Price Index."},
      {"sourceSlug": "hedonic-regression", "sourceName": "Hedonic regression (housing market analysis)", "verb": "APPLIED_TO", "targetSlug": "housing-economics", "targetName": "Housing market analysis and environmental valuation", "context": "Hedonic regression is one of the most widely used tools in housing economics — decomposing house prices into the implicit values of location, size, neighbourhood, and amenities, with applications to environmental valuation and school quality measurement."}
    ],
    "places": [
      {"name": "United States (BLS, BEA, Boskin Commission, national accounts application)", "role": "The US was the primary context for the development and institutionalisation of hedonic price indices — the US Bureau of Labor Statistics and Bureau of Economic Analysis adopted hedonic methods for computers and software following the Boskin Commission recommendations"},
      {"name": "Global (Eurostat, OECD, international statistical agencies)", "role": "Hedonic methods have been adopted by statistical agencies worldwide — Eurostat, the OECD, and national statistical offices use hedonic price indices for information technology goods as recommended by international guidelines"}
    ],
    "subjects": ["Econometrics", "Modern Era", "Price Indices", "Housing Economics", "National Accounts", "Applied Economics", "Statistical Methods", "Technology Economics"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Hedonic regression (Griliches 1961, Rosen 1974) is a foundational econometric method for quality-adjusted price measurement — central to the construction of official price indices for technology goods and housing. Its adoption by the US BLS and BEA contributed to the measured IT productivity miracle of the 1990s and has transformed national accounting. Its application to housing markets has made it one of the most productive tools in applied environmental and urban economics.",
      "significanceCategory": "significant"
    }
  }
},

"metabolic-control-analysis": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785metabolic-control-analysis.json",
  "slug": "metabolic-control-analysis",
  "data": {
    "summary": "Metabolic Control Analysis (MCA) is a mathematical framework for quantifying how the control of metabolic fluxes (the rates of biochemical reactions) and concentrations of metabolic intermediates is distributed among the enzymes and transporters in a metabolic pathway. MCA was developed independently and almost simultaneously by Henrik Kacser and James A. Burns (University of Edinburgh, 1973) and by Reinhart Heinrich and Tom Rapoport (Humboldt University Berlin, 1974), with Kacser and Burns's paper 'The Control of Flux' (Symposia of the Society for Experimental Biology, 1973) and Heinrich and Rapoport's paper 'A Linear Steady-State Treatment of Enzymatic Chains' (European Journal of Biochemistry, 1974) as the foundational publications. MCA provides a precise quantitative framework for analysing metabolic systems that superseded the earlier intuition that metabolism was controlled by a single 'rate-limiting step'.\n\nThe central concepts of MCA are the control coefficients: the flux control coefficient (the relative change in flux through a pathway in response to a relative change in the activity of a specific enzyme) and the concentration control coefficient (the relative change in the concentration of a metabolite in response to a relative change in enzyme activity). The summation theorem — a fundamental result of MCA stating that the flux control coefficients of all enzymes in a pathway sum to exactly 1 — shows that control of a metabolic flux is not concentrated in a single rate-limiting enzyme but is distributed among all enzymes in proportion to their individual flux control coefficients. In most real metabolic systems, control is distributed, with no single enzyme having exclusive control.\n\nMCA has been widely applied in biochemistry, systems biology, and metabolic engineering — the rational design of cells and organisms for biotechnological applications (production of pharmaceutical compounds, biofuels, or food ingredients by engineered microorganisms). The framework's quantitative tools for identifying which enzymes are the primary control points of a metabolic pathway are central to metabolic engineering strategies for increasing the production of desired metabolites. MCA is also a foundational framework of systems biology — the quantitative, system-level approach to biological complexity that emerged in the late 1990s.",
    "causes": [
      "The inadequacy of the rate-limiting step concept in biochemistry — the intuition that metabolism was controlled by a single enzyme (the 'bottleneck' or 'rate-limiting step') that set the pace for the entire pathway — motivated Kacser/Burns and Heinrich/Rapoport to develop MCA as a quantitative framework that could replace this intuition with rigorous analysis showing that control is typically distributed among multiple enzymes.",
      "The availability of enzyme kinetics data and the development of computational methods for analysing systems of nonlinear differential equations (the biochemical kinetics of metabolic pathways) provided the technical foundation for MCA — the framework's mathematical tools (sensitivity analysis, summation theorems, connectivity theorems) required both theoretical biochemistry and computational analysis.",
      "The growing importance of metabolic engineering — the rational manipulation of microbial metabolism for biotechnological purposes — created applied demand for quantitative methods like MCA that could identify the optimal targets for enzyme overexpression or deletion to increase the production of desired metabolites."
    ],
    "effects": [
      "MCA's summation theorem — showing that flux control is distributed among all enzymes rather than concentrated in a single rate-limiting step — fundamentally changed biochemistry's understanding of metabolic regulation, replacing the misleading rate-limiting step concept with a quantitative framework for analysing distributed control.",
      "MCA became a foundational framework of metabolic engineering — the rational design of microbial cells for biotechnological production — providing quantitative tools for identifying the primary control points of metabolic pathways and optimising the distribution of enzyme activities for maximal production of desired metabolites.",
      "MCA's concepts and formalism were integrated into the broader programme of systems biology in the late 1990s — contributing to the quantitative, system-level approach to biological complexity that characterises modern computational biology and the analysis of metabolic networks in the context of genomics and proteomics."
    ],
    "relationships": [
      {"sourceSlug": "metabolic-control-analysis", "sourceName": "MCA (Kacser/Burns 1973, Heinrich/Rapoport 1974)", "verb": "DEVELOPED_BY", "targetSlug": "henrik-kacser", "targetName": "Henrik Kacser and James Burns (University of Edinburgh, 1973)", "context": "Kacser and Burns developed MCA at the University of Edinburgh in 1973 — their paper 'The Control of Flux' established the flux control coefficient and summation theorem, showing that metabolic control is distributed rather than concentrated in a rate-limiting step."},
      {"sourceSlug": "metabolic-control-analysis", "sourceName": "MCA (flux control coefficients, summation theorem)", "verb": "APPLIED_IN", "targetSlug": "metabolic-engineering", "targetName": "Metabolic engineering (biotechnology, bioproduction)", "context": "MCA provides quantitative tools for identifying the primary control points of metabolic pathways — central to metabolic engineering strategies for increasing the production of desired metabolites in engineered microorganisms."},
      {"sourceSlug": "metabolic-control-analysis", "sourceName": "MCA (quantitative systems analysis)", "verb": "CONTRIBUTES_TO", "targetSlug": "systems-biology", "targetName": "Systems biology (quantitative, systems-level biology)", "context": "MCA's quantitative framework for analysing metabolic systems was integrated into systems biology in the late 1990s — contributing to the computational analysis of metabolic networks and the quantitative, systems-level approach to biological complexity."}
    ],
    "places": [
      {"name": "University of Edinburgh (Kacser/Burns, 1973, UK)", "role": "MCA was developed simultaneously at the University of Edinburgh by Henrik Kacser and James Burns — their 1973 paper 'The Control of Flux' is one of the two foundational publications of the field"},
      {"name": "Humboldt University Berlin (Heinrich/Rapoport, 1974, Germany)", "role": "MCA was independently developed at Humboldt University Berlin by Reinhart Heinrich and Tom Rapoport — their 1974 paper established the same mathematical framework from a different perspective, providing the dual founding of the field"}
    ],
    "subjects": ["Biochemistry", "Modern Era", "Systems Biology", "Metabolic Engineering", "Mathematical Biology", "Enzymology", "Biotechnology", "Quantitative Biology"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Metabolic Control Analysis (Kacser/Burns 1973, Heinrich/Rapoport 1974) is a foundational framework of quantitative biochemistry — replacing the rate-limiting step concept with rigorous analysis showing that metabolic control is distributed among multiple enzymes. Its summation theorem is one of the key theoretical results of biochemistry, and its application in metabolic engineering and systems biology has made it central to modern biotechnology and computational biology.",
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
