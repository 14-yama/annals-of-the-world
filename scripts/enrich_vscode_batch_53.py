#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 53 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: the-fox-and-the-grapes (Aesop), the-three-little-pigs,
          the-princess-and-the-pea (Andersen), the-steadfast-tin-soldier (Andersen),
          rumplestiltskin (Brothers Grimm), mother-hulda (Brothers Grimm),
          town-musicians-of-bremen (Brothers Grimm),
          the-wolf-and-the-seven-young-goats (Brothers Grimm)
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-53-may2026"

ENRICHMENTS = {

"the-fox-and-the-grapes": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-fox-and-the-grapes.json",
  "slug": "the-fox-and-the-grapes",
  "data": {
    "summary": "The Fox and the Grapes is one of the most famous fables attributed to Aesop (c. 620–564 BCE), recorded in the Aesopic corpus (Perry Index no. 15) and the primary source of the expression 'sour grapes' in the English language and its equivalents in dozens of other languages. The fable narrates the story of a hungry fox who sees a bunch of grapes hanging high on a vine and tries repeatedly to reach them — after failing to jump high enough, the fox walks away declaring that the grapes are probably sour and not worth eating. Phaedrus's Latin version (1st century CE) and La Fontaine's French version (Le Renard et les raisins, 1668) are the two most influential transmissions of the fable in Western literary culture.\n\nThe Fox and the Grapes is the foundational fable for the psychological concept of cognitive dissonance and rationalisation — the fox's declaration that the grapes are sour is the archetypal example of what Leon Festinger later (1957) theorised as cognitive dissonance reduction: the psychological mechanism by which individuals rationalise their failures and unattained desires by devaluing them. The fable is cited in psychology textbooks as the first recorded observation of this mechanism, giving a 2,500-year-old animal tale a formal role in 20th-century cognitive psychology.\n\nThe phrase 'sour grapes' — meaning the dismissal of something desirable as not worth having after failing to obtain it — has entered virtually every major European language and many non-European languages as an idiom, making The Fox and the Grapes one of the most linguistically productive fables in the Aesopic corpus. Its psychological precision — the fox's transparent self-deception, the gap between what he says and what his behaviour reveals — has made it one of the most frequently cited fables in discussions of rationalisation, self-deception, and motivated reasoning.",
    "causes": [
      "The Greek oral fable tradition attributed to Aesop (c. 620–564 BCE) — the tradition of short animal tales with explicit moral conclusions used as proverbial wisdom — produced the Fox and the Grapes fable as one of the paradigmatic examples of self-deception and the rationalisation of failure.",
      "The Mediterranean agricultural context — the familiarity of the vine and grape harvest as cultural symbols in Greek and Roman culture — made the grapes a vivid and culturally resonant object for the fox's failed desire, giving the fable its memorable visual and sensory quality.",
      "The transmission of the fable through Phaedrus's Latin verses (1st century CE) and La Fontaine's French version (1668) ensured its continuous presence in European moral and literary culture — La Fontaine's elegant rendering made it the paradigmatic example of the fable genre in French literature."
    ],
    "effects": [
      "'Sour grapes' has entered virtually every major language as an idiom for dismissing something desirable after failing to obtain it — one of the most linguistically productive phrases to emerge from the Aesopic fable tradition, demonstrating the extraordinary power of a simple animal tale to generate lasting idiomatic expression.",
      "The Fox and the Grapes is cited in cognitive psychology as a proto-observation of cognitive dissonance — Leon Festinger's theory of cognitive dissonance (1957) describes the same psychological mechanism (rationalising unattained desires by devaluing them) that the fox demonstrates, giving the fable a formal connection to 20th-century cognitive psychology.",
      "La Fontaine's Le Renard et les raisins (1668) became one of the most memorised and recited texts in French primary education — a foundational element of French literary culture, demonstrating how Aesopic fables achieved cultural embedding through the literary adaptation tradition."
    ],
    "relationships": [
      {"sourceSlug": "aesop", "sourceName": "Aesop (c. 620–564 BCE, Greek fabulist — oral tradition; Perry Index 15)", "verb": "AUTHORS", "targetSlug": "the-fox-and-the-grapes", "targetName": "The Fox and the Grapes (Aesopic fable, Perry Index 15 — 'sour grapes'; rationalisation of failure)", "context": "The Fox and the Grapes is attributed to Aesop (c. 620–564 BCE) in the Aesopic corpus — the primary source of the 'sour grapes' idiom and an archetypal observation of self-deception and rationalisation."},
      {"sourceSlug": "the-fox-and-the-grapes", "sourceName": "The Fox and the Grapes ('sour grapes' — cognitive dissonance; Festinger 1957)", "verb": "ANTICIPATES", "targetSlug": "cognitive-dissonance-theory", "targetName": "Cognitive dissonance theory (Leon Festinger, 1957 — rationalisation of unattained desires)", "context": "The Fox and the Grapes is cited in cognitive psychology as a proto-observation of cognitive dissonance — the fox's declaration that the grapes are sour exemplifies the psychological mechanism Festinger formalised in 1957."},
      {"sourceSlug": "the-fox-and-the-grapes", "sourceName": "The Fox and the Grapes (La Fontaine — Le Renard et les raisins 1668; French primary education)", "verb": "ADAPTED_BY", "targetSlug": "jean-de-la-fontaine", "targetName": "Jean de La Fontaine (Le Renard et les raisins, Fables 1668 — paradigmatic French fable)", "context": "La Fontaine's Le Renard et les raisins (1668) is the most elegant French version of the fable — a paradigmatic text of French primary education and a central reference in French literary culture."}
    ],
    "places": [
      {"name": "Ancient Greece (Aesopic oral tradition, c. 620–564 BCE; Mediterranean vineyard context)", "role": "The Fox and the Grapes emerged from the Aesopic oral tradition in ancient Greece — the vineyard and grape harvest as cultural symbols gave the fable its vivid Mediterranean agricultural context"},
      {"name": "France (La Fontaine's Fables 1668 — French primary education; 'sour grapes' idiom in all European languages)", "role": "La Fontaine's version (1668) became the paradigmatic French text — a foundational element of French primary education and the vehicle through which the 'sour grapes' idiom entered European literary culture"}
    ],
    "subjects": ["Ancient Greek Literature", "Ancient Era", "Aesop", "Fable", "Moral Philosophy", "Folk Literature", "La Fontaine", "Cognitive Psychology"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Fox and the Grapes (Aesop, c. 6th century BCE; Perry Index 15) is one of the most linguistically productive fables in world literature — 'sour grapes' has entered virtually every major language as an idiom. Its psychological precision anticipates cognitive dissonance theory (Festinger, 1957), and La Fontaine's version (1668) became a foundational text of French literary education, demonstrating the remarkable cultural longevity of a simple animal tale.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-three-little-pigs": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-three-little-pigs.json",
  "slug": "the-three-little-pigs",
  "data": {
    "summary": "The Three Little Pigs is a traditional fairy tale of uncertain origin, recorded in its most widely known English version in James Orchard Halliwell-Phillipps's Nursery Rhymes and Nursery Tales (1842/1849) and later in Joseph Jacobs's English Fairy Tales (1890), and associated with the English oral tradition, though related tale types exist across European and world folk traditions (ATU type 124). The tale narrates the story of three pigs who each build a house of straw, sticks, and bricks respectively; a wolf (or 'Big Bad Wolf') attempts to blow down each house, succeeding with the straw and stick houses (whose builders flee to the brick house) but failing with the brick house, where the pigs are safe and the wolf is defeated (in different versions: by the failure to blow, by falling down the chimney into a pot, or by being killed).\n\nThe Three Little Pigs is one of the most widely known and frequently analysed fairy tales in Western literature — its central structure (three siblings of increasing wisdom or diligence, the third's greater effort providing safety) is a fundamental tale pattern in world folklore. The tale's moral — that diligence, hard work, and building on a solid foundation protect against danger — is one of the most direct moral instructions in the fairy tale tradition, and the phrase 'I'll huff and I'll puff and I'll blow your house down' (the wolf's threat) is one of the most recognised phrases from the fairy tale tradition in the English language.\n\nThe Three Little Pigs achieved global cultural reach through Walt Disney's animated short The Three Little Pigs (1933) — produced by the Silly Symphony unit and winner of the Academy Award for Best Animated Short Film, the film's song 'Who's Afraid of the Big Bad Wolf?' became a hit during the Great Depression, interpreted as a Depression-era anthem of collective optimism against economic catastrophe. The Disney film is one of the most commercially successful animated shorts ever made, and its cultural impact made the Three Little Pigs one of the most recognised Western folk tale figures worldwide.",
    "causes": [
      "The English oral folk tradition — the tale pattern of three siblings of increasing wisdom (the third more diligent or clever than the first two) using different materials for building — produced the Three Little Pigs story as one of the paradigmatic English-language fairy tales, recorded in Halliwell-Phillipps (1842) and Jacobs (1890).",
      "The tale's didactic simplicity — the clear moral that diligence and solid foundations protect against danger, embodied in the straw-sticks-bricks progression — made it a highly effective vehicle for moral instruction of young children, ensuring its widespread use in early childhood education and its embedding in primary school curricula.",
      "Walt Disney's decision to adapt the Three Little Pigs as a Silly Symphony short (1933) — released during the Great Depression and interpreted as an allegory of collective optimism against economic disaster ('Who's Afraid of the Big Bad Wolf?') — gave the tale extraordinary cultural resonance as a Depression-era text and permanent global reach through Disney's distribution."
    ],
    "effects": [
      "Walt Disney's The Three Little Pigs (1933) won the Academy Award for Best Animated Short Film and its song 'Who's Afraid of the Big Bad Wolf?' became a Depression-era hit — widely interpreted as a collective optimism anthem, the film's cultural impact made the Three Little Pigs one of the most recognised fairy tale figures worldwide.",
      "The Three Little Pigs is one of the most widely taught tales in early childhood education — its clear moral (diligence and solid foundations protect against danger) and its memorable straw-sticks-bricks structure make it a paradigmatic vehicle for character education and early literacy across cultures.",
      "The Big Bad Wolf has become one of the most recognisable villains in Western popular culture — used as a metaphor for threatening forces in political cartoons, advertising, and popular media, and the target of revisionary retellings (The True Story of the Three Little Pigs, Jon Scieszka, 1989) that give him a sympathetic perspective."
    ],
    "relationships": [
      {"sourceSlug": "the-three-little-pigs", "sourceName": "Three Little Pigs (Halliwell-Phillipps 1842, Jacobs 1890 — English oral tradition; ATU 124)", "verb": "RECORDED_BY", "targetSlug": "joseph-jacobs", "targetName": "Joseph Jacobs (English Fairy Tales, 1890 — standard English text)", "context": "Joseph Jacobs recorded the Three Little Pigs in English Fairy Tales (1890) — the most widely cited English-language version, based on the oral tradition recorded by Halliwell-Phillipps (1842)."},
      {"sourceSlug": "the-three-little-pigs", "sourceName": "Three Little Pigs (Disney 1933 — Academy Award; 'Who's Afraid of the Big Bad Wolf'; Depression era)", "verb": "ADAPTED_AS", "targetSlug": "disney-silly-symphony-1933", "targetName": "Disney's Three Little Pigs (1933 Silly Symphony — Academy Award, Depression-era anthem)", "context": "Disney's animated short (1933) won the Academy Award for Best Animated Short Film — its 'Who's Afraid of the Big Bad Wolf?' became a Depression-era hit, giving the tale global cultural reach."},
      {"sourceSlug": "the-three-little-pigs", "sourceName": "Three Little Pigs (diligence, solid foundations — straw, sticks, bricks moral pattern)", "verb": "TEACHES", "targetSlug": "diligence-and-prudence", "targetName": "Moral of diligence and prudent preparation (early childhood education and character formation)", "context": "The Three Little Pigs' clear moral — that diligence and solid foundations protect against danger — makes it a paradigmatic vehicle for character education and early literacy across cultures worldwide."}
    ],
    "places": [
      {"name": "England (oral tradition — Halliwell-Phillipps 1842, Jacobs 1890; English fairy tale canon)", "role": "The Three Little Pigs is associated with the English oral tradition — recorded by Halliwell-Phillipps (1842) and Jacobs (1890), it is one of the paradigmatic English-language fairy tales"},
      {"name": "United States (Disney Silly Symphony 1933 — Great Depression context; global cultural reach)", "role": "Disney's Three Little Pigs (1933) was produced in Hollywood during the Great Depression — its cultural resonance as a Depression-era optimism anthem gave it permanent global reach"}
    ],
    "subjects": ["English Literature", "19th Century", "Fairy Tale", "Folk Literature", "Children's Literature", "Disney Animation", "Moral Philosophy", "English Oral Tradition"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Three Little Pigs (English oral tradition, recorded 1842/1890) is one of the most widely known and taught fairy tales in the world — its clear moral of diligence and solid foundations, the memorable straw-sticks-bricks structure, and Disney's 1933 adaptation (Academy Award, Depression-era anthem) gave it extraordinary global cultural reach. The Big Bad Wolf is one of the most recognisable fairy tale villains in Western popular culture.",
      "significanceCategory": "highly-significant"
    }
  }
},

"the-princess-and-the-pea": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-princess-and-the-pea.json",
  "slug": "the-princess-and-the-pea",
  "data": {
    "summary": "The Princess and the Pea (Danish: Prinsessen på ærten) is a fairy tale by Hans Christian Andersen (1805–1875), first published on 8 May 1835 in the first instalment of Eventyr fortalte for Børn ('Fairy Tales Told for Children') — one of Andersen's first published fairy tales, alongside The Tinderbox, Little Claus and Big Claus, and Thumbelina. The tale narrates the story of a prince who wants to marry a real princess but cannot find one; when a bedraggled young woman arrives at the palace claiming to be a princess, the queen tests her authenticity by placing a single pea under twenty mattresses and twenty feather beds; the woman is unable to sleep for the discomfort of the pea, and her extreme sensitivity is taken as proof of her royal authenticity.\n\nThe Princess and the Pea is one of Andersen's shortest tales — a single page in its original form — and is unusual in his canon for being entirely ironic: the test for royal authenticity is the ability to feel a pea through twenty mattresses and twenty feather beds, which is extreme sensitivity rather than any moral, intellectual, or practical quality. The tale's satirical implication — that aristocratic refinement is a kind of hypersensitivity, an absurd over-cultivation of delicacy — has been widely noted, though Andersen may have intended the tale as a straightforward fairy tale rather than social satire.\n\nThe Princess and the Pea has entered global culture as an idiom for extreme sensitivity — describing someone who is 'a princess and the pea' suggests hypersensitivity, excessive delicacy, or complaint about trivial discomforts. Andersen based the tale on a motif from oral folk tradition (a sensitivity test for true royalty exists in several European folk traditions), but his version is the most widely known. The tale has been adapted in musical theatre (Once Upon a Mattress, 1959, which ran on Broadway for two years), opera, and film, and its central image of the pea under the mattresses is one of the most immediately recognisable in the Andersen canon.",
    "causes": [
      "Hans Christian Andersen's adaptation of a folk motif — the sensitivity test for true royalty, existing in several European oral folk traditions — provided the narrative germ for The Princess and the Pea, which Andersen transformed into his own distinctive literary fairy tale.",
      "Andersen's first fairy tale publication (1835) — the desire to establish his voice as a fairy tale author — placed The Princess and the Pea in the first instalment of Eventyr fortalte for Børn, where its brevity and irony demonstrated his range and his ability to handle the fairy tale form with lightness and wit.",
      "The European aristocratic culture of Andersen's era — the association of noble birth with extreme delicacy, refinement, and sensitivity — provided the cultural logic for the test's premise: that only a 'real' princess would be so exquisitely sensitive as to feel a pea through twenty mattresses."
    ],
    "effects": [
      "'A princess and the pea' or 'princess on a pea' has entered several languages as an idiom for excessive sensitivity or complaint about trivial discomfort — demonstrating the linguistic productivity of the tale's central image and its application in social commentary about over-sensitivity.",
      "The Princess and the Pea has been adapted in musical theatre (Once Upon a Mattress, 1959) — a Broadway musical that ran for two years and has been frequently revived, demonstrating the tale's theatrical viability despite (or because of) its brevity and ironic premise.",
      "The Princess and the Pea is widely used in discussions of Andersen's relationship to aristocratic culture — its ironic premise (extreme delicacy as the criterion for royal authenticity) positions it as either a straightforward fairy tale or a gentle satire of aristocratic hypersensitivity, making it a productive text for analysis of Andersen's social attitudes."
    ],
    "relationships": [
      {"sourceSlug": "hans-christian-andersen", "sourceName": "Hans Christian Andersen (1805–1875, Danish author — first fairy tale publication 1835)", "verb": "AUTHORS", "targetSlug": "the-princess-and-the-pea", "targetName": "The Princess and the Pea (1835 — one of Andersen's first fairy tales; sensitivity test for royalty)", "context": "Andersen published The Princess and the Pea in May 1835 in his first fairy tale instalment — the tale's ironic premise (extreme delicacy as proof of royal authenticity) is characteristic of his wit."},
      {"sourceSlug": "the-princess-and-the-pea", "sourceName": "The Princess and the Pea (Once Upon a Mattress — Broadway musical 1959)", "verb": "ADAPTED_AS", "targetSlug": "once-upon-a-mattress", "targetName": "Once Upon a Mattress (Broadway musical, 1959 — Mary Rodgers; two-year run)", "context": "Once Upon a Mattress (1959) — a Broadway musical adaptation of The Princess and the Pea — ran for two years and has been frequently revived, demonstrating the tale's theatrical viability."},
      {"sourceSlug": "the-princess-and-the-pea", "sourceName": "The Princess and the Pea ('princess on a pea' idiom — hypersensitivity, delicacy)", "verb": "GENERATES_IDIOM", "targetSlug": "hypersensitivity-cultural-expression", "targetName": "Cultural expression of hypersensitivity ('princess and the pea' — complaint about trivial discomfort)", "context": "'Princess and the pea' has entered several languages as an idiom for excessive sensitivity or complaint about trivial discomfort — demonstrating the linguistic productivity of the tale's central image."}
    ],
    "places": [
      {"name": "Denmark (Andersen's first fairy tale instalment, May 1835 — Copenhagen publication)", "role": "The Princess and the Pea was published in Copenhagen in May 1835 in Andersen's first Eventyr instalment — one of his very first published fairy tales, demonstrating his light, ironic touch"},
      {"name": "Global (Broadway 1959 — Once Upon a Mattress; idiom in several languages; widely adapted)", "role": "The Princess and the Pea has been adapted worldwide — Once Upon a Mattress (1959) ran on Broadway for two years, and the 'princess and the pea' idiom has entered several languages"}
    ],
    "subjects": ["Danish Literature", "19th Century", "Fairy Tale", "Hans Christian Andersen", "Children's Literature", "Satire", "Folk Literature", "Musical Theatre"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Princess and the Pea (Andersen, 1835) is one of Andersen's most ironic and concise tales — its premise (extreme delicacy as proof of royal authenticity) has generated the 'princess and the pea' idiom for hypersensitivity and was adapted as Once Upon a Mattress (Broadway, 1959). As one of Andersen's first published fairy tales, it demonstrates his distinctive wit and lightness of touch.",
      "significanceCategory": "significant"
    }
  }
},

"the-steadfast-tin-soldier": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-steadfast-tin-soldier.json",
  "slug": "the-steadfast-tin-soldier",
  "data": {
    "summary": "The Steadfast Tin Soldier (Danish: Den standhaftige tinsoldat) is a fairy tale by Hans Christian Andersen (1805–1875), first published on 2 October 1838 in the second volume of Eventyr fortalte for Børn ('Fairy Tales Told for Children'). The tale narrates the story of a one-legged tin soldier (one of twenty-five cast from an old tin spoon, the last of whom received only one leg due to insufficient tin) who falls in love with a paper ballerina, is thrown out of a window by a jealous jack-in-the-box, is swallowed by a fish, and is ultimately thrown into a fire where both he and the ballerina are consumed — and from the ashes a small tin heart is found the next day.\n\nThe Steadfast Tin Soldier is one of Andersen's most dark and psychologically complex tales — unlike his other tales where the protagonist's virtues are rewarded, the Tin Soldier's stoic devotion, courage, and steadfastness lead not to triumph but to death, and the tale ends not with a happy ending but with the poignant image of the heart-shaped tin from the soldier's melted body and the ballerina's sequin. The tale has been read as a meditation on the acceptance of fate, the beauty of unrequited love, the dignity of steadfastness in the face of loss, and the Romantic belief in the transcendence of spiritual devotion over material circumstance.\n\nThe Steadfast Tin Soldier has been widely admired as one of Andersen's greatest achievements — its economy, its emotional depth, its refusal of the conventional happy ending, and its haunting final image make it a canonical example of the literary fairy tale at its highest level. The tale has been adapted in ballet (the Shostakovich-related The Little Tin Soldier), in Fantasia 2000 (Disney, 1999), and in numerous literary retellings, and its image of the one-legged soldier who loves the paper dancer with unfailing devotion has become one of the most recognisable images in Andersen's canon.",
    "causes": [
      "Andersen's personal experience of unrequited love — his repeated romantic failures and his sense of devotion to figures who did not reciprocate — has been read into the Tin Soldier's stoic, unrequited devotion to the paper ballerina, making the tale one of the most autobiographical in Andersen's canon.",
      "The Romantic aesthetic of steadfastness and spiritual transcendence — the Romantic belief that noble devotion, even unrequited and ultimately unsuccessful, has inherent worth and beauty — provided the philosophical framework for the Tin Soldier's story, in which death is not defeat but the completion of a perfectly devoted life.",
      "Andersen's gift for finding pathos in inanimate objects and marginalised figures — the one-legged soldier who lacks the full complement of tin, the paper dancer who appears to be one-legged but is merely standing on one foot — gave the tale its characteristic blend of whimsy and emotional depth."
    ],
    "effects": [
      "The Steadfast Tin Soldier is widely regarded as one of Andersen's greatest achievements — its economy, emotional depth, and refusal of the conventional happy ending established it as a canonical example of the literary fairy tale at its highest level, influencing subsequent writers of fairy tales and fantasy fiction.",
      "The tale's dark, non-triumphant ending — the Tin Soldier and ballerina consumed by fire, only a heart-shaped tin remaining — established a tradition of elegiac, non-redemptive fairy tales that influenced subsequent children's literature and gave respectability to the sad ending as a valid fairy tale conclusion.",
      "The Steadfast Tin Soldier has been adapted in ballet, animated film (Fantasia 2000, Disney, 1999), and numerous literary retellings — its haunting final image has inspired artists and writers across multiple media, demonstrating the tale's capacity to generate new interpretations and emotional responses."
    ],
    "relationships": [
      {"sourceSlug": "hans-christian-andersen", "sourceName": "Hans Christian Andersen (1805–1875 — unrequited love; steadfastness in the face of loss)", "verb": "AUTHORS", "targetSlug": "the-steadfast-tin-soldier", "targetName": "The Steadfast Tin Soldier (1838 — one-legged soldier, paper ballerina; non-triumphant ending)", "context": "Andersen published The Steadfast Tin Soldier in 1838 — one of his darkest and most emotionally complex tales, ending not in triumph but in the soldier's death and the haunting image of a tin heart."},
      {"sourceSlug": "the-steadfast-tin-soldier", "sourceName": "Steadfast Tin Soldier (non-triumphant ending — elegiac fairy tale; literary fairy tale canon)", "verb": "ESTABLISHES", "targetSlug": "elegiac-fairy-tale-tradition", "targetName": "Elegiac fairy tale tradition (non-redemptive ending — children's literature innovation)", "context": "The Steadfast Tin Soldier's dark, non-triumphant ending established the elegiac fairy tale as a legitimate form — the sad ending as a valid fairy tale conclusion, influencing subsequent children's literature."},
      {"sourceSlug": "the-steadfast-tin-soldier", "sourceName": "Steadfast Tin Soldier (Fantasia 2000 — Disney adaptation; ballet, literary retellings)", "verb": "ADAPTED_AS", "targetSlug": "fantasia-2000", "targetName": "Fantasia 2000 (Disney, 1999 — animated adaptation of The Steadfast Tin Soldier)", "context": "The Steadfast Tin Soldier was adapted in Disney's Fantasia 2000 (1999) — one of multiple adaptations in ballet and animated film demonstrating the tale's enduring capacity to inspire artistic interpretation."}
    ],
    "places": [
      {"name": "Denmark (Copenhagen — Andersen 1838; Romantic aesthetic; autobiographical unrequited love)", "role": "The Steadfast Tin Soldier was published in Copenhagen in 1838 — the tale's Romantic aesthetic of steadfast devotion in the face of loss reflects Andersen's own experience of unrequited love"},
      {"name": "Global (ballet, Disney Fantasia 2000, literary retellings — widely adapted across media)", "role": "The Steadfast Tin Soldier has been adapted in ballet, Disney's Fantasia 2000 (1999), and numerous literary retellings — its haunting final image has inspired artists and writers across multiple media"}
    ],
    "subjects": ["Danish Literature", "19th Century", "Fairy Tale", "Hans Christian Andersen", "Romantic Literature", "Children's Literature", "Elegiac Fiction", "Unrequited Love"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Steadfast Tin Soldier (Andersen, 1838) is one of Andersen's greatest and most emotionally complex tales — its non-triumphant ending (soldier and ballerina consumed by fire, only a tin heart remaining) established the elegiac fairy tale as a legitimate form. Widely adapted in ballet, Disney's Fantasia 2000, and literary retellings, it is a canonical example of the literary fairy tale at its highest level.",
      "significanceCategory": "highly-significant"
    }
  }
},

"rumplestiltskin": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780rumplestiltskin.json",
  "slug": "rumplestiltskin",
  "data": {
    "summary": "Rumpelstiltskin (German: Rumpelstilzchen) is a German fairy tale first recorded by the Brothers Grimm in Kinder- und Hausmärchen ('Children's and Household Tales') as tale KHM 55, in the first edition (1812), and revised in subsequent editions with the most widely read version appearing in the 7th edition (1857). The tale narrates the story of a miller who boasts to the king that his daughter can spin gold from straw — the daughter is locked in a room with a spinning wheel and straw and told to spin gold or die; a mysterious little man appears and spins the gold in exchange for her necklace, ring, and finally the promise of her firstborn child; when the king marries her and the firstborn arrives, the little man returns to claim the child; but the queen is granted a three-day reprieve if she can guess his name, and ultimately discovers his name (Rumpelstiltskin) through a spy who observes him dancing and singing in the forest.\n\nRumpelstiltskin is classified as ATU type 500 ('The Name of the Supernatural Helper') and exists in related versions across European and world folk traditions — the motif of the supernatural helper whose power is broken when his name is discovered is widespread in Germanic, British (Tom Tit Tot), and Scottish folk traditions. The tale's central mystery — the power of a secret name — is connected to the ancient magical belief that knowing a being's true name gives power over it, a belief found in Egyptian, Hebrew, Greek, and Norse magical traditions.\n\nRumpelstiltskin's cultural legacy in the modern era is remarkably varied — the name 'Rumpelstiltskin' has become an idiom in some legal contexts (notably in Rumpelstiltskin-related constitutional cases in the United States about the right to know one's biological father's name), the tale is a central text in feminist analysis (the miller's lie commodifies his daughter; the queen is dependent on supernatural help to spin gold she cannot actually spin), and it is one of the most frequently adapted of all Grimm fairy tales in popular fiction.",
    "causes": [
      "The Germanic folk tradition of supernatural helpers with secret names (ATU type 500) — the widespread European belief that knowing a supernatural being's true name gives power over it — produced the Rumpelstiltskin story as one of the paradigmatic examples of this magical tradition, recorded by the Grimm brothers from German oral informants.",
      "The Brothers Grimm's collection project — the recording of German folk narratives — drove the inclusion of Rumpelstiltskin in the Kinder- und Hausmärchen (1812), alongside related tale types from British tradition (Tom Tit Tot) that share the same core motif.",
      "The ancient magical belief in the power of names — found in Egyptian magic (the true name of Ra), Hebrew tradition (the prohibition on pronouncing the name of God), and Norse mythology (the runes as named powers) — provided the deep cultural substructure for the tale's central premise that knowing Rumpelstiltskin's name breaks his power."
    ],
    "effects": [
      "Rumpelstiltskin has become one of the most widely known and frequently adapted Grimm fairy tales — the bizarre little man who can spin gold from straw is one of the most recognisable fairy tale figures in Western popular culture, generating theatrical, operatic, cinematic, and literary adaptations across multiple cultures.",
      "The tale has been analysed in feminist fairy tale criticism as a narrative of female commodification — the miller's lie reduces his daughter to an instrument of economic advancement, and the queen's dependence on supernatural help to spin gold she cannot actually spin highlights the gap between the social expectations placed on women and their actual capacities.",
      "In American legal culture, 'Rumpelstiltskin' has given its name to a doctrine in family law and constitutional cases — the right to know one's biological parent's name, even if hidden — demonstrating the remarkable diffusion of a fairy tale figure into formal legal discourse."
    ],
    "relationships": [
      {"sourceSlug": "brothers-grimm", "sourceName": "Brothers Grimm (KHM 55, Kinder- und Hausmärchen — 1st ed. 1812; 7th ed. 1857)", "verb": "RECORDS", "targetSlug": "rumplestiltskin", "targetName": "Rumpelstiltskin (KHM 55 — spinning gold, secret name, ATU type 500)", "context": "The Brothers Grimm recorded Rumpelstiltskin in Kinder- und Hausmärchen (1812) — one of the paradigmatic ATU type 500 ('The Name of the Supernatural Helper') tales."},
      {"sourceSlug": "rumplestiltskin", "sourceName": "Rumpelstiltskin (secret name — Egyptian/Hebrew/Norse magical tradition; power over named beings)", "verb": "CONNECTS_TO", "targetSlug": "magical-naming-tradition", "targetName": "Ancient magical naming tradition (Egyptian, Hebrew, Norse — true name gives power over being)", "context": "Rumpelstiltskin's central premise — that knowing a supernatural being's true name breaks its power — connects to the ancient magical belief in the power of names found in Egyptian, Hebrew, and Norse tradition."},
      {"sourceSlug": "rumplestiltskin", "sourceName": "Rumpelstiltskin (feminist analysis — miller commodifies daughter; queen's supernatural dependence)", "verb": "EXAMINED_BY", "targetSlug": "feminist-fairy-tale-criticism", "targetName": "Feminist fairy tale criticism (female commodification, supernatural dependence — Grimm tales)", "context": "Feminist critics analyse Rumpelstiltskin as a narrative of female commodification — the miller's lie reduces his daughter to an instrument of economic advancement, highlighting the gap between social expectations placed on women and their actual capacities."}
    ],
    "places": [
      {"name": "Germany (Grimm collection, 1812 — oral informants; Germanic ATU 500 tradition)", "role": "Rumpelstiltskin was recorded by the Brothers Grimm from German oral informants in 1812 — one of the paradigmatic examples of the ATU type 500 tale type in the Germanic folk tradition"},
      {"name": "Global (theatrical, operatic, cinematic adaptations; American legal doctrine — 'Rumpelstiltskin doctrine')", "role": "Rumpelstiltskin has been adapted worldwide in theatrical, operatic, and cinematic forms — and has given its name to a legal doctrine in American family law about the right to know one's biological parent"}
    ],
    "subjects": ["German Literature", "19th Century", "Fairy Tale", "Brothers Grimm", "Folk Literature", "Magical Thinking", "Feminist Criticism", "Children's Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Rumpelstiltskin (Grimm, KHM 55, 1812) is one of the most widely known and frequently adapted Grimm fairy tales — the ATU type 500 tale of the supernatural helper whose power is broken by the discovery of his name. Its connection to ancient magical naming traditions, its feminist analysis as a narrative of female commodification, and its entry into American legal doctrine demonstrate its remarkable cultural longevity.",
      "significanceCategory": "significant"
    }
  }
},

"mother-hulda": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780mother-hulda.json",
  "slug": "mother-hulda",
  "data": {
    "summary": "Mother Hulda (German: Frau Holle) is a German fairy tale recorded by the Brothers Grimm in Kinder- und Hausmärchen ('Children's and Household Tales') as tale KHM 24, in the first edition (1812), and one of the most significant tales in the Grimm collection from a folkloric and religious history perspective. The tale narrates the story of a widow's two daughters — a diligent, good-natured stepdaughter and an idle, vain biological daughter — who fall into a well and find themselves in an underground realm ruled by Mother Hulda (Frau Holle); the good stepdaughter works hard for Mother Hulda and is rewarded with a shower of gold when she returns to the upper world; the idle daughter shirks her work and is covered in pitch (black tar) as her reward.\n\nMother Hulda is far more significant than its modest fairy tale frame suggests — Frau Holle (or Holda, Hulda, Perchta) is a major Germanic folk deity, associated with winter (when she shakes out her feather bed, snow falls on earth), spinning (she is the patron of spinning women), the dead (she leads a 'wild hunt' of the souls of the dead), and the underworld. She is one of the few Germanic pre-Christian deities to survive in continuous folk tradition to the modern period, preserved in fairy tale disguise in the Grimm collection and in folk customs across Germany, Austria, and Switzerland.\n\nThe Grimm brothers were aware of Frau Holle's mythological significance — Jacob Grimm's Deutsche Mythologie (German Mythology, 1835) discusses her in detail, identifying her with the Germanic goddess Holda and connecting her to Norse mythology (possibly to Frigg or Hel). Mother Hulda/Frau Holle is thus one of the most important survivals of Germanic pre-Christian religious tradition in the fairy tale form, and the tale is a unique document of the Christianisation of Germanic religious culture — the goddess transformed into a fairy tale helper, her religious functions (spinner, ruler of the dead, winter goddess) preserved in attenuated form.",
    "causes": [
      "The survival of Germanic folk religion in oral tradition — Frau Holle's identification with the Germanic goddess Holda, her associations with winter, spinning, and the dead — preserved her in folk memory as a powerful supernatural figure, disguised as a fairy tale helper in the Christian era.",
      "The Brothers Grimm's collection project — and Jacob Grimm's scholarly awareness of Frau Holle's mythological significance (explored in Deutsche Mythologie, 1835) — drove both the recording of the tale and the recognition of its religious historical importance as a survival of pre-Christian Germanic religious tradition.",
      "The universal fairy tale structure of the two contrasted sisters (diligent vs. idle, rewarded vs. punished) — one of the most widespread tale types in European folk tradition — provided the narrative frame within which Frau Holle's mythological significance was preserved and transmitted to modern audiences."
    ],
    "effects": [
      "Mother Hulda is one of the most important survivals of Germanic pre-Christian religious tradition in the fairy tale form — the tale preserves, in disguised form, the attributes and functions of the Germanic goddess Holda (winter, spinning, the dead), providing evidence for the religious practices and beliefs of pre-Christian Germanic culture.",
      "Frau Holle remains a living figure in German, Austrian, and Swiss folk culture — Frau Holle mountains (Hoher Meissner in Hesse is associated with her), folk customs of spinning and the wild hunt, and regional winter festivals continue to invoke Frau Holle, demonstrating the remarkable survival of pre-Christian religious traditions in living folk culture.",
      "Mother Hulda has been analysed as a document of the Christianisation of Germanic religious culture — the transformation of a goddess into a fairy tale helper, her religious functions attenuated and moralised, is a case study in how Christianity absorbed and transformed pre-Christian religious traditions rather than simply replacing them."
    ],
    "relationships": [
      {"sourceSlug": "brothers-grimm", "sourceName": "Brothers Grimm (KHM 24, Kinder- und Hausmärchen — Jacob Grimm's Deutsche Mythologie 1835)", "verb": "RECORDS", "targetSlug": "mother-hulda", "targetName": "Mother Hulda (KHM 24 — Frau Holle, Germanic deity of winter, spinning, and the dead)", "context": "The Brothers Grimm recorded Mother Hulda in 1812 — Jacob Grimm identified Frau Holle as a survival of the Germanic goddess Holda in Deutsche Mythologie (1835)."},
      {"sourceSlug": "mother-hulda", "sourceName": "Mother Hulda (Frau Holle — Germanic goddess Holda; winter, spinning, dead; pre-Christian religion)", "verb": "PRESERVES", "targetSlug": "germanic-pre-christian-religion", "targetName": "Germanic pre-Christian religion (goddess Holda — winter, spinning, wild hunt, underworld)", "context": "Mother Hulda is one of the most important survivals of Germanic pre-Christian religious tradition in fairy tale form — Frau Holle's attributes (winter, spinning, the dead) preserve the functions of the Germanic goddess Holda in Christianised disguise."},
      {"sourceSlug": "mother-hulda", "sourceName": "Mother Hulda (Christianisation — goddess → fairy tale helper; religious functions moralised)", "verb": "DOCUMENTS", "targetSlug": "christianisation-of-germanic-culture", "targetName": "Christianisation of Germanic religious culture (pre-Christian deity → fairy tale figure)", "context": "Mother Hulda documents the Christianisation of Germanic religious culture — the transformation of a goddess into a fairy tale helper, with her religious functions (winter, spinning, the dead) preserved in attenuated and moralised form."}
    ],
    "places": [
      {"name": "Germany, Austria, Switzerland (Frau Holle — Hoher Meissner mountain, Hesse; regional folk customs)", "role": "Frau Holle is associated with specific German landscapes (Hoher Meissner in Hesse) and regional winter folk customs — a living figure in German, Austrian, and Swiss folk culture"},
      {"name": "Germany (Kinder- und Hausmärchen 1812; Jacob Grimm's Deutsche Mythologie 1835 — scholarly analysis)", "role": "Mother Hulda was recorded in Germany in 1812 — Jacob Grimm's Deutsche Mythologie (1835) analysed Frau Holle's mythological significance, identifying her with the Germanic goddess Holda"}
    ],
    "subjects": ["German Literature", "19th Century", "Fairy Tale", "Brothers Grimm", "Germanic Religion", "Folk Literature", "Pre-Christian Religion", "Mythology"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Mother Hulda (Grimm, KHM 24, 1812) is far more significant than its fairy tale frame suggests — Frau Holle is one of the most important survivals of Germanic pre-Christian religious tradition, preserving the attributes of the goddess Holda (winter, spinning, the dead) in Christianised fairy tale form. As a document of Germanic religious history and the Christianisation of pre-Christian cult traditions, it is uniquely valuable in the comparative study of European religions.",
      "significanceCategory": "highly-significant"
    }
  }
},

"town-musicians-of-bremen": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780town-musicians-of-bremen.json",
  "slug": "town-musicians-of-bremen",
  "data": {
    "summary": "The Town Musicians of Bremen (German: Die Bremer Stadtmusikanten) is a German fairy tale recorded by the Brothers Grimm in Kinder- und Hausmärchen ('Children's and Household Tales') as tale KHM 27, in the first edition (1812). The tale narrates the story of four ageing animals — a donkey, a dog, a cat, and a rooster — each of whom is about to be killed by their owners for being too old and no longer useful; the donkey proposes that they all go to Bremen to become town musicians; on the way they discover a robbers' cottage, frighten away the robbers through their combined noise, and settle in the cottage. The animals never actually reach Bremen — the journey is complete once they have found a place where they are valued (by each other, and by themselves) and no longer threatened.\n\nThe Town Musicians of Bremen is one of the most popular Grimm fairy tales in Germany — the city of Bremen has adopted the four musicians as its civic emblem, and a famous bronze sculpture of the stacked animals (by Gerhard Marcks, 1951) stands in front of the Bremen Town Hall, touched for good luck by millions of tourists annually. The tale is celebrated in Germany as a narrative of solidarity, self-determination, and the value of collective action by those who have been discarded by society — the four animals achieve freedom not through magical transformation or royal rescue but through their own collective wit and courage.\n\nThe Town Musicians of Bremen has a remarkable international reception — it is widely known across Europe, East Asia (particularly in Japan and South Korea, where the tale is taught in primary schools), and has been adapted in numerous theatrical, animated, and musical forms. The tale's message of solidarity among the marginalised and the collective power of those deemed useless has resonated across political contexts, from Weimar Germany to contemporary social inclusion discourse.",
    "causes": [
      "The North German oral tradition — the tale type of the group of animals who combine their individual talents to overcome a threat — provided the narrative material that the Brothers Grimm recorded from informants in the Lower Saxony region associated with Bremen, giving the tale its specifically north German geographical setting.",
      "The Brothers Grimm's collection project — the recording of German folk narratives — drove the inclusion of the Bremen Town Musicians in the Kinder- und Hausmärchen (1812), where it became one of the most popular and frequently adapted tales in the collection.",
      "The social relevance of the tale's theme — the animals deemed too old and useless by their owners who find collective solidarity and freedom — resonated across German cultural history, particularly during periods of social dislocation (Weimar Germany, post-war reconstruction) when the tale's message of solidarity among the marginalised was politically resonant."
    ],
    "effects": [
      "The Town Musicians of Bremen became the civic emblem of the city of Bremen — the bronze sculpture of the four stacked animals (Gerhard Marcks, 1951) in front of the Bremen Town Hall is one of the most photographed sculptures in Germany and a major tourist attraction, touched for good luck by millions of visitors annually.",
      "The tale's message of solidarity among those deemed useless and the collective power of the marginalised has resonated across political contexts — cited in social inclusion discourse, solidarity movements, and the cultural politics of ageing, the tale provides a narrative of collective self-determination against institutional abandonment.",
      "The Town Musicians of Bremen has been widely adapted in animated film, theatre, and music — including a famous Soviet animated film (The Musicians of Bremen, 1969, with songs by Gennady Gladkov) that became a beloved classic of Soviet children's culture, demonstrating the tale's international cultural reach."
    ],
    "relationships": [
      {"sourceSlug": "brothers-grimm", "sourceName": "Brothers Grimm (KHM 27, Kinder- und Hausmärchen — North German oral tradition, 1st ed. 1812)", "verb": "RECORDS", "targetSlug": "town-musicians-of-bremen", "targetName": "Town Musicians of Bremen (KHM 27 — donkey, dog, cat, rooster; collective solidarity)", "context": "The Brothers Grimm recorded the Town Musicians of Bremen in 1812 from North German oral informants — one of the most popular Grimm fairy tales and the civic emblem of the city of Bremen."},
      {"sourceSlug": "town-musicians-of-bremen", "sourceName": "Town Musicians of Bremen (Bremen civic emblem — Gerhard Marcks sculpture 1951; tourist attraction)", "verb": "SYMBOLISES", "targetSlug": "city-of-bremen", "targetName": "City of Bremen (Germany — civic emblem; Gerhard Marcks bronze sculpture 1951)", "context": "The Town Musicians of Bremen became the civic emblem of Bremen — Gerhard Marcks's bronze sculpture (1951) in front of the Town Hall is one of the most photographed in Germany, touched for good luck by millions of tourists."},
      {"sourceSlug": "town-musicians-of-bremen", "sourceName": "Town Musicians of Bremen (Soviet animated film 1969 — beloved classic of Soviet children's culture)", "verb": "ADAPTED_AS", "targetSlug": "musicians-of-bremen-soviet-1969", "targetName": "The Musicians of Bremen (Soviet animated film, 1969 — beloved classic of Soviet children's culture)", "context": "The Soviet animated film The Musicians of Bremen (1969, with songs by Gennady Gladkov) became a beloved classic of Soviet children's culture — demonstrating the tale's international reach beyond German cultural tradition."}
    ],
    "places": [
      {"name": "Bremen, Germany (civic emblem — Gerhard Marcks bronze sculpture 1951; North German oral tradition)", "role": "The Town Musicians of Bremen became the civic emblem of Bremen — the 1951 bronze sculpture in front of the Town Hall is one of Germany's most photographed and is touched for good luck by millions of tourists annually"},
      {"name": "International (Soviet animated film 1969; Japan and South Korea primary school curriculum; widely adapted)", "role": "The Town Musicians of Bremen has been adapted internationally — the Soviet animated film (1969) is a beloved classic, and the tale is taught in primary schools in Japan and South Korea"}
    ],
    "subjects": ["German Literature", "19th Century", "Fairy Tale", "Brothers Grimm", "Folk Literature", "Solidarity", "Children's Literature", "Animal Fable"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Town Musicians of Bremen (Grimm, KHM 27, 1812) is one of the most popular Grimm fairy tales — celebrated as a narrative of solidarity among those deemed useless, it became the civic emblem of Bremen (Gerhard Marcks bronze sculpture, 1951). Its international reach (Soviet animated classic 1969; primary school curricula in Japan and South Korea) and its resonance in social inclusion discourse demonstrate its continuing cultural vitality.",
      "significanceCategory": "significant"
    }
  }
},

"the-wolf-and-the-seven-young-goats": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-wolf-and-the-seven-young-goats.json",
  "slug": "the-wolf-and-the-seven-young-goats",
  "data": {
    "summary": "The Wolf and the Seven Young Goats (German: Der Wolf und die sieben jungen Geißlein) is a German fairy tale recorded by the Brothers Grimm in Kinder- und Hausmärchen ('Children's and Household Tales') as tale KHM 5, in the first edition (1812). The tale narrates the story of a mother goat who goes to fetch food and warns her seven young kids not to open the door to the wolf; the wolf attempts three times to enter, disguising his voice and his paw — on his third attempt (with chalk to whiten his paw) he succeeds in entering while the mother is away and swallows six of the seven kids, while the seventh hides in the clock case; the mother returns, discovers what has happened, finds the wolf sleeping under a tree with his swollen belly, cuts him open with scissors, frees the six kids (still alive), fills the wolf's belly with stones, and the wolf drowns when he tries to drink from a well.\n\nThe Wolf and the Seven Young Goats is classified as ATU tale type 123 ('The Wolf and the Kids') and shares its central motif with the Little Red Riding Hood tale type (ATU 333) — the wolf who deceives and swallows the victim whole, and the rescue by cutting open the wolf's belly — making it part of a related complex of wolf tales in European folk tradition that explore the threat of deception and the danger of opening the door to strangers.\n\nThe Wolf and the Seven Young Goats is one of the earliest tales in the Grimm collection (KHM 5) and one of the most widely taught in German-speaking countries as an early childhood protective narrative — a story that teaches children about the danger of strangers, deception, and the importance of not opening the door to those who claim to be someone they are not. Its central pedagogical message (do not be deceived by appearances; do not open the door to strangers) is one of the most direct child safety narratives in the fairy tale tradition.",
    "causes": [
      "The European wolf folklore tradition — the wolf as the primary threat to domestic animals and children in the agricultural communities of medieval and early modern Europe — provided the cultural context for the Wolf and the Seven Young Goats, one of a cluster of European folk tales (Red Riding Hood, Three Little Pigs, Big Bad Wolf) in which the wolf threatens the household.",
      "The Brothers Grimm's collection project — the recording of German folk narratives — drove the inclusion of the Wolf and the Seven Young Goats as KHM 5 in the Kinder- und Hausmärchen (1812), where its placement as one of the earliest tales in the collection reflects its pedagogical importance for young children.",
      "The universal parental anxieties about child safety and deception — the need to teach children to recognise and resist deception by dangerous figures who pretend to be trustworthy — drove the development and transmission of the tale as a child safety narrative in European folk tradition."
    ],
    "effects": [
      "The Wolf and the Seven Young Goats is one of the most widely taught fairy tales in German-speaking primary education — its child safety message (do not open the door to strangers; do not be deceived by false appearances) has made it a standard element of early childhood safety education in Germany, Austria, and Switzerland.",
      "The tale's shared motif with Little Red Riding Hood (wolf swallowing victims whole; rescue by cutting open the belly) demonstrates the existence of a related cluster of ATU wolf tales in European folk tradition — the comparative study of these tales illuminates the folk narrative strategies for addressing the threat of deception and violence in pre-modern European agricultural communities.",
      "The Mother Goat's decisive action — finding the wolf, cutting him open, rescuing her kids, and filling him with stones — makes her one of the most active and effective maternal figures in the Grimm collection, and the tale has been analysed as a narrative of maternal agency and protective power in the fairy tale tradition."
    ],
    "relationships": [
      {"sourceSlug": "brothers-grimm", "sourceName": "Brothers Grimm (KHM 5, Kinder- und Hausmärchen — ATU 123; early childhood tale, 1st ed. 1812)", "verb": "RECORDS", "targetSlug": "the-wolf-and-the-seven-young-goats", "targetName": "Wolf and Seven Young Goats (KHM 5 — mother goat, deceptive wolf, child safety narrative)", "context": "The Brothers Grimm recorded the Wolf and Seven Young Goats as KHM 5 in 1812 — one of the earliest and most pedagogically important tales in the collection, teaching children about the danger of deception."},
      {"sourceSlug": "the-wolf-and-the-seven-young-goats", "sourceName": "Wolf and Seven Young Goats (ATU 123 — Little Red Riding Hood; wolf swallows victims; rescue by cutting)", "verb": "SHARES_MOTIF_WITH", "targetSlug": "little-red-riding-hood", "targetName": "Little Red Riding Hood (ATU 333 — wolf swallows grandmother; rescue; European wolf tale cluster)", "context": "The Wolf and Seven Young Goats shares the central motif with Little Red Riding Hood (ATU 333) — the wolf swallowing victims whole and the rescue by cutting open the belly — demonstrating a related cluster of European wolf tales."},
      {"sourceSlug": "the-wolf-and-the-seven-young-goats", "sourceName": "Wolf and Seven Young Goats (child safety — do not open door; deception by false appearance)", "verb": "TEACHES", "targetSlug": "child-safety-education", "targetName": "Child safety education (stranger danger — deception, protective narratives for young children)", "context": "The Wolf and Seven Young Goats is one of the most direct child safety narratives in the fairy tale tradition — teaching children not to open the door to strangers who use deception to pretend to be someone they are not."}
    ],
    "places": [
      {"name": "Germany (Kinder- und Hausmärchen, 1812 — KHM 5; German-speaking primary education)", "role": "Recorded in Germany in 1812 as KHM 5 — one of the earliest tales in the Grimm collection, widely taught in German, Austrian, and Swiss primary education as a child safety narrative"},
      {"name": "European wolf folklore tradition (agricultural communities — wolf as domestic threat; ATU 123 tale type)", "role": "The Wolf and Seven Young Goats belongs to the European wolf folklore tradition in which the wolf threatens the household — a cluster of ATU 123 and 333 tales addressing the threat of deception and the danger of domestic violation"}
    ],
    "subjects": ["German Literature", "19th Century", "Fairy Tale", "Brothers Grimm", "Folk Literature", "Child Safety", "Children's Literature", "Wolf Folklore"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "The Wolf and the Seven Young Goats (Grimm, KHM 5, 1812) is one of the most widely taught early childhood protective narratives in German-speaking countries — its message of deception awareness and the danger of opening the door to strangers makes it a direct child safety tale. Its shared motif with Little Red Riding Hood (ATU 333) places it within the comparative study of European wolf folk tales.",
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
