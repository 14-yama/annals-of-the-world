#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 52 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: the-ugly-duckling (Andersen), the-little-match-girl (Andersen),
          thumbelina (Andersen), the-cat-in-the-hat (Dr. Seuss),
          the-frog-prince (Brothers Grimm), matilda (Roald Dahl),
          the-ants-and-the-grasshopper (Aesop), the-boy-who-cried-wolf (Aesop)
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-52-may2026"

ENRICHMENTS = {

"the-ugly-duckling": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-ugly-duckling.json",
  "slug": "the-ugly-duckling",
  "data": {
    "summary": "The Ugly Duckling (Danish: Den grimme ælling) is a fairy tale by Hans Christian Andersen (1805–1875), first published on 11 November 1843 in the fourth volume of Eventyr fortalte for Børn ('Fairy Tales Told for Children'). The tale narrates the story of an ugly, grey bird hatched in a duck's nest — rejected by the farm animals and other ducks for his appearance, driven away by his own mother, forced to survive alone through a brutal winter — who discovers in spring that he has grown into a beautiful white swan. The tale is one of the most explicitly autobiographical of all Andersen's fairy tales: Andersen, born to a poor cobbler's family in Odense, raised in poverty and obscurity, mocked for his ungainly appearance and manner, eventually achieved fame as the great literary artist of Denmark — and he identified deeply with the ugly duckling who is revealed as a swan.\n\nThe Ugly Duckling is among the most universally applicable of all Andersen's tales — its central metaphor (the ugly duckling who is really a swan, the outsider who is really exceptional, the suffering that precedes transformation) has become one of the most widely used metaphors in global culture, applied to everything from personal development narratives to talent discovery in sports and business, to national coming-of-age narratives. 'The ugly duckling story' has entered virtually every major language as a phrase for the narrative of hidden potential revealed, making it one of the most pervasive fairy tale metaphors in world culture.\n\nThe tale's implicit ideology — the consolation of suffering through the discovery of innate superiority — has also been critiqued by scholars who note that the ugly duckling's transformation is not the result of hard work or personal change, but the discovery of his true aristocratic nature (swans are royal birds in European tradition). This critique positions the tale as a conservative fantasy of natural aristocracy rather than a democratic narrative of self-improvement, and this tension gives the tale its enduring analytical interest.",
    "causes": [
      "Andersen's own autobiographical experience — his childhood poverty in Odense, his ungainly appearance, his social marginalisation in Copenhagen intellectual society, and his eventual emergence as a celebrated writer — provided the direct inspiration for the tale, which is the most personal and self-referential of all Andersen's fairy tales.",
      "The European tradition of transformation narratives — the folk tale motif of the disguised prince, the enchanted animal restored to human form, and the ugly exterior concealing a beautiful interior — provided the narrative structure that Andersen adapted into his most personal metaphor.",
      "The Danish social context of Andersen's era — the class consciousness, the aristocratic prestige of swans as royal birds, and the social hierarchy of the Danish court that Andersen navigated as a socially ambiguous figure (celebrated enough to dine with kings, but never fully accepted) — shaped the tale's specific dynamics of social exclusion and eventual transformation."
    ],
    "effects": [
      "'The ugly duckling' has entered virtually every major language as a metaphor for hidden potential, the outsider who turns out to be exceptional, and the suffering that precedes transformation — one of the most pervasive fairy tale metaphors in world culture, applied in personal development, talent discovery, sports, business, and national identity narratives.",
      "The Ugly Duckling's influence on the narrative of individual artistic and personal development has been extraordinary — the tale provides the archetypal structure for the artist's bildungsroman (the misunderstood, suffering artist who is ultimately revealed as a genius), applied in literary and biographical narratives across cultures.",
      "The critique of the Ugly Duckling's implicit ideology — that the ugly duckling's transformation is a discovery of innate superiority rather than earned transformation — has generated significant scholarly analysis of the tale as a conservative fantasy of natural aristocracy, adding analytical depth to what appears to be a simple children's story."
    ],
    "relationships": [
      {"sourceSlug": "hans-christian-andersen", "sourceName": "Hans Christian Andersen (1805–1875, autobiographical tale — poor cobbler's son to celebrated writer)", "verb": "AUTHORS", "targetSlug": "the-ugly-duckling", "targetName": "The Ugly Duckling (1843 — most autobiographical of Andersen's fairy tales)", "context": "Andersen published The Ugly Duckling in November 1843 — the tale is explicitly autobiographical, reflecting his own experience of poverty, social marginalisation, and eventual literary fame."},
      {"sourceSlug": "the-ugly-duckling", "sourceName": "The Ugly Duckling (hidden potential, outsider revealed as exceptional — universal metaphor)", "verb": "PROVIDES_METAPHOR_FOR", "targetSlug": "hidden-potential-narrative", "targetName": "Hidden potential narrative (personal development, talent discovery, bildungsroman)", "context": "'The ugly duckling' has become one of the most universally applied metaphors in world culture — used in personal development, talent discovery, and the artist's bildungsroman narrative."},
      {"sourceSlug": "the-ugly-duckling", "sourceName": "The Ugly Duckling (innate superiority vs. earned transformation — conservative fantasy critique)", "verb": "CRITIQUED_AS", "targetSlug": "natural-aristocracy-ideology", "targetName": "Natural aristocracy ideology (innate superiority vs. democratic self-improvement)", "context": "Scholars have critiqued the Ugly Duckling's implicit ideology — the transformation is a discovery of innate aristocratic nature (swans as royal birds), not earned change, positioning the tale as a conservative fantasy of natural superiority."}
    ],
    "places": [
      {"name": "Denmark (Odense — Andersen's birthplace and childhood; Danish farm and court context)", "role": "The Ugly Duckling is set in a Danish farm context — reflecting Andersen's Odense childhood and the Danish social hierarchy that shaped the tale's dynamics of social exclusion and transformation"},
      {"name": "Global (virtually every language — 'ugly duckling' as universal metaphor; personal development culture)", "role": "The ugly duckling metaphor has entered virtually every major language — one of the most pervasive fairy tale metaphors in global personal development, sports, business, and national identity narratives"}
    ],
    "subjects": ["Danish Literature", "19th Century", "Fairy Tale", "Hans Christian Andersen", "Autobiography", "Folk Literature", "Children's Literature", "Metaphor"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Ugly Duckling (Andersen, 1843) is one of Andersen's most autobiographical and universally resonant tales — the metaphor of the ugly duckling who becomes a swan has entered virtually every major language as a phrase for hidden potential and the suffering that precedes transformation. Its application across personal development, talent discovery, and artistic biography makes it one of the most practically cited fairy tales in world culture.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-little-match-girl": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-little-match-girl.json",
  "slug": "the-little-match-girl",
  "data": {
    "summary": "The Little Match Girl (Danish: Den lille pige med svovlstikkerne, 'The Little Girl with the Matches') is a fairy tale by Hans Christian Andersen (1805–1875), first published on 18 December 1845 in the third volume of the collected Eventyr ('Fairy Tales'), alongside The Fir Tree and The Snow Queen. The tale narrates the story of a poor little girl who, on New Year's Eve, freezes to death on the streets while striking matches to warm herself — each match illuminates a brief vision of warmth and comfort (a roaring stove, a table set with roast goose, a Christmas tree, and finally her deceased grandmother, the only person who had ever been kind to her) before the flame dies and the cold returns. In the final vision, her grandmother carries her to heaven, where she will no longer be cold or hungry.\n\nThe Little Match Girl is one of the bleakest and most emotionally powerful of all Andersen's tales — unlike most fairy tales, it offers no rescue, no transformation, no prince, no happy ending: the child dies of cold and hunger on a city street on New Year's Eve while wealthy citizens celebrate inside. The tale has been analysed as a social critique of 19th-century poverty and urban inequality (the gap between the warm, prosperous households visible through the windows and the frozen, starving child outside), as a religious fantasy of heavenly consolation for earthly suffering, and as a document of Andersen's own complex relationship with poverty and death.\n\nThe Little Match Girl has become one of the most widely adapted fairy tales in world culture — adapted for stage, film, opera, and television in dozens of countries, and cited in discussions of child poverty, social inequality, and the limits of religious consolation. The image of the little girl striking her matches in the cold is one of the most powerful images in European children's literature, and the tale's emotional directness has made it one of the most frequently cited examples of Andersen's genius.",
    "causes": [
      "The social conditions of 19th-century Copenhagen — the severe poverty of the urban poor, the sharp contrast between the wealth of the bourgeoisie and the suffering of street children on New Year's Eve — provided the social context for the tale, which Andersen described as inspired by a picture of a poor girl trying to warm herself with matches.",
      "Andersen's personal experience of poverty and his complex relationship with death — his childhood in extreme poverty in Odense, his repeated proximity to death in his fiction, and his religious faith that death was a passage to a better world — shaped the tale's combination of social realism and religious consolation.",
      "The 19th-century tradition of literary sentimentalism — the use of the suffering child as a vehicle for social critique and emotional effect (Dickens's Oliver Twist, Little Nell in The Old Curiosity Shop) — provided the cultural context for Andersen's tale, which is among the most powerful examples of this tradition."
    ],
    "effects": [
      "The Little Match Girl has been adapted in dozens of stage, film, opera, and television productions worldwide — its combination of social realism, emotional power, and spiritual consolation makes it one of the most theatrically and cinematically productive of all Andersen's tales.",
      "The tale is cited in discussions of child poverty and social inequality as a literary archetype of the suffering poor child — the image of the freezing child looking in at warmth from outside has become one of the most powerful symbols of social exclusion and inequality in European literary culture.",
      "The Little Match Girl's religious consolation — the grandmother's ascent to heaven — has made it a subject of theological analysis and critique, positioned at the intersection of social critique and religious fantasy: the tale simultaneously criticises the social conditions that kill the child and offers a heavenly escape that relieves the pressure for social change."
    ],
    "relationships": [
      {"sourceSlug": "hans-christian-andersen", "sourceName": "Hans Christian Andersen (1805–1875, social critique and religious consolation)", "verb": "AUTHORS", "targetSlug": "the-little-match-girl", "targetName": "The Little Match Girl (1845 — child dies of cold and hunger; heavenly consolation)", "context": "Andersen published The Little Match Girl in December 1845 — one of his bleakest tales, in which a poor child freezes to death on New Year's Eve with no rescue, only a vision of heaven."},
      {"sourceSlug": "the-little-match-girl", "sourceName": "The Little Match Girl (social critique — poverty, urban inequality; bourgeois warmth vs. frozen child)", "verb": "CRITIQUES", "targetSlug": "19th-century-urban-poverty", "targetName": "19th-century urban poverty (Copenhagen — child poverty, social inequality)", "context": "The Little Match Girl critiques 19th-century urban poverty — the contrast between wealthy households and the freezing child outside has become a literary archetype of social exclusion and inequality."},
      {"sourceSlug": "the-little-match-girl", "sourceName": "The Little Match Girl (suffering child — Dickens, sentimentalism; social realism tradition)", "verb": "BELONGS_TO", "targetSlug": "literary-sentimentalism", "targetName": "19th-century literary sentimentalism (Dickens — Oliver Twist, Little Nell; suffering child archetype)", "context": "The Little Match Girl belongs to the 19th-century tradition of literary sentimentalism — the suffering child as a vehicle for social critique and emotional effect, alongside Dickens's Oliver Twist and Little Nell."}
    ],
    "places": [
      {"name": "Copenhagen, Denmark (New Year's Eve — frozen streets; wealthy households visible from outside)", "role": "The Little Match Girl is set on the frozen streets of Copenhagen on New Year's Eve — Andersen's personal experience of Danish poverty and the sharp urban contrast between wealth and poverty shaped the tale"},
      {"name": "Global (theatrical, cinematic, operatic adaptations — dozens of countries; social inequality discourse)", "role": "The Little Match Girl has been adapted worldwide in stage, film, and opera — its image of the freezing child has become a universal symbol of social exclusion cited in global discussions of child poverty"}
    ],
    "subjects": ["Danish Literature", "19th Century", "Fairy Tale", "Hans Christian Andersen", "Social Critique", "Child Poverty", "Folk Literature", "Children's Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Little Match Girl (Andersen, 1845) is one of the most emotionally powerful and socially acute of all fairy tales — a child dies of cold and hunger with no rescue, only a vision of heaven. Its image of the freezing child looking in at warmth from outside has become a universal symbol of social exclusion and poverty; its dozens of theatrical, cinematic, and operatic adaptations demonstrate its enduring emotional and cultural power.",
      "significanceCategory": "highly-significant"
    }
  }
},

"thumbelina": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780thumbelina.json",
  "slug": "thumbelina",
  "data": {
    "summary": "Thumbelina (Danish: Tommelise, 'Thumbelina' or 'Thumb Elisa') is a fairy tale by Hans Christian Andersen (1805–1875), first published on 16 December 1835 in the first volume of Eventyr fortalte for Børn ('Fairy Tales Told for Children'), alongside The Tinderbox, Little Claus and Big Claus, and The Princess on the Pea — Andersen's very first published fairy tale collection. The tale narrates the story of a tiny girl, no bigger than a thumb, who is born from a flower seed given to a childless woman by an old witch — kidnapped by a toad who wants her as a bride for her son, she escapes, is adopted by a field mouse, is almost forced to marry a blind mole, is rescued by the swallow she tended through the winter, and is carried to the warm land of flowers, where she meets the tiny flower-king, Prince Cornelius (or 'Flower Fairy'), who becomes her husband.\n\nThumbelina is one of Andersen's most original creations — unlike most of his other tales, it has no clear folk tale precursor and is largely Andersen's own invention, drawing on the European literary tradition of tiny humans (Lilliputians, Tom Thumb) and on his own imagination. The tale has been analysed as a narrative of female autonomy and social pressure — Thumbelina is repeatedly subjected to the desires of larger creatures (the toad, the mole) who want to use her for their purposes, and her journey ends only when she finds a world (the flower world) where she is the right size — as well as a fantasy of the artist's need for a sympathetic environment.\n\nThumbelina is one of Andersen's most frequently adapted tales — its charming protagonist, its series of colourful episodes, and its themes of smallness and belonging have made it a favourite for theatrical, operatic, and cinematic adaptation. The most widely seen adaptation is Don Bluth's animated film Thumbelina (1994), and the tale has generated numerous illustrated editions and literary retellings in the 20th and 21st centuries.",
    "causes": [
      "Andersen's creative imagination — Thumbelina is largely Andersen's original creation, with no clear folk tale precursor, drawing on the European literary tradition of tiny humans (Tom Thumb, Lilliputians in Swift's Gulliver's Travels) and on his gift for episodic adventure narrative.",
      "The European literary tradition of tiny humans — from Tom Thumb (English, French, German folk tales) through Swift's Lilliputians (1726) — provided the cultural archetype of the tiny human in an oversized world that Andersen transformed into his own distinctive fairy tale.",
      "Andersen's personal social experience — his sense of being too small for the social world he inhabited, his need for an environment where his gifts would be recognised and valued — has been read into Thumbelina's search for a world where she is the right size, making the tale one of his most personal creations."
    ],
    "effects": [
      "Thumbelina established the tiny, isolated female protagonist as a fairy tale archetype — a figure who must navigate a world that is too large, too threatening, and too socially demanding, finding belonging only when she discovers a community sized for her — influencing subsequent children's fantasy narratives.",
      "Thumbelina has generated numerous stage, opera, and film adaptations — the tale's episodic structure (the toad, the field mouse, the mole, the swallow) provides a natural narrative arc for theatrical and cinematic adaptation, and its themes of smallness and belonging resonate with child audiences.",
      "The tale's feminist reading — Thumbelina as a figure of female autonomy repeatedly subjected to the desires of larger creatures who want to control her, finding liberation only in a world of equals — has made it a subject of feminist fairy tale analysis alongside The Little Mermaid and The Wild Swans."
    ],
    "relationships": [
      {"sourceSlug": "hans-christian-andersen", "sourceName": "Hans Christian Andersen (1805–1875 — Thumbelina largely original creation, no folk precursor)", "verb": "AUTHORS", "targetSlug": "thumbelina", "targetName": "Thumbelina (1835 — Andersen's first published fairy tale volume; tiny girl seeking belonging)", "context": "Andersen published Thumbelina in December 1835 in his first fairy tale volume — largely an original creation, drawing on the European tradition of tiny humans and on his own experience of social displacement."},
      {"sourceSlug": "thumbelina", "sourceName": "Thumbelina (tiny protagonist in oversized world — Tom Thumb, Lilliputians literary tradition)", "verb": "EXTENDS", "targetSlug": "tiny-human-literary-tradition", "targetName": "Tiny human literary tradition (Tom Thumb, Lilliputians — Gulliver's Travels 1726)", "context": "Thumbelina extends the European literary tradition of tiny humans — transforming the Tom Thumb / Lilliputian archetype into Andersen's distinctively personal fairy tale of a tiny girl seeking a world sized for her."},
      {"sourceSlug": "thumbelina", "sourceName": "Thumbelina (female autonomy — toad, mole; feminist fairy tale analysis)", "verb": "EXAMINED_BY", "targetSlug": "feminist-fairy-tale-criticism", "targetName": "Feminist fairy tale criticism (female autonomy, social pressure — Andersen's tales)", "context": "Feminist critics have analysed Thumbelina as a narrative of female autonomy — the protagonist is repeatedly subjected to the desires of larger creatures who want to control her, finding liberation only in a world of equals."}
    ],
    "places": [
      {"name": "Denmark (Andersen's imagination — first fairy tale volume, December 1835; no specific geography)", "role": "Thumbelina was published in December 1835 in Andersen's first fairy tale volume — largely an original creation without specific geographic setting, reflecting Andersen's personal sense of social displacement"},
      {"name": "Global (theatrical, operatic, cinematic adaptations — Don Bluth 1994; widely illustrated)", "role": "Thumbelina has been adapted worldwide in stage, opera, and film — the most widely seen adaptation is Don Bluth's animated film (1994), and the tale has generated numerous illustrated editions globally"}
    ],
    "subjects": ["Danish Literature", "19th Century", "Fairy Tale", "Hans Christian Andersen", "Children's Literature", "Fantasy", "Folk Literature", "Female Protagonist"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Thumbelina (Andersen, 1835) is one of Andersen's most charming and original fairy tales — largely his own creation, the tale of a tiny girl seeking a world sized for her has been adapted in stage, opera, and film worldwide. Its feminist reading as a narrative of female autonomy resisting social pressure and its place in the European tradition of tiny human stories give it enduring literary and critical interest.",
      "significanceCategory": "significant"
    }
  }
},

"the-cat-in-the-hat": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-cat-in-the-hat.json",
  "slug": "the-cat-in-the-hat",
  "data": {
    "summary": "The Cat in the Hat is a children's picture book by the American author and illustrator Theodor Seuss Geisel (Dr. Seuss, 1904–1991), published by Random House on 12 March 1957, and one of the most important and influential books in the history of children's literacy education. The Cat in the Hat was written in direct response to a 1954 Life magazine article by John Hersey (and a subsequent article in The Atlantic by Rudolf Flesch, 'Why Johnny Can't Read') that criticised the 'Dick and Jane' primers used to teach reading as boring and educationally ineffective — Bennett Cerf and William Spaulding of Houghton Mifflin challenged Seuss to write a compelling children's reader using only 220 specific words from the first-grade vocabulary list, and Seuss produced the book using only 236 words.\n\nThe Cat in the Hat narrates the story of a wet, boring Saturday afternoon in which two bored children are visited by a tall anthropomorphic cat wearing a hat who introduces chaos, fun, and mess into their ordered household — accompanied by two mischievous Things (Thing One and Thing Two) — before cleaning everything up perfectly just before their mother returns home. The book's combination of simple vocabulary, rhythmic verse, anarchic humour, and vivid illustration created a reading experience so compelling that children actively wanted to read it — making it both a revolution in reading instruction methodology and a perennial bestseller (over 10 million copies sold).\n\nThe Cat in the Hat transformed the children's book market and reading instruction — its success created the 'Beginner Books' division of Random House (beginning readers series), influenced the development of literacy materials globally, and established Dr. Seuss as the most commercially successful and culturally influential author of children's books in the 20th century. The Cat in the Hat's influence on American childhood and literacy education for the last 70 years is virtually without parallel.",
    "causes": [
      "The 1954–1955 reading crisis debates in American education — articles by John Hersey (Life, 1954) and Rudolf Flesch (Why Johnny Can't Read, 1955) criticising the boring, ineffective 'Dick and Jane' primers — created the educational demand for a more engaging beginning reader, and the challenge from Bennett Cerf and William Spaulding to write a compelling book using only 220 first-grade vocabulary words directly produced The Cat in the Hat.",
      "Dr. Seuss's creative approach — his combination of anarchic humour, rhythmic verse, and vivid illustration — provided the means to create a compelling reading experience within the severe vocabulary constraint, demonstrating that educational effectiveness and creative delight were not mutually exclusive.",
      "The post-war American middle-class anxiety about education — the Cold War context (Sputnik, 1957, was launched in October of the same year as the book's publication) and the growing national concern about educational achievement — created a receptive market for a book that promised to solve the reading problem in American primary schools."
    ],
    "effects": [
      "The Cat in the Hat transformed American reading instruction — its commercial success (selling over 10 million copies) demonstrated that beginning readers could be both educationally effective and genuinely engaging, inspiring a generation of 'Beginner Books' and beginning reader series that permanently changed literacy education materials.",
      "Dr. Seuss's Cat in the Hat created the Beginner Books division of Random House (1958), which published the first reader series — a direct institutional consequence of the book's educational and commercial success that shaped children's publishing for decades.",
      "The Cat in the Hat has become one of the most culturally embedded children's books in American culture — the Cat, Thing One, and Thing Two are among the most recognised figures in American popular culture, the book is cited as the most influential literacy text in 20th-century American education, and it has been adapted in stage productions, animated specials (1971), and feature films."
    ],
    "relationships": [
      {"sourceSlug": "dr-seuss", "sourceName": "Dr. Seuss (Theodor Seuss Geisel, 1904–1991, American author and illustrator)", "verb": "AUTHORS", "targetSlug": "the-cat-in-the-hat", "targetName": "The Cat in the Hat (1957 — 236 words from first-grade vocabulary; revolution in reading instruction)", "context": "Dr. Seuss wrote The Cat in the Hat (1957) in response to the 'Why Johnny Can't Read' educational crisis — using only 236 words to create a compelling beginning reader that transformed literacy education."},
      {"sourceSlug": "the-cat-in-the-hat", "sourceName": "The Cat in the Hat (Beginner Books — Random House 1958; beginning reader series)", "verb": "CREATES", "targetSlug": "beginner-books-random-house", "targetName": "Beginner Books (Random House, 1958 — beginning reader series created by the Cat in the Hat's success)", "context": "The Cat in the Hat's commercial and educational success directly created the Beginner Books division of Random House (1958) — a beginning reader series that permanently shaped children's literacy publishing."},
      {"sourceSlug": "the-cat-in-the-hat", "sourceName": "The Cat in the Hat (Dick and Jane critique — Why Johnny Can't Read, Hersey, Flesch 1954–55)", "verb": "RESPONDS_TO", "targetSlug": "american-reading-instruction-crisis", "targetName": "American reading instruction crisis (Dick and Jane primers — Why Johnny Can't Read, 1955)", "context": "The Cat in the Hat was written in direct response to the 1954–55 critique of American reading instruction — John Hersey's Life article and Flesch's 'Why Johnny Can't Read' challenged Seuss to create a more engaging beginning reader."}
    ],
    "places": [
      {"name": "United States (Random House, New York — published 12 March 1957; American literacy education)", "role": "The Cat in the Hat was published by Random House in New York on 12 March 1957 — written for the American primary school reading curriculum and transforming American literacy education"},
      {"name": "Global (10+ million copies; cultural icon — Thing One and Thing Two; stage and film adaptations)", "role": "The Cat in the Hat has sold over 10 million copies worldwide — the Cat, Thing One, and Thing Two are among the most recognised figures in global popular culture, with stage and film adaptations worldwide"}
    ],
    "subjects": ["American Literature", "20th Century", "Dr. Seuss", "Children's Literature", "Literacy Education", "Picture Books", "Reading Instruction", "Illustrated Books"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Cat in the Hat (Dr. Seuss, 1957) is one of the most important books in the history of children's literacy education — its revolution in beginning reader methodology (compelling vocabulary-controlled text) created the Beginner Books series, sold over 10 million copies, and permanently changed how literacy materials were conceived. Dr. Seuss's cultural impact on 20th-century American childhood is virtually without parallel.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-frog-prince": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-frog-prince.json",
  "slug": "the-frog-prince",
  "data": {
    "summary": "The Frog Prince (German: Der Froschkönig oder der eiserne Heinrich, 'The Frog King, or Iron Henry') is a German fairy tale first published by the Brothers Grimm in Kinder- und Hausmärchen ('Children's and Household Tales') as tale KHM 1 — the very first tale in the Grimm collection — in its first edition (1812). The tale narrates the story of a princess who drops her golden ball into a well; a frog retrieves the ball in exchange for the promise that she will let him eat from her plate, sleep in her bed, and be her companion; the princess reluctantly fulfils the promise but throws the frog against the wall (in the 1812 original) or kisses him (in many later adaptations) — whereupon the frog is transformed into a handsome prince.\n\nThe Frog Prince is classified as ATU type 440 ('The Frog King') and exists in related versions across European, American, and Asian folk traditions. The tale's most famous cultural transformation is from 'throwing the frog against the wall' (the original Grimm version — the violence of the princess's disgust breaks the spell) to 'kissing the frog' (the modern popular version — the princess's willingness to overcome her revulsion) — a shift that fundamentally transforms the moral of the story and demonstrates how fairy tale meanings change in transmission and adaptation.\n\nThe Frog Prince occupies a central position in psychoanalytic fairy tale analysis — Bruno Bettelheim's The Uses of Enchantment (1976) reads the tale as a narrative of adolescent sexual awakening and the princess's need to overcome her revulsion at male sexuality before achieving mature love. The tale's placement as the first tale in the Grimm collection (KHM 1) has been taken to signal its importance as a paradigmatic tale; and its central image — the transformation of the disgusting into the beautiful through the fulfilment of a promise — has made it one of the most analysed of all European fairy tales.",
    "causes": [
      "The European folk tradition of animal-bridegroom tales (ATU type 425, 440) — the narrative of a young woman who must overcome her revulsion at an animal husband to achieve love and transformation — provided the narrative structure from which the Frog Prince emerges, a widespread tradition existing across European, Asian, and American folk cultures.",
      "The Brothers Grimm's collection project — the recording of German folk narratives to establish the German literary tradition — drove the recording of The Frog King from oral informants in 1812 and its placement as the first tale in their collection, signalling its paradigmatic importance.",
      "The subsequent editorial tradition — the Grimm brothers' revision of The Frog King in later editions of the Kinder- und Hausmärchen, and the popular adaptation of 'throwing the frog' to 'kissing the frog' in 20th-century retellings — demonstrates the active role of editors and popular culture in transforming fairy tale meanings."
    ],
    "effects": [
      "'Kiss the frog' has entered the English language as a metaphor for persisting with an unpleasant task or situation in the hope of a rewarding transformation — the phrase is used in business management literature (adapted from the tale) as an instruction to begin with unpleasant tasks.",
      "The Frog Prince's placement as KHM 1 — the first tale in the Grimm collection — has made it a paradigmatic tale for the entire Grimm corpus, analysed as a template for the collection's narrative values: the fulfilment of promises, the transformation of the ugly into the beautiful, and the role of revulsion in narrative.",
      "The Frog Prince is one of the most frequently adapted fairy tales in popular culture — generating stage, film, operatic, and literary adaptations ranging from Terry Gilliam's Time Bandits to Disney's The Princess and the Frog (2009), and serving as the central metaphor in management literature on overcoming reluctance."
    ],
    "relationships": [
      {"sourceSlug": "brothers-grimm", "sourceName": "Brothers Grimm (Jacob 1785–1863 and Wilhelm 1786–1859, Kinder- und Hausmärchen KHM 1, 1812)", "verb": "RECORDS", "targetSlug": "the-frog-prince", "targetName": "The Frog Prince (KHM 1 — first tale in the Grimm collection; 'throw the frog' vs. 'kiss the frog')", "context": "The Brothers Grimm recorded The Frog King as KHM 1 — the very first tale in their Kinder- und Hausmärchen (1812), signalling its paradigmatic importance for the entire collection."},
      {"sourceSlug": "the-frog-prince", "sourceName": "The Frog Prince (Bruno Bettelheim — adolescent sexual awakening; Uses of Enchantment 1976)", "verb": "ANALYSED_BY", "targetSlug": "uses-of-enchantment", "targetName": "The Uses of Enchantment (Bruno Bettelheim, 1976 — psychoanalytic fairy tale analysis)", "context": "Bruno Bettelheim's The Uses of Enchantment (1976) analyses The Frog Prince as a narrative of adolescent sexual awakening — the princess overcoming her revulsion at male sexuality to achieve mature love."},
      {"sourceSlug": "the-frog-prince", "sourceName": "The Frog Prince (kiss the frog — business management metaphor; eat the frog)", "verb": "PROVIDES_METAPHOR_FOR", "targetSlug": "business-management-culture", "targetName": "Business management culture ('kiss the frog', 'eat the frog' — overcoming reluctance)", "context": "'Kiss the frog' and 'eat the frog' (based on the Frog Prince tale) are widely used in business management literature as metaphors for beginning with unpleasant tasks and overcoming reluctance."}
    ],
    "places": [
      {"name": "Germany (Kinder- und Hausmärchen, 1812 — KHM 1; Brothers Grimm; Hessian oral tradition)", "role": "The Frog King was recorded by the Brothers Grimm from German oral informants in 1812 — placed first in the Kinder- und Hausmärchen as KHM 1, signalling its paradigmatic importance"},
      {"name": "Global (ATU 440 — European and American folk tradition; Disney Princess and the Frog 2009)", "role": "The Frog Prince exists across European, American, and Asian folk traditions (ATU 440) — Disney's The Princess and the Frog (2009) is its most widely seen modern adaptation"}
    ],
    "subjects": ["German Literature", "19th Century", "Fairy Tale", "Brothers Grimm", "Folk Literature", "Children's Literature", "Psychoanalysis", "Animal Bridegroom"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Frog Prince (Grimm, KHM 1, 1812) is the first tale in the Grimm collection — its placement signals its paradigmatic importance for European fairy tale culture. Its psychoanalytic analysis (Bettelheim, 1976) and the transformation of 'throw the frog' to 'kiss the frog' demonstrate the active role of interpretation in fairy tale reception; its management metaphors ('kiss/eat the frog') show the tale's remarkable diffusion into business culture.",
      "significanceCategory": "highly-significant"
    }
  }
},

"matilda": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780matilda.json",
  "slug": "matilda",
  "data": {
    "summary": "Matilda is a children's novel by the British author Roald Dahl (1916–1990), illustrated by Quentin Blake, first published by Jonathan Cape in October 1988 — Dahl's penultimate children's novel and one of the best-selling children's books of the late 20th century, having sold over 17 million copies worldwide. The novel narrates the story of Matilda Wormwood, a precociously intelligent and widely read five-year-old girl who is dismissed and neglected by her shallow, television-addicted parents and the bullying headmistress Miss Trunchbull, but is recognised and loved by her teacher Miss Honey — and who develops telekinetic powers that she uses to overthrow the tyrannical Miss Trunchbull and secure a happy future for herself and Miss Honey.\n\nMatilda is a classic example of Dahl's characteristic literary formula: the intelligent, sensitive child protagonist who suffers under the cruelty of brutal adults, develops special powers, and achieves a liberating and often violent revenge against those who oppressed them (Charlie and the Chocolate Factory, James and the Giant Peach). The novel's celebration of reading and intellectual curiosity — Matilda reads voraciously from the public library, consuming Dickens, Hemingway, Steinbeck, and Kipling — made it a book about books, unusual in children's literature, and contributed to its popularity among bookish children and their parents.\n\nMatilda has had an exceptional afterlife in popular culture — it was adapted as a feature film by Danny DeVito (1996) and as a West End and Broadway musical (Matilda the Musical, Royal Shakespeare Company, 2011) — the RSC's Matilda the Musical won seven Olivier Awards and four Tony Awards, and its global tour has played to millions of audiences, making it one of the most successful theatrical adaptations of a children's book in history. Dahl's novel has been particularly influential in children's literature for its celebration of reading as a refuge and liberation, and its unflinching portrait of adult cruelty toward children.",
    "causes": [
      "Roald Dahl's personal experience — his difficult school years (harsh corporal punishment at Repton School), his sense of being misunderstood and underestimated, and his lifelong commitment to children's literature as a vehicle for the child's perspective against adult authority — shaped Matilda's core narrative of the brilliant child suffering under adult oppression.",
      "The tradition of the child genius in English literature — from Jane Eyre (Charlotte Brontë) through David Copperfield (Dickens) to Pippi Longstocking (Astrid Lindgren) — provided the cultural archetype of the gifted, mistreated child who triumphs over adult cruelty that Dahl adapted into his own darkly comic voice.",
      "The late 1980s anxiety about children's education and reading — the concern about television's displacement of reading as children's primary leisure activity (embodied in Matilda's television-addicted parents) — gave the novel a specific cultural resonance as a polemic for reading and intellectual curiosity against passive media consumption."
    ],
    "effects": [
      "Matilda has sold over 17 million copies worldwide and remains one of the most read children's books in British and American school curricula — its celebration of reading and intellectual curiosity has made it a foundational text for promoting literacy, frequently cited as a book that inspired a love of reading in children.",
      "Matilda the Musical (Royal Shakespeare Company, 2011) won seven Olivier Awards and four Tony Awards — one of the most acclaimed musical theatre productions of the 21st century, with a global tour that has played to millions of audiences and established Matilda as a major theatrical franchise.",
      "Matilda's portrait of the brilliant, mistreated child who triumphs over adult cruelty has been enormously influential on subsequent children's literature — its formula (special child, brutal adults, liberating revenge) is echoed in the Harry Potter series and other children's fantasy novels, and it validated a darker, more unsentimental approach to children's fiction."
    ],
    "relationships": [
      {"sourceSlug": "roald-dahl", "sourceName": "Roald Dahl (1916–1990, British children's author — Matilda his penultimate novel)", "verb": "AUTHORS", "targetSlug": "matilda", "targetName": "Matilda (1988 — brilliant child, telekinesis, Miss Trunchbull; 17 million copies sold)", "context": "Dahl published Matilda in 1988 — one of his final children's novels, celebrating reading and intellectual curiosity and his characteristic formula of the sensitive child triumphing over brutal adults."},
      {"sourceSlug": "matilda", "sourceName": "Matilda (RSC Matilda the Musical — 7 Olivier Awards, 4 Tony Awards; global tour)", "verb": "ADAPTED_AS", "targetSlug": "matilda-the-musical", "targetName": "Matilda the Musical (RSC, 2011 — 7 Olivier Awards, 4 Tony Awards; global tour)", "context": "The Royal Shakespeare Company's Matilda the Musical (2011) won seven Olivier Awards and four Tony Awards — one of the most acclaimed and commercially successful musical theatre adaptations of a children's book in history."},
      {"sourceSlug": "matilda", "sourceName": "Matilda (reading as refuge — Dickens, Hemingway, Steinbeck in the library; anti-television)", "verb": "ADVOCATES_FOR", "targetSlug": "reading-and-literacy", "targetName": "Reading and literacy (children's literature as advocacy for intellectual curiosity)", "context": "Matilda's celebration of reading — the girl who consumes Dickens, Hemingway, and Steinbeck from the public library — made it a polemic for reading and intellectual curiosity against passive media consumption, frequently cited as a book that inspired children to read."}
    ],
    "places": [
      {"name": "United Kingdom (Jonathan Cape, London — October 1988; RSC Matilda the Musical 2011)", "role": "Matilda was published by Jonathan Cape in London in October 1988 — the RSC's Matilda the Musical (2011) opened at the Cambridge Theatre in the West End, becoming a major theatrical institution"},
      {"name": "Global (17 million copies — school curricula in UK and US; Danny DeVito film 1996; global musical tour)", "role": "Matilda has sold 17 million copies worldwide, is widely taught in UK and US school curricula, and the global tour of Matilda the Musical has played to millions of audiences across multiple continents"}
    ],
    "subjects": ["British Literature", "20th Century", "Roald Dahl", "Children's Literature", "Reading Advocacy", "Musical Theatre", "Child Protagonist", "Fantasy Fiction"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Matilda (Roald Dahl, 1988) is one of the most beloved and commercially successful children's novels of the late 20th century — its celebration of reading and intellectual curiosity has made it a foundational literacy text, and the RSC's Matilda the Musical (2011, seven Olivier Awards, four Tony Awards) is one of the most acclaimed theatrical adaptations of a children's book in history.",
      "significanceCategory": "highly-significant"
    }
  }
},

"the-ants-and-the-grasshopper": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-ants-and-the-grasshopper.json",
  "slug": "the-ants-and-the-grasshopper",
  "data": {
    "summary": "The Ant and the Grasshopper (or The Ants and the Grasshopper) is one of the most famous fables attributed to Aesop (c. 620–564 BCE), recorded in the Aesopic corpus (Perry Index no. 373) and one of the foundational texts of the Western moral tradition. The fable narrates the story of a grasshopper who spends the summer months singing and enjoying himself, while the ants spend the same months gathering and storing food for winter — when winter arrives, the grasshopper is starving and begs the ants for food, but they refuse, asking what he was doing all summer; he replies that he was singing, and they reply that if he sang all summer, he can dance all winter.\n\nThe fable is the Western tradition's most concise expression of the morality of industriousness, prudence, and the virtue of preparing for the future — the moral 'it is best to prepare for the days of necessity' (Perry's version) or 'one must work in summer to eat in winter' establishes the ant as an archetype of virtuous industry and the grasshopper as an archetype of improvident pleasure-seeking. The fable is one of the earliest and most widely distributed in the Aesopic corpus — versions appear in Babrius (1st century CE) and Phaedrus (1st century CE), and it was well known in the ancient Greek world as one of the paradigmatic Aesopic fables.\n\nThe Ant and the Grasshopper has been reworked and contested throughout Western history — La Fontaine's version (La Cigale et la Fourmi, 1668) is the best-known French version; Bramwell Fletcher's political readings and Somerset Maugham's short story 'The Ant and the Grasshopper' (1924) contested the moral by sympathising with the grasshopper's pleasure-seeking against the ants' joyless industry; and in contemporary political discourse the fable is cited in debates about welfare policy (the ants as the tax-paying productive workers, the grasshopper as the undeserving poor who did not plan ahead). The fable's political valence has been repeatedly contested and reversed, demonstrating the continuing ideological power of its simple opposition.",
    "causes": [
      "The Greek oral fable tradition attributed to Aesop (c. 620–564 BCE) — the tradition of short animal tales with explicit moral conclusions, used as proverbial wisdom and rhetorical examples in Greek education and oratory — produced the Ant and Grasshopper fable as one of the paradigmatic examples of prudent industry against improvident pleasure.",
      "The ancient Greek agricultural calendar — the crucial importance of summer preparation (harvesting, storing grain) for winter survival in the Mediterranean agricultural cycle — made the fable's contrast between summer industry and winter hunger a vivid and immediately comprehensible moral lesson.",
      "The transmission of the Aesopic corpus through Babrius, Phaedrus, and the Byzantine Aesop collections — and the integration of Aesop's fables into European primary education through the medieval and Renaissance periods — ensured the continuous transmission and cultural embedding of the Ant and Grasshopper fable in Western moral culture."
    ],
    "effects": [
      "The Ant and the Grasshopper established the ant as the archetype of industrious virtue and the grasshopper as the archetype of improvident pleasure-seeking in Western moral culture — an opposition that has structured moral discourse about work, saving, and prudence from ancient Greece to contemporary welfare policy debates.",
      "La Fontaine's version (La Cigale et la Fourmi, 1668) — the best-known French version of the fable — became the paradigmatic text of the genre in French literature, making the fable a foundational element of French primary education and a central reference in French moral and political discourse.",
      "The fable's citation in contemporary political discourse about welfare policy — the ants as the productive, tax-paying workers versus the grasshopper as the undeserving recipient who failed to plan ahead — demonstrates the remarkable longevity of the fable's political valence and its continued use as a template for arguments about individual responsibility versus collective obligation."
    ],
    "relationships": [
      {"sourceSlug": "aesop", "sourceName": "Aesop (c. 620–564 BCE, Greek fabulist — oral tradition; Perry Index 373)", "verb": "AUTHORS", "targetSlug": "the-ants-and-the-grasshopper", "targetName": "The Ant and the Grasshopper (Aesopic fable, Perry Index 373 — industriousness vs. improvidence)", "context": "The Ant and the Grasshopper is attributed to Aesop (c. 620–564 BCE) in the Aesopic corpus — one of the paradigmatic Aesopic fables establishing the ant as an archetype of virtuous industry."},
      {"sourceSlug": "the-ants-and-the-grasshopper", "sourceName": "The Ant and the Grasshopper (La Fontaine — La Cigale et la Fourmi 1668; French primary education)", "verb": "ADAPTED_BY", "targetSlug": "jean-de-la-fontaine", "targetName": "Jean de La Fontaine (La Cigale et la Fourmi, Fables 1668 — best-known French version)", "context": "La Fontaine's La Cigale et la Fourmi (1668) is the best-known French version of the fable — a foundational text of French primary education and the paradigmatic example of the fable genre in French literature."},
      {"sourceSlug": "the-ants-and-the-grasshopper", "sourceName": "The Ant and the Grasshopper (welfare policy — ants as productive workers, grasshopper as undeserving poor)", "verb": "CITED_IN", "targetSlug": "welfare-policy-debate", "targetName": "Welfare policy debate (individual responsibility vs. collective obligation — political discourse)", "context": "The Ant and the Grasshopper is cited in contemporary welfare policy debates — the ants as productive tax-payers versus the grasshopper as the undeserving recipient who failed to plan ahead, demonstrating the fable's continuing political valence."}
    ],
    "places": [
      {"name": "Ancient Greece (Aesopic oral tradition, c. 620–564 BCE; Mediterranean agricultural cycle)", "role": "The Ant and Grasshopper fable emerged from the Aesopic oral tradition in ancient Greece — the agricultural significance of summer preparation for winter survival made the fable's moral immediately comprehensible"},
      {"name": "France (La Fontaine's La Cigale et la Fourmi, 1668 — French primary education; paradigmatic French fable)", "role": "La Fontaine's version (1668) became the paradigmatic French version of the fable — a foundational text of French primary education and a central reference in French moral and political discourse"}
    ],
    "subjects": ["Ancient Greek Literature", "Ancient Era", "Aesop", "Fable", "Moral Philosophy", "Folk Literature", "Political Philosophy", "La Fontaine"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Ant and the Grasshopper (Aesop, c. 6th century BCE; Perry Index 373) is one of the most widely distributed fables in Western moral tradition — establishing the ant as an archetype of industrious virtue and the grasshopper as improvident pleasure-seeking. La Fontaine's version (1668) became the paradigmatic French text; its citation in welfare policy debates demonstrates the remarkable longevity of the fable's political valence across 2,500 years.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-boy-who-cried-wolf": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-boy-who-cried-wolf.json",
  "slug": "the-boy-who-cried-wolf",
  "data": {
    "summary": "The Boy Who Cried Wolf (also 'The Shepherd Boy and the Wolf') is one of the most famous fables attributed to Aesop (c. 620–564 BCE), recorded in the Aesopic corpus (Perry Index no. 210) and one of the most widely known fables in the world. The fable narrates the story of a shepherd boy who, bored while watching his flock, repeatedly cries 'Wolf! Wolf!' to alarm the villagers, who come running to help — only to find no wolf and the boy laughing. When a wolf actually does come and the boy cries wolf again, the villagers no longer believe him and do not come; the wolf kills the sheep (and in some versions, the boy).\n\nThe fable is the Western tradition's most concise expression of the consequences of dishonesty and the destruction of trust through repeated false alarms — the moral 'nobody believes a liar even when he tells the truth' establishes a foundational principle of social epistemology: that credibility is a finite resource that is destroyed by repeated deception, and that the consequences of destroyed credibility can be fatal. The fable is one of the earliest and most widely distributed in the Aesopic corpus — it was known in the ancient Greek world and was transmitted through Babrius, Phaedrus, and the medieval Aesop collections.\n\nThe Boy Who Cried Wolf has entered the English language as an idiom — 'to cry wolf' means to raise a false alarm — and is one of the most widely cited fables in discussions of credibility, trust, and the consequences of dishonesty in individual, organisational, and political contexts. The fable is used in discussions of media credibility (news outlets that repeatedly raise false alarms lose credibility), political communication (politicians who cry wolf about threats), emergency management (false alarms desensitising populations to real emergencies), and financial markets (analysts who repeatedly predict crashes). Its application across such diverse domains demonstrates the remarkable power of a simple narrative structure to crystallise a fundamental social truth.",
    "causes": [
      "The Greek oral fable tradition attributed to Aesop (c. 620–564 BCE) — the tradition of short animal (or human) tales with explicit moral conclusions used as proverbial wisdom — produced the Boy Who Cried Wolf fable as one of the paradigmatic examples of the social consequences of dishonesty.",
      "The ancient Greek shepherd's social context — the vulnerability of flocks to wolf predation, the collective vigilance required to protect livestock, and the social contract between the shepherd boy and the villagers — made the fable's scenario immediately comprehensible as a violation of the social trust on which collective defence depended.",
      "The transmission of the Aesopic corpus through the ancient and medieval educational tradition — Aesop's fables were used in Greek and Roman primary education as moral exemplars and rhetorical training — ensured the continuous transmission of the fable as a fundamental element of Western moral education."
    ],
    "effects": [
      "'To cry wolf' has entered virtually every major language as an idiom for raising a false alarm — one of the most widely used idiomatic phrases in English and in many other languages, demonstrating the remarkable diffusion of the fable's central insight into ordinary language.",
      "The Boy Who Cried Wolf is the foundational fable for discussions of credibility, trust, and the consequences of false alarms in emergency management, media, political communication, and financial analysis — cited across these domains as the archetypal narrative of how dishonesty destroys the credibility needed for truthful warnings to be effective.",
      "The fable's principle — that credibility is a finite resource destroyed by deception, with potentially fatal consequences — has been formulated in game theory and social epistemology as a fundamental insight about the social value of honesty, connecting a 2,500-year-old fable to contemporary formal theories of trust and signalling."
    ],
    "relationships": [
      {"sourceSlug": "aesop", "sourceName": "Aesop (c. 620–564 BCE, Greek fabulist — oral tradition; Perry Index 210)", "verb": "AUTHORS", "targetSlug": "the-boy-who-cried-wolf", "targetName": "The Boy Who Cried Wolf (Aesopic fable, Perry Index 210 — dishonesty destroys credibility)", "context": "The Boy Who Cried Wolf is attributed to Aesop (c. 620–564 BCE) in the Aesopic corpus — one of the paradigmatic fables establishing the social consequences of dishonesty and false alarms."},
      {"sourceSlug": "the-boy-who-cried-wolf", "sourceName": "The Boy Who Cried Wolf ('cry wolf' idiom — virtually every major language)", "verb": "ESTABLISHES_IDIOM", "targetSlug": "credibility-and-trust", "targetName": "Credibility and trust ('to cry wolf' — false alarm, destroyed trust idiom in global culture)", "context": "'To cry wolf' has entered virtually every major language as an idiom for raising false alarms — demonstrating the remarkable diffusion of the fable's central insight into ordinary language and cultural discourse."},
      {"sourceSlug": "the-boy-who-cried-wolf", "sourceName": "The Boy Who Cried Wolf (emergency management, media, political communication, financial analysis)", "verb": "CITED_IN", "targetSlug": "communication-credibility", "targetName": "Communication credibility (emergency management, media, political communication — false alarm dynamics)", "context": "The Boy Who Cried Wolf is cited across emergency management, media credibility, political communication, and financial analysis as the archetypal narrative of how repeated false alarms destroy the credibility needed for truthful warnings to be effective."}
    ],
    "places": [
      {"name": "Ancient Greece (Aesopic oral tradition, c. 620–564 BCE; shepherd and village social context)", "role": "The Boy Who Cried Wolf emerged from the Aesopic oral tradition in ancient Greece — the shepherd-village social context made the fable's scenario immediately comprehensible as a violation of the social trust on which collective defence depended"},
      {"name": "Global (virtually every language — 'cry wolf' idiom; emergency management, media, politics)", "role": "'Cry wolf' has entered virtually every major language as an idiom — the fable is cited globally in emergency management, media credibility, and political communication discussions"}
    ],
    "subjects": ["Ancient Greek Literature", "Ancient Era", "Aesop", "Fable", "Moral Philosophy", "Folk Literature", "Communication Theory", "Social Epistemology"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Boy Who Cried Wolf (Aesop, c. 6th century BCE; Perry Index 210) is one of the most globally diffused fables in world literature — 'to cry wolf' has entered virtually every major language as an idiom for false alarms. Its principle that dishonesty destroys credibility, with potentially fatal consequences, is cited across emergency management, media, political communication, and game theory, demonstrating the remarkable longevity of a 2,500-year-old fable's moral insight.",
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
