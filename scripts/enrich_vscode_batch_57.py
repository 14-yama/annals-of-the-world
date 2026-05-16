#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 57 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Cross-cultural texts — philosophy, cosmology, chronicles, epics:
  From 782-Class (epic/literary texts):
    the-myth-of-sisyphus, the-silmarillion, the-tale-of-kieu, epic-of-king-gesar
  From 781-Class (chronicles and popular science):
    a-brief-history-of-time, primary-chronicle, kojiki, history-of-rome
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-57-may2026"

ENRICHMENTS = {

"the-myth-of-sisyphus": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782the-myth-of-sisyphus.json",
  "slug": "the-myth-of-sisyphus",
  "data": {
    "era": "Modern",
    "eraSlug": "modern",
    "eraDivision": "Modern",
    "eraDivisionCode": "950",
    "period": "1942",
    "continent": "Europe",
    "region": "Western Europe",
    "subjectHeadings": ["Artifacts & Texts -- Philosophy & Existentialism -- France -- Modern"],
    "subjects": ["French Literature", "Existentialism", "Absurdism", "Albert Camus", "Philosophy", "20th Century", "French Philosophy", "Modern Literature"],
    "frameworks": ["INTELLECTUAL_HISTORY", "CAUSE_AND_EFFECT"],
    "summary": "The Myth of Sisyphus is a 1942 philosophical essay by Albert Camus (1913–1960) that stands as one of the foundational texts of Absurdist philosophy. The essay opens with Camus's audacious claim that 'there is but one truly serious philosophical problem, and that is suicide' — arguing that the fundamental question for philosophy is not metaphysical but existential: why should one continue to live given the irrationality and meaninglessness of existence? Camus defines the absurd as the tension between humanity's deep desire for clarity, meaning, and order, and the universe's silent, indifferent refusal to satisfy that desire.\n\nThe essay develops through a tripartite structure: first, an analysis of the 'absurd feeling' as a philosophical starting point; second, a critique of three philosophical responses to the absurd — 'philosophical suicide' (Kierkegaard's leap of faith, Husserl's phenomenological return to essence), which Camus rejects as intellectual dishonesty; and physical suicide, which he also rejects; and finally, 'absurd revolt' — the affirmation of life in full consciousness of its meaninglessness. The essay's most celebrated section is the closing meditation on Sisyphus, the Greek hero condemned by the gods to roll a boulder up a hill for eternity only to watch it roll back down. Camus declares that Sisyphus must be imagined happy — his revolt against the absurdity of his fate, his full consciousness of it, and his continued effort constitute a human triumph.\n\nThe Myth of Sisyphus was published in the same year as Camus's novel The Stranger (1942) and closely associated with Jean-Paul Sartre's Being and Nothingness (1943) and the post-World War II existentialist movement in Paris — though Camus later rejected the existentialist label, insisting that Absurdism was distinct from existentialism (which, he argued, evaded the absurd through commitment or religion). The phrase 'one must imagine Sisyphus happy' has become one of the most quoted philosophical conclusions of the 20th century, and the essay's concepts — the absurd, revolt, freedom, passion — entered the general cultural vocabulary of the postwar world, influencing writers from Samuel Beckett to Haruki Murakami.",
    "causes": [
      "World War II and the Nazi occupation of France (1940–1944) — Camus wrote The Myth of Sisyphus during the German occupation of France, and the essay's engagement with the question of suicide and the meaning of resistance was directly shaped by the experience of living under totalitarian occupation, giving philosophical urgency to the question of whether life was worth continuing.",
      "The European existentialist tradition — Kierkegaard's leap of faith, Nietzsche's nihilism, Husserl's phenomenology, and Heidegger's analysis of anxiety and Being-towards-death provided Camus with the philosophical interlocutors against whom he defined Absurdism; the essay is substantially a critical response to what Camus called the 'philosophical suicides' of his predecessors who resolved the absurd through religion or systematic philosophy.",
      "Camus's personal intellectual formation — his Algerian Mediterranean background (shaped by sun, sea, physical pleasure, and the 'absurd' gap between the beauty of the natural world and human suffering), his early tuberculosis (which gave him a heightened sense of mortality), and his engagement with the French literary tradition of Malraux, Valéry, and Gide — produced the particular sensibility and the concrete, image-driven style of The Myth of Sisyphus."
    ],
    "effects": [
      "The Myth of Sisyphus established Absurdism as a major philosophical and literary movement — its concepts of the absurd, revolt, and the affirmation of life without appeal to transcendent meaning shaped postwar literature and theatre, including Samuel Beckett's Waiting for Godot (1953), Eugène Ionesco's Rhinoceros (1959), and Harold Pinter's The Birthday Party (1957), all of which dramatise the absurdist condition Camus described.",
      "Camus's distinction between the absurd and existentialism — his critique of Kierkegaard, Sartre, and Heidegger as 'philosophical suicides' who evaded the absurd rather than living it — sparked the famous intellectual quarrel between Camus and Sartre (culminating in their public break in 1952) that defined the cultural politics of postwar Paris and introduced the concept of 'committed literature' (littérature engagée) versus Camus's more aesthetically detached humanism.",
      "The phrase 'one must imagine Sisyphus happy' became a cultural touchstone for the 20th-century humanist response to meaninglessness — cited in existentialist literature, in responses to personal tragedy, in secular philosophy, and in popular culture as a shorthand for the affirmation of life without recourse to God or transcendent purpose; it is arguably the most quoted philosophical sentence of the post-1945 West."
    ],
    "relationships": [
      {"sourceSlug": "albert-camus", "sourceName": "Albert Camus (1913–1960 — French-Algerian writer; The Stranger; Nobel 1957)", "verb": "AUTHORS", "targetSlug": "the-myth-of-sisyphus", "targetName": "The Myth of Sisyphus (1942 — Absurdism; revolt; 'one must imagine Sisyphus happy')", "context": "Camus wrote The Myth of Sisyphus during the German occupation of France — the essay established Absurdism as a philosophical position distinct from existentialism and introduced the concept of absurd revolt."},
      {"sourceSlug": "the-myth-of-sisyphus", "sourceName": "The Myth of Sisyphus (absurd consciousness — revolt against meaninglessness; Beckett; Theatre of the Absurd)", "verb": "INFLUENCES", "targetSlug": "waiting-for-godot", "targetName": "Waiting for Godot (Samuel Beckett, 1953 — Theatre of the Absurd; meaninglessness; two men waiting)", "context": "Beckett's Waiting for Godot (1953) dramatised the absurdist condition — two men waiting endlessly for a Godot who never comes — that Camus had theorised in The Myth of Sisyphus; the play is the theatrical embodiment of Camus's philosophical analysis."},
      {"sourceSlug": "the-myth-of-sisyphus", "sourceName": "The Myth of Sisyphus (Camus vs. Sartre — 'philosophical suicide'; engaged literature debate; 1952 break)", "verb": "SHAPES", "targetSlug": "jean-paul-sartre", "targetName": "Jean-Paul Sartre (1905–1980 — Being and Nothingness; existentialism; engaged literature)", "context": "Camus's critique of existentialism as a 'philosophical suicide' in The Myth of Sisyphus set up the intellectual tension with Sartre that culminated in their famous public break in 1952 — one of the defining intellectual quarrels of postwar Paris."}
    ],
    "places": [
      {"name": "Paris, France (1942 — German occupation; existentialist literary circle; publication context)", "role": "The Myth of Sisyphus was written and published in German-occupied Paris — the existential context of occupation gave philosophical urgency to Camus's argument that life must be affirmed in full consciousness of its meaninglessness"},
      {"name": "Algeria (Camus's formation — Mediterranean sensibility; sun and sea; absurd gap between beauty and suffering)", "role": "Camus's Algerian background — the Mediterranean sensibility of sun, physical pleasure, and the sharp awareness of mortality — gave The Myth of Sisyphus its distinctive concrete imagery and its non-academic, embodied approach to philosophical questions"}
    ],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Myth of Sisyphus (Camus, 1942) is one of the most influential philosophical texts of the 20th century — it established Absurdism as a major intellectual movement, gave the postwar world its most resonant philosophical vocabulary for confronting meaninglessness, and produced the most quoted philosophical sentence of the modern era: 'one must imagine Sisyphus happy.'",
      "significanceCategory": "continental"
    },
    "quote": "'One must imagine Sisyphus happy.' — Albert Camus, The Myth of Sisyphus (1942)"
  }
},

"a-brief-history-of-time": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781a-brief-history-of-time.json",
  "slug": "a-brief-history-of-time",
  "data": {
    "era": "Contemporary",
    "eraSlug": "contemporary",
    "eraDivision": "Contemporary",
    "eraDivisionCode": "960",
    "period": "1988",
    "continent": "Global",
    "region": "Global",
    "subjectHeadings": ["Artifacts & Texts -- Popular Science & Cosmology -- United Kingdom -- Contemporary"],
    "subjects": ["Cosmology", "Physics", "Stephen Hawking", "Popular Science", "20th Century", "Black Holes", "Big Bang", "British Science"],
    "frameworks": ["INTELLECTUAL_HISTORY", "CAUSE_AND_EFFECT"],
    "summary": "A Brief History of Time: From the Big Bang to Black Holes (1988) is a landmark popular science book by Stephen Hawking (1942–2018), theoretical physicist at the University of Cambridge, that became one of the bestselling popular science books in history. Published on 1 April 1988 by Bantam Books, it remained on the British Sunday Times bestsellers list for a record 237 weeks — over four and a half years — and has sold approximately 25 million copies worldwide in more than 40 languages. Hawking aimed to write a book about the cosmos accessible to non-specialist readers, famously noting that each equation included would halve the book's sales; the book contains only one equation (E = mc²).\n\nThe book covers the great questions of cosmology — the origin and nature of the universe, the nature of time, the physics of black holes, the expansion of the universe, the possibility of time travel, and the prospect of a unified 'theory of everything' reconciling general relativity and quantum mechanics. It explains Hawking's own contributions to physics, particularly Hawking radiation (1974) — the theoretical prediction that black holes emit thermal radiation due to quantum effects near the event horizon, implying that black holes evaporate over time — and the no-boundary proposal (developed with James Hartle, 1983) suggesting that the universe has no boundary in imaginary time and therefore no moment of creation requiring a 'first cause.' Hawking's discussion of whether a unified theory of physics would allow us to 'know the mind of God' gave the book a philosophical and spiritual dimension that widened its appeal beyond science.\n\nA Brief History of Time transformed the popular perception of theoretical physics — it demonstrated that cutting-edge cosmological ideas could reach a mass audience of tens of millions, and established popular science as a serious literary and commercial genre. Its success inspired a generation of physicists, science writers, and science communicators, and helped create the culture of popular science (books, lectures, documentaries) that has been one of the notable features of late 20th and early 21st-century public culture. Hawking's personal story — producing the book while severely physically disabled by motor neurone disease (ALS) and communicating through a speech synthesiser — gave the book additional cultural resonance as an emblem of intellectual triumph over physical limitation.",
    "causes": [
      "The rapid development of theoretical cosmology and particle physics in the 1970s and 1980s — Hawking's own work on black hole radiation (1974) and the Hartle-Hawking no-boundary proposal (1983), together with the experimental confirmation of the Big Bang theory through cosmic microwave background radiation — created a body of new cosmological knowledge urgently in need of popular explanation.",
      "The success of earlier popular science books — particularly Carl Sagan's Cosmos (1980) and its companion television series — demonstrated that there was a large audience for accessible accounts of the universe; Hawking's agent Peter Guzzardi pressed him to make the draft of A Brief History of Time accessible to a general reader, and the book's success exceeded all predictions.",
      "Hawking's personal circumstances — his severe physical disability (motor neurone disease, ALS) which had by 1988 reduced him to communicating through a computer voice synthesiser — gave his voice a distinctive quality and his project an additional human dimension that made the book culturally resonant beyond the scientific content itself."
    ],
    "effects": [
      "A Brief History of Time established popular science as a major publishing genre — its extraordinary commercial success (25 million copies, 237 weeks on the bestseller list) demonstrated that books about physics, cosmology, and mathematics could compete with fiction bestsellers, and directly inspired the wave of popular science publishing that followed: Penrose's The Emperor's New Mind (1989), Gleick's Chaos (1988), Pinker's The Language Instinct (1994), and dozens of others.",
      "Hawking became the most recognisable scientist in the world — his wheelchair, his voice synthesiser, and A Brief History of Time made him a global celebrity who embodied the triumph of intellect over physical limitation, and his subsequent popular books (Black Holes and Baby Universes, 1993; The Universe in a Nutshell, 2001) extended his influence; he became a cultural icon appearing in The Simpsons, Star Trek, and Pink Floyd's music.",
      "The book's philosophical conclusion — that a unified theory of physics would allow us to 'know the mind of God' — sparked sustained public debate about the relationship between physics and religion, contributing to the late 20th-century surge of popular interest in science-and-religion dialogue that produced books by Dawkins, Collins, Polkinghorne, and others; the quote is one of the most discussed scientific-theological propositions of the modern era."
    ],
    "relationships": [
      {"sourceSlug": "stephen-hawking", "sourceName": "Stephen Hawking (1942–2018 — Cambridge; Hawking radiation; motor neurone disease)", "verb": "AUTHORS", "targetSlug": "a-brief-history-of-time", "targetName": "A Brief History of Time (1988 — 25 million copies; cosmology; 'know the mind of God')", "context": "Hawking wrote A Brief History of Time while severely disabled by ALS — his personal story, his scientific genius, and his accessible prose made the book the most successful popular science book of the 20th century."},
      {"sourceSlug": "a-brief-history-of-time", "sourceName": "A Brief History of Time (popular science revolution — 25M copies; physics accessible to millions)", "verb": "TRANSFORMS", "targetSlug": "popular-science-publishing", "targetName": "Popular Science Publishing (late 20th c — Cosmos; Chaos; Selfish Gene; science for mass audiences)", "context": "A Brief History of Time's extraordinary success transformed popular science publishing — demonstrating that physics and cosmology could outsell fiction and inspiring a generation of popular science authors and communicators."},
      {"sourceSlug": "a-brief-history-of-time", "sourceName": "A Brief History of Time (Hawking radiation — black holes; event horizons; quantum gravity)", "verb": "EXPLAINS", "targetSlug": "hawking-radiation", "targetName": "Hawking Radiation (1974 — black hole evaporation; quantum effects; thermodynamics of black holes)", "context": "A Brief History of Time was the primary vehicle through which Hawking's theoretical discovery of Hawking radiation — the prediction that black holes emit thermal radiation and eventually evaporate — reached a mass audience of tens of millions."}
    ],
    "places": [
      {"name": "Cambridge, UK (Hawking's base — Lucasian Professor of Mathematics; Cambridge cosmology group)", "role": "Cambridge University was Hawking's institutional home — he held the Lucasian Professorship of Mathematics (previously held by Newton) and the Cambridge theoretical physics group was the intellectual context in which A Brief History of Time was conceived"},
      {"name": "Global (25 million copies — 40+ languages; mass audience; science communication revolution)", "role": "A Brief History of Time reached a global audience of tens of millions — translated into 40+ languages and selling 25 million copies, it made Hawking the world's most famous living scientist and sparked a global popular science publishing boom"}
    ],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "A Brief History of Time (Hawking, 1988) sold 25 million copies in 40+ languages — the most successful popular science book ever — and transformed physics from an arcane discipline into mass popular culture. It created the template for popular science publishing, made Hawking a global icon, and sparked lasting public debate about cosmology, time, and 'the mind of God.'",
      "significanceCategory": "continental"
    },
    "quote": "'If we discover a complete theory, it would be the ultimate triumph of human reason — for then we should know the mind of God.' — Stephen Hawking, A Brief History of Time (1988)"
  }
},

"primary-chronicle": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781primary-chronicle.json",
  "slug": "primary-chronicle",
  "data": {
    "era": "Medieval",
    "eraSlug": "medieval",
    "eraDivision": "Medieval",
    "eraDivisionCode": "930",
    "period": "c. 1110–1118 CE",
    "continent": "Europe",
    "region": "Eastern Europe",
    "subjectHeadings": ["Artifacts & Texts -- Chronicles & History -- Kievan Rus' -- Medieval"],
    "subjects": ["Kievan Rus'", "Medieval Russia", "Medieval Ukraine", "Orthodox Christianity", "Eastern European History", "Historical Chronicles", "Rurikid Dynasty", "Slavic History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "RELIGIOUS_FRAMEWORKS"],
    "summary": "The Primary Chronicle (Russian: Повесть временных лет, Povest' vremennykh let — 'The Tale of Bygone Years') is a medieval chronicle compiled c. 1110–1118 CE, traditionally attributed to the monk Nestor of the Kyiv-Pechersk Lavra (Monastery of the Caves). It is the foundational historical text of Kievan Rus' and the primary source for the early history of the Eastern Slavic peoples — covering the period from the Biblical Flood and the dispersion of Noah's sons, through the legendary origins of the Slavic peoples, to the early 12th century CE. The chronicle is preserved in several manuscript recensions, the most important being the Laurentian Codex (1377) and the Hypatian Codex (c. 1425), both of which contain the text with later additions by subsequent compilers.\n\nThe Primary Chronicle is a compilation drawing on Byzantine chronicles (Georgios Hamartolos, George Synkellos), oral tradition, legal documents (including the treaties between Rus' and Byzantium), and hagiographic literature. Its most celebrated episodes include: the calling of the Varangians — the story of the invitation to Rurik and his brothers in 862 CE, which became the founding legend of the Rurikid dynasty; the conversion of Princess Olga of Rus' to Christianity in Constantinople; the vivid account of Prince Vladimir I's investigation of the world's religions and his choice of Orthodox Christianity — with the famous remark by his emissaries from Constantinople that in the great church of Hagia Sophia 'we knew not whether we were in heaven or on earth' — and the Baptism of Rus' in 988 CE.\n\nThe Primary Chronicle exercised a determining influence on the historical consciousness of all three Eastern Slavic peoples — Russians, Ukrainians, and Belarusians — all of whom trace their political and cultural origins to Kievan Rus' and draw on the chronicle as their foundational historical text. Its account of the Baptism of Rus' legitimised the Russian Orthodox Church's claim to Apostolic continuity from Byzantium and shaped the identification of Russia with Orthodox Christian civilisation for over a millennium. The chronicle's account of Rurikid origins was used to legitimate dynastic claims for centuries and remains a foundational document in ongoing historical and political disputes about the relationship between Russia, Ukraine, and Belarus — including contemporary debates about the ownership of the Kievan Rus' heritage.",
    "causes": [
      "The Christianisation of Rus' (988 CE) under Prince Vladimir I — the conversion of Kievan Rus' to Orthodox Christianity brought Byzantine scholarly and literary culture to Rus', including the genre of the chronicle and the Byzantine world-historical framework (from Creation to the present), which provided both the model and the institutional infrastructure for the Primary Chronicle's compilation.",
      "The political fragmentation of Kievan Rus' in the late 11th and early 12th centuries — the bitter succession conflicts among Vladimir I's descendants that threatened to destroy the Rurikid state created both the urgency and the audience for a comprehensive historical account that traced the origins of the Rurikid dynasty and the unity of the Rus' peoples.",
      "The intellectual and spiritual culture of the Kyiv-Pechersk Lavra (Monastery of the Caves) — founded by Antony and Theodosius of the Caves in the 11th century, the Lavra became the intellectual centre of Rus' and the institutional home of chronicle-writing; the tradition of scholarly monks engaged in the compilation and interpretation of history created the conditions for the Primary Chronicle's production."
    ],
    "effects": [
      "The Primary Chronicle established the founding mythology of Eastern Slavic political identity — its account of the calling of the Varangians (the 'Norman theory' of the origins of the Rus' state), the Baptism of Rus', and the genealogy of the Rurikid dynasty became the canonical narrative of Russian, Ukrainian, and Belarusian historical origins, shaping national identities that persist to the present day.",
      "The Primary Chronicle's account of the Baptism of Rus' became the cornerstone of Russian Orthodox identity — the claim that Rus' received Christianity directly from Byzantium (the 'Third Rome' theory, developed in the 15th century, drew on this inheritance) shaped Russia's self-understanding as the heir to Byzantine Christian civilisation and the protector of Orthodox Christianity for over a millennium.",
      "The chronicle established the model of the Russian historical chronicle (летопись, letopis') as a literary and historical genre — the Primary Chronicle was the model for all subsequent Russian, Ukrainian, and Belarusian chronicles (the Novgorod Chronicle, the Galician-Volhynian Chronicle, etc.) and for the entire tradition of Russian historical writing that culminated in Karamzin's History of the Russian State (1818–1829)."
    ],
    "relationships": [
      {"sourceSlug": "nestor-the-chronicler", "sourceName": "Nestor the Chronicler (d. c. 1114 — monk of Kyiv-Pechersk Lavra; hagiographer; Primary Chronicle)", "verb": "AUTHORS", "targetSlug": "primary-chronicle", "targetName": "Primary Chronicle (c. 1110–1118 — founding of Rus'; Baptism 988 CE; Rurikid origins)", "context": "Nestor compiled the Primary Chronicle at the Kyiv-Pechersk Lavra — drawing on Byzantine chronicles, oral tradition, and legal documents to create the foundational historical text of Kievan Rus'."},
      {"sourceSlug": "primary-chronicle", "sourceName": "Primary Chronicle (Baptism of Rus' 988 CE — Hagia Sophia vision; Orthodox Christianity; Byzantine inheritance)", "verb": "LEGITIMISES", "targetSlug": "russian-orthodox-church", "targetName": "Russian Orthodox Church (988 CE founded — Third Rome; Byzantine inheritance; Patriarchate)", "context": "The Primary Chronicle's account of the Baptism of Rus' — especially the emissaries' vision in Hagia Sophia — became the founding narrative of Russian Orthodox identity and the basis for the Church's claim to Byzantine apostolic continuity."},
      {"sourceSlug": "primary-chronicle", "sourceName": "Primary Chronicle (Varangian calling — Rurik 862 CE; Rurikid dynasty; Norman theory of Rus' origins)", "verb": "SHAPES", "targetSlug": "rurikid-dynasty", "targetName": "Rurikid Dynasty (862–1598 CE — founding of Rus'; Kiev; Moscow; legitimising mythology)", "context": "The Primary Chronicle's account of the calling of Rurik in 862 CE became the canonical founding myth of the Rurikid dynasty — used to legitimise dynastic claims for centuries and debated by historians of Russia, Ukraine, and Belarus to the present day."}
    ],
    "places": [
      {"name": "Kyiv (Kievan Rus' — Kyiv-Pechersk Lavra; Baptism of Rus' 988 CE; Rurikid capital)", "role": "Kyiv was the capital of Kievan Rus' and the site of the Kyiv-Pechersk Lavra where the Primary Chronicle was compiled — the chronicle's central narrative concerns the history of Kyiv and the Rurikid dynasty"},
      {"name": "Constantinople (Hagia Sophia — Byzantine Christianity; Olga's conversion; emissaries' vision)", "role": "Constantinople and Hagia Sophia are central to the Primary Chronicle's account of the Christianisation of Rus' — the emissaries' report that they 'knew not whether we were in heaven or on earth' in the great church became the canonical narrative of Russia's adoption of Orthodox Christianity"}
    ],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Primary Chronicle (c. 1110–1118) is the founding historical text of Eastern Slavic civilisation — it established the canonical narratives of the Rurikid dynasty's origins, the Baptism of Rus' (988 CE), and the Byzantine inheritance of Russian Orthodox Christianity that shaped Russia, Ukraine, and Belarus for over a millennium. Its account of the emissaries in Hagia Sophia — 'we knew not whether we were in heaven or on earth' — is perhaps the most consequential diplomatic tourism report in world history.",
      "significanceCategory": "world-changing"
    },
    "quote": "'We knew not whether we were in heaven or on earth — for on earth there is no such splendour or such beauty.' — emissaries of Vladimir I at Hagia Sophia, Primary Chronicle (988 CE episode)"
  }
},

"kojiki": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781kojiki.json",
  "slug": "kojiki",
  "data": {
    "era": "Medieval",
    "eraSlug": "medieval",
    "eraDivision": "Medieval",
    "eraDivisionCode": "930",
    "period": "712 CE",
    "continent": "Asia",
    "region": "East Asia",
    "subjectHeadings": ["Artifacts & Texts -- Mythology & Sacred Texts -- Japan -- Medieval"],
    "subjects": ["Japanese History", "Japanese Mythology", "Shinto", "Imperial Japan", "East Asian History", "Ancient Japan", "Sacred Texts", "Medieval Japan"],
    "frameworks": ["RELIGIOUS_FRAMEWORKS", "STRUCTURAL_ANALYSIS"],
    "summary": "The Kojiki (古事記, 'Record of Ancient Matters') is the oldest extant chronicle of Japan, compiled in 712 CE under the imperial patronage of Empress Genmei (661–721) by Ō no Yasumaro (d. 723), who transcribed oral traditions recited by the imperial court memorist Hieda no Are. The Kojiki records the mythological origins of Japan — the creation of the Japanese islands by the gods Izanagi and Izanami; the birth of the sun goddess Amaterasu, the moon god Tsukuyomi, and the storm god Susanoo; Amaterasu's withdrawal into the Rock Cave of Heaven (Ama-no-Iwato) and subsequent emergence; the descent of Ninigi-no-Mikoto (Amaterasu's grandson) to the islands of Japan; and the founding of the imperial dynasty, traced through a line of legendary emperors to the historical Empress Suiko (r. 593–628). The text is written in classical Chinese with Japanese phonetic elements (man'yōgana).\n\nThe Kojiki is the primary mythological source of Shinto — Japan's indigenous religious tradition — and provides the narrative foundation for the veneration of kami (spirits/deities), the rituals of Shinto shrines, and the religious identity of the Japanese imperial family. Together with the Nihon Shoki (720 CE, compiled eight years later), it established the genealogy of the imperial family as direct descendants of the sun goddess Amaterasu, providing the theological legitimacy for the Japanese imperial institution — which continues in unbroken succession to the present day as the world's oldest reigning monarchy. The text's mythology — particularly the Amaterasu-Susanoo conflict, the Rock Cave episode, and Ninigi's descent — is fundamental to Japanese religious iconography, literature, theatre, and art across fourteen centuries.\n\nThe Kojiki exercised a pervasive and enduring influence on Japanese culture — its narratives were foundational for the noh drama, for classical Japanese poetry (the Man'yōshū draws on its themes), for the architectural tradition of Shinto shrines, and for the political ideology of the imperial state throughout Japanese history. The kokugaku (National Learning) scholars of the 18th century — particularly Motoori Norinaga, who produced the first complete scholarly commentary (Kojikiden, 44 volumes, 1798) — used the text to articulate a Japanese national identity independent of Chinese cultural influence. The text's mythology was mobilised in Meiji state ideology (1868–1912) and the ultra-nationalist period (1930s–1945) as the basis for the ideology of imperial divinity (kokutai) — formally renounced by Emperor Hirohito in his 1946 'Humanity Declaration.'",
    "causes": [
      "Empress Genmei's political need for a comprehensive official history — the late 7th and early 8th centuries were a period of centralisation of the Japanese state (the Taika Reform 645 CE, the Taiho Code 702 CE), and the compilation of the Kojiki was part of the imperial project of establishing the ideological and mythological foundations of the new centralised state, asserting the divine ancestry of the imperial family and the unity of the Japanese people.",
      "The threat of the loss of oral tradition — Hieda no Are, the memorist who recited the traditions recorded in the Kojiki, was said to have exceptional powers of memory, but the traditions were at risk of being lost or corrupted; Empress Genmei's commission of Ō no Yasumaro to record the traditions was a conscious preservation effort, though it was also a political act of selecting and fixing particular versions of the mythology.",
      "Chinese cultural influence and the need for a Japanese response — the adoption of Chinese writing, Buddhism, and Confucian statecraft by the Japanese court from the 6th century onward created both the technical means (literacy, bureaucratic historiography) and the cultural pressure for a distinctly Japanese mythological record; the Kojiki was in part a response to the challenge of maintaining Japanese cultural identity within a Sinicised context."
    ],
    "effects": [
      "The Kojiki established the mythological foundation of the Shinto religious tradition and the theological legitimacy of the Japanese imperial institution — its account of the imperial family's divine descent from Amaterasu has been the basis of imperial ideology for over 1,300 years, surviving through radical changes in Japan's political structure including the Meiji Restoration (1868) and the postwar constitutional monarchy.",
      "The Kojiki's mythology shaped all major forms of Japanese cultural expression — the noh drama, the kabuki theatre, Japanese painting (Yamato-e), classical poetry, and the architecture and ritual of Shinto shrines; its narrative episodes (Susanoo's slaying of the Yamata no Orochi, Amaterasu's Rock Cave, Izanagi's descent to Yomi) are among the most persistent themes in Japanese art and literature across fourteen centuries.",
      "The 18th-century kokugaku movement — inspired by Motoori Norinaga's monumental Kojikiden commentary — used the Kojiki to articulate a Japanese national identity rooted in Shinto and the imperial tradition that was explicitly anti-Chinese and anti-Buddhist; this movement shaped Japanese Romanticism, Japanese nationalism, the Meiji Restoration, and ultimately the ultra-nationalism of the 20th century — making the Kojiki one of the most politically consequential texts in Japanese history."
    ],
    "relationships": [
      {"sourceSlug": "ono-yasumaro", "sourceName": "Ō no Yasumaro (d. 723 — Japanese court noble; compiled Kojiki from Hieda no Are's recitation)", "verb": "COMPILES", "targetSlug": "kojiki", "targetName": "Kojiki (712 CE — Amaterasu; Susanoo; divine imperial ancestry; foundation of Shinto)", "context": "Ō no Yasumaro compiled the Kojiki on the orders of Empress Genmei — transcribing and organising the oral traditions recited by Hieda no Are to create Japan's oldest official mythological and historical chronicle."},
      {"sourceSlug": "kojiki", "sourceName": "Kojiki (divine imperial descent — Amaterasu; kokutai; imperial theology; Meiji state ideology)", "verb": "LEGITIMISES", "targetSlug": "japanese-imperial-family", "targetName": "Japanese Imperial Family (660 BCE–present — world's oldest monarchy; Amaterasu descent; divine lineage)", "context": "The Kojiki's account of the imperial family's descent from Amaterasu provided the theological foundation for Japanese imperial legitimacy for over 1,300 years — and was formally renounced only in Hirohito's 1946 'Humanity Declaration.'"},
      {"sourceSlug": "kojiki", "sourceName": "Kojiki (Motoori Norinaga — Kojikiden 1798; kokugaku; Japanese national identity; Shinto revival)", "verb": "INSPIRES", "targetSlug": "motoori-norinaga", "targetName": "Motoori Norinaga (1730–1801 — Kojikiden; kokugaku; Japanese national spirit; mono no aware)", "context": "Motoori Norinaga's 44-volume Kojikiden commentary (1798) used the Kojiki to articulate a Japanese cultural identity independent of Chinese influence — launching the kokugaku movement that shaped Japanese nationalism and the Meiji Restoration."}
    ],
    "places": [
      {"name": "Nara, Japan (710 CE capital — Empress Genmei; Nara period; centralised Japanese state)", "role": "The Kojiki was compiled in Nara (then the capital of Japan) under Empress Genmei — the Nara period (710–794 CE) was the height of early Japanese state-building and cultural consolidation, of which the Kojiki was a key ideological product"},
      {"name": "Japan (Shinto shrines — Ise Jingu; Izumo; imperial ritual; 14 centuries of cultural influence)", "role": "The Kojiki's mythology permeates the entire landscape of Japanese sacred geography — the great Shinto shrines of Ise (dedicated to Amaterasu) and Izumo (associated with Susanoo) are the institutional embodiments of the Kojiki's cosmology"}
    ],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Kojiki (712 CE) is the foundational sacred text of Japanese civilisation — it established the mythological basis of Shinto, the theological legitimacy of the Japanese imperial institution (the world's oldest reigning monarchy), and the cultural identity of the Japanese people across fourteen centuries. Its mythology permeates Japanese art, literature, religion, and politics from the Nara period to the present day.",
      "significanceCategory": "world-changing"
    },
    "quote": "'Therefore, I, Yasumaro, with reverence and awe, have compiled and edited the old words, carefully selecting, and have respectfully presented them.' — Ō no Yasumaro, Preface to the Kojiki (712 CE)"
  }
},

"the-tale-of-kieu": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782the-tale-of-kieu.json",
  "slug": "the-tale-of-kieu",
  "data": {
    "era": "Early Modern",
    "eraSlug": "early-modern",
    "eraDivision": "Early Modern",
    "eraDivisionCode": "940",
    "period": "c. 1813–1820",
    "continent": "Asia",
    "region": "Southeast Asia",
    "subjectHeadings": ["Artifacts & Texts -- National Epics & Poetry -- Vietnam -- Early Modern"],
    "subjects": ["Vietnamese Literature", "Vietnamese History", "Southeast Asian History", "National Epic", "19th Century", "Confucian Ethics", "Early Modern Asia", "Poetry"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "RELIGIOUS_FRAMEWORKS"],
    "summary": "The Tale of Kieu (Vietnamese: Truyện Kiều; full title Đoạn trường tân thanh, 'New Cries from a Broken Heart') is a narrative poem in 3,254 lines of lục bát (six-eight syllable verse) by the Vietnamese poet and mandarin Nguyễn Du (1765–1820), written c. 1813–1820 and generally regarded as the masterpiece of Vietnamese literature and the Vietnamese national epic. The poem adapts a Chinese novel (Kim Vân Kiều truyện, attributed to Thanh Tâm Tài Nhân, c. 17th century) into a Vietnamese poem of extraordinary lyrical beauty, following the fifteen-year odyssey of Vương Thúy Kiều — a talented, virtuous young woman from a Confucian family — who is sold into prostitution to save her father from prison and endures repeated betrayals, enslavements, and misfortunes before being reunited with her family and her faithful lover Kim Trọng at the poem's conclusion.\n\nThe poem is celebrated for the consummate beauty of its lục bát verse — a distinctly Vietnamese poetic form alternating six and eight syllable lines — and for Nguyễn Du's mastery of both Vietnamese and Chinese literary allusion. The poem engages with the great moral and philosophical questions of Confucian thought — loyalty (trung), filial piety (hiếu), the conflict between love and duty, the role of fate (số phận) and heavenly justice (thiên lý) — while also reflecting on the political turbulence of late 18th-century Vietnam (the Tây Sơn rebellion, the fall of the Lê dynasty, and the rise of the Nguyễn dynasty). Kiều's extraordinary talent in poetry, music, and chess marks her as the ideal of the Vietnamese cultivated woman, while her suffering makes her the archetypal figure of Vietnamese feminine resilience.\n\nThe Tale of Kieu has shaped Vietnamese culture for two centuries — it is the most quoted text in Vietnamese literature, the source of hundreds of proverbs and idioms, and a model for Vietnamese poetry. Its protagonist Kiều is so identified with the Vietnamese people's collective experience of suffering, resilience, and the tension between talent and fate that the poem has been called a national allegory: Vietnamese across political divides have cited Kiều's story to make sense of their historical experience. Ho Chi Minh quoted Kieu to rally resistance fighters; Ngô Đình Diệm quoted Kieu to justify his government; Vietnamese refugees cited Kieu to process their displacement. The poem survived French colonialism, the Vietnam War, and the division of Vietnam as the primary marker of Vietnamese cultural continuity.",
    "causes": [
      "The political turbulence of late 18th-century Vietnam — Nguyễn Du lived through the Tây Sơn rebellion (1771–1802), the fall of the Lê dynasty, and the establishment of the Nguyễn dynasty under Gia Long (1802), serving as a mandarin in a government he had conflicting loyalties toward; this experience of historical upheaval and personal moral compromise gave the poem its distinctive melancholy and its meditation on fate, loyalty, and the gap between virtue and outcome.",
      "The Chinese literary tradition — particularly the 17th-century Chinese novel Jin Yun Qiao zhuan and the broader tradition of Tang poetry, Confucian ethics, and Chinese romantic narrative — gave Nguyễn Du his narrative source material and his literary models; his extraordinary achievement was to transform a Chinese prose romance into a distinctly Vietnamese poetic masterpiece, using the lục bát metre to give the story a Vietnamese emotional register.",
      "The Vietnamese lục bát tradition — the alternating six-eight syllable verse form of Vietnamese oral and written poetry — provided Nguyễn Du with a poetic form perfectly suited to expressing the Vietnamese emotional palette: the alternating rhythm enacts the tension between aspiration and resignation, joy and sorrow, that is the poem's emotional core."
    ],
    "effects": [
      "The Tale of Kieu established Vietnamese as a fully mature literary language capable of the highest poetic expression — its 3,254 lines demonstrated that Vietnamese (viết chữ Nôm, the native Vietnamese script) could achieve the literary density and emotional depth of Chinese literary language, contributing to the prestige of Vietnamese as a literary medium and to the subsequent development of Vietnamese national literature.",
      "Kiều became the archetypal figure of Vietnamese cultural identity — her story of talent, suffering, resilience, and eventual redemption was adopted as a national allegory by Vietnamese of all political persuasions, used to make sense of Vietnam's historical experience of foreign domination, colonialism, war, and division; the poem's famous line 'A hundred years — in this life span on earth, / talent and destiny are apt to feud' became the most quoted expression of the Vietnamese historical condition.",
      "The Tale of Kieu's survival through French colonialism (1858–1954), the Vietnam War (1955–1975), and the postwar unification of Vietnam made it the primary vehicle of Vietnamese cultural continuity — the one text that could be cited by communist and anticommunist, north and south, exile and resident, as a shared cultural possession; it remains the most cited text in contemporary Vietnamese political and literary discourse."
    ],
    "relationships": [
      {"sourceSlug": "nguyen-du", "sourceName": "Nguyễn Du (1765–1820 — Vietnamese poet; mandarin; Lê–Nguyễn transition; 'the Poet of Vietnam')", "verb": "AUTHORS", "targetSlug": "the-tale-of-kieu", "targetName": "The Tale of Kieu (c. 1813–1820 — 3,254 lục bát lines; Kiều; Vietnamese national epic)", "context": "Nguyễn Du wrote The Tale of Kieu during his service as a mandarin under the Nguyễn dynasty — drawing on a Chinese source but transforming it into the supreme masterpiece of Vietnamese literature and the Vietnamese national epic."},
      {"sourceSlug": "the-tale-of-kieu", "sourceName": "The Tale of Kieu (Vietnamese national identity — cultural continuity; colonial survival; diaspora touchstone)", "verb": "DEFINES", "targetSlug": "vietnamese-cultural-identity", "targetName": "Vietnamese Cultural Identity (Confucian ethics; resilience; talent and fate; North-South unity)", "context": "The Tale of Kieu became the defining text of Vietnamese cultural identity across two centuries — cited by Ho Chi Minh, Ngô Đình Diệm, and Vietnamese diaspora alike as the shared cultural possession that transcended political division."},
      {"sourceSlug": "the-tale-of-kieu", "sourceName": "The Tale of Kieu (lục bát mastery — six-eight verse; Vietnamese poetic tradition; literary language prestige)", "verb": "ESTABLISHES", "targetSlug": "vietnamese-luc-bat-tradition", "targetName": "Vietnamese Lục Bát Tradition (6-8 syllable verse — folk song; national poetry; lyrical form)", "context": "The Tale of Kieu elevated the lục bát (six-eight syllable) verse form to literary prestige — demonstrating that the distinctly Vietnamese folk metre could achieve the highest literary expression and establishing it as the canonical form of Vietnamese narrative poetry."}
    ],
    "places": [
      {"name": "Vietnam (national epic — Hội An, Huế, Hanoi; colonial and war-era cultural continuity)", "role": "The Tale of Kieu is the primary cultural text of Vietnam — cited across all regions and political divisions as the expression of Vietnamese identity, it is the poem every educated Vietnamese knows from memory"},
      {"name": "Hà Tĩnh, Vietnam (Nguyễn Du's birthplace — Tiên Điền village; family literary tradition)", "role": "Nguyễn Du was born in Tiên Điền village, Hà Tĩnh province — a region with a strong literary tradition; his family's cultivation and his personal experience of political turbulence shaped the poem's distinctive combination of Confucian ethics and existential melancholy"}
    ],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Tale of Kieu (Nguyễn Du, c. 1820) is Vietnam's national epic — the single most important text in Vietnamese culture, cited by every Vietnamese political figure from Ho Chi Minh to Ngô Đình Diệm, used to make sense of Vietnam's experience of colonialism, war, and division. Its protagonist Kiều is the archetypal figure of Vietnamese resilience: talented, virtuous, repeatedly victimised, and ultimately surviving.",
      "significanceCategory": "continental"
    },
    "quote": "'A hundred years — in this life span on earth, / talent and destiny are apt to feud.' — Nguyễn Du, The Tale of Kieu (opening lines)"
  }
},

"epic-of-king-gesar": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782epic-of-king-gesar.json",
  "slug": "epic-of-king-gesar",
  "data": {
    "era": "Medieval",
    "eraSlug": "medieval",
    "eraDivision": "Medieval",
    "eraDivisionCode": "930",
    "period": "c. 11th–20th century CE (ongoing)",
    "continent": "Asia",
    "region": "Central Asia",
    "subjectHeadings": ["Artifacts & Texts -- Oral Epics & Mythology -- Tibet & Mongolia -- Medieval"],
    "subjects": ["Tibetan Literature", "Mongolian Literature", "Central Asian History", "Epic Poetry", "Oral Tradition", "Buddhism", "Shamanism", "UNESCO Heritage"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "RELIGIOUS_FRAMEWORKS"],
    "summary": "The Epic of King Gesar (Tibetan: གེ་སར་རྒྱལ་པོ་; Mongolian: Гэсэрийн тууж) is the world's longest living oral epic tradition — with documented versions spanning over 120 volumes in print editions and ongoing oral transmission in Tibetan, Mongolian, Buryat, Ladakhi, Bhutanese, and several other languages. The epic centres on King Gesar of Ling — a legendary warrior-hero and divine king who descends from the celestial realm to combat demons and tyrants threatening humanity — whose story encompasses warfare, romance, shamanic power, Buddhist cosmology, and heroic virtue across hundreds of distinct episodes. The core narrative originated in the Tibetan cultural sphere, probably in the 11th–12th centuries CE, and has been continuously elaborated by oral bards (sngrun-pa or 'Gesar bards') whose extended performances can last days and who traditionally enter trance states to channel new material directly from King Gesar's spirit.\n\nThe Epic of Gesar serves multiple functions across its performance communities — it is a source of heroic values (courage, loyalty, divine mandate), a vehicle for Buddhist and shamanistic religious concepts, a compendium of folk medicine, jurisprudence, and ethnographic knowledge, and a living oral tradition that continues to generate new episodes. The epic has been documented across Tibet, Mongolia, Inner Mongolia (China), Buryatia (Russia), Ladakh, Bhutan, Nepal, and the Mongolian diaspora communities of Central Asia — making it one of the most geographically extensive oral traditions in the world. Gesar is venerated as a religious figure — a protector deity (dharma-pāla) in Tibetan Buddhism, a manifestation of Padmasambhava according to some traditions, and a shamanic spirit in Mongolian tradition.\n\nThe Epic of King Gesar was proclaimed a UNESCO Intangible Cultural Heritage in 2009, recognising its unique status as the world's longest living oral epic. Chinese, Tibetan, and Mongolian governments have made major investments in recording, publishing, and preserving the tradition. Gesar is a national hero for Tibetan, Mongolian, and Buryat peoples — his story embodies values of heroic virtue, divine mandate, and the protection of humanity against evil that resonate across the Buddhist and shamanic cultural sphere of Inner and Central Asia. The ongoing performance tradition — with bards who continue to channel new episodes while in trance — makes the Gesar epic unique among the world's great epic traditions as a living, evolving mythology.",
    "causes": [
      "The synthesis of Tibetan shamanic traditions and Tibetan Buddhism in the 11th–12th centuries — the Epic of Gesar emerged at a period when Tibetan Buddhism was consolidating its hold on Central Asia and absorbing pre-Buddhist shamanic traditions; the hero Gesar embodies this synthesis, combining the divine warrior of shamanic cosmology with the Bodhisattva ideal of Buddhist compassion and the goal of protecting sentient beings.",
      "The historical and political turbulence of the Tibetan and Mongolian cultural sphere — the Mongol Empire's expansion and its adoption of Tibetan Buddhism in the 13th century, the wars between Tibetan principalities, and the ongoing conflicts with the demons (klu, bdud, gshin rje) that the epic narrativises reflect real historical experiences of conflict and displacement that the epic both recorded and gave mythological form.",
      "The oral bardic tradition of Central Asia — the figure of the shamanic bard who receives texts in trance, common to Mongolian, Turkic, and Tibetan traditions (cf. the Manas epic of the Kyrgyz, the Alpamish of the Uzbeks), provided the performance framework that allowed the Gesar epic to grow continuously across centuries; the trance performance format meant the epic could not be 'closed' but remained permanently open to new episodes."
    ],
    "effects": [
      "The Epic of Gesar created a shared heroic mythology across the Tibetan-Mongolian Buddhist cultural sphere — Gesar is a national hero for Tibetan, Mongolian, Buryat, and Kalmyk peoples, providing a common cultural reference across the vast region of Inner Asia that was shaped by Tibetan Buddhism and Mongolian political culture; his story embodies the shared values of divine mandate, heroic virtue, and the protection of community.",
      "The ongoing oral tradition of the Gesar bards — performers who continue to channel new episodes in trance states in the 21st century — represents a unique survival of the oral epic performance tradition in an age of mass literacy; UNESCO's recognition of the tradition in 2009 has stimulated major documentation and preservation efforts across China, Mongolia, and Russia, and the tradition has found new audiences through recorded performances, written editions, and online media.",
      "The Gesar epic's role as a vehicle for Tibetan cultural identity under Chinese sovereignty — since the 1950 incorporation of Tibet into the People's Republic of China, the Epic of Gesar has served as a major marker of Tibetan cultural distinctiveness; the Chinese government has both recognised the epic as national cultural heritage and been cautious about its use as a vehicle for Tibetan nationalist sentiment, making it a contested cultural resource in contemporary Sino-Tibetan relations."
    ],
    "relationships": [
      {"sourceSlug": "gesar-of-ling", "sourceName": "King Gesar of Ling (legendary Tibetan hero — divine warrior; tamer of demons; protector deity)", "verb": "INSPIRES", "targetSlug": "epic-of-king-gesar", "targetName": "Epic of King Gesar (c. 11th c.–ongoing — world's longest epic; 120+ volumes; Tibet, Mongolia, Buryatia)", "context": "The legendary King Gesar is the central figure of the world's longest living oral epic tradition — his story of divine descent, heroic warfare against demons, and protection of humanity has been performed and elaborated by Tibetan, Mongolian, and Buryat bards for nearly a millennium."},
      {"sourceSlug": "epic-of-king-gesar", "sourceName": "Epic of King Gesar (UNESCO 2009 — living oral tradition; bards in trance; ongoing performance)", "verb": "EMBODIES", "targetSlug": "tibetan-cultural-identity", "targetName": "Tibetan Cultural Identity (Buddhist civilisation — dharma protection; Gesar as national hero; distinct from China)", "context": "The Epic of Gesar is the primary vehicle of Tibetan cultural identity — a shared heroic mythology that has served as a marker of Tibetan distinctiveness under Chinese sovereignty since 1950."},
      {"sourceSlug": "epic-of-king-gesar", "sourceName": "Epic of King Gesar (Buddhism + shamanism synthesis — dharma-pāla; Padmasambhava; Mongolian shamanism)", "verb": "SYNTHESISES", "targetSlug": "tibetan-buddhism", "targetName": "Tibetan Buddhism (Vajrayana — Padmasambhava; Dalai Lamas; Inner Asian cultural sphere)", "context": "The Epic of Gesar embodies the synthesis of Tibetan Buddhism and pre-Buddhist shamanic traditions — Gesar is both a dharma-pāla (protector deity) in Tibetan Buddhist cosmology and a shamanic hero in Mongolian tradition, making the epic a vehicle for religious integration across the Inner Asian cultural sphere."}
    ],
    "places": [
      {"name": "Ling (legendary Tibetan kingdom — Gesar's homeland; divine descent; heroic battles)", "role": "The legendary Kingdom of Ling is King Gesar's homeland in the epic — a mythologised version of the historical Tibetan principalities of eastern Tibet (Kham), where the oral tradition is strongest"},
      {"name": "Tibet, Mongolia, Buryatia (living oral tradition — bards; trance performance; UNESCO 2009)", "role": "The Epic of Gesar's performance tradition spans Tibet, Mongolia, Inner Mongolia (China), Buryatia (Russia), Ladakh, and Bhutan — the geographic extent of the Tibetan Buddhist and Mongolian cultural sphere"}
    ],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Epic of King Gesar is the world's longest living oral epic tradition — 120+ volumes, still performed by trance bards in the 21st century across Tibet, Mongolia, and Buryatia. It is the founding heroic mythology of the Tibetan-Mongolian Buddhist cultural sphere and a UNESCO Intangible Cultural Heritage (2009), unique as an oral epic still growing after nearly a millennium of continuous performance.",
      "significanceCategory": "continental"
    },
    "quote": "'When King Gesar descends from heaven / to tame the demons and tyrants, / he carries the mandate of heaven / and the compassion of all Buddhas.' — traditional invocation of the Gesar bards"
  }
},

"the-silmarillion": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782the-silmarillion.json",
  "slug": "the-silmarillion",
  "data": {
    "era": "Contemporary",
    "eraSlug": "contemporary",
    "eraDivision": "Contemporary",
    "eraDivisionCode": "960",
    "period": "1977 (posthumous publication)",
    "continent": "Europe",
    "region": "Western Europe",
    "subjectHeadings": ["Artifacts & Texts -- Mythology & Secondary World -- United Kingdom -- Contemporary"],
    "subjects": ["English Literature", "Fantasy Literature", "J.R.R. Tolkien", "Secondary World Mythology", "20th Century", "British Literature", "Mythology", "Modern Fantasy"],
    "frameworks": ["INTELLECTUAL_HISTORY", "STRUCTURAL_ANALYSIS"],
    "summary": "The Silmarillion is a posthumously published collection of mythopoeic writings by J.R.R. Tolkien (1892–1973), edited by his son Christopher Tolkien and published by George Allen & Unwin on 15 September 1977 — four years after the author's death. The book presents the history of Middle-earth's earliest ages in five interconnected sections: the Ainulindalë (the creation myth — Ilúvatar creates the world through the 'Music of the Ainur'); the Valaquenta (an account of the angelic Valar and Maiar); the Quenta Silmarillion (the vast history of the First Age, centring on three jewels — the Silmarils, created by the Noldorin elf Fëanor — containing the light of the Two Trees of Valinor and stolen by Morgoth, the first Dark Lord); the Akallabêth (the downfall of the island kingdom of Númenor); and Of the Rings of Power and the Third Age (a summary bridging to The Lord of the Rings).\n\nThe Silmarillion reveals The Lord of the Rings as the visible surface of a mythological system of extraordinary depth and internal consistency — a legendarium on which Tolkien worked from approximately 1916 (the 'Book of Lost Tales,' begun in a hospital tent during the Battle of the Somme) to his death in 1973. The book draws explicitly on Norse mythology (the Ainulindalë echoes Völuspá), Finnish mythology (the Kalevala was Tolkien's direct model for tone and structure), Old English epic (Beowulf), Celtic mythology, and Christian theology (the Fall of the Noldor parallels the Fall of Man, and Morgoth is explicitly a Satanic figure). Tolkien regarded the creation of a modern mythology — to supply what he considered England's lack of a native mythological tradition comparable to the Norse or Finnish — as a central project of his literary life.\n\nThe Silmarillion transformed the understanding of Tolkien's achievement and established secondary world-building as the foundational ambition of modern fantasy literature. The creation of fully realised fictional worlds with their own languages, histories, mythologies, and geographies — demonstrated by Middle-earth's extraordinary depth — has been the defining aspiration of fantasy writers from Ursula K. Le Guin and George R.R. Martin to Brandon Sanderson. The book also demonstrated that the 20th century was capable of producing mythology with genuine spiritual depth; its influence on popular culture, accelerated by Peter Jackson's Lord of the Rings films (2001–2003) and Amazon's The Rings of Power series (2022–), continues to expand.",
    "causes": [
      "The Battle of the Somme (July–November 1916) — Tolkien began the mythological writing that became The Silmarillion while recovering from trench fever contracted during the Battle of the Somme, and the catastrophic loss of his closest friends in the battle (two of three members of his Tea Club and Barrovian Society died) gave the themes of the Silmarillion — the fall of great civilisations, the corruption of the good, and the endurance of friendship against darkness — their urgent personal resonance.",
      "Tolkien's scholarly encounter with Old Norse, Old English, and Finnish literature — as a professional philologist at Oxford, Tolkien's deep engagement with the Eddas, Beowulf, and the Kalevala (which he translated) gave him both the literary models and the conviction that a modern English mythology needed to be created; his invention of the Elvish languages (Quenya and Sindarin) preceded and generated the mythology.",
      "Tolkien's Roman Catholic faith — particularly the Augustinian theology of creation, fall, and redemption — provided the theological framework for The Silmarillion: Ilúvatar's creation through music, Morgoth's rebellion (paralleling Satan's fall), the corruption of the Númenóreans (paralleling the Fall of Man), and the ultimate eucatastrophe of redemption are all shaped by Catholic theological categories."
    ],
    "effects": [
      "The Silmarillion established secondary world-building as the central ambition of modern fantasy literature — Tolkien's demonstration that a fictional world could have the mythological depth, linguistic consistency, and historical complexity of a real ancient civilisation set the standard against which all subsequent fantasy world-builders measure themselves; George R.R. Martin, Brandon Sanderson, Ursula K. Le Guin, and dozens of other major fantasy authors have cited Tolkien as the model for what world-building can achieve.",
      "The publication of The Silmarillion sparked an enormous secondary literature of Tolkien scholarship and fan creation — the Tolkien Society (founded 1969) and its Mythlore journal, the scholarly edition of Christopher Tolkien's 12-volume History of Middle-earth (1983–1996), and the vast online community of Tolkien enthusiasts reading the Silmarillion as a mythological primary source demonstrate the book's extraordinary cultural resonance.",
      "The Silmarillion's mythology provided the source material for Amazon's The Rings of Power television series (2022–), for which Amazon paid approximately $250 million for the rights to Tolkien's appendices and supplementary materials — the largest rights acquisition in streaming television history; the series brought the stories of the First and Second Ages of Middle-earth to a global audience of hundreds of millions, demonstrating the commercial viability of the Silmarillion's mythology in the age of streaming."
    ],
    "relationships": [
      {"sourceSlug": "j-r-r-tolkien", "sourceName": "J.R.R. Tolkien (1892–1973 — Oxford philologist; Lord of the Rings; Elvish languages; 57 years on the legendarium)", "verb": "AUTHORS", "targetSlug": "the-silmarillion", "targetName": "The Silmarillion (1977 posthumous — Ainulindalë; First Age; Fëanor; Middle-earth mythology)", "context": "Tolkien worked on the mythology of The Silmarillion from 1916 to his death in 1973 — a lifetime's work published posthumously by his son Christopher, revealing The Lord of the Rings as the surface of a mythological iceberg."},
      {"sourceSlug": "the-silmarillion", "sourceName": "The Silmarillion (secondary world-building — depth of world; linguistic consistency; mythology for England)", "verb": "ESTABLISHES", "targetSlug": "modern-fantasy-literature", "targetName": "Modern Fantasy Literature (Tolkien — Le Guin; Martin; Sanderson; secondary world tradition)", "context": "The Silmarillion established secondary world-building — creating fully realised fictional worlds with their own languages, histories, and mythologies — as the central ambition and distinguishing practice of modern fantasy literature."},
      {"sourceSlug": "kalevala", "sourceName": "Kalevala (Elias Lönnrot 1835/1849 — Finnish national epic; mythological model; lament tradition)", "verb": "MODELS", "targetSlug": "the-silmarillion", "targetName": "The Silmarillion (1977 — Ainulindalë; Elvish lament tradition; Tolkien's 'mythology for England')", "context": "The Kalevala was Tolkien's direct literary model for The Silmarillion — he translated the Finnish epic and was inspired by it to attempt the creation of a comparable mythology for England; the Elvish lament tradition and the melancholy tone of the Silmarillion directly echo the Kalevala's Finnic register."}
    ],
    "places": [
      {"name": "Oxford, UK (Tolkien's base — Pembroke and Merton Colleges; Inklings; 57 years of mythological composition)", "role": "Oxford was Tolkien's professional and creative home — his work as Professor of Anglo-Saxon and then Merton Professor of English Language and Literature at Oxford provided both the scholarly resources and the Inklings writing circle (with C.S. Lewis) that sustained the decades-long composition of The Silmarillion"},
      {"name": "Battle of the Somme, France (1916 — trench fever; death of friends; genesis of the legendarium)", "role": "Tolkien began writing the Book of Lost Tales (the earliest version of The Silmarillion) while recovering from trench fever contracted during the Battle of the Somme — the catastrophic losses of the battle gave the mythology its themes of civilisational fall and friendship against darkness"}
    ],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Silmarillion (Tolkien, 1977) revealed the full depth of Middle-earth's mythology — a 57-year project that established secondary world-building as the defining ambition of modern fantasy literature. Its influence on every major fantasy author since Tolkien, combined with the Amazon Rings of Power series (2022–), makes it arguably the most influential work of mythology produced in the 20th century.",
      "significanceCategory": "continental"
    },
    "quote": "'In the beginning Eru, the One, who in the Elvish tongue is named Ilúvatar, made the Ainur of his thought; and they made a great Music before him.' — The Silmarillion, Ainulindalë (1977)"
  }
},

"history-of-rome": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781history-of-rome.json",
  "slug": "history-of-rome",
  "data": {
    "era": "Classical",
    "eraSlug": "classical",
    "eraDivision": "Classical",
    "eraDivisionCode": "920",
    "period": "c. 27 BCE–17 CE",
    "continent": "Europe",
    "region": "Mediterranean",
    "subjectHeadings": ["Artifacts & Texts -- Historical Chronicles -- Roman Empire -- Classical"],
    "subjects": ["Roman History", "Classical Antiquity", "Ancient Rome", "Livy", "Ab Urbe Condita", "Roman Republic", "Classical Literature", "Mediterranean History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "summary": "Ab Urbe Condita (Latin: 'From the Founding of the City') is a monumental history of Rome from its mythological founding by Romulus and Remus in 753 BCE to the reign of Augustus, composed by the Roman historian Titus Livius — Livy (c. 64 BCE–17 CE) — in 142 books, of which 35 survive complete (Books 1–10 covering 753–293 BCE and Books 21–45 covering 218–167 BCE). Livy worked in Rome under the patronage of Augustus Caesar, who reportedly called him 'a Pompeian' despite his republican sympathies — a remark that testifies to the independence and seriousness of Livy's engagement with the Roman past. His History combines rhetorical skill, patriotic sentiment, moral purpose, and detailed narrative in a prose style that was admired throughout antiquity as a model of Latin eloquence.\n\nAb Urbe Condita is the primary source for many of the most celebrated episodes of early and middle Roman history — the Rape of Lucretia and the founding of the Roman Republic (509 BCE), the Gallic sack of Rome (390 BCE), the Samnite Wars, and above all the Second Punic War (218–202 BCE) — Hannibal's crossing of the Alps, the catastrophic Roman defeat at Cannae (216 BCE) where approximately 70,000 Roman soldiers died in a single afternoon, and the dramatic rise of Scipio Africanus and Rome's ultimate victory. Though Livy's method was more rhetorical than strictly critical — he reproduced and embellished earlier Roman annalists and legendary traditions rather than subjecting sources to rigorous scrutiny — his depictions of Roman heroes (Horatius Cocles at the bridge, Cincinnatus called from his plough, Fabius Maximus the Delayer, Scipio Africanus) became the canonical images of Roman virtue in Western education for two millennia.\n\nLivy's History was the foundational text of Roman history in Western education from the imperial period through the medieval manuscript tradition to the Renaissance humanists who saw Republican Rome as the supreme model of civic virtue. Machiavelli's Discourses on Livy (c. 1517) — his analysis of republican government, civic virtue, and political realism — is the most influential political text of the Renaissance, treating Livy's Rome as a case study in political theory that remains applicable to all times. The French and American Revolutionaries drew on Livy's Roman exempla as political models, and the Roman republican vocabulary that pervades the US founding documents — Senate, Capitol, consul, republic, dictator — is mediated substantially through the Livian tradition. Only 35 of the original 142 books survive; the losses represent some of the most lamented gaps in classical scholarship.",
    "causes": [
      "The Augustan political project — the transformation of the Roman Republic into the Principate under Augustus (27 BCE) created both the political need for a comprehensive historical account that would legitimate the new order by tracing Rome's greatness to its republican foundations, and the patronage network (Maecenas's circle, which included Horace and Virgil) that sustained Livy's decades-long project.",
      "The Roman annalistic tradition — the systematic recording of Roman history by pontifical annals (fasti) and by the annalistic historians of the late Republic (Fabius Pictor, Cato the Elder, Valerius Antias) provided Livy with the source material he compiled and embellished; his History is substantially a rhetorical and moral reworking of existing annalistic material rather than primary research.",
      "Livy's Patavine (Paduan) background and his perception of Roman moral decline — Livy came from Patavium (modern Padua) in Cisalpine Gaul, where Roman traditions of virtue and discipline were regarded as still intact; his History was conceived as a moral mirror holding up the Roman ancestral virtues (mos maiorum) as an example and rebuke to the Rome of his own age."
    ],
    "effects": [
      "Livy's History was the primary vehicle through which the Roman exempla — the canonical stories of Roman virtue, from Horatius at the bridge to Scipio Africanus — were transmitted to Western education from antiquity through the Renaissance; every educated European from the 1st century CE to the 19th century encountered these stories through Livy, making his History arguably the most influential history book ever written in terms of its duration and breadth of cultural influence.",
      "Machiavelli's Discourses on Livy (c. 1517) — the most important political text of the Renaissance — used Livy's Rome as a case study in republican government, civic virtue, and the conditions for political stability and expansion; through Machiavelli, Livy's influence reached the French philosophes, the American Founders, and the entire tradition of civic republicanism that shaped modern democratic theory.",
      "The Republican vocabulary that pervades the US constitutional system — Senate (from the Roman Senatus), Capitol (from the Capitoline Hill), consul (the term used for the executive in several early republican proposals), republic (from res publica), fasces (the symbol of authority on the Speaker's podium) — was transmitted through the humanist tradition that drew on Livy, making Ab Urbe Condita an indirect shaping force on the American constitutional order."
    ],
    "relationships": [
      {"sourceSlug": "livy", "sourceName": "Titus Livius — Livy (c. 64 BCE–17 CE — Roman historian; Patavium; Augustan patronage; 142 books)", "verb": "AUTHORS", "targetSlug": "history-of-rome", "targetName": "Ab Urbe Condita (c. 27 BCE–17 CE — 142 books; Romulus to Augustus; Hannibal; Scipio)", "context": "Livy wrote Ab Urbe Condita over approximately 40 years — his monumental history from Rome's founding to his own time became the foundational text of Roman history in Western education for nearly two millennia."},
      {"sourceSlug": "history-of-rome", "sourceName": "Ab Urbe Condita (Roman exempla — Horatius; Cincinnatus; Scipio; Hannibal; mos maiorum)", "verb": "MODELS", "targetSlug": "discourses-on-livy-machiavelli", "targetName": "Discourses on Livy (Machiavelli, c. 1517 — republican theory; civic virtue; political realism)", "context": "Machiavelli's Discourses on Livy — his most systematic political work — used Livy's Rome as a case study in republican government and political realism, transmitting Livy's Roman exempla to the modern tradition of democratic political theory."},
      {"sourceSlug": "history-of-rome", "sourceName": "Ab Urbe Condita (Roman vocabulary — Senate; Capitol; Republic; fasces; American Founders)", "verb": "SHAPES", "targetSlug": "american-constitutional-system", "targetName": "American Constitutional System (1787 — Senate; Capitol; republican government; Roman model)", "context": "The Roman republican vocabulary of the US Constitution — Senate, Capitol, republic, fasces — was transmitted to the American Founders through the humanist tradition of Cicero, Livy, Plutarch, and Machiavelli; Ab Urbe Condita was a foundational text in this transmission."}
    ],
    "places": [
      {"name": "Rome (Augustan — Forum; Senate; Capitoline; Republican exempla; Hannibal's threat)", "role": "Livy wrote his History in Rome under the patronage of Augustus — his narrative centres on Rome itself as the protagonist: the city that survived Hannibal at Cannae, expelled its kings, conquered the Mediterranean, and whose republican virtues were the model for all subsequent civic cultures"},
      {"name": "Carthage / Africa (Hannibal — Second Punic War 218–202 BCE; Alps crossing; Cannae; Scipio's victory)", "role": "The most dramatic episodes of Livy's surviving books concern the Second Punic War — Hannibal's invasion of Italy, the catastrophic Roman defeat at Cannae, and Scipio Africanus's counter-invasion of Africa; these chapters are the most vivid historical narrative in classical Latin prose"}
    ],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Ab Urbe Condita (Livy, c. 27 BCE) is the primary source for Roman history from the founding to Augustus — 142 books whose surviving 35 shaped Western education, political theory, and republican vocabulary for two millennia. Through Machiavelli's Discourses on Livy and the American Founders' Roman models, Livy's account of Roman republican virtue is an indirect founding document of modern democracy.",
      "significanceCategory": "world-changing"
    },
    "quote": "'This is the most wholesome and beneficial thing about history: you see examples of every kind of behaviour set forth on a clear and illuminated monument, and from that you can take both what to imitate and what to avoid.' — Livy, Preface to Ab Urbe Condita"
  }
},

}  # end ENRICHMENTS


def load_json(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path: str, data: dict):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  ✓ Saved {path}")

def build_edit_log(slug: str, enrichment: dict) -> list:
    entries = []
    ts = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    for field, value in enrichment.items():
        entries.append({
            "field": field,
            "oldValue": None,
            "newValue": value if isinstance(value, str) else json.dumps(value),
            "editedAt": ts,
            "editorId": EDITOR_ID,
            "sessionId": SESSION_ID,
        })
    return entries

def enrich_entity(slug: str, spec: dict, dry_run: bool = False) -> bool:
    filepath = spec['filepath']
    enrichment = spec['data']

    if not os.path.exists(filepath):
        print(f"  ✗ File not found: {filepath}")
        return False

    data = load_json(filepath)
    entities = data.get('entities', [])
    entity = next((e for e in entities if e.get('slug') == slug), None)
    if not entity:
        print(f"  ✗ Entity '{slug}' not found in {filepath}")
        return False

    # Check if already enriched
    current_summary = entity.get('summary', '')
    details_raw = entity.get('detailsJson', '{}')
    details = json.loads(details_raw) if isinstance(details_raw, str) else (details_raw or {})
    existing_summary = details.get('summary', current_summary)
    if existing_summary and len(existing_summary) >= 800:
        print(f"  ↷ SKIP {slug} (already {len(existing_summary)}c)")
        return False

    print(f"  → Enriching {slug}  (was {len(existing_summary)}c → {len(enrichment.get('summary',''))}c)")
    if dry_run:
        return True

    # Extract top-level fields from enrichment
    TOP_LEVEL = {'era', 'eraSlug', 'eraDivision', 'eraDivisionCode', 'period',
                 'continent', 'region', 'subjectHeadings', 'subjects', 'frameworks',
                 'born', 'died', 'founded', 'startDate', 'endDate'}
    top_updates = {k: v for k, v in enrichment.items() if k in TOP_LEVEL}
    detail_updates = {k: v for k, v in enrichment.items() if k not in TOP_LEVEL}

    # Apply top-level updates
    entity.update(top_updates)

    # Apply detailsJson updates
    detail_updates['summary'] = enrichment.get('summary', '')
    details.update(detail_updates)
    entity['detailsJson'] = json.dumps(details, ensure_ascii=False)

    # Mark as needing sync
    entity['_unsyncedEdits'] = True

    # Record edit log
    if '_editLog' not in details:
        details['_editLog'] = []
    details['_editLog'].extend(build_edit_log(slug, enrichment))
    entity['detailsJson'] = json.dumps(details, ensure_ascii=False)

    save_json(filepath, data)
    return True


def main():
    dry_run = '--dry-run' in sys.argv
    if dry_run:
        print("=== DRY RUN — no files will be written ===\n")

    print(f"Batch 57 enrichment — {len(ENRICHMENTS)} entities\n")
    success, skipped, failed = 0, 0, 0

    for slug, spec in ENRICHMENTS.items():
        print(f"[{slug}]")
        result = enrich_entity(slug, spec, dry_run=dry_run)
        if result:
            success += 1
        else:
            # Check if skipped or failed
            filepath = spec['filepath']
            if os.path.exists(filepath):
                data = load_json(filepath)
                e = next((x for x in data.get('entities', []) if x.get('slug') == slug), None)
                if e:
                    raw = e.get('detailsJson', '{}')
                    d = json.loads(raw) if isinstance(raw, str) else (raw or {})
                    s = d.get('summary', e.get('summary', ''))
                    if s and len(s) >= 800:
                        skipped += 1
                    else:
                        failed += 1
                else:
                    failed += 1
            else:
                failed += 1

    print(f"\n{'DRY RUN' if dry_run else 'DONE'}: {success} enriched, {skipped} skipped, {failed} failed")
    if not dry_run and success > 0:
        print(f"\nNext step: env $(cat .env | xargs) npx tsx scripts/sync_gateway.ts --local")


if __name__ == '__main__':
    main()
