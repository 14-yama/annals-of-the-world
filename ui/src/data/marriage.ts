/* ──────────────────────────────────────────────────────────────────────────
   Marriage & Union — Every major marriage custom, ceremony type, and
   legal evolution across 10,000+ years of human pair-bonding.
   ────────────────────────────────────────────────────────────────────────── */

export interface Marriage {
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

export interface MarriageCategory {
  id: string
  label: string
  color: string
  icon: string
}

export const MARRIAGE_CATEGORIES: MarriageCategory[] = [
  { id: 'ceremony',    label: 'Wedding Ceremonies & Rituals',           color: '#D4AF37', icon: 'Heart' },
  { id: 'legal',       label: 'Marriage Laws & Legal Frameworks',       color: '#4A90D9', icon: 'Scale' },
  { id: 'arranged',    label: 'Arranged & Political Marriages',         color: '#C53030', icon: 'Handshake' },
  { id: 'religious',   label: 'Religious Marriage Traditions',           color: '#6B3FA0', icon: 'Church' },
  { id: 'dowry',       label: 'Dowry, Bride Price & Gift Exchange',     color: '#DD6B20', icon: 'Gift' },
  { id: 'rights',      label: "Women's Rights & Marriage Equality",     color: '#38A169', icon: 'Shield' },
  { id: 'customs',     label: 'Courtship Customs & Betrothal',          color: '#8B6914', icon: 'Flower2' },
  { id: 'modern',      label: 'Modern Marriage & Partnership',          color: '#718096', icon: 'Users' },
]

export const ERA_LABELS: Record<string, { label: string; color: string; period: string }> = {
  prehistoric:  { label: 'Prehistoric',     color: '#6B4D1B', period: 'Before 3,000 BCE' },
  ancient:      { label: 'Ancient World',   color: '#8B4513', period: '3,000 BCE – 500 CE' },
  medieval:     { label: 'Medieval',        color: '#A67C2E', period: '500 – 1500 CE' },
  earlyModern:  { label: 'Early Modern',    color: '#C5963A', period: '1500 – 1800 CE' },
  modern:       { label: 'Modern',          color: '#4A90D9', period: '1800 – 1945 CE' },
  contemporary: { label: 'Contemporary',    color: '#6B3FA0', period: '1945 CE – Present' },
}

export const MARRIAGES: Marriage[] = [
  // ═══════════════════════════════════════════════════════
  // PREHISTORIC — Before 3,000 BCE
  // ═══════════════════════════════════════════════════════

  { slug: 'pair-bonding', name: 'Pair Bonding & Early Unions', era: 'prehistoric', category: 'ceremony', subcategory: 'Origins of Marriage', origin: 'Global', civilization: 'Various', yearIntroduced: '~10,000 BCE', description: 'The earliest evidence of formalized pair-bonding appears with settled agriculture. Before farming, human groups likely practiced fluid partnerships. With property, livestock, and inherited land, marriage became the institution that determined who inherited what.', impact: 'Marriage likely arose not from romance but from property rights. The institution that dominates human social life began as an economic contract.' },

  { slug: 'bride-capture', name: 'Marriage by Capture', era: 'prehistoric', category: 'customs', subcategory: 'Forced Marriage', origin: 'Global', civilization: 'Various', yearIntroduced: '~8,000 BCE', description: 'Raiding neighboring groups for brides was common in many prehistoric and early historic societies. This practice reinforced tribal alliances through force and is the origin of customs like carrying the bride over the threshold. Some Central Asian and African communities practiced ritual versions into the 20th century.', impact: 'One of the oldest marriage customs. Its echoes survive in wedding traditions worldwide — the "best man" originally helped the groom fight off the bride\'s family.' },

  { slug: 'exogamy-rules', name: 'Clan Exogamy Rules', era: 'prehistoric', category: 'arranged', subcategory: 'Kinship Rules', origin: 'Global', civilization: 'Various', yearIntroduced: '~7,000 BCE', description: 'Nearly all early societies developed rules requiring marriage outside one\'s own clan or kinship group (exogamy). These rules prevented inbreeding and forced alliances between groups. Violating exogamy taboos carried severe punishment — sometimes death.', impact: 'Exogamy rules are humanity\'s oldest marriage law. They forced cooperation between hostile groups and laid the foundation for complex societies.' },

  // ═══════════════════════════════════════════════════════
  // ANCIENT — 3,000 BCE – 500 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'mesopotamian-marriage', name: 'Mesopotamian Marriage Contracts', era: 'ancient', category: 'legal', subcategory: 'Written Marriage Law', origin: 'Mesopotamia (Iraq)', civilization: 'Sumerian / Babylonian', yearIntroduced: '~2,400 BCE', description: 'The world\'s oldest written marriage contracts come from Sumer. Marriage was a legal transaction between families — the groom paid a bride price (terhatum) and the bride\'s family provided a dowry. Hammurabi\'s Code (1754 BCE) codified divorce rights, adultery penalties, and inheritance rules.', impact: 'The first written marriage laws. Hammurabi\'s Code influenced marriage law across the ancient Near East and set patterns still visible in modern legal systems.' },

  { slug: 'egyptian-marriage', name: 'Egyptian Marriage Equality', era: 'ancient', category: 'rights', subcategory: 'Women\'s Property Rights', origin: 'Egypt', civilization: 'Egyptian', yearIntroduced: '~2,500 BCE', description: 'Ancient Egyptian women had unusually equal marriage rights — they could own property, initiate divorce, and enter prenuptial agreements protecting their assets. Marriage was a private contract (no state or religious ceremony required). Women kept their own names after marriage.', impact: 'Egyptian marriage was the most egalitarian in the ancient world. Women\'s marriage rights wouldn\'t be this progressive again in the West until the 19th century.' },

  { slug: 'hindu-vivaha', name: 'Hindu Vedic Wedding (Vivaha)', era: 'ancient', category: 'religious', subcategory: 'Sacred Ceremony', origin: 'India', civilization: 'Vedic / Hindu', yearIntroduced: '~1500 BCE', description: 'The Hindu Vivaha (wedding) revolves around the sacred fire (Agni). The couple walks seven steps (Saptapadi) around the fire, each step a vow. The ceremony is described in the Rigveda — making it one of the oldest continuously practiced wedding rituals. The fire god Agni serves as divine witness.', impact: 'The Saptapadi ceremony is practiced by over 1 billion Hindus today, virtually unchanged for 3,500 years. It is the longest continuously performed wedding ritual in human history.' },

  { slug: 'chinese-six-rites', name: 'Chinese Six Rites of Marriage', era: 'ancient', category: 'arranged', subcategory: 'Formalized Matchmaking', origin: 'China', civilization: 'Zhou Dynasty', yearIntroduced: '~1,000 BCE', description: 'The Zhou Dynasty codified marriage into six formal rites (liuli): proposal, birthday matching, betrothal gifts, bride price, date selection, and the wedding ceremony. A matchmaker mediated all negotiations. The bride\'s and groom\'s horoscopes had to be compatible.', impact: 'Chinese marriage customs influenced Korea, Japan, and Vietnam for millennia. The matchmaker tradition persists in modern Chinese dating culture.' },

  { slug: 'roman-marriage', name: 'Roman Marriage (Confarreatio)', era: 'ancient', category: 'legal', subcategory: 'Legal Marriage Types', origin: 'Roman Empire', civilization: 'Roman', yearIntroduced: '~500 BCE', description: 'Rome had multiple marriage forms: confarreatio (religious, for patricians), coemptio (purchase-ceremony), and usus (cohabitation for one year). Only confarreatio was religious — most Roman marriages were civil contracts. Either spouse could initiate divorce. Augustus later penalized unmarried citizens with the Lex Julia.', impact: 'Roman marriage law is the direct ancestor of Western civil marriage. The concept of marriage as a legal contract (not just a religious rite) comes from Rome.' },

  { slug: 'greek-dowry-system', name: 'Greek Dowry System', era: 'ancient', category: 'dowry', subcategory: 'Family Wealth Transfer', origin: 'Greece', civilization: 'Greek', yearIntroduced: '~800 BCE', description: 'Greek marriage required the bride\'s father to provide a substantial dowry (proix) — land, money, or goods. The dowry legally belonged to the wife but was managed by the husband. If divorced, the full dowry had to be returned. A woman without a dowry was essentially unmarriageable.', impact: 'The Greek dowry system spread throughout the Mediterranean and into Europe. Dowry customs persist in South Asia, the Middle East, and parts of Africa today.' },

  { slug: 'jewish-ketubah', name: 'Jewish Marriage Contract (Ketubah)', era: 'ancient', category: 'legal', subcategory: 'Spousal Protection', origin: 'Israel / Judea', civilization: 'Jewish', yearIntroduced: '~440 BCE', description: 'The Ketubah is a legally binding marriage contract specifying the husband\'s obligations to his wife — financial support, clothing, and conjugal rights. Uniquely, it protected the wife by requiring a substantial financial penalty for divorce. The Ketubah became legally required under Shimon ben Shetach.', impact: 'The Ketubah was revolutionary — a legal document specifically designed to protect women in marriage. Its concept influenced Islamic mahr and Christian canon law.' },

  // ═══════════════════════════════════════════════════════
  // MEDIEVAL — 500 – 1500 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'christian-sacrament', name: 'Marriage as Christian Sacrament', era: 'medieval', category: 'religious', subcategory: 'Church Control of Marriage', origin: 'Europe', civilization: 'Catholic Christian', yearIntroduced: '~1184 CE', description: 'The Council of Verona (1184) declared marriage a sacrament — indissoluble and under Church authority. Before this, marriage was largely a private/family matter. The Church required public banns, witnesses, and priestly blessing. The Fourth Lateran Council (1215) banned secret marriages.', impact: 'Transformed marriage from a family contract to a religious sacrament. The Catholic Church controlled European marriage for 800 years — divorce was impossible until the Reformation.' },

  { slug: 'islamic-nikah', name: 'Islamic Marriage Contract (Nikah)', era: 'medieval', category: 'religious', subcategory: 'Contractual Marriage', origin: 'Arabia / Islamic World', civilization: 'Islamic', yearIntroduced: '~622 CE', description: 'Islamic nikah is a civil contract (not a sacrament) requiring the bride\'s consent, witnesses, and mahr (a mandatory gift from groom to bride that remains her property). The Quran granted women inheritance and property rights within marriage — revolutionary for 7th-century Arabia. Polygyny is permitted (up to 4 wives) with conditions of equal treatment.', impact: 'Islamic marriage law gave women property rights 1,200 years before Western women achieved them. The nikah contract model influenced marriage law across Asia and Africa.' },

  { slug: 'courtly-love', name: 'Courtly Love & Romance Ideal', era: 'medieval', category: 'customs', subcategory: 'Cultural Movement', origin: 'France (Occitania)', civilization: 'European', yearIntroduced: '~1100 CE', description: 'Troubadour poets in southern France invented "courtly love" (fin\'amors) — the idea that love should be passion-driven, idealized, and devoted. Ironically, courtly love was almost always extramarital (marriages were political). Eleanor of Aquitaine\'s "courts of love" debated love\'s rules as legal cases.', impact: 'Courtly love invented romantic love as a cultural ideal. Every love song, rom-com, and Valentine\'s card descends from 12th-century troubadour poetry.' },

  { slug: 'dynastic-marriage', name: 'Dynastic & Alliance Marriages', era: 'medieval', category: 'arranged', subcategory: 'Royal & Political Marriages', origin: 'Europe / Asia', civilization: 'Multiple', yearIntroduced: '~500 CE', description: 'Royal marriages were treaties in human form. Children were betrothed as infants to seal alliances. The Habsburgs married their way to control of Europe ("Let others wage war; thou, happy Austria, marry"). Catherine de\' Medici, Eleanor of Aquitaine, and countless princesses were diplomatic currency.', impact: 'Dynastic marriage shaped the map of Europe for 1,000 years. Wars, successions, and the fate of nations turned on who married whom.' },

  { slug: 'african-lobola', name: 'African Bride Price (Lobola)', era: 'medieval', category: 'dowry', subcategory: 'Bride Wealth', origin: 'Sub-Saharan Africa', civilization: 'Bantu / Various', yearIntroduced: '~800 CE', description: 'Lobola (bride price) requires the groom\'s family to pay cattle, goods, or money to the bride\'s family. Unlike dowry (which flows from bride\'s family to groom), lobola flows to the bride\'s family as compensation for her labor and fertility. It formalizes the bond between two families, not just two individuals.', impact: 'Lobola remains widely practiced across Southern and East Africa. It\'s both celebrated as cultural tradition and debated as a barrier to marriage for poorer men.' },

  // ═══════════════════════════════════════════════════════
  // EARLY MODERN — 1500 – 1800 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'protestant-reformation-marriage', name: 'Protestant Marriage Reform', era: 'earlyModern', category: 'religious', subcategory: 'Reformation', origin: 'Germany / Europe', civilization: 'Protestant', yearIntroduced: '1525 CE', description: 'Martin Luther rejected marriage as a sacrament — calling it a "worldly thing" governed by civil law. He married a former nun (Katharina von Bora) in 1525, shocking Catholic Europe. Protestant churches allowed clergy to marry and permitted divorce for adultery or desertion.', impact: 'The Reformation broke the Catholic monopoly on marriage. Luther\'s reforms laid groundwork for civil marriage and modern divorce law.' },

  { slug: 'marriage-act-1753', name: 'English Marriage Act (Lord Hardwicke\'s)', era: 'earlyModern', category: 'legal', subcategory: 'State Regulation', origin: 'England', civilization: 'British', yearIntroduced: '1753 CE', description: 'The first law requiring marriages to be performed in church, by a licensed clergyman, with parental consent for those under 21. It ended secret marriages (like those at Fleet Prison) and clandestine elopements. Scotland\'s non-adoption created Gretna Green — the famous runaway wedding destination.', impact: 'The first state regulation of marriage in the English-speaking world. Established the legal requirements (license, ceremony, registration) that persist globally today.' },

  { slug: 'japanese-miai', name: 'Japanese Arranged Marriage (Miai)', era: 'earlyModern', category: 'arranged', subcategory: 'Formal Matchmaking', origin: 'Japan', civilization: 'Japanese', yearIntroduced: '~1600 CE', description: 'The Tokugawa Era formalized miai — arranged meetings between potential spouses mediated by a nakodo (go-between). Families exchanged gifts (yuino), verified social status, and negotiated terms. Love was considered irrelevant; duty and family harmony mattered. Miai dominated Japanese marriage until the 1960s.', impact: 'Miai shaped Japanese society for 400 years. Even today, about 5-6% of Japanese marriages begin through formal arranged meetings.' },

  { slug: 'slave-marriage-ban', name: 'Denial of Marriage to Enslaved People', era: 'earlyModern', category: 'rights', subcategory: 'Marriage Prohibition', origin: 'Americas', civilization: 'Colonial / American', yearIntroduced: '~1660 CE', description: 'Enslaved people in the Americas were legally denied marriage because they were classified as property, not persons. "Jumping the broom" became a symbolic marriage ceremony. Slave owners could separate married couples at will — an estimated one-third of slave marriages were destroyed by forced sale.', impact: 'The denial of marriage was a cornerstone of slavery\'s dehumanization. Its legacy persists in disparities in Black marriage rates and family structures.' },

  // ═══════════════════════════════════════════════════════
  // MODERN — 1800 – 1945 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'married-womens-property', name: 'Married Women\'s Property Acts', era: 'modern', category: 'rights', subcategory: 'Legal Equality', origin: 'United States / England', civilization: 'Anglo-American', yearIntroduced: '1839 CE', description: 'Under English common law (coverture), a married woman had no separate legal existence — her property, earnings, and even her body belonged to her husband. Mississippi (1839) passed the first Married Women\'s Property Act. England followed in 1870 and 1882. These acts slowly restored women\'s legal personhood.', impact: 'Ended one of the most oppressive legal doctrines in Western history. For the first time in centuries, married women could own property, sign contracts, and keep their earnings.' },

  { slug: 'white-wedding', name: 'The White Wedding Tradition', era: 'modern', category: 'ceremony', subcategory: 'Fashion & Ritual', origin: 'England', civilization: 'British / Western', yearIntroduced: '1840 CE', description: 'Queen Victoria wore white at her 1840 wedding to Prince Albert — breaking the tradition of colorful wedding dresses. White symbolized wealth (only the rich could keep white clean), not purity (that association came later). Photography spread the image. Within a generation, white weddings became the global standard.', impact: 'One person\'s fashion choice became a worldwide tradition. The white wedding dress is now the default in dozens of cultures that never had the tradition before.' },

  { slug: 'civil-marriage-france', name: 'Civil Marriage (State-Only Weddings)', era: 'modern', category: 'legal', subcategory: 'Secularization', origin: 'France / Europe', civilization: 'French / European', yearIntroduced: '1804 CE', description: 'Napoleon\'s Civil Code made civil marriage mandatory — religious ceremonies were optional and had no legal standing. Marriage became a contract between citizens and the state, not between souls and God. Most European countries followed: Germany (1875), Switzerland (1874), Turkey (1926).', impact: 'Separated marriage from religion permanently. Civil marriage is now the legal standard worldwide — even in highly religious countries.' },

  { slug: 'interracial-marriage-bans', name: 'Anti-Miscegenation Laws', era: 'modern', category: 'rights', subcategory: 'Racial Restrictions', origin: 'United States / Colonial', civilization: 'American / Colonial', yearIntroduced: '1691 CE', description: 'Virginia banned interracial marriage in 1691. By 1924, 30 US states prohibited marriage between white and non-white people. Nazi Germany\'s Nuremberg Laws (1935) banned marriages between Jews and non-Jews. These laws were tools of racial hierarchy masked as "protecting" marriage.', impact: 'Anti-miscegenation laws persisted until Loving v. Virginia (1967). The fight to overturn them became a precedent for same-sex marriage rights.' },

  { slug: 'arranged-marriage-decline', name: 'Rise of Love Marriage', era: 'modern', category: 'customs', subcategory: 'Cultural Shift', origin: 'Western World', civilization: 'Western', yearIntroduced: '~1800 CE', description: 'The Enlightenment and Romantic movement transformed marriage from an economic arrangement to an emotional bond. By 1900, "love matches" were the norm in the West. This was revolutionary — for most of human history, marrying for love was considered foolish or dangerous.', impact: 'The biggest shift in marriage history. Love marriage, now the global ideal, is barely 200 years old. Most human marriages throughout history were arranged.' },

  // ═══════════════════════════════════════════════════════
  // CONTEMPORARY — 1945 CE – Present
  // ═══════════════════════════════════════════════════════

  { slug: 'marriage-equality', name: 'Same-Sex Marriage Legalization', era: 'contemporary', category: 'rights', subcategory: 'LGBTQ+ Rights', origin: 'Netherlands / Global', civilization: 'Global', yearIntroduced: '2001 CE', description: 'The Netherlands became the first country to legalize same-sex marriage in 2001. By 2024, 35 countries recognize it — including the US (Obergefell v. Hodges, 2015), all of Western Europe, Taiwan, and parts of Latin America. The movement went from criminal to legal in one generation.', impact: 'The fastest expansion of marriage rights in history. Same-sex marriage is now a defining civil rights issue and a marker of democratic progress.' },

  { slug: 'no-fault-divorce', name: 'No-Fault Divorce', era: 'contemporary', category: 'legal', subcategory: 'Divorce Reform', origin: 'Soviet Union / United States', civilization: 'Global', yearIntroduced: '1969 CE', description: 'California\'s Family Law Act (1969) introduced no-fault divorce — ending the requirement to prove adultery, cruelty, or abandonment. (Soviet Russia had it since 1917.) By 2010, no-fault divorce was available in all 50 US states and most Western countries. England finally adopted it in 2022.', impact: 'Divorce rates initially doubled, then stabilized. No-fault divorce gave women an exit from abusive marriages without public humiliation or perjury.' },

  { slug: 'indian-dowry-prohibition', name: 'India Dowry Prohibition Act', era: 'contemporary', category: 'dowry', subcategory: 'Legal Reform', origin: 'India', civilization: 'Indian', yearIntroduced: '1961 CE', description: 'India banned dowry demands in 1961 after a surge in "dowry deaths" — brides murdered or driven to suicide when their families couldn\'t pay. Despite the ban, dowry remains widespread: an estimated $130 billion in dowries are exchanged annually in India. Enforcement remains weak.', impact: 'Proved that laws alone cannot end entrenched customs. India\'s dowry crisis highlights the gap between legal reform and cultural practice.' },

  { slug: 'cohabitation-revolution', name: 'Cohabitation Revolution', era: 'contemporary', category: 'modern', subcategory: 'Partnership Without Marriage', origin: 'Scandinavia / Western World', civilization: 'Western', yearIntroduced: '~1970 CE', description: 'Sweden led the cohabitation revolution — by 2020, over 60% of Swedish first children are born to unmarried cohabiting parents. Across the West, cohabitation has replaced marriage as the first union for most couples. Some countries (France\'s PACS, UK civil partnerships) created legal alternatives to marriage.', impact: 'Marriage is becoming optional. In many Western countries, fewer than half of adults are married — the lowest rate in recorded history.' },

  { slug: 'child-marriage-ban', name: 'Global Campaign Against Child Marriage', era: 'contemporary', category: 'rights', subcategory: 'Child Protection', origin: 'Global', civilization: 'Global', yearIntroduced: '~2000 CE', description: 'UNICEF estimates 650 million women alive today were married before age 18. Child marriage rates are declining but remain high in Sub-Saharan Africa and South Asia. The UN Sustainable Development Goals target elimination by 2030. Despite laws, enforcement is weak — poverty and cultural norms drive the practice.', impact: 'Child marriage deprives girls of education, health, and autonomy. Ending it is recognized as one of the most effective interventions for global development.' },

  { slug: 'online-dating', name: 'Online Dating & Algorithmic Matchmaking', era: 'contemporary', category: 'modern', subcategory: 'Digital Courtship', origin: 'United States / Global', civilization: 'Global', yearIntroduced: '1995 CE', description: 'Match.com (1995) and subsequent apps (eHarmony, Tinder, Bumble, Hinge) transformed how people meet partners. By 2023, over 40% of US couples meet online — more than any other method. Algorithms now play matchmaker, replacing family, friends, and community.', impact: 'The most fundamental change in courtship since the love marriage revolution. Algorithms are now the world\'s most prolific matchmakers.' },
]
