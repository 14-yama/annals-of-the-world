#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 36 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: amesha-spenta, hansel-and-gretel,
          epic-of-jangar, a-storm-of-swords,
          akuaba, armenian-eternity-sign,
          chane-opratoire (chaîne opératoire), formal-concept-analysis
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-36-may2026"

ENRICHMENTS = {

"amesha-spenta": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780amesha-spenta.json",
  "slug": "amesha-spenta",
  "data": {
    "summary": "The Amesha Spenta (Avestan: 𐬀𐬨𐬆𐬱𐬀 𐬯𐬞𐬆𐬧𐬙𐬀, 'Holy/Bounteous Immortals') are the six or seven supreme divine beings in Zoroastrianism — the most ancient Iranian religion, founded by the prophet Zarathustra (Zoroaster) and surviving in the Avesta, the sacred scriptures of Zoroastrianism. The Amesha Spenta (also transliterated as Aməša Spənta) are the principal divine emanations or attributes of Ahura Mazda (the 'Lord of Wisdom', the supreme deity of Zoroastrianism), each embodying a cosmic and ethical principle: Vohu Manah ('Good Mind', associated with cattle/animals), Asha Vahishta ('Best Truth/Righteousness', associated with fire), Khshathra Vairya ('Desirable Dominion', associated with metals/sky), Spenta Armaiti ('Holy Devotion', associated with earth), Haurvatat ('Wholeness/Perfection', associated with water), and Ameretat ('Immortality', associated with plants). Ahura Mazda himself is sometimes counted as the seventh Amesha Spenta.\n\nThe Amesha Spenta are not only cosmic divine powers but also ethical principles that the faithful are called to embody — their veneration is simultaneously cosmic worship and ethical commitment: devotion to Asha Vahishta (Truth/Righteousness) means both worshipping the divine principle of truth and living a life of truthfulness and justice. This fusion of cosmic theology with ethical obligation is characteristic of Zoroastrianism's emphasis on moral choice (the freedom to choose between truth, Asha, and falsehood, Druj) as the basis of the cosmic and moral order. The Amesha Spenta represent the cosmic beneficent powers against the destructive forces of Angra Mainyu (the 'Hostile Spirit', principle of evil, destruction, and falsehood).\n\nThe Amesha Spenta have had significant influence beyond Zoroastrianism itself — scholars have identified structural parallels with the Jewish angelology of the post-exilic period (the Archangels of Judaism: Michael, Gabriel, Raphael, Uriel), with the Platonic divine intermediary tradition, and with the Gnostic aeon theology. The Zoroastrian concept of a supreme deity whose cosmic attributes are hypostatised as semi-divine intermediaries between the divine and the human appears to have influenced Jewish and early Christian theological development during the Achaemenid and Hellenistic periods.",
    "causes": [
      "Zarathustra's theological reform of ancient Iranian polytheism — the transformation of the ancient Iranian divine beings (yazatas) into either cosmic divine principles in service of Ahura Mazda or demonic powers in service of Angra Mainyu — provided the theological context from which the Amesha Spenta emerged: they are the cosmic hypostatisations of Ahura Mazda's supreme divine attributes.",
      "The Achaemenid Persian empire's establishment of Zoroastrianism as the royal religion (6th–4th centuries BCE) — with the Achaemenid kings' inscriptions invoking Ahura Mazda as the supreme deity — created the political and cultural context for the full development of Zoroastrian theology, including the Amesha Spenta as the cosmic divine council of the supreme deity.",
      "The ancient Iranian religious tradition's conception of cosmic dualism — the eternal struggle between the beneficent Ahura Mazda and the destructive Angra Mainyu — provided the theological framework within which the Amesha Spenta function as the principal divine powers of the beneficent cosmic order, embodying the ethical and cosmic principles of truth, righteousness, and wholeness against the forces of falsehood and destruction."
    ],
    "effects": [
      "The Amesha Spenta's conception of a supreme deity's cosmic attributes hypostatised as divine intermediaries appears to have influenced Jewish angelology — particularly the post-exilic archangel tradition (Michael, Gabriel, Raphael, Uriel, Saraqael, Raguel) — during the period of Achaemenid Persian rule over Judea (538–332 BCE), when Jewish theology was in intensive contact with Zoroastrian theological ideas.",
      "The Zoroastrian cosmic dualism of Asha (Truth/Cosmic Order) vs. Druj (Falsehood/Chaos) — with the Amesha Spenta embodying the cosmic principles of truth and goodness — influenced the later development of Manichaeism (the 3rd-century gnostic religion of Mani, which drew on Zoroastrian dualism alongside Buddhist and Christian elements) and Zurvanism.",
      "The Amesha Spenta as cosmic ethical principles — with each divine being representing both a cosmic reality and an ethical obligation — exemplify Zoroastrianism's distinctive fusion of cosmological and ethical thought, which has influenced the comparative study of ancient Iranian religion and the history of religious ethics."
    ],
    "relationships": [
      {"sourceSlug": "amesha-spenta", "sourceName": "Amesha Spenta (six Holy Immortals)", "verb": "PART_OF", "targetSlug": "zoroastrianism", "targetName": "Zoroastrianism (Avesta, Ahura Mazda)", "context": "The Amesha Spenta are the principal divine emanations of Ahura Mazda in Zoroastrianism — the six cosmic and ethical divine principles that embody the beneficent order of truth, righteousness, wholeness, and immortality."},
      {"sourceSlug": "amesha-spenta", "sourceName": "Amesha Spenta (divine intermediaries)", "verb": "INFLUENCES", "targetSlug": "jewish-angelology", "targetName": "Jewish angelology (Archangels, post-exilic period)", "context": "The Amesha Spenta's conception of divine intermediaries hypostatising the supreme deity's attributes appears to have influenced the development of Jewish archangelology during the period of Achaemenid Persian rule over Judea."},
      {"sourceSlug": "amesha-spenta", "sourceName": "Amesha Spenta (cosmic dualism, Asha vs. Druj)", "verb": "EXPRESSED_IN", "targetSlug": "avesta", "targetName": "Avesta (sacred scriptures of Zoroastrianism)", "context": "The Amesha Spenta are described primarily in the Gathas (the oldest texts of the Avesta, attributed to Zarathustra himself) and the Yasna (liturgical texts) — the sacred scriptures that define Zoroastrian theology."}
    ],
    "places": [
      {"name": "Ancient Iran (Avestan culture, Zarathustra's homeland)", "role": "The Amesha Spenta emerge from the ancient Iranian religious tradition — associated with the Avestan-speaking culture of ancient Iran (probably eastern Iran or Central Asia) and the theological reform of Zarathustra"},
      {"name": "Achaemenid Persian Empire (6th–4th centuries BCE, royal Zoroastrianism)", "role": "The Achaemenid Empire — the first great Persian empire — institutionalised Zoroastrianism as the royal religion and created the political and cultural context for the full elaboration of Zoroastrian theology, including the Amesha Spenta"}
    ],
    "subjects": ["Zoroastrianism", "Ancient Era", "Ancient Iranian Religion", "Theology", "Divine Beings", "Avesta", "Comparative Religion", "Ancient Persia"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Amesha Spenta are the six supreme divine beings of Zoroastrianism — the cosmic and ethical principles of the world's oldest surviving monotheistic religion, whose theology of divine intermediaries and cosmic dualism appears to have influenced Jewish angelology during the Achaemenid period. They embody Zoroastrianism's distinctive fusion of cosmological and ethical thought, and their influence on subsequent religious traditions (Judaism, Manichaeism) makes them significant for the comparative history of religion.",
      "significanceCategory": "significant"
    }
  }
},

"hansel-and-gretel": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780hansel-and-gretel.json",
  "slug": "hansel-and-gretel",
  "data": {
    "summary": "Hansel and Gretel (German: Hänsel und Gretel) is one of the most widely known fairy tales in the world, first published by the Brothers Grimm (Jacob Grimm, 1785–1863, and Wilhelm Grimm, 1786–1859) in the first edition of their Kinder- und Hausmärchen (Children's and Household Tales, 1812) as story 15 — and substantially revised in subsequent editions (1819, 1857) to make it more morally suitable for children. The story follows the children Hansel and Gretel, who are abandoned in the forest by their poor father and desperate stepmother, discover a gingerbread house inhabited by a witch who plans to eat them, and outwit and kill the witch, returning home with her treasure. Its core narrative elements — the dangerous forest, the abandoned children, the devouring witch, the clever children's escape — draw on deep-rooted European folk narrative traditions of child abandonment, forest danger, and the triumph of resourcefulness over supernatural threat.\n\nHansel and Gretel is one of the Grimms' canonical tales — part of the core corpus of perhaps 20 tales (alongside Cinderella, Snow White, Rapunzel, Little Red Riding Hood, Sleeping Beauty, Rumpelstiltskin, and The Frog Prince) that constituted the Grimm fairy tale tradition as it entered the global cultural imagination through the 19th and 20th centuries. The tale reflects the social anxieties of early modern German peasant culture — the fear of famine and child abandonment, the terror of the forest as the space outside social order, and the particular fear of the child-devouring witch as embodiment of perverted motherhood — embedded in a narrative structure that moves from vulnerability to empowerment.\n\nThe tale has been subject to extensive psychological, feminist, and cultural interpretation — Bruno Bettelheim's The Uses of Enchantment (1976) interpreted it as a psychological drama of childhood separation anxiety and oedipal conflict; feminist scholars have analysed the witch as an inversion of the maternal figure; and the tale's resonance with the historical experience of childhood deprivation, abandonment, and danger has given it a particular afterlife in Holocaust literature (the forest, the gingerbread house as false shelter, the oven as killing device). Engelbert Humperdinck's opera Hänsel und Gretel (1893) is the most celebrated musical adaptation.",
    "causes": [
      "The Brothers Grimm's collection and publication of oral German folk tales — their project, conceived in the early 19th century, of recovering authentic German folk culture (Volksgeist) from the oral tradition of German-speaking communities — gave Hansel and Gretel its written form: the tale was contributed by the Hassenpflug family, probably originally of French Huguenot origin, and was refined across multiple editions of the Kinder- und Hausmärchen.",
      "The social realities of early modern European peasant life — famine, child abandonment, the terror of the forest as a space of danger and death, the prevalence of stepparents (following high maternal mortality in childbirth) — provided the material substrate from which the tale's narrative anxieties were constructed: Hansel and Gretel is a fantasy working-through of very real threats faced by early modern children.",
      "The European fairy tale tradition's long history of narratives about dangerous supernatural beings (witches, trolls, giants) who threaten children — the cultural reservoir of folk narrative that the Grimms drew on — provided the narrative conventions (the witch in the gingerbread house, the oven) that give the tale its archetypal quality and its resonance across cultures."
    ],
    "effects": [
      "Hansel and Gretel became one of the core texts of the global fairy tale canon — translated into hundreds of languages, adapted in hundreds of film, television, theatrical, and operatic productions, and embedded in the cultural imagination of children worldwide through the Grimm tradition's global dissemination in the 19th–20th centuries.",
      "Engelbert Humperdinck's opera Hänsel und Gretel (1893) — premiered at Weimar under Richard Strauss — became the most performed German opera of the 19th century and the most beloved of all fairy tale operas, introducing the tale to audiences who had encountered it primarily as a children's story and establishing it as a vehicle for serious artistic expression.",
      "The tale's afterlife in Holocaust memory and literature — the oven, the forest, the child-devouring witch — has made Hansel and Gretel a recurring reference point for Holocaust representations, from Anne Michaels' Fugitive Pieces to contemporary visual art, demonstrating the tale's capacity to carry the weight of historical trauma through its archetypal narrative structure."
    ],
    "relationships": [
      {"sourceSlug": "jacob-and-wilhelm-grimm", "sourceName": "Brothers Grimm (Jacob and Wilhelm)", "verb": "PUBLISHES", "targetSlug": "hansel-and-gretel", "targetName": "Hansel and Gretel (Grimm, 1812)", "context": "The Brothers Grimm first published Hansel and Gretel in the 1812 Kinder- und Hausmärchen — collected from the Hassenpflug family — and substantially revised it across subsequent editions to produce the canonical version."},
      {"sourceSlug": "hansel-and-gretel", "sourceName": "Hansel and Gretel (Grimm, 1812)", "verb": "PART_OF", "targetSlug": "grimms-fairy-tales", "targetName": "Grimms' Fairy Tales (Kinder- und Hausmärchen, 1812–1857)", "context": "Hansel and Gretel is one of the canonical tales of the Grimm collection — part of the core corpus of perhaps 20 tales that constituted the Grimm fairy tale tradition as it entered the global cultural imagination."},
      {"sourceSlug": "hansel-and-gretel", "sourceName": "Hansel and Gretel (Hänsel und Gretel)", "verb": "ADAPTED_AS", "targetSlug": "hansel-und-gretel-opera", "targetName": "Hänsel und Gretel (Humperdinck opera, 1893)", "context": "Humperdinck's opera Hänsel und Gretel (1893) — premiered under Richard Strauss — became the most performed German opera of the 19th century and the most celebrated musical adaptation of the Grimm tale."}
    ],
    "places": [
      {"name": "German-speaking Europe (Grimm collection, 1812)", "role": "Hansel and Gretel is set in an archetypal German forest landscape — the dark woodland space of danger and transformation — and was collected by the Grimms from German-speaking oral tradition in the early 19th century"},
      {"name": "Global (translation into hundreds of languages, 19th–21st century)", "role": "The Grimm fairy tales — including Hansel and Gretel — were translated globally throughout the 19th and 20th centuries, making the tale one of the most widely known stories in the world"}
    ],
    "subjects": ["Fairy Tales", "Modern Era", "Brothers Grimm", "German Literature", "Folklore", "Children's Literature", "Oral Tradition", "Cultural Memory"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Hansel and Gretel (Grimm, 1812) is one of the most widely known fairy tales in the world — a canonical text of the Grimm collection that reflects deep-rooted European folk narrative traditions and social anxieties about child abandonment and forest danger. Its operatic adaptation (Humperdinck, 1893), its psychological interpretation (Bettelheim, 1976), and its resonance in Holocaust memory demonstrate its capacity to carry cultural weight across centuries and contexts.",
      "significanceCategory": "significant"
    }
  }
},

"epic-of-jangar": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782epic-of-jangar.json",
  "slug": "epic-of-jangar",
  "data": {
    "summary": "The Epic of Jangar (Kalmyk: Жангр, Zhangar; Mongolian: Жангар, Jangar) is the heroic epic of the Kalmyk people — a Mongolian Buddhist people whose ancestors migrated from the Dzungaria (western Mongolia) region to the lower Volga steppe in the early 17th century — and one of the three great epics of the Mongolian world alongside the Epic of Manas (of the Kyrgyz) and the Epic of Gesar (of the Tibetan/Mongolian world). The Jangar epic centres on the hero Jangar Khan, the ideal ruler of the mythical paradise kingdom of Bumba (also called Bumba-ba), and his twelve paladins (baatyrs, 'heroes') — who together defend the perfect land against external enemies. The paradise of Bumba is characterised by eternal spring, eternal youth (its inhabitants are permanently twenty-five years old), and the absence of death, disease, and suffering — an ideal world whose beauty and perfection gives the heroes their motivation for endless martial devotion.\n\nThe Jangar was performed by specialist bards called Jangarch (or Jangarchi), who memorised and performed the epic's 12–25+ songs (different performers and regions had different collections of songs) in multi-day performances accompanied by the Mongolian lute (tovshur). The oral tradition was first recorded in Russian in the 18th century — Nisan Ubashi (a Kalmyk scholar) recorded part of it in 1804–1805, and the Russian scholar Alexander von Bergmann made the first complete Russian translation in 1866 — and the Kalmyk oral tradition was systematically collected by Russian and Kalmyk scholars in the 19th–20th centuries. The standard Soviet-era canonical text (1978, compiled by Basang Dordzhiev and other scholars) includes 25 songs.\n\nThe Jangar is the primary monument of Kalmyk national literature and cultural identity — the Kalmyk people, decimated in the 18th century and again in the Soviet era (the 1943 deportation of the entire Kalmyk people to Siberia by Stalin, killing approximately 40% of the population), have maintained the Jangar as the central expression of their cultural survival and national heritage. The epic's vision of Bumba, the paradise without death or suffering, has resonated particularly strongly with a people who have repeatedly faced existential threats to their survival.",
    "causes": [
      "The nomadic warrior culture of the Mongolian peoples — the culture of mounted warfare, heroic virtue (bravery, loyalty, martial skill, generosity), and the celebration of the ideal ruler and his heroic companions — provided the cultural substrate from which the Jangar epic crystallised over centuries of oral transmission, reflecting the values and social organisation of the Oirat/Kalmyk steppe confederation.",
      "The Kalmyk migration to the lower Volga steppe (early 17th century) — which established the Kalmyk Khanate in the Russian borderland between European and Asian civilisations — created the historical context for the Jangar as it is known today: a heroic epic that celebrated the ideal of the independent steppe kingdom (Bumba) and the heroic defence of that paradise against external enemies.",
      "Tibetan Buddhism's adoption by the Kalmyk people — which provided the religious framework of the epic's paradise of Bumba (incorporating Buddhist concepts of the pure land and liberation from suffering) — fused the pre-Buddhist steppe heroic tradition with Buddhist metaphysics, creating the distinctive synthesis of martial heroism and Buddhist utopian imagination that characterises the Jangar."
    ],
    "effects": [
      "The Jangar's celebration as the primary national epic of the Kalmyk people — particularly its recognition during the Soviet period (despite the complications of the 1943 deportation) and its 1940 anniversary celebration — made it the cultural symbol of Kalmyk national identity and survival, and it continues to be the central monument of Kalmyk literature.",
      "The Jangarch tradition — the specialist bards who memorised and performed the epic — is one of the last surviving traditions of Central Asian epic oral performance, and the study of Jangarch performance traditions has contributed to the comparative study of Central Asian oral epic alongside the Manas tradition of the Kyrgyz and the Gesar tradition of the Tibetan world.",
      "The Jangar's vision of Bumba — the paradise of eternal spring, eternal youth, and the absence of death — provides a distinctive philosophical dimension to the Mongolian epic tradition: unlike most heroic epics (which are motivated by honour, vengeance, or territorial conquest), the Jangar's heroes fight to maintain a perfect paradise, giving the martial heroism a utopian and metaphysical dimension."
    ],
    "relationships": [
      {"sourceSlug": "epic-of-jangar", "sourceName": "Epic of Jangar (Kalmyk national epic)", "verb": "EMBODIES", "targetSlug": "kalmyk-national-identity", "targetName": "Kalmyk national identity and cultural heritage", "context": "The Jangar is the primary monument of Kalmyk national literature — the central expression of Kalmyk cultural identity, especially after the 1943 deportation decimated the Kalmyk people."},
      {"sourceSlug": "epic-of-jangar", "sourceName": "Epic of Jangar (Jangarch oral tradition)", "verb": "PART_OF", "targetSlug": "central-asian-oral-epic", "targetName": "Central Asian oral epic tradition (Manas, Gesar, Jangar)", "context": "The Jangar is one of the three great epics of the Mongolian/Central Asian world — alongside the Kyrgyz Epic of Manas and the Tibetan/Mongolian Epic of Gesar — and its Jangarch performance tradition is one of the last surviving Central Asian oral epic traditions."},
      {"sourceSlug": "epic-of-jangar", "sourceName": "Epic of Jangar (paradise of Bumba)", "verb": "INFLUENCED_BY", "targetSlug": "tibetan-buddhism", "targetName": "Tibetan Buddhism (pure land, liberation from suffering)", "context": "The Jangar's paradise of Bumba — with its eternal spring, eternal youth, and absence of death — reflects the fusion of Mongolian heroic tradition with Tibetan Buddhist concepts of the pure land and liberation from suffering, creating the distinctive Buddhist-heroic synthesis of the epic."}
    ],
    "places": [
      {"name": "Kalmykia (lower Volga steppe, Russia, Kalmyk homeland)", "role": "The Kalmyk Republic in Russia — on the lower Volga steppe — is the homeland of the Kalmyk people and the primary context for the preservation and performance of the Jangar epic"},
      {"name": "Dzungaria (western Mongolia, Oirat origin)", "role": "The Jangar epic originated with the Oirat Mongolian peoples of Dzungaria (western Mongolia) — ancestors of the Kalmyk who migrated to the Volga steppe in the 17th century — and reflects the steppe heroic culture of the Oirat confederation"}
    ],
    "subjects": ["Kalmyk Literature", "Medieval Era", "Oral Epic", "Mongolian Culture", "Central Asian Literature", "Buddhist Literature", "Nomadic Culture", "Heroic Poetry"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Epic of Jangar is the primary monument of Kalmyk national literature — one of the three great epics of the Mongolian/Central Asian world, alongside the Kyrgyz Epic of Manas and the Tibetan/Mongolian Gesar. Its paradise of Bumba (eternal youth, no death) reflects the fusion of steppe heroic tradition with Tibetan Buddhist utopian imagination. The epic's significance as a symbol of Kalmyk cultural survival — especially after the devastating 1943 Soviet deportation — gives it extraordinary resonance.",
      "significanceCategory": "significant"
    }
  }
},

"a-storm-of-swords": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783a-storm-of-swords.json",
  "slug": "a-storm-of-swords",
  "data": {
    "summary": "A Storm of Swords is the third novel in George R. R. Martin's A Song of Ice and Fire epic fantasy series, published on 8 August 2000 by Bantam Books — widely regarded by fans and critics as the best volume in the series, and the source of the series' most famous narrative event: the Red Wedding (the massacre of Robb Stark, his mother Catelyn Tully-Stark, and the Northern army at the wedding feast of Edmure Tully). With over 10 million copies sold, it is the best-selling volume of the series. A Storm of Swords covers the aftermath of the War of the Five Kings — the deaths of Robb Stark, Renly Baratheon, and Stannis's defeat at Blackwater — while advancing the story of Daenerys Targaryen's conquest of Essos, Jon Snow's experiences beyond the Wall with the wildlings, Tyrion Lannister's survival after the Battle of the Blackwater, and Jaime Lannister's transformation following the loss of his sword hand.\n\nThe Red Wedding — in which Walder Frey and Roose Bolton massacre Robb Stark and his Northern army at the wedding feast under the sacred protection of guest right — is the single most shocking narrative event in the A Song of Ice and Fire series and one of the most famous plot twists in the history of popular fiction. Its combination of narrative misdirection (the apparent security of guest right, the apparent political resolution of the Frey-Tully wedding), the scale of the betrayal, and the deaths of what had been presented as the main protagonist's family — coming after the series had already killed its apparent first protagonist (Ned Stark in book 1) — established Martin's narrative as uniquely willing to subvert the reader's expectations of heroic fantasy. The Red Wedding's HBO adaptation in Season 3 (Episode 9, 'The Rains of Castamere', directed by David Nutter) produced one of the most widely shared collective audience shock reactions in television history.\n\nA Storm of Swords also contains the most concentrated sequence of major character transformations in the series: Jaime Lannister's redemption arc (the Oathbreaker who becomes the Oathkeeper), Arya Stark's journey toward the Faceless Men, Sansa's escape from King's Landing, Joffrey's assassination at his own wedding (the Purple Wedding), and Jon Snow's election as Lord Commander of the Night's Watch. The novel demonstrates Martin's narrative ambition at its fullest: a plot of extraordinary complexity in which no character's arc follows the expected heroic trajectory.",
    "causes": [
      "Martin's deliberate subversion of heroic fantasy conventions — established through the killing of Ned Stark in A Game of Thrones — reached its culmination in A Storm of Swords' Red Wedding: the systematic building of reader investment in Robb Stark's arc (the Young Wolf, the seemingly invincible conqueror) made the betrayal maximally devastating, demonstrating that no character in the series was safe.",
      "The historical precedent of the Black Dinner (Edinburgh, 1440) and the Massacre of Glencoe (1692) — real Scottish historical events in which guests were murdered in violation of the laws of hospitality — provided Martin with the historical model for the Red Wedding, rooting one of fiction's most shocking events in historical precedent.",
      "The complexity of the Wars of the Roses that Martin drew on for A Song of Ice and Fire — in which alliances shifted constantly, betrayals were endemic, and the most powerful lords were frequently destroyed by their own political miscalculations — provided the political model for A Storm of Swords' massive narrative upheaval, in which the entire political landscape of Westeros is transformed in a single volume."
    ],
    "effects": [
      "The Red Wedding — both in the novel and in its HBO adaptation — became one of the most famous plot twists in the history of popular fiction, producing a collective cultural shock reaction (the filmed 'reaction videos' of viewers responding to the Red Wedding episode became a viral phenomenon) and demonstrating that prestige television had the capacity to produce the same narrative impact as a literary plot twist.",
      "A Storm of Swords' subversion of the expected heroic fantasy trajectory — killing the apparent protagonist, destroying the apparent winning side, and refusing all conventional narrative resolution — influenced a generation of fantasy writers and readers, establishing the 'grimdark' subgenre's expectation that heroic narratives should not guarantee the survival or success of their protagonists.",
      "The Purple Wedding (Joffrey's assassination) — the death of the series' primary villain at his own wedding celebration, in the same book as the Red Wedding — produced a deliberate structural irony that demonstrated Martin's mastery of narrative juxtaposition: the readers' relief at Joffrey's death is immediately complicated by the political consequences for Tyrion, who is falsely accused."
    ],
    "relationships": [
      {"sourceSlug": "george-r-r-martin", "sourceName": "George R. R. Martin (born 1948)", "verb": "AUTHORS", "targetSlug": "a-storm-of-swords", "targetName": "A Storm of Swords (2000)", "context": "Martin published A Storm of Swords as the third volume of A Song of Ice and Fire — the most widely praised in the series, containing the Red Wedding and the Purple Wedding, demonstrating his narrative ambition at its fullest."},
      {"sourceSlug": "a-storm-of-swords", "sourceName": "A Storm of Swords (Red Wedding)", "verb": "PART_OF", "targetSlug": "a-song-of-ice-and-fire", "targetName": "A Song of Ice and Fire (Martin series, 1996–)", "context": "A Storm of Swords is the third and most celebrated volume of A Song of Ice and Fire — containing the Red Wedding, one of the most famous plot twists in popular fiction history."},
      {"sourceSlug": "a-storm-of-swords", "sourceName": "A Storm of Swords (Red Wedding, HBO Season 3)", "verb": "ADAPTED_AS", "targetSlug": "game-of-thrones-season-3", "targetName": "Game of Thrones Season 3 (HBO, 2013)", "context": "The Red Wedding was adapted in Game of Thrones Season 3, Episode 9 ('The Rains of Castamere') — producing one of the most widely shared collective audience shock reactions in television history."}
    ],
    "places": [
      {"name": "The Twins (Frey stronghold, site of the Red Wedding)", "role": "The Twins — the castle of Walder Frey at the crossing of the Green Fork of the Trident — is the site of the Red Wedding massacre, one of the most significant locations in A Song of Ice and Fire"},
      {"name": "Westeros (War of the Five Kings aftermath, widespread transformation)", "role": "A Storm of Swords transforms the entire political landscape of Westeros — through the Red Wedding, the Purple Wedding, and the multiple deaths of major characters — making it the volume in which the series' most dramatic narrative upheavals concentrate"}
    ],
    "subjects": ["Fantasy Fiction", "Modern Era", "George R. R. Martin", "Epic Fantasy", "Red Wedding", "21st Century", "American Literature", "Television Adaptation"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "A Storm of Swords (Martin, 2000) is the most acclaimed volume of A Song of Ice and Fire — the source of the Red Wedding, one of the most famous and impactful plot twists in popular fiction history. The Red Wedding's HBO adaptation produced a collective viral shock reaction unprecedented in television history. The novel's systematic subversion of heroic fantasy expectations — killing the apparent winning protagonist — defined the 'grimdark' fantasy tradition.",
      "significanceCategory": "highly-significant"
    }
  }
},

"akuaba": {
  "filepath": "data/appwrite-export/entities/784-Class-784/784akuaba.json",
  "slug": "akuaba",
  "data": {
    "summary": "The Akuaba (Akan: plural Akua'ba or Akuamma; also spelled akua'ba) is a type of carved wooden fertility doll or figurine produced by the Akan peoples of Ghana and Ivory Coast — particularly the Asante (Ashanti), the largest and most powerful of the Akan peoples — used by women wishing to conceive children, to ensure a healthy pregnancy, and to promote the birth of a beautiful child. The akuaba figure is characterised by a distinctive flattened, disk-shaped head (representing ideals of Akan beauty: a high, rounded forehead), a cylindrical or tubular neck adorned with rings, a schematised body with outstretched horizontal arms, and minimal facial features (dot eyes, small nose and mouth). The proportions — large head, small body — reflect both the stylised aesthetic conventions of Akan figurative art and the importance placed on the head (the ti) in Akan cosmology as the seat of the soul and spiritual identity.\n\nAccording to Akan tradition, a woman wishing to conceive would commission an akuaba figure from a specialist carver (okyeame), carry it on her back as she would carry a living child, and treat it with the care due to a real infant — feeding it, adorning it with beads and cloth, and taking it to the shrine of the deity Nyame or the ancestral spirit (obosom) associated with fertility. The akuaba serves as a spiritual intermediary — its treatment as a living child is understood to attract the spiritual force that will make the woman's womb receptive, and its beautiful, well-proportioned form is understood to influence the beauty of the child conceived. After a successful birth, the akuaba would typically be returned to the shrine or kept as a protective object.\n\nAkuaba figures became one of the most widely collected and exhibited examples of African art in Western museums and private collections from the late 19th century onwards — they are among the most recognised symbols of West African art internationally, and their distinctive disk-head form influenced Western avant-garde artists (particularly the primitivist movement of the early 20th century, including Picasso's engagement with African sculpture). The akuaba represents the intersection of Akan spiritual practice, aesthetics, and the global history of African art's reception in the West.",
    "causes": [
      "Akan cosmology and spiritual practice — the Akan belief in the spiritual power of figurative objects consecrated to deities and ancestral spirits as intermediaries between the human and divine worlds — provided the religious context for the akuaba: a consecrated object whose treatment as a living child attracts the spiritual force of fertility.",
      "The Akan aesthetic tradition's emphasis on the idealised head (ti) as the seat of the soul and spiritual identity — and the specific Akan beauty ideals of a high, rounded forehead, a smooth complexion, and well-proportioned features — determined the characteristic disk-head form of the akuaba and its role as a model of beautiful human form to influence the conceived child.",
      "The late 19th-century Western collection of African art — particularly the systematic collection of Akan gold weights, kente textiles, and figurative objects (including akuaba) by European colonial administrators, missionaries, and collectors — brought the akuaba into Western museums and private collections and began its global career as an icon of West African art."
    ],
    "effects": [
      "The akuaba's distinctive disk-head form became one of the most recognised symbols of West African art internationally — exhibited in the British Museum, the Metropolitan Museum of Art, the Musée du Quai Branly, and hundreds of other collections — and its aesthetic influenced Western primitivist artists of the early 20th century who drew on African sculptural conventions.",
      "The akuaba's widespread collection and exhibition contributed to the global recognition of Akan art as a sophisticated aesthetic tradition — the Asante's goldsmithing, kente weaving, and figurative sculpture (including the akuaba) were recognised in the 20th century as among the most accomplished traditions of African visual culture.",
      "The akuaba continues to be produced and used in Ghana and Ivory Coast as a spiritual object and as a marker of Akan cultural identity — its simultaneous existence as a living spiritual practice and as a globally circulating art object makes it a paradigm case for the complexities of African material culture's place in the global art market."
    ],
    "relationships": [
      {"sourceSlug": "akuaba", "sourceName": "Akuaba (Akan fertility figure)", "verb": "PRODUCED_BY", "targetSlug": "asante-people", "targetName": "Asante (Ashanti) people of Ghana", "context": "The akuaba is produced primarily by the Asante (Ashanti) and other Akan peoples of Ghana and Ivory Coast — a carved wooden fertility figure used in spiritual practice to ensure conception and a beautiful child."},
      {"sourceSlug": "akuaba", "sourceName": "Akuaba (disk-head form, Akan aesthetics)", "verb": "INFLUENCES", "targetSlug": "western-primitivism", "targetName": "Western primitivist art movement (Picasso, early 20th century)", "context": "The akuaba's distinctive disk-head form influenced Western primitivist artists of the early 20th century — particularly Picasso and other avant-garde artists who drew on African sculptural conventions in their radical transformation of European visual art."},
      {"sourceSlug": "akuaba", "sourceName": "Akuaba (fertility spiritual practice)", "verb": "REFLECTS", "targetSlug": "akan-cosmology", "targetName": "Akan cosmology (ti, obosom, Nyame)", "context": "The akuaba reflects Akan cosmological beliefs about the spiritual power of consecrated figurative objects — the head (ti) as the seat of the soul, the obosom (deity/ancestral spirit) as intermediary, and the spiritual force of fertility as divinely bestowed."}
    ],
    "places": [
      {"name": "Ghana and Ivory Coast (Akan peoples, production and use)", "role": "The akuaba is produced and used primarily by the Akan peoples of Ghana and Ivory Coast — particularly the Asante — and continues to be a living spiritual practice as well as a globally circulating art object"},
      {"name": "Western museums (British Museum, Metropolitan Museum of Art, global collection)", "role": "Akuaba figures are held in major museum collections worldwide — they are among the most widely collected examples of West African art and have been central to the Western reception of African sculpture as aesthetic tradition"}
    ],
    "subjects": ["African Art", "Pre-Modern Era", "Akan Culture", "Ghanaian History", "Material Culture", "Fertility", "African Religion", "Visual Art"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Akuaba is one of the most widely recognised symbols of West African art internationally — a carved Akan fertility figure whose distinctive disk-head form reflects Akan spiritual practice, cosmology, and beauty aesthetics. Its global collection and exhibition contributed to the recognition of Akan art as a sophisticated tradition, and its form influenced Western primitivist artists of the early 20th century. It represents the intersection of living spiritual practice and global art market circulation.",
      "significanceCategory": "significant"
    }
  }
},

"armenian-eternity-sign": {
  "filepath": "data/appwrite-export/entities/784-Class-784/784armenian-eternity-sign.json",
  "slug": "armenian-eternity-sign",
  "data": {
    "summary": "The Armenian Eternity Sign (Armenian: ԱրArmenian: Արերական նշան, Arekakan nshan; also Khachkar-related symbol, or the Armenian sun wheel) is an ancient curvilinear swastika-like symbol — a rotating wheel or sun wheel composed of curved arms or S-shaped spirals — that appears in Armenian folk art, architecture, manuscript illumination, and khachkars (cross-stones) from the early medieval period onwards, and has been adopted in modern times as a symbol of Armenian national identity, eternity, and cultural continuity. The symbol typically appears as a wheel with four curved, right-angled, or S-shaped arms radiating from a central point, suggesting continuous rotation and the cycle of the sun — its visual form is related to ancient solar symbols found across Eurasia from the Bronze Age onwards, but its specific Armenian elaboration has a distinctive character in the context of medieval Armenian Christian art.\n\nThe Armenian Eternity Sign appears prominently in the decorative carving of medieval Armenian churches (5th–14th centuries), particularly in the carved stone reliefs of the churches of Geghard, Tatev, and Haghpat — UNESCO World Heritage Sites — and in the intricate carved cross-stones (khachkars) that are the most distinctive art form of medieval Armenian Christianity. In this context, the symbol functions as a Christian symbol of eternity, divine infinity, and the solar character of Christ ('Christ as the Sun of Righteousness') — fusing pre-Christian Armenian solar symbolism with Christian theological meaning. The symbol's appearance in the medieval Armenian illuminated manuscript tradition (the Armenian School of miniature painting, 10th–17th centuries) extended its cultural reach across the Armenian diaspora.\n\nIn the post-independence period of Armenia (since 1991), the Armenian Eternity Sign has experienced a significant revival as a marker of Armenian national identity and cultural heritage — appearing on jewellery, textiles, tattoos, and digital design, and used by Armenian diaspora communities worldwide as a symbol of connection to the Armenian homeland and the continuity of Armenian civilisation. The symbol thus serves as both a medieval religious symbol and a contemporary national identity marker.",
    "causes": [
      "The ancient solar symbolism of the Armenian highlands — the pre-Christian tradition of sun veneration among the ancient Armenian and Urartu peoples, reflected in the solar wheel symbols that appear in ancient Armenian rock art and Bronze Age artefacts — provided the cultural substrate from which the Armenian Eternity Sign developed, fusing pre-Christian solar symbolism with medieval Christian theological content.",
      "The Armenian Christian artistic tradition — particularly the medieval khachkar (cross-stone) tradition (9th–14th centuries) and the church stone-carving tradition — provided the artistic context in which the Armenian Eternity Sign was most elaborately developed: the carved stone reliefs of medieval Armenian churches combined the Christian cross with geometric and solar decorative patterns, of which the eternity sign was a central element.",
      "The Armenian national awakening of the 19th century and the renewed emphasis on Armenian cultural heritage following the Genocide of 1915 — which gave Armenian cultural symbols extraordinary weight as markers of identity, survival, and resistance — created the conditions for the Armenian Eternity Sign's revival as a contemporary national identity marker."
    ],
    "effects": [
      "The Armenian Eternity Sign's association with the medieval khachkar tradition — the carved cross-stones that are the most distinctive art form of Armenian Christian civilisation — gave the symbol its primary resonance as a marker of Armenian cultural identity: the khachkar tradition was inscribed on UNESCO's Representative List of the Intangible Cultural Heritage of Humanity in 2010.",
      "The revival of the Armenian Eternity Sign as a contemporary national identity marker — particularly in the post-Soviet period — has made it one of the most widely used Armenian cultural symbols in the diaspora: it appears in Armenian community contexts worldwide as a connection to the homeland and a symbol of the continuity of Armenian civilisation.",
      "The Armenian Eternity Sign's dual character as both a medieval religious symbol and a contemporary national identity marker reflects the broader pattern of Armenia's ancient and medieval cultural heritage (khachkars, illuminated manuscripts, medieval church architecture) serving as the symbolic resources for modern national identity."
    ],
    "relationships": [
      {"sourceSlug": "armenian-eternity-sign", "sourceName": "Armenian Eternity Sign (solar wheel)", "verb": "APPEARS_IN", "targetSlug": "khachkar-tradition", "targetName": "Armenian Khachkar tradition (carved cross-stones)", "context": "The Armenian Eternity Sign appears prominently in the decorative carving of medieval khachkars (cross-stones) — the most distinctive art form of Armenian Christianity — fusing pre-Christian solar symbolism with Christian theology of eternity."},
      {"sourceSlug": "armenian-eternity-sign", "sourceName": "Armenian Eternity Sign (national identity)", "verb": "SYMBOL_OF", "targetSlug": "armenian-national-identity", "targetName": "Armenian national identity and cultural continuity", "context": "In the post-independence period (since 1991), the Armenian Eternity Sign has been adopted as a marker of Armenian national identity — appearing on jewellery, textiles, and digital design in the Armenian diaspora as a symbol of connection to the homeland."},
      {"sourceSlug": "armenian-eternity-sign", "sourceName": "Armenian Eternity Sign (solar symbol)", "verb": "RELATED_TO", "targetSlug": "ancient-solar-symbolism", "targetName": "Ancient solar symbolism (Eurasian Bronze Age)", "context": "The Armenian Eternity Sign belongs to the tradition of ancient solar wheel symbols found across Eurasia from the Bronze Age — its specific Armenian elaboration in medieval Christian art fuses this ancient solar symbolism with Christian theological content."}
    ],
    "places": [
      {"name": "Armenia and historical Armenian highlands (origin and primary context)", "role": "The Armenian Eternity Sign is rooted in the cultural tradition of the Armenian highlands — appearing in ancient rock art, medieval church carving, and khachkars across historical Armenia, including areas now in Turkey, Georgia, and Azerbaijan"},
      {"name": "Armenian diaspora (global contemporary use)", "role": "The Armenian Eternity Sign is used by Armenian diaspora communities worldwide — particularly in Russia, France, Lebanon, the United States, and Australia — as a symbol of cultural identity and connection to the Armenian homeland"}
    ],
    "subjects": ["Armenian Culture", "Medieval Era", "National Symbols", "Armenian Christianity", "Visual Art", "Cultural Identity", "Medieval Art", "Diaspora"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Armenian Eternity Sign is one of the most important symbols of Armenian cultural identity — deeply embedded in the medieval khachkar tradition (UNESCO Intangible Cultural Heritage) and revived in the post-Soviet period as a national identity marker. It fuses pre-Christian solar symbolism with Christian theological content, and its presence in the Armenian diaspora makes it a living symbol of Armenian civilisational continuity and cultural survival.",
      "significanceCategory": "significant"
    }
  }
},

"chane-opratoire": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785chaîne-opératoire.json",
  "slug": "chane-opratoire",
  "data": {
    "summary": "The chaîne opératoire (French: 'operational chain' or 'technical sequence') is a methodological concept in prehistoric archaeology and cognitive archaeology, developed primarily by the French archaeologist André Leroi-Gourhan (1911–1986) in the 1960s–1970s, that describes the entire sequence of technical operations involved in producing an artefact — from the selection of raw materials through the successive stages of manufacture, use, repair, and discard. The concept enables archaeologists to analyse not only the finished artefact but the complete technical process that produced it, recovering the skills, intentions, planning, and cultural transmission involved in prehistoric technology. By analysing the waste products (debitage), cores, and tools in context, archaeologists using the chaîne opératoire approach can reconstruct the mental template (schème opératoire) that organised the technical sequence and the social and cognitive dimensions of ancient technological practice.\n\nLeroi-Gourhan developed the chaîne opératoire in the context of his broader programme of gesture-and-symbol (geste et symbole) anthropology — his interest in the evolution of human technical gesture and cognitive capacity as the material substrate of human culture. The chaîne opératoire was central to his analysis of Palaeolithic stone tool industries and Upper Palaeolithic art, and it became the foundational concept for the study of lithic (stone tool) technology in French prehistoric archaeology. Its application to the Palaeolithic record revealed the extraordinary planning depth and technical sophistication of early modern humans — the Mousterian and Acheulean industries showed levels of technical sequencing that implied significant working memory, planning capacity, and social transmission of technical knowledge.\n\nThe chaîne opératoire has had broad influence beyond lithic analysis — it has been applied to the study of ceramic production, metalworking, textile manufacture, and other craft technologies in prehistoric and historical contexts, and its emphasis on technical process (rather than merely the finished artefact) has influenced the archaeology of technology, cognitive archaeology, and the study of skilled practice in anthropology. It has contributed to the cognitive revolution in prehistoric archaeology — the recognition that Palaeolithic humans had modern cognitive capacities — and to the broader study of the evolution of human technological intelligence.",
    "causes": [
      "André Leroi-Gourhan's broad programme of gesture-and-symbol anthropology — his interest in the evolution of human technical gesture and its relationship to cognitive and cultural development — led him to develop the chaîne opératoire as a tool for analysing the complete technical sequence of artefact production, recovering the cognitive and social dimensions of ancient technology.",
      "The limitations of traditional archaeological typology — the classification of artefacts by their final form (shape, size, type) without attention to the process of their manufacture — motivated Leroi-Gourhan and his students to develop the chaîne opératoire as a process-oriented alternative: an approach that treated the entire technical sequence as the primary unit of analysis, not merely the finished object.",
      "The development of systematic refitting studies in French Palaeolithic archaeology — the physical reassembly of stone flakes and cores from excavation assemblages to reconstruct the reduction sequences — provided the empirical basis for chaîne opératoire analysis and demonstrated the extraordinary detail that could be recovered about prehistoric technical practice from systematic spatial and relational analysis."
    ],
    "effects": [
      "The chaîne opératoire became the foundational concept for the study of lithic technology in French and subsequently international prehistoric archaeology — enabling the reconstruction of technical sequences, skill levels, raw material procurement strategies, and social transmission of technical knowledge from stone tool assemblages.",
      "The chaîne opératoire's application to the Palaeolithic record contributed to the cognitive revolution in prehistoric archaeology — revealing the planning depth, working memory requirements, and technical sophistication of early modern humans and Neanderthals, and contributing to debates about the evolution of human cognitive capacity and the emergence of behavioural modernity.",
      "The concept's extension beyond lithic analysis — to ceramics, metalworking, textiles, and other craft technologies — demonstrated its generality as an analytical framework for the archaeology of technology, and its influence on cognitive archaeology, the anthropology of skilled practice, and the study of social learning and cultural transmission has been substantial."
    ],
    "relationships": [
      {"sourceSlug": "andre-leroi-gourhan", "sourceName": "André Leroi-Gourhan (1911–1986)", "verb": "DEVELOPS", "targetSlug": "chane-opratoire", "targetName": "Chaîne opératoire (1960s–1970s)", "context": "Leroi-Gourhan developed the chaîne opératoire as part of his broader programme of gesture-and-symbol anthropology — an approach that analysed the complete technical sequence of artefact production to recover the cognitive and social dimensions of ancient technology."},
      {"sourceSlug": "chane-opratoire", "sourceName": "Chaîne opératoire (technical sequence analysis)", "verb": "APPLIED_TO", "targetSlug": "lithic-technology", "targetName": "Lithic (stone tool) technology analysis", "context": "The chaîne opératoire became the foundational concept for the study of lithic technology in prehistoric archaeology — enabling the reconstruction of complete technical sequences, skill levels, and social transmission of knowledge from stone tool assemblages."},
      {"sourceSlug": "chane-opratoire", "sourceName": "Chaîne opératoire (cognitive archaeology)", "verb": "CONTRIBUTES_TO", "targetSlug": "cognitive-revolution-in-archaeology", "targetName": "Cognitive revolution in prehistoric archaeology", "context": "The chaîne opératoire's revelation of the planning depth and technical sophistication of Palaeolithic humans contributed to the cognitive revolution in prehistoric archaeology — the recognition that early modern humans had modern cognitive capacities."}
    ],
    "places": [
      {"name": "France (Leroi-Gourhan's academic base, development context)", "role": "The chaîne opératoire was developed in the French tradition of prehistoric archaeology — particularly at the University of Paris (Panthéon-Sorbonne) and in the context of French Palaeolithic cave archaeology in the Dordogne and other regions"},
      {"name": "Global (international adoption, applied to worldwide archaeological contexts)", "role": "The chaîne opératoire has been adopted internationally — applied to lithic, ceramic, and craft technologies from the Lower Palaeolithic to historical periods across Africa, Asia, Europe, and the Americas"}
    ],
    "subjects": ["Archaeology", "Ancient Era", "André Leroi-Gourhan", "Prehistoric Technology", "Cognitive Archaeology", "Stone Tools", "Palaeolithic", "Technical Sequence"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The chaîne opératoire (Leroi-Gourhan, 1960s–1970s) is the foundational concept of the study of prehistoric technology — enabling the reconstruction of complete technical sequences from stone tool assemblages and contributing to the cognitive revolution in prehistoric archaeology. Its revelation of the planning depth and technical sophistication of Palaeolithic humans transformed understanding of the evolution of human cognitive capacity and cultural transmission.",
      "significanceCategory": "significant"
    }
  }
},

"formal-concept-analysis": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785formal-concept-analysis.json",
  "slug": "formal-concept-analysis",
  "data": {
    "summary": "Formal Concept Analysis (FCA) is a mathematical theory and computational method for data analysis and knowledge representation, developed by Rudolf Wille (1937–2017) and his colleagues at the Technical University of Darmstadt (Germany) beginning in the early 1980s — first comprehensively described in Wille's paper 'Restructuring Lattice Theory: An Approach Based on Hierarchies of Concepts' (1982). FCA provides a mathematically rigorous framework for identifying and representing conceptual structures in datasets: given a formal context (a triple consisting of a set of objects, a set of attributes, and a binary relation between them — which objects have which attributes), FCA identifies all formal concepts (maximal sets of objects sharing a maximal set of common attributes) and organises them into a concept lattice (a hierarchical structure visualised as a Hasse diagram) that represents the conceptual hierarchy implicit in the data.\n\nThe mathematical foundation of FCA is order theory and lattice theory — specifically, the theory of Galois connections between power sets, which defines the formal concept as a pair (extent, intent) where the extent is the maximal set of objects sharing the intent (the maximal set of common attributes), and the intent is the maximal set of attributes shared by the extent. The concept lattice, in which formal concepts are ordered by inclusion of extents (or equivalently, intents), provides a complete and computationally tractable representation of the conceptual structure of the dataset. Wille developed FCA explicitly as an application of mathematics to human communication and knowledge organisation — his motivation was to make formal mathematical structures interpretable and usable for knowledge workers in natural language contexts.\n\nFCA has been applied in a wide range of domains — information retrieval (conceptual search and navigation), software engineering (detecting clones, refactoring object-oriented code), bioinformatics (gene expression analysis), linguistics (lexical semantics, construction grammar), archaeology, and machine learning (association rule mining, concept formation). Its combination of mathematical rigour, visual interpretability (the concept lattice diagram), and computational tractability made it an important tool in the field of knowledge discovery and data mining from the 1990s onwards.",
    "causes": [
      "Wille's intellectual programme of 'restructuring lattice theory' — his concern that abstract mathematical theories had lost touch with their intellectual roots and with human understanding — motivated his development of FCA as an application of lattice theory to knowledge organisation: a formal mathematical framework that was explicitly oriented toward interpretability and usability in human knowledge work.",
      "The development of data analysis and knowledge representation as practical requirements of the information society — the growing need for methods to extract meaningful structures from large datasets, to represent knowledge in computationally tractable form, and to support information retrieval and decision-making — provided the applied context in which FCA found its most important applications from the 1990s onwards.",
      "The mathematical tradition of Galois connections and lattice theory — the formal algebraic structures that underlie the definition of formal concepts and concept lattices — provided the rigorous mathematical foundation that gave FCA its distinctive combination of theoretical depth and computational tractability."
    ],
    "effects": [
      "FCA's concept lattice became a widely used data visualisation and knowledge representation tool — particularly in information retrieval, software engineering, and bioinformatics — enabling analysts to visualise conceptual structures in datasets and to navigate knowledge spaces through hierarchical concept relationships.",
      "FCA's connection to association rule mining (the TITANIC algorithm and related methods use FCA's formal concept structure to extract association rules from transaction datasets) made it an important tool in the field of knowledge discovery and data mining, contributing to the broader development of machine learning and data science methods.",
      "Rudolf Wille's FCA inspired a substantial international research community — centred on the annual International Conference on Formal Concept Analysis (ICFCA) — and contributed to the development of conceptual knowledge processing as a field, integrating mathematical, computer science, and cognitive perspectives on knowledge representation and learning."
    ],
    "relationships": [
      {"sourceSlug": "rudolf-wille", "sourceName": "Rudolf Wille (1937–2017)", "verb": "DEVELOPS", "targetSlug": "formal-concept-analysis", "targetName": "Formal Concept Analysis (1982)", "context": "Wille developed FCA at TU Darmstadt beginning in the early 1980s — first described in his 1982 paper 'Restructuring Lattice Theory' — as an application of lattice theory to knowledge organisation and conceptual data analysis."},
      {"sourceSlug": "formal-concept-analysis", "sourceName": "FCA (concept lattice, Galois connections)", "verb": "FOUNDED_ON", "targetSlug": "lattice-theory", "targetName": "Lattice theory and order theory (mathematics)", "context": "FCA is mathematically founded on lattice theory and Galois connections — the formal algebraic structures that define the formal concept as a maximal object-attribute pair and the concept lattice as their hierarchical organisation."},
      {"sourceSlug": "formal-concept-analysis", "sourceName": "FCA (knowledge discovery, data mining)", "verb": "APPLIED_IN", "targetSlug": "knowledge-discovery", "targetName": "Knowledge discovery and data mining", "context": "FCA's concept lattice is applied in information retrieval, software engineering, bioinformatics, and data mining — its combination of mathematical rigour and visual interpretability made it an important tool for extracting conceptual structures from large datasets."}
    ],
    "places": [
      {"name": "Technical University of Darmstadt, Germany (1980s, development context)", "role": "FCA was developed at TU Darmstadt by Rudolf Wille and his research group — the centre of the international FCA research community that developed the theory and its applications from the 1980s"},
      {"name": "International (ICFCA conferences, global application)", "role": "FCA has been applied internationally — the annual International Conference on Formal Concept Analysis (ICFCA) brings together researchers from mathematics, computer science, and applied domains worldwide"}
    ],
    "subjects": ["Mathematics", "Modern Era", "Rudolf Wille", "Data Analysis", "Knowledge Representation", "Lattice Theory", "Computer Science", "Information Science"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Formal Concept Analysis (Wille, 1982) is a significant mathematical method for knowledge representation and data analysis — providing a rigorous framework for identifying conceptual structures in datasets through concept lattices. It has been applied in information retrieval, software engineering, bioinformatics, and data mining, and inspired an international research community. Its contribution to knowledge discovery and data science represents the practical application of abstract mathematical theory (lattice theory) to real-world data analysis.",
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
