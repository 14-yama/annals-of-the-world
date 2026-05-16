#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 32 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: haggadah, grimms-fairy-tales, gospel-of-judas,
          corpus-juris-civilis, computing-machinery-and-intelligence-1950,
          ainiakbari, anna-karenina, and-quiet-flows-the-don
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-32-may2026"

ENRICHMENTS = {

"haggadah": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780haggadah.json",
  "slug": "haggadah",
  "data": {
    "summary": "The Passover Haggadah (Hebrew: הַגָּדָה, 'the telling') is the Jewish liturgical text that prescribes the order of the Passover Seder — the ritual meal conducted on the eve of Passover (14 Nisan) in which Jewish families retell the story of the Exodus from Egypt, fulfilling the biblical commandment of Exodus 13:8 ('You shall tell your son on that day: It is because of what the LORD did for me when I came out of Egypt'). The Haggadah is not a single authored text but a composite liturgical compilation that reached something like its current form during the Geonic period (c. 600–1000 CE), incorporating biblical passages, Talmudic interpretations, Midrashic expansions, the four questions (Ma Nishtana), the account of the ten plagues, the songs Dayenu and Chad Gadya, and the meal itself. With over 3,500 printed editions documented (more than any other Jewish book), the Haggadah is the most widely produced Jewish religious text after the Bible.\n\nThe Seder (Hebrew: 'order') structures the Passover evening through a specific liturgical sequence of 15 steps — from the opening Kadesh (sanctification) through the Maggid (the telling of the Exodus story), the meal, and the concluding songs — designed to involve all participants, especially children (who ask the four questions: 'Why is this night different from all other nights?'). The Haggadah's pedagogy is explicitly intergenerational: the obligation is to retell the Exodus story 'as if you yourself came out of Egypt', creating an experiential identification with the liberation narrative across generations. The three matzot, the four cups of wine, the bitter herbs (maror), and the Seder plate are ritual objects that embody the theological meanings of the Passover narrative.\n\nThe Haggadah's historical significance lies both in its liturgical function — sustaining Jewish identity through two millennia of diaspora by annually reenacting the founding liberation narrative — and in its extraordinary adaptability: every generation and community has produced its own Haggadah (the Maxwell House Haggadah, distributed in America since 1932; the Kibbutz Haggadah; the feminist Haggadah; the anti-slavery Haggadah) tailored to its specific social and theological concerns.",
    "causes": [
      "The biblical commandment to retell the Exodus story to one's children (Exodus 13:8, Deuteronomy 6:20–25) — which establishes the obligation of intergenerational narrative transmission of the liberation story — is the foundational religious imperative from which the Haggadah derives its liturgical form and its characteristic question-and-answer pedagogy.",
      "The destruction of the Second Temple (70 CE) and the subsequent restructuring of Jewish religious life — the shift from the sacrificial cult of the Temple to the home-centred, text-based rabbinic Judaism of the Diaspora — transformed the Passover sacrifice into the Passover Seder, and the Mishnah's tractate Pesachim (c. 200 CE) provided the first systematic outline of the Seder that became the basis of the Haggadah.",
      "The Diaspora condition of Jewish life — the experience of living as a minority under foreign rule, whether in Babylonia, Rome, medieval Europe, or the modern world — gave the Passover Haggadah its recurring political resonance: the Exodus story of liberation from slavery was annually re-experienced as a narrative of hope and identity by communities that often lived under conditions of oppression and discrimination."
    ],
    "effects": [
      "The Passover Seder is the most widely practised Jewish ritual worldwide — observed by more Jews than any other Jewish religious practice — and the Haggadah's annual retelling of the Exodus has been the primary vehicle for the transmission of Jewish identity and historical memory across two thousand years of Diaspora.",
      "The Haggadah's influence on political liberation movements has been substantial — its imagery has been adopted by African American civil rights activists (the connection between the Passover liberation narrative and the African American experience of slavery and liberation is explicit in the spirituals 'Go Down, Moses', 'Let My People Go'), by feminist theologians, by Jewish socialists, and by every group that has identified with the Exodus narrative of liberation from oppression.",
      "The extraordinary diversity of Haggadah editions — over 3,500 documented printed versions — is a testament to the text's adaptability and its capacity to incorporate the concerns of every generation and community: the Maxwell House Haggadah (used by most American Jews for the 20th century), the feminist Haggadah, the Kibbutz Haggadah, and the environmentalist Haggadah all represent the living tradition of Jewish liturgical creativity."
    ],
    "relationships": [
      {"sourceSlug": "haggadah", "sourceName": "Passover Haggadah (composite text, c. 600–1000 CE)", "verb": "RETELLS", "targetSlug": "exodus", "targetName": "Book of Exodus (Passover liberation narrative)", "context": "The Haggadah is the liturgical vehicle for the annual retelling of the Exodus narrative — its Maggid section incorporates biblical texts, Talmudic interpretations, and Midrashic expansions of the Exodus story in the form of a pedagogical dialogue."},
      {"sourceSlug": "haggadah", "sourceName": "Passover Haggadah", "verb": "STRUCTURES", "targetSlug": "passover-seder", "targetName": "Passover Seder (most widely practised Jewish ritual)", "context": "The Haggadah prescribes the 15-step Seder order — from Kadesh through Maggid to the concluding songs — structuring the ritual meal that is the most widely practised Jewish religious observance worldwide."},
      {"sourceSlug": "haggadah", "sourceName": "Passover Haggadah (liberation narrative)", "verb": "INSPIRES", "targetSlug": "african-american-civil-rights", "targetName": "African American civil rights movement ('Let My People Go')", "context": "The Passover liberation narrative has been foundational for African American spiritual and civil rights rhetoric — 'Go Down, Moses', 'Let My People Go', and the connection between slavery in Egypt and the American slave experience runs through the entire African American religious and political tradition."}
    ],
    "places": [
      {"name": "Jewish Diaspora (worldwide, 70 CE–present)", "role": "The Passover Seder has been conducted in every country of the Jewish Diaspora for two thousand years — from Babylon and Rome through medieval Europe, North Africa, and the Americas to the modern world — the most geographically dispersed and temporally continuous ritual in human religious history"},
      {"name": "Land of Israel / modern Israel (Passover origin and return)", "role": "The Haggadah concludes with 'Next year in Jerusalem!' — the annual expression of hope for return to the Land of Israel that sustained Diaspora Jewish identity for two millennia and which took on new meaning with the establishment of the State of Israel in 1948"}
    ],
    "subjects": ["Judaism", "Classical Era", "Passover", "Jewish Liturgy", "Hebrew Bible", "Ritual", "Jewish History", "Liberation"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Passover Haggadah is the most widely practised Jewish ritual text — with over 3,500 printed editions, it is the most produced Jewish book after the Bible. The Passover Seder has transmitted Jewish identity and the Exodus liberation narrative across two thousand years of Diaspora, and its liberation imagery has inspired civil rights movements from the African American spiritual tradition to contemporary human rights advocacy.",
      "significanceCategory": "world-changing"
    }
  }
},

"grimms-fairy-tales": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780grimms-fairy-tales.json",
  "slug": "grimms-fairy-tales",
  "data": {
    "summary": "Grimms' Fairy Tales (German: Kinder- und Hausmärchen, 'Children's and Household Tales') is the collection of fairy tales and folk narratives compiled by the brothers Jacob Grimm (1785–1863) and Wilhelm Grimm (1786–1859), first published in two volumes (1812 and 1815) and revised through seven editions (the final edition in 1857) — one of the best-known and most influential works in the Western literary tradition, with the tales translated into over 160 languages and the collection one of the most widely distributed books in history after the Bible. The 1857 edition contains 211 tales, including the most famous fairy tales in the Western canon: Cinderella, Snow White, Rapunzel, Rumpelstiltskin, Hansel and Gretel, Little Red Riding Hood, Sleeping Beauty, The Frog Prince, and dozens of others.\n\nGrimms' Fairy Tales was presented by the brothers as the rescue of authentic German folk tradition — the collection of oral tales from German peasants and rural storytellers. This claim of authenticity has been substantially revised by subsequent scholarship: many of the tales were contributed by middle-class, often French-influenced informants (including the Hessian storyteller Dorothea Viehmann and the Hassenpflug family), and the tales were heavily edited and revised across editions — with earlier, more violent and sexually explicit versions gradually softened and moralised to suit a family readership. The 'authentic folk tale' was in significant part a literary construction of Romantic nationalism.\n\nThe psychological and cultural significance of Grimms' Fairy Tales has been enormous — Bruno Bettelheim's The Uses of Enchantment (1976) argued that fairy tales use archetypal symbolic narratives to help children work through fundamental psychological conflicts, and this psychoanalytic interpretation has shaped a century of scholarship on fairy tales. The tales' recurring motifs — the wicked stepmother, the youngest of three brothers, the magical helper, the forest as liminal space, the prince's kiss — have been identified as universal archetypes by structuralist folklorists (Vladimir Propp's Morphology of the Folktale) and Jungian psychologists.",
    "causes": [
      "German Romantic nationalism — the Romantic movement's celebration of Volk (folk/people) culture as the authentic expression of national character, and the nationalist response to Napoleonic occupation that sought to discover and preserve a distinctively German cultural heritage — gave the Grimms their project: the salvage of oral folk tradition as a monument of German national identity.",
      "Jacob Grimm's linguistic and philological work — his development of Grimm's Law (the systematic description of consonant shifts between Proto-Indo-European and Germanic languages), which laid the foundation for comparative linguistics — and his partnership with Wilhelm in the scholarly tradition of German Romanticism gave the Fairy Tales collection its intellectual context: the folk tale was understood as a linguistic and cultural fossil preserving archaic Germanic heritage.",
      "The development of the children's book market in 19th-century Europe — the growing commercial demand for wholesome, morally improving children's literature — drove the progressive softening and moralisation of the Grimm tales through successive editions, transforming the original collection (which included explicit sexual and violent content) into the family-appropriate text that became the standard."
    ],
    "effects": [
      "Grimms' Fairy Tales established the Western fairy tale canon — its versions of Cinderella, Snow White, Sleeping Beauty, Rapunzel, and Hansel and Gretel are the versions that shaped all subsequent cultural retellings, adaptations, and Disney films, and the Grimm versions have effectively displaced the earlier Perrault versions in popular consciousness.",
      "The Grimm tales' influence on 20th-century popular culture through the Disney animated features (Snow White, 1937; Cinderella, 1950; Sleeping Beauty, 1959; Rapunzel/Tangled, 2010) and their subsequent adaptations has been incalculable — the Walt Disney Company's identity is substantially built on the Grimm fairy tale foundation.",
      "The scholarly and psychoanalytic interpretation of fairy tales — from Freudian readings of the tales' sexual symbolism to Bruno Bettelheim's account of their therapeutic function for children to Vladimir Propp's structuralist analysis — was generated primarily by the Grimm collection, making the Fairy Tales the primary corpus for the academic study of narrative structure and folklore."
    ],
    "relationships": [
      {"sourceSlug": "jacob-grimm", "sourceName": "Jacob Grimm (1785–1863) and Wilhelm Grimm (1786–1859)", "verb": "COMPILES", "targetSlug": "grimms-fairy-tales", "targetName": "Grimms' Fairy Tales (Kinder- und Hausmärchen, 1812–1857)", "context": "The Grimm brothers collected, edited, and revised their fairy tales through seven editions (1812–1857), transforming oral folk tradition and literary sources into the canonical Western fairy tale collection."},
      {"sourceSlug": "grimms-fairy-tales", "sourceName": "Grimms' Fairy Tales", "verb": "ESTABLISHES", "targetSlug": "western-fairy-tale-canon", "targetName": "Western fairy tale canon (Cinderella, Snow White, Rapunzel, etc.)", "context": "The Grimm versions of Cinderella, Snow White, Sleeping Beauty, Rapunzel, and Hansel and Gretel are the canonical versions that shaped all subsequent retellings, Disney adaptations, and popular cultural versions of these tales."},
      {"sourceSlug": "grimms-fairy-tales", "sourceName": "Grimms' Fairy Tales", "verb": "INFLUENCES", "targetSlug": "disney-animated-features", "targetName": "Walt Disney's animated features (Snow White 1937, Cinderella 1950, etc.)", "context": "Walt Disney's foundational animated features — Snow White (1937), Cinderella (1950), Sleeping Beauty (1959) — are directly based on Grimm tales, making the Grimm collection the foundation on which the Disney cultural empire was partly built."}
    ],
    "places": [
      {"name": "Kassel, Germany (1812 first edition, Grimms' primary work location)", "role": "Kassel was the Grimms' primary location during the collection of the Fairy Tales — where they received informants and worked as librarians at the court of King Jerome of Westphalia during the Napoleonic period"},
      {"name": "Global (160+ languages, one of the most distributed books in history)", "role": "Grimms' Fairy Tales has been translated into over 160 languages and is one of the most widely distributed books in history — its reach into virtually every literary culture makes it the most globally pervasive work of European folk literature"}
    ],
    "subjects": ["German Literature", "Modern Era", "Folklore", "Fairy Tales", "Children's Literature", "Romanticism", "19th Century", "World Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Grimms' Fairy Tales (1812–1857) established the Western fairy tale canon — translated into over 160 languages and one of the most widely distributed books in history. The Grimm versions of Cinderella, Snow White, Sleeping Beauty, Rapunzel, and Hansel and Gretel shaped all subsequent retellings and Disney adaptations. The collection is the primary corpus for the academic study of narrative structure, folklore, and the psychological function of fairy tales.",
      "significanceCategory": "world-changing"
    }
  }
},

"gospel-of-judas": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780gospel-of-judas.json",
  "slug": "gospel-of-judas",
  "data": {
    "summary": "The Gospel of Judas is a Gnostic text purporting to record secret conversations between Jesus and Judas Iscariot in the days before the Crucifixion, known to exist from the church father Irenaeus of Lyon's criticism of it c. 180 CE but lost until a fragmentary Coptic manuscript (Codex Tchacos) was discovered in Egypt c. 1970 and eventually published by National Geographic in April 2006 following its conservation and scholarly analysis. The text presents Judas not as the betrayer of Jesus but as his most favoured disciple — the only apostle who truly understands Jesus's cosmic mission — and his 'betrayal' is reinterpreted as fulfilling Jesus's own instruction: 'You will sacrifice the man who clothes me' (referring to Jesus's physical body), enabling the liberation of Jesus's divine spirit from its material imprisonment.\n\nThe Gospel of Judas represents one of the most radical revisions of the canonical passion narrative in Gnostic Christianity — its theological framework is dualistic, viewing the material world as the creation of a lower, ignorant deity (the Demiurge) and the physical body as a prison for the divine spark within. In this framework, death is liberation and the Crucifixion is a positive event enabling the escape of Jesus's divine spirit from bodily imprisonment. The canonical Judas — the quintessential betrayer, whose name became synonymous with treachery in Western culture — is transformed into a heroic, enlightened disciple acting at his master's instruction.\n\nThe Gospel of Judas's 2006 publication generated enormous public interest and media coverage — it was presented as a potentially revolutionary revision of Christian origins that would force a reassessment of Judas's role in the Passion narrative. Subsequent scholarship has been more cautious: the text is a 2nd-century Gnostic composition that reflects the diversity of early Christian interpretation rather than any historical information about the historical Judas, but its publication significantly raised public awareness of Gnostic Christianity and the diversity of early Christian texts beyond the canonical New Testament.",
    "causes": [
      "The Gnostic Christian tradition's revisionary relationship to the canonical Gospels — its practice of producing alternative 'secret' accounts of Jesus's teaching (gospels attributed to Thomas, Mary, Philip, Judas) that presented the Gnostic interpretation of salvation as the hidden inner teaching that Jesus imparted only to his enlightened disciples — generated the Gospel of Judas as part of this broader Gnostic literary production.",
      "Irenaeus of Lyon's critique (c. 180 CE) — in Against Heresies, his systematic refutation of Gnostic Christianity — is the earliest evidence that the Gospel of Judas existed, and his description of it (Cainites who 'produce a fictitious history which they style the Gospel of Judas') provides the earliest external reference to the text's existence and its Gnostic theological context.",
      "The discovery and eventual publication of the Codex Tchacos — the Egyptian papyrus codex containing the Gospel of Judas, which was found c. 1970 and passed through various hands before its eventual conservation and publication by National Geographic in 2006 — provided the modern evidence for a text that had been lost for approximately 1,700 years."
    ],
    "effects": [
      "The Gospel of Judas's 2006 publication significantly raised public awareness of Gnostic Christianity and the diversity of early Christian texts — it demonstrated once again (following the 1945 Nag Hammadi discoveries and the publication of the Gospel of Thomas) that the canonical New Testament represented the victory of one form of Christianity over many competing alternatives.",
      "The text's rehabilitation of Judas as a heroic figure acting at Jesus's instruction has influenced a variety of scholarly and popular reassessments of the Judas figure — from Elaine Pagels's and Karen King's scholarly commentary to popular fiction and film treatments — contributing to a broader cultural reassessment of the canonical Passion narrative's traditional villains.",
      "The Gospel of Judas's media coverage — particularly National Geographic's presentation of it as potentially revolutionary — generated significant public discussion about the relationship between the canonical Gospels and the non-canonical texts of early Christianity, contributing to the broader cultural phenomenon of popular interest in 'lost gospels' and alternative Christian origins."
    ],
    "relationships": [
      {"sourceSlug": "gospel-of-judas", "sourceName": "Gospel of Judas (c. 2nd century CE)", "verb": "PART_OF", "targetSlug": "gnostic-christianity", "targetName": "Gnostic Christian literary tradition (Nag Hammadi texts)", "context": "The Gospel of Judas is part of the Gnostic Christian literary tradition that produced alternative accounts of Jesus's teaching for audiences within the diverse early Christian movement — known from Irenaeus's critique c. 180 CE and rediscovered in the Codex Tchacos."},
      {"sourceSlug": "gospel-of-judas", "sourceName": "Gospel of Judas (rehabilitation of Judas)", "verb": "REVISES", "targetSlug": "judas-iscariot", "targetName": "Judas Iscariot (canonical betrayer figure)", "context": "The Gospel of Judas transforms Judas from the canonical betrayer into Jesus's most enlightened disciple who acts on his master's instruction — a radical revision of the figure whose name became synonymous with treachery in Western culture."},
      {"sourceSlug": "gospel-of-judas", "sourceName": "Gospel of Judas (Codex Tchacos, 2006 publication)", "verb": "CONTEMPORARY_WITH", "targetSlug": "gospel-of-thomas", "targetName": "Gospel of Thomas and other Nag Hammadi texts", "context": "The Gospel of Judas, together with the Gospel of Thomas and other non-canonical texts, collectively demonstrate the extraordinary diversity of early Christian literature and the variety of theological interpretations of Jesus's mission in the 1st–2nd centuries CE."}
    ],
    "places": [
      {"name": "Egypt (discovery c. 1970, Coptic manuscript context)", "role": "The Codex Tchacos was found in Egypt — the country that preserved the most significant Gnostic texts (Nag Hammadi library, Gospel of Judas) through the practice of burying texts in sealed jars in the dry desert soil"},
      {"name": "Lyon, Gaul (Irenaeus's critique, c. 180 CE, earliest reference)", "role": "Irenaeus of Lyon's Against Heresies (c. 180 CE) contains the earliest known reference to the Gospel of Judas — demonstrating that the text was known and criticised by orthodox Christianity in the 2nd century"}
    ],
    "subjects": ["Gnostic Christianity", "Classical Era", "New Testament Apocrypha", "Early Christianity", "Judas Iscariot", "Christian Texts", "Nag Hammadi", "Biblical Scholarship"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Gospel of Judas (c. 2nd century CE, published 2006) is the most sensational of the non-canonical Gospel texts — its rehabilitation of Judas as Jesus's most enlightened disciple generated enormous public interest and contributed to the broader cultural reassessment of early Christian diversity. Together with the Gospel of Thomas, it demonstrates that the canonical New Testament represents the victory of one form of early Christianity over many competing alternatives.",
      "significanceCategory": "significant"
    }
  }
},

"corpus-juris-civilis": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781corpus-juris-civilis.json",
  "slug": "corpus-juris-civilis",
  "data": {
    "summary": "The Corpus Juris Civilis (Body of Civil Law) is the compilation of Roman law ordered by the Emperor Justinian I (527–565 CE) and executed under the supervision of the legal scholar Tribonian (c. 500–547 CE) between 529 and 534 CE — the most comprehensive and influential legal compilation in history, which became the foundation of the civil law tradition followed by the majority of the world's legal systems. The Corpus consists of four parts: the Codex (529, revised 534) — a collection of imperial rescripts and constitutions from Hadrian to Justinian; the Digest (or Pandects, 533) — a systematic anthology of classical Roman jurists' opinions covering all areas of law; the Institutes (533) — a textbook introducing the Digest for law students; and the Novels (Novellae Constitutiones) — Justinian's own new legislation issued after 534.\n\nThe Digest is the intellectual centrepiece of the Corpus Juris Civilis — a 50-book anthology of extracts from the writings of approximately 39 classical Roman jurists (Papinian, Ulpian, Paul, Gaius, Modestinus, and others) covering contract, property, succession, tort, criminal law, and the philosophical foundations of law ('Justice is the constant and perpetual will to render to each his due' — Ulpian, defining justice in the Digest's opening words). The Digest preserved approximately one-third of all classical Roman jurisprudence and its rediscovery in the 11th century at the University of Bologna (c. 1070 CE, in a manuscript found in Amalfi) launched the revival of Roman law that became the foundation of European legal education.\n\nThe Corpus Juris Civilis is the root document of the civil law tradition — the legal tradition followed by approximately 60% of the world's population in continental Europe, Latin America, East Asia, and many other regions — in contrast to the common law tradition of England and its former colonies. The Napoleonic Code (1804), the German Civil Code (1900), the Swiss Civil Code (1907), and the legal codes of most European states, Latin American countries, and many Asian legal systems are ultimately derived from the Corpus Juris Civilis.",
    "causes": [
      "Justinian's imperial programme of restoration — his ambition to reconquer the Western Roman Empire (which he partially achieved through Belisarius's campaigns in Africa and Italy) was accompanied by an equally ambitious programme of legal and religious unification, of which the Corpus Juris Civilis was the legal centrepiece: the systematic codification of Roman law as the universal legal framework of the restored empire.",
      "The fragmentation and complexity of Roman law by the 6th century — the accumulation of centuries of imperial rescripts, senatorial decrees, praetorian edicts, and juristic opinions had produced a body of law so vast and contradictory that no practitioner could master it — created the urgent need for a systematic compilation and rationalisation that Justinian's commission provided.",
      "The availability of the classical Roman juristic tradition — the great jurists of the 2nd–3rd centuries CE (Papinian, Ulpian, Paul, Gaius) had produced a body of legal writing unmatched in sophistication and comprehensiveness — provided the intellectual material that Tribonian's commission organised, edited, and systematised into the Digest."
    ],
    "effects": [
      "The rediscovery of the Digest at the University of Bologna c. 1070 CE launched the revival of Roman law that became the foundation of European legal education — the Bologna glossators (Irnerius and his successors) and their commentaries on the Corpus Juris Civilis established the university legal curriculum that trained European lawyers for five centuries and produced the civil law tradition.",
      "The Corpus Juris Civilis is the root of the civil law tradition — the legal tradition of approximately 60% of the world's population — followed in continental Europe, Latin America, East Asia, and many other regions. The Napoleonic Code (1804), derived from the Corpus through the French legal tradition, spread the Roman legal tradition across Europe and Latin America, making it the most influential legal text in the history of human civilisation.",
      "The Corpus Juris Civilis's preservation of classical Roman jurisprudence — approximately one-third of all classical Roman legal writing survives only in the Digest — made it the primary source for the history of Roman law and the foundation of the comparative legal scholarship that began with the 16th-century humanist jurists (Cujas, Budé, Alciat)."
    ],
    "relationships": [
      {"sourceSlug": "justinian-i", "sourceName": "Justinian I (527–565 CE)", "verb": "COMMISSIONS", "targetSlug": "corpus-juris-civilis", "targetName": "Corpus Juris Civilis (529–534 CE)", "context": "Justinian commissioned the Corpus Juris Civilis as part of his programme of imperial restoration — Tribonian supervised the compilation of the Codex, Digest, and Institutes between 529 and 534."},
      {"sourceSlug": "corpus-juris-civilis", "sourceName": "Corpus Juris Civilis (rediscovery, c. 1070)", "verb": "FOUNDS", "targetSlug": "civil-law-tradition", "targetName": "Civil law tradition (continental Europe, Latin America, East Asia)", "context": "The rediscovery of the Digest at Bologna c. 1070 CE launched the revival of Roman law that became the foundation of the civil law tradition — followed by approximately 60% of the world's population in continental Europe, Latin America, and East Asia."},
      {"sourceSlug": "corpus-juris-civilis", "sourceName": "Corpus Juris Civilis", "verb": "INSPIRES", "targetSlug": "napoleonic-code", "targetName": "Napoleonic Code (1804)", "context": "The Napoleonic Code — derived from the French civil law tradition ultimately rooted in the Corpus Juris Civilis — spread the Roman legal tradition across Europe and Latin America, and is the most widely influential derivative of Justinian's compilation."}
    ],
    "places": [
      {"name": "Constantinople (529–534 CE, compilation context)", "role": "Justinian's capital Constantinople — the seat of the Eastern Roman Empire — where Tribonian and his commission of 17 jurists compiled the Corpus Juris Civilis at Justinian's command between 529 and 534"},
      {"name": "Bologna (c. 1070 CE, rediscovery and revival)", "role": "The University of Bologna — where the Digest was rediscovered c. 1070 and where Irnerius and the glossators began the systematic study of Roman law that became the foundation of European legal education"}
    ],
    "subjects": ["Roman Law", "Medieval Era", "Justinian", "Legal History", "Civil Law", "Byzantine Empire", "Roman History", "Comparative Law"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Corpus Juris Civilis (Justinian, 529–534 CE) is the most influential legal compilation in history — the root document of the civil law tradition followed by approximately 60% of the world's population. The Napoleonic Code and the legal systems of continental Europe, Latin America, and East Asia are ultimately derived from it. Its rediscovery at Bologna c. 1070 launched the revival of Roman law that established university legal education and shaped five centuries of European jurisprudence.",
      "significanceCategory": "world-changing"
    }
  }
},

"computing-machinery-and-intelligence-1950": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781computing-machinery-and-intelligence-195.json",
  "slug": "computing-machinery-and-intelligence-1950",
  "data": {
    "summary": "'Computing Machinery and Intelligence' is the paper by Alan Turing (1912–1954), published in the philosophical journal Mind in October 1950 — one of the most influential papers in the history of science and philosophy, which inaugurated the field of artificial intelligence research and introduced the foundational thought experiment of machine intelligence: the Turing Test (which Turing called the 'Imitation Game'). The paper begins with the question 'Can machines think?' and immediately reframes it: rather than trying to answer this question (which Turing considers meaningless because of the difficulty of defining 'thinking'), Turing proposes the Imitation Game — a test in which a human interrogator communicates via text with two respondents (one human, one machine) and attempts to determine which is which. If the machine can reliably deceive the interrogator into thinking it is human, Turing proposes, we have a meaningful operational substitute for the question of machine thought.\n\nThe paper covers remarkable philosophical and scientific ground in 14 pages: Turing anticipates and addresses nine objections to machine intelligence (the theological objection, the 'heads in the sand' objection, the mathematical objection based on Gödel's incompleteness theorems, the argument from consciousness, arguments from disabilities, Lady Lovelace's objection about originality, the argument from the continuity of the nervous system, the argument from informality of behaviour, and the argument from extra-sensory perception), and proposes that the most promising approach to building an intelligent machine is through machine learning — 'learning machines' that begin with simple rules and improve through experience, rather than programming all knowledge in advance.\n\nTuring's 1950 paper is the founding document of artificial intelligence as a research programme — his operational definition of intelligence through the Imitation Game, his argument that there is no principled reason why machines cannot exhibit intelligent behaviour, and his proposal of machine learning as the preferred approach have structured the entire subsequent development of AI research, from the symbolic AI of the 1950s–1980s through the neural network revolution of the 1980s–1990s to the deep learning revolution of the 2010s.",
    "causes": [
      "Turing's theoretical work on computation — the 1936 paper 'On Computable Numbers', which introduced the Turing machine as a model of universal computation and demonstrated the limits of mechanical computation through the undecidability of the halting problem — gave Turing the foundational theoretical framework from which to address the question of machine intelligence: if a Turing machine can compute any computable function, can it simulate human thought?",
      "The development of stored-programme electronic computers in the late 1940s — which Turing was directly involved in (the Manchester Mark 1, 1948, and the ACE project at the National Physical Laboratory) — provided the empirical context for the 1950 paper: Turing was writing about what real machines could do, not hypothetical devices, and the Imitation Game was proposed as a practical test that might be conducted with existing technology.",
      "The philosophical tradition of the mind-body problem — the debate about the relationship between mental states and physical processes, which had become urgent in the context of computing machines that seemed to simulate mental operations — gave Turing's paper its philosophical context: the Imitation Game was proposed as an operational way of cutting through the philosophical difficulties of the traditional question 'Can machines think?'"
    ],
    "effects": [
      "The Turing Test (Imitation Game) became the foundational benchmark for artificial intelligence — used in the Loebner Prize competition (annual Turing Test contest, founded 1990), cited in virtually every introduction to AI and philosophy of mind, and the touchstone for debates about machine consciousness and intelligence from 1950 to the present.",
      "Turing's proposal of machine learning as the preferred approach to building intelligent machines — 'learning machines' that improve through experience rather than being explicitly programmed — anticipated the neural network and machine learning paradigm that became dominant in the 2010s through deep learning, making his 1950 paper the foundational document of modern AI's most successful approach.",
      "The 1950 paper's philosophical influence on the philosophy of mind has been immense — its operationalist approach to the question of machine intelligence (replacing 'can machines think?' with a behavioural test) influenced functionalism in philosophy of mind, the debates between Searle's Chinese Room argument and Turing's behaviourist approach, and the entire subsequent philosophy of cognitive science."
    ],
    "relationships": [
      {"sourceSlug": "alan-turing", "sourceName": "Alan Turing (1912–1954)", "verb": "AUTHORS", "targetSlug": "computing-machinery-and-intelligence-1950", "targetName": "'Computing Machinery and Intelligence' (1950)", "context": "Turing published the paper in Mind in October 1950, drawing on his theoretical work on computation and his practical experience with early computers to introduce the Imitation Game as a test of machine intelligence."},
      {"sourceSlug": "computing-machinery-and-intelligence-1950", "sourceName": "'Computing Machinery and Intelligence' (Turing Test)", "verb": "FOUNDS", "targetSlug": "artificial-intelligence", "targetName": "Artificial intelligence as a research programme", "context": "Turing's 1950 paper is the founding document of AI research — its operational definition of intelligence through the Imitation Game, its anticipation and rebuttal of objections to machine intelligence, and its proposal of machine learning all structured the subsequent development of the field."},
      {"sourceSlug": "computing-machinery-and-intelligence-1950", "sourceName": "Turing Test (1950)", "verb": "CHALLENGED_BY", "targetSlug": "chinese-room-argument", "targetName": "Searle's Chinese Room argument (1980)", "context": "John Searle's Chinese Room thought experiment (1980) was the most influential philosophical challenge to the Turing Test — arguing that passing the Imitation Game requires only syntactic manipulation and does not demonstrate semantic understanding or consciousness."}
    ],
    "places": [
      {"name": "Manchester, England (1950, Turing's working context at Manchester University)", "role": "Turing wrote 'Computing Machinery and Intelligence' while working at the Victoria University of Manchester, where he was involved in the development of the Manchester Mark 1 stored-programme computer"},
      {"name": "Mind journal (October 1950, publication)", "role": "The paper was published in Mind — the flagship journal of British analytic philosophy — reflecting Turing's intention to address the philosophical community rather than only the computing community"}
    ],
    "subjects": ["Computer Science", "Modern Era", "Alan Turing", "Artificial Intelligence", "Philosophy of Mind", "Technology", "20th Century", "Machine Learning"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Turing's 'Computing Machinery and Intelligence' (1950) is the founding document of artificial intelligence — introducing the Turing Test, anticipating machine learning, and structuring the entire subsequent development of AI research from symbolic AI to deep learning. Its influence on philosophy of mind, cognitive science, and the development of computing is incalculable. The Turing Test remains the foundational benchmark for machine intelligence 75 years after its proposal.",
      "significanceCategory": "world-changing"
    }
  }
},

"ainiakbari": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781ainiakbari.json",
  "slug": "ainiakbari",
  "data": {
    "summary": "The Ain-i-Akbari (Persian: آئین اکبری, 'Institutes of Akbar') is the third and final volume of the Akbarnama — the official history and administrative record of the Mughal Emperor Akbar's reign, written by his court chronicler Abu'l-Fazl ibn Mubarak (1551–1602) and completed c. 1598 CE. While the first two volumes of the Akbarnama narrate the events of Akbar's reign from 1542 to 1602, the Ain-i-Akbari is a comprehensive administrative encyclopedia of the Mughal Empire — a detailed description of Akbar's government, court protocols, military organisation, revenue administration, religious institutions, arts, sciences, geography, and the peoples and resources of the empire. It is the most detailed primary source for the administration and culture of the Mughal Empire at its height and one of the most important administrative histories in any pre-modern tradition.\n\nThe Ain-i-Akbari is divided into five books: Book I on the royal household and court ceremonies; Book II on the imperial military (the mansabdari system, the cavalry, artillery, elephants); Book III on the judicial and revenue administration (the zabti revenue system, the classification of provinces and districts); Book IV on literature, learning, and the sciences (philosophy, astronomy, mathematics, music, painting); and Book V on 'Hindu' religions and philosophy — a remarkable comparative survey of Indian religious traditions (Hinduism, Jainism, Zoroastrianism, and others) reflecting Akbar's famous policy of religious tolerance (Din-i-Ilahi). Abu'l-Fazl's account of Akbar's religious curiosity — his audiences with Hindu scholars, Jain monks, Portuguese Jesuits, and Zoroastrian priests at his court — is the primary evidence for the extraordinary religious pluralism of Akbar's court culture.\n\nThe Ain-i-Akbari's statistics are among the most detailed quantitative records of any pre-modern state — its enumeration of revenue districts, population estimates, agricultural yields, military strengths, and commercial routes provides an unparalleled quantitative picture of the Mughal Empire's administrative geography. The British colonial administration found it indispensable as a baseline for understanding the subcontinent's pre-colonial administrative structure.",
    "causes": [
      "Akbar's programme of systematic administrative reform — his development of the mansabdari system (the graded hierarchy of military and civil rank), the zabti revenue assessment system (standardising land revenue across the empire), and the centralised bureaucratic administration — created both the need for a systematic record of these institutions and the bureaucratic apparatus to compile it.",
      "Abu'l-Fazl's intellectual project — his ambition to present Akbar as a divinely inspired universal sovereign who embodied the best of all religious and philosophical traditions — gave the Ain-i-Akbari its distinctive character: it is simultaneously an administrative record and a theological argument for Akbar's unique spiritual authority as the synthesis of all wisdom traditions.",
      "Akbar's religious syncretism and his policy of sulh-i-kul ('peace with all') — his prohibition of religious discrimination in state service, his abolition of the jizya (poll tax on non-Muslims), and his establishment of the Ibadat Khana (House of Worship) for interfaith dialogue — provided the religious and cultural content that Abu'l-Fazl documented in the Ain-i-Akbari's fifth book."
    ],
    "effects": [
      "The Ain-i-Akbari is the primary administrative and cultural source for the Mughal Empire at its height — its detailed enumeration of revenue districts, provincial administrations, military organisation, and court ceremonial is the foundation for the historical study of Akbar's governance and the Mughal imperial system that endured until the 18th century.",
      "The Ain-i-Akbari's account of Akbar's religious pluralism — his audiences with representatives of all Indian religious traditions, his synthesis of Islamic and Hindu governance, and his Din-i-Ilahi (a personal syncretic faith) — made it a primary source for the study of religious tolerance in Mughal India and for arguments about the indigenous Indian tradition of pluralism.",
      "The British East India Company and the colonial administration used the Ain-i-Akbari as a baseline administrative reference for understanding the pre-colonial structure of Indian governance — contributing to the colonial administrative project of codifying and systematising what the British understood as 'traditional' Indian institutions."
    ],
    "relationships": [
      {"sourceSlug": "abul-fazl", "sourceName": "Abu'l-Fazl ibn Mubarak (1551–1602)", "verb": "AUTHORS", "targetSlug": "ainiakbari", "targetName": "Ain-i-Akbari (c. 1598 CE)", "context": "Abu'l-Fazl wrote the Ain-i-Akbari as the third volume of the Akbarnama at Akbar's court, completing it c. 1598 — a comprehensive administrative encyclopedia of the Mughal Empire at its height."},
      {"sourceSlug": "ainiakbari", "sourceName": "Ain-i-Akbari", "verb": "DOCUMENTS", "targetSlug": "mughal-empire-administration", "targetName": "Mughal Empire's administrative system (mansabdari, zabti)", "context": "The Ain-i-Akbari is the primary source for the Mughal administrative system — its detailed description of the mansabdari hierarchy, the zabti revenue assessment, and the provincial administration is the foundation of our knowledge of Mughal governance."},
      {"sourceSlug": "ainiakbari", "sourceName": "Ain-i-Akbari (Book V)", "verb": "DOCUMENTS", "targetSlug": "akbars-religious-pluralism", "targetName": "Akbar's policy of religious tolerance (sulh-i-kul, Din-i-Ilahi)", "context": "The fifth book of the Ain-i-Akbari is the primary source for Akbar's extraordinary religious pluralism — his audiences with Hindu scholars, Jain monks, Portuguese Jesuits, and Zoroastrian priests, and his policy of sulh-i-kul ('peace with all')."}
    ],
    "places": [
      {"name": "Fatehpur Sikri and Agra, Mughal Empire (c. 1598, composition context)", "role": "Abu'l-Fazl compiled the Ain-i-Akbari at Akbar's court — primarily at Fatehpur Sikri and Agra — the administrative and cultural centres of the Mughal Empire at its height"},
      {"name": "Mughal India (comprehensive coverage of entire empire)", "role": "The Ain-i-Akbari covers the entire Mughal Empire — from the Punjab to Bengal, from Kabul to the Deccan — in its enumeration of revenue districts, provincial administrations, and geographical surveys"}
    ],
    "subjects": ["Mughal History", "Early Modern Era", "Abu'l-Fazl", "Mughal Administration", "Indian History", "Persian Literature", "Akbar", "Primary Source"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Ain-i-Akbari (Abu'l-Fazl, c. 1598 CE) is the most detailed administrative encyclopedia of any pre-modern South Asian state — the primary source for the Mughal Empire's governance under Akbar, including its mansabdari system, zabti revenue assessment, and the extraordinary religious pluralism of Akbar's court. Its quantitative detail and comprehensive coverage make it indispensable for the history of Mughal India at its height.",
      "significanceCategory": "highly-significant"
    }
  }
},

"anna-karenina": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783anna-karenina.json",
  "slug": "anna-karenina",
  "data": {
    "summary": "Anna Karenina is the novel by Count Lev Nikolayevich Tolstoy (1828–1910), published serially in the Russian Messenger (Russky Vestnik) from 1875 to 1877 and as a book in 1878 — widely considered one of the greatest novels ever written and the supreme achievement of the realist novel tradition. The novel opens with one of the most famous sentences in world literature: 'All happy families are alike; each unhappy family is unhappy in its own way' — a maxim that encapsulates the novel's central concern with the varieties of human unhappiness, desire, and social constraint. The narrative follows two interweaved storylines: the passionate, doomed affair of Anna Karenina (a beautiful, intelligent married aristocrat) with the cavalry officer Count Vronsky, which ends in Anna's suicide under a train; and the contrasting story of Konstantin Levin, a landowner struggling with questions of faith, love, agricultural reform, and the meaning of life, who finds happiness in marriage to Kitty and in his work on the land.\n\nAnna Karenina is simultaneously a society novel, a psychological novel, and a philosophical novel — Tolstoy's presentation of Anna's inner life (her growing paranoia, jealousy, and alienation as her social position deteriorates and her relationship with Vronsky begins to fail) is among the most penetrating psychological analyses in fiction; and the Levin subplot is a barely disguised philosophical autobiography in which Tolstoy works through his own crisis of faith and his rejection of secular aristocratic culture. The two plots are linked by Tolstoy's moral judgement on Anna's transgression — a judgement that has been contested by readers and critics since the novel's publication — and by the epigraph from Romans 12:19: 'Vengeance is mine; I will repay, saith the Lord.'\n\nAnna Karenina has been adapted for film more than any other classic novel — approximately 30 film and television adaptations exist, including Greta Garbo (1935), Vivien Leigh (1948), Sophie Marceau (1997), and Keira Knightley (2012) — and its heroine has been one of the most discussed figures in the feminist criticism of the literary canon, as critics debate whether Tolstoy condemns or sympathises with Anna's transgression of social convention.",
    "causes": [
      "Tolstoy's personal crisis of faith and his growing dissatisfaction with the values of Russian aristocratic society — which he was simultaneously depicting and condemning — gave Anna Karenina its dual structure: Anna's tragedy is the social cost of desire in a hypocritical society; Levin's quest is Tolstoy's own autobiographical search for authentic values, culminating in his religious conversion.",
      "The specific social context of Russian aristocratic society in the 1870s — the post-emancipation crisis of the Russian gentry (who had lost their serf labour), the development of Russian capitalism and the railways (symbolised by the train that kills Anna), the reform debates, and the clash between Western liberal values and Slavophile traditionalism — provided Anna Karenina its specific historical and social texture.",
      "Tolstoy's study of the psychological consequences of transgressing social convention — his compassionate attention to the mechanisms by which Russian society punishes Anna's adultery not through explicit condemnation but through the withdrawal of social recognition, the cutting of calls, the closed drawing room doors — gave the novel its sociological precision and its devastating portrayal of social ostracism."
    ],
    "effects": [
      "Anna Karenina's opening sentence — 'All happy families are alike; each unhappy family is unhappy in its own way' — became one of the most cited sentences in world literature, a maxim that has entered the common cultural vocabulary as a summary of the novel's investigation of the varieties of human unhappiness.",
      "The novel's influence on subsequent literary fiction has been immense — Dostoevsky, Turgenev, Henry James, Flaubert's Madame Bovary (an earlier treatment of the same theme of adultery and social transgression), Nabokov, and Faulkner all acknowledged Anna Karenina as a primary model for the psychological novel and the social novel — and Tolstoy's interior monologue technique (particularly in the final section depicting Anna's deteriorating consciousness) is a precursor of stream of consciousness.",
      "Anna Karenina's feminist reception — the debate about whether Tolstoy condemns Anna for her adultery or sympathises with her as a victim of a hypocritical patriarchal society — has been one of the most sustained discussions in feminist literary criticism, and the novel remains central to academic debates about women, desire, and social constraint in the literary canon."
    ],
    "relationships": [
      {"sourceSlug": "leo-tolstoy", "sourceName": "Leo Tolstoy (1828–1910)", "verb": "AUTHORS", "targetSlug": "anna-karenina", "targetName": "Anna Karenina (1875–1878)", "context": "Tolstoy wrote Anna Karenina over four years, weaving his autobiographical search for faith and authentic values (the Levin subplot) with his psychological analysis of social transgression and its consequences (the Anna subplot)."},
      {"sourceSlug": "anna-karenina", "sourceName": "Anna Karenina (Tolstoy)", "verb": "PARALLEL_WITH", "targetSlug": "madame-bovary-flaubert", "targetName": "Madame Bovary (Flaubert, 1857)", "context": "Anna Karenina and Madame Bovary are the two supreme achievements of the realist novel's treatment of female adultery and social transgression — Flaubert's Emma Bovary and Tolstoy's Anna Karenina are the two great fictional heroines of the consequences of desire in a society that punishes women for transgressing its conventions."},
      {"sourceSlug": "anna-karenina", "sourceName": "Anna Karenina opening sentence", "verb": "ESTABLISHES", "targetSlug": "literary-maxim", "targetName": "'Happy families are alike' as a literary maxim", "context": "'All happy families are alike; each unhappy family is unhappy in its own way' is one of the most cited opening sentences in world literature — a maxim that has entered the common cultural vocabulary as a summary of the novel's investigation of unhappiness."}
    ],
    "places": [
      {"name": "Moscow and St. Petersburg (narrative setting, 1870s)", "role": "The two great Russian cities — St. Petersburg (the aristocratic social world where Anna moves and from which she is progressively excluded) and Moscow (where Levin courts Kitty) — together constitute the novel's social geography"},
      {"name": "Russia (1875–1878, serial publication context)", "role": "Anna Karenina was written and published in the Russia of the 1870s — the period of post-emancipation social upheaval, the development of Russian capitalism, and Tolstoy's own spiritual crisis that led to his radical Christianity of the 1880s"}
    ],
    "subjects": ["Russian Literature", "Modern Era", "Leo Tolstoy", "Realist Novel", "19th Century", "Russian History", "Adultery in Literature", "Women in Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Anna Karenina (Tolstoy, 1875–1878) is one of the greatest novels ever written — its opening sentence is one of the most cited in world literature, its psychological depth and social precision make it the supreme achievement of the realist novel tradition, and its heroine is among the most discussed figures in feminist literary criticism. Together with War and Peace, it established Tolstoy as one of the two or three greatest novelists in world literature.",
      "significanceCategory": "world-changing"
    }
  }
},

"and-quiet-flows-the-don": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783and-quiet-flows-the-don.json",
  "slug": "and-quiet-flows-the-don",
  "data": {
    "summary": "And Quiet Flows the Don (Russian: Тихий Дон, Tikhiy Don, 'The Quiet Don') is the epic novel by Mikhail Sholokhov (1905–1984), published in four volumes between 1928 and 1940 — the most significant work of Soviet literature and one of the great epics of 20th-century world literature, awarded the Nobel Prize in Literature in 1965. The novel follows the Cossack community of the Vyoshenskaya stanitsa (settlement) on the Don River in southern Russia through the First World War (1914–1917), the Russian Revolution (1917), and the brutal Civil War (1918–1920) — primarily through the perspective of Grigory Melekhov, a Cossack who moves back and forth between the White and Red armies, driven by personal loyalty, love, and the disintegration of his world. The epic scope — approximately 700,000 words, following multiple generations of Cossack families across twenty years of catastrophic upheaval — earned Sholokhov comparisons to Tolstoy, whose War and Peace is the only Russian novel of comparable scope and ambition.\n\nThe Quiet Don (as it is also known) is remarkable for its moral complexity — Sholokhov presents the Cossacks of the Don region with extraordinary sympathy and detail, depicting their traditional culture, their pride, their violence, and their capacity for both heroism and atrocity, and Grigory Melekhov's political oscillation (unable to commit to either the Reds or the Whites, he ends the novel alone, with everything he loved destroyed) makes him one of the most tragic heroes in Russian literature. The novel's treatment of the Russian Civil War — which Soviet literary doctrine required to be presented as a heroic Red victory over reactionary Whites — is surprisingly balanced, depicting atrocities on both sides and refusing the Manichaean clarity of Socialist Realist ideology.\n\nThe Quiet Don's authorship has been disputed since its publication — allegations that Sholokhov plagiarised the manuscript of a dead White Army officer have persisted for decades, and the discovery of the original manuscript in 1999 substantially (though not conclusively) confirmed Sholokhov's authorship. The Nobel Committee in 1965 cited Sholokhov for 'the artistic power and integrity with which, in his epic of the Don, he has given expression to a historic phase in the life of the Russian people.'",
    "causes": [
      "Sholokhov's personal origins — he was born in the Don Cossack region and spent his formative years there during the revolutionary and civil war period — gave The Quiet Don its extraordinary ethnographic precision and emotional authenticity: the novel is grounded in the specific culture, landscape, and language of the Don Cossacks in a way that could only come from intimate knowledge.",
      "The destruction of traditional Cossack society in the Russian Civil War — the Don Cossacks, who had served as the Tsar's elite cavalry, were caught between the White armies (who sought to restore the old order) and the Red armies (who saw the Cossacks as class enemies), and were subject to systematic Bolshevik 'decossackisation' (raskazachivaniye) that killed hundreds of thousands — provided the historical catastrophe that drives the novel.",
      "The Soviet literary context of the 1920s–1930s — the period before the full consolidation of Socialist Realism as the mandatory aesthetic doctrine — allowed Sholokhov the moral and artistic freedom to write The Quiet Don with a complexity and ambivalence about the Civil War that would have been impossible after the 1934 First Congress of Soviet Writers established Socialist Realism as the obligatory form."
    ],
    "effects": [
      "The Quiet Don is the supreme achievement of Soviet literature — its moral complexity, its refusal of ideological simplification, and its Tolstoyan scope and ambition made it simultaneously the most praised and the most problematic work in the Soviet canon: Stalin's personal protection of Sholokhov shielded him from the consequences of a work that contradicted Socialist Realist doctrine.",
      "Sholokhov's 1965 Nobel Prize — the first Soviet writer to be awarded the Nobel Prize since Boris Pasternak (who was forced to refuse it in 1958) — was a significant moment in the Cold War cultural politics of literature: the Nobel Committee's recognition of The Quiet Don implicitly endorsed Sholokhov's moral complexity over the Socialist Realism that Soviet literary doctrine demanded.",
      "The Quiet Don's portrait of the Don Cossack world — their songs, festivals, agriculture, family structures, and the landscape of the Don steppe — is the most important literary document of a culture that was largely destroyed in the Soviet period, and Sholokhov's epic preserves it with the same documentary completeness that Homer preserves Mycenaean culture or Virgil preserves Republican Roman values."
    ],
    "relationships": [
      {"sourceSlug": "mikhail-sholokhov", "sourceName": "Mikhail Sholokhov (1905–1984)", "verb": "AUTHORS", "targetSlug": "and-quiet-flows-the-don", "targetName": "And Quiet Flows the Don (1928–1940)", "context": "Sholokhov wrote The Quiet Don over approximately twelve years, drawing on his Don Cossack origins to produce the most ambitious epic of Soviet literature — awarded the Nobel Prize in Literature in 1965."},
      {"sourceSlug": "and-quiet-flows-the-don", "sourceName": "The Quiet Don (Nobel Prize, 1965)", "verb": "COMPARED_TO", "targetSlug": "war-and-peace-tolstoy", "targetName": "War and Peace (Tolstoy)", "context": "The Quiet Don's Tolstoyan scope — following multiple generations of Cossack families through twenty years of war and revolution — earned Sholokhov consistent comparisons to Tolstoy, and War and Peace is the only Russian novel of comparable epic ambition."},
      {"sourceSlug": "and-quiet-flows-the-don", "sourceName": "The Quiet Don (moral complexity)", "verb": "CHALLENGES", "targetSlug": "socialist-realism", "targetName": "Socialist Realism (Soviet literary doctrine)", "context": "The Quiet Don's moral complexity — its balanced treatment of Red and White atrocities, Grigory Melekhov's refusal of ideological commitment — challenged Socialist Realism's requirement for unambiguous revolutionary heroism, making Sholokhov's work an anomaly that only Stalin's personal protection preserved."}
    ],
    "places": [
      {"name": "Don River region, southern Russia (narrative setting, 1912–1922)", "role": "The Don Cossack territory — the steppes, rivers, and villages of the Don River region in southern Russia — is both the setting and the subject of The Quiet Don, depicted with extraordinary ethnographic detail"},
      {"name": "Soviet Union (1928–1940, publication context)", "role": "The Quiet Don was published during the most turbulent years of Soviet history — collectivisation, the purges, the consolidation of Stalinist power — and Sholokhov's personal relationship with Stalin was the political foundation on which the novel's publication and survival depended"}
    ],
    "subjects": ["Russian Literature", "Modern Era", "Soviet Literature", "Cossacks", "Russian Civil War", "Sholokhov", "Nobel Prize", "Epic Novel"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "And Quiet Flows the Don (Sholokhov, 1928–1940) is the supreme achievement of Soviet literature — a Tolstoyan epic of the Don Cossacks through the First World War, Revolution, and Civil War, awarded the Nobel Prize in 1965. Its moral complexity and refusal of ideological simplification make it unique in the Soviet literary canon, and its portrait of the destroyed Don Cossack world preserves with documentary completeness a culture swept away by the Soviet period.",
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
