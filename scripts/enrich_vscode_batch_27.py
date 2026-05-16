#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 27 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: book-of-ruth, death-of-a-salesman, emile-or-on-education, ecce-homo,
          a-farewell-to-arms, a-portrait-of-the-artist-as-a-young-man,
          augustan-history, a-sand-county-almanac-leopold
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-27-may2026"

ENRICHMENTS = {

"book-of-ruth": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780book-of-ruth.json",
  "slug": "book-of-ruth",
  "data": {
    "summary": "The Book of Ruth is a short narrative book of the Hebrew Bible (Old Testament), comprising four chapters that tell the story of Ruth, a Moabite widow who accompanies her Israelite mother-in-law Naomi back to Bethlehem after both their husbands have died, declaring her loyalty in one of the most celebrated expressions of faithfulness in world literature: 'Where you go I will go, and where you stay I will stay. Your people will be my people and your God my God' (Ruth 1:16). In Bethlehem, Ruth gleans grain in the fields of Boaz — a wealthy relative of Naomi — who eventually marries her under the institution of levirate marriage, providing both women with security, and the book ends with the revelation that Ruth and Boaz are the great-grandparents of David, ancestor of the Messianic line.\n\nThe Book of Ruth is unusual among the books of the Hebrew Bible for several reasons: it is one of only two books named for a woman (the other being Esther); its protagonist is a foreign woman — a Moabite, whose people were traditionally enemies of Israel — whose loyalty and virtue are presented as equal or superior to those of the Israelites around her; it contains no mention of God's direct intervention or of major national events, focusing entirely on the private lives of ordinary people; and its tone is warm, humane, and literary in a way that makes it one of the most beautifully crafted narratives in the Bible. The book's date of composition is debated — it may reflect conditions of the pre-monarchical period it depicts (c. 1100 BCE), but many scholars date the final composition to the post-exilic period (c. 450–400 BCE), when it may have served as a counter-narrative to Ezra's prohibition on intermarriage with foreigners.\n\nThe Book of Ruth's theological and cultural significance is considerable: its universalist message (that loyalty and virtue transcend ethnic boundaries) stands in creative tension with the separatist nationalism of parts of the Hebrew Bible; its narrative of a foreign woman accepted into the community of Israel through her loyalty and love prefigures the New Testament's theme of Gentile inclusion; and its portrait of female solidarity between Naomi and Ruth is one of the most resonant in sacred literature.",
    "causes": [
      "The social institution of levirate marriage (Hebrew: yibbum) — the obligation of a deceased man's kinsman to marry his widow — and the institution of the kinsman-redeemer (go'el) who could redeem the family's land and social position provide the social and legal framework within which Ruth's story takes place and which Boaz's marriage to Ruth resolves.",
      "The agricultural society of early Israel — with its provision for the poor to glean (collect the grain left behind after the harvest) in others' fields, a legally mandated form of social welfare (Leviticus 19:9–10) — provides the immediate narrative setting in which Ruth and Boaz meet and the expression of Israelite social values that the story celebrates.",
      "The post-exilic controversy over intermarriage — Ezra's prohibition on foreign wives (Ezra 9–10, c. 458 BCE) and Nehemiah's similar measures — may have provided the political context within which the Book of Ruth was edited or composed as a counter-narrative, arguing through the story of David's Moabite ancestor that ethnic purity requirements were inconsistent with the tradition's own history."
    ],
    "effects": [
      "The Book of Ruth's universalist message — that a foreign woman's loyalty and virtue could make her more fully part of Israel than ethnic birth alone — influenced the New Testament's theological universalism and its welcome of Gentile converts, contributing to the Christian theological tradition of spiritual adoption transcending ethnic boundaries.",
      "Ruth's declaration of loyalty to Naomi ('Where you go I will go...') has become one of the most cited expressions of loyalty and love in Western culture — used at weddings, funerals, and in secular contexts as a near-universal expression of committed fidelity, giving the Book of Ruth a cultural influence far beyond its specifically religious significance.",
      "The Book of Ruth's literary structure — its careful patterning, its resolution of social crisis through the application of ancient institutions, and its integration of the private love story into the grand Davidic genealogy — has been studied as a model of biblical narrative art, influencing biblical narrative criticism and the interpretation of Hebrew narrative style."
    ],
    "relationships": [
      {"sourceSlug": "book-of-ruth", "sourceName": "Book of Ruth", "verb": "PART_OF", "targetSlug": "hebrew-bible", "targetName": "Hebrew Bible (Ketuvim, Writings)", "context": "The Book of Ruth is part of the Ketuvim (Writings), the third section of the Hebrew Bible — read liturgically in Judaism at Shavuot (Pentecost) and a canonical text of both the Jewish and Christian traditions."},
      {"sourceSlug": "book-of-ruth", "sourceName": "Book of Ruth", "verb": "ESTABLISHES_GENEALOGY_OF", "targetSlug": "david-king-of-israel", "targetName": "David, King of Israel", "context": "The Book of Ruth ends with the revelation that Ruth and Boaz are the great-grandparents of David — linking the Moabite woman's story into the Davidic genealogy and the Messianic line."},
      {"sourceSlug": "book-of-ruth", "sourceName": "Book of Ruth (universalist message)", "verb": "CONTRASTS_WITH", "targetSlug": "ezra-book", "targetName": "Book of Ezra (prohibition of intermarriage)", "context": "Many scholars read the Book of Ruth as a counter-narrative to Ezra's post-exilic prohibition on intermarriage — arguing through David's Moabite ancestry that ethnic exclusivity was inconsistent with Israel's own tradition."}
    ],
    "places": [
      {"name": "Moab and Bethlehem (narrative setting, c. 1100 BCE?)", "role": "The narrative geography — Ruth's journey from Moab to Bethlehem with Naomi, and the agricultural community of Bethlehem where the story unfolds"},
      {"name": "Post-exilic Judah (probable final composition context, c. 450–400 BCE)", "role": "The possible context of the book's final compilation — the controversy over intermarriage under Ezra and Nehemiah that may have made Ruth's story politically significant"}
    ],
    "subjects": ["Hebrew Bible", "Classical Era", "Biblical Literature", "Jewish History", "Ancient Israel", "Theological Text", "Women in History", "Religious Texts"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Book of Ruth is one of the most beautifully crafted narratives in the Hebrew Bible — its portrait of a Moabite woman's loyalty ('Where you go I will go') whose virtue transcends ethnic boundaries has made it a foundational text of the universalist tradition in both Judaism and Christianity. Ruth's declaration of loyalty has become one of the most widely cited expressions of committed fidelity in Western culture.",
      "significanceCategory": "significant"
    }
  }
},

"death-of-a-salesman": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780death-of-a-salesman.json",
  "slug": "death-of-a-salesman",
  "data": {
    "summary": "Death of a Salesman is the play by Arthur Miller (1915–2005), which premiered on Broadway at the Morosco Theatre on 10 February 1949 (directed by Elia Kazan, with Lee J. Cobb as Willy Loman) and won the Pulitzer Prize for Drama and the Tony Award for Best Play — one of the most celebrated and widely performed plays in the American theatrical canon and a foundational text in the critique of the American Dream. Its protagonist, Willy Loman, is a 63-year-old travelling salesman in Brooklyn whose career is collapsing, whose sons have failed to live up to his expectations, and who lives in a world of delusion and memory — the play moving between present and past in an innovative expressionistic structure in which Willy's memories and fantasies break into the action of the present — until Willy kills himself in a car 'accident', hoping that the life insurance payment will give his son Biff the money to succeed in business. The play's famous last lines, spoken by Linda at Willy's poorly attended funeral — 'We're free... We're free...' — are devastating in their irony.\n\nDeath of a Salesman is a tragedy in the classical sense — the downfall of a man whose fatal flaw is his devotion to an illusion (the American Dream of success through personal attractiveness and salesmanship) — but Miller wrote it as a 'tragedy of the common man', arguing in his famous essay 'Tragedy and the Common Man' (1949) that the ordinary person is as fit a subject for tragedy as the kings and heroes of classical drama. Willy Loman's surname ('Lo-man' — low man) is one of the most famous bits of symbolism in American drama: the man at the bottom of the social hierarchy whose aspirations, delusions, and dignity are those of every salesman, every father, every person who has invested their self-worth in the image others have of them.\n\nDeath of a Salesman is one of the most produced plays in the American theatrical repertoire — revived on Broadway and in regional theatres throughout the world every generation — and its critique of the American Dream, its portrayal of a working-class family's collapse under the weight of impossible aspirations, and its formal innovation (the fluid movement between past and present, fantasy and reality) have made it a foundational text of modern American drama.",
    "causes": [
      "Arthur Miller's personal experience of the Depression-era America in which he grew up — the collapse of his father's business, the family's financial precarity, and the culture of masculine self-making and commercial success that Depression America measured men against — gave Death of a Salesman its autobiographical emotional truth and its critique of the American Dream.",
      "The post-war American consumer boom and the ideology of success-through-salesmanship — the expanding commercial culture of late 1940s America in which every man was expected to be a salesman of himself (personality, likability, 'being well-liked') — gave the play its immediate cultural resonance and its critique of the specifically American form of the self-deluded pursuit of success.",
      "Miller's formal innovation of the expressionistic, memory-fractured dramatic structure — influenced by Tennessee Williams's Glass Menagerie (1944) and by the German Expressionist theatre tradition — gave Death of a Salesman its technical originality, dissolving the boundaries between present action and memory to dramatise Willy's psychological condition from the inside."
    ],
    "effects": [
      "Death of a Salesman established the 'tragedy of the common man' as a viable and powerful dramatic genre — demonstrating that the working-class protagonist could sustain tragic drama with the same dignity and emotional force as the heroic figures of classical tragedy, and influencing a generation of American playwrights including Tennessee Williams, Sam Shepard, and Edward Albee.",
      "The play's critique of the American Dream — its argument that the ideology of success through personality and sales performance is a destructive illusion that destroys families and individuals who cannot measure up to its demands — made Death of a Salesman a central text in the cultural critique of American capitalism and the performative demands it places on men.",
      "Willy Loman became one of the archetypal figures of American culture — 'a willy loman' entered the cultural vocabulary as a term for the pathetic, deluded salesman sacrificed on the altar of the American Dream, and the play's Pulitzer Prize and Tony wins in 1949 established it immediately as a canonical text of American drama."
    ],
    "relationships": [
      {"sourceSlug": "arthur-miller", "sourceName": "Arthur Miller (1915–2005)", "verb": "AUTHORS", "targetSlug": "death-of-a-salesman", "targetName": "Death of a Salesman (1949)", "context": "Miller wrote Death of a Salesman in six weeks in 1948 — drawing on autobiographical experience of Depression-era America and his own father's commercial failure to create the definitive critique of the American Dream in dramatic form."},
      {"sourceSlug": "death-of-a-salesman", "sourceName": "Death of a Salesman", "verb": "CRITIQUES", "targetSlug": "american-dream", "targetName": "American Dream (ideology of commercial success)", "context": "Death of a Salesman's central argument is the critique of the American Dream as a destructive illusion — Willy Loman's belief that 'being well-liked' and salesmanship can substitute for genuine achievement destroys his family and himself."},
      {"sourceSlug": "death-of-a-salesman", "sourceName": "Death of a Salesman", "verb": "ESTABLISHES", "targetSlug": "common-man-tragedy", "targetName": "Tragedy of the common man (Miller's dramatic theory)", "context": "Miller's 1949 essay 'Tragedy and the Common Man' argued that the ordinary person's aspiration and downfall is as fit for tragedy as the heroic figures of Aristotle's Poetics — Death of a Salesman was his proof of this argument."}
    ],
    "places": [
      {"name": "New York City, Brooklyn (play's setting, 1949)", "role": "The setting of the play — the Loman family home in Brooklyn, surrounded by the encroaching apartment blocks that have transformed the neighbourhood Willy remembers"},
      {"name": "Broadway, New York (10 February 1949 premiere)", "role": "The opening of Death of a Salesman at the Morosco Theatre — one of the most celebrated Broadway openings in history, with Lee J. Cobb's performance of Willy Loman creating an immediate theatrical event"}
    ],
    "subjects": ["American Drama", "Modern Era", "Theatre", "American Literature", "20th Century", "Cultural Criticism", "Drama", "Arthur Miller"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Death of a Salesman (Arthur Miller, 1949) is one of the most celebrated plays in the American theatrical canon — its tragedy of a working-class salesman destroyed by his devotion to the American Dream established Miller's 'tragedy of the common man' as a valid dramatic form and provided the definitive critique of American commercial culture's demands on masculinity. It has been continuously produced worldwide since 1949.",
      "significanceCategory": "world-changing"
    }
  }
},

"emile-or-on-education": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780emile-or-on-education.json",
  "slug": "emile-or-on-education",
  "data": {
    "summary": "Émile, ou De l'éducation ('Emile, or On Education') is the treatise on education by Jean-Jacques Rousseau (1712–1778), published in 1762 — one of the most influential books in the history of educational theory and child psychology, and a foundational text of Romanticism, modern pedagogy, and the philosophy of childhood. In five books, Rousseau traces the ideal education of a fictional boy named Emile from birth to adulthood, arguing that children are naturally good but corrupted by society and civilisation, and that the proper education should follow nature rather than impose conventional social values: the child should learn through direct experience of the natural world, through the development of the senses and then the reasoning faculties in the correct developmental sequence, and should be protected from books, premature social contact, and the corrupting influence of adult values until the appropriate developmental stage.\n\nRousso's educational philosophy rests on his fundamental conviction (expressed in the Social Contract, published the same year) that 'man is born free, and everywhere he is in chains' — applied to education, this means that the child is born with natural goodness and curiosity that conventional education destroys through rote learning, social conformity, and premature instruction. Émile is educated outside society (by a tutor on a country estate) and learns through direct experience rather than books — he learns to swim before he reads, learns carpentry as a practical trade, and encounters abstract ideas only when his concrete experience has prepared him for them. Book 5 — 'Sophy, or Woman' — describes the ideal education for Emile's future wife in terms that are starkly unequal: Sophy is to be educated for dependence, modesty, and pleasing men, a vision that provoked immediate feminist critique (Mary Wollstonecraft's Vindication of the Rights of Woman, 1792, was written in direct response).\n\nÉmile was immediately condemned by the Archbishop of Paris and the Paris Parlement, burned in both Paris and Geneva, and Rousseau was forced to flee France — making it one of the most notorious books of the Enlightenment. Its influence on subsequent educational theory has been enormous: Pestalozzi, Froebel, Dewey, Montessori, and Piaget all developed their theories in explicit or implicit dialogue with Rousseau's insistence that education should follow the child's natural developmental stages.",
    "causes": [
      "Rousseau's conviction that human nature is fundamentally good but corrupted by society — expressed throughout his work from the First and Second Discourses through the Social Contract — gave Émile its foundational premise: that the purpose of education is to protect natural goodness from social corruption while preparing the child for adult life in a corrupt society.",
      "The 18th-century European debate about education — sparked by Locke's Thoughts Concerning Education (1693), which argued that the child's mind is a blank slate to be written on by experience — provided the intellectual context within which Rousseau's radically different naturalist theory stood out: for Rousseau, the child is not a blank slate but a naturally good being who must be protected from the wrong kind of experience.",
      "Rousseau's own troubled relationship with childhood, parenthood, and society — his Confessions reveals that he abandoned all five of his own children to the foundling hospital — gave Émile its compensatory fantasy character: the ideal education he could not provide his own children, and the idealized parent-child relationship he could not have."
    ],
    "effects": [
      "Émile's influence on Western educational theory has been transformative — Pestalozzi's 'learning by doing', Froebel's kindergarten movement, Dewey's progressive education, Montessori's child-centred pedagogy, and Piaget's developmental psychology all develop in explicit or implicit dialogue with Rousseau's insistence that education should follow the child's natural developmental stages rather than impose premature adult instruction.",
      "Mary Wollstonecraft's A Vindication of the Rights of Woman (1792) — the foundational text of feminist political thought — was written in direct response to Émile Book 5's sexist account of women's education: Wollstonecraft argued that Rousseau's prescription for Sophy was a prescription for women's subjection, making Émile inadvertently the catalyst for the first systematic statement of feminist educational theory.",
      "Rousseau's concept of childhood innocence and natural goodness — the child as a being with a distinct and valuable developmental stage rather than merely an incomplete adult — transformed Western culture's conception of childhood, contributing to the Romantic valorisation of childhood experience (Wordsworth's 'spots of time', Blake's Songs of Innocence and Experience) and ultimately to modern child-centred educational practice."
    ],
    "relationships": [
      {"sourceSlug": "jean-jacques-rousseau", "sourceName": "Jean-Jacques Rousseau (1712–1778)", "verb": "AUTHORS", "targetSlug": "emile-or-on-education", "targetName": "Émile, or On Education (1762)", "context": "Rousseau published Émile in 1762, the same year as the Social Contract — his comprehensive treatise on natural education, immediately condemned and burned by the Paris Parlement and the Geneva authorities."},
      {"sourceSlug": "emile-or-on-education", "sourceName": "Émile, or On Education (Book 5)", "verb": "PROVOKES", "targetSlug": "a-vindication-of-the-rights-of-woman", "targetName": "Mary Wollstonecraft's A Vindication of the Rights of Woman (1792)", "context": "Émile Book 5's account of Sophy's education for dependence and pleasing men was the direct target of Wollstonecraft's Vindication — making Rousseau's educational treatise the inadvertent catalyst for the first systematic feminist educational theory."},
      {"sourceSlug": "emile-or-on-education", "sourceName": "Émile", "verb": "INFLUENCES", "targetSlug": "progressive-education", "targetName": "Progressive education (Pestalozzi, Froebel, Dewey, Montessori)", "context": "Rousseau's Émile is the foundational text of the progressive education tradition — Pestalozzi, Froebel, Dewey, and Montessori all developed child-centred pedagogies in explicit response to Rousseau's insistence that education should follow the child's natural developmental stages."}
    ],
    "places": [
      {"name": "Paris and Geneva (1762, publication and condemnation)", "role": "Émile was published in Paris and immediately condemned and burned there and in Geneva — forcing Rousseau to flee France and rendering him a fugitive for several years"},
      {"name": "Western educational institutions (18th–20th centuries, ongoing influence)", "role": "The sphere of Émile's influence — from Pestalozzi's institutions in Switzerland through Dewey's progressive schools in the United States to Montessori schools worldwide"}
    ],
    "subjects": ["Educational Philosophy", "Enlightenment", "Early Modern Era", "Rousseau", "Childhood", "Pedagogy", "18th Century", "French Philosophy"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Émile (Rousseau, 1762) is the foundational text of Western educational theory — its insistence that education should follow the child's natural developmental stages rather than impose premature adult instruction influenced Pestalozzi, Froebel, Dewey, Montessori, and Piaget, and ultimately shaped modern child-centred educational practice. Its sexist account of women's education inadvertently catalysed the first systematic feminist educational theory in Wollstonecraft's Vindication.",
      "significanceCategory": "world-changing"
    }
  }
},

"ecce-homo": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780ecce-homo.json",
  "slug": "ecce-homo",
  "data": {
    "summary": "Ecce Homo: How One Becomes What One Is (German: Ecce Homo: Wie man wird, was man ist) is the autobiographical work of Friedrich Nietzsche (1844–1900), written in a burst of extraordinary energy in October 1888 — two to three months before his mental collapse in January 1889 in Turin — and published posthumously in 1908, more than a decade after his breakdown. In Ecce Homo, Nietzsche reviews his own philosophical development and his major works (The Birth of Tragedy, Human All Too Human, Thus Spoke Zarathustra, Beyond Good and Evil, On the Genealogy of Morality, Twilight of the Idols, The Antichrist, The Case of Wagner) with a mixture of philosophical clarity, extraordinary self-appreciation ('Why I Am So Wise', 'Why I Am So Clever', 'Why I Write Such Good Books'), and moments of grandiosity that retrospectively raise the question of whether the mental illness that would consume him was already affecting his writing.\n\nEcce Homo is simultaneously Nietzsche's clearest and most accessible self-presentation — the chapters on his individual works contain some of his most lucid explanations of his philosophical aims — and his most difficult and disturbing text. The combination of genuine philosophical insight, remarkable self-awareness, bitter polemic (particularly against Wagner and German culture), and megalomaniacal self-aggrandisement makes Ecce Homo one of the strangest and most unsettling documents in the history of Western philosophy: a philosopher's last self-portrait on the threshold of madness.\n\nThe title is the Latin phrase Pontius Pilate used when presenting the flagellated Jesus to the Jerusalem crowd — 'Behold the man!' — and Nietzsche's use of it as the title of his philosophical autobiography is characteristically provocative and multilayered: an identification of himself as a man to be looked upon, a secular replacement for Christ, and an allusion to the kind of fate his philosophical work might bring upon him. Nietzsche had already written in a letter that he was 'dynamite' — that his philosophy would fundamentally transform Western thought — and Ecce Homo is in part his attempt to control the interpretation of his explosive legacy.",
    "causes": [
      "Nietzsche's growing conviction in 1888 that his philosophical work was being misunderstood or ignored — and his determination to write the definitive account of his own philosophy before the 'revaluation of all values' he was preparing could be distorted by his interpreters — drove Ecce Homo's urgency and its self-promotional tone.",
      "The extraordinary productive burst of 1888 — the year in which Nietzsche wrote The Case of Wagner, Twilight of the Idols, The Antichrist, Nietzsche Contra Wagner, and Ecce Homo, all within months — suggests either an extraordinary creative peak or (as many scholars have argued) the hypomanic phase of the bipolar or syphilitic neurological condition that would produce his collapse in January 1889.",
      "Nietzsche's physical and social isolation — his itinerant life as a solitary philosopher in Swiss and Italian mountain towns, his dependence on a small circle of correspondents and his sister Elisabeth's problematic stewardship of his work — gave Ecce Homo the quality of a message in a bottle thrown at a future that might understand him as his present did not."
    ],
    "effects": [
      "Ecce Homo's posthumous publication in 1908 — shaped by Nietzsche's sister Elisabeth Förster-Nietzsche, who controlled his archive and later associated his work with Nazi ideology — raised persistent questions about the relationship between Nietzsche's philosophy and the megalomaniacal tone of his last writings, making the book's interpretation inseparable from the question of his mental state.",
      "The chapters of Ecce Homo in which Nietzsche reviews his individual works remain among the most accessible guides to his philosophical intentions — his account of what he was trying to do in Thus Spoke Zarathustra, Beyond Good and Evil, and On the Genealogy of Morality is invaluable for Nietzsche scholarship and for understanding the coherence of his philosophical project.",
      "Ecce Homo's literary style — its combination of philosophical aphorism, autobiographical narrative, and prophetic self-presentation — influenced 20th-century philosophical autobiography and the genre of the philosophical manifesto, particularly in its use of personal voice and self-dramatisation to present philosophical claims."
    ],
    "relationships": [
      {"sourceSlug": "friedrich-nietzsche", "sourceName": "Friedrich Nietzsche (1844–1900)", "verb": "AUTHORS", "targetSlug": "ecce-homo", "targetName": "Ecce Homo (1888, published 1908)", "context": "Nietzsche wrote Ecce Homo in October 1888, two to three months before his mental collapse — his last major philosophical text and his retrospective account of his entire philosophical project."},
      {"sourceSlug": "ecce-homo", "sourceName": "Ecce Homo", "verb": "REVIEWS", "targetSlug": "thus-spoke-zarathustra", "targetName": "Thus Spoke Zarathustra and Nietzsche's major works", "context": "Ecce Homo contains Nietzsche's own chapter-by-chapter account of his major works, providing the most authoritative available guide to his philosophical intentions."},
      {"sourceSlug": "ecce-homo", "sourceName": "Ecce Homo (appropriation)", "verb": "MISAPPROPRIATED_BY", "targetSlug": "elisabeth-forster-nietzsche", "targetName": "Elisabeth Förster-Nietzsche (archive control)", "context": "Nietzsche's sister Elisabeth controlled his archive after his collapse and shaped the publication and interpretation of his works, including Ecce Homo — her nationalist and antisemitic interpretation was contrary to Nietzsche's own views expressed in the work."}
    ],
    "places": [
      {"name": "Turin, Italy (October 1888, composition)", "role": "Nietzsche wrote Ecce Homo in Turin in October 1888 — the city where he had his mental breakdown in January 1889 on the Piazza Carlo Alberto"},
      {"name": "Weimar (Nietzsche Archive, posthumous publication)", "role": "The Nietzsche Archive in Weimar — controlled by Elisabeth Förster-Nietzsche — where Ecce Homo was held and eventually published in 1908, shaped by Elisabeth's editorial decisions"}
    ],
    "subjects": ["Philosophy", "Modern Era", "Nietzsche", "Autobiography", "19th Century", "Continental Philosophy", "German Literature", "Philosophy of Self"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Ecce Homo (Nietzsche, 1888, published 1908) is Nietzsche's last philosophical work and his retrospective account of his entire philosophical project — written on the threshold of madness, combining his clearest self-explanations with megalomaniacal self-aggrandisement. Its chapters reviewing his major works remain indispensable for Nietzsche scholarship, and the circumstances of its composition and publication raise fundamental questions about the relationship between his philosophy and his mental breakdown.",
      "significanceCategory": "significant"
    }
  }
},

"a-farewell-to-arms": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783a-farewell-to-arms.json",
  "slug": "a-farewell-to-arms",
  "data": {
    "summary": "A Farewell to Arms is the novel by Ernest Hemingway (1899–1961), published in September 1929 — one of the masterpieces of American Modernist fiction and the defining American novel of World War I, drawing directly on Hemingway's own experience as an 18-year-old ambulance driver on the Italian front in 1918. Its protagonist, Frederic Henry, is an American serving as a lieutenant in the Italian Ambulance Corps on the Isonzo front; he is wounded, falls in love with the British nurse Catherine Barkley, deserts after the disastrous Italian retreat from Caporetto (October 1917), and escapes with Catherine to Switzerland, where she dies in childbirth. The novel's ending — Henry walking back to the hotel in the rain alone after Catherine's death — is one of the most famous endings in American literature: the absolute, arbitrary termination of love and meaning by death, with no consolation, no resolution, and no redemption.\n\nA Farewell to Arms is the definitive statement of Hemingway's characteristic technique: the 'iceberg theory' of prose in which the emotional weight of the narrative is carried below the surface in what is omitted rather than what is stated; the declarative, paratactic sentences that accumulate into overwhelming emotional weight; the stoic code of behaviour under pressure (the 'Hemingway code hero'); and the use of rain as a pervasive metaphor for death and meaninglessness throughout the novel (Catherine says she has a premonition of death 'in the rain'). Published the same year as Remarque's All Quiet on the Western Front (1929), it is part of the extraordinary wave of World War I literature (Sassoon, Owen, Graves, Remarque, Hemingway) that definitively shaped the 20th-century perception of the Great War as catastrophic, meaningless waste.\n\nThe novel's famous opening — the description of the war in the plain below the mountains, the troops marching in the rain, the dust and mud — is one of the great opening paragraphs of American fiction, and Hemingway's style in A Farewell to Arms influenced a generation of American writers (Fitzgerald, Faulkner, Steinbeck, and the entire subsequent tradition of American realist fiction).",
    "causes": [
      "Hemingway's direct experience of World War I — his wounding at Fossalta di Piave in July 1918 while delivering chocolate to Italian troops, his recovery in the American Red Cross hospital in Milan, and his passionate affair with Agnes von Kurowsky (the nurse on whom Catherine Barkley is partly based) — gave A Farewell to Arms its autobiographical intensity and the specific texture of its Italian front setting.",
      "The Italian military disaster at Caporetto (24 October – 19 November 1917) — in which the Italian Second Army was routed by an Austro-German offensive, losing 300,000 prisoners and causing the chaotic retreat that the novel depicts — provided A Farewell to Arms with its central military catastrophe and its image of a war collapsed into meaningless flight.",
      "The post-war 'Lost Generation' literary sensibility — the conviction that the values of civilisation and patriotism that had sent millions to die in the trenches had been exposed as lies — gave A Farewell to Arms its nihilistic moral structure: the novel is Hemingway's own farewell to the arms (weapons) and to the arms (embrace) of a world in which neither military nor romantic love can survive the arbitrary violence of war."
    ],
    "effects": [
      "A Farewell to Arms established Hemingway's 'iceberg theory' prose style as a dominant force in 20th-century American fiction — his paratactic sentences, his understatement, his principle of omitting what the reader can sense beneath the surface — influencing the development of American realist prose from Steinbeck and Fitzgerald through Raymond Carver and minimalist fiction.",
      "Together with All Quiet on the Western Front (also 1929) and the poetry of Owen and Sassoon, A Farewell to Arms created the canonical perception of World War I as a catastrophic waste of young lives for meaningless causes — a cultural framing of the Great War that has dominated Western historical memory for nearly a century.",
      "The novel's portrayal of the love story between Frederic and Catherine — a love both transcendent and doomed, ended by the arbitrary biological fact of childbirth — became a defining model of Modernist tragic romance, and its nihilistic ending (no consolation, no redemption, just rain and loss) has become the canonical image of Hemingway's war-inflected existentialism."
    ],
    "relationships": [
      {"sourceSlug": "ernest-hemingway", "sourceName": "Ernest Hemingway (1899–1961)", "verb": "AUTHORS", "targetSlug": "a-farewell-to-arms", "targetName": "A Farewell to Arms (1929)", "context": "Hemingway wrote A Farewell to Arms drawing on his 1918 experience as an ambulance driver on the Italian front and his convalescent affair with a nurse — the most directly autobiographical of his major novels."},
      {"sourceSlug": "a-farewell-to-arms", "sourceName": "A Farewell to Arms", "verb": "DOCUMENTS", "targetSlug": "battle-of-caporetto", "targetName": "Italian retreat from Caporetto (October 1917)", "context": "The novel's central military episode — Frederic Henry's retreat from Caporetto and the execution of officers by the Carabinieri — is based on the real Caporetto disaster of October 1917."},
      {"sourceSlug": "a-farewell-to-arms", "sourceName": "A Farewell to Arms", "verb": "ESTABLISHES", "targetSlug": "hemingway-style", "targetName": "Hemingway's iceberg theory prose style", "context": "A Farewell to Arms is the definitive statement of Hemingway's prose technique — the paratactic sentences, the emotional understatement, and the iceberg theory of omitting what the narrative carries below the surface."}
    ],
    "places": [
      {"name": "Italian front — Isonzo/Caporetto, Italy (1917–1918, narrative setting)", "role": "The Italian front of World War I — the Isonzo River battles and the Caporetto disaster — which Hemingway experienced as an ambulance driver and which provides the novel's military setting"},
      {"name": "Milan and Switzerland (narrative setting, 1918)", "role": "The hospital in Milan where Frederic convalesces and falls in love with Catherine, and Switzerland where they escape and where Catherine dies"}
    ],
    "subjects": ["American Literature", "Modern Era", "World War I", "Modernism", "American Fiction", "20th Century", "Hemingway", "War Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "A Farewell to Arms (Hemingway, 1929) is the defining American novel of World War I — establishing Hemingway's iceberg theory prose style as a dominant force in 20th-century American fiction and, together with All Quiet on the Western Front, creating the canonical perception of the Great War as catastrophic, meaningless waste. Its nihilistic ending became the canonical image of Modernist tragic romance.",
      "significanceCategory": "world-changing"
    }
  }
},

"a-portrait-of-the-artist-as-a-young-man": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783a-portrait-of-the-artist-as-a-young-man.json",
  "slug": "a-portrait-of-the-artist-as-a-young-man",
  "data": {
    "summary": "A Portrait of the Artist as a Young Man is the semi-autobiographical Bildungsroman (coming-of-age novel) of James Joyce (1882–1941), published in book form in 1916 after serial publication in The Egoist (1914–1915) — the first of Joyce's three great novels (followed by Ulysses, 1922, and Finnegans Wake, 1939) and the technical breakthrough in which Joyce developed the stream-of-consciousness interior monologue technique that would transform 20th-century fiction. The novel follows Stephen Dedalus — a thinly disguised Joyce — from early childhood through his Jesuit education in Ireland, his adolescent crisis of religious doubt and sexual temptation (the famous 'Hell Sermon' that drives him to confession and temporary piety), his rejection of Catholicism and Irish nationalism, and his final commitment to art as his vocation and exile as his necessary condition. The novel ends with Stephen's journal entries before his departure for Paris: 'I go to encounter for the millionth time the reality of experience and to forge in the smithy of my soul the uncreated conscience of my race.'\n\nA Portrait of the Artist as a Young Man is technically revolutionary — its prose style shifts from the impressionistic simplicity of baby language in the novel's opening sentences ('Once upon a time and a very good time it was there was a moocow coming down along the road and this moocow that was coming down along the road met a nicens little boy named baby tuckoo') through adolescent lyricism, religious rhetoric, and complex interior monologue to the mature, detached aesthetic theory of the final chapters, tracking the development of Stephen's consciousness through the evolution of the prose style itself. The famous Villanelle that Stephen composes in Chapter 5 is Joyce's self-conscious experiment in poetic form; and the aesthetic theory Stephen articulates — drawing on Aquinas's concept of claritas to develop a secular theory of aesthetic 'epiphany' — is the theoretical manifesto of Joyce's own Modernist aesthetic.\n\nA Portrait initiated the central themes and techniques of Modernism: the stream of consciousness as the primary mode of psychological representation; the artist-as-exile figure who must leave his homeland and its religious, political, and familial demands to create; and the Bildungsroman as a vehicle for exploring the formation of artistic consciousness in the modern secular world.",
    "causes": [
      "Joyce's own experience of Jesuit education at Clongowes Wood College and Belvedere College in Dublin — the rigid Catholic institutional world that shaped his intellect while he was progressively rejecting its authority — gave A Portrait its autobiographical intensity and its precise rendering of the psychological dynamics of a brilliant, rebellious consciousness within an authoritarian religious educational system.",
      "The Irish Literary Revival (W.B. Yeats, Lady Gregory, the Abbey Theatre) and the concurrent Irish nationalist movement — which offered Joyce a ready-made identity as an Irish national writer — provided the specific cultural pressures against which Stephen's artistic individualism and his rejection of national and religious identity are defined in the novel.",
      "The Ibsenite and Symbolist literary traditions that Joyce absorbed through his voracious reading (he wrote an article on Ibsen's New Drama for the Fortnightly Review at 18) provided the model of the artist as solitary truth-teller against bourgeois society, and the late 19th-century French Symbolist aesthetic (Mallarmé, Verlaine) the poetic sensibility through which Stephen's artistic vocation is expressed."
    ],
    "effects": [
      "A Portrait of the Artist established the stream-of-consciousness interior monologue as the primary technical resource of Modernist fiction — Joyce's shifting prose styles, tracking the development of Stephen's consciousness through the evolution of his narrative voice, demonstrated that the novel's primary material was the texture of inner experience rather than external event.",
      "The figure of Stephen Dedalus — the artist-as-exile who rejects homeland, religion, and family in the name of artistic freedom — became the archetypal figure of Modernist artistic identity, influencing the Künstlerroman tradition from Proust and Woolf through the 20th-century novel of artistic formation.",
      "Joyce's aesthetic theory of 'epiphany' — the sudden revelation of the essential character of a thing or experience that is the aim of artistic representation — influenced 20th-century literary criticism and practice, particularly the short story tradition (Chekhov's 'slice of life', the Joycean epiphany in the stories of Dubliners and their influence on the contemporary short story)."
    ],
    "relationships": [
      {"sourceSlug": "james-joyce", "sourceName": "James Joyce (1882–1941)", "verb": "AUTHORS", "targetSlug": "a-portrait-of-the-artist-as-a-young-man", "targetName": "A Portrait of the Artist as a Young Man (1916)", "context": "Joyce published A Portrait as his first major novel — a semi-autobiographical Bildungsroman tracking the development of his own artistic consciousness through the fictional persona of Stephen Dedalus."},
      {"sourceSlug": "a-portrait-of-the-artist-as-a-young-man", "sourceName": "A Portrait of the Artist as a Young Man", "verb": "PRECEDES", "targetSlug": "ulysses-joyce", "targetName": "James Joyce's Ulysses (1922)", "context": "A Portrait establishes Stephen Dedalus as a character who reappears in Ulysses — his aesthetic theory and his rejection of Ireland are the foundations on which Ulysses's mature Dublin of 1904 is built."},
      {"sourceSlug": "a-portrait-of-the-artist-as-a-young-man", "sourceName": "A Portrait", "verb": "ESTABLISHES", "targetSlug": "stream-of-consciousness", "targetName": "Stream-of-consciousness technique in Modern fiction", "context": "A Portrait is the technical breakthrough in which Joyce developed the shifting interior monologue that tracks Stephen's developing consciousness — the foundational demonstration of the stream-of-consciousness technique that Ulysses would take to its extreme."}
    ],
    "places": [
      {"name": "Dublin and Clongowes Wood, Ireland (narrative setting, c. 1882–1902)", "role": "The biographical geography of A Portrait — Joyce's Dublin, his Jesuit schools (Clongowes Wood and Belvedere), and the University College Dublin where Stephen develops his aesthetic theory"},
      {"name": "Trieste and Paris (Joyce's exile, 1904–1916, context of composition)", "role": "A Portrait was written in exile — Joyce in Trieste and then in Zurich, writing the novel of his Irish childhood and education from the perspective of the self-imposed exile its ending announces"}
    ],
    "subjects": ["Modernist Literature", "Modern Era", "Irish Literature", "Bildungsroman", "James Joyce", "20th Century", "English Literature", "Artistic Autobiography"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "A Portrait of the Artist as a Young Man (Joyce, 1916) is the founding text of Modernist interior monologue fiction — its shifting prose styles tracking the development of Stephen Dedalus's consciousness demonstrated that the novel's primary material was the texture of inner experience, establishing the stream-of-consciousness technique that Ulysses would take to its extreme. Its figure of the artist-as-exile became the archetypal model of Modernist artistic identity.",
      "significanceCategory": "world-changing"
    }
  }
},

"augustan-history": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781augustan-history.json",
  "slug": "augustan-history",
  "data": {
    "summary": "The Historia Augusta (Latin: Scriptores Historiae Augustae, 'Writers of Augustan History') is a collection of biographies of Roman emperors from Hadrian (r. 117–138 CE) to Numerian and Carinus (d. 285 CE), purportedly written by six different authors in the reigns of Diocletian and Constantine (c. 295–330 CE), but almost certainly the work of a single forger writing c. 360–400 CE who invented most of the six 'authors', fabricated documents, letters, and quotations, and interpolated vast amounts of fictional material into what appears to be a continuation of Suetonius's Lives of the Twelve Caesars. The Historia Augusta is simultaneously the most controversial text in Latin historical literature — a documented forgery in which fiction is interwoven with genuine historical tradition in ways that remain impossible to disentangle — and an indispensable primary source for the history of the 2nd and 3rd century Roman Empire, particularly for the difficult period of the Crisis of the Third Century (235–284 CE) for which it is sometimes the only surviving narrative source.\n\nThe Historia Augusta's historical unreliability has been known since the 17th century, and modern scholarship (particularly the work of Hermann Dessau in 1889, who definitively demonstrated its 4th-century forgery character) has established that many of its supposed documents, quoted letters, and biographical details are invented. Yet for the period 235–284 CE — for which Cassius Dio, Herodian, and other historians either do not survive or break off — the Historia Augusta is sometimes the only narrative source, however unreliable. Its biographies of Gordian III, Philip the Arab, Decius, Valerian, and the 'soldier emperors' of the Crisis period are our primary (and deeply problematic) narrative accounts of one of the most turbulent periods in Roman imperial history.\n\nThe mystery of who wrote the Historia Augusta — what purpose the elaborate fiction of multiple authorship served, and why a 4th-century author would fabricate biographies of 2nd and 3rd century emperors — remains one of the great puzzles of ancient literary history, and the work continues to generate more scholarly controversy than almost any other Latin text.",
    "causes": [
      "The loss of most of the primary historical sources for the 3rd century Roman Empire (the Crisis of the Third Century, 235–284 CE) — the gaps in Cassius Dio's History, the partial survival of Herodian, and the disappearance of other contemporary sources — left a vacuum that the Historia Augusta's 4th-century compiler filled with a mixture of genuine tradition and elaborate invention.",
      "The model of Suetonius's Lives of the Twelve Caesars — the influential 2nd-century CE collection of imperial biographies from Julius Caesar to Domitian, which the Historia Augusta explicitly continues — provided both the literary format (the emperor's life and character assessed by anecdotes) and the cultural prestige that made the format worth continuing and imitating.",
      "The 4th-century cultural context of the Historia Augusta's probable composition — the pagan revival under Julian the Apostate (r. 361–363 CE) and the nostalgia for classical Roman culture among the educated pagan aristocracy of late Rome — may have motivated its author to construct an elaborate, entertaining historical fiction celebrating the Roman imperial tradition."
    ],
    "effects": [
      "Despite its forgery character, the Historia Augusta remains one of the most important Latin texts for the history of the Roman Empire in the 2nd and 3rd centuries — for the period 235–284 CE, it is often the only narrative source, and scholars must use it with extreme caution, attempting to separate genuine tradition from the author's inventions.",
      "The Historia Augusta's elaborate fabrication — its invented documents, letters, and biographical details — has made it a foundational case study in ancient historical forgery and source criticism, raising fundamental methodological questions about how historians use texts whose reliability is systematically compromised.",
      "The persistent scholarly debate about the Historia Augusta's authorship, date, purpose, and the possibility of separating genuine tradition from invention has generated an extraordinary body of scholarship over three centuries, making it one of the most discussed texts in Latin studies and a touchstone for debates about historical method and textual criticism."
    ],
    "relationships": [
      {"sourceSlug": "augustan-history", "sourceName": "Historia Augusta (c. 360–400 CE)", "verb": "CONTINUES", "targetSlug": "suetonius", "targetName": "Suetonius, Lives of the Twelve Caesars", "context": "The Historia Augusta is presented as a continuation of Suetonius's Lives — its biographies begin where Suetonius ends, covering the emperors from Hadrian to the late 3rd century CE."},
      {"sourceSlug": "augustan-history", "sourceName": "Historia Augusta", "verb": "PRIMARY_SOURCE_FOR", "targetSlug": "crisis-of-the-third-century", "targetName": "Crisis of the Third Century (235–284 CE)", "context": "For the Crisis of the Third Century — when the Roman Empire nearly collapsed under military pressure, civil war, and economic crisis — the Historia Augusta is often the only surviving narrative source, despite its systematic unreliability."},
      {"sourceSlug": "augustan-history", "sourceName": "Historia Augusta (forgery)", "verb": "STUDIED_BY", "targetSlug": "ancient-source-criticism", "targetName": "Ancient historical source criticism (Dessau, 1889)", "context": "Hermann Dessau's 1889 demonstration that the Historia Augusta is a 4th-century forgery made it a foundational case study in ancient historical source criticism — the canonical example of a text that must be used despite known systematic unreliability."}
    ],
    "places": [
      {"name": "Rome (c. 360–400 CE, probable composition)", "role": "The probable context of the Historia Augusta's composition — the late 4th century Rome of the pagan aristocratic revival, where a single forger constructed an elaborate fiction of multiple imperial biographers"},
      {"name": "Roman Empire (2nd–3rd centuries CE, narrative scope)", "role": "The historical period the Historia Augusta covers — from Hadrian (117 CE) through the Crisis of the Third Century (284 CE), the most turbulent period of the high empire"}
    ],
    "subjects": ["Roman History", "Classical Era", "Late Antiquity", "Latin Literature", "Historical Forgery", "Roman Empire", "Source Criticism", "Biography"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Historia Augusta (c. 360–400 CE) is the most controversial Latin historical text — a documented forgery that is nevertheless the only narrative source for much of the Crisis of the Third Century (235–284 CE). Its status as both indispensable and systematically unreliable has made it a foundational case study in ancient source criticism and one of the most intensively debated texts in Latin scholarship.",
      "significanceCategory": "significant"
    }
  }
},

"a-sand-county-almanac-leopold": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781a-sand-county-almanac-leopold.json",
  "slug": "a-sand-county-almanac-leopold",
  "data": {
    "summary": "A Sand County Almanac: And Sketches Here and There is the posthumously published masterwork of the American ecologist and environmental philosopher Aldo Leopold (1887–1948), published by Oxford University Press in 1949 — one year after Leopold's death from a heart attack while fighting a brush fire on a neighbour's land near his Wisconsin farm — and widely regarded as the foundational text of modern environmental ethics and the conservation movement in the United States. In three parts, the Almanac combines the lyrical natural history of Leopold's 'worn-out farm' (a former farmstead in Sand County, Wisconsin, that he and his family spent weekends restoring) through the twelve months of the year; sketches of wild places and wildlife encounters from his career as a forest manager and conservation scientist; and, in the final essay 'The Land Ethic', the philosophical manifesto that is Leopold's most enduring intellectual contribution: the argument that human ethics must be extended to include the land community (soils, waters, plants, and animals) and that 'a thing is right when it tends to preserve the integrity, stability, and beauty of the biotic community. It is wrong when it tends otherwise.'\n\nLeopold spent his career with the US Forest Service and later as the first Professor of Game Management at the University of Wisconsin, where he developed the science of wildlife ecology and the concept of ecosystem management — and A Sand County Almanac brought his scientific understanding together with his philosophical and literary gifts in a work that addressed a general audience rather than specialists. Leopold wrote the Almanac over many years and revised it extensively, and its prose is among the finest nature writing in American literature — his descriptions of crane music at dawn, the prairie fires of October, and the death of a green-eyed wolf ('I was young then, and full of trigger-itch; I thought that because fewer wolves meant more deer, that no wolves would mean hunters' paradise. But after seeing the green fire die, I realized then, and have known ever since, that there was something new to me in those eyes') are classics of the genre.\n\nA Sand County Almanac is the foundational text of environmental ethics — the work that first articulated the idea that humans have ethical obligations to non-human nature as a whole, not merely to individual animals or species. Its 'land ethic' provided the philosophical foundation for the environmental movement of the 1960s–70s (Rachel Carson acknowledged Leopold as a major influence), the Wilderness Act of 1964, and the entire subsequent development of environmental philosophy, conservation biology, and ecological ethics.",
    "causes": [
      "Leopold's career-transforming experience of watching a wolf die — described in the essay 'Thinking Like a Mountain' — in which he saw 'the green fire dying in the wolf's eyes' and began to understand that predators were essential to the health of the whole ecosystem, gradually shifting his view from the hunter-manager perspective to the ecological holist perspective that animates the Land Ethic.",
      "The ecological understanding of the biotic community as a system — developed by plant ecologist Frederic Clements, animal ecologist Charles Elton, and Leopold himself — provided the scientific foundation for the Land Ethic's claim that the land is not merely a collection of resources but a community of interdependent organisms in which humans are members rather than conquerors.",
      "The rapid post-war development of American agriculture — the mechanisation, chemical fertilisation, and monoculture expansion that was transforming the American landscape in the 1940s — gave A Sand County Almanac its urgency: Leopold was writing against the tide of a utilitarian approach to land use that he saw as ecologically and ethically catastrophic."
    ],
    "effects": [
      "The Land Ethic — Leopold's argument that ethical consideration must be extended to the whole biotic community — became the foundational principle of environmental ethics as an academic discipline, influencing the field's development through J. Baird Callicott's systematic exposition, Holmes Rolston III's environmental philosophy, and the deep ecology movement.",
      "A Sand County Almanac directly influenced Rachel Carson's Silent Spring (1962) — the book that launched the modern environmental movement — and the broader environmental awakening of the 1960s; Leopold's ecological thinking provided the framework within which Carson's pesticide critique and the subsequent environmental legislation (Clean Air Act, Clean Water Act, Endangered Species Act) were grounded.",
      "The Wilderness Act of 1964 — which established the US National Wilderness Preservation System and protected millions of acres of federal land from development — drew directly on Leopold's philosophy of wilderness as ecologically and spiritually necessary for human life, and the land trust and conservation easement movements trace their inspiration to his work."
    ],
    "relationships": [
      {"sourceSlug": "aldo-leopold", "sourceName": "Aldo Leopold (1887–1948)", "verb": "AUTHORS", "targetSlug": "a-sand-county-almanac-leopold", "targetName": "A Sand County Almanac (1949)", "context": "Leopold wrote A Sand County Almanac over many years and revised it extensively, dying of a heart attack in April 1948 just days after Oxford University Press accepted the manuscript for publication."},
      {"sourceSlug": "a-sand-county-almanac-leopold", "sourceName": "A Sand County Almanac", "verb": "FOUNDS", "targetSlug": "environmental-ethics", "targetName": "Environmental ethics (the Land Ethic)", "context": "The Land Ethic essay is the foundational text of environmental ethics — the first systematic argument that humans have ethical obligations to the whole biotic community, not merely to other humans or domestic animals."},
      {"sourceSlug": "a-sand-county-almanac-leopold", "sourceName": "A Sand County Almanac", "verb": "INFLUENCES", "targetSlug": "rachel-carson", "targetName": "Rachel Carson's Silent Spring (1962)", "context": "Carson acknowledged Leopold as a major intellectual influence — his ecological framework provided the foundation for her critique of pesticide use and the broader environmental movement that followed Silent Spring."}
    ],
    "places": [
      {"name": "Sand County, Wisconsin (the 'worn-out farm', narrative setting)", "role": "The former farmstead in Sand County, Wisconsin that Leopold and his family spent weekends restoring — the direct inspiration for the Almanac's seasonal observations and the living demonstration of ecological restoration"},
      {"name": "United States (national environmental policy influence)", "role": "The sphere of A Sand County Almanac's most direct policy influence — the Wilderness Act of 1964, the Clean Water and Clean Air Acts, and the entire framework of American environmental regulation draw on the ecological philosophy Leopold articulated"}
    ],
    "subjects": ["Ecology", "Environmental Philosophy", "Contemporary Era", "Natural History", "Conservation", "United States", "20th Century", "Environmental Ethics"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "A Sand County Almanac (Aldo Leopold, 1949) is the foundational text of environmental ethics — its 'Land Ethic' essay first articulated the idea that humans have ethical obligations to the whole biotic community, providing the philosophical foundation for the environmental movement. Its influence on Rachel Carson's Silent Spring, the Wilderness Act of 1964, and the entire subsequent development of conservation policy and environmental philosophy makes it one of the most consequential environmental texts in history.",
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
