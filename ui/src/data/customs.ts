/* ──────────────────────────────────────────────────────────────────────────
   Customs & Traditions — The rituals, social rules, and cultural practices
   that defined daily life across civilizations and centuries.
   ────────────────────────────────────────────────────────────────────────── */

export interface Custom {
  slug: string
  name: string
  era: string
  category: string
  subcategory: string
  origin: string
  civilization: string
  yearIntroduced: string
  description: string
  impact: string
}

export interface CustomCategory {
  id: string
  label: string
  color: string
  icon: string
}

export const CUSTOM_CATEGORIES: CustomCategory[] = [
  { id: 'death',       label: 'Death, Burial & Mourning Rites',       color: '#718096', icon: 'Skull' },
  { id: 'food',        label: 'Feasting, Fasting & Food Customs',     color: '#DD6B20', icon: 'UtensilsCrossed' },
  { id: 'greeting',    label: 'Greetings, Gestures & Etiquette',      color: '#4A90D9', icon: 'HandMetal' },
  { id: 'rites',       label: 'Coming-of-Age & Initiation Rites',     color: '#C53030', icon: 'Flame' },
  { id: 'festival',    label: 'Festivals, Holidays & Celebrations',   color: '#D4AF37', icon: 'PartyPopper' },
  { id: 'taboo',       label: 'Taboos, Superstitions & Prohibitions', color: '#2D2A24', icon: 'Ban' },
  { id: 'hospitality', label: 'Hospitality & Guest Customs',          color: '#38A169', icon: 'Home' },
  { id: 'social',      label: 'Social Hierarchy & Status Customs',    color: '#6B3FA0', icon: 'Crown' },
]

export const ERA_LABELS: Record<string, { label: string; color: string; period: string }> = {
  prehistoric:  { label: 'Prehistoric',     color: '#6B4D1B', period: 'Before 3,000 BCE' },
  ancient:      { label: 'Ancient World',   color: '#8B4513', period: '3,000 BCE – 500 CE' },
  medieval:     { label: 'Medieval',        color: '#A67C2E', period: '500 – 1500 CE' },
  earlyModern:  { label: 'Early Modern',    color: '#C5963A', period: '1500 – 1800 CE' },
  modern:       { label: 'Modern',          color: '#4A90D9', period: '1800 – 1945 CE' },
  contemporary: { label: 'Contemporary',    color: '#6B3FA0', period: '1945 CE – Present' },
}

export const CUSTOMS: Custom[] = [
  // ═══════════════════════════════════════════════════════
  // PREHISTORIC — Before 3,000 BCE
  // ═══════════════════════════════════════════════════════

  { slug: 'deliberate-burial', name: 'Intentional Burial of the Dead', era: 'prehistoric', category: 'death', subcategory: 'Funeral Origins', origin: 'Global', civilization: 'Neanderthal / Homo sapiens', yearIntroduced: '~100,000 BCE', description: 'The oldest known intentional burials date to ~100,000 BCE (Qafzeh Cave, Israel). Bodies were placed in fetal position, sometimes with tools, flowers, and red ochre. Neanderthals also buried their dead — suggesting this custom may predate modern humans.', impact: 'The beginning of all funeral custom. Deliberate burial implies belief in an afterlife — making it the oldest evidence of human spirituality.' },

  { slug: 'cave-painting-ritual', name: 'Cave Art as Collective Ritual', era: 'prehistoric', category: 'rites', subcategory: 'Spiritual Ceremony', origin: 'Europe / Global', civilization: 'Upper Paleolithic', yearIntroduced: '~40,000 BCE', description: 'Lascaux, Altamira, and Chauvet caves were not homes — they were ritual spaces. Hand stencils, animal paintings, and geometric symbols were created by firelight in inaccessible chambers. Evidence suggests initiation ceremonies, shamanic trances, and collective rituals.', impact: 'The first known group rituals. Cave art proves that shared ceremony — gathering together for a symbolic purpose — is as old as modern human culture.' },

  { slug: 'food-sharing-customs', name: 'Communal Feasting', era: 'prehistoric', category: 'food', subcategory: 'Shared Meals', origin: 'Global', civilization: 'Various', yearIntroduced: '~12,000 BCE', description: 'The earliest evidence of large-scale communal feasting comes from Natufian sites in the Levant. Hundreds of people gathered to eat, drink, and celebrate. Göbekli Tepe (11,000 BCE) may have been built specifically for feasting — the first purpose-built banquet hall.', impact: 'Communal feasting may have driven the invention of agriculture and architecture. People didn\'t settle down to farm — they farmed so they could feast together.' },

  { slug: 'hospitality-sacred', name: 'Sacred Duty of Hospitality', era: 'prehistoric', category: 'hospitality', subcategory: 'Guest Rights', origin: 'Global', civilization: 'Various', yearIntroduced: '~10,000 BCE', description: 'Nearly every ancient culture held hospitality as a sacred duty. Refusing food and shelter to a stranger violated divine law — Greek xenia, Arabic diyafa, Norse gestrisni. Travelers depended on this custom for survival in a world without inns, roads, or police.', impact: 'Hospitality customs enabled trade, migration, and cultural exchange across vast distances. Without sacred hospitality, the ancient world could not have functioned.' },

  // ═══════════════════════════════════════════════════════
  // ANCIENT — 3,000 BCE – 500 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'egyptian-mummification', name: 'Egyptian Mummification', era: 'ancient', category: 'death', subcategory: 'Preservation of the Dead', origin: 'Egypt', civilization: 'Egyptian', yearIntroduced: '~2,600 BCE', description: 'The Egyptians perfected body preservation over 3,000 years. Full mummification took 70 days: organ removal (except the heart), natron drying, linen wrapping, and ritual prayers. Only the wealthy could afford it — peasants were simply buried in desert sand. The process preserved bodies for millennia.', impact: 'History\'s most elaborate death custom. Egyptian mummification drove advances in chemistry, anatomy, and medicine that benefited the living.' },

  { slug: 'olympic-games-ancient', name: 'Greek Olympic Games', era: 'ancient', category: 'festival', subcategory: 'Athletic Festival', origin: 'Greece (Olympia)', civilization: 'Greek', yearIntroduced: '776 BCE', description: 'Held every four years at Olympia in honor of Zeus. Athletes competed nude, women were banned from attending, and all Greek wars paused during the Olympic Truce (ekecheiria). Winners received only olive wreaths — but became heroes in their home city-states. The Games ran continuously for 1,168 years.', impact: 'The longest-running sporting event in history. The Olympics demonstrated that shared ritual could unite warring peoples — an idea the modern Olympics revived in 1896.' },

  { slug: 'roman-saturnalia', name: 'Roman Saturnalia Festival', era: 'ancient', category: 'festival', subcategory: 'Winter Festival', origin: 'Roman Empire', civilization: 'Roman', yearIntroduced: '~217 BCE', description: 'A week-long December festival where social rules were inverted: masters served slaves, gambling was permitted, gifts were exchanged, and candles lit the long nights. Public business halted and schools closed. The Christian church later absorbed Saturnalia\'s customs into Christmas.', impact: 'Most Christmas traditions — gift-giving, candles, feasting, decoration — come directly from Saturnalia. The Romans invented the modern holiday season.' },

  { slug: 'caste-system-india', name: 'Indian Caste System (Varna)', era: 'ancient', category: 'social', subcategory: 'Hereditary Social Hierarchy', origin: 'India', civilization: 'Vedic / Hindu', yearIntroduced: '~1500 BCE', description: 'The Rigveda describes four varnas: Brahmins (priests), Kshatriyas (warriors), Vaishyas (merchants), Shudras (laborers). Below all were the "untouchables" (Dalits). Caste determined occupation, marriage partners, diet, and social contact. Violation meant severe social punishment or ostracism.', impact: 'The most elaborate social hierarchy in human history. Despite legal abolition (1950), caste still shapes Indian marriage, politics, and daily life for 1.4 billion people.' },

  { slug: 'chinese-ancestor-worship', name: 'Chinese Ancestor Veneration', era: 'ancient', category: 'death', subcategory: 'Ongoing Spirit Care', origin: 'China', civilization: 'Chinese', yearIntroduced: '~1,500 BCE', description: 'The Shang Dynasty formalized ancestral veneration — the belief that dead family members influence the living. Families made regular offerings of food, drink, and "spirit money" at ancestral altars. The Qingming (Tomb Sweeping) Festival brought entire families to clean graves and present offerings.', impact: 'Ancestor worship shaped Chinese family structure, ethics, and governance for 3,500 years. Confucian filial piety — the duty to honor parents and ancestors — remains a cornerstone of East Asian culture.' },

  { slug: 'roman-handshake', name: 'The Handshake', era: 'ancient', category: 'greeting', subcategory: 'Trust Gesture', origin: 'Greece / Rome', civilization: 'Greco-Roman', yearIntroduced: '~500 BCE', description: 'Originally a gesture proving you carried no weapon — grasping the right (sword) hand showed peaceful intent. Roman reliefs show handshakes sealing treaties and business deals. The custom spread with the Roman Empire and became the default Western greeting.', impact: 'The world\'s most common greeting gesture (pre-COVID). The handshake crossed every cultural boundary and became the universal seal of agreement.' },

  { slug: 'food-taboos', name: 'Dietary Laws & Food Taboos', era: 'ancient', category: 'taboo', subcategory: 'Forbidden Foods', origin: 'Multiple Regions', civilization: 'Jewish / Hindu / Various', yearIntroduced: '~1,300 BCE', description: 'Jewish kashrut laws banned pork, shellfish, and mixing meat with dairy. Hindu customs prohibited beef (cows are sacred). Islamic halal rules later mirrored many kashrut restrictions. These weren\'t about health — they were identity markers separating "us" from "them."', impact: 'Food taboos are among the most powerful cultural markers in human history. They define religious identity, trigger wars, and persist for millennia with remarkable tenacity.' },

  // ═══════════════════════════════════════════════════════
  // MEDIEVAL — 500 – 1500 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'feudal-oath', name: 'Feudal Oath of Fealty', era: 'medieval', category: 'social', subcategory: 'Loyalty Ritual', origin: 'Europe', civilization: 'European', yearIntroduced: '~800 CE', description: 'A vassal knelt, placed his hands between his lord\'s hands, and swore loyalty unto death. In exchange, the lord granted land (a fief) and protection. This ritual — homage and investiture — was the social contract that held medieval Europe together. Breaking the oath was the ultimate crime.', impact: 'Feudal oaths structured European society for 700 years. The ritual of swearing loyalty with hands clasped persists in courtroom oaths today.' },

  { slug: 'japanese-tea-ceremony', name: 'Japanese Tea Ceremony (Chanoyu)', era: 'medieval', category: 'hospitality', subcategory: 'Ritualized Hospitality', origin: 'Japan', civilization: 'Japanese', yearIntroduced: '~1400 CE', description: 'Sen no Rikyū perfected chanoyu — the ritualized preparation and serving of matcha tea. Every gesture, utensil, and silence carries meaning. The tiny tea room equalizes all guests — samurai and merchants sit together. The four principles: harmony (wa), respect (kei), purity (sei), tranquility (jaku).', impact: 'The most refined hospitality ritual ever developed. The tea ceremony influenced Japanese architecture, pottery, flower arrangement, and the global concept of mindfulness.' },

  { slug: 'ramadan-fasting', name: 'Ramadan Fasting', era: 'medieval', category: 'food', subcategory: 'Religious Fasting', origin: 'Arabia / Islamic World', civilization: 'Islamic', yearIntroduced: '624 CE', description: 'Muslims fast from dawn to sunset during the month of Ramadan — no food, water, smoking, or sexual activity. The fast builds empathy with the hungry, demonstrates self-discipline, and creates communal solidarity. Iftar (the evening meal breaking fast) is a major social event, often shared with strangers.', impact: 'Practiced by 1.8 billion Muslims annually. Ramadan is the largest simultaneous act of collective self-discipline in human history.' },

  { slug: 'samurai-bushido', name: 'Bushido — The Way of the Warrior', era: 'medieval', category: 'social', subcategory: 'Honor Code', origin: 'Japan', civilization: 'Japanese', yearIntroduced: '~1200 CE', description: 'Bushido codified the samurai honor code: loyalty, frugality, martial skill, and honor unto death. Seppuku (ritual suicide) was required rather than face capture or dishonor. A samurai\'s two swords (daisho) were his soul. The code governed behavior, dress, speech, and even how to die.', impact: 'Bushido shaped Japanese national character long after the samurai class was abolished (1876). Its emphasis on duty, honor, and loyalty persists in Japanese corporate and social culture.' },

  { slug: 'pilgrimage-custom', name: 'Religious Pilgrimage', era: 'medieval', category: 'rites', subcategory: 'Sacred Journey', origin: 'Global', civilization: 'Multiple', yearIntroduced: '~700 CE', description: 'The Hajj (Mecca), Camino de Santiago (Spain), Canterbury (England), and Varanasi (India) drew millions of pilgrims. Pilgrimage was both spiritual obligation and international adventure — travelers crossed continents, shared stories, and spread ideas. Chaucer\'s Canterbury Tales captures the social mixing.', impact: 'Pilgrimage created the world\'s first tourism industry. It drove road construction, inn-keeping, mapmaking, and cross-cultural exchange on an enormous scale.' },

  // ═══════════════════════════════════════════════════════
  // EARLY MODERN — 1500 – 1800 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'bow-curtsy', name: 'Bowing & Curtseying as Social Protocol', era: 'earlyModern', category: 'greeting', subcategory: 'Court Etiquette', origin: 'Europe / East Asia', civilization: 'European / East Asian', yearIntroduced: '~1500 CE', description: 'European court etiquette reached extreme elaboration — the depth of a bow or curtsy communicated exact social rank. Louis XIV\'s Versailles had rules for every gesture. Japanese bowing has 3 levels (15°, 30°, 45°). These customs encoded social hierarchy into physical movement.', impact: 'Bowing survives in Japan, Korea, and formal Western contexts. It demonstrates that greeting customs are not about friendliness — they\'re about power and rank.' },

  { slug: 'dueling-honor', name: 'Dueling as Honor Culture', era: 'earlyModern', category: 'social', subcategory: 'Honor Defense', origin: 'Europe / Americas', civilization: 'European', yearIntroduced: '~1500 CE', description: 'When insulted, European gentlemen were expected to issue a formal challenge (via "seconds") and fight with swords or pistols. Refusing meant social death. Hundreds of thousands died in duels — including Alexander Hamilton (1804). France lost an estimated 10,000 aristocrats to dueling between 1589 and 1610.', impact: 'Dueling defined aristocratic masculinity for 400 years. Its decline tracks the rise of law courts and the idea that the state — not the individual — should resolve disputes.' },

  { slug: 'witch-trial-mania', name: 'Witch Trial Hysteria', era: 'earlyModern', category: 'taboo', subcategory: 'Moral Panic', origin: 'Europe / Americas', civilization: 'European / Colonial', yearIntroduced: '~1450 CE', description: 'Between 1450 and 1750, an estimated 40,000–60,000 people were executed for witchcraft — 80% women. The Malleus Maleficarum (1487) provided a handbook. Salem (1692) is famous, but the real epicenter was Europe. Accusations often targeted healers, widows, and social outsiders.', impact: 'The largest moral panic in European history. Witch trials reveal how fear, misogyny, and social anxiety can hijack legal systems with lethal results.' },

  { slug: 'coffeehouse-culture', name: 'Coffeehouse Culture', era: 'earlyModern', category: 'food', subcategory: 'Social Gathering', origin: 'Ottoman Empire → Europe', civilization: 'Ottoman / European', yearIntroduced: '~1550 CE', description: 'Ottoman coffeehouses (kahvehane) were spaces for conversation, chess, and news. London\'s coffeehouses (from 1652) became "penny universities" where anyone could sit, debate, and hear the latest ideas. Lloyd\'s of London started as a coffeehouse. The French Revolution was planned in Parisian cafés.', impact: 'Coffeehouses created the public sphere — spaces where strangers discussed politics, business, and ideas as equals. Democratic debate owes as much to coffee as to philosophy.' },

  // ═══════════════════════════════════════════════════════
  // MODERN — 1800 – 1945 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'tipping-custom', name: 'Tipping Custom', era: 'modern', category: 'hospitality', subcategory: 'Service Gratuity', origin: 'England → United States', civilization: 'Anglo-American', yearIntroduced: '~1840 CE', description: 'Tipping originated in English coffeehouses (boxes labeled "To Insure Promptness"). Americans adopted it after the Civil War — restaurant owners used tips to avoid paying freed Black workers wages. Anti-tipping movements repeatedly failed. Today, US servers depend on tips for 60%+ of income.', impact: 'Tipping is uniquely American in its extremity. It created a two-tier wage system that most other developed nations have rejected as exploitative.' },

  { slug: 'christmas-modern', name: 'The Invention of Modern Christmas', era: 'modern', category: 'festival', subcategory: 'Holiday Reinvention', origin: 'Britain / United States', civilization: 'Western', yearIntroduced: '~1843 CE', description: 'Dickens\' "A Christmas Carol" (1843), Prince Albert\'s Christmas tree (1848), and Coca-Cola\'s Santa Claus (1931) invented Christmas as we know it. Before the Victorians, Christmas was a rowdy street festival, not a family gathering. The Puritans had actually banned it (1647-1660).', impact: 'Modern Christmas is a Victorian invention less than 200 years old. It is now the world\'s largest annual commercial and cultural event.' },

  { slug: 'national-anthem-standing', name: 'Standing for National Anthems', era: 'modern', category: 'social', subcategory: 'Patriotic Ritual', origin: 'Europe / Global', civilization: 'Global', yearIntroduced: '~1800 CE', description: 'Standing during the national anthem became customary in the 19th century as nation-states replaced empires. The custom signals loyalty, unity, and respect for the state. Refusing to stand (like Colin Kaepernick in 2016) is considered deeply transgressive — proving the custom\'s power.', impact: 'A simple physical gesture that encodes national identity, loyalty, and political conformity. Standing customs demonstrate how bodily ritual enforces social cohesion.' },

  { slug: 'halloween-evolution', name: 'Halloween as Commercial Holiday', era: 'modern', category: 'festival', subcategory: 'Celtic-to-Commercial', origin: 'Ireland → United States', civilization: 'Irish-American', yearIntroduced: '~1900 CE', description: 'Samhain (Celtic festival of the dead) merged with All Hallows\' Eve (Christian). Irish immigrants brought it to America. Trick-or-treating began in the 1930s. By 2023, Americans spend $12.2 billion annually on Halloween — costumes, candy, and decorations. It is the second-largest US commercial holiday.', impact: 'The transformation from ancient death ritual to commercial spectacle in 100 years. Halloween exemplifies how capitalism absorbs and repurposes sacred customs.' },

  // ═══════════════════════════════════════════════════════
  // CONTEMPORARY — 1945 CE – Present
  // ═══════════════════════════════════════════════════════

  { slug: 'black-friday', name: 'Black Friday & Consumerist Rituals', era: 'contemporary', category: 'festival', subcategory: 'Commercial Ritual', origin: 'United States / Global', civilization: 'Global', yearIntroduced: '~1960 CE', description: 'The day after Thanksgiving became the biggest shopping day in the US. By 2020, Black Friday had spread globally — even to countries without Thanksgiving. Lines, stampedes, and fights over discounted TVs became annual media spectacles. Singles\' Day (China, 11/11) now dwarfs Black Friday with $84 billion in sales (2024).', impact: 'Shopping has become ritual. Black Friday and Singles\' Day reveal that consumer capitalism has created its own sacred calendar of high holy days.' },

  { slug: 'social-media-customs', name: 'Social Media Etiquette & Digital Customs', era: 'contemporary', category: 'greeting', subcategory: 'Digital Social Norms', origin: 'Global', civilization: 'Global', yearIntroduced: '~2005 CE', description: 'New customs evolved for digital life: following/unfollowing etiquette, "likes" as social currency, ghosting, posting birthday wishes publicly, announcing life events via social media before telling family. These customs emerged organically and evolve constantly — yesterday\'s norm is today\'s cringe.', impact: 'Humanity\'s first truly global customs, shared across all cultures simultaneously. Digital etiquette changes faster than any previous social norm system.' },

  { slug: 'gender-reveal-parties', name: 'Gender Reveal Parties', era: 'contemporary', category: 'rites', subcategory: 'Modern Birth Ritual', origin: 'United States', civilization: 'American', yearIntroduced: '2008 CE', description: 'Blogger Jenna Karvunidis cut a cake with pink filling to reveal her baby\'s sex — and created a global phenomenon. Gender reveals escalated into fireworks, skydiving, and (in one case) a California wildfire. Karvunidis later regretted the trend as her daughter came out as non-binary.', impact: 'A custom that went from zero to global in 15 years, then faced backlash. Gender reveal parties illustrate how quickly modern customs can form, spread, and become controversial.' },

  { slug: 'death-doula', name: 'Death Doulas & Modern Death Customs', era: 'contemporary', category: 'death', subcategory: 'End-of-Life Reimagining', origin: 'United States / Global', civilization: 'Global', yearIntroduced: '~2010 CE', description: 'The "death positive" movement challenges Western death denial. Death doulas guide the dying and their families. Green burials (no embalming, biodegradable caskets) are growing. Home funerals are legal in most US states. The movement asks: after a century of medicalizing death, have we forgotten how to die?', impact: 'A counter-cultural movement reconnecting modern people with death customs their great-grandparents practiced naturally. Death is being reclaimed from hospitals and funeral homes.' },
]
