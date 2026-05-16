#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 02 (7 high-priority entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities covered (from enrichment_queue top priorities, imp=7–9):
  judaism, king-dongmyeong-of-goguryeo, suppiluliuma-i, merneith,
  prasenajit, lord-xinling, malik-al-ashtar

No conflict risk: Gemini on queue[200:300], Ollama on queue[325:525].
"""

import json
import os
import sys
import time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-02-may2026"

# ─────────────────────────────────────────────────────────────────────────────
# Hand-authored enrichments (Claude Sonnet 4.6 / GitHub Copilot)
# ─────────────────────────────────────────────────────────────────────────────

ENRICHMENTS = {

"judaism": {
  "filepath": "data/appwrite-export/entities/141-Class-141/141judaism.json",
  "slug": "judaism",
  "data": {
    "summary": "Judaism is one of the oldest monotheistic traditions in the world, tracing its origins to the covenant between God and Abraham recorded in the Hebrew Bible (c. 2000 BCE) and codified into law through the Mosaic revelation at Sinai. It is simultaneously a religion, a civilisation, and an ethnic identity — a layered inheritance that has survived diaspora, persecution, and radical transformation across four millennia. At its core stands the Torah (the first five books of Moses), the Talmud (the great rabbinic commentary compiled between 200–500 CE), and an unbroken chain of textual interpretation that gave rise to the concept of the 'People of the Book.'\n\nThe Babylonian exile (586 BCE) was the crucible of rabbinic Judaism: deprived of the Temple, Jewish scholars reconstituted worship around Torah study and synagogue prayer — a portable religious infrastructure that enabled Jewish identity to survive without territorial sovereignty for over 1,900 years. The destruction of the Second Temple by Rome in 70 CE further accelerated this transformation, producing the Mishnah, the Talmud, and a diaspora community that stretched from Spain to Persia, maintaining cultural and religious coherence through textual authority rather than political power.\n\nIn the modern era, Judaism gave birth to both Zionism — the movement for Jewish national self-determination that established the State of Israel in 1948 — and to the Reform, Conservative, and Orthodox movements that redefined the tradition's relationship to modernity after the European Enlightenment. The Holocaust (1941–1945), which killed six million Jews — approximately two-thirds of European Jewry — became the defining trauma of 20th-century Jewish identity, reshaping theology, politics, and memory across the global Jewish community. Today approximately 15–16 million Jews worldwide maintain traditions originating in one of humanity's oldest continuous literary civilisations.",
    "causes": [
      "The Bronze Age emergence of Abrahamic monotheism in Canaan, distinguishing Israelite religion from surrounding polytheistic cultures and establishing the covenant framework at the heart of Judaism.",
      "The Babylonian exile (586 BCE) dismantled Temple-based religion and compelled rabbinical reinterpretation of Jewish practice as a portable, text-centred tradition independent of land or sanctuary.",
      "Roman destruction of the Second Temple in 70 CE permanently ended sacrificial worship and empowered the Pharisaic-Rabbinic movement to codify Jewish law into the Mishnah and Talmud — the foundation of all subsequent Judaism."
    ],
    "effects": [
      "Judaism gave rise to Christianity and Islam, its two monotheistic successor traditions, which together account for over half the global population and share foundational scripture, ethical frameworks, and prophetic history.",
      "Rabbinic Judaism's emphasis on literacy, argumentation, and textual study produced disproportionately high rates of intellectual achievement across philosophy, science, law, and literature throughout subsequent centuries.",
      "Zionism, born from 19th-century Jewish nationalism, established the State of Israel in 1948 — permanently reshaping Middle Eastern geopolitics and creating one of the 20th century's most consequential and contested nation-building projects."
    ],
    "relationships": [
      {"sourceSlug": "judaism", "sourceName": "Judaism", "verb": "INFLUENCES", "targetSlug": "christianity", "targetName": "Christianity", "context": "Christianity emerged from 1st-century Second Temple Judaism; Jesus, Paul, and the apostles were all Jewish, and the Hebrew Bible forms the Old Testament of the Christian canon."},
      {"sourceSlug": "judaism", "sourceName": "Judaism", "verb": "INFLUENCES", "targetSlug": "islam", "targetName": "Islam", "context": "Islamic theology, scripture, and law draw extensively on Jewish monotheism, prophetic tradition, and legal reasoning; Muhammad's early community was deeply shaped by contact with Jewish communities in Medina."},
      {"sourceSlug": "judaism", "sourceName": "Judaism", "verb": "CONTAINS", "targetSlug": "torah", "targetName": "Torah", "context": "The Torah — the first five books of Moses — constitutes the foundational canonical text of Judaism, containing the 613 commandments (mitzvot) that govern Jewish religious and ethical life."},
      {"sourceSlug": "judaism", "sourceName": "Judaism", "verb": "LEADS_TO", "targetSlug": "zionism", "targetName": "Zionism", "context": "Modern Zionism emerged from 19th-century Jewish nationalism responding to antisemitism, culminating in the 1948 establishment of the State of Israel as a Jewish homeland after two millennia of diaspora."},
      {"sourceSlug": "babylon", "sourceName": "Babylonian Captivity", "verb": "TRANSFORMS", "targetSlug": "judaism", "targetName": "Judaism", "context": "The Babylonian exile (586–538 BCE) forced Judaism to reconstitute itself without the Temple, transforming it from a sacrificial cult into a text-based religion capable of surviving in diaspora."},
      {"sourceSlug": "holocaust", "sourceName": "Holocaust", "verb": "TRANSFORMS", "targetSlug": "judaism", "targetName": "Judaism", "context": "The Nazi genocide (1941–1945) killed six million Jews, permanently reshaping Jewish theology, political identity, and the movement for a Jewish state."}
    ],
    "places": [
      {"name": "Jerusalem, Israel", "role": "Site of the First and Second Temple; holiest city in Judaism"},
      {"name": "Babylon (Iraq)", "role": "Location of the Babylonian exile (586–538 BCE) and centre of Talmudic scholarship"},
      {"name": "Yavneh, Roman Judea", "role": "Site where rabbinic Judaism was codified after the Temple's destruction in 70 CE"}
    ],
    "subjects": ["Religion", "World History", "Philosophy", "Literature", "Ethics", "Monotheism", "Middle East", "Israel", "Diaspora", "Classical Era"],
    "frameworks": ["THEOLOGICAL_FRAMEWORK", "CAUSE_AND_EFFECT", "COMPARATIVE_RELIGION"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Judaism is the root tradition from which Christianity and Islam — together comprising over 3.5 billion adherents — both descended, and its emphasis on literacy, law, and monotheism reshaped the moral architecture of Western civilisation, the development of international law, and the course of Middle Eastern history through the founding of Israel in 1948.",
      "significanceCategory": "world-changing"
    }
  }
},

"king-dongmyeong-of-goguryeo": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221king-dongmyeong-of-goguryeo.json",
  "slug": "king-dongmyeong-of-goguryeo",
  "data": {
    "summary": "King Dongmyeong (58–19 BCE, r. 37–19 BCE), born Jumong or Go Jumong, was the legendary founder of Goguryeo — the powerful ancient Korean kingdom that dominated the northern Korean peninsula and Manchuria for nearly seven centuries. Revered in Korean tradition as a divine hero of semi-supernatural birth, Jumong's founding myth — preserved in the Samguk Sagi (1145 CE) — describes him as the son of Haemosu, a god of heaven, and Lady Yuhwa, a water goddess, born from an egg after his mother was impregnated by sunlight. The legend draws direct parallels with other ancient East Asian founding myths and was instrumental in asserting Goguryeo's legitimacy as a divinely sanctioned state.\n\nJumong fled his stepbrothers' persecution at the Buyeo court and established his capital at Jolbon (modern North Korea/China border region), uniting fragmented tribes into a centralised kingdom. His military campaigns systematically absorbed neighbouring polities — Songyang of Biryu, the Malgal people, and the southern Okjeo tribes — demonstrating both personal martial ability and political acumen. In the Samguk Sagi account, Jumong ruled for 19 years, establishing the institutional and territorial foundations that later Goguryeo kings would expand into one of the Three Kingdoms of Korea.\n\nGoguryeo, which Jumong founded, reached its apex under Gwanggaeto the Great (391–413 CE), whose stele records over 64 conquests across the Korean peninsula, Manchuria, and beyond. The kingdom's resistance to the Sui dynasty's massive invasion (598–614 CE) — repulsing armies numbering in the hundreds of thousands — became a foundational story of Korean national resilience. Goguryeo's cultural legacy endures in the name 'Korea' (Goryeo → Korea) and in the Goguryeo tomb murals, designated a UNESCO World Heritage site in 2004.",
    "causes": [
      "The fragmented tribal society of the Yalu River and Manchurian regions in the 1st century BCE lacked centralised political authority, creating conditions for a charismatic military leader to unite disparate groups.",
      "Jumong's exile from the Buyeo court — driven by jealousy over his exceptional archery skills — was the immediate catalyst for founding Goguryeo, transforming personal crisis into state-building.",
      "The decline of the Chinese Han dynasty's Lelang commandery created a political vacuum in northern Korea that Goguryeo systematically filled during its first two centuries of expansion."
    ],
    "effects": [
      "Goguryeo became one of the Three Kingdoms of Korea alongside Baekje and Silla, establishing the political and cultural framework of Korean civilisation that persisted until unification under Silla in 668 CE.",
      "Goguryeo's successful military resistance against the Sui dynasty's invasions (598–614 CE) contributed to the collapse of the Sui Empire, demonstrating the strategic importance of the Korean kingdoms in East Asian geopolitics.",
      "The name 'Korea' derives from the Goryeo dynasty (918–1392 CE), itself named in homage to Goguryeo, meaning Jumong's founding act echoes in the modern international name for the Korean nation."
    ],
    "relationships": [
      {"sourceSlug": "king-dongmyeong-of-goguryeo", "sourceName": "King Dongmyeong of Goguryeo", "verb": "FOUNDS", "targetSlug": "goguryeo", "targetName": "Goguryeo Kingdom", "context": "Jumong founded Goguryeo in 37 BCE in the Jolbon region, establishing the dynasty and kingdom that would dominate northern Korea and Manchuria for nearly 700 years."},
      {"sourceSlug": "king-dongmyeong-of-goguryeo", "sourceName": "King Dongmyeong of Goguryeo", "verb": "INFLUENCES", "targetSlug": "gwanggaeto-the-great", "targetName": "Gwanggaeto the Great", "context": "Jumong's founding legacy provided the dynastic legitimacy invoked by Gwanggaeto the Great, who expanded Goguryeo to its greatest territorial extent in the early 5th century CE."},
      {"sourceSlug": "king-dongmyeong-of-goguryeo", "sourceName": "King Dongmyeong of Goguryeo", "verb": "INFLUENCES", "targetSlug": "three-kingdoms-of-korea", "targetName": "Three Kingdoms of Korea", "context": "Goguryeo's founding set the political stage for the Three Kingdoms period, in which Goguryeo, Baekje, and Silla competed for dominance across the Korean peninsula."},
      {"sourceSlug": "king-dongmyeong-of-goguryeo", "sourceName": "King Dongmyeong of Goguryeo", "verb": "OCCURS_IN", "targetSlug": "korean-peninsula", "targetName": "Korean Peninsula", "context": "Goguryeo's core territory spanned the northern Korean peninsula and present-day Manchuria, shaping the geography and culture of the entire region."}
    ],
    "places": [
      {"name": "Jolbon (Jibe), Manchuria", "role": "First capital of Goguryeo, established by Jumong c. 37 BCE"},
      {"name": "Buyeo Kingdom, Manchuria", "role": "Kingdom from which Jumong fled before founding Goguryeo"},
      {"name": "Pyongyang, Korea", "role": "Later Goguryeo capital and cultural centre of the kingdom"}
    ],
    "subjects": ["Korean History", "East Asian History", "Ancient History", "Founding Myths", "Kingship", "Military History", "Classical Era", "Korea", "China", "Goguryeo"],
    "frameworks": ["POLITICAL_HISTORY", "MYTHOLOGY_AND_RELIGION", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Jumong's founding of Goguryeo in 37 BCE established the most powerful of the Three Kingdoms of Korea, whose name and cultural legacy gave Korea its modern international identity; Goguryeo's military resistance to the Sui dynasty contributed to the collapse of a Chinese empire, demonstrating the pivotal role of Korean kingdoms in shaping East Asian history.",
      "significanceCategory": "continental"
    }
  }
},

"suppiluliuma-i": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221suppiluliuma-i.json",
  "slug": "suppiluliuma-i",
  "data": {
    "summary": "Suppiluliuma I (r. c. 1344–1322 BCE) was the greatest military conqueror of the Hittite Empire, who transformed a struggling Anatolian kingdom into one of the Near East's two superpowers — a feat accomplished through a combination of diplomatic cunning, tactical innovation, and merciless campaigning. His conquests dismantled the Mitanni Empire, extended Hittite control across modern Syria and Lebanon to the border of Egyptian-controlled Canaan, and restructured the entire balance of power in the ancient Near East. The 'Amarna Letters' — diplomatic correspondence discovered in Egypt in 1887 — document the era's superpower politics, and Suppiluliuma's campaigns forced Egypt's Pharaoh Akhenaten to abandon territory his predecessors had held for generations.\n\nSuppiluliuma's Syrian campaigns were conducted in two phases. The first great campaign (c. 1340 BCE) crossed the Euphrates and carved deep into Mitanni territory, installing Hittite-aligned client kings in cities from Carchemish to Aleppo. The second, definitive campaign (c. 1330–1325 BCE) completed the destruction of the Mitanni Empire, placed his sons Piyassili and Telepinu on the thrones of Carchemish and Aleppo respectively, and created a chain of Hittite-controlled buffer states stretching to the border of Egyptian-controlled Palestine. The episode of Suppiluliuma receiving a letter from the Egyptian queen Dahamunzu — almost certainly Ankhesenamun, widow of Tutankhamun — requesting one of his sons as a husband, revealing her fear of Egypt's internal instability, is one of the most dramatic diplomatic episodes preserved from the ancient world.\n\nSuppiluliuma's death came from a plague epidemic — possibly introduced by Egyptian prisoners of war after his son Zannanza was murdered en route to Egypt — which killed both Suppiluliuma and his successor Arnuwanda II in quick succession. Despite his death, the territorial and political framework he established defined Hittite power for the next century, culminating in the Battle of Kadesh (1274 BCE) between Hittite King Muwatalli II and Ramesses II, the world's first recorded peace treaty.",
    "causes": [
      "The political instability of the Mitanni Empire — weakened by internal succession crises and Egyptian pressure — created a strategic opportunity that Suppiluliuma exploited with systematic military campaigns.",
      "The religious revolution of Akhenaten in Egypt (c. 1353–1336 BCE) distracted pharaonic attention from foreign policy, leaving Egypt's Syrian provinces inadequately defended against Hittite expansion.",
      "Suppiluliuma's own administrative and military reforms — including the placement of loyal sons as vassal kings across Syria — created a durable network of control that previous Hittite kings had failed to establish."
    ],
    "effects": [
      "The destruction of the Mitanni Empire permanently ended one of the great Bronze Age powers and reshuffled the Near Eastern political order into a Hittite-Egyptian bipolar system that shaped the region for over a century.",
      "Suppiluliuma's placement of his sons as rulers of Carchemish and Aleppo established a Hittite regional dynasty in Syria that persisted until the Sea Peoples' invasions destroyed the Hittite Empire around 1200 BCE.",
      "The plague that Suppiluliuma's army brought back from Syria killed him, his heir, and devastated the Hittite homeland — demonstrating how epidemiological consequences of imperial expansion could undermine even the greatest military triumphs."
    ],
    "relationships": [
      {"sourceSlug": "suppiluliuma-i", "sourceName": "Suppiluliuma I", "verb": "DEFEATS", "targetSlug": "mitanni", "targetName": "Mitanni Empire", "context": "Suppiluliuma's campaigns of the 1330s BCE destroyed Mitanni as a major power, dividing its territory between Hittite vassals and the rival Assyrian kingdom."},
      {"sourceSlug": "suppiluliuma-i", "sourceName": "Suppiluliuma I", "verb": "TRANSFORMS", "targetSlug": "hittite-empire", "targetName": "Hittite Empire", "context": "Suppiluliuma transformed the Hittite kingdom from a regional Anatolian power into a Near Eastern superpower, with territory stretching from the Aegean coast to northern Syria."},
      {"sourceSlug": "suppiluliuma-i", "sourceName": "Suppiluliuma I", "verb": "INFLUENCES", "targetSlug": "battle-of-kadesh", "targetName": "Battle of Kadesh", "context": "Suppiluliuma's Syrian conquests established the Hittite strategic position that made the Battle of Kadesh (1274 BCE) — the greatest chariot battle of the ancient world — inevitable."},
      {"sourceSlug": "akhenaten", "sourceName": "Akhenaten", "verb": "INFLUENCES", "targetSlug": "suppiluliuma-i", "targetName": "Suppiluliuma I", "context": "Akhenaten's religious revolution and diplomatic passivity left Egypt's Syrian territories poorly defended, enabling Suppiluliuma's conquests."},
      {"sourceSlug": "suppiluliuma-i", "sourceName": "Suppiluliuma I", "verb": "OCCURS_IN", "targetSlug": "ancient-near-east", "targetName": "Ancient Near East", "context": "Suppiluliuma's campaigns took place across the ancient Near East — modern Turkey, Syria, and Lebanon — restructuring the entire regional power balance."}
    ],
    "places": [
      {"name": "Hattusa (modern Boğazkale, Turkey)", "role": "Hittite capital and seat of Suppiluliuma's power"},
      {"name": "Carchemish (modern Turkey/Syria border)", "role": "Key city captured and ruled by Suppiluliuma's son Piyassili"},
      {"name": "Mitanni heartland (northern Syria/Iraq)", "role": "Territory conquered and dismantled during Suppiluliuma's campaigns"}
    ],
    "subjects": ["Ancient History", "Hittites", "Near Eastern History", "Military History", "Diplomacy", "Bronze Age", "Classical Era", "Turkey", "Syria", "Imperialism"],
    "frameworks": ["POLITICAL_HISTORY", "MILITARY_HISTORY", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Suppiluliuma I destroyed the Mitanni Empire and made the Hittites one of only two Near Eastern superpowers, a transformation whose consequences — including the Battle of Kadesh and the world's first peace treaty — reverberated for over a century after his death.",
      "significanceCategory": "continental"
    }
  }
},

"merneith": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220merneith.json",
  "slug": "merneith",
  "data": {
    "summary": "Merneith (fl. c. 2950 BCE) was a queen of the First Dynasty of ancient Egypt and very likely its first female ruler — possibly the world's first documented female head of state — who served as regent for her young son Den after the death of her husband King Djet. Whether Merneith held the title of pharaoh in her own right remains debated, but the evidence is compelling: she possesses her own royal tomb at Abydos (Tomb Y) of a size and quality comparable to those of male kings, she is listed on the Saqqara king list and the Palermo Stone, she was buried with the full regalia of royal funerary equipment including sacrificed retainers, and her name appears in royal serekhs (the standard device for recording a pharaoh's name). Her name means 'Beloved of Neith,' invoking the powerful war and weaving goddess of the north.\n\nThe discovery and excavation of Merneith's tomb by Flinders Petrie in 1900 at Abydos revealed artifacts consistent with royal status: she was buried with 40 subsidiary graves containing retainers sacrificed to serve her in the afterlife — a practice standard for pharaohs of the period. Clay seal impressions bearing her name were found near the tomb of her son Den, suggesting she exercised administrative authority during his minority. The Palermo Stone, a fragmentary annals record created in the Fifth Dynasty, includes Merneith among the sequence of early rulers, lending institutional weight to the interpretation of her as a reigning queen.\n\nMerneith's possible reign occurred in a period when the Egyptian state was still being consolidated — the First Dynasty represented the unification of Upper and Lower Egypt under a single kingship — making her regency (and possible direct rule) a critical test of early dynastic political institutions. If she did reign as pharaoh, she preceded Hatshepsut — Egypt's most celebrated female ruler — by nearly 1,500 years, making her one of the earliest women to exercise supreme political authority in recorded history.",
    "causes": [
      "The premature death of her husband King Djet left their young son Den unable to govern, creating the dynastic necessity for a senior royal woman — Merneith — to assume regency.",
      "The political consolidation of the First Dynasty required a stable succession mechanism, and Merneith's status as the Great Royal Wife and mother of the heir made her the natural regent.",
      "Early dynastic Egyptian religion and royal ideology did not systematically exclude women from royal roles; the precedent of the goddess Neith (after whom Merneith was named) as a warrior-creator deity may have legitimised female authority."
    ],
    "effects": [
      "Merneith's apparent regency and possible direct reign established a precedent for female royal authority in ancient Egypt that — if recognised in her own time — prefigured later female pharaohs including Sobekneferu, Hatshepsut, and Cleopatra VII by centuries.",
      "Her son Den reigned as one of the most successful and long-lived First Dynasty pharaohs, suggesting that Merneith's regency provided effective continuity of royal administration during a critical early period.",
      "Merneith's tomb complex at Abydos — with its full royal mortuary equipment — contributed to Egyptologists' understanding of early dynastic mortuary practice and the role of royal women in the consolidation of pharaonic power."
    ],
    "relationships": [
      {"sourceSlug": "merneith", "sourceName": "Merneith", "verb": "LEADS_TO", "targetSlug": "den-pharaoh", "targetName": "Den (Pharaoh)", "context": "Merneith served as regent for her son Den during his minority, enabling the stable succession that made Den one of the longest-ruling First Dynasty pharaohs."},
      {"sourceSlug": "merneith", "sourceName": "Merneith", "verb": "INFLUENCES", "targetSlug": "hatshepsut", "targetName": "Hatshepsut", "context": "If Merneith's reign is accepted as pharaonic, she established the earliest precedent for female pharaonic rule, a tradition that culminated with Hatshepsut's full royal reign c. 1479–1458 BCE."},
      {"sourceSlug": "merneith", "sourceName": "Merneith", "verb": "OCCURS_IN", "targetSlug": "ancient-egypt", "targetName": "Ancient Egypt", "context": "Merneith's possible reign occurred during the First Dynasty — the foundational period of Egyptian state formation — at Abydos and Memphis."},
      {"sourceSlug": "djet", "sourceName": "Djet (Pharaoh)", "verb": "LEADS_TO", "targetSlug": "merneith", "targetName": "Merneith", "context": "The death of Djet (Merneith's husband) during Den's minority created the succession gap that Merneith's regency filled."}
    ],
    "places": [
      {"name": "Abydos, Egypt", "role": "Location of Merneith's royal tomb (Tomb Y), equal in scale to First Dynasty male pharaoh tombs"},
      {"name": "Saqqara, Egypt", "role": "Site of secondary tomb and administrative records confirming Merneith's royal status"},
      {"name": "Memphis, Egypt", "role": "First Dynasty administrative capital where Merneith likely exercised royal authority as regent"}
    ],
    "subjects": ["Ancient Egypt", "Women's History", "Prehistoric Era", "Monarchy", "Archaeology", "African History", "Early Civilisation", "Egyptology", "Gender History", "Kingship"],
    "frameworks": ["GENDER_HISTORY", "POLITICAL_HISTORY", "ARCHAEOLOGICAL_EVIDENCE"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Merneith is possibly the world's first documented female head of state (c. 2950 BCE), whose royal tomb at Abydos and administrative records suggest she exercised pharaonic authority — predating Hatshepsut by 1,500 years and establishing the earliest known precedent for female political sovereignty.",
      "significanceCategory": "world-changing"
    }
  }
},

"prasenajit": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221prasenajit.json",
  "slug": "prasenajit",
  "data": {
    "summary": "Prasenajit (c. 6th–5th century BCE) was the king of Kosala — one of the sixteen great kingdoms (mahajanapadas) of ancient India — and a contemporary and personal friend of the historical Buddha. His reign is documented in both Buddhist Pali scriptures and Jain texts, and he appears in numerous suttas as a thoughtful, sometimes morally conflicted monarch who engaged the Buddha in philosophical dialogue on questions of ethics, governance, and the nature of kingship. Unlike many ancient rulers portrayed one-dimensionally in religious literature, Prasenajit is depicted with nuance: he was capable of cruelty and injustice, willing to acknowledge his errors, and genuinely transformed by repeated conversations with the Buddha at Sravasti, his capital.\n\nThe kingdom of Kosala occupied what is today the Uttar Pradesh state of India, and Prasenajit's long reign coincided with the rise of Buddhism as a major religious and philosophical movement. He provided land and support for the Jetavana monastery near Sravasti — the site most associated with the Buddha's teaching ministry — and his court became a focal point for early Buddhist intellectual exchange. The Pali texts record 11 major suttas (discourses) involving Prasenajit, in which he questions the Buddha about topics ranging from personal conduct and the merit of charitable giving to the nature of aging, death, and non-self. His sister was reportedly given in marriage to Bimbisara of Magadha, creating a dynastic alliance between the two dominant northern Indian kingdoms.\n\nPrasenajit's reign ended tragically: his son Vidudabha staged a coup and seized the throne, while Prasenajit — forced to flee — died of exposure near the gates of Rajagriha before being able to obtain military assistance from Magadha. The subsequent annihilation of the Shakya clan by Vidudabha — the tribe from which the Buddha himself descended — fulfilled what Buddhist texts presented as the karmic consequence of an earlier injustice. Kosala was eventually absorbed by Magadha under Ajatashatru, ending its independent existence.",
    "causes": [
      "The political landscape of the Ganges plain in the 6th–5th century BCE featured intensely competitive mahajanapadas in which powerful kings like Prasenajit of Kosala and Bimbisara of Magadha consolidated territory through war, alliance, and marriage.",
      "The emergence of Buddhism and Jainism as reformist movements critical of Vedic ritual gave educated kings like Prasenajit an intellectual alternative to Brahminical religion and a different framework for understanding royal duty (dharma).",
      "The strategic alliance between Kosala and Magadha through Prasenajit's marriage connection to Bimbisara temporarily stabilised the two kingdoms' rivalry — but ultimately failed to prevent Magadha's absorption of Kosala."
    ],
    "effects": [
      "Prasenajit's patronage of the Jetavana monastery at Sravasti made it the single most important site in early Buddhist teaching, hosting more of the Buddha's discourses than any other location and shaping the content of the Pali Canon.",
      "His philosophical dialogues with the Buddha, preserved in 11 Pali suttas, provided early Buddhist literature with vivid examples of kingship ethics and the challenge of reconciling political power with moral virtue.",
      "The fall of Kosala to Magadha accelerated the Magadhan expansion that ultimately produced the Maurya Empire under Chandragupta (c. 321 BCE) — the first empire to unite most of the Indian subcontinent."
    ],
    "relationships": [
      {"sourceSlug": "prasenajit", "sourceName": "Prasenajit", "verb": "INFLUENCES", "targetSlug": "gautama-buddha", "targetName": "Gautama Buddha", "context": "Prasenajit's repeated philosophical dialogues with the Buddha at Sravasti are preserved in 11 major Pali suttas, making him one of the most documented royal interlocutors of early Buddhism."},
      {"sourceSlug": "prasenajit", "sourceName": "Prasenajit", "verb": "CONTAINS", "targetSlug": "jetavana-monastery", "targetName": "Jetavana Monastery", "context": "Prasenajit's patronage gave the Buddhist community the Jetavana monastery near Sravasti, which became the primary residence and teaching ground of the historical Buddha."},
      {"sourceSlug": "prasenajit", "sourceName": "Prasenajit", "verb": "OCCURS_IN", "targetSlug": "kosala", "targetName": "Kingdom of Kosala", "context": "Prasenajit ruled Kosala from its capital Sravasti, overseeing the kingdom's height of power before its eventual absorption by Magadha."},
      {"sourceSlug": "bimbisara", "sourceName": "Bimbisara of Magadha", "verb": "INFLUENCES", "targetSlug": "prasenajit", "targetName": "Prasenajit", "context": "The dynastic alliance between Prasenajit's Kosala and Bimbisara's Magadha — cemented by marriage — shaped the geopolitics of the Ganges plain during early Buddhist period."}
    ],
    "places": [
      {"name": "Sravasti (modern Shravasti, Uttar Pradesh, India)", "role": "Capital of Kosala and site of Prasenajit's court and the Jetavana monastery"},
      {"name": "Rajagriha (Magadha capital)", "role": "City where Prasenajit died after fleeing his son's coup"},
      {"name": "Ganges Plain, India", "role": "The contested political landscape of the sixteen mahajanapadas during Prasenajit's reign"}
    ],
    "subjects": ["Ancient India", "Buddhism", "Classical Era", "Kingship", "Indian Philosophy", "South Asian History", "Early Buddhism", "Mahajanapadas", "Ethics", "Patronage"],
    "frameworks": ["RELIGIOUS_HISTORY", "POLITICAL_HISTORY", "BIOGRAPHICAL"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Prasenajit's patronage of the Jetavana monastery made Sravasti the most important site in early Buddhist teaching, and his philosophical dialogues with the Buddha — preserved in 11 Pali suttas — provide the most detailed surviving portrait of royal ethics in early Indian civilisation.",
      "significanceCategory": "regional"
    }
  }
},

"lord-xinling": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220lord-xinling.json",
  "slug": "lord-xinling",
  "data": {
    "summary": "Lord Xinling (d. 243 BCE), personal name Wei Wuji, was a prince of the state of Wei during China's Warring States period (475–221 BCE) and is celebrated in Chinese history as one of the 'Four Lords of the Warring States' — a group of aristocratic patrons renowned for maintaining vast households of talented retainers (binkè) whose skills could be deployed for diplomatic, military, and political purposes. Xinling was the half-brother of King Anxi of Wei, and his foresight, military acumen, and remarkable personal humility in the service of others made him a defining model of virtuous leadership in classical Chinese thought.\n\nXinling's most celebrated achievement was the relief of Zhao in 258 BCE. When the state of Qin besieged the Zhao capital Handan in what became the epic Siege of Handan, Xinling persuaded his brother the king of Wei to send a relief army — and when the king vacillated, Xinling used his remarkable network of retainers to steal the military tally (the symbol of command over Wei's troops), personally execute the general who refused to advance, and lead 80,000 Wei troops to join forces with Chu to lift the siege and inflict a major defeat on Qin. This act of decisive insubordination, taken to honour an alliance at personal risk to himself, is recounted in the Shiji (Records of the Grand Historian) as one of the most dramatic episodes in Warring States history.\n\nDespite this victory, Xinling's later years were marked by political marginalisation and excessive drinking. Distrusted by his own brother who feared his popularity, Xinling lived in Wei for years, declining to participate in government. Qin exploited this by bribing Wei officials to spread rumours that made the king further suspicious of his brother. Xinling died in 243 BCE, reportedly from excessive drinking brought on by political despair. His death removed Wei's most capable military mind just decades before Qin extinguished the state in 225 BCE.",
    "causes": [
      "The Warring States period's intensely competitive interstate system created a premium on talented military and diplomatic advisors, driving aristocrats to compete for talent through generous patronage systems.",
      "Xinling's exceptional status as a royal half-brother gave him both the resources to maintain a large household of retainers and the independence to act outside normal bureaucratic channels when he judged it necessary.",
      "Qin's growing military dominance in the late Warring States period created existential pressure on Wei and its allies, making bold strategic interventions — like Xinling's relief of Zhao — both necessary and heroic."
    ],
    "effects": [
      "The relief of Handan in 258 BCE demonstrated that Qin's military machine could be checked through coordinated allied resistance, temporarily slowing Qin's unification of China by several decades.",
      "Xinling's model of virtuous patronage — the nobleman who cultivated talented retainers, treated them with dignity regardless of social status, and deployed them in service of justice rather than self-interest — became an idealised type in Chinese political culture.",
      "Xinling's death in 243 BCE and the subsequent political decline of Wei removed one of the last serious obstacles to Qin's final conquest of the remaining Warring States kingdoms, completed by Qin Shi Huang between 230–221 BCE."
    ],
    "relationships": [
      {"sourceSlug": "lord-xinling", "sourceName": "Lord Xinling", "verb": "INFLUENCES", "targetSlug": "siege-of-handan", "targetName": "Siege of Handan", "context": "Xinling's theft of the military tally and leadership of the Wei relief force broke the Qin siege of Handan in 258 BCE, one of the decisive military events of the Warring States period."},
      {"sourceSlug": "lord-xinling", "sourceName": "Lord Xinling", "verb": "INFLUENCES", "targetSlug": "warring-states-period", "targetName": "Warring States Period", "context": "Xinling was one of the most capable aristocratic leaders of the Warring States era, whose strategies temporarily checked Qin expansion and whose patronage model became canonical in Chinese statecraft literature."},
      {"sourceSlug": "qin-dynasty", "sourceName": "Qin Dynasty", "verb": "INFLUENCES", "targetSlug": "lord-xinling", "targetName": "Lord Xinling", "context": "Qin's agents spread disinformation to undermine Wei's trust in Xinling, successfully marginalising Wei's best military commander and contributing to Wei's eventual conquest."},
      {"sourceSlug": "lord-xinling", "sourceName": "Lord Xinling", "verb": "OCCURS_IN", "targetSlug": "wei-state", "targetName": "State of Wei", "context": "Xinling was a prince of Wei, serving his half-brother King Anxi as an independent strategic actor in Wei's defence against Qin."}
    ],
    "places": [
      {"name": "Wei (Daliang, modern Kaifeng, Henan, China)", "role": "Xinling's home state and the political centre of his activities"},
      {"name": "Handan (Zhao capital, Hebei, China)", "role": "City relieved by Xinling's intervention in 258 BCE"},
      {"name": "Warring States China", "role": "The geopolitical landscape of the late Zhou dynasty in which Xinling's career unfolded"}
    ],
    "subjects": ["Chinese History", "Warring States Period", "Classical Era", "Military History", "Political Philosophy", "Patronage", "China", "Ancient History", "Confucianism", "Statecraft"],
    "frameworks": ["POLITICAL_HISTORY", "BIOGRAPHICAL", "MILITARY_HISTORY"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Lord Xinling's relief of Handan in 258 BCE inflicted one of Qin's few major military defeats during its drive to unify China, and his model of virtuous aristocratic patronage became a canonical ideal in Chinese political thought recorded by Sima Qian in the Shiji.",
      "significanceCategory": "regional"
    }
  }
},

"malik-al-ashtar": {
  "filepath": "data/appwrite-export/entities/262-Class-262/262malik-al-ashtar.json",
  "slug": "malik-al-ashtar",
  "data": {
    "summary": "Malik ibn al-Harith al-Nakha'i, known as Malik al-Ashtar ('Malik the Pierced Eye,' c. 600–658 CE), was one of the most celebrated military commanders and political figures of early Islam — a devoted companion of Ali ibn Abi Talib, the fourth caliph, and the recipient of the most detailed surviving letter of political philosophy from the early Islamic period. Born into the Nakha'i tribe of Yemen, Malik earned his cognomen from a wound sustained in battle and became known for extraordinary bravery, tactical brilliance, and fierce loyalty to Ali's cause in the tumultuous years following the death of Uthman ibn Affan.\n\nMalik was appointed governor of Egypt by Ali ibn Abi Talib in 658 CE — a moment of supreme political importance, as Egypt's vast agricultural revenue was essential to any caliphal government. Ali wrote him the famous Ahd Malik al-Ashtar ('Covenant/Charter to Malik al-Ashtar'), an extraordinary administrative and ethical treatise covering every aspect of governance: the duties of rulers to their subjects, the treatment of the poor and working classes, the management of the military, the selection of judges and tax collectors, and the ethical foundations of political authority. This document, preserved in Ali's collected letters (Nahj al-Balagha), is considered by Shia scholars and many political philosophers to be one of the most sophisticated statements of Islamic political ethics ever produced, and the United Nations referenced it in a 2002 report as containing principles consistent with modern human rights standards.\n\nMalik never reached Egypt to govern it. According to the most widely accepted account, he was assassinated by a Muawiya agent who poisoned him with honey at a rest stop during the journey. Ali, upon learning of his death, reportedly grieved more profoundly than for any other companion and said: 'Malik was to me as I was to the Messenger of God' — a statement that encapsulates Malik's standing in early Islamic history and the loss his death represented for the Alid cause in the First Fitna (Islamic civil war).",
    "causes": [
      "Ali ibn Abi Talib's succession to the caliphate in 656 CE following Uthman's assassination plunged early Islam into civil war (the First Fitna), creating the context in which Malik's military and political talents became strategically critical.",
      "Malik's tribal origin in the Nakha'i — a Yemeni tribe with deep pre-Islamic warrior traditions — gave him the martial ethos and personal authority among Arabian fighters that made him effective as a military commander.",
      "Muawiya ibn Abi Sufyan's rivalry with Ali for the caliphate created direct motivation to eliminate Ali's most capable supporters, making Malik a target for assassination."
    ],
    "effects": [
      "The 'Covenant to Malik al-Ashtar' (Ahd Malik) became one of the foundational texts of Islamic political philosophy, influencing Islamic governance theory for over 1,400 years and cited by the UN in 2002 as consistent with contemporary human rights principles.",
      "Malik's death before reaching Egypt was a catastrophic strategic loss for Ali: without his governance Egypt slipped toward Muawiya's sphere, undermining Ali's caliphate and contributing to the Alid defeat in the First Fitna.",
      "Malik's memory became central to Shia Islamic identity: revered as a martyr and model of virtue, he is honoured in Shia commemorative traditions and his shrine at Al-Qurnah (Iraq) remains a pilgrimage site."
    ],
    "relationships": [
      {"sourceSlug": "malik-al-ashtar", "sourceName": "Malik al-Ashtar", "verb": "INFLUENCES", "targetSlug": "ali-ibn-abi-talib", "targetName": "Ali ibn Abi Talib", "context": "Malik was Ali's most trusted and capable military commander; Ali's grief at Malik's death and his statement equating Malik's relationship to himself with his own relationship to Muhammad reveals the depth of their bond."},
      {"sourceSlug": "ali-ibn-abi-talib", "sourceName": "Ali ibn Abi Talib", "verb": "DEFINES", "targetSlug": "malik-al-ashtar", "targetName": "Malik al-Ashtar", "context": "Ali's 'Covenant to Malik al-Ashtar' is one of the most remarkable documents in Islamic history — a detailed charter of good governance written specifically for Malik's appointment as governor of Egypt."},
      {"sourceSlug": "malik-al-ashtar", "sourceName": "Malik al-Ashtar", "verb": "INFLUENCES", "targetSlug": "first-fitna", "targetName": "First Fitna", "context": "Malik's military campaigns on Ali's behalf in the First Fitna — at the Battle of the Camel and Siffin — were crucial to the Alid cause; his death dramatically weakened it."},
      {"sourceSlug": "muawiya-i", "sourceName": "Muawiya I", "verb": "INFLUENCES", "targetSlug": "malik-al-ashtar", "targetName": "Malik al-Ashtar", "context": "Muawiya ordered or facilitated Malik's assassination by poison in 658 CE to prevent him from consolidating Ali's control over Egypt."},
      {"sourceSlug": "malik-al-ashtar", "sourceName": "Malik al-Ashtar", "verb": "INFLUENCES", "targetSlug": "nahj-al-balagha", "targetName": "Nahj al-Balagha", "context": "The Covenant to Malik al-Ashtar, addressed to him by Ali, forms one of the most celebrated sections of the Nahj al-Balagha and shaped Shia political philosophy for centuries."}
    ],
    "places": [
      {"name": "Kufa, Iraq", "role": "Ali's capital and base of Malik's military operations during the First Fitna"},
      {"name": "Al-Qurnah, Iraq", "role": "Traditional location of Malik's tomb, now a Shia pilgrimage site"},
      {"name": "Egypt", "role": "Province Malik was appointed to govern — and to which he died en route"}
    ],
    "subjects": ["Early Islam", "Shia Islam", "Military History", "Political Philosophy", "Classical Era", "Iraq", "Islamic Governance", "First Fitna", "Ali ibn Abi Talib", "Islamic History"],
    "frameworks": ["THEOLOGICAL_FRAMEWORK", "POLITICAL_HISTORY", "BIOGRAPHICAL"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Malik al-Ashtar was Ali ibn Abi Talib's most capable military commander whose assassination weakened the Alid cause in the First Fitna, and the 'Covenant to Malik al-Ashtar' — written for him by Ali — became one of Islamic civilisation's most sophisticated statements of political ethics, cited by the United Nations in 2002 as consistent with modern human rights principles.",
      "significanceCategory": "regional"
    }
  }
}

}  # end ENRICHMENTS

# ─────────────────────────────────────────────────────────────────────────────
# Core enrichment logic (identical pattern to batch_01)
# ─────────────────────────────────────────────────────────────────────────────

def find_entity_in_file(data: dict, slug: str):
    """Find entity by slug in a data file."""
    entities = data.get("entities", [])
    for i, e in enumerate(entities):
        if e.get("slug") == slug:
            return i, e
    return None, None


def build_edit_log(old_entity: dict, new_data: dict, now_iso: str) -> list:
    entries = []
    for field in ("summary", "importanceScore", "historicalSignificance"):
        old_val = old_entity.get(field)
        new_val = new_data.get(field)
        if new_val is not None and old_val != new_val:
            entries.append({
                "field": field, "oldValue": old_val, "newValue": new_val,
                "editorId": EDITOR_ID, "timestamp": now_iso
            })
    old_details = json.loads(old_entity.get("detailsJson") or "{}")
    for field in ("causes", "effects", "relationships", "places", "subjects", "frameworks"):
        old_val = old_details.get(field, [])
        new_val = new_data.get(field, [])
        if new_val and old_val != new_val:
            entries.append({
                "field": field, "oldValue": old_val, "newValue": new_val,
                "editorId": EDITOR_ID, "timestamp": now_iso
            })
    return entries


def enrich_entity(slug: str, spec: dict, dry_run: bool = False) -> bool:
    filepath = spec["filepath"]
    new_data  = spec["data"]

    if not os.path.exists(filepath):
        print(f"  [SKIP] {slug}: file not found at {filepath}")
        return False

    with open(filepath, "r", encoding="utf-8") as fh:
        file_data = json.load(fh)

    idx, entity = find_entity_in_file(file_data, slug)
    if entity is None:
        # Try first entity in file
        if file_data.get("entities"):
            idx, entity = 0, file_data["entities"][0]
            print(f"  [NOTE] {slug}: using first entity in file (slug={entity.get('slug')})")
        else:
            print(f"  [SKIP] {slug}: entity not found in file")
            return False

    now_iso = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    # Build edit log
    edit_entries = build_edit_log(entity, new_data, now_iso)

    # Parse existing detailsJson
    existing_details = json.loads(entity.get("detailsJson") or "{}")
    existing_edit_log = existing_details.get("_editLog", [])

    # Merge details
    new_details = {**existing_details}
    for field in ("causes", "effects", "relationships", "places", "subjects",
                  "frameworks", "historicalSignificance"):
        if new_data.get(field):
            new_details[field] = new_data[field]

    new_details["_editLog"] = (existing_edit_log + edit_entries)[-50:]
    new_details["_unsyncedEdits"] = True

    # Update entity top-level fields
    entity["summary"]              = new_data.get("summary", entity.get("summary", ""))
    entity["frameworks"]           = new_data.get("frameworks", entity.get("frameworks", []))
    entity["subjects"]             = new_data.get("subjects", entity.get("subjects", []))
    entity["historicalSignificance"] = new_data.get("historicalSignificance")
    if new_data.get("importanceScore"):
        entity["importanceScore"]  = new_data["importanceScore"]
    entity["detailsJson"]          = json.dumps(new_details, ensure_ascii=False)

    if dry_run:
        summary_len = len(entity["summary"])
        print(f"  [DRY] {slug}: summary={summary_len}c, causes={len(new_details.get('causes',[]))}, rels={len(new_details.get('relationships',[]))}")
        return True

    file_data["entities"][idx] = entity
    with open(filepath, "w", encoding="utf-8") as fh:
        json.dump(file_data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    summary_len = len(entity["summary"])
    hs = new_data.get("historicalSignificance", {})
    print(f"  [OK] {slug}: {summary_len}c summary, score={hs.get('significanceScore','?')}, "
          f"causes={len(new_details.get('causes',[]))}, "
          f"rels={len(new_details.get('relationships',[]))}")
    return True


def main():
    dry_run = "--dry-run" in sys.argv
    mode = "DRY RUN" if dry_run else "LIVE"
    print(f"\n{'='*60}")
    print(f"VS CODE ENRICHMENT — Batch 02 — {mode}")
    print(f"{'='*60}")
    print(f"Entities: {len(ENRICHMENTS)}")
    print(f"Editor:   {EDITOR_ID}")
    print()

    ok = fail = 0
    for slug, spec in ENRICHMENTS.items():
        print(f"[{ok+fail+1}/{len(ENRICHMENTS)}] {slug}")
        if enrich_entity(slug, spec, dry_run=dry_run):
            ok += 1
        else:
            fail += 1

    print(f"\n{'='*60}")
    print(f"Done: {ok} enriched, {fail} failed")
    print(f"{'='*60}\n")

    if ok > 0 and not dry_run:
        print("Next steps:")
        print("  1. Run sync_gateway to push to Appwrite:")
        print("     APPWRITE_API_KEY=<key> npx tsx scripts/sync_gateway.ts --local")
        print("  2. Commit:")
        print("     git add data/appwrite-export && git commit -m 'enrichment: vscode batch 02 — 7 entities'")


if __name__ == "__main__":
    main()
