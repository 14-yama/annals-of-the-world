#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 45 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: shakespeares-sonnets, the-birth-of-tragedy, sutta-pitaka,
          le-roman-de-la-rose, lives-of-the-most-excellent-painters-sculptors-and-architects,
          poetic-edda, natya-shastra, quotations-from-chairman-mao-tse-tung
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-45-may2026"

ENRICHMENTS = {

"shakespeares-sonnets": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780shakespeares-sonnets.json",
  "slug": "shakespeares-sonnets",
  "data": {
    "summary": "Shakespeare's Sonnets is the collection of 154 sonnets by William Shakespeare (1564–1616), published in 1609 by the bookseller Thomas Thorpe in a quarto edition (SHAKE-SPEARES SONNETS. Never before Imprinted.) — a publication that may not have been authorised by Shakespeare, who apparently did not see the collection through the press. The sonnets are divided into two groups: Sonnets 1–126, addressed to a young man (the 'Fair Youth') whose identity has been endlessly debated (candidates include Henry Wriothesley, Earl of Southampton, and William Herbert, Earl of Pembroke), and Sonnets 127–154, addressed to or about a dark-haired woman (the 'Dark Lady', also unidentified). The collection also contains a dedication to 'Mr. W. H.' (the 'begetter' of the sonnets) whose identity remains one of the great puzzles of English literary history.\n\nThe sonnets explore the interlocking themes of love, time, beauty, immortality, desire, jealousy, and artistic creation with a density and psychological complexity unparalleled in the English lyric tradition. Sonnet 18 ('Shall I compare thee to a summer's day?'), Sonnet 29 ('When, in disgrace with fortune and men's eyes'), Sonnet 73 ('That time of year thou mayst in me behold'), Sonnet 116 ('Let me not to the marriage of true minds'), Sonnet 129 ('Th' expense of spirit in a waste of shame'), and Sonnet 130 ('My mistress' eyes are nothing like the sun') are among the most celebrated poems in the English language. The collection's formal mastery — the English (Shakespearean) sonnet form of three quatrains and a couplet (ABAB CDCD EFEF GG), used to develop and complicate an argument or image — is the definitive expression of the English sonnet.\n\nThe Sonnets were largely ignored or embarrassed over in the 18th century (the passionate address to the young man was uncomfortable for later readers) but were reclaimed by the Romantics and have been central to English literary culture since. Their biographical interpretation — the attempt to identify the Fair Youth, the Dark Lady, and the Rival Poet as historical figures — has generated an enormous scholarly and popular literature, making them not only the greatest achievement in the English lyric tradition but also the most intensely biographical literary puzzle in English letters.",
    "causes": [
      "The English sonnet tradition — established by Surrey's translations of Petrarch, developed by Sidney's Astrophil and Stella (1591), Spenser's Amoretti (1595), and Daniel's Delia (1592) — provided the generic framework and formal conventions that Shakespeare both mastered and transformed: the Shakespearean sonnet's three-quatrain structure is a distinctly English modification of the Petrarchan form.",
      "The patronage culture of Elizabethan court and aristocratic society — the practice of poets addressing extended lyric sequences to noble patrons or beloveds — provided the social context for the Sonnets' address to the young man: whatever their biographical basis, the sonnets are shaped by the conventions of Elizabethan patronage poetry.",
      "The plague closure of the London theatres (1592–1593) — which interrupted Shakespeare's career as a playwright and drove him toward non-dramatic poetry — is the likely context for the composition of the Sonnets' early poems: the dedication of Venus and Adonis (1593) and The Rape of Lucrece (1594) to the Earl of Southampton suggests the same patronage relationship that may underlie the Fair Youth sonnets."
    ],
    "effects": [
      "The Sonnets established the English or Shakespearean sonnet form (ABAB CDCD EFEF GG) as the dominant English variant of the Italian sonnet — in distinction from the Petrarchan (ABBAABBA CDECDE), and its three-quatrain structure became the model for subsequent English sonnet sequences (Donne, Milton, Keats, Wordsworth, Hopkins).",
      "The Romantic reclamation of the Sonnets — Keats's and Coleridge's admiration for their psychological depth, and the subsequent development of biographical interpretation — established them as the central document of Shakespeare's personal life, the lens through which his inner world has been (controversially) reconstructed.",
      "The Sonnets' exploration of same-sex desire — the passionate address to the young man in Sonnets 1–126 — has made them a central text in the history of sexuality and LGBTQ literary history: they have been read as evidence of Shakespeare's bisexuality and as the most celebrated examples of same-sex love poetry in the English literary tradition."
    ],
    "relationships": [
      {"sourceSlug": "william-shakespeare", "sourceName": "William Shakespeare (1564–1616)", "verb": "AUTHORS", "targetSlug": "shakespeares-sonnets", "targetName": "Shakespeare's Sonnets (published 1609, 154 sonnets)", "context": "Shakespeare's 154 sonnets were published in 1609 — the definitive expression of the English sonnet form and the most psychologically complex lyric sequence in the English language."},
      {"sourceSlug": "shakespeares-sonnets", "sourceName": "Sonnets (Fair Youth, Dark Lady — biographical puzzle)", "verb": "DEDICATED_TO", "targetSlug": "mr-w-h", "targetName": "Mr. W. H. (unidentified dedicatee, 1609 Quarto)", "context": "The 1609 Quarto's dedication to 'Mr. W. H.' — the 'begetter' of the sonnets — is one of the great unresolved puzzles of English literary history, with candidates including Wriothesley (Southampton) and Herbert (Pembroke)."},
      {"sourceSlug": "shakespeares-sonnets", "sourceName": "Sonnets (same-sex desire, Fair Youth sequence)", "verb": "CENTRAL_DOCUMENT_OF", "targetSlug": "history-of-sexuality-literature", "targetName": "LGBTQ literary history and history of sexuality in literature", "context": "The passionate address to the young man in Sonnets 1–126 has made the Sonnets a central text in LGBTQ literary history — the most celebrated examples of same-sex love poetry in the English tradition."}
    ],
    "places": [
      {"name": "London (Elizabethan court culture, theatrical environment, 1590s–1600s)", "role": "Shakespeare composed the sonnets in London in the context of Elizabethan court culture and theatrical life — the patronage relationships, plague closures, and social dynamics of late Elizabethan London shaped the sonnets' composition"},
      {"name": "England (publication 1609, Thomas Thorpe; Elizabethan sonnet tradition)", "role": "The Sonnets were published in England in 1609 by Thomas Thorpe — possibly without Shakespeare's authorisation — in the context of the flourishing Elizabethan sonnet sequence tradition (Sidney, Spenser, Daniel)"}
    ],
    "subjects": ["English Literature", "Early Modern Era", "William Shakespeare", "Poetry", "Sonnet", "Elizabethan Literature", "Renaissance", "Lyric Poetry"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Shakespeare's Sonnets (1609) are the greatest achievement in the English lyric tradition — 154 poems that established the English sonnet form, explored love, time, beauty, and desire with unparalleled psychological depth, and generated the most intensely biographical literary puzzle in English letters. Their exploration of same-sex desire has made them central to LGBTQ literary history; their formal mastery defined the English sonnet for four centuries.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-birth-of-tragedy": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-birth-of-tragedy.json",
  "slug": "the-birth-of-tragedy",
  "data": {
    "summary": "The Birth of Tragedy from the Spirit of Music (German: Die Geburt der Tragödie aus dem Geiste der Musik) is the first published work of Friedrich Nietzsche (1844–1900), issued in January 1872 and written while he was a professor of classical philology at the University of Basel. Originally subtitled 'from the spirit of music' (reflecting the influence of Richard Wagner, to whom the work is dedicated and whose music drama Nietzsche saw as the rebirth of Dionysian art), the work was reissued in 1886 with a new preface ('Attempt at a Self-Criticism') in which Nietzsche both revised his earlier position and distanced himself from Wagner.\n\nThe Birth of Tragedy develops the distinction between two fundamental artistic drives: the Apollonian (from Apollo, the god of light, reason, and form) — the drive toward beauty, order, individuation, and rational coherence, expressed in sculpture and epic poetry — and the Dionysian (from Dionysus, the god of wine and ecstasy) — the drive toward dissolution of individual boundaries, irrational ecstasy, and the embrace of primordial suffering and unity, expressed in music. Nietzsche argues that Greek tragedy achieved its extraordinary power by fusing these two drives: the Dionysian musical chorus (the origin of tragedy in satyr plays and choral song) was organised by Apollonian dramatic form to produce an art that expressed the tragic knowledge that existence is fundamentally suffering and chaos, while simultaneously affirming life through beauty.\n\nNietzsche further argues that Greek tragedy was destroyed by Socratic rationalism — Euripides's rationalist transformation of tragedy, under the influence of Socrates, banished the Dionysian and produced an 'optimistic' drama that could not sustain the tragic vision — and that Wagner's music drama represents the rebirth of authentic Dionysian art in modern Germany. The Apollo/Dionysus distinction became one of the most influential conceptual pairs in subsequent aesthetic theory, philosophy of culture, and cultural criticism.",
    "causes": [
      "Nietzsche's classical philological training and his deep engagement with Greek tragedy — his study of Aeschylus, Sophocles, and Euripides, and his dissatisfaction with conventional classical scholarship's sunny idealisation of Greece as the land of 'noble simplicity and quiet grandeur' (Winckelmann's formula) — drove his argument that Greek culture was founded on the acknowledgment of suffering, not its denial.",
      "Nietzsche's encounter with Schopenhauer's philosophy — particularly Schopenhauer's Will as the blind, striving, suffering force underlying all existence, and his theory of music as the most direct expression of the Will — provided the metaphysical framework for the Birth of Tragedy's account of the Dionysian: the Dionysian is Nietzsche's aesthetic translation of Schopenhauerian metaphysics.",
      "Nietzsche's friendship with and admiration for Richard Wagner — the two met in 1868, and Nietzsche was a regular visitor to Tribschen (Wagner's home) — was the biographical and intellectual context for the Birth of Tragedy's argument: Nietzsche saw Wagner's music dramas as the contemporary realisation of the Dionysian artistic impulse."
    ],
    "effects": [
      "The Apollo/Dionysus distinction became one of the most widely used conceptual pairs in Western cultural theory — applied in anthropology (Ruth Benedict's Patterns of Culture), psychology (Freud's Eros and Thanatos), philosophy of culture (Walter Pater), and cultural criticism — demonstrating the extraordinary productivity of Nietzsche's initial conceptual innovation.",
      "The Birth of Tragedy's critique of Socratic rationalism — the argument that Western culture's commitment to reason had suppressed the Dionysian and produced a life-denying optimism — inaugurated Nietzsche's lifelong critique of rationalism, morality, and 'slave values' that culminated in his mature philosophy (Thus Spoke Zarathustra, Beyond Good and Evil, On the Genealogy of Morality).",
      "The Birth of Tragedy was received poorly by Nietzsche's classical philological colleagues (Ulrich von Wilamowitz-Möllendorff's devastating critical pamphlet of 1872 attacked its unscholarly methods) but became enormously influential outside classical philology — it is one of the foundational texts of 20th-century aesthetics, cultural theory, and philosophy."
    ],
    "relationships": [
      {"sourceSlug": "friedrich-nietzsche", "sourceName": "Friedrich Nietzsche (1844–1900, German philosopher)", "verb": "AUTHORS", "targetSlug": "the-birth-of-tragedy", "targetName": "The Birth of Tragedy (Die Geburt der Tragödie, January 1872)", "context": "Nietzsche published The Birth of Tragedy in January 1872 — his first book, developing the Apollo/Dionysus distinction as the key to Greek tragic art and arguing for Wagner's music drama as its modern rebirth."},
      {"sourceSlug": "the-birth-of-tragedy", "sourceName": "Birth of Tragedy (Apollo/Dionysus, tragic vision)", "verb": "ESTABLISHES", "targetSlug": "apollonian-dionysian-distinction", "targetName": "Apollonian/Dionysian conceptual distinction (aesthetics, cultural theory)", "context": "The Apollo/Dionysus distinction became one of the most widely used conceptual pairs in Western cultural theory — applied in anthropology, psychology, philosophy of culture, and cultural criticism."},
      {"sourceSlug": "the-birth-of-tragedy", "sourceName": "Birth of Tragedy (Wagner dedication, Dionysian music)", "verb": "DEDICATED_TO", "targetSlug": "richard-wagner", "targetName": "Richard Wagner (1813–1883, composer, music drama)", "context": "Nietzsche dedicated the Birth of Tragedy to Richard Wagner and argued that Wagner's music dramas represented the modern rebirth of Dionysian art — a position he later repudiated when he broke with Wagner."}
    ],
    "places": [
      {"name": "Basel (Nietzsche's professorship, composition context, 1869–1879)", "role": "Nietzsche was professor of classical philology at the University of Basel when he wrote The Birth of Tragedy — the academic context that both enabled and constrained the work, received poorly by his scholarly colleagues"},
      {"name": "Tribschen, Lucerne (Wagner's home — Nietzsche's visits, friendship)", "role": "Nietzsche was a regular visitor to Wagner's home at Tribschen on Lake Lucerne in the early 1870s — the friendship was the biographical context for the Birth of Tragedy's Wagnerian argument"}
    ],
    "subjects": ["German Philosophy", "Modern Era", "Friedrich Nietzsche", "Aesthetics", "Greek Tragedy", "Classical Antiquity", "Philosophy of Art", "Cultural Theory"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Birth of Tragedy (Nietzsche, 1872) established the Apollo/Dionysus distinction as one of the most productive conceptual pairs in Western cultural theory and inaugurated Nietzsche's lifelong critique of Western rationalism. Its influence extends from 20th-century aesthetics (Pater, Ruth Benedict) and psychology (Freud) to cultural theory (Benjamin) and philosophy. As the founding text of Nietzsche's philosophical project, it remains one of the most influential works of 19th-century German philosophy.",
      "significanceCategory": "highly-significant"
    }
  }
},

"sutta-pitaka": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780sutta-pitaka.json",
  "slug": "sutta-pitaka",
  "data": {
    "summary": "The Sutta Pitaka (Pali: Suttapiṭaka, 'Basket of Discourses') is the largest of the three 'baskets' (pitakas) of the Pali Canon (Tipiṭaka) — the scriptural canon of Theravāda Buddhism — and the primary collection of the Buddha's teachings (sutta, Sanskrit: sūtra). It is divided into five Nikāyas ('collections'): the Dīgha Nikāya ('Long Discourses', 34 suttas), the Majjhima Nikāya ('Middle-Length Discourses', 152 suttas), the Saṃyutta Nikāya ('Connected Discourses', approximately 2,900 suttas organised by topic), the Aṅguttara Nikāya ('Numerical Discourses', approximately 9,550 suttas organised by numerical categories), and the Khuddaka Nikāya ('Minor Collection', comprising 18 smaller texts including the Dhammapada, Jātaka tales, Udāna, and Sutta Nipāta). The complete Sutta Pitaka is one of the most extensive collections of early religious literature in any language.\n\nThe Sutta Pitaka presents itself as the direct record of the teachings (dhamma) of Gotama Buddha (c. 5th–4th century BCE) — each sutta begins with 'Evam me sutam' ('Thus have I heard') and locates the discourse in a specific place and social context, creating the impression of direct reportage of the Buddha's teachings to specific audiences. Modern scholarship regards the Sutta Pitaka as the product of oral transmission and gradual accretion over several centuries following the Buddha's death (parinibbāna), with the canonical texts fixed at a series of councils — the First Council (Rājagṛha, shortly after the Buddha's death), the Second Council (Vesālī, c. 100 years later), and the Third Council (Pāṭaliputra, c. 250 BCE under Ashoka's patronage) — and written down in Sri Lanka c. 1st century BCE.\n\nThe Sutta Pitaka contains the core teachings of Buddhism: the Four Noble Truths (the truth of suffering, the truth of the origin of suffering in craving, the truth of the cessation of suffering, and the truth of the Noble Eightfold Path as the way to cessation), the Three Marks of Existence (anicca — impermanence, dukkha — suffering/unsatisfactoriness, anattā — non-self), the doctrine of dependent origination (paṭicca-samuppāda), and the ethics and meditation practices of the Buddhist path.",
    "causes": [
      "The teaching activity of Gotama Buddha (c. 5th–4th century BCE) — his 45 years of teaching across the Gangetic plain after his enlightenment at Bodh Gaya — provided the original discourses that the Sutta Pitaka claims to preserve: the Sutta Pitaka is, in its self-presentation, the direct record of the Buddha's teaching.",
      "The Buddhist tradition of oral transmission — the practice of monks memorising and reciting the teachings through group recitation (saṅgīti) at the series of councils following the Buddha's death — preserved the teachings and shaped their canonical form: the formulaic language, repetitions, and mnemonic structures of the suttas reflect their composition for oral transmission.",
      "Ashoka's patronage of Buddhism — his convening of the Third Council at Pāṭaliputra (c. 250 BCE), his sending of missions throughout India and beyond, and the subsequent transmission of Theravāda Buddhism to Sri Lanka by his son Mahinda — was a crucial moment in the preservation and propagation of the Pali Canon: the texts were written down in Sri Lanka c. 1st century BCE, preserving the Pali textual tradition."
    ],
    "effects": [
      "The Sutta Pitaka became the foundational scriptural authority of Theravāda Buddhism — the form of Buddhism practiced in Sri Lanka, Myanmar, Thailand, Laos, and Cambodia — providing the textual basis for Theravāda doctrine, monastic practice, and lay ethics across South and Southeast Asia for over two thousand years.",
      "The translation of the Pali Canon into Sinhalese, Burmese, Thai, Khmer, Lao, and other languages — and subsequently into European languages (beginning with Rhys Davids's translations in the 19th century) — transmitted the Buddha's teachings throughout Asia and eventually to the Western world, making the Sutta Pitaka one of the primary channels for Buddhism's global diffusion.",
      "The academic study of the Pali Canon — pioneered by the Pali Text Society (founded by T. W. Rhys Davids in 1881) — produced critical editions and translations of the complete Pali Canon in European languages, making the Sutta Pitaka available to Western scholarship and contributing to the development of Buddhist Studies as an academic discipline."
    ],
    "relationships": [
      {"sourceSlug": "sutta-pitaka", "sourceName": "Sutta Pitaka (Five Nikāyas, Pali Canon)", "verb": "PART_OF", "targetSlug": "pali-canon", "targetName": "Pali Canon (Tipiṭaka) — Theravāda Buddhist scripture", "context": "The Sutta Pitaka is the largest of the three baskets of the Pali Canon — the primary scriptural authority of Theravāda Buddhism, comprising the Five Nikāyas with approximately 12,600 suttas."},
      {"sourceSlug": "sutta-pitaka", "sourceName": "Sutta Pitaka (Four Noble Truths, Eightfold Path, Buddhist teachings)", "verb": "CONTAINS", "targetSlug": "core-buddhist-doctrine", "targetName": "Core Buddhist doctrine (Four Noble Truths, Three Marks, Eightfold Path)", "context": "The Sutta Pitaka contains the core teachings of Buddhism — the Four Noble Truths, the Three Marks of Existence, dependent origination, and the Noble Eightfold Path — as presented in the attributed discourses of the Buddha."},
      {"sourceSlug": "sutta-pitaka", "sourceName": "Sutta Pitaka (Third Council, Ashoka patronage)", "verb": "COMPILED_UNDER", "targetSlug": "ashoka-maurya", "targetName": "Ashoka (r. 268–232 BCE, Maurya emperor, Buddhism patron)", "context": "Ashoka's convening of the Third Buddhist Council at Pāṭaliputra (c. 250 BCE) and his patronage of the Theravāda tradition was crucial for the preservation and propagation of the Pali Canon."}
    ],
    "places": [
      {"name": "Gangetic Plain, India (Buddha's teaching activity, c. 5th–4th century BCE)", "role": "The Sutta Pitaka's discourses are located in specific places across the Gangetic plain — Rājagṛha, Sāvatthī, Vesālī, Campā — reflecting the geography of the Buddha's teaching activity"},
      {"name": "Sri Lanka (written down c. 1st century BCE; Theravāda primary transmission centre)", "role": "The Pali Canon was written down in Sri Lanka c. 1st century BCE — making Sri Lanka the primary centre for the preservation and transmission of the Theravāda textual tradition"}
    ],
    "subjects": ["Buddhist Literature", "Ancient Era", "Buddhism", "Pali Canon", "Theravāda Buddhism", "Religious Texts", "Indian Literature", "Oral Tradition"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Sutta Pitaka (Pali Canon, compiled c. 5th–1st century BCE) is the foundational scriptural authority of Theravāda Buddhism — the primary textual record of the Buddha's teachings, containing the Four Noble Truths, the Noble Eightfold Path, and the ethical and meditative framework that guides the religious life of hundreds of millions of people in Sri Lanka, Myanmar, Thailand, Laos, and Cambodia. One of the most extensive collections of early religious literature in any language.",
      "significanceCategory": "world-changing"
    }
  }
},

"le-roman-de-la-rose": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780le-roman-de-la-rose.json",
  "slug": "le-roman-de-la-rose",
  "data": {
    "summary": "Le Roman de la Rose ('The Romance of the Rose') is a medieval French allegorical poem in two parts by two different authors: the first 4,058 lines were composed c. 1230 by Guillaume de Lorris (c. 1200–1240?), and the work was continued and completed by Jean de Meun (Jean de Meung, c. 1240–1305?) in approximately 17,722 additional lines c. 1275, for a total of approximately 21,780 lines of octosyllabic couplets. It is the most widely copied and influential secular text in the French Middle Ages — over 300 manuscripts survive — and the central text of the debate about love, sexuality, and the nature of woman in medieval French literary culture.\n\nGuillaume de Lorris's shorter, courtly first part presents a dreamer-narrator who enters a walled garden and attempts to win the Rose (symbolising the beloved's favour) through a series of encounters with allegorical figures — Idleness, Pleasure, Courtesy, Beauty, Youth, Generosity, and their opponents Danger, Fear, Shame, and Jealousy — in the tradition of the courtly love (fin'amor) allegory. Jean de Meun's much longer continuation radically transforms the poem's tone and theme: it expands the allegorical drama into an encyclopaedic work of anti-courtly and satirical literature, incorporating long digressions on Reason, Nature, and Genius, a parody of the Romance of the Rose's own allegorical conventions, an extended discourse by the Jealous Husband and the Old Woman that is sexually explicit and anti-feminist, and a concluding 'plucking of the rose' (sexual consummation) that is described in aggressive, comic, and phallic imagery.\n\nThe Roman de la Rose generated one of the first major literary debates in European vernacular literature: the Quarrel of the Rose (Querelle de la Rose, c. 1401–1402), in which Christine de Pizan and Jean Gerson attacked Jean de Meun's misogyny and obscenity, while Pierre Col and Jean de Montreuil defended the poem's moral intention. This debate is an early landmark in the history of literary criticism and feminist thought.",
    "causes": [
      "The troubadour and trouvère tradition of courtly love allegory — the Provençal and Old French literary tradition of love poetry expressing the relationship between the courtly lover and the unattainable lady through elaborate formal conventions — provided the generic framework for Guillaume de Lorris's first part: the Roman de la Rose is the most elaborate courtly love allegory in Old French.",
      "Jean de Meun's encyclopaedic intellectual ambition — his desire to incorporate the entire intellectual culture of the Latin medieval tradition (Ovid's Ars Amatoria, Boethius's Consolation, Alan of Lille's De Planctu Naturae, Alain de Insulis's Anticlaudianus) into a vernacular French poem — drove the radical expansion of the Roman de la Rose from a courtly love allegory into an encyclopaedic work of medieval learning.",
      "The social and intellectual context of 13th-century Paris — the University of Paris, with its debates over Aristotelian philosophy, courtly literature, and the nature of love — provided both the audience and the intellectual framework for Jean de Meun's continuation: the poem reflects and engages with the university culture of its time."
    ],
    "effects": [
      "The Roman de la Rose was the most widely copied secular text in medieval French — over 300 manuscripts — and its influence on subsequent French literature (Machaut, Deschamps, Christine de Pizan) and English literature (Chaucer, who translated an early portion of the Roman) was enormous: it defined the conventions of allegorical love poetry for the late medieval period.",
      "The Quarrel of the Rose (c. 1401–1402) — Christine de Pizan's and Jean Gerson's attacks on Jean de Meun's misogyny — is one of the earliest documented feminist literary debates in European history, and Christine de Pizan's engagement with the Roman de la Rose in the Querelle shaped her subsequent works (The Book of the City of Ladies) as a pioneer of feminist literary criticism.",
      "Jean de Meun's continuation of the Roman de la Rose introduced a radically different conception of love literature — encyclopaedic, satirical, sexually explicit, anti-courtly, and proto-naturalist — that anticipated later Renaissance humanism's challenge to courtly idealisation and contributed to the diversification of medieval literary culture."
    ],
    "relationships": [
      {"sourceSlug": "jean-de-meun", "sourceName": "Jean de Meun (c. 1240–1305?, French poet)", "verb": "CO-AUTHORS", "targetSlug": "le-roman-de-la-rose", "targetName": "Le Roman de la Rose (~21,780 lines, c. 1230 + c. 1275)", "context": "Jean de Meun continued Guillaume de Lorris's shorter courtly allegory (4,058 lines, c. 1230) with approximately 17,722 additional lines c. 1275 — transforming the poem into an encyclopaedic, satirical, and sexually explicit work."},
      {"sourceSlug": "le-roman-de-la-rose", "sourceName": "Roman de la Rose (Jean de Meun misogyny — Querelle de la Rose)", "verb": "OPPOSED_BY", "targetSlug": "christine-de-pizan", "targetName": "Christine de Pizan (c. 1364–c. 1430, feminist literary critic)", "context": "Christine de Pizan's attack on Jean de Meun's misogyny in the Quarrel of the Rose (c. 1401–1402) is one of the earliest feminist literary debates in European history — Christine's engagement shaped her Book of the City of Ladies."},
      {"sourceSlug": "le-roman-de-la-rose", "sourceName": "Roman de la Rose (Chaucer translation, influence on English literature)", "verb": "INFLUENCES", "targetSlug": "the-canterbury-tales", "targetName": "Geoffrey Chaucer and English medieval literature", "context": "Chaucer translated a portion of the Roman de la Rose into English and was deeply influenced by it — the Roman's allegorical conventions and Jean de Meun's encyclopaedic approach are present throughout Chaucer's work."}
    ],
    "places": [
      {"name": "France (Paris, 13th-century University context; Old French literary culture)", "role": "Le Roman de la Rose was composed in France (c. 1230 and c. 1275) within the Old French literary culture of the 13th century — Jean de Meun was associated with the University of Paris environment"},
      {"name": "Medieval Europe (over 300 manuscripts; read across France, England, Flanders, Italy)", "role": "The Roman de la Rose was the most widely copied secular text in medieval French — over 300 manuscripts survive, demonstrating its diffusion across medieval European literary culture"}
    ],
    "subjects": ["French Literature", "Medieval Era", "Courtly Love", "Allegorical Poetry", "Medieval Literature", "Old French", "Feminism", "Literary Debate"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Le Roman de la Rose (Guillaume de Lorris c. 1230 + Jean de Meun c. 1275) is the most widely copied secular text in medieval French — over 300 manuscripts — and the central text of medieval allegorical love poetry. Its influence on Chaucer, Christine de Pizan, and French literary culture was enormous; the Quarrel of the Rose (c. 1401–1402) it generated is one of the earliest feminist literary debates in European history.",
      "significanceCategory": "world-changing"
    }
  }
},

"lives-of-the-most-excellent-painters-sculptors-and-architects": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780lives-of-the-most-excellent-painters-sculptors-and-architects.json",
  "slug": "lives-of-the-most-excellent-painters-sculptors-and-architects",
  "data": {
    "summary": "Le Vite de' più eccellenti pittori, scultori, e architettori ('Lives of the Most Excellent Painters, Sculptors, and Architects', commonly known as the Vite or Vasari's Lives) is a collection of artists' biographies by the Italian painter and architect Giorgio Vasari (1511–1574), first published in 1550 (by Lorenzo Torrentino, Florence) in two volumes, and substantially revised and expanded in a second edition in 1568 (by Giunti, Florence). The 1568 edition contains 161 biographies of artists from Cimabue (c. 1240–1302) to Vasari's own contemporaries, organised in roughly chronological order and divided into three 'ages' of Italian art: the first age (from Cimabue to around 1400, the recovery of the arts after the 'barbarian' Middle Ages), the second age (Ghiberti, Donatello, Masaccio, Brunelleschi — the development of the arts toward perfection), and the third and culminating age (Leonardo, Michelangelo, Raphael, Titian — the maniera moderna, the full achievement of classical perfection).\n\nThe Vite is the founding document of art history as a discipline — the first systematic attempt to write the history of the visual arts as a narrative of artists' lives, schools, and stylistic development, and to analyse artistic quality in terms that could be applied comparatively and historically. Its narrative framework — the idea that art declined with the fall of Rome and was reborn (rinascita, 'renaissance') in 13th-century Italy, developed through successive generations, and reached its summit in Michelangelo — both gave the Renaissance its name and created the interpretive framework that shaped art historical understanding for four centuries.\n\nVasari's Vite is also an invaluable (if not uncritical) primary source for the lives of Renaissance artists — many details of the lives of Masaccio, Botticelli, Leonardo, Raphael, and dozens of others survive only in Vasari's biographies — and a crucial document for the social history of Renaissance artists, the development of the artist as a social type, and the economics and organisation of Renaissance workshop practice.",
    "causes": [
      "Humanist biography and the tradition of ancient writers on the arts — Pliny the Elder's Natural History (which contains biographical accounts of ancient painters and sculptors), Vitruvius's De Architectura, and the humanist biographies of poets and artists — provided the literary models and the intellectual framework for Vasari's project: the Lives is a vernacular humanist biography project modelled on ancient precedents.",
      "Vasari's personal formation in the Florentine and Roman artistic milieu — his training in Florence under the Medici patronage network, his acquaintance with Michelangelo (whom he knew personally and treated as the culmination of the entire artistic development), and his participation in the Florentine artistic community — gave him the social access and personal knowledge that make the Lives an invaluable primary source.",
      "Cardinal Alessandro Farnese's and subsequently Duke Cosimo I de' Medici's patronage of Vasari — the political context of Medicean Florence and the desire of the Medici to present Florence as the capital of Italian art — shaped the Lives' narrative: the Florentine-centrist perspective and the elevation of Florentine artists (Giotto, Brunelleschi, Michelangelo) over Venetian and Roman rivals reflects the Florentine political context."
    ],
    "effects": [
      "Vasari's Vite created the interpretive framework that shaped art historical understanding of the Italian Renaissance for four centuries — the three-age narrative of rebirth, development, and summit; the idea of artistic progress toward a classical ideal; and the elevation of Florence and Michelangelo as the summit of artistic achievement — establishing the vocabulary and conceptual categories of Renaissance art history.",
      "Vasari's narrative invention of the 'Renaissance' — his use of the term rinascita ('rebirth') to describe the recovery of the arts after the medieval period — effectively created the historical concept of the Renaissance as a period and cultural movement: the Renaissance as a historical category is substantially a Vasarian construct.",
      "The Vite established the biography of the artist as the primary genre of art historical writing — the tradition of organising art history around the lives of individual artists that persisted from Vasari through the 19th century (it only began to be challenged by Wölfflin's formalism and Alois Riegl's Kunstwollen in the late 19th century) — making it the founding document of the biographical tradition in art history."
    ],
    "relationships": [
      {"sourceSlug": "giorgio-vasari", "sourceName": "Giorgio Vasari (1511–1574, Italian painter and architect)", "verb": "AUTHORS", "targetSlug": "lives-of-the-most-excellent-painters-sculptors-and-architects", "targetName": "Vite de' più eccellenti pittori (1550, expanded 1568)", "context": "Vasari published the Vite in 1550 (expanded 1568) — 161 artist biographies that founded art history as a discipline and created the narrative of the Italian Renaissance."},
      {"sourceSlug": "lives-of-the-most-excellent-painters-sculptors-and-architects", "sourceName": "Vite (rinascita, three ages of Italian art, Renaissance narrative)", "verb": "ESTABLISHES", "targetSlug": "concept-of-the-renaissance", "targetName": "The concept of the Renaissance (rinascita, rebirth of the arts)", "context": "Vasari's use of rinascita ('rebirth') to describe the recovery of the arts after the medieval period effectively created the historical concept of the Renaissance — the period category is substantially a Vasarian narrative construct."},
      {"sourceSlug": "lives-of-the-most-excellent-painters-sculptors-and-architects", "sourceName": "Vite (Michelangelo as summit, Florence-centred)", "verb": "FEATURES", "targetSlug": "michelangelo", "targetName": "Michelangelo Buonarroti (1475–1564)", "context": "Vasari's Vite treats Michelangelo as the culmination of the entire development of Renaissance art — Vasari knew Michelangelo personally and his biography is the most important contemporary account of Michelangelo's life and work."}
    ],
    "places": [
      {"name": "Florence (Medicean artistic centre, Vasari's primary subject and patron)", "role": "Vasari's Florence-centred perspective — trained in Florence, working for Cosimo I de' Medici — shapes the Vite's elevation of Florentine art as the summit of the Renaissance tradition"},
      {"name": "Rome (Vasari's artistic formation, Vatican, Michelangelo's Rome)", "role": "Vasari spent significant periods in Rome — the artistic capital of the maniera moderna — and his Roman experience, including personal contact with Michelangelo, enriched the Vite's accounts of the High Renaissance"}
    ],
    "subjects": ["Italian Literature", "Early Modern Era", "Giorgio Vasari", "Art History", "Renaissance", "Biography", "Italian Art", "Art Criticism"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Vasari's Lives (1550, expanded 1568) is the founding document of art history as a discipline — it created the narrative of the Italian Renaissance (the three-age framework, the concept of rinascita), established the biographical tradition in art writing, and remains an invaluable primary source for Renaissance artists. Its narrative invention of the 'Renaissance' as a historical category makes it one of the most consequential cultural texts in the history of European art.",
      "significanceCategory": "world-changing"
    }
  }
},

"poetic-edda": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780poetic-edda.json",
  "slug": "poetic-edda",
  "data": {
    "summary": "The Poetic Edda (Old Norse: Edda; also known as the Elder Edda or Sæmundar Edda, though neither attribution is accurate) is a collection of Old Norse mythological and heroic poems preserved primarily in the Codex Regius manuscript (Konungsbók, 'King's Book'), a vellum codex written c. 1270 CE in Iceland, donated to the Danish King Frederick III in 1662 and now in the Árni Magnússon Institute for Icelandic Studies, Reykjavik. The Codex Regius contains 29 poems; additional poems from other manuscripts are conventionally included in editions of the Poetic Edda, bringing the total to approximately 34–40 poems depending on the edition. The poems are thought to have been composed between the 9th and 13th centuries CE, with some possibly preserving material of considerably greater antiquity.\n\nThe Poetic Edda falls into two groups: mythological poems (Völuspá, 'The Seeress's Prophecy' — a cosmological narrative from the creation of the world to Ragnarök and the new world after; Hávamál, 'Words of the High One' — wisdom poetry attributed to Odin; Vafþrúðnismál, Grímnismál, Skírnismál, Lokasenna, Þrymskviða, and others dealing with Norse gods — Odin, Thor, Freyr, Loki) and heroic poems (the Sigurd cycle — Reginsmál, Fáfnismál, Sigrdrífumál, Atlakviða, Atlamál, and others — dealing with the legend of Sigurd the dragon-slayer and the Nibelungen material that also underlies the German Nibelungenlied).\n\nThe Poetic Edda is the primary source for Norse mythology and the Norse heroic tradition — it contains the most detailed surviving accounts of Norse cosmology (the Nine Worlds, Yggdrasil, the creation, Ragnarök), Norse deities (Odin, Thor, Freyr, Freyja, Loki, Baldr), and the mythological and heroic narrative material that shaped Old Norse literature, skaldic poetry, and medieval Scandinavian culture.",
    "causes": [
      "The conversion of Iceland and Scandinavia to Christianity (c. 1000 CE) — and the subsequent concern of Icelandic scholars to preserve pre-Christian poetic and mythological material — was the primary context for the preservation of the Poetic Edda: the 13th-century Icelandic manuscript tradition that preserved both the Poetic Edda and Snorri Sturluson's Prose Edda was motivated by scholarly concern to document the pre-Christian past.",
      "The specific genius of the Icelandic manuscript tradition — the extraordinary productivity of 13th-century Icelandic scribes in recording Old Norse poetry, sagas, and laws — was the mechanism of preservation: without the Codex Regius (c. 1270 CE) and related manuscripts, the Poetic Edda would have been lost.",
      "The Old Norse skaldic tradition — the poetic culture of court poets who composed intricate alliterative and kenning-based verse — provided the literary context for the Eddic poems: the mythological and heroic narratives of the Poetic Edda were part of the same Old Norse poetic universe as skaldic verse, and knowledge of the myths was essential for understanding skaldic kennings."
    ],
    "effects": [
      "The Poetic Edda became the primary source for Norse mythology in the modern world — the Norse mythological tradition that inspired Wagner's Ring Cycle (the Sigurd cycle of the Poetic Edda is the immediate source for the Nibelung material), Tolkien's Middle-earth (Gandalf is modelled on the Eddic Odin; the names of Tolkien's dwarves come from the Dvergatal in Völuspá), and contemporary popular culture (Marvel Comics' Thor).",
      "Wagner's Ring Cycle (Der Ring des Nibelungen, 1848–1874) — directly based on the Norse Eddic Sigurd cycle and the German Nibelungenlied — transformed Poetic Edda material into the most ambitious music drama in the Western tradition, cementing the Norse mythological tradition's place in European cultural consciousness.",
      "The 19th-century Nordic revival — the Romantic nationalist interest in Norse mythology as the authentic spiritual heritage of the Germanic and Scandinavian peoples — drew primarily on the Poetic Edda, making it a central text in the formation of Scandinavian national identities and the Nordic cultural tradition."
    ],
    "relationships": [
      {"sourceSlug": "poetic-edda", "sourceName": "Poetic Edda (Codex Regius, c. 1270, Norse mythology)", "verb": "PRIMARY_SOURCE_FOR", "targetSlug": "norse-mythology", "targetName": "Norse mythology (Odin, Thor, Loki, Ragnarök, Nine Worlds)", "context": "The Poetic Edda is the primary source for Norse mythology — it contains the most detailed surviving accounts of Norse cosmology, deities, and the mythological narrative material that shaped medieval Scandinavian culture."},
      {"sourceSlug": "poetic-edda", "sourceName": "Poetic Edda (Sigurd cycle, Nibelung material)", "verb": "INFLUENCES", "targetSlug": "ring-cycle-wagner", "targetName": "Wagner's Ring Cycle (Der Ring des Nibelungen, 1848–1874)", "context": "Wagner's Ring Cycle is directly based on the Norse Eddic Sigurd cycle and the German Nibelungenlied — the Poetic Edda material was the immediate source for the most ambitious music drama in the Western tradition."},
      {"sourceSlug": "poetic-edda", "sourceName": "Poetic Edda (Völuspá, Dvergatal, Odin figure)", "verb": "INFLUENCES", "targetSlug": "tolkiens-middle-earth", "targetName": "Tolkien's Middle-earth (The Lord of the Rings, The Hobbit)", "context": "Tolkien drew directly on the Poetic Edda — Gandalf is modelled on the Eddic Odin (wandering old man with staff and wide hat), and the names of the dwarves in The Hobbit come directly from the Dvergatal in Völuspá."}
    ],
    "places": [
      {"name": "Iceland (Codex Regius c. 1270 CE; Árni Magnússon Institute, Reykjavik)", "role": "The Codex Regius containing the Poetic Edda was written in Iceland c. 1270 CE and is now preserved in the Árni Magnússon Institute in Reykjavik — Iceland's 13th-century manuscript tradition was the primary vehicle of preservation"},
      {"name": "Scandinavia and the Old Norse world (9th–13th century composition context)", "role": "The Poetic Edda's poems were composed in the Old Norse world (Scandinavia, Iceland) between the 9th and 13th centuries — reflecting the pre-Christian Norse mythological and heroic tradition"}
    ],
    "subjects": ["Norse Literature", "Medieval Era", "Old Norse", "Norse Mythology", "Epic Poetry", "Icelandic Literature", "Germanic Tradition", "Mythology"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Poetic Edda (Codex Regius, c. 1270 CE) is the primary source for Norse mythology and the Norse heroic tradition. Its influence on Wagner's Ring Cycle, Tolkien's Middle-earth, and contemporary popular culture (Marvel's Thor) demonstrates its extraordinary cultural reach. As the primary textual witness to pre-Christian Norse religion and mythology, it is one of the foundational documents of Northern European cultural identity.",
      "significanceCategory": "world-changing"
    }
  }
},

"natya-shastra": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780natya-shastra.json",
  "slug": "natya-shastra",
  "data": {
    "summary": "The Nāṭyaśāstra (Sanskrit: नाट्यशास्त्र, 'Treatise on Theatre/Drama') is an ancient Indian Sanskrit treatise on the performing arts — drama, dance, and music — attributed to the sage Bharata Muni and composed c. 200 BCE – 200 CE (dates are debated, with scholars placing the core text anywhere from the 2nd century BCE to the 4th century CE). It is the most comprehensive and authoritative ancient Indian treatise on the performing arts, covering the entire range of theatrical performance: the origin of drama (the 'fifth Veda', said to have been created by Brahma), the construction of the theatre (ranga), stagecraft (bhūmikā), acting technique (abhinaya), the theory of rasa (aesthetic emotion), music (svara), dance (nṛtta), costume, makeup, and the 36 subsidiary elements of theatrical production. The Nāṭyaśāstra contains approximately 6,000 verses across 36 chapters.\n\nThe Nāṭyaśāstra's most influential theoretical contribution is the Rasa theory — the analysis of the aesthetic experience of drama (and by extension all art) in terms of eight (later nine) rasas ('flavours', 'essences', 'aesthetic emotions'): śṛṅgāra (love, romance), hāsya (humour, comedy), karuṇa (pathos, sorrow), raudra (fury, wrath), vīra (heroism, courage), bhayānaka (terror, fear), bībhatsa (disgust, repugnance), adbhuta (wonder, amazement), and the later addition of śānta (peace, serenity). Each rasa is produced by specific determinants (vibhāva), consequents (anubhāva), and transitory emotions (vyabhicāribhāva) — a systematic analysis of how theatrical performance produces specific aesthetic responses in the spectator.\n\nThe Rasa theory became the foundational framework of Indian aesthetics — applied not only to drama and dance but to poetry (kāvya), music (sangīta), and the visual arts — and continues to be the primary theoretical framework for classical Indian performing arts, influencing the major systems of classical Indian dance (Bharatanatyam, Kathak, Odissi, Manipuri, Kuchipudi, Mohiniyattam, Kathakali, Sattriya) and the traditions of Indian classical theatre and music.",
    "causes": [
      "The Vedic sacrificial tradition and its dramatic re-enactments — the origin myth of the Nāṭyaśāstra itself traces drama to Brahma's creation of a 'fifth Veda' combining elements of the four Vedas — reflects the connection between Vedic ritual and early Indian theatrical performance: the Nāṭyaśāstra is partly a systematisation of the performance traditions embedded in Vedic ritual.",
      "The flourishing of Sanskrit drama in the classical period — the tradition of Sanskrit court drama by playwrights such as Bhāsa, Kālidāsa (Abhijñānaśākuntalam, Vikramorvaśīyam), Śūdraka (Mṛcchakaṭika), and Harsha — both reflected and generated the theoretical systematisation in the Nāṭyaśāstra: the treatise codifies the practice of Sanskrit classical drama.",
      "The Sanskrit grammatical and philosophical traditions — the practice of systematic treatise-writing (śāstra) in the Indian intellectual tradition, exemplified by Pāṇini's Aṣṭādhyāyī and the philosophical sūtras — provided the intellectual model for the Nāṭyaśāstra's comprehensive systematic analysis of theatrical performance."
    ],
    "effects": [
      "The Rasa theory became the foundational framework of Indian aesthetics — it was elaborated and debated by later theorists (Abhinavagupta's Abhinavabhāratī commentary, c. 1000 CE, is the most important theoretical development), applied to Sanskrit poetry (the rasa of kāvya), and remains the primary theoretical framework for classical Indian performing arts.",
      "The Nāṭyaśāstra's influence on the major traditions of classical Indian dance — Bharatanatyam's codified abhinaya (expressive gesture) system, the classification of gestures (mudrā/hasta), and the emotional range of the rasas are all grounded in the Nāṭyaśāstra — makes it the foundational textual authority for the living performing arts traditions of India.",
      "Abhinavagupta's 10th–11th century commentary on the Nāṭyaśāstra (Abhinavabhāratī) elaborated the Rasa theory into a comprehensive aesthetic philosophy — his analysis of the spectator's experience of rasa (sādharaṇīkaraṇa, 'generalisation') as a form of aesthetic consciousness continues to be debated in Indian aesthetics and influenced comparative aesthetics in the 20th century."
    ],
    "relationships": [
      {"sourceSlug": "bharata-muni", "sourceName": "Bharata Muni (legendary sage, Nāṭyaśāstra author)", "verb": "AUTHORS", "targetSlug": "natya-shastra", "targetName": "Nāṭyaśāstra (c. 200 BCE – 200 CE, ~6,000 verses, 36 chapters)", "context": "The Nāṭyaśāstra is attributed to the legendary sage Bharata Muni — a comprehensive treatise on drama, dance, and music composed c. 200 BCE–200 CE, the most authoritative ancient Indian treatise on the performing arts."},
      {"sourceSlug": "natya-shastra", "sourceName": "Nāṭyaśāstra (Rasa theory, 8/9 rasas, aesthetic emotions)", "verb": "ESTABLISHES", "targetSlug": "rasa-theory-indian-aesthetics", "targetName": "Rasa theory (Indian aesthetics, foundational framework)", "context": "The Nāṭyaśāstra's Rasa theory — the analysis of aesthetic experience in terms of eight (later nine) rasas — became the foundational framework of Indian aesthetics, applied to drama, poetry, music, and dance."},
      {"sourceSlug": "natya-shastra", "sourceName": "Nāṭyaśāstra (abhinaya, mudrā, classical dance authority)", "verb": "FOUNDATIONAL_TEXT_OF", "targetSlug": "classical-indian-dance", "targetName": "Classical Indian dance traditions (Bharatanatyam, Kathak, Odissi, etc.)", "context": "The Nāṭyaśāstra's codification of gesture (mudrā/hasta), abhinaya (expressive acting), and the rasa framework is the foundational textual authority for all major classical Indian dance traditions."}
    ],
    "places": [
      {"name": "India (Sanskrit court culture, c. 200 BCE – 200 CE; classical theatre context)", "role": "The Nāṭyaśāstra was composed in the Sanskrit court culture of ancient India — the same cultural context that produced the major Sanskrit dramatists (Bhāsa, Kālidāsa, Śūdraka) whose work it codifies"},
      {"name": "Indian subcontinent (living performing arts traditions — Tamil Nadu, Rajasthan, Odisha, Manipur)", "role": "The classical Indian dance traditions (Bharatanatyam in Tamil Nadu, Kathak in Rajasthan, Odissi in Odisha) all derive their theoretical framework from the Nāṭyaśāstra — the text's authority is pan-Indian across living performing arts"}
    ],
    "subjects": ["Sanskrit Literature", "Ancient Era", "Indian Performing Arts", "Aesthetics", "Drama Theory", "Indian Philosophy", "Dance Theory", "Classical India"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Nāṭyaśāstra (c. 200 BCE – 200 CE) is the most comprehensive and authoritative ancient Indian treatise on the performing arts and the foundational text of Indian aesthetics. Its Rasa theory became the primary framework for Indian aesthetic analysis — applied to drama, poetry, music, and dance — and its codification of gesture and abhinaya remains the textual authority for all major classical Indian dance traditions, making it a living theoretical foundation for the performing arts of one of the world's great civilisations.",
      "significanceCategory": "world-changing"
    }
  }
},

"quotations-from-chairman-mao-tse-tung": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780quotations-from-chairman-mao-tse-tung.json",
  "slug": "quotations-from-chairman-mao-tse-tung",
  "data": {
    "summary": "Quotations from Chairman Mao Tse-tung (Chinese: 毛主席语录, Máo Zhǔxí Yǔlù, 'Quotations from Chairman Mao'), widely known as the Little Red Book (小红书), is a collection of brief quotations from speeches and writings of Mao Zedong (1893–1976), Chairman of the Communist Party of China, compiled and published by the People's Liberation Army under the direction of Lin Biao (Mao's Defence Minister) and first distributed within the military in 1964. A mass civilian edition was published in 1966 at the start of the Cultural Revolution, and the book subsequently became the most published book in the history of the world: an estimated 5–6.5 billion copies were printed during the Cultural Revolution (1966–1976), making it by some measures the second most printed book after the Bible.\n\nThe Little Red Book contains 427 quotations from Mao's writings and speeches, organised by subject in 33 chapters covering topics such as the Communist Party, classes in Chinese society, the mass line, war and peace, imperialism, criticism and self-criticism, party discipline, and the cultural revolution. The quotations range from strategic political analysis to aphoristic wisdom, and the book was designed for easy memorisation and recitation: its physical format — small red vinyl cover, pocket-sized, with bold headings and short quotations — facilitated its use as a handbook for political education and as a ritual object in Cultural Revolution practice.\n\nDuring the Cultural Revolution, possession and constant reference to the Little Red Book was mandatory across China — reciting passages, 'studying' the book in group sessions, and waving it at political rallies were obligatory practices. The book's status as a quasi-sacred text of Communist China — used for collective oath-taking, displayed in homes and workplaces, and treated with near-religious reverence — made it one of the defining objects of 20th-century political culture and a paradigm case of the state-directed production of a political sacred text.",
    "causes": [
      "The Cultural Revolution (1966–1976) — Mao's political campaign to reassert his authority against the party bureaucracy by mobilising the Red Guards (student and youth militias) and purging 'capitalist roaders' and 'counter-revolutionaries' — created the political context for the mass distribution of the Little Red Book: it was the primary text of Cultural Revolution political indoctrination and the primary vehicle of the Maoist personality cult.",
      "Lin Biao's compilation and promotion of the Little Red Book — his initial distribution within the PLA in 1964 as a military political education text, and his subsequent championing of it as the indispensable guide to Mao Zedong Thought — was the direct institutional occasion for the book's creation and mass distribution.",
      "The mass mobilisation character of Chinese Communist Party politics under Mao — the consistent pattern of using mass political campaigns, education drives, and collective study sessions to implement ideological directives — provided the organisational infrastructure for the Little Red Book's mandatory mass distribution and use."
    ],
    "effects": [
      "The Cultural Revolution's mandatory use of the Little Red Book — the group recitation sessions, the waving of the red book at political rallies, the use of quotations as ideological touchstones — made it the most physically prominent object of 20th-century political culture and the paradigm case of a state-produced political cult object.",
      "The Little Red Book's global distribution during the 1960s–1970s — translated into over 60 languages and distributed to Third World liberation movements, New Left activists in Europe and North America, and communist parties worldwide — made it an icon of radical politics in the 1960s: Mao's Little Red Book was prominently displayed by student revolutionaries in Paris in May 1968.",
      "The Little Red Book's extraordinary print run (5–6.5 billion copies) redirected enormous resources of Chinese paper, printing, and publishing away from other uses during the Cultural Revolution — contributing to the cultural and educational destruction of the Cultural Revolution period and the suppression of other literary and intellectual production."
    ],
    "relationships": [
      {"sourceSlug": "mao-zedong", "sourceName": "Mao Zedong (1893–1976, Chairman of the CPC)", "verb": "AUTHORED_QUOTATIONS_IN", "targetSlug": "quotations-from-chairman-mao-tse-tung", "targetName": "Little Red Book (Quotations from Chairman Mao, first distributed 1964)", "context": "The Little Red Book compiles 427 quotations from Mao Zedong's writings and speeches, compiled under Lin Biao for PLA political education in 1964 — subsequently mass-distributed during the Cultural Revolution."},
      {"sourceSlug": "quotations-from-chairman-mao-tse-tung", "sourceName": "Little Red Book (5–6.5 billion copies, Cultural Revolution)", "verb": "MASS_PRODUCED_DURING", "targetSlug": "chinese-cultural-revolution", "targetName": "Chinese Cultural Revolution (1966–1976)", "context": "The Little Red Book was the primary text of Cultural Revolution political indoctrination — an estimated 5–6.5 billion copies were printed during 1966–1976, making it the most printed book in history after the Bible."},
      {"sourceSlug": "quotations-from-chairman-mao-tse-tung", "sourceName": "Little Red Book (Paris 1968, global radical politics)", "verb": "SYMBOL_OF", "targetSlug": "global-left-1960s", "targetName": "Global radical left and New Left politics (1960s–1970s)", "context": "The Little Red Book became an international icon of 1960s radical politics — displayed by student revolutionaries in Paris in May 1968 and distributed to Third World liberation movements and New Left groups worldwide."}
    ],
    "places": [
      {"name": "China (PLA distribution 1964; mass distribution during Cultural Revolution 1966–1976)", "role": "The Little Red Book was first distributed within the PLA in 1964 and subsequently mass-distributed across all of China during the Cultural Revolution — the mandatory 5–6.5 billion copy print run was a defining act of the Maoist political culture"},
      {"name": "Paris, France and global left (May 1968, New Left, Third World liberation movements)", "role": "The Little Red Book became a global icon of radical politics in the 1960s — prominently displayed by Paris student revolutionaries in May 1968 and distributed to liberation movements and communist parties worldwide"}
    ],
    "subjects": ["Chinese Literature", "Modern Era", "Mao Zedong", "Chinese Communism", "Cultural Revolution", "Political Text", "20th Century", "Chinese History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Little Red Book (1964/1966) is the most printed book in history after the Bible — 5–6.5 billion copies during the Cultural Revolution. As the primary text of Cultural Revolution political indoctrination and the vehicle of the Maoist personality cult, it shaped the lives of hundreds of millions of Chinese people. Its global distribution made it an international icon of 1960s radical politics. It is the definitive example of state-produced political sacred text and mass political indoctrination through printed material.",
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
