#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 29 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: cat-on-a-hot-tin-roof, euthyphro, epistle-to-the-galatians, gay-science,
          adventures-of-huckleberry-finn, a-thousand-splendid-suns,
          a-dialogue-of-comfort-against-tribulation-1534, a-game-of-thrones
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-29-may2026"

ENRICHMENTS = {

"cat-on-a-hot-tin-roof": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780cat-on-a-hot-tin-roof.json",
  "slug": "cat-on-a-hot-tin-roof",
  "data": {
    "summary": "Cat on a Hot Tin Roof is the play by Tennessee Williams (1911–1983), which premiered on Broadway at the Morosco Theatre on 24 March 1955 (directed by Elia Kazan, with Ben Gazzara as Brick and Barbara Bel Geddes as Maggie) and won the Pulitzer Prize for Drama in 1955 — his second after A Streetcar Named Desire (1947). Set on a Mississippi Delta plantation over a single evening, the play centres on the dysfunctional Pollitt family assembled to celebrate the birthday of Big Daddy (a cotton millionaire dying of cancer), the collision between his favourite son Brick (an alcoholic ex-footballer consumed by guilt over the death of his friend Skipper and unable to consummate his marriage) and Brick's wife Maggie (the 'cat on a hot tin roof' — restless, sexually frustrated, fighting for her place in the family and the inheritance). The play's central preoccupation is with mendacity — Big Daddy's deathbed declaration that 'mendacity is the system we live in' stands as the play's moral centre — and with the denied homoerotic love between Brick and Skipper, which Williams presents as the emotional truth that none of the characters can name or acknowledge.\n\nCat on a Hot Tin Roof is one of the most psychologically intense dramas in the American theatrical canon, and one of the most controversial in its original production: director Elia Kazan persuaded Williams to rewrite Act III to give Big Daddy a larger role and to soften Brick's psychological resolution, producing two versions of the play (the original, which Williams preferred; and the Broadway version, which is more commonly performed). The play's frank treatment of homosexuality — even in the oblique, unspoken form in which it appears — was daring for 1955 Broadway, and the 1958 film adaptation (with Paul Newman and Elizabeth Taylor) was required to suppress the homosexual subtext entirely by the Hollywood Production Code.\n\nWilliams's three great plays — The Glass Menagerie (1944), A Streetcar Named Desire (1947), and Cat on a Hot Tin Roof (1955) — collectively established him as the preeminent poet-dramatist of the American stage, and Cat on a Hot Tin Roof's treatment of desire, denial, and the lies by which families maintain their coherence at the cost of truth is his most psychologically complex achievement.",
    "causes": [
      "Williams's autobiographical experience of suppressed homosexuality — in 1950s America, when being gay required concealment — gave Cat on a Hot Tin Roof its central thematic preoccupation with the unspeakable desire that destroys Brick and Skipper's friendship, and its portrait of a family system maintained by mendacity rather than truth.",
      "The collaboration with Elia Kazan — who had directed both A Streetcar Named Desire (1947) and Death of a Salesman (1949) and whose directorial demands shaped the Broadway text of Cat on a Hot Tin Roof — gave the play its theatrical intensity and its revised Act III, though Williams's preferred text restores the darker original ending.",
      "The culture of post-war American masculinity — the 1950s ideal of the athletic, heterosexual male breadwinner, exemplified by Brick's sporting past and his failure to live up to its expectations — gave Cat on a Hot Tin Roof its specific social context: Brick's alcoholic paralysis is the price of a society in which his actual emotional life cannot be acknowledged."
    ],
    "effects": [
      "Cat on a Hot Tin Roof's treatment of homosexual desire (in the oblique, denied form in which it appears) was a significant moment in the gradual emergence of LGBT themes in American mainstream theatre — the play's insistence that Brick's grief over Skipper is the key to his psychological paralysis is the most prominent treatment of male homosexual love in American mainstream drama before the AIDS crisis.",
      "The two-version problem of Cat on a Hot Tin Roof — the tension between Williams's preferred text and the Kazan-revised Broadway version — has made the play a significant case study in the ethics of playwright-director collaboration and the question of authorial intent in theatrical production.",
      "Williams's three great plays of 1944–1955 — The Glass Menagerie, A Streetcar Named Desire, Cat on a Hot Tin Roof — established the American poetic drama tradition in which psychological intensity, lyrical language, and social critique combine in ways that influenced Sam Shepard, Lanford Wilson, and the subsequent development of American dramatic writing."
    ],
    "relationships": [
      {"sourceSlug": "tennessee-williams", "sourceName": "Tennessee Williams (1911–1983)", "verb": "AUTHORS", "targetSlug": "cat-on-a-hot-tin-roof", "targetName": "Cat on a Hot Tin Roof (1955)", "context": "Williams's second Pulitzer Prize-winning play — drawing on his autobiographical experience of suppressed homosexuality and his collaboration with Elia Kazan to produce his most psychologically complex dramatic achievement."},
      {"sourceSlug": "cat-on-a-hot-tin-roof", "sourceName": "Cat on a Hot Tin Roof", "verb": "EXPLORES", "targetSlug": "homosexuality-american-drama", "targetName": "Homosexual subtext in American mainstream drama (1950s)", "context": "The Brick–Skipper relationship — the denied homoerotic love that Williams presents as the psychological key to Brick's paralysis — was the most prominent treatment of male homosexual desire in American mainstream theatre before the AIDS crisis."},
      {"sourceSlug": "cat-on-a-hot-tin-roof", "sourceName": "Cat on a Hot Tin Roof (two versions)", "verb": "DEMONSTRATES", "targetSlug": "playwright-director-collaboration", "targetName": "Playwright-director collaboration in American theatre (Williams–Kazan)", "context": "The existence of two competing versions of Act III — Williams's preferred text and the Kazan-revised Broadway version — makes Cat on a Hot Tin Roof the most discussed case of authorial compromise in American theatrical history."}
    ],
    "places": [
      {"name": "Mississippi Delta (play's setting, 1950s)", "role": "The Pollitt cotton plantation in the Mississippi Delta — the Southern Gothic setting that Williams uses as the social and physical environment in which mendacity, desire, and family dynamics play out"},
      {"name": "Broadway, New York (24 March 1955 premiere)", "role": "The Morosco Theatre premiere of Cat on a Hot Tin Roof — directed by Elia Kazan, winning the Pulitzer Prize for Drama — running for 694 performances"}
    ],
    "subjects": ["American Drama", "Contemporary Era", "Tennessee Williams", "Theatre", "20th Century", "American Literature", "Southern Literature", "Drama"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Cat on a Hot Tin Roof (Tennessee Williams, 1955) won Williams his second Pulitzer Prize and is his most psychologically intense work — its treatment of suppressed homosexual desire, family mendacity, and the lies by which families maintain coherence at the cost of truth is the most complex achievement of the American poetic drama tradition. Together with A Streetcar Named Desire, it established Williams as the preeminent poet-dramatist of the American stage.",
      "significanceCategory": "highly-significant"
    }
  }
},

"euthyphro": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780euthyphro.json",
  "slug": "euthyphro",
  "data": {
    "summary": "The Euthyphro is a Socratic dialogue by Plato (c. 428–348 BCE), composed c. 399 BCE (shortly before the trial of Socrates, to which the dialogue's framing refers) — one of the most philosophically significant short dialogues in the Platonic corpus, and the locus classicus of a problem that has remained at the centre of the philosophy of religion for more than two millennia: the Euthyphro dilemma. The dialogue is set on the porch of the King-Archon in Athens, where Socrates encounters the seer Euthyphro — who is prosecuting his own father for impiety (having left a servant to die bound in a ditch while Euthyphro sought religious guidance) — and engages him in a discussion of the nature of piety (Greek: hosion) and impiety. Euthyphro offers several definitions of piety that Socrates systematically refutes, and the dialogue concludes without a successful definition — a classic aporetic ending.\n\nThe philosophical core of the Euthyphro is the dilemma Socrates poses at 10a: 'Is the pious beloved by the gods because it is pious, or is it pious because it is beloved by the gods?' — the Euthyphro dilemma. This question, in its theological form, asks whether what God commands is good because God commands it (the Divine Command Theory) or whether God commands what is good because it is independently good — a dilemma that strikes at the foundations of theistic ethics. If the former (Divine Command Theory), then morality is arbitrary — God could in principle command torture, and it would be good. If the latter, then goodness is independent of God's will, and God is constrained by an independent standard of goodness — apparently compromising divine omnipotence or making God unnecessary to ethics. This dilemma has been debated by theologians and philosophers from the medieval scholastics (Aquinas vs. Ockham) through Leibniz and Spinoza to contemporary metaethics.\n\nThe Euthyphro also serves as an introduction to Plato's theory of Forms — Socrates's demand for a single definition of piety that applies to all pious actions is his characteristic demand for the Form (the essence, the universal) rather than a list of examples — and as a portrait of Socratic method applied to a practical moral and religious problem in a recognisably Athenian context.",
    "causes": [
      "The imminent trial of Socrates on charges of impiety (asebeia) — prosecuted by Meletus, Anytus, and Lycon, and resulting in Socrates's execution in 399 BCE — gave the Euthyphro its framing urgency: Socrates, about to be tried for impiety, meets a man who prosecutes his own father for the same crime, and the dramatic irony of their mutual uncertainty about piety is the dialogue's dramatic engine.",
      "The tension in Greek religious thought between traditional piety (the performance of rituals demanded by the Olympian gods) and Socratic philosophy (the demand that moral claims be given reasoned justification) — exemplified by Socrates's daimonion (divine inner voice), which was one of the grounds of his prosecution — gave the dialogue its immediate social and philosophical context.",
      "Plato's programme of developing a philosophically defensible account of ethics against the Sophists' relativism — the Sophists claimed that justice and piety were merely conventional, varying by city and culture — gave the Euthyphro its systematic purpose: the demonstration that piety cannot be defined by reference to divine approval alone, without a prior independent standard of goodness."
    ],
    "effects": [
      "The Euthyphro dilemma is one of the most influential arguments in the history of philosophy of religion — its sharp formulation of the tension between divine command theory and independent moral standards has structured the debate between divine command theorists (Ockham, Scotus, modern evangelical ethics) and natural law theorists (Aquinas, Grotius, Leibniz) for 2,400 years.",
      "The dialogue's aporetic ending — Euthyphro's hurried departure without a successful definition of piety — is a paradigm of the Socratic method's negative function: the demonstration that apparent moral and religious certainty conceals profound confusion, and that the first step of philosophy is the acknowledgment of ignorance (Socratic aporia).",
      "Euthyphro's prosecution of his father for impiety is the first systematic dramatisation in Western literature of the tension between religious obligation and family loyalty — a tension that recurs in Antigone's conflict between divine and human law, in Paul's letter on faith versus works of the law, and in numerous subsequent philosophical and theological treatments of the conflict between religious and natural obligations."
    ],
    "relationships": [
      {"sourceSlug": "plato", "sourceName": "Plato (c. 428–348 BCE)", "verb": "AUTHORS", "targetSlug": "euthyphro", "targetName": "Euthyphro (c. 399 BCE)", "context": "Plato wrote the Euthyphro c. 399 BCE — shortly before the trial of Socrates — as one of the early 'Socratic' dialogues presenting Socrates in conversation with an interlocutor whose apparent certainty about moral or religious matters is systematically dissolved by Socratic questioning."},
      {"sourceSlug": "euthyphro", "sourceName": "Euthyphro (Euthyphro dilemma, 10a)", "verb": "ESTABLISHES", "targetSlug": "divine-command-theory-debate", "targetName": "Divine Command Theory vs. Natural Law debate in ethics", "context": "The Euthyphro dilemma ('Is the pious beloved by the gods because it is pious, or pious because it is beloved?') is the foundational formulation of the tension between divine command ethics and independent moral standards — a debate central to medieval scholasticism, Reformation ethics, and contemporary philosophy of religion."},
      {"sourceSlug": "euthyphro", "sourceName": "Euthyphro", "verb": "PRECEDES", "targetSlug": "apology-plato", "targetName": "Apology of Socrates (399 BCE)", "context": "The Euthyphro is set immediately before the trial of Socrates — the Apology being Plato's account of the trial itself — and the two dialogues are companion texts depicting the philosophical context of Socrates's confrontation with Athenian religious authority."}
    ],
    "places": [
      {"name": "Athens (porch of the King-Archon, c. 399 BCE)", "role": "The porch of the King-Archon in Athens — the magistrate's office where religious charges were registered — the setting of the Euthyphro, which dramatises Socrates's last philosophical conversation before his trial"},
      {"name": "Western philosophical tradition (ongoing influence)", "role": "The Euthyphro dilemma has been debated in every period of Western philosophical and theological thought — from the medieval scholastics through the Reformation to contemporary analytic philosophy of religion"}
    ],
    "subjects": ["Philosophy", "Classical Era", "Plato", "Socratic Dialogues", "Ancient Greece", "Philosophy of Religion", "Ethics", "Greek Philosophy"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Plato's Euthyphro (c. 399 BCE) is the locus classicus of the Euthyphro dilemma — the question whether morality is good because God commands it or whether God commands it because it is independently good — one of the most influential arguments in the history of the philosophy of religion. This dilemma has structured the debate between divine command theory and natural law ethics for 2,400 years.",
      "significanceCategory": "highly-significant"
    }
  }
},

"epistle-to-the-galatians": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780epistle-to-the-galatians.json",
  "slug": "epistle-to-the-galatians",
  "data": {
    "summary": "The Epistle to the Galatians is a letter written by the Apostle Paul (c. 5–67 CE) to the Christian communities of Galatia (in central Asia Minor, modern Turkey), probably c. 48–55 CE — one of the most theologically significant and polemically charged texts in the New Testament, and the founding document of the Pauline doctrine of justification by faith alone (sola fide) that became the theological core of the Protestant Reformation. The letter is written in response to the influence of Jewish-Christian teachers ('Judaizers') who were insisting that gentile converts to Christianity must also observe the Torah (particularly circumcision) in order to be saved; Paul's furious response — 'If anyone is preaching to you a gospel contrary to the one you received, let him be accursed' (Galatians 1:9) — is the most polemical opening in the New Testament.\n\nGalatians 3:28 contains one of the most radical statements of spiritual equality in the ancient world: 'There is neither Jew nor Greek, there is neither slave nor free man, there is neither male nor female; for you are all one in Christ Jesus' — a passage that has been foundational for Christian arguments for racial equality, the abolition of slavery, and gender equality across two millennia, even as its practical application has been hotly contested. Paul's autobiographical account in chapters 1–2 — his conversion experience, his visit to Jerusalem, and his confrontation of Peter at Antioch ('I opposed him to his face, for he stood condemned') — is the primary source for the history of the earliest Christian communities and the tensions between Pauline Christianity and the Jerusalem church.\n\nMartin Luther's intensive study of Galatians during his preparation of his Lectures on Galatians (1519) was the central moment of the Protestant Reformation's theological formation — Luther said of Galatians that it was his 'Kate von Bora' (his wife, the person he loved most), and his commentary on the letter established sola fide as the formal principle of Reformation theology. Calvin's commentary on Galatians similarly shaped Reformed theology's understanding of grace, faith, and the law.",
    "causes": [
      "The crisis in the Galatian churches caused by the Judaizers — the Jewish-Christian missionaries (possibly from Jerusalem) who insisted that gentile converts must observe the Mosaic Law to be saved — provoked Paul's most polemical and theologically concentrated letter, forcing him to articulate the foundational principle of his mission: that faith in Christ, not observance of the Torah, is the basis of salvation.",
      "Paul's personal theological development — his conviction that his Damascus Road experience (Galatians 1:15–16: 'God set me apart before I was born and called me through his grace, to reveal his Son to me, in order that I might preach him among the Gentiles') had given him a direct revelation of the gospel independent of human tradition — gave Galatians its autobiographical intensity and its assertion of apostolic authority.",
      "The conflict between Pauline Christianity (the gospel for the Gentiles, freedom from the Torah) and Jerusalem Christianity (represented by James, Peter, and the conservative Jewish-Christian community) — described in Galatians 2's account of the Jerusalem conference and the Antioch incident — is the foundational crisis of early Christian history, and Galatians is its primary documentary evidence."
    ],
    "effects": [
      "Martin Luther's rediscovery of Paul's doctrine of justification by faith alone in Galatians — 'I have been crucified with Christ; it is no longer I who live, but Christ who lives in me; and the life I now live in the flesh I live by faith in the Son of God' (Galatians 2:20) — was the theological foundation of the Protestant Reformation, making Galatians arguably the most historically consequential New Testament epistle.",
      "Galatians 3:28 ('neither Jew nor Greek, neither slave nor free, neither male nor female') has been the most-cited New Testament text in arguments for human equality across racial, class, and gender lines — cited by abolitionists, suffragists, and advocates of racial equality as the foundational Christian statement of universal human dignity.",
      "Paul's assertion of his independent apostolic authority (derived from direct revelation, not human tradition) in Galatians established the model of the individual conscience against institutional authority that runs through Luther's 'Here I stand' and the entire Protestant tradition — making Galatians a foundational text of the Western tradition of individual religious conscience against communal authority."
    ],
    "relationships": [
      {"sourceSlug": "paul-the-apostle", "sourceName": "Paul the Apostle (c. 5–67 CE)", "verb": "AUTHORS", "targetSlug": "epistle-to-the-galatians", "targetName": "Epistle to the Galatians (c. 48–55 CE)", "context": "Paul wrote Galatians in response to the Judaizers who were undermining his mission among the Gentiles — the most polemical of his letters and the one that most directly articulates his doctrine of justification by faith."},
      {"sourceSlug": "epistle-to-the-galatians", "sourceName": "Galatians (sola fide)", "verb": "INSPIRES", "targetSlug": "protestant-reformation", "targetName": "Protestant Reformation (Luther's doctrine of justification by faith alone)", "context": "Martin Luther's lectures on Galatians (1519) were the central moment of the Reformation's theological formation — his doctrine of sola fide (justification by faith alone) is drawn directly from Paul's argument in Galatians."},
      {"sourceSlug": "epistle-to-the-galatians", "sourceName": "Galatians 3:28", "verb": "CITED_BY", "targetSlug": "abolitionism", "targetName": "Abolitionist movement (Christian arguments against slavery)", "context": "'There is neither Jew nor Greek, neither slave nor free, neither male nor female; for you are all one in Christ Jesus' (Galatians 3:28) has been the most-cited New Testament text in Christian arguments for racial equality and the abolition of slavery."}
    ],
    "places": [
      {"name": "Galatia, Asia Minor (c. 48–55 CE, recipient communities)", "role": "The Christian communities of Galatia (central Asia Minor, modern Turkey) to whom Paul addressed the letter — predominantly gentile converts threatened by the Judaizer mission"},
      {"name": "European Reformation (16th century, transformative reception)", "role": "Luther's Germany — where intensive study of Galatians (1519) became the theological foundation of the Protestant Reformation and transformed the religious history of Europe"}
    ],
    "subjects": ["Christian Theology", "Classical Era", "New Testament", "Paul the Apostle", "Christianity", "Religious Texts", "Reformation", "Biblical Literature"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Epistle to the Galatians (Paul, c. 48–55 CE) is the founding document of the doctrine of justification by faith alone — the theological core of the Protestant Reformation. Luther's intensive study of Galatians (1519) was the central moment of Reformation theology; Galatians 3:28 is the most-cited New Testament text in arguments for human equality. No other New Testament epistle has been more directly consequential for the political and religious history of Western civilization.",
      "significanceCategory": "world-changing"
    }
  }
},

"gay-science": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780gay-science.json",
  "slug": "gay-science",
  "data": {
    "summary": "The Gay Science (German: Die fröhliche Wissenschaft) is the philosophical aphorism collection by Friedrich Nietzsche (1844–1900), first published in 1882 (Books I–IV) with a fifth book added in the 1887 second edition — the text in which Nietzsche first articulates his most famous and provocative ideas: the proclamation that 'God is dead' (Section 125, 'The Madman'), the concept of the 'eternal recurrence' (Section 341, 'The Greatest Heavy Burden'), and the first appearance of the character Zarathustra (Section 342, 'Incipit tragoedia' — 'The tragedy begins'), which anticipates Thus Spoke Zarathustra (1883–1885). The title is taken from the Provençal term gaya scienza — the art of the troubadours, the 'joyful wisdom' of those who celebrate life in verse and music — and reflects Nietzsche's aspiration to a philosophy that affirms life with joy rather than burdening it with metaphysical gravity.\n\nSection 125 of The Gay Science — 'The Madman' — is one of the most celebrated passages in 19th-century philosophy: a madman runs through the marketplace crying 'God is dead! God remains dead! And we have killed him!' — not as a simple atheistic announcement (Nietzsche assumes his audience no longer believes in God) but as a proclamation of cultural crisis: the death of God means the death of the entire system of metaphysical and moral values that Western civilisation had derived from the Christian tradition. The question is what values will replace them — and whether humanity can bear the weight of creating new values in a world without transcendent foundations. This is the problem that Nietzsche's entire subsequent philosophy addresses.\n\nSection 341 — 'The Greatest Heavy Burden' — presents the thought experiment of eternal recurrence: if a demon told you that you must live your life again, exactly as you have lived it, infinitely many times, how would you react? — and proposes that the affirmation of eternal recurrence is the test of one's ability to affirm life absolutely, the touchstone of the Nietzschean ideal of the person who loves life so completely that they would wish to live it again forever. These ideas — the death of God, the eternal recurrence, the Übermensch as the human response to the challenge of living without God — are the philosophical core of Nietzsche's mature work.",
    "causes": [
      "Nietzsche's personal liberation from his Wagnerian discipleship — the decisive break with Richard Wagner (which he had been working through since Human All Too Human, 1878) — freed him for the affirmative, life-celebrating philosophy of The Gay Science, which was written in the period of his full independence and his embrace of the 'free spirit' ideal.",
      "Nietzsche's recovery from a severe illness (1881–1882) — during which he experienced what he described as a series of revelatory insights, including the first formulation of the eternal recurrence in August 1881 at Sils-Maria, Switzerland — gave The Gay Science its ecstatic, revelatory quality and its sense of ideas arriving with the force of inspiration rather than systematic philosophical derivation.",
      "The late 19th-century crisis of European Christianity — the progressive de-Christianisation of educated European culture under the impact of scientific materialism, Darwinian evolution, and biblical criticism — provided the cultural context within which Nietzsche's proclamation of the 'death of God' was received not as naive atheistic provocation but as the philosophical recognition of a cultural fact already partly accomplished."
    ],
    "effects": [
      "The Gay Science's Section 125 — 'God is dead! God remains dead! And we have killed him!' — became the most widely cited philosophical statement of the 19th century and has shaped the cultural self-understanding of Western secular modernity, from existentialist theology (the 'Death of God' theology of the 1960s) through nihilism to postmodern philosophy.",
      "The concept of eternal recurrence — as Nietzsche develops it from The Gay Science through Thus Spoke Zarathustra and beyond — became the central thought experiment of 20th-century existentialist philosophy, influencing Heidegger's analysis of 'being-toward-death', Camus's The Myth of Sisyphus, and the existentialist tradition's engagement with the question of how to affirm life in the absence of transcendent meaning.",
      "The Gay Science's 'Incipit tragoedia' section — the first appearance of Zarathustra — launched the process that produced Thus Spoke Zarathustra (1883–1885), Nietzsche's most influential work, and established the figure of Zarathustra as the philosopher who descends from his solitude to teach the Übermensch and the eternal recurrence to a humanity that does not yet know how to hear them."
    ],
    "relationships": [
      {"sourceSlug": "friedrich-nietzsche", "sourceName": "Friedrich Nietzsche (1844–1900)", "verb": "AUTHORS", "targetSlug": "gay-science", "targetName": "The Gay Science (1882, second edition 1887)", "context": "Nietzsche wrote the first four books of The Gay Science in 1882, following his break with Wagner and a period of serious illness — adding the fifth book in 1887 after the critical and commercial failure of Thus Spoke Zarathustra."},
      {"sourceSlug": "gay-science", "sourceName": "Gay Science Section 125", "verb": "ANNOUNCES", "targetSlug": "death-of-god", "targetName": "Death of God (Nietzsche's cultural proclamation)", "context": "'The Madman' in Section 125 — 'God is dead! God remains dead! And we have killed him!' — is Nietzsche's most famous proclamation: not of atheism, but of cultural crisis — the collapse of the metaphysical and moral system derived from Christian theism."},
      {"sourceSlug": "gay-science", "sourceName": "Gay Science Section 342 (Incipit tragoedia)", "verb": "PRECEDES", "targetSlug": "thus-spoke-zarathustra", "targetName": "Thus Spoke Zarathustra (1883–1885)", "context": "Section 342 of The Gay Science is the first appearance of the character Zarathustra — 'Incipit tragoedia' (the tragedy begins) — directly anticipating the philosophical drama of Thus Spoke Zarathustra."}
    ],
    "places": [
      {"name": "Sils-Maria, Engadin, Switzerland (August 1881, eternal recurrence insight)", "role": "The village in the Swiss Alps where Nietzsche had the insight of eternal recurrence in August 1881 — which he recorded in a notebook and developed into Section 341 of The Gay Science"},
      {"name": "Genoa (1881–1882, composition context)", "role": "Nietzsche wrote most of The Gay Science in Genoa during the winter of 1881–1882 — the Mediterranean climate that he associated with intellectual clarity and affirmative philosophy"}
    ],
    "subjects": ["Philosophy", "Modern Era", "Nietzsche", "Existentialism", "19th Century", "Continental Philosophy", "German Philosophy", "Atheism"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Gay Science (Nietzsche, 1882/1887) is the text in which Nietzsche first proclaimed the death of God, formulated the eternal recurrence, and introduced Zarathustra — the three central ideas of his mature philosophy. 'God is dead! God remains dead! And we have killed him!' has become the most cited philosophical statement of the 19th century and has shaped the cultural self-understanding of Western secular modernity.",
      "significanceCategory": "world-changing"
    }
  }
},

"adventures-of-huckleberry-finn": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783adventures-of-huckleberry-finn.json",
  "slug": "adventures-of-huckleberry-finn",
  "data": {
    "summary": "Adventures of Huckleberry Finn is the novel by Mark Twain (Samuel Langhorne Clemens, 1835–1910), published in the United Kingdom in December 1884 and in the United States in February 1885 — widely regarded as the greatest American novel, and described by Ernest Hemingway in 1935 as the book from which 'all modern American literature' comes. The novel follows Huckleberry Finn — the son of the town drunk, a boy outside the constraints of 'civilised' society — and Jim, the enslaved man who is fleeing from his owner Miss Watson (who intends to sell him South), as they travel down the Mississippi River on a raft. The novel's moral and emotional climax comes in Chapter 31, when Huck writes a letter to Miss Watson revealing Jim's location — and then tears it up, saying 'All right, then, I'll go to hell' — choosing his personal loyalty to Jim over the religious, social, and legal values of the slave society in which he has been raised, in one of the most celebrated moral decisions in American fiction.\n\nHuckleberry Finn is the first great American novel written in the vernacular voice of its protagonist — the colloquial, ungrammatical, rhythmically precise voice of Huck Finn is the model for American literary vernacular from Hemingway through Salinger's Holden Caulfield to contemporary American fiction. The novel's satirical portrait of antebellum Southern society — its hypocrisy, its violence, its sentimental religiosity deployed to justify the brutal institution of slavery — is the most devastating critique in American fiction, and Jim's dignity, intelligence, and humanity are presented in ways that subvert the racist stereotypes of Twain's own culture.\n\nHuckleberry Finn has been simultaneously celebrated as the founding masterpiece of American literature and subjected to continuous controversy — banned from library shelves from its initial publication (by the Concord Public Library in 1885, which called it 'trash') through the 20th century for its language (its use of the word 'nigger', which appears 219 times), its coarse vernacular, and its moral unconventionality. The debate about the novel's racial politics — whether its portrait of Jim reinforces or subverts racial stereotypes, and particularly whether Tom Sawyer's cruel 'evasion' chapters at the novel's end undermine its earlier moral seriousness — remains one of the most contested questions in American literary criticism.",
    "causes": [
      "Twain's own childhood in Hannibal, Missouri — a slaveholding town on the Mississippi — and his adult retrospective recognition of slavery's horror, mediated through his friendship with the freed slave George Griffin and his developing racial conscience, gave Huckleberry Finn its autobiographical moral intensity and its portrait of antebellum Missouri through the distancing perspective of a morally confused but fundamentally decent boy.",
      "The vernacular tradition of American Southwestern humour — the comedic genre of violent, exaggerated, coarsely funny tales from the frontier South, represented by writers like George Washington Harris (Sut Lovingood) and Johnson Jones Hooper — provided the literary tradition from which Twain developed Huck's narrative voice, transforming the Southwestern vernacular from comedy to moral seriousness.",
      "The post-Reconstruction crisis of American racial politics — the betrayal of the freed slaves' hopes in the 1870s–1880s, the rise of Jim Crow laws, and the progressive resegregation of the South — gave Huckleberry Finn (published 1885) its political urgency: Twain's portrait of slavery was simultaneously historical fiction and a comment on the racial politics of his own time."
    ],
    "effects": [
      "Hemingway's famous declaration (Green Hills of Africa, 1935) that 'all modern American literature comes from one book by Mark Twain called Huckleberry Finn' is the most influential statement of the novel's foundational role in American literary history — Hemingway, Faulkner, Steinbeck, and Salinger all explicitly acknowledge Huck's vernacular voice as the model for American literary prose.",
      "The novel's controversy — its continuous banning and challenge from 1885 to the present, on grounds ranging from coarseness to racism — has made Huckleberry Finn the most frequently banned novel in American schools and the most debated text in the American literary curriculum, raising fundamental questions about the relationship between literary value and racial representation.",
      "Huck's decision to 'go to hell' rather than betray Jim — his rejection of the religious and social values of slave society in favour of personal moral loyalty — became the canonical American literary expression of moral conscience against social conformity, influencing the American literary tradition's engagement with the individual conscience against unjust social norms."
    ],
    "relationships": [
      {"sourceSlug": "mark-twain", "sourceName": "Mark Twain (1835–1910)", "verb": "AUTHORS", "targetSlug": "adventures-of-huckleberry-finn", "targetName": "Adventures of Huckleberry Finn (1884/1885)", "context": "Twain wrote Huckleberry Finn over seven years (1876–1883), drawing on his Hannibal, Missouri childhood and developing Huck's vernacular voice as the vehicle for his most sustained moral and satirical achievement."},
      {"sourceSlug": "adventures-of-huckleberry-finn", "sourceName": "Huckleberry Finn", "verb": "ESTABLISHES", "targetSlug": "american-vernacular-novel", "targetName": "American vernacular novel (Hemingway's 'all modern American literature')", "context": "Hemingway's 1935 declaration that 'all modern American literature comes from one book by Mark Twain called Huckleberry Finn' identifies Huck's colloquial voice as the foundational model for American prose style."},
      {"sourceSlug": "adventures-of-huckleberry-finn", "sourceName": "Huck Finn (Chapter 31 decision)", "verb": "DRAMATISES", "targetSlug": "moral-conscience-vs-convention", "targetName": "Individual moral conscience against social convention", "context": "Huck's decision to tear up the letter reporting Jim's location — 'All right, then, I'll go to hell' — choosing personal loyalty to Jim over religious and social obligation — is the canonical literary expression of individual moral conscience against unjust social norms."}
    ],
    "places": [
      {"name": "Mississippi River and Missouri (narrative setting, antebellum period)", "role": "The Mississippi River — the central fact of Twain's childhood and the symbolic axis of American geography — provides the novel's setting and its freedom metaphor: Huck and Jim are free on the river, enslaved by society on shore"},
      {"name": "Hannibal, Missouri (Twain's childhood, biographical source)", "role": "Twain's hometown of Hannibal, Missouri — the original of the fictional St. Petersburg and Pokeville — whose slaveholding society provided the autobiographical material for Huckleberry Finn's portrait of antebellum Missouri"}
    ],
    "subjects": ["American Literature", "Classical Era", "Mark Twain", "American Fiction", "19th Century", "Race in Literature", "Mississippi River", "Slavery"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Adventures of Huckleberry Finn (Twain, 1884/1885) is the foundational text of American literature — Hemingway's declaration that 'all modern American literature comes from one book by Mark Twain called Huckleberry Finn' identifies its vernacular voice and moral seriousness as the origin point of American prose fiction. Huck's decision to 'go to hell' rather than betray Jim is the canonical American literary expression of individual conscience against social injustice.",
      "significanceCategory": "world-changing"
    }
  }
},

"a-thousand-splendid-suns": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783a-thousand-splendid-suns.json",
  "slug": "a-thousand-splendid-suns",
  "data": {
    "summary": "A Thousand Splendid Suns is the novel by Khaled Hosseini (born 1965), published in May 2007 — his second novel after The Kite Runner (2003) — and a #1 New York Times bestseller that remained on the bestseller list for more than a year, selling over four million copies in the United States alone. The novel follows two Afghan women — Mariam, an illegitimate girl from Herat, and Laila, a girl from Kabul — whose lives intersect when both are forced into marriage with the same abusive man, Rasheed, across the backdrop of thirty years of Afghan history: from the relative modernism of the pre-Soviet period through the Soviet occupation (1979–1989), the Mujahideen civil war (1989–1996), the Taliban regime (1996–2001), and the American invasion and its aftermath. The title comes from a 17th-century poem about Kabul by Saib-e-Tabrizi: 'One could not count the moons that shimmer on her roofs / And the thousand splendid suns that hide behind her walls.'\n\nA Thousand Splendid Suns is the most widely read literary account of Afghan women's experience under the Taliban — its portrait of Mariam and Laila's suffering under Rasheed (whose abusive household mirrors the Taliban's treatment of women at the national level) and their solidarity, love, and eventual mutual liberation is both a personal story of survival and a political indictment of the Taliban's systematic oppression of women. The novel's empathetic, detailed portrayal of Afghan civilian life across three decades of war, displacement, and occupation — the loss of family, the destruction of Kabul, the desperate daily existence of ordinary Afghans — gave Western readers a personal human perspective on a country they had heard of primarily in terms of geopolitical strategy.\n\nHosseini's two Afghanistan novels — The Kite Runner and A Thousand Splendid Suns — have done more to shape the Western popular understanding of Afghanistan than any other literary works, and their commercial success established a new template for the 'literary witness' novel that combines personal narrative with political documentation of humanitarian crisis.",
    "causes": [
      "Hosseini's own experience as an Afghan exile — born in Kabul, his family sought asylum in the United States in 1980 after the Soviet invasion, and he became a US citizen in 1989 — gave A Thousand Splendid Suns its autobiographical emotional foundation and the specific knowledge of Afghan culture, society, and history that grounds its narrative.",
      "The renewed Western attention to Afghanistan following the September 11 2001 attacks and the subsequent American invasion — and the specific attention to the Taliban's treatment of Afghan women as a justification for military intervention — created both the political context and the literary market for a novel that gave Afghan women's experience human particularity.",
      "The success of The Kite Runner (2003) — which sold 12 million copies worldwide and established Hosseini as the literary voice of Afghan experience for Western readers — created the audience and the cultural context for A Thousand Splendid Suns, and Hosseini's deliberate decision to focus on women's experience (in contrast to The Kite Runner's male perspective) gave the second novel its specific political focus."
    ],
    "effects": [
      "A Thousand Splendid Suns became the primary literary representation of Afghan women's experience under the Taliban for Western readers — its emotional power and narrative accessibility gave millions of readers in the United States and Europe a personal understanding of the human cost of the Taliban regime that no journalistic or historical account had achieved.",
      "The novel's commercial success — combined with The Kite Runner — established Hosseini as the most commercially successful author of 'literary witness' fiction from the Islamic world for Western audiences, and contributed to the development of the literary market for novels about the human experience of war and occupation in Afghanistan, Iraq, and other conflict zones.",
      "Hosseini's Khaled Hosseini Foundation — established in 2008 partly with proceeds from A Thousand Splendid Suns — has funded humanitarian projects for Afghan women and families, making the novel's commercial success directly consequential for the people whose experience it represents."
    ],
    "relationships": [
      {"sourceSlug": "khaled-hosseini", "sourceName": "Khaled Hosseini (born 1965)", "verb": "AUTHORS", "targetSlug": "a-thousand-splendid-suns", "targetName": "A Thousand Splendid Suns (2007)", "context": "Hosseini wrote A Thousand Splendid Suns as his second Afghanistan novel — drawing on his experience as an Afghan exile in the United States to portray Afghan women's experience across thirty years of war and Taliban rule."},
      {"sourceSlug": "a-thousand-splendid-suns", "sourceName": "A Thousand Splendid Suns", "verb": "DOCUMENTS", "targetSlug": "taliban-regime-afghanistan", "targetName": "Taliban regime in Afghanistan (1996–2001)", "context": "The novel's central sections, set during the Taliban period, are the most widely read literary account of the Taliban's systematic oppression of women — its mandatory burqa, prohibition of education and employment, and systematic domestic violence."},
      {"sourceSlug": "a-thousand-splendid-suns", "sourceName": "A Thousand Splendid Suns (with The Kite Runner)", "verb": "SHAPES_PERCEPTION_OF", "targetSlug": "afghanistan", "targetName": "Western understanding of Afghanistan", "context": "Hosseini's two Afghanistan novels have done more to shape the Western popular understanding of Afghanistan than any other literary works — giving millions of Western readers a personal human perspective on a country they had previously known only through geopolitical news coverage."}
    ],
    "places": [
      {"name": "Kabul and Herat, Afghanistan (1970s–2000s, narrative setting)", "role": "The novel traces the destruction of Kabul — from the vibrant, relatively modern city of the 1970s through the Soviet occupation, the Mujahideen civil war, and the Taliban period — as the backdrop to Mariam and Laila's stories"},
      {"name": "United States (Hosseini exile, literary reception)", "role": "Hosseini wrote A Thousand Splendid Suns as an Afghan-American living in California — the novel's Western success established it as the primary literary mediation of Afghan experience for an American and European readership"}
    ],
    "subjects": ["Contemporary Literature", "Contemporary Era", "Afghan Literature", "Women's History", "War Literature", "Khaled Hosseini", "21st Century", "Humanitarian Fiction"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "A Thousand Splendid Suns (Hosseini, 2007) is the most widely read literary account of Afghan women's experience under the Taliban — its emotional portrayal of Mariam and Laila's suffering and solidarity gave millions of Western readers a personal human perspective on Afghanistan that no journalistic account had achieved. Together with The Kite Runner, it has shaped the Western popular understanding of Afghan history and culture more than any other literary work.",
      "significanceCategory": "significant"
    }
  }
},

"a-dialogue-of-comfort-against-tribulation-1534": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781a-dialogue-of-comfort-against-tribulatio.json",
  "slug": "a-dialogue-of-comfort-against-tribulation-1534",
  "data": {
    "summary": "A Dialogue of Comfort Against Tribulation is the prose work by Sir Thomas More (1478–1535), written in 1534 while More was imprisoned in the Tower of London awaiting trial and execution for his refusal to swear the Oath of Supremacy recognising Henry VIII as Supreme Head of the Church of England — one of the most remarkable works of Christian consolation literature in the English language, written in the full knowledge that the author would almost certainly be executed. The dialogue is cast in the form of a conversation between two Hungarian cousins, Vincent and Anthony, set in the context of the Turkish threat to Hungary (following the Ottoman victory at Mohács in 1526) — a transparent allegorical displacement of More's own situation, as the Turk threatening Hungary represents the king threatening More's conscience and life. Anthony — the elder, wiser cousin who counsels courage and acceptance of martyrdom — is clearly More's self-presentation.\n\nA Dialogue of Comfort draws on the entire tradition of classical and Christian consolation literature — Boethius's Consolation of Philosophy (written, like More's text, in prison awaiting execution), Seneca's consolatory letters, and the Christian tradition of imitatio Christi (following Christ through suffering) — and applies them to the specific situation of a man facing death for the sake of his religious conscience. More's argument is that tribulation (suffering) is not a punishment to be feared but a gift to be embraced: it strengthens virtue, cleanses sin, conforms the sufferer to Christ's passion, and is the pathway to eternal life. The work is remarkable for its combination of theological argument, classical learning, practical psychology, and occasional gentle humour — More's wit does not desert him even in the shadow of death.\n\nA Dialogue of Comfort Against Tribulation is one of the most significant works of English Renaissance prose — important both as a literary achievement and as a biographical document of extraordinary moral courage. It was written alongside More's other Tower works (a Treatise on the Passion, a Treatise to Receive the Blessed Body of Our Lord), and together they constitute the most sustained literary expression of principled resistance to royal tyranny in English history.",
    "causes": [
      "More's imprisonment in the Tower of London from 17 April 1534 — following his refusal to swear the Oath of Supremacy — and his full understanding that his refusal would likely result in his execution under the Treason Act gave the Dialogue of Comfort its specific existential context: a work of intellectual and spiritual preparation for death written by a man who knew he was going to die.",
      "The tradition of consolation literature — classical (Boethius's Consolation of Philosophy, Seneca's letters) and Christian (the imitatio Christi tradition of Thomas à Kempis) — provided More with the literary models and the intellectual resources from which to construct his own consolation, giving the work its learned, intertextual character.",
      "The allegorical displacement of More's London situation onto Hungarian cousins discussing the Turkish threat — a transparent fiction that allowed More to write about his own situation without naming it directly — provided the legal and psychological protection of indirection, as More could not safely write a direct account of his conflict with Henry VIII."
    ],
    "effects": [
      "A Dialogue of Comfort Against Tribulation is one of the founding texts of English Renaissance prose — its combination of classical learning, Christian theology, and vernacular English style contributed to the development of the English literary essay and the tradition of prose meditation that runs through Francis Bacon, John Donne, and Jeremy Taylor.",
      "More's canonisation by the Catholic Church in 1935 — on the 400th anniversary of his execution — was partly grounded in the Tower writings, including the Dialogue of Comfort, which established his intellectual and spiritual credentials for martyrdom: the Dialogue is the most sustained literary evidence of the thought and courage of England's most significant martyr of the Reformation.",
      "The work's argument for the acceptance of tribulation as spiritually valuable — drawing on classical Stoic and Christian consolation traditions — contributed to the development of the English martyrological tradition and the consolation literature produced during the religious conflicts of the 16th and 17th centuries."
    ],
    "relationships": [
      {"sourceSlug": "thomas-more", "sourceName": "Thomas More (1478–1535)", "verb": "AUTHORS", "targetSlug": "a-dialogue-of-comfort-against-tribulation-1534", "targetName": "A Dialogue of Comfort Against Tribulation (1534)", "context": "More wrote the Dialogue of Comfort in the Tower of London during 1534, while awaiting trial for refusing to swear the Oath of Supremacy — one of the most remarkable literary works produced under the immediate threat of execution in English history."},
      {"sourceSlug": "a-dialogue-of-comfort-against-tribulation-1534", "sourceName": "Dialogue of Comfort", "verb": "DRAWS_FROM", "targetSlug": "consolation-of-philosophy-boethius", "targetName": "Boethius's Consolation of Philosophy (524 CE)", "context": "More's Dialogue draws explicitly on Boethius's Consolation — itself written in prison awaiting execution — as its most direct literary model for the genre of consolation philosophy in the face of death for conscience's sake."},
      {"sourceSlug": "a-dialogue-of-comfort-against-tribulation-1534", "sourceName": "Dialogue of Comfort", "verb": "DOCUMENTS", "targetSlug": "english-reformation-conflict", "targetName": "English Reformation conflict between Henry VIII and Thomas More", "context": "The Dialogue of Comfort is the primary literary document of More's principled resistance to Henry VIII's Act of Supremacy — written in the Tower while awaiting the execution that resulted from that resistance."}
    ],
    "places": [
      {"name": "Tower of London (1534, composition)", "role": "More wrote A Dialogue of Comfort in the Tower of London between April 1534 and his trial in July 1535 — the prison that became the site of his most significant literary achievements and his preparation for martyrdom"},
      {"name": "Allegorical Hungary (narrative setting)", "role": "More displaced his London situation onto fictional Hungary under Turkish threat — a transparent allegory that allowed him to write about his own situation without naming Henry VIII or directly addressing the Act of Supremacy"}
    ],
    "subjects": ["English Literature", "Early Modern Era", "Thomas More", "Reformation", "Consolation Literature", "English Renaissance", "Martyrdom", "Catholic Church"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "A Dialogue of Comfort Against Tribulation (Thomas More, 1534) is one of the most remarkable works of English Renaissance prose — written in the Tower of London as More prepared for his execution for refusing to recognize Henry VIII's supremacy over the Church. Its combination of classical learning, Christian theology, and vernacular English style made it a founding text of English prose meditation and a primary document of the English Reformation's most significant martyrdom.",
      "significanceCategory": "significant"
    }
  }
},

"a-game-of-thrones": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783a-game-of-thrones.json",
  "slug": "a-game-of-thrones",
  "data": {
    "summary": "A Game of Thrones is the first volume of the epic fantasy series A Song of Ice and Fire by George R.R. Martin (born 1948), published in August 1996 by Bantam Books — the founding text of one of the most commercially successful and culturally influential fantasy series in the history of the genre, which has sold over 90 million copies worldwide and was adapted into the HBO television series Game of Thrones (2011–2019), one of the most-watched television series in history. Set in the fictional medieval world of Westeros — a continent in which seasons last for years and supernatural threats lurk beyond an enormous northern wall — A Game of Thrones follows multiple interleaved storylines: the honourable Ned Stark, Lord of Winterfell, drawn into the political intrigue of the royal court; Daenerys Targaryen, exiled princess and heir to the dragon-riding dynasty displaced by a rebellion; and numerous other viewpoint characters caught in the wars, conspiracies, and dynastic struggles over the Iron Throne of Westeros.\n\nA Game of Thrones transformed the epic fantasy genre by introducing a moral and narrative sophistication unprecedented in commercial fantasy — its willingness to kill major viewpoint characters (most famously Ned Stark, the novel's apparent protagonist, executed at the novel's climax), its portrayal of the political consequences of idealism and honour in a world of ruthless cynicism, and its explicit sexual and violent content challenged the conventions of Tolkienian heroic fantasy. Martin's approach — drawing inspiration from the Wars of the Roses and other episodes of medieval dynastic conflict, from Tolkien filtered through the historical novel tradition — produced a fantasy series in which the 'realistic' political and human complexity of historical fiction was combined with the fantastical elements of traditional epic fantasy.\n\nThe HBO television adaptation of A Game of Thrones (2011–2019) — one of the most expensive and widely watched television productions in history, peaking at 44 million viewers per episode — took the series from the enthusiastic readership of fantasy literature to global mainstream cultural phenomenon, making Westeros and its characters among the most recognisable fictional settings in contemporary popular culture.",
    "causes": [
      "Martin's dissatisfaction with the narrative constraints of television — he had spent the 1980s writing for The Twilight Zone and Beauty and the Beast, where budget constraints limited the scale of battle and fantasy sequences — led him to conceive A Song of Ice and Fire as a narrative unconstrained by production budget, envisioning battles and dragons and armies at a scale that no TV budget of the early 1990s could realise.",
      "The Tolkienian fantasy tradition and its commercial successors (Terry Brooks, Robert Jordan's Wheel of Time series) — which dominated commercial fantasy in the 1980s–1990s — provided both the genre conventions (epic scope, secondary world, multiple storylines) that Martin worked within and the comfortable heroic moral certainties that he deliberately subverted.",
      "Martin's engagement with the Wars of the Roses — the 15th-century English dynastic conflicts between the houses of Lancaster and York — and the broader tradition of medieval historical fiction (particularly the model of the Byzantine/medieval court intrigues in fantasy form) gave A Song of Ice and Fire its historical texture and its realistic political complexity."
    ],
    "effects": [
      "A Game of Thrones transformed the epic fantasy genre — its 'gritty realism', willingness to kill central characters, and moral complexity without clear heroic resolution spawned the 'grimdark' fantasy subgenre (Joe Abercrombie, Scott Lynch, Patrick Rothfuss) and established a new standard of psychological and political complexity for commercial fantasy writing.",
      "The HBO adaptation of Game of Thrones (2011–2019) was the most successful television adaptation of fantasy literature ever produced — making Westeros and its characters globally recognisable, driving fantasy literature into mainstream cultural prominence, and demonstrating that the fantasy genre could sustain the same prestige television treatment as historical drama.",
      "A Song of Ice and Fire's commercial success — the series has sold over 90 million copies — transformed the commercial fantasy market, establishing the market for long, complex, multi-volume epic fantasy series with sophisticated political and psychological content, and influencing publishers' and readers' expectations of the fantasy genre."
    ],
    "relationships": [
      {"sourceSlug": "george-rr-martin", "sourceName": "George R.R. Martin (born 1948)", "verb": "AUTHORS", "targetSlug": "a-game-of-thrones", "targetName": "A Game of Thrones (1996)", "context": "Martin conceived A Song of Ice and Fire in 1991 and published A Game of Thrones in 1996 — drawing on the Wars of the Roses for political complexity and on his frustration with television production constraints to imagine a narrative without budget limitations."},
      {"sourceSlug": "a-game-of-thrones", "sourceName": "A Game of Thrones / A Song of Ice and Fire", "verb": "ADAPTS_INTO", "targetSlug": "game-of-thrones-hbo", "targetName": "Game of Thrones (HBO, 2011–2019)", "context": "The HBO television adaptation — one of the most expensive and widely watched productions in television history — took A Song of Ice and Fire from the enthusiastic readership of fantasy literature to global mainstream cultural phenomenon."},
      {"sourceSlug": "a-game-of-thrones", "sourceName": "A Game of Thrones (grimdark elements)", "verb": "ESTABLISHES", "targetSlug": "grimdark-fantasy", "targetName": "Grimdark fantasy subgenre (Abercrombie, Lynch)", "context": "A Game of Thrones's willingness to kill protagonists, its moral complexity without heroic resolution, and its explicit violence and sex established the 'grimdark' fantasy subgenre that dominated commercial fantasy in the 2000s–2010s."}
    ],
    "places": [
      {"name": "Westeros (fictional continent, narrative setting)", "role": "The fictional continent of Westeros — a medieval secondary world where seasons last years and supernatural threats lurk beyond the Wall — is the primary setting of A Song of Ice and Fire and one of the most elaborately world-built fictional settings in contemporary fantasy"},
      {"name": "New Jersey and Santa Fe (Martin's composition locations)", "role": "Martin wrote A Game of Thrones in Santa Fe, New Mexico (where he moved from New Jersey in 1979) — the novel conceived initially as an unfilmable epic in the period of his frustration with television narrative constraints"}
    ],
    "subjects": ["Fantasy Literature", "Contemporary Era", "George R.R. Martin", "Epic Fantasy", "Television Adaptation", "American Fiction", "21st Century", "Popular Culture"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "A Game of Thrones (George R.R. Martin, 1996) is the founding text of A Song of Ice and Fire — the series that transformed commercial epic fantasy with its political complexity, moral ambiguity, and willingness to kill protagonists, and which became the basis for the most successful television adaptation of fantasy literature ever made. Its influence on the fantasy genre and on popular culture through the HBO adaptation has been enormous.",
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
