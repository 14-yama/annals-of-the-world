#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 54 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: the-wealth-of-nations (Adam Smith), rich-dad-poor-dad (Kiyosaki),
          the-memoirs-of-sherlock-holmes, the-return-of-sherlock-holmes (Conan Doyle),
          the-adventures-of-tom-bombadil (Tolkien),
          guinness-world-records, quidditch-through-the-ages (Rowling), go-dog-go (Eastman)
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-54-may2026"

ENRICHMENTS = {

"the-wealth-of-nations": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-wealth-of-nations.json",
  "slug": "the-wealth-of-nations",
  "data": {
    "summary": "The Wealth of Nations — full title An Inquiry into the Nature and Causes of the Wealth of Nations — is a foundational work of classical economics by Scottish moral philosopher and political economist Adam Smith (1723–1790), published in two volumes on 9 March 1776 in London by W. Strahan and T. Cadell. The work is widely regarded as the foundational text of modern economics as a systematic discipline — Smith articulates the principle of the division of labour as the primary source of productive efficiency (illustrated by the famous pin factory example), argues that national wealth is created by productive labour rather than by accumulated gold and silver (refuting mercantilist doctrine), and develops the concept of the 'invisible hand' — the idea that individuals pursuing their own self-interest in competitive markets inadvertently promote the economic welfare of society as a whole.\n\nThe Wealth of Nations is structured in five books: Book I analyses the division of labour and the theory of value; Book II addresses capital accumulation; Book III examines the development of European nations; Book IV critiques mercantilism and physiocracy; and Book V addresses the revenue and expenditure of the sovereign. The work synthesises a vast range of historical and contemporary economic observation with theoretical arguments, drawing on Smith's observations of manufacturing, trade, agriculture, and colonial economics in Britain and Europe. Smith's arguments against mercantilist protectionism and for free trade became the intellectual foundation of 19th-century British free trade policy, culminating in the repeal of the Corn Laws (1846).\n\nThe Wealth of Nations has remained one of the most influential and widely read works in the history of economic thought — it shaped liberal political economy, provided the intellectual framework for the free trade movement, influenced Karl Marx's critique of capitalism (Capital, 1867), and remains a standard reference text in economics, politics, and the history of ideas. Smith's core concepts — the division of labour, the invisible hand, comparative advantage, and the critique of mercantilism — are foundational elements of modern economic education worldwide.",
    "causes": [
      "Adam Smith's decade-long research project — begun during his time as tutor to the young Duke of Buccleuch in France (1764–1766), where he encountered French physiocratic economists, and continued at his home in Kirkcaldy — provided the intellectual environment for synthesising moral philosophy, economic observation, and historical analysis into the Wealth of Nations.",
      "The mercantilist economic doctrine dominant in 18th-century Britain and Europe — which held that national wealth consisted of accumulated gold and silver, and was best increased through protectionist trade policies and colonial exploitation — provided the primary intellectual target for Smith's critique of state-directed economic management.",
      "The Industrial Revolution beginning in Britain in the 1760s and 1770s — the emergence of manufacturing based on the division of labour, the factory system, and expanding domestic and international trade — provided the empirical context for Smith's analysis of productive labour and the sources of national wealth."
    ],
    "effects": [
      "The Wealth of Nations became the foundational text of classical economics — providing the intellectual framework for laissez-faire liberalism, free trade advocacy, and the critique of mercantilist protectionism that dominated 19th-century British and European economic policy, culminating in the repeal of the Corn Laws (1846) and the adoption of free trade as British economic orthodoxy.",
      "Smith's concept of the 'invisible hand' — individuals pursuing self-interest in competitive markets inadvertently promoting social welfare — became one of the most influential and contested ideas in the history of economics, invoked by advocates of market liberalism and critiqued by economists, sociologists, and political philosophers across the ideological spectrum.",
      "Karl Marx's Capital (1867) began with a direct engagement with Smith's labour theory of value — the critique of Smith and Ricardo became the intellectual starting point of Marxist political economy, demonstrating how the Wealth of Nations shaped the intellectual history of capitalism's critics as profoundly as its advocates."
    ],
    "relationships": [
      {"sourceSlug": "adam-smith", "sourceName": "Adam Smith (1723–1790 — Scottish moral philosopher; division of labour, invisible hand)", "verb": "AUTHORS", "targetSlug": "the-wealth-of-nations", "targetName": "The Wealth of Nations (1776 — foundational text of classical economics)", "context": "Adam Smith published The Wealth of Nations in 1776 — the foundational text of modern economics as a systematic discipline, arguing that national wealth is created by productive labour and free markets rather than by mercantilist protectionism."},
      {"sourceSlug": "the-wealth-of-nations", "sourceName": "Wealth of Nations (free trade — critique of mercantilism; Corn Laws repeal 1846)", "verb": "INFLUENCES", "targetSlug": "free-trade-movement", "targetName": "Free trade movement (19th century Britain — Corn Laws repeal 1846; British free trade policy)", "context": "Smith's arguments against mercantilist protectionism became the intellectual foundation of 19th-century British free trade policy — directly contributing to the repeal of the Corn Laws in 1846."},
      {"sourceSlug": "the-wealth-of-nations", "sourceName": "Wealth of Nations (labour theory of value — Marx's Capital 1867; critique of political economy)", "verb": "INFLUENCES", "targetSlug": "das-kapital-1867", "targetName": "Capital (Marx, 1867 — critique of political economy; labour theory of value)", "context": "Karl Marx's Capital (1867) began with a direct engagement with Smith's labour theory of value — the critique of Smith and Ricardo was the intellectual starting point of Marxist political economy."}
    ],
    "places": [
      {"name": "Edinburgh and Kirkcaldy, Scotland (Smith's research 1766–1776 — intellectual environment; Edinburgh Enlightenment)", "role": "The Wealth of Nations was researched and written in Kirkcaldy, Scotland, in the context of the Scottish Enlightenment — Smith's home environment provided the intellectual community and the empirical observation of Scottish manufacturing and trade"},
      {"name": "London (W. Strahan and T. Cadell, 9 March 1776 — publication; British political economy context)", "role": "Published in London on 9 March 1776 by W. Strahan and T. Cadell — the year of the American Declaration of Independence, in the context of British imperial economic debate"}
    ],
    "subjects": ["Economics", "18th Century", "Adam Smith", "Classical Economics", "Political Economy", "Enlightenment", "Free Trade", "Scottish Enlightenment"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Wealth of Nations (Adam Smith, 1776) is the foundational text of modern economics — its principles of the division of labour, the invisible hand, and the critique of mercantilism shaped liberal political economy, British free trade policy (Corn Laws repeal 1846), and Karl Marx's critique of capitalism. One of the most influential works in the history of ideas, it remains a standard reference across economics, politics, and the history of thought.",
      "significanceCategory": "world-changing"
    }
  }
},

"rich-dad-poor-dad": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780rich-dad-poor-dad.json",
  "slug": "rich-dad-poor-dad",
  "data": {
    "summary": "Rich Dad Poor Dad: What the Rich Teach Their Kids About Money That the Poor and Middle Class Do Not is a personal finance book by Robert T. Kiyosaki (b. 1947) and Sharon Lechter, first published in April 1997 by Tech Press Inc. (self-published) and subsequently by Warner Books/Business Plus. The book presents a series of financial lessons framed through the contrasting philosophies of Kiyosaki's two 'fathers': his biological father — the 'poor dad' — a highly educated government employee who followed conventional financial advice (get a good education, find a secure job, save money, buy a house) and died nearly penniless; and the father of his best friend — the 'rich dad' — who had minimal formal education but became wealthy through financial literacy, asset building, and entrepreneurship.\n\nRich Dad Poor Dad has become one of the bestselling personal finance books of all time — selling over 32 million copies in 109 languages (as of 2021) and spending more than six years on The New York Times bestseller list. Its core argument is that the traditional middle-class approach to money (work for wages, pay taxes, buy consumer goods and a home) perpetuates financial dependence, while financial freedom requires building assets that generate passive income (businesses, real estate, intellectual property) rather than working for earned income that is taxed at higher rates. The book introduced the concepts of the 'rat race', 'financial literacy', and 'passive income' to mass popular culture.\n\nRich Dad Poor Dad is highly controversial — critics (including financial journalist John Reed and economists) have disputed whether the 'rich dad' was a real person, questioned Kiyosaki's financial advice (particularly his advocacy of real estate investment and tax avoidance strategies), and noted that much of the book's advice is vague or potentially harmful. Nevertheless, its cultural impact is undeniable: it triggered a personal finance publishing phenomenon, inspired the Rich Dad franchise (games, courses, seminars), and fundamentally shifted public discourse about financial literacy, passive income, and entrepreneurship in the late 1990s and 2000s.",
    "causes": [
      "The cultural context of the 1990s American economic boom — the dot-com expansion, the democratisation of investment through mutual funds and 401(k) plans, and the growing popular interest in wealth building — provided the receptive audience for Kiyosaki's argument that financial literacy, not conventional employment, was the path to wealth.",
      "Kiyosaki's own background in Hawaiian real estate investment and direct sales (including Amway) — and his conviction that conventional financial advice given to the middle class was fundamentally flawed — motivated the book's argument that traditional education does not teach financial literacy.",
      "The personal finance genre's evolution in the 1990s — from technical investment advice to accessible financial philosophy — created the market niche in which Rich Dad Poor Dad's narrative-driven, aphoristic approach (avoiding technical financial jargon in favour of memorable principles) could achieve mass-market success."
    ],
    "effects": [
      "Rich Dad Poor Dad became one of the bestselling personal finance books of all time — selling over 32 million copies in 109 languages, it popularised the concepts of passive income, financial literacy, and the distinction between assets and liabilities for a mass global audience, fundamentally shaping popular financial thinking in the late 1990s and 2000s.",
      "The Rich Dad brand expanded into a global franchise — the CASHFLOW board game (designed to teach financial concepts), a series of follow-up books, seminars, and courses generated hundreds of millions of dollars in revenue, demonstrating the commercial model of the personal finance celebrity brand that combined publishing with education and events.",
      "Rich Dad Poor Dad triggered significant controversy and criticism — John Reed's detailed refutation of Kiyosaki's financial claims, academic critiques of his tax advice, and questions about the 'rich dad' character's existence generated ongoing public debate about financial literacy education, the reliability of popular personal finance advice, and the ethics of wealth-building seminars."
    ],
    "relationships": [
      {"sourceSlug": "robert-kiyosaki", "sourceName": "Robert T. Kiyosaki (b. 1947 — Hawaiian businessman; Rich Dad franchise; personal finance celebrity)", "verb": "AUTHORS", "targetSlug": "rich-dad-poor-dad", "targetName": "Rich Dad Poor Dad (1997 — 32+ million copies; passive income, financial literacy mass popularisation)", "context": "Kiyosaki published Rich Dad Poor Dad in 1997 — one of the bestselling personal finance books of all time, introducing passive income and financial literacy as mass popular culture concepts."},
      {"sourceSlug": "rich-dad-poor-dad", "sourceName": "Rich Dad Poor Dad (passive income — rat race, assets vs liabilities; financial literacy education)", "verb": "POPULARISES", "targetSlug": "financial-literacy-movement", "targetName": "Financial literacy movement (passive income, asset building — mass popular education; 1990s–2000s)", "context": "Rich Dad Poor Dad popularised the concepts of passive income, financial literacy, and the distinction between assets and liabilities for a mass global audience, shaping popular financial discourse in the late 1990s and 2000s."},
      {"sourceSlug": "rich-dad-poor-dad", "sourceName": "Rich Dad Poor Dad (CASHFLOW board game — Rich Dad franchise; seminars, courses)", "verb": "GENERATES", "targetSlug": "rich-dad-franchise", "targetName": "Rich Dad franchise (CASHFLOW board game, seminars, courses — personal finance celebrity brand)", "context": "Rich Dad Poor Dad expanded into the Rich Dad franchise — the CASHFLOW board game, seminars, and courses generated hundreds of millions in revenue, establishing the personal finance celebrity brand model."}
    ],
    "places": [
      {"name": "Hawaii / United States (Kiyosaki's real estate background; 1997 publication; New York Times bestseller list)", "role": "Rich Dad Poor Dad was inspired by Kiyosaki's Hawaiian background and published in the United States in 1997 — it spent more than six years on the New York Times bestseller list, establishing a dominant presence in American personal finance culture"},
      {"name": "Global (32+ million copies; 109 languages; international franchise — Asia, Australia, Europe, Latin America)", "role": "Rich Dad Poor Dad became a global phenomenon — 32+ million copies sold in 109 languages, with particularly strong sales in Asia, Australia, and Latin America, demonstrating the universal appeal of financial independence messaging"}
    ],
    "subjects": ["Personal Finance", "21st Century", "Robert Kiyosaki", "Financial Literacy", "Self-Help", "Entrepreneurship", "Popular Culture", "American Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Rich Dad Poor Dad (Kiyosaki, 1997) is one of the bestselling personal finance books of all time — 32+ million copies, 109 languages — and a transformative force in popular financial culture, popularising passive income and financial literacy as mass concepts. Despite significant controversy about its claims and advice, its cultural impact on financial discourse and the personal finance publishing genre was enormous.",
      "significanceCategory": "significant"
    }
  }
},

"the-memoirs-of-sherlock-holmes": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-memoirs-of-sherlock-holmes.json",
  "slug": "the-memoirs-of-sherlock-holmes",
  "data": {
    "summary": "The Memoirs of Sherlock Holmes is the second collection of Sherlock Holmes short stories by Arthur Conan Doyle (1859–1930), published in book form in December 1893 by George Newnes, Ltd., following serial publication in The Strand Magazine (December 1892 – December 1893). The collection contains twelve stories — including some of the most celebrated in the Holmes canon: The Adventure of Silver Blaze (the racehorse mystery, source of the 'dog in the night-time' clue), The Adventure of the Musgrave Ritual (Holmes's first case as narrated in retrospect), The Adventure of the Greek Interpreter (the first appearance of Mycroft Holmes), and The Final Problem — the story in which Holmes and Professor Moriarty fall to their apparent deaths at the Reichenbach Falls in Switzerland.\n\nThe Memoirs is especially significant in the Sherlock Holmes canon because it contains The Final Problem (1893) — the story in which Conan Doyle attempted to kill off Holmes by sending him over the Reichenbach Falls with the 'Napoleon of Crime', Professor Moriarty. The public reaction to Holmes's apparent death was extraordinary: thousands of readers cancelled their subscriptions to The Strand Magazine, hundreds wore black mourning dress in London's streets, and the public outcry was so intense that Conan Doyle was compelled to resurrect Holmes in The Adventure of the Empty House (1903) — a ten-year gap in Holmes's career that Doyle filled retrospectively.\n\nThe Memoirs also introduces Mycroft Holmes — the older, more brilliant but less active brother — and the Diogenes Club, and establishes the villainous Professor Moriarty as Holmes's supreme intellectual antagonist. The collection is a milestone in the development of detective fiction: The Final Problem's moral and psychological complexity, the tragedy of the 'good detective' apparently sacrificed in the defeat of the 'Napoleon of Crime', elevated the detective genre beyond puzzle fiction toward genuine literary tragedy.",
    "causes": [
      "Conan Doyle's desire to end the Sherlock Holmes stories — his frustration with Holmes overshadowing his other literary work and his conviction that Holmes was preventing him from writing more serious literature — drove the decision to kill off the detective in The Final Problem, which ends the Memoirs.",
      "The extraordinary commercial success of the first Holmes collection (The Adventures of Sherlock Holmes, 1892) and the sustained demand from The Strand Magazine's readership for further Holmes stories drove the production of The Memoirs — Conan Doyle continued writing despite his ambivalence, producing some of the finest stories in the canon.",
      "The Swiss Alps setting of the Reichenbach Falls — visited by Conan Doyle during a holiday in 1893 — provided the dramatic landscape for The Final Problem's climactic confrontation, and the geography of the falls made the double fall a plausible and spectacular denouement."
    ],
    "effects": [
      "The public reaction to Holmes's death in The Final Problem (1893) was the most dramatic literary mourning event of the Victorian era — thousands of reader cancelled Strand subscriptions, hundreds wore black in London streets, and the public outcry became a landmark in the history of celebrity and reader response, demonstrating that Holmes had become genuinely culturally real to his audience.",
      "The ten-year 'hiatus' between Holmes's apparent death (1893) and his resurrection in The Adventure of the Empty House (1903) became one of the most famous gaps in literary history — generating stories, pastiches, and fan fiction about what Holmes was doing during those years, and demonstrating the extraordinary cultural afterlife of the character.",
      "The introduction of Professor Moriarty in The Final Problem established the 'Napoleon of Crime' as the archetypal criminal mastermind in detective fiction — Moriarty's structural role (the intellectual equal and dark mirror of the detective) became a foundational convention of the genre, imitated in countless detective stories and thrillers."
    ],
    "relationships": [
      {"sourceSlug": "arthur-conan-doyle", "sourceName": "Arthur Conan Doyle (1859–1930 — Sherlock Holmes creator; The Strand Magazine)", "verb": "AUTHORS", "targetSlug": "the-memoirs-of-sherlock-holmes", "targetName": "The Memoirs of Sherlock Holmes (1893 — The Final Problem; Reichenbach Falls; Moriarty)", "context": "Conan Doyle published The Memoirs of Sherlock Holmes in 1893 — the collection ends with The Final Problem, in which Holmes and Moriarty fall to their apparent deaths at the Reichenbach Falls."},
      {"sourceSlug": "the-memoirs-of-sherlock-holmes", "sourceName": "Memoirs of Sherlock Holmes (The Final Problem 1893 — public mourning; Strand Magazine cancellations)", "verb": "GENERATES", "targetSlug": "holmes-public-mourning-1893", "targetName": "Holmes public mourning (1893 — Victorian reader response; black dress in London; Strand cancellations)", "context": "The public reaction to Holmes's apparent death in The Final Problem (1893) was extraordinary — thousands cancelled Strand subscriptions, hundreds wore mourning dress in London streets — a landmark in the history of celebrity and reader response."},
      {"sourceSlug": "the-memoirs-of-sherlock-holmes", "sourceName": "Memoirs of Sherlock Holmes (Moriarty — Napoleon of Crime; criminal mastermind archetype)", "verb": "INTRODUCES", "targetSlug": "professor-moriarty", "targetName": "Professor Moriarty (Napoleon of Crime — criminal mastermind archetype; detective fiction convention)", "context": "The Memoirs introduces Professor Moriarty as Holmes's supreme antagonist — the 'Napoleon of Crime' established the criminal mastermind as the archetypal villain in detective fiction, imitated across the genre."}
    ],
    "places": [
      {"name": "London (The Strand Magazine — Victorian readership; public mourning 1893; Diogenes Club)", "role": "The Memoirs of Sherlock Holmes was serialised in The Strand Magazine in London — the public mourning for Holmes's death in the Victorian city demonstrated the character's extraordinary cultural reality to his audience"},
      {"name": "Reichenbach Falls, Switzerland (The Final Problem — dramatic death scene; Conan Doyle's 1893 holiday)", "role": "The Reichenbach Falls near Meiringen, Switzerland — visited by Conan Doyle in 1893 — became the iconic setting for Holmes's apparent death in The Final Problem"}
    ],
    "subjects": ["English Literature", "Victorian Era", "Detective Fiction", "Arthur Conan Doyle", "Sherlock Holmes", "Short Stories", "Crime Fiction", "Victorian Culture"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Memoirs of Sherlock Holmes (Conan Doyle, 1893) contains The Final Problem — the story of Holmes's apparent death at the Reichenbach Falls, which provoked the most dramatic literary mourning in Victorian England (black dress in London streets, mass Strand cancellations). It introduced Professor Moriarty as the archetypal criminal mastermind and elevated detective fiction toward literary tragedy.",
      "significanceCategory": "highly-significant"
    }
  }
},

"the-return-of-sherlock-holmes": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-return-of-sherlock-holmes.json",
  "slug": "the-return-of-sherlock-holmes",
  "data": {
    "summary": "The Return of Sherlock Holmes is the third collection of Sherlock Holmes short stories by Arthur Conan Doyle (1859–1930), published in book form in 1905 by George Newnes, Ltd., following serial publication in The Strand Magazine (October 1903 – December 1904). The collection contains thirteen stories and begins with The Adventure of the Empty House — the story in which Holmes dramatically reveals himself to be alive after his apparent death at the Reichenbach Falls in The Final Problem (1893), explaining that he used his knowledge of baritsu (a Japanese system of wrestling) to prevent Moriarty from pulling him over the edge, and that he has spent three years in disguise — the 'Great Hiatus' — travelling to avoid Moriarty's surviving associates.\n\nThe Return of Sherlock Holmes was one of the most eagerly anticipated publications in literary history — the ten-year interval between The Final Problem (1893) and The Adventure of the Empty House (1903) had created intense public anticipation, and the first story of the Return achieved extraordinary popularity. The stories in the Return are widely considered among Conan Doyle's finest — including The Adventure of the Dancing Men (the cipher mystery), The Adventure of the Priory School (the Duke of Holdernesse case), The Adventure of the Six Napoleons (the Borgia pearl), and The Adventure of the Second Stain (the international diplomatic crisis).\n\nThe Return established several important developments in Holmes's later career: the villain Colonel Sebastian Moran (Moriarty's chief of staff, the 'second most dangerous man in London'), the air-gun as a murder weapon, and Holmes's more complex emotional and professional maturity. The collection demonstrates Conan Doyle's craft at its peak — the stories balance Holmes's deductive brilliance with richer psychological portraits of Watson, more complex plots, and a greater range of social settings from aristocratic country houses to London's underworld.",
    "causes": [
      "The overwhelming public demand for Holmes's resurrection — the reader outcry at The Final Problem (1893), the persistent public pressure on Conan Doyle, and the financial incentives offered by publishers and magazine editors — eventually compelled Doyle to resurrect Holmes despite his personal preference to continue with other literary work.",
      "Conan Doyle's growing craft as a short story writer — the decade between the Memoirs (1893) and the Return (1905) allowed him to develop his technique, and the Return stories demonstrate a more sophisticated approach to plot construction, characterisation, and the integration of detective logic with social observation.",
      "The 'Great Hiatus' — Holmes's three-year absence, which Doyle explained through Holmes's disguised travels to Tibet, Persia, and Mecca — created the retrospective narrative challenge that Doyle met in The Empty House, providing a plausible explanation for the survival that satisfied the public's demand for continuity."
    ],
    "effects": [
      "The Return of Sherlock Holmes confirmed Holmes as the most commercially valuable fictional character of the Edwardian era — the sustained public enthusiasm for Holmes's resurrection and the critical success of the Return's stories demonstrated that the detective genre had achieved a level of mass cultural embedding unprecedented in earlier literary history.",
      "The Return's stories — particularly The Dancing Men (cipher), The Six Napoleons (Borgia pearl), and The Second Stain (diplomatic crisis) — established the range of the Holmes canon, demonstrating that the detective story could encompass cryptography, international diplomacy, aristocratic intrigue, and urban crime with equal facility.",
      "The Adventure of the Empty House's explanation of Holmes's survival during the 'Great Hiatus' (Tibet, Persia, Mecca; disguised as 'Sigerson the Norwegian explorer') became one of the most analysed passages in the Holmes canon — the focus of 'Sherlockian' scholarship, fan fiction, and dramatic adaptations exploring the three missing years."
    ],
    "relationships": [
      {"sourceSlug": "arthur-conan-doyle", "sourceName": "Arthur Conan Doyle (1859–1930 — Holmes resurrection; The Strand Magazine; reader pressure)", "verb": "AUTHORS", "targetSlug": "the-return-of-sherlock-holmes", "targetName": "The Return of Sherlock Holmes (1905 — The Empty House; Great Hiatus explanation; Edwardian era)", "context": "Conan Doyle published The Return of Sherlock Holmes in 1905 — compelled by public demand, he resurrected Holmes in The Adventure of the Empty House (1903) after a ten-year apparent death."},
      {"sourceSlug": "the-return-of-sherlock-holmes", "sourceName": "The Return (The Empty House — Great Hiatus; baritsu; Colonel Moran)", "verb": "CONTINUES", "targetSlug": "the-memoirs-of-sherlock-holmes", "targetName": "The Memoirs of Sherlock Holmes (1893 — The Final Problem; apparent death at Reichenbach)", "context": "The Return of Sherlock Holmes continues directly from the Memoirs — The Empty House explains Holmes's survival at the Reichenbach Falls and reveals the Great Hiatus, satisfying the public demand for continuity after a ten-year absence."},
      {"sourceSlug": "the-return-of-sherlock-holmes", "sourceName": "Return of Sherlock Holmes (Great Hiatus — Tibet, Persia, Mecca; Sherlockian scholarship)", "verb": "GENERATES", "targetSlug": "sherlockian-scholarship", "targetName": "Sherlockian scholarship (Great Hiatus pastiches — fan fiction, dramatic adaptations, academic study)", "context": "The Return's explanation of the Great Hiatus (Holmes disguised as 'Sigerson the Norwegian' in Tibet, Persia, and Mecca) became a focus of Sherlockian scholarship and fan fiction exploring the three missing years."}
    ],
    "places": [
      {"name": "London (The Strand Magazine — Edwardian readership; public enthusiasm for Holmes's return)", "role": "The Return of Sherlock Holmes was serialised in The Strand Magazine in Edwardian London — its publication was one of the most eagerly anticipated literary events in British publishing history"},
      {"name": "Tibet, Persia, Mecca (the 'Great Hiatus' — Holmes's disguised travels as 'Sigerson the Norwegian')", "role": "Holmes's supposed travels during the Great Hiatus (Tibet, Persia, Mecca) — as explained in The Empty House — became some of the most discussed passages in the Holmes canon, generating pastiches and scholarly analysis"}
    ],
    "subjects": ["English Literature", "Edwardian Era", "Detective Fiction", "Arthur Conan Doyle", "Sherlock Holmes", "Short Stories", "Crime Fiction", "Popular Culture"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Return of Sherlock Holmes (Conan Doyle, 1905) was one of the most eagerly anticipated publications in literary history — the resurrection of Holmes after a ten-year 'death' demonstrated the character's unique cultural reality. The Return's stories (Dancing Men cipher, Six Napoleons, Second Stain) are considered among Doyle's finest, and the Great Hiatus explanation generated a tradition of Sherlockian scholarship and fan fiction.",
      "significanceCategory": "significant"
    }
  }
},

"the-adventures-of-tom-bombadil": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-adventures-of-tom-bombadil.json",
  "slug": "the-adventures-of-tom-bombadil",
  "data": {
    "summary": "The Adventures of Tom Bombadil and Other Verses from the Red Book is a collection of sixteen poems by J.R.R. Tolkien (1892–1973), published on 22 November 1962 by George Allen & Unwin. The collection is presented as verses from the 'Red Book of Westmarch' (the fictional manuscript from which The Lord of the Rings is supposed to be taken), providing a Middle-earth fictional frame for Tolkien's poetry. The title poem 'The Adventures of Tom Bombadil' was first published in The Oxford Magazine in February 1934, long before The Lord of the Rings, and presents a playful, rhythmically energetic account of the mysterious figure Tom Bombadil — encountered in The Fellowship of the Ring — in his earlier adventures.\n\nThe Adventures of Tom Bombadil is significant both as a document of Tolkien's development as a poet and as a key text in the scholarship of Middle-earth — the poem explores Tom Bombadil's nature and his relationships with the creatures of the Old Forest, and its publication in 1934 demonstrates that Bombadil preceded The Lord of the Rings as a character in Tolkien's imagination. The collection also includes 'The Sea-Bell (or Frodo's Dreme)' — a melancholy poem about a man who sails to an enchanted land but cannot belong there, widely interpreted as autobiographical — and several Hobbit poems and riddles that illuminate the cultural life of the Shire.\n\nThe collection is a valuable text for Tolkien scholars interested in the relationship between his poetry and his prose mythology — several poems predate The Lord of the Rings and offer insight into Tolkien's creative process, while others are written in the voices of Hobbit characters, extending the imaginative world of Middle-earth in poetic form. Tom Bombadil himself remains one of the most debated figures in Tolkien scholarship — his immunity to the One Ring, his cheerful indifference to Sauron's power, and his ambiguous ontological status (is he a Maia? a Vala? something older?) have generated extensive scholarly and fan speculation.",
    "causes": [
      "Tolkien's long engagement with the Tom Bombadil character — first created as a children's story for his children and first published in poem form in 1934, decades before The Lord of the Rings — motivated the compilation of The Adventures of Tom Bombadil as a retrospective collection of his lighter poetry.",
      "The publication of The Lord of the Rings (1954–1955) and its extraordinary success created a readership hungry for any additional material from Middle-earth — The Adventures of Tom Bombadil (1962) met this demand by offering poems set in or adjacent to the Middle-earth world, framed as Hobbit cultural material from the Red Book.",
      "George Allen & Unwin's interest in publishing additional Tolkien material — driven by the commercial success of The Lord of the Rings — provided the publishing context for The Adventures of Tom Bombadil, which Tolkien assembled from poems written across many decades."
    ],
    "effects": [
      "The Adventures of Tom Bombadil became an important text in Tolkien scholarship — the title poem's 1934 original publication date demonstrates that Tom Bombadil predates The Lord of the Rings, providing evidence for the chronological development of Tolkien's mythology and the relationship between his poetry and prose.",
      "Tom Bombadil's complex theological status in the collection — his immunity to the One Ring, his cheerful indifference to Sauron, his songs as the medium of his power — has generated extensive scholarly speculation about his nature, making him one of the most debated figures in Tolkien scholarship and fan communities.",
      "The framing of the collection as verses from the Red Book of Westmarch — presented as Hobbit cultural material, written in Hobbit voices — extended Tolkien's practice of 'secondary world' creation through the conceit of a fictional manuscript, demonstrating his consistent use of the fictional textual frame to deepen the reality of Middle-earth."
    ],
    "relationships": [
      {"sourceSlug": "j-r-r-tolkien", "sourceName": "J.R.R. Tolkien (1892–1973 — Tom Bombadil character; Red Book framing; Middle-earth poetry)", "verb": "AUTHORS", "targetSlug": "the-adventures-of-tom-bombadil", "targetName": "The Adventures of Tom Bombadil (1962 — Hobbit verses; Red Book; Tom Bombadil pre-Lord of the Rings)", "context": "Tolkien published The Adventures of Tom Bombadil in 1962 — the collection frames sixteen poems as verses from the Red Book of Westmarch, and the title poem's 1934 origin predates The Lord of the Rings."},
      {"sourceSlug": "the-adventures-of-tom-bombadil", "sourceName": "Adventures of Tom Bombadil (Tom Bombadil — immunity to Ring; One Ring; scholarly debate)", "verb": "EXPLORES", "targetSlug": "tom-bombadil", "targetName": "Tom Bombadil (Middle-earth — immunity to One Ring; ontological mystery; pre-Lord of the Rings character)", "context": "The Adventures of Tom Bombadil provides the fullest poetic portrait of Tom Bombadil — his immunity to the One Ring and his ambiguous ontological status (Maia? Vala? something older?) have generated extensive Tolkien scholarship."},
      {"sourceSlug": "the-adventures-of-tom-bombadil", "sourceName": "Adventures of Tom Bombadil (Red Book of Westmarch — fictional manuscript frame; secondary world creation)", "verb": "EXTENDS", "targetSlug": "the-lord-of-the-rings", "targetName": "The Lord of the Rings (1954–55 — Red Book of Westmarch; fictional manuscript conceit; Middle-earth)", "context": "The Adventures of Tom Bombadil extends The Lord of the Rings' fictional manuscript conceit — framed as verses from the Red Book of Westmarch, it deepens the secondary world of Middle-earth through Hobbit cultural material."}
    ],
    "places": [
      {"name": "Oxford, England (Tolkien's academic career — Tom Bombadil created for his children; Oxford Magazine 1934)", "role": "Tom Bombadil was created in Oxford during Tolkien's career as a professor — first published in The Oxford Magazine in 1934, he preceded the entire Lord of the Rings mythology"},
      {"name": "Middle-earth (fictional — Old Forest; Shire; Red Book of Westmarch — Tolkien's secondary world)", "role": "The Adventures of Tom Bombadil is set in Middle-earth — framed as Hobbit cultural material from the Red Book of Westmarch, it extends the secondary world Tolkien created in The Lord of the Rings"}
    ],
    "subjects": ["English Literature", "20th Century", "J.R.R. Tolkien", "Fantasy Literature", "Poetry", "Middle-earth", "Children's Literature", "Mythology"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "The Adventures of Tom Bombadil (Tolkien, 1962) is a key text for Tolkien scholars — the title poem's 1934 origin predates The Lord of the Rings, demonstrating Tom Bombadil's priority in Tolkien's imagination. The collection's Red Book framing extends Tolkien's secondary world creation through poetry, and Tom Bombadil's immunity to the One Ring remains one of the most debated questions in Tolkien scholarship.",
      "significanceCategory": "significant"
    }
  }
},

"guinness-world-records": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780guinness-world-records.json",
  "slug": "guinness-world-records",
  "data": {
    "summary": "The Guinness World Records (originally published as The Guinness Book of Records) is an annual reference book published by Guinness World Records Ltd., first published on 27 August 1955 by the Guinness Brewery as a commercial gift for pub landlords. The first edition was compiled by twin brothers Norris (1925–2004) and Ross McWhirter (1925–1975) after managing director Sir Hugh Beaver was unable to settle a pub argument about whether the golden plover or the grouse was Europe's fastest game bird — the concept was that a book of verified facts about superlatives (the fastest, the tallest, the oldest, the heaviest, the most numerous) could settle similar disputes and serve as a promotional tool for the brewery.\n\nThe Guinness Book of Records became one of the bestselling copyright books of all time — it has appeared on The New York Times bestseller list more than any other book, has sold over 143 million copies in more than 100 countries, and has been published in at least 37 languages. Its annual publication (first as a UK edition, expanded globally from the 1960s) made it a fixture of Christmas gift-giving in the English-speaking world — 'looking up records in the Guinness Book' became a cultural ritual that persisted for decades, and the book's role as a family reference and object of wonder established it as one of the most widely owned reference books in history.\n\nGuinness World Records transformed the concept of the 'record' from a competitive sporting achievement into a cultural category — the pursuit of Guinness records became a global participatory phenomenon, generating thousands of record-breaking attempts annually in categories from athletics to eating, from the bizarre to the inspiring. The brand's evolution from printed annual to a global media and events organisation — including record certification, live events, and television specials — demonstrates how a promotional concept became a self-sustaining cultural institution.",
    "causes": [
      "Sir Hugh Beaver's pub argument (August 1951) about whether the golden plover or the grouse was Europe's fastest game bird — and his realisation that similar arguments about superlatives were unresolvable without a reliable reference work — provided the founding concept for the Guinness Book of Records as a verified compendium of superlatives.",
      "Norris and Ross McWhirter's exceptional research abilities — both were professional fact-finders and journalists who had established a research agency — provided the practical capacity to compile and verify the enormous range of facts required for the first edition in a remarkably short time.",
      "The Guinness Brewery's commercial strategy — distributing the book free to pub landlords as a promotional tool — provided the initial distribution network that gave the book its first audience, demonstrating how a corporate promotional item could become an independent cultural institution."
    ],
    "effects": [
      "The Guinness Book of Records became one of the bestselling copyright books of all time — appearing on the New York Times bestseller list more than any other book, selling over 143 million copies — and its annual Christmas gift-giving presence made it one of the most widely owned reference books in the English-speaking world.",
      "The Guinness record concept transformed 'record-breaking' from a competitive achievement into a global participatory phenomenon — the pursuit of Guinness records in categories from the athletic to the bizarre created a worldwide culture of superlative-seeking that generated thousands of record attempts annually, from school children to professional performers.",
      "The assassination of Ross McWhirter in November 1975 — he was shot at his doorstep by IRA gunmen after offering a £50,000 reward for information leading to the arrest of IRA bombers — transformed the Guinness Book's history into a tragic chapter of the Troubles, demonstrating that the book's founders were directly implicated in the political violence of the era."
    ],
    "relationships": [
      {"sourceSlug": "norris-mcwhirter", "sourceName": "Norris McWhirter (1925–2004) and Ross McWhirter (1925–1975) — research journalists; Guinness compilers", "verb": "COMPILES", "targetSlug": "guinness-world-records", "targetName": "Guinness World Records (1955 — bestselling copyright book; 143+ million copies; record-breaking culture)", "context": "Norris and Ross McWhirter compiled the first Guinness Book of Records (1955) at the commission of the Guinness Brewery — their fact-finding expertise created one of the bestselling copyright books of all time."},
      {"sourceSlug": "guinness-world-records", "sourceName": "Guinness World Records (record-breaking culture — participatory phenomenon; global events)", "verb": "CREATES", "targetSlug": "record-breaking-culture", "targetName": "Record-breaking culture (participatory — thousands of annual attempts; global phenomenon; Guinness certification)", "context": "Guinness World Records transformed 'record-breaking' into a global participatory phenomenon — the pursuit of Guinness records in categories from the athletic to the bizarre generated thousands of annual attempts worldwide."},
      {"sourceSlug": "guinness-world-records", "sourceName": "Guinness World Records (Ross McWhirter assassination 1975 — IRA; Troubles; £50,000 reward)", "verb": "IMPLICATES", "targetSlug": "the-troubles-northern-ireland", "targetName": "The Troubles (Northern Ireland — IRA; Ross McWhirter assassination November 1975)", "context": "Ross McWhirter's assassination by IRA gunmen in November 1975 — after he offered a £50,000 reward for information on IRA bombers — directly connected the Guinness Book's history to the political violence of the Troubles."}
    ],
    "places": [
      {"name": "Ireland / London (Guinness Brewery — pub argument August 1951; first published 27 August 1955)", "role": "The Guinness Book of Records was conceived from a pub argument in August 1951 and first published on 27 August 1955 by the Guinness Brewery — a corporate promotional item that became an independent cultural institution"},
      {"name": "Global (143+ million copies; 100+ countries; 37+ languages; annual Christmas gift-giving tradition)", "role": "Guinness World Records achieved global reach — 143+ million copies in over 100 countries and 37 languages, with the annual Christmas gift-giving tradition making it one of the most widely owned reference books in history"}
    ],
    "subjects": ["Reference Books", "20th Century", "Norris McWhirter", "Popular Culture", "Record-Breaking", "British Culture", "Commercial Publishing", "Cultural Institutions"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Guinness World Records (first published 1955) is one of the bestselling copyright books of all time — appearing on the New York Times bestseller list more than any other book, selling 143+ million copies. It transformed 'record-breaking' into a global participatory culture, and its founding story (a Guinness pub argument about game birds) became one of the most charming origin stories in publishing history.",
      "significanceCategory": "significant"
    }
  }
},

"quidditch-through-the-ages": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780quidditch-through-the-ages.json",
  "slug": "quidditch-through-the-ages",
  "data": {
    "summary": "Quidditch Through the Ages is a companion book to the Harry Potter series by J.K. Rowling (b. 1965), published on 12 March 2001 by Bloomsbury (UK) and Scholastic (US), simultaneously with Fantastic Beasts and Where to Find Them. The book is presented as a real in-universe text — a copy of the book described as being found in the Hogwarts library, 'written by' Kennilworthy Whisp — that describes the history, rules, and teams of Quidditch, the fictional wizarding sport played on broomsticks. Both Quidditch Through the Ages and Fantastic Beasts were published for Comic Relief, with all author royalties donated to the charity.\n\nQuidditch Through the Ages is an example of the 'fictional textbook' genre within the Harry Potter universe — books presented as real in-universe artefacts that expand the world of wizarding Britain by providing detailed fictional histories, taxonomies, and cultural contexts beyond what appears in the main novels. The book describes the origins of Quidditch (from a fictional historical account of broomstick games in medieval Britain), the evolution of the rules and equipment, and the thirteen principal Quidditch teams of Britain and Ireland.\n\nThe publication of Quidditch Through the Ages and Fantastic Beasts demonstrated J.K. Rowling's awareness of secondary world creation as a commercial and cultural strategy — the in-universe fictional textbook format allowed her to expand the Harry Potter world without continuing the main narrative, generating new layers of detail that deepened the immersive quality of the wizarding world for fans. The books also demonstrated the enormous commercial power of the Harry Potter brand — both sold in the millions worldwide and made substantial donations to Comic Relief. The Quidditch sport itself became one of the Harry Potter universe's most significant cultural exports, inspiring 'Muggle Quidditch' (now 'Quadball'), a real athletic sport played on university campuses worldwide with a broom between the legs.",
    "causes": [
      "J.K. Rowling's creation of Quidditch as the central wizarding sport in the Harry Potter novels — with its distinctive positions (Seeker, Keeper, Chaser, Beater), equipment (the Golden Snitch, Bludgers, Quaffle), and cultural significance in the wizarding world — created a detailed enough fictional sport to support an entire companion book.",
      "Comic Relief's collaboration with Rowling and Bloomsbury — the decision to publish two companion books simultaneously for charity — provided both the publishing vehicle and the philanthropic framing that gave the project additional cultural legitimacy beyond mere commercial spin-off.",
      "The Harry Potter fandom's extraordinary appetite for additional world-building material — the desire for more detail about Hogwarts, wizarding culture, and the historical depth of the wizarding world — created the market for fictional companion books presented as in-universe artefacts."
    ],
    "effects": [
      "Quidditch Through the Ages became a bestseller worldwide — demonstrating the extraordinary commercial power of the Harry Potter brand to extend far beyond the main novels and generating millions in donations for Comic Relief, establishing a model for franchise companion books as both commercial products and charitable vehicles.",
      "Quidditch inspired the creation of 'Muggle Quidditch' (now officially 'Quadball') — a real athletic sport played on university campuses worldwide, adapted from the fictional game with a broom between the legs; the International Quidditch Association (IQA) was founded in 2010, and the sport is now played in over 40 countries, demonstrating how a fictional sport can inspire a real-world athletic movement.",
      "Quidditch Through the Ages demonstrated the viability of the 'fictional textbook' as a Harry Potter franchise format — establishing the template for subsequent in-universe companion books (The Tales of Beedle the Bard, 2008) and for the Wizarding World's expansion into theme parks, films, and merchandise."
    ],
    "relationships": [
      {"sourceSlug": "j-k-rowling", "sourceName": "J.K. Rowling (b. 1965 — Harry Potter universe; in-universe fictional textbook format)", "verb": "AUTHORS", "targetSlug": "quidditch-through-the-ages", "targetName": "Quidditch Through the Ages (2001 — Comic Relief; fictional Hogwarts library book; Quidditch history)", "context": "Rowling published Quidditch Through the Ages in 2001 for Comic Relief — an in-universe fictional textbook presenting the history and rules of Quidditch, demonstrating the Harry Potter universe's capacity for secondary world expansion."},
      {"sourceSlug": "quidditch-through-the-ages", "sourceName": "Quidditch Through the Ages (Muggle Quidditch — Quadball; IQA founded 2010; 40+ countries)", "verb": "INSPIRES", "targetSlug": "quadball", "targetName": "Quadball (formerly Muggle Quidditch — real athletic sport; IQA 2010; 40+ countries)", "context": "The fictional sport Quidditch inspired 'Muggle Quidditch' (now Quadball) — a real athletic sport played on university campuses worldwide with a broom between the legs; the IQA was founded in 2010 and the sport is now played in over 40 countries."},
      {"sourceSlug": "quidditch-through-the-ages", "sourceName": "Quidditch Through the Ages (Comic Relief — charitable proceeds; franchise companion model)", "verb": "COMPLEMENTS", "targetSlug": "fantastic-beasts-and-where-to-find-them", "targetName": "Fantastic Beasts and Where to Find Them (2001 — companion to Quidditch Through the Ages; Comic Relief)", "context": "Quidditch Through the Ages was published simultaneously with Fantastic Beasts and Where to Find Them (2001) for Comic Relief — together they established the in-universe fictional textbook as a Harry Potter franchise format."}
    ],
    "places": [
      {"name": "United Kingdom (Bloomsbury 2001 — Comic Relief; Harry Potter fandom; wizarding Britain)", "role": "Published by Bloomsbury in 2001 for Comic Relief — Quidditch Through the Ages extended the wizarding Britain of the Harry Potter novels with a fictional history of the sport"},
      {"name": "Global (Muggle Quidditch/Quadball — 40+ countries; university campuses; IQA 2010)", "role": "Quidditch Through the Ages inspired Quadball, now played in over 40 countries — a real athletic movement born from a fictional book, demonstrating the Harry Potter universe's extraordinary cultural generativity"}
    ],
    "subjects": ["English Literature", "21st Century", "J.K. Rowling", "Fantasy Literature", "Harry Potter", "Children's Literature", "Sports Culture", "Charitable Publishing"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Quidditch Through the Ages (Rowling, 2001) is a landmark example of the 'fictional textbook' as a franchise companion format — published for Comic Relief, it expanded the Harry Potter universe while raising millions for charity. Its most remarkable legacy is inspiring Quadball (formerly Muggle Quidditch), a real athletic sport now played in over 40 countries, demonstrating how a fictional sport can generate a genuine global athletic movement.",
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
