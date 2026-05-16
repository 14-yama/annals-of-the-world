#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 47 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: the-tale-of-genji, the-interpretation-of-dreams, the-second-sex,
          waiting-for-godot, the-republic, the-pilgrims-progress,
          the-imitation-of-christ, upanishads
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-47-may2026"

ENRICHMENTS = {

"the-tale-of-genji": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-tale-of-genji.json",
  "slug": "the-tale-of-genji",
  "data": {
    "summary": "The Tale of Genji (Japanese: 源氏物語, Genji Monogatari) is a novel (or extended prose narrative) by the Japanese court lady and diarist Murasaki Shikibu (c. 978 – c. 1014 or 1025 CE), composed in Early Middle Japanese at the Heian court in the early 11th century CE (c. 1000–1010 CE, though composition may have begun as early as 995). Consisting of 54 chapters and approximately 1,000 pages in most modern translations, it is widely regarded as the world's first novel — or, more carefully, the first prose narrative of sufficient length, psychological depth, and structural complexity to be called novelistic in a meaningful sense. It was written for and read aloud to the ladies of the imperial court by Murasaki Shikibu, a lady-in-waiting to Empress Shōshi.\n\nThe Tale of Genji follows the life, loves, and psychological development of Hikaru Genji, the son of the Japanese emperor and a low-ranking consort (the 'Shining Prince'), through his political marginalisation, numerous love affairs, political exile, and eventual return to favour — and, after Genji's death (not narrated directly), the lives of the next generation. The novel's first part (Chapters 1–33) follows Genji from birth through his political maturity; a transitional chapter ('Wakana' — 'New Herbs') depicts Genji's decline; and the final chapters ('The Uji Chapters', 44–54) follow Kaoru and Niou, younger men connected to Genji, in a more melancholy and unresolved manner. The work is distinguished by its extraordinary psychological complexity — the interior lives of its characters, particularly its women characters, are rendered with a sensitivity and depth unprecedented in world literature — and by the Buddhist aesthetics of mono no aware ('the pathos of things', the bittersweet melancholy of impermanence) that pervades the narrative.\n\nThe Tale of Genji has been continuously read, copied, illustrated, adapted, and commented upon in Japan for over a millennium, generating the largest body of commentary and artistic response of any Japanese literary work. It was translated into modern Japanese by Akiko Yosano (1912) and Junichiro Tanizaki (1941), and into English by Arthur Waley (1925–1933), Edward Seidensticker (1976), and Royall Tyler (2001).",
    "causes": [
      "The extraordinary cultural and literary environment of the Heian court (794–1185 CE) — the concentrated, refined court culture at Heiankyō (Kyoto) with its emphasis on aesthetic sensitivity, literary production, and the cultivation of emotional refinement (aware) — provided both the audience and the cultural vocabulary for the Tale of Genji.",
      "The kana syllabary — the phonetic Japanese writing system (hiragana and katakana) developed in the 9th century CE, distinct from the Chinese characters (kanji) used for official and male writing — made possible the development of a vernacular Japanese literary tradition in which women writers were central: Murasaki Shikibu and other Heian women writers composed in kana.",
      "Murasaki Shikibu's specific biographical position — as a lady-in-waiting to Empress Shōshi and a woman of considerable literary education (she apparently had access to Chinese classics and could compose Chinese verse, unusual for women of her era) — gave her both the access to the imperial court world she depicted and the literary resources to render it with psychological depth."
    ],
    "effects": [
      "The Tale of Genji established the psychological novel — prose fiction's capacity to render the interior lives of characters with complexity and depth — as a literary achievement, and was recognised by later critics (most recently, in the context of world literary history) as demonstrating that the novel form can emerge in any literary tradition given the right cultural conditions, not only in 18th-century Europe.",
      "The Tale of Genji generated the largest commentary tradition of any Japanese literary work — from the 12th century to the present, an unbroken series of interpretive and artistic responses (illustrated manuscripts, retellings, noh plays, kabuki adaptations, manga, anime) — making it the central text of Japanese literary culture, comparable in cultural centrality to Shakespeare in English.",
      "Murasaki Shikibu's achievement demonstrated the capacity of women writers to produce works of the highest literary ambition — her example was central to the Japanese tradition of women's literature, and the Tale of Genji's global reception (particularly the Waley translation's impact on Virginia Woolf and the Bloomsbury group) contributed to its recognition as world literature."
    ],
    "relationships": [
      {"sourceSlug": "murasaki-shikibu", "sourceName": "Murasaki Shikibu (c. 978 – c. 1014, Japanese court lady)", "verb": "AUTHORS", "targetSlug": "the-tale-of-genji", "targetName": "The Tale of Genji (Genji Monogatari, c. 1000–1010 CE, 54 chapters)", "context": "Murasaki Shikibu composed the Tale of Genji c. 1000–1010 CE at the Heian court — widely regarded as the world's first novel and the central text of Japanese literary culture."},
      {"sourceSlug": "the-tale-of-genji", "sourceName": "Tale of Genji (mono no aware, Buddhist aesthetics, psychological depth)", "verb": "EXEMPLIFIES", "targetSlug": "heian-court-culture", "targetName": "Heian court culture (794–1185 CE, Japan)", "context": "The Tale of Genji is the supreme expression of Heian court culture — its refined Buddhist aesthetics of mono no aware, its elaborate depiction of court ritual and social hierarchy, and its kana prose style define the Heian literary achievement."},
      {"sourceSlug": "the-tale-of-genji", "sourceName": "Tale of Genji (Waley translation 1925–1933 — Bloomsbury)", "verb": "TRANSMITTED_TO", "targetSlug": "western-modernist-literature", "targetName": "Western Modernist literature (Arthur Waley, Bloomsbury, Virginia Woolf)", "context": "Arthur Waley's English translation (1925–1933) introduced the Tale of Genji to Western readers — Virginia Woolf reviewed it admiringly, and the Bloomsbury group's reception helped establish it as a canonical work of world literature."}
    ],
    "places": [
      {"name": "Heiankyō (Kyoto), Japan — Heian imperial court, 11th century CE", "role": "The Tale of Genji was written at and about the Heian imperial court in Heiankyō (modern Kyoto) — the concentrated court culture of the capital is both the setting and the cultural world of the novel"},
      {"name": "Japan (millennium-long reception: illustrated manuscripts, noh, kabuki, manga, anime)", "role": "The Tale of Genji has been continuously read, illustrated, adapted, and commented upon in Japan for over a millennium — generating the largest body of artistic response of any Japanese literary work"}
    ],
    "subjects": ["Japanese Literature", "Medieval Era", "Murasaki Shikibu", "Heian Period", "Novel", "Women Writers", "Japanese Culture", "Asian Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Tale of Genji (Murasaki Shikibu, c. 1000–1010 CE) is widely regarded as the world's first novel — a 54-chapter prose narrative of extraordinary psychological depth that established the novelistic exploration of interior life as a literary achievement. It is the central text of Japanese literary culture, generating over a millennium of commentary and artistic response. Its recognition as world literature (through Waley's 1925–1933 translation) contributed to the decentring of the European novel's claim to primacy.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-interpretation-of-dreams": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-interpretation-of-dreams.json",
  "slug": "the-interpretation-of-dreams",
  "data": {
    "summary": "The Interpretation of Dreams (German: Die Traumdeutung) is a foundational work of psychoanalysis by the Austrian neurologist Sigmund Freud (1856–1939), published on 4 November 1899 (though Freud dated it 1900, considering it a work of the new century). It is the first systematic exposition of Freud's theory of the unconscious, of repression, and of the method of psychoanalysis — presented through the analysis of a large number of dreams (including many of Freud's own, most notably the 'Dream of Irma's Injection', analysed as the founding specimen of the method). The book argues that dreams are the 'royal road to the unconscious' — that the apparently nonsensical content of dreams is the result of a process (the 'dream-work') by which the latent content (the unconscious wishes and thoughts that generate the dream) is transformed into the manifest content (the remembered dream) through four mechanisms: condensation (Verdichtung), displacement (Verschiebung), considerations of representability (Rücksicht auf Darstellbarkeit), and secondary elaboration (sekundäre Bearbeitung).\n\nThe Interpretation of Dreams is the founding text of psychoanalysis as a theory and as a therapeutic practice — it introduced the fundamental concepts (the unconscious, repression, wish-fulfilment, the dream-work, the Oedipus complex, psychic determinism) that would define Freudian psychoanalysis and shape 20th-century culture. Freud himself considered it his greatest work and described its publication as 'the most daring enterprise I have ever undertaken'. It was initially received coolly by the scientific community (only 351 copies sold in the first six years) but gradually became one of the most influential intellectual works of the 20th century, cited and debated in psychiatry, psychology, literary criticism, philosophy, anthropology, and cultural theory.\n\nThe book's cultural impact extended far beyond psychiatry — the Freudian vocabulary (the unconscious, repression, the id/ego/superego, the Oedipus complex) entered everyday language, and Freud's model of the unconscious as the source of dreams, art, and human motivation shaped literary Modernism (Joyce's Ulysses, Surrealism, Woolf's stream of consciousness), social theory (Marcuse, Adorno), and feminist criticism (Juliet Mitchell, Jacqueline Rose).",
    "causes": [
      "Freud's self-analysis (begun 1897) — the systematic analysis of his own dreams and memories following the death of his father (1896), which Freud described as the most important event in a man's life — provided both the method and the primary material for The Interpretation of Dreams: many of the dreams analysed in the book are Freud's own.",
      "The 19th-century neurological and psychiatric tradition — Freud's training as a neurologist under Ernst Brücke and Jean-Martin Charcot, his collaboration with Josef Breuer on Studies in Hysteria (1895), and his engagement with the pre-Freudian literature on dreams (Schopenhauer, Nietzsche, the dream theorists) — provided the intellectual context from which he developed his theory.",
      "The specific clinical problems of hysteria and neurosis — patients (primarily women) whose symptoms could not be explained organically and appeared to be connected to memories and fantasies — drove Freud toward the hypothesis of an active unconscious that could explain both normal dream content and pathological symptom formation."
    ],
    "effects": [
      "The Interpretation of Dreams established the conceptual foundation of psychoanalysis — the theory of the unconscious, repression, wish-fulfilment, the dream-work, and the Oedipus complex — that shaped psychiatry, psychotherapy, and the social sciences throughout the 20th century and continues to be debated, applied, and contested.",
      "Freud's model of the unconscious and its mechanisms (condensation, displacement, symbolism) became the primary theoretical framework for literary criticism's engagement with the unconscious dimensions of literary texts — from the Surrealists' deliberate cultivation of the unconscious through the psychoanalytic literary criticism of the 20th century (Lacan, Derrida, Žižek).",
      "The Freudian vocabulary ('the unconscious', 'repression', 'the Oedipus complex', 'projection', 'denial', 'displacement') entered the common language — by the mid-20th century, these terms had become part of everyday discourse, demonstrating the extraordinary cultural diffusion of Freud's conceptual framework beyond the technical psychiatric context."
    ],
    "relationships": [
      {"sourceSlug": "sigmund-freud", "sourceName": "Sigmund Freud (1856–1939, neurologist and founder of psychoanalysis)", "verb": "AUTHORS", "targetSlug": "the-interpretation-of-dreams", "targetName": "The Interpretation of Dreams (Die Traumdeutung, published 1899/1900)", "context": "Freud published The Interpretation of Dreams in 1899/1900 — the founding text of psychoanalysis, introducing the theory of the unconscious, repression, and the dream-work."},
      {"sourceSlug": "the-interpretation-of-dreams", "sourceName": "Interpretation of Dreams (unconscious, repression, dream-work)", "verb": "ESTABLISHES", "targetSlug": "psychoanalytic-theory", "targetName": "Psychoanalytic theory and psychoanalysis as a discipline", "context": "The Interpretation of Dreams introduced the core concepts of psychoanalysis — the unconscious, repression, wish-fulfilment, the Oedipus complex — that defined the psychoanalytic movement and shaped 20th-century psychiatry, psychology, and cultural theory."},
      {"sourceSlug": "the-interpretation-of-dreams", "sourceName": "Interpretation of Dreams (unconscious, condensation, displacement — Surrealism)", "verb": "INFLUENCES", "targetSlug": "literary-modernism", "targetName": "Literary Modernism and Surrealism (Joyce, Woolf, Breton, Dalí)", "context": "Freud's theory of the unconscious and dream-mechanisms shaped literary Modernism and Surrealism — André Breton's Surrealist Manifesto (1924) explicitly draws on Freud; Joyce's stream of consciousness and Woolf's narrative technique are informed by Freudian concepts of mind."}
    ],
    "places": [
      {"name": "Vienna (Freud's home and practice — Berggasse 19 — fin-de-siècle context)", "role": "Freud wrote The Interpretation of Dreams in Vienna, where he had his neurological practice at Berggasse 19 — the fin-de-siècle Viennese intellectual environment of the 1890s was the immediate context for his theoretical development"},
      {"name": "Europe and the United States (psychoanalytic movement diffusion — Berlin, London, New York)", "role": "The psychoanalytic movement spread from Vienna through Germany, Britain (Ernest Jones), and the United States (Abraham Brill, G. Stanley Hall) — The Interpretation of Dreams' concepts were diffused through the International Psychoanalytic Association (founded 1910)"}
    ],
    "subjects": ["Psychology", "Modern Era", "Sigmund Freud", "Psychoanalysis", "Unconscious", "Dream Theory", "Austrian Literature", "Science History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Interpretation of Dreams (Freud, 1899/1900) is the founding text of psychoanalysis and one of the most influential intellectual works of the 20th century. Its theory of the unconscious, repression, and the dream-work shaped psychiatry, psychology, literary criticism, social theory, and everyday language — the Freudian vocabulary entered common discourse and its model of the unconscious influenced literary Modernism, Surrealism, and cultural theory across the century.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-second-sex": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-second-sex.json",
  "slug": "the-second-sex",
  "data": {
    "summary": "The Second Sex (French: Le Deuxième Sexe) is a foundational work of feminist philosophy and social theory by the French existentialist philosopher and novelist Simone de Beauvoir (1908–1986), published in two volumes in Paris on 5 June 1949 by Gallimard. The work consists of two parts: Volume I, 'Facts and Myths' (Faits et mythes), which analyses the biological, psychoanalytic, Marxist, and historical constructions of 'woman'; and Volume II, 'Lived Experience' (L'Expérience vécue), which analyses woman's concrete situation — her childhood, adolescence, sexual initiation, marriage, motherhood, and aging — from a phenomenological perspective. The book's opening declaration — 'One is not born, but rather becomes, a woman' ('On ne naît pas femme: on le devient') — is one of the most cited sentences in feminist philosophy and the foundational statement of the social constructionist approach to gender.\n\nThe Second Sex applies Sartrean existentialist philosophy (freedom, situation, bad faith, the Other) to the situation of women — arguing that woman has been constituted as the 'Other' (the Second Sex) relative to man (the Subject, the Absolute), denied the possibility of authentic self-determination by a patriarchal culture that defines femininity as passivity, immanence, and dependence rather than transcendence and freedom. De Beauvoir's analysis draws on existentialism (Sartre), Marxism (Engels), psychoanalysis (Freud, Adler), anthropology (Lévi-Strauss), and literary criticism (analyses of Montherlant, D. H. Lawrence, Claudel, Breton, and Stendhal's constructions of femininity in literature) to build a comprehensive account of women's oppression and its cultural mechanisms.\n\nThe Second Sex caused an immediate scandal in France — the Vatican placed it on the Index Librorum Prohibitorum, Sartre's companion Albert Camus accused de Beauvoir of making Frenchmen look ridiculous, and Gallimard printed two editions within the first week — and became one of the most widely read and influential texts of the 20th century, directly shaping the second-wave feminist movement of the 1960s–1970s.",
    "causes": [
      "De Beauvoir's existentialist philosophical formation — her lifelong intellectual collaboration with Sartre, her engagement with Hegelian philosophy (the master/slave dialectic, the constitution of the Other), and her application of Sartrean freedom and situation to the concrete conditions of women's lives — provided the philosophical framework for The Second Sex's analysis.",
      "De Beauvoir's personal experience as an intellectual woman in mid-20th-century France — her refusal of marriage (her pact with Sartre), her career as a philosopher, novelist, and essayist, and her experience of the constraints that French society placed on women's intellectual and professional ambitions — provided the biographical motivation for the project.",
      "The post-war French intellectual climate — the intense debates about freedom, oppression, and political commitment in the wake of the Occupation and Liberation — provided the political context for The Second Sex: de Beauvoir's analysis of women's oppression as a political question, a matter of freedom and unfreedom, placed it squarely within the existentialist political culture of the postwar."
    ],
    "effects": [
      "The Second Sex directly shaped the second-wave feminist movement of the 1960s–1970s — Betty Friedan acknowledged its influence on The Feminine Mystique (1963), Kate Millett's Sexual Politics (1970) and Germaine Greer's The Female Eunuch (1970) both engage with de Beauvoir's framework, and the declaration 'One is not born, but rather becomes, a woman' became the foundational statement of gender constructionism.",
      "De Beauvoir's concept of women as the 'Other' — constituted as the secondary sex relative to the male Subject — became the primary framework for feminist theoretical analysis of gender, applied in sociology, philosophy, literary criticism, and cultural studies, and was developed by Judith Butler (Gender Trouble, 1990) into the theory of gender performativity.",
      "The Second Sex's literary critical sections — the analyses of how male authors (Montherlant, Lawrence, Claudel, Breton, Stendhal) construct femininity — became models for feminist literary criticism, establishing the analysis of gender representation in literature as a central feminist critical practice."
    ],
    "relationships": [
      {"sourceSlug": "simone-de-beauvoir", "sourceName": "Simone de Beauvoir (1908–1986, French existentialist philosopher)", "verb": "AUTHORS", "targetSlug": "the-second-sex", "targetName": "The Second Sex (Le Deuxième Sexe, 1949, 2 volumes)", "context": "De Beauvoir published The Second Sex in 1949 — the foundational text of modern feminism, introducing 'One is not born, but rather becomes, a woman' and the concept of woman as the 'Other'."},
      {"sourceSlug": "the-second-sex", "sourceName": "Second Sex (woman as Other, social constructionism, gender)", "verb": "FOUNDATIONAL_TEXT_OF", "targetSlug": "second-wave-feminism", "targetName": "Second-wave feminism (1960s–1970s — Friedan, Millett, Greer)", "context": "The Second Sex directly shaped second-wave feminism — Betty Friedan's The Feminine Mystique (1963), Kate Millett's Sexual Politics (1970), and Germaine Greer's The Female Eunuch (1970) all engage with de Beauvoir's framework."},
      {"sourceSlug": "the-second-sex", "sourceName": "Second Sex (gender as social construction — Butler, gender performativity)", "verb": "INFLUENCES", "targetSlug": "gender-theory", "targetName": "Gender theory and Judith Butler's Gender Trouble (1990)", "context": "De Beauvoir's 'One is not born, but rather becomes, a woman' — the foundational statement of gender constructionism — was taken up and developed by Judith Butler in Gender Trouble (1990) into the theory of gender performativity."}
    ],
    "places": [
      {"name": "Paris, France (published June 1949; immediate scandal — Vatican Index, 2 editions first week)", "role": "The Second Sex was published in Paris in June 1949 — causing immediate scandal (Vatican Index, Camus criticism) but also extraordinary demand (two editions in the first week)"},
      {"name": "United States and global feminist movements (second-wave feminism, 1960s–1970s)", "role": "The Second Sex's influence spread from France to the United States and global feminist movements — it was the philosophical foundation of second-wave feminism and shaped women's liberation movements worldwide"}
    ],
    "subjects": ["French Philosophy", "Modern Era", "Simone de Beauvoir", "Feminism", "Existentialism", "Gender Theory", "Social Theory", "20th Century"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Second Sex (de Beauvoir, 1949) is the foundational text of modern feminism — its analysis of woman as the 'Other' and its declaration that 'One is not born, but rather becomes, a woman' are the philosophical foundations of gender constructionism. It directly shaped second-wave feminism (Friedan, Millett, Greer) and influenced Judith Butler's gender performativity theory. As the most important feminist philosophical text of the 20th century, it transformed how women's situation is understood across philosophy, sociology, literature, and political theory.",
      "significanceCategory": "world-changing"
    }
  }
},

"waiting-for-godot": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780waiting-for-godot.json",
  "slug": "waiting-for-godot",
  "data": {
    "summary": "Waiting for Godot (French: En attendant Godot) is a play in two acts by the Irish playwright and novelist Samuel Beckett (1906–1989), written in French in 1948–1949, first performed at the Théâtre de Babylone in Paris on 5 January 1953 (directed by Roger Blin), translated into English by Beckett himself in 1954, and widely recognised as the most important play of the 20th century and the defining work of the Theatre of the Absurd. Beckett was awarded the Nobel Prize in Literature in 1969, with the committee citing his work for giving 'destitution its elevation' in a new literary form.\n\nThe play presents two tramps, Vladimir (Didi) and Estragon (Gogo), waiting by a leafless tree on an empty road for the arrival of a mysterious person named Godot, who never comes — on each of the play's two evenings, a boy arrives to announce that Godot will not come today but will certainly come tomorrow. Two other characters appear briefly: Pozzo, a domineering and eventually blind master, and Lucky, his mute (in Act II) slave who carries luggage and performs an extraordinary stream-of-consciousness monologue ('think, pig') in Act I. The play's minimalist dramatic situation — two men waiting, doing nothing, almost nothing happens, nothing changes — was the most radical challenge to the conventions of dramatic form since the invention of drama: nothing is resolved, no plot develops, the wait continues.\n\nWaiting for Godot is the paradigmatic work of Absurdist theatre — it enacts, rather than merely represents, the absurdity of human existence (the waiting without purpose, the repetition, the forgetting, the mutual dependence of characters who cannot leave and cannot act). Beckett's dramatic method — stripping away all theatrical conventions (plot, psychological characterisation, resolution) to expose the bare minimum of theatrical presence — influenced every subsequent movement in post-war theatre, from the British kitchen-sink drama through Pinter's Theatre of Menace to the post-dramatic theatre of the 21st century.",
    "causes": [
      "Beckett's philosophical formation in European existentialism and his engagement with the 'literature of the impossible' — his critical essays on Kafka, his reading of Descartes, Schopenhauer, and Leibniz, and his development of the 'trilogy' (Molloy, Malone Dies, The Unnamable) in the same creative period — provided the philosophical context for Waiting for Godot's exploration of human existence as purposeless waiting.",
      "Beckett's wartime experience in France — his service in the French Resistance (1941–1942), his hiding in rural France after the Resistance network was betrayed, and his experience of the grinding uncertainty of waiting in dangerous circumstances — is frequently cited as a biographical source for the play's situation of waiting in existential uncertainty.",
      "The French avant-garde theatrical tradition — the Theatre of Cruelty (Artaud), the Surrealist theatrical experiments, and the critical reception of Beckett's prose trilogy in Parisian literary culture (Beckett was published by Les Éditions de Minuit, the resistance publisher) — provided the theatrical and intellectual environment for the first production."
    ],
    "effects": [
      "Waiting for Godot transformed 20th-century theatre — its radical stripping away of dramatic convention (plot, resolution, psychological realism) demonstrated that theatre could be stripped to the bare minimum of theatrical situation and still produce profound dramatic power, opening up the entire range of post-dramatic and minimalist theatre.",
      "Beckett's influence on subsequent playwrights was pervasive — Harold Pinter acknowledged Beckett as his most important influence (Pinter's Theatre of Menace shares Beckett's minimalist situation and menacing uncertainty), and Beckett's impact extended through Tom Stoppard (Rosencrantz and Guildenstern Are Dead directly engages with Waiting for Godot), Edward Albee, and the entire tradition of post-war avant-garde theatre.",
      "The phrase 'waiting for Godot' entered the English and French languages as an idiom for waiting for something that will never arrive — a cultural shorthand for futile or perpetual waiting that demonstrates the play's extraordinary cultural penetration beyond the theatrical context."
    ],
    "relationships": [
      {"sourceSlug": "samuel-beckett", "sourceName": "Samuel Beckett (1906–1989, Irish playwright and novelist)", "verb": "AUTHORS", "targetSlug": "waiting-for-godot", "targetName": "Waiting for Godot (En attendant Godot, Paris premiere January 1953)", "context": "Beckett wrote Waiting for Godot in French in 1948–1949; its Paris premiere (5 January 1953) was directed by Roger Blin and became the most important theatrical event of the post-war period."},
      {"sourceSlug": "waiting-for-godot", "sourceName": "Waiting for Godot (Absurdism, minimalism, stripping dramatic convention)", "verb": "PARADIGMATIC_WORK_OF", "targetSlug": "theatre-of-the-absurd", "targetName": "Theatre of the Absurd (Ionesco, Pinter, Albee — 1950s–1960s)", "context": "Waiting for Godot is the paradigmatic work of Absurdist theatre — its radical stripping of dramatic convention defined the movement and influenced every subsequent post-war avant-garde theatrical tradition."},
      {"sourceSlug": "waiting-for-godot", "sourceName": "Waiting for Godot (Beckett's influence — Pinter, Stoppard)", "verb": "INFLUENCES", "targetSlug": "harold-pinter", "targetName": "Harold Pinter (1930–2008, British playwright, Theatre of Menace)", "context": "Harold Pinter acknowledged Beckett as his primary influence — Pinter's Theatre of Menace (The Birthday Party, The Caretaker) shares Beckett's minimalist dramatic situation, menacing uncertainty, and refusal of resolution."}
    ],
    "places": [
      {"name": "Paris, France (Théâtre de Babylone, 5 January 1953 — first performance, Roger Blin)", "role": "Waiting for Godot had its world premiere at the Théâtre de Babylone in Paris on 5 January 1953 — directed by Roger Blin, the production was the most important theatrical event of the immediate post-war period"},
      {"name": "Europe and the English-speaking world (translation 1954; global theatrical reception)", "role": "Beckett translated Waiting for Godot into English in 1954 and the play's influence spread across the English-speaking world — its London premiere (1955) and New York premiere (1956) established it as the defining play of post-war theatre"}
    ],
    "subjects": ["Irish Literature", "Modern Era", "Samuel Beckett", "Theatre of the Absurd", "Drama", "Existentialism", "20th Century", "French Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Waiting for Godot (Beckett, 1953) is the most important play of the 20th century — its radical stripping of dramatic convention (plot, resolution, characterisation) defined the Theatre of the Absurd and transformed post-war theatre worldwide. Beckett's influence on Pinter, Stoppard, and Albee, and the phrase 'waiting for Godot' as a cultural idiom, demonstrate its extraordinary reach. The Nobel Prize (1969) recognised Beckett as having given 'destitution its elevation' in a new literary form.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-republic": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-republic.json",
  "slug": "the-republic",
  "data": {
    "summary": "The Republic (Greek: Πολιτεία, Politeia) is the central and most widely read work of the ancient Greek philosopher Plato (c. 428–348 BCE), composed c. 375–360 BCE, a dialogue in ten books in which Socrates (Plato's teacher and primary interlocutor) and his companions discuss the nature of justice (dikaiosynē), the ideal city-state (kallipolis), the education of the guardians, the theory of knowledge and the Forms, the nature of the soul, and the character of the philosopher-king. It is the most influential work of political philosophy ever written, the foundational text of Western political theory, and one of the supreme achievements of ancient Greek philosophy.\n\nThe Republic develops an account of the just city (kallipolis) as an analogy for the just soul — the three classes of the kallipolis (rulers/philosopher-kings, auxiliaries/warriors, producers) correspond to the three parts of the soul (reason, spirit, appetite). The philosopher-kings are those who have ascended from the cave (the Allegory of the Cave, Book VII — Plato's most famous image: prisoners in a cave mistake shadows on the wall for reality, until one is freed and ascends to see the sunlight of the Good) and can see the Forms (the unchanging, eternal, perfect realities of which sensible things are imperfect copies) — only those who have seen the Good can rule wisely. The Republic also contains the first systematic discussion of political systems (oligarchy, democracy, tyranny) and their relation to character types, the famous critique of poetry as imitation (mimēsis) of the sensible world (itself an imitation of the Forms), and the Myth of Er (a near-death vision of the afterlife and the souls' choice of new lives).\n\nThe Republic's philosophical influence is comprehensive — its theory of Forms shaped the entire subsequent development of metaphysics (Neoplatonism, Christian theology, Idealism); its political philosophy shaped the tradition of political theory from Augustine through Machiavelli to Rousseau and Marx; and its educational theory (the education of the philosopher-king through mathematics, music, gymnastics, and philosophy) shaped the Western conception of liberal education.",
    "causes": [
      "Plato's political context — the execution of Socrates (399 BCE) by the Athenian democracy, which Plato experienced as a catastrophic political failure, and the subsequent instability of Greek city-state politics (the fall of the Thirty Tyrants, the Corinthian War, the Peloponnesian War's aftermath) — drove Plato's determination to understand what justice is and what a truly just political order would look like.",
      "The Socratic philosophical tradition — Plato's apprenticeship to Socrates (c. 407–399 BCE) and his continuation of the Socratic method of philosophical dialogue — provided the form and method of the Republic: the dialogue as a vehicle for philosophical inquiry, and Socrates as the central questioner whose method exposes contradictions and drives toward truth.",
      "Plato's mathematical and Pythagorean influences — his encounter with Pythagorean philosophy in Sicily (c. 388 BCE) and his sustained engagement with mathematics as a model of knowledge of eternal truths — provided the epistemological framework for the theory of Forms and the account of mathematical knowledge as an intermediate between opinion (about sensible things) and intellection (about the Forms)."
    ],
    "effects": [
      "The Republic's theory of Forms (eternal, perfect, unchanging realities accessible only to reason) became the foundational metaphysical framework of the Neoplatonic tradition (Plotinus, Porphyry, Iamblichus) and, through Neoplatonism, of Christian theology (Augustine's God as the Form of the Good, the eternal truths as ideas in the divine mind).",
      "The Republic's political philosophy — the analysis of political systems as expressions of character types, the concept of the philosopher-king, the critique of democracy as the rule of appetite — shaped the entire subsequent tradition of Western political philosophy, from Aristotle's critique in the Politics through Cicero, Augustine, Machiavelli, Rousseau, and Marx.",
      "Alfred North Whitehead's famous remark that 'the safest general characterisation of the European philosophical tradition is that it consists of a series of footnotes to Plato' applies with particular force to the Republic — its influence on metaphysics, political philosophy, epistemology, aesthetics, and educational theory is so pervasive that Western philosophy can hardly be understood without it."
    ],
    "relationships": [
      {"sourceSlug": "plato", "sourceName": "Plato (c. 428–348 BCE, Athenian philosopher)", "verb": "AUTHORS", "targetSlug": "the-republic", "targetName": "The Republic (Politeia, c. 375–360 BCE, 10 books)", "context": "Plato composed the Republic c. 375–360 BCE — the central work of his philosophy, containing the theory of Forms, the Allegory of the Cave, and the political theory of the kallipolis."},
      {"sourceSlug": "the-republic", "sourceName": "Republic (Allegory of the Cave, Forms, philosopher-king)", "verb": "ESTABLISHES", "targetSlug": "platonic-philosophy", "targetName": "Platonic philosophy (Theory of Forms, metaphysics, epistemology)", "context": "The Republic establishes Plato's Theory of Forms and the Allegory of the Cave — the metaphysical and epistemological framework that shaped Neoplatonism, Christian theology, and the entire subsequent history of Western philosophy."},
      {"sourceSlug": "the-republic", "sourceName": "Republic (kallipolis, philosopher-king, political philosophy)", "verb": "FOUNDATIONAL_TEXT_OF", "targetSlug": "western-political-theory", "targetName": "Western political philosophy (Aristotle, Cicero, Augustine, Machiavelli, Rousseau, Marx)", "context": "The Republic is the foundational text of Western political theory — its analysis of political systems, the critique of democracy, and the concept of the philosopher-king shaped political thought from Aristotle through Machiavelli and Marx."}
    ],
    "places": [
      {"name": "Athens, Greece (Socrates' trial and execution 399 BCE; Plato's Academy c. 387 BCE)", "role": "The Republic was composed in Athens, at the Academy that Plato founded c. 387 BCE — the execution of Socrates by Athenian democracy was the political trauma that drove Plato's investigation of justice and the ideal city"},
      {"name": "Greek world and Western civilisation (continuous philosophical tradition)", "role": "The Republic's influence extends across the entire Western philosophical tradition — its concepts (Forms, kallipolis, philosopher-king, Allegory of the Cave) are foundational to philosophy, theology, political theory, and educational thought from antiquity to the present"}
    ],
    "subjects": ["Greek Philosophy", "Ancient Era", "Plato", "Political Philosophy", "Epistemology", "Metaphysics", "Justice", "Classical Antiquity"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Republic (Plato, c. 375–360 BCE) is the most influential work of political philosophy ever written and one of the supreme achievements of ancient Greek philosophy. Its Theory of Forms shaped Neoplatonism and Christian theology; its political theory shaped Western political thought from Aristotle through Rousseau and Marx; its Allegory of the Cave is the most famous philosophical image in the Western tradition. Whitehead's description of Western philosophy as 'a series of footnotes to Plato' applies most forcefully to the Republic.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-pilgrims-progress": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-pilgrims-progress.json",
  "slug": "the-pilgrims-progress",
  "data": {
    "summary": "The Pilgrim's Progress from This World to That Which Is to Come (commonly The Pilgrim's Progress) is a Christian allegorical novel by the English author John Bunyan (1628–1688), written during his second imprisonment in Bedford Gaol (1675–1676) and first published in London on 18 February 1678 by Nathaniel Ponder. It is one of the most significant works of religious English literature and is regarded as one of the first novels in the English language. The work is an allegory of the Christian life — the spiritual journey of a man named Christian from the City of Destruction (the world) to the Celestial City (Heaven), encountering figures representing spiritual states and temptations (Worldly Wiseman, Mr. Legality, Apollyon, Faithful, Hopeful, Ignorance, By-ends, Vanity Fair) along the way.\n\nThe Pilgrim's Progress was the most widely printed and distributed book in the English-speaking world after the Bible for two centuries following its publication (1678 – c. 1880) — it was translated into over 200 languages, was the primary book owned by Protestant households alongside the Bible, and shaped the religious and literary imagination of the English-speaking world from the Puritan era through the Victorian period. Its allegorical method — giving abstract spiritual states concrete fictional form as named characters and locations — created the basic model for the Protestant popular religious imagination.\n\nBunyan wrote the Pilgrim's Progress from personal experience of Nonconformist Christianity: he was a tinker's son, a Nonconformist (Baptist) preacher who was imprisoned from 1660–1672 for preaching without a licence under the Clarendon Code, and again briefly in 1675–1676. The book's extraordinary power comes from its combination of simple, direct English prose (based on the King James Bible's rhythms and vocabulary) with a vivid allegorical imagination — it reads simultaneously as spiritual autobiography and as a narrative adventure.",
    "causes": [
      "Bunyan's imprisonment — his twelve-year imprisonment in Bedford Gaol (1660–1672) for unlicensed preaching under the Clarendon Code, and his brief second imprisonment (1675–1676) during which he composed the Pilgrim's Progress — provided the biographical context for a work about the soul's journey through a hostile world toward redemption.",
      "The Puritan theological tradition — Bunyan's formation as a Nonconformist Baptist preacher, his deep knowledge of the King James Bible, and his engagement with the Calvinist doctrines of grace, election, and the Christian's spiritual warfare — provided the theological framework for the allegory: the journey from the City of Destruction to the Celestial City is a Calvinist map of conversion and sanctification.",
      "The English allegorical tradition — the medieval dream-vision (William Langland's Piers Plowman, the best analogue for Bunyan's form) and the Spenserian allegorical romance (The Faerie Queene) — provided the literary models for Bunyan's allegorical narrative, though his source was primarily the Bible rather than classical or medieval literature."
    ],
    "effects": [
      "The Pilgrim's Progress was the most widely distributed book in the English-speaking world after the Bible for over two centuries — printed in hundreds of editions, translated into over 200 languages, and owned by virtually every Protestant household — making it arguably the most influential single book in the formation of Protestant popular culture.",
      "Bunyan's narrative vocabulary — Vanity Fair, the Slough of Despond, the Valley of the Shadow of Death, the Delectable Mountains, Doubting Castle, Giant Despair — entered the English language as cultural idioms that are still current; 'Vanity Fair' in particular became one of the most powerful tropes in English literature (Thackeray's novel).",
      "The Pilgrim's Progress's influence on subsequent English literature is extensive — Thackeray's Vanity Fair (the title), Hawthorne's allegorical fiction, Louisa May Alcott's Little Women (the girls reading the Pilgrim's Progress), and C. S. Lewis's Pilgrim's Regress (1933) all draw directly on Bunyan's model."
    ],
    "relationships": [
      {"sourceSlug": "john-bunyan", "sourceName": "John Bunyan (1628–1688, English Nonconformist preacher)", "verb": "AUTHORS", "targetSlug": "the-pilgrims-progress", "targetName": "The Pilgrim's Progress (first published 18 February 1678)", "context": "Bunyan wrote The Pilgrim's Progress during his second imprisonment (1675–1676) — the most widely distributed book in the English-speaking world after the Bible for two centuries, translated into over 200 languages."},
      {"sourceSlug": "the-pilgrims-progress", "sourceName": "Pilgrim's Progress (Vanity Fair, Slough of Despond — cultural idioms)", "verb": "CONTRIBUTES_IDIOMS_TO", "targetSlug": "english-language-culture", "targetName": "English language and cultural idiom (Vanity Fair, Slough of Despond, etc.)", "context": "Bunyan's allegorical place names (Vanity Fair, the Slough of Despond, Doubting Castle, Giant Despair) entered the English language as cultural idioms — Thackeray's Vanity Fair is the most celebrated literary use."},
      {"sourceSlug": "the-pilgrims-progress", "sourceName": "Pilgrim's Progress (Protestant popular culture, 200 languages)", "verb": "FOUNDATIONAL_TEXT_OF", "targetSlug": "protestant-popular-culture", "targetName": "Protestant popular culture (Nonconformist, Baptist, missionary traditions)", "context": "The Pilgrim's Progress was the primary popular religious book of Protestant Christianity after the Bible — owned by virtually every Protestant household, carried by English-speaking missionaries worldwide, and translated into over 200 languages."}
    ],
    "places": [
      {"name": "Bedford, England (Bunyan's imprisonment — Bedford Gaol 1660–1672, 1675–1676)", "role": "Bunyan wrote The Pilgrim's Progress during his second imprisonment in Bedford Gaol (1675–1676) — the city of Bedford has Bunyan monuments and the Bedford Museum dedicated to his memory"},
      {"name": "English-speaking Protestant world (200+ language translations; missionary circulation)", "role": "The Pilgrim's Progress was carried worldwide by English-speaking Protestant missionaries — translated into over 200 languages and distributed across Africa, Asia, and the Americas as the primary text of Protestant popular religious culture"}
    ],
    "subjects": ["English Literature", "Early Modern Era", "John Bunyan", "Christian Allegory", "Protestantism", "Puritan Literature", "Novel", "Religious Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Pilgrim's Progress (Bunyan, 1678) is one of the most widely distributed books in the English-speaking world after the Bible — printed in hundreds of editions, translated into over 200 languages, and owned by virtually every Protestant household for two centuries. Its allegorical vocabulary (Vanity Fair, Slough of Despond) entered the English language; its influence on subsequent English literature (Thackeray, Hawthorne, Alcott, C. S. Lewis) was extensive; and its place in Protestant popular culture was foundational for the formation of English-speaking Christianity worldwide.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-imitation-of-christ": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-imitation-of-christ.json",
  "slug": "the-imitation-of-christ",
  "data": {
    "summary": "The Imitation of Christ (Latin: De Imitatione Christi) is a Christian devotional book attributed to Thomas à Kempis (c. 1380–1471), a Dutch-German Augustinian canon at the monastery of St Agnes near Zwolle in the Netherlands, composed c. 1418–1427 CE and first circulated in manuscript form from c. 1420. The Imitation of Christ is the most widely translated Christian devotional work after the Bible and one of the most widely read spiritual books in the history of Christianity, translated into over 95 languages and published in thousands of editions over six centuries. It is the foundational text of the Devotio Moderna (Modern Devotion), the 14th–15th century spiritual reform movement in the Low Countries associated with Geert Groote and the Brethren of the Common Life.\n\nThe Imitation of Christ consists of four books: Book I ('Counsels on the Spiritual Life') — on the vanity of worldly learning and the importance of self-knowledge; Book II ('Counsels on the Inner Life') — on spiritual progress through humility and peace; Book III ('On Inward Consolation') — a dialogue between Christ and the soul, the longest and most personal book, in which Christ speaks directly to the soul about love, temptation, and divine consolation; and Book IV ('On the Blessed Sacrament') — on the Eucharist as the central practice of Christian life. The book's central theme is the imitation of Christ through humility, self-denial, and interior conversion: its opening line — 'What does it profit you to enter into deep discussion of the Trinity if you lack humility, and so are displeasing to the Trinity?' — sets the tone of practical piety over speculative theology.\n\nThe Imitation of Christ shaped the interior life of Catholic and Protestant saints and scholars — Erasmus, Thomas More, Thomas Cranmer, Ignatius of Loyola, Francis de Sales, John Wesley, and Thomas Merton all read it with devotion — and has been a primary devotional text of Western Christianity for six centuries.",
    "causes": [
      "The Devotio Moderna movement — the spiritual reform movement founded by Geert Groote (1340–1384) in the Low Countries, which emphasised practical interior piety, humility, self-denial, and regular reading of Scripture over scholastic speculation — was the immediate spiritual context for the Imitation of Christ: Thomas à Kempis was a member of the Brethren of the Common Life, Groote's movement.",
      "The late medieval criticism of scholastic theology — the reaction against the arid speculative theology of the late scholastic tradition and the desire for a more personal, interior, and affective spirituality — drove the Imitation's emphasis on practical piety over intellectual speculation: 'What does it profit you to enter into deep discussion of the Trinity if you lack humility?'",
      "The tradition of Christian mystical and devotional writing — the Rhineland mysticism of Meister Eckhart, Johannes Tauler, and Heinrich Suso, and the Flemish mysticism of Jan van Ruusbroec — provided the spiritual vocabulary and the emphasis on interior life and union with God that the Imitation synthesised into a more practical and accessible form."
    ],
    "effects": [
      "The Imitation of Christ's influence on Christian spirituality — both Catholic and Protestant — across six centuries is unparalleled among devotional texts: it shaped the spirituality of Ignatius of Loyola (who read it daily), Francis de Sales, Thomas Merton, and countless others, and was central to the formation of both Jesuit spirituality and Protestant devotional piety.",
      "The Imitation was one of the first books printed on the Gutenberg press and immediately became a bestseller in the print era — its extraordinary diffusion through early print (hundreds of editions in the first century of printing) demonstrates the demand for practical devotional literature and the role of print in the democratisation of spiritual reading.",
      "The Imitation's influence on Christian education — particularly through the Jesuit educational tradition, which used the book extensively — shaped the formation of Catholic educated elites across Europe and the Americas for centuries, making it one of the most important texts in the history of Western religious education."
    ],
    "relationships": [
      {"sourceSlug": "thomas-a-kempis", "sourceName": "Thomas à Kempis (c. 1380–1471, Augustinian canon, Devotio Moderna)", "verb": "AUTHORS", "targetSlug": "the-imitation-of-christ", "targetName": "The Imitation of Christ (De Imitatione Christi, c. 1418–1427, 4 books)", "context": "Thomas à Kempis composed the Imitation of Christ c. 1418–1427 — the most widely read Christian devotional work after the Bible, translated into over 95 languages and published in thousands of editions over six centuries."},
      {"sourceSlug": "the-imitation-of-christ", "sourceName": "Imitation of Christ (Devotio Moderna, practical piety over speculation)", "verb": "FOUNDATIONAL_TEXT_OF", "targetSlug": "devotio-moderna", "targetName": "Devotio Moderna (Modern Devotion, 14th–15th century Low Countries spiritual reform)", "context": "The Imitation of Christ is the foundational text of the Devotio Moderna — Geert Groote's 14th–15th century spiritual reform movement in the Low Countries, which emphasised practical interior piety over scholastic speculation."},
      {"sourceSlug": "the-imitation-of-christ", "sourceName": "Imitation of Christ (Jesuit spirituality, Ignatius, daily reading)", "verb": "INFLUENCES", "targetSlug": "jesuit-spirituality", "targetName": "Jesuit spirituality and education (Ignatius of Loyola, Spiritual Exercises)", "context": "Ignatius of Loyola read the Imitation of Christ daily and it profoundly shaped Jesuit spirituality — the Jesuit educational tradition used the book extensively in the formation of Catholic educated elites across Europe and the Americas."}
    ],
    "places": [
      {"name": "Zwolle (St Agnes monastery, Netherlands — Thomas à Kempis's home, composition context)", "role": "Thomas à Kempis composed the Imitation at the monastery of St Agnes near Zwolle in the Netherlands — the heartland of the Devotio Moderna movement founded by Geert Groote in the same region"},
      {"name": "Catholic and Protestant Christianity worldwide (95+ language translations; 6 centuries of devotional use)", "role": "The Imitation has been translated into over 95 languages and used in devotional practice across Catholic and Protestant Christianity for six centuries — one of the most widely distributed books in the history of Western Christianity"}
    ],
    "subjects": ["Christian Devotion", "Medieval Era", "Thomas à Kempis", "Catholic Spirituality", "Devotio Moderna", "Latin Literature", "Religious Literature", "Mysticism"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Imitation of Christ (Thomas à Kempis, c. 1418–1427) is the most widely read Christian devotional work after the Bible — translated into over 95 languages and published in thousands of editions over six centuries. Its emphasis on practical interior piety over intellectual speculation shaped the Devotio Moderna, Jesuit spirituality, and Protestant devotional piety. The book's influence on Ignatius of Loyola, Francis de Sales, John Wesley, and Thomas Merton makes it one of the most consequential texts in the history of Christian spirituality.",
      "significanceCategory": "world-changing"
    }
  }
},

"upanishads": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780upanishads.json",
  "slug": "upanishads",
  "data": {
    "summary": "The Upanishads (Sanskrit: उपनिषद्, Upaniṣad, from upa 'near' + ni 'down' + sad 'to sit' — 'sitting down near a teacher') are a collection of ancient Sanskrit texts that constitute the philosophical and metaphysical culmination of Vedic literature — the last layer (hence 'Vedānta', the 'end of the Vedas') of the Vedic corpus, composed c. 800–200 BCE (the principal Upanishads) and continuing into the medieval period (the later or minor Upanishads, of which over 100 exist). The principal (mukhya) Upanishads number approximately 13 (according to the most canonical listing: Bṛhadāraṇyaka, Chāndogya, Taittirīya, Aitareya, Kaṭha, Īśā, Kena, Muṇḍaka, Māṇḍūkya, Praśna, Śvetāśvatara, Kaushītaki, and Maitrī), composed in classical Sanskrit (some in mixed prose and verse, others in verse) and preserved within the four Vedas as their concluding philosophical commentaries.\n\nThe Upanishads are the foundational texts of Vedānta philosophy and of the Hindu understanding of the ultimate nature of reality. Their central philosophical teachings revolve around: Brahman (the ultimate, impersonal, infinite reality underlying all existence — 'that from which all beings are born, in which they live, and into which they return'); Ātman (the individual Self or soul — identical with Brahman in the non-dualist Advaita interpretation: 'tat tvam asi', 'that thou art'); Karma and rebirth; and Moksha (liberation from the cycle of death and rebirth through knowledge of the identity of Ātman and Brahman). The Upanishads contain the foundational philosophical statements of Hindu metaphysics — 'Aham Brahmāsmi' ('I am Brahman'), 'Tat tvam asi' ('That thou art'), 'Prajñānam Brahma' ('Consciousness is Brahman'), 'Ayam ātmā Brahma' ('This Self is Brahman') — the 'four great sayings' (mahāvākyas) that became the philosophical touchstones of Vedānta.\n\nThe Upanishads were translated into Persian by Prince Dara Shukoh (1657), into Latin by Anquetil-Duperron (from Dara Shukoh's Persian version, 1801–1802), and their reception by Schopenhauer — who called the Oupnek'hat (Anquetil-Duperron's translation) 'the solace of my life' — was instrumental in introducing Hindu philosophy to Western thought.",
    "causes": [
      "The Vedic ritual tradition's internal critique — the Āraṇyakas (forest texts) and early Upanishads represent a philosophical interiorisation of the Vedic sacrificial tradition: rather than external ritual, the Upanishads develop the idea that the inner reality of the sacrifice (the fire, the breath, the self) is identical with the ultimate reality (Brahman) — a move from ritual to philosophy.",
      "The intellectual environment of the Axial Age in India (c. 800–200 BCE) — the period of intense philosophical and religious questioning across India (including the emergence of Buddhism and Jainism) that questioned the authority of Vedic ritual and sought deeper philosophical accounts of reality — provided the context for the Upanishads' move from ritual to philosophical inquiry.",
      "The guru-student (guru-śiṣya) tradition — the transmission of philosophical insight through direct teaching between teacher and student, in the forest retreats (āśramas) away from the village — provided the social and intellectual context for the Upanishadic dialogues: many Upanishads are structured as teaching conversations between great teachers (Yājñavalkya, Uddālaka Āruṇi) and their students or wives."
    ],
    "effects": [
      "The Upanishads became the foundational texts of Vedānta philosophy — the three major Vedānta schools (Advaita Vedānta of Shankaracharya, Viśiṣṭādvaita of Rāmānuja, and Dvaita of Madhva) all base their divergent philosophical positions on interpretations of the same Upanishadic texts — making them the primary philosophical authority for the Hindu intellectual tradition.",
      "Schopenhauer's encounter with the Upanishads (through Anquetil-Duperron's Latin translation, 1801–1802) was a decisive philosophical influence — he acknowledged the Upanishads as the closest non-Western philosophical tradition to his own thought, and his discovery contributed to the 19th-century European engagement with Indian philosophy that shaped Nietzsche, Schopenhauer, and subsequently the Western New Age tradition.",
      "The Upanishads' influence on modern Hindu reform — Swami Vivekananda's presentation of Advaita Vedānta at the Parliament of World Religions (Chicago, 1893), the Theosophical Society's promotion of Indian spiritual philosophy, and the global spread of yoga, meditation, and non-dualist philosophy — all drew primarily on Upanishadic teaching, making the Upanishads the primary channel through which Hindu philosophy reached the modern world."
    ],
    "relationships": [
      {"sourceSlug": "upanishads", "sourceName": "Upanishads (c. 800–200 BCE, principal Upanishads, Vedānta)", "verb": "CONCLUDING_LAYER_OF", "targetSlug": "vedic-literature", "targetName": "Vedic literature (Ṛgveda, Sāmaveda, Yajurveda, Atharvaveda, Brāhmaṇas, Āraṇyakas)", "context": "The Upanishads are the concluding philosophical layer of the Vedic corpus — 'Vedānta' (the end of the Vedas) — representing a philosophical interiorisation of the Vedic sacrificial tradition."},
      {"sourceSlug": "upanishads", "sourceName": "Upanishads (Brahman, Ātman, tat tvam asi — Vedānta philosophy)", "verb": "FOUNDATIONAL_TEXT_OF", "targetSlug": "vedanta-philosophy", "targetName": "Vedānta philosophy (Advaita — Shankara; Viśiṣṭādvaita — Rāmānuja; Dvaita — Madhva)", "context": "The Upanishads are the foundational texts of Vedānta — the three major Vedānta schools (Advaita, Viśiṣṭādvaita, Dvaita) all base their divergent philosophical positions on interpretations of the same Upanishadic texts."},
      {"sourceSlug": "upanishads", "sourceName": "Upanishads (Schopenhauer, Oupnek'hat, European philosophy)", "verb": "INFLUENCES", "targetSlug": "arthur-schopenhauer", "targetName": "Arthur Schopenhauer (1788–1860, German philosopher)", "context": "Schopenhauer called Anquetil-Duperron's Latin translation of the Upanishads 'the solace of my life' — his encounter with the Upanishads reinforced his philosophical development and was instrumental in introducing Hindu philosophy to Western thought."}
    ],
    "places": [
      {"name": "Ancient India (Gangetic plain, forest retreats/āśramas, c. 800–200 BCE)", "role": "The principal Upanishads were composed in the forest retreats (āśramas) of ancient India c. 800–200 BCE — the intellectual environment of the Axial Age in India that also produced Buddhism and Jainism"},
      {"name": "Europe (Anquetil-Duperron Latin translation 1801–1802; Schopenhauer, 19th-century reception)", "role": "Anquetil-Duperron's Latin translation (1801–1802) brought the Upanishads to European readers — Schopenhauer's engagement was decisive for the European reception of Hindu philosophy"}
    ],
    "subjects": ["Sanskrit Literature", "Ancient Era", "Vedānta", "Hindu Philosophy", "Indian Religion", "Metaphysics", "Oral Tradition", "Religious Texts"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Upanishads (c. 800–200 BCE) are the foundational texts of Vedānta philosophy and the philosophical summit of Hindu religious thought. Their teaching of Brahman, Ātman, and moksha is the basis of the three major Vedānta schools; their influence on Schopenhauer introduced Hindu metaphysics to Western thought; and Swami Vivekananda's Advaita Vedānta — presented at Chicago in 1893 — made the Upanishads the primary channel through which Hindu philosophy reached the modern world.",
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
