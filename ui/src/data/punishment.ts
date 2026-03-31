/* ──────────────────────────────────────────────────────────────────────────
   Corporal Punishment & Justice — The evolution of punishment, discipline,
   and justice systems from blood vengeance to restorative justice.
   ────────────────────────────────────────────────────────────────────────── */

export interface Punishment {
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

export interface PunishmentCategory {
  id: string
  label: string
  color: string
  icon: string
}

export const PUNISHMENT_CATEGORIES: PunishmentCategory[] = [
  { id: 'corporal',     label: 'Bodily Punishment (Beatings, Branding, Mutilation)', color: '#C53030', icon: 'Gavel' },
  { id: 'execution',    label: 'Capital Punishment & Execution Methods',   color: '#2D2A24', icon: 'Skull' },
  { id: 'imprisonment', label: 'Imprisonment, Exile & Forced Labor',      color: '#718096', icon: 'Lock' },
  { id: 'public',       label: 'Public Shame, Humiliation & Spectacle',   color: '#DD6B20', icon: 'Eye' },
  { id: 'legal',        label: 'Law Codes & Legal Frameworks',            color: '#4A90D9', icon: 'Scale' },
  { id: 'reform',       label: 'Punishment Reform & Abolition Movements', color: '#38A169', icon: 'Shield' },
  { id: 'religious',    label: 'Religious & Spiritual Punishment',         color: '#6B3FA0', icon: 'BookOpen' },
  { id: 'modern',       label: 'Modern Justice & Human Rights',           color: '#D4AF37', icon: 'Landmark' },
]

export const ERA_LABELS: Record<string, { label: string; color: string; period: string }> = {
  prehistoric:  { label: 'Prehistoric',     color: '#6B4D1B', period: 'Before 3,000 BCE' },
  ancient:      { label: 'Ancient World',   color: '#8B4513', period: '3,000 BCE – 500 CE' },
  medieval:     { label: 'Medieval',        color: '#A67C2E', period: '500 – 1500 CE' },
  earlyModern:  { label: 'Early Modern',    color: '#C5963A', period: '1500 – 1800 CE' },
  modern:       { label: 'Modern',          color: '#4A90D9', period: '1800 – 1945 CE' },
  contemporary: { label: 'Contemporary',    color: '#6B3FA0', period: '1945 CE – Present' },
}

export const PUNISHMENTS: Punishment[] = [
  // ═══════════════════════════════════════════════════════
  // PREHISTORIC — Before 3,000 BCE
  // ═══════════════════════════════════════════════════════

  { slug: 'blood-feud', name: 'Blood Feud & Clan Vengeance', era: 'prehistoric', category: 'corporal', subcategory: 'Collective Retaliation', origin: 'Global', civilization: 'Various', yearIntroduced: '~10,000 BCE', description: 'Before law codes, justice was personal. If someone killed your kinsman, your entire clan was obligated to take revenge — often escalating into multi-generational feuds. The cycle of retaliation could destroy both clans. This was the default "justice system" for most of human prehistory.', impact: 'Blood feuds are the oldest form of justice — and the most destructive. Every written law code in history exists to replace clan vengeance with state-controlled punishment.' },

  { slug: 'banishment', name: 'Banishment from the Group', era: 'prehistoric', category: 'imprisonment', subcategory: 'Social Exile', origin: 'Global', civilization: 'Various', yearIntroduced: '~10,000 BCE', description: 'In small-scale societies, exile was a death sentence. Being cast out meant no protection from predators, enemies, or starvation. Banishment required no prison, no guards, and no executioner — the wilderness did the work. Many cultures considered exile worse than death because it erased your social existence.', impact: 'The first form of imprisonment — confinement turned inside out. Rather than locking someone in, you locked them out. Exile remained a common punishment into the 19th century (Australia, Siberia).' },

  // ═══════════════════════════════════════════════════════
  // ANCIENT — 3,000 BCE – 500 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'hammurabi-code', name: 'Code of Hammurabi — "An Eye for an Eye"', era: 'ancient', category: 'legal', subcategory: 'First Written Law Code', origin: 'Babylon (Iraq)', civilization: 'Babylonian', yearIntroduced: '~1754 BCE', description: 'The most famous ancient law code prescribed 282 laws carved on a stone stele. "If a man puts out the eye of an equal, his eye shall be put out." But Hammurabi\'s Code was not equal — punishments varied by social class. A noble who struck a noble paid a fine; a slave who struck a noble lost an ear.', impact: 'The principle of proportional punishment (lex talionis) replaced unlimited vengeance. "An eye for an eye" was actually a restraint — you could only take one eye, not a life.' },

  { slug: 'roman-crucifixion', name: 'Roman Crucifixion', era: 'ancient', category: 'execution', subcategory: 'State Execution', origin: 'Roman Empire', civilization: 'Roman', yearIntroduced: '~500 BCE', description: 'Rome reserved crucifixion for slaves, rebels, and non-citizens — it was considered too degrading for Roman citizens. Victims were nailed or tied to wooden crosses and left to die of asphyxiation, exposure, or blood loss over hours or days. Bodies were displayed on roads as deterrents. Spartacus\' revolt ended with 6,000 crucifixions along the Appian Way.', impact: 'The most infamous execution method in history — not because of Rome, but because of Jesus of Nazareth. The cross became Christianity\'s central symbol, transforming a tool of terror into a sign of hope.' },

  { slug: 'roman-gladiatorial', name: 'Gladiatorial Execution (Damnatio ad Bestias)', era: 'ancient', category: 'public', subcategory: 'Execution as Entertainment', origin: 'Roman Empire', civilization: 'Roman', yearIntroduced: '~264 BCE', description: 'Rome turned execution into mass entertainment. Condemned criminals were torn apart by wild animals, forced to fight gladiators, or used in elaborate mythological "re-enactments" of death scenes. The Colosseum could hold 50,000 spectators watching people die. The practice continued for over 600 years.', impact: 'The merger of justice and entertainment. Rome proved that states can normalize extreme violence by packaging it as spectacle — a warning that echoes in modern media culture.' },

  { slug: 'persian-scaphism', name: 'Persian Scaphism ("The Boats")', era: 'ancient', category: 'execution', subcategory: 'Prolonged Execution', origin: 'Persia (Iran)', civilization: 'Achaemenid Persian', yearIntroduced: '~500 BCE', description: 'Described by Plutarch (possibly exaggerated): the victim was trapped between two boats, force-fed milk and honey until diarrhea began, then left in stagnant water for insects to breed in their flesh. Death came over days or weeks. Whether fully accurate or not, it reflects the ancient imagination for creative cruelty.', impact: 'Represents the extreme end of ancient punishment — designed not just to kill but to maximize suffering. Its existence (or legend) served as a deterrent across empires.' },

  { slug: 'athenian-ostracism', name: 'Athenian Ostracism', era: 'ancient', category: 'public', subcategory: 'Democratic Exile', origin: 'Athens (Greece)', civilization: 'Greek', yearIntroduced: '508 BCE', description: 'Once a year, Athenian citizens could vote to exile anyone they feared was becoming too powerful. Each voter scratched a name on a pottery shard (ostrakon). If 6,000 votes were cast, the "winner" was banished for 10 years — without loss of property or citizenship. It was democracy\'s immune system.', impact: 'The world\'s first democratic punishment. Ostracism used exile as a preventive measure against tyranny — punishing potential harm, not actual crime.' },

  { slug: 'chinese-five-punishments', name: 'Chinese Five Punishments (Wuxing)', era: 'ancient', category: 'corporal', subcategory: 'State Punishment System', origin: 'China', civilization: 'Chinese', yearIntroduced: '~2,000 BCE', description: 'Ancient China codified five escalating punishments: tattooing the face (mo), cutting off the nose (yi), cutting off a foot (yue), castration (gong), and death (da pi). The Qin Dynasty applied these ruthlessly. Later dynasties substituted some with beatings and exile, but the framework persisted for millennia.', impact: 'One of the oldest codified punishment systems. China\'s five punishments influenced legal practice across East Asia and demonstrate how states systematize violence.' },

  // ═══════════════════════════════════════════════════════
  // MEDIEVAL — 500 – 1500 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'trial-by-ordeal', name: 'Trial by Ordeal', era: 'medieval', category: 'religious', subcategory: 'Divine Judgment', origin: 'Europe / Global', civilization: 'European / Various', yearIntroduced: '~500 CE', description: 'When guilt was uncertain, God decided. Accused people plunged their hands in boiling water, gripped hot iron, or were thrown into rivers — if they survived (or sank rather than floated), God had proven their innocence. The Fourth Lateran Council abolished ordeal in 1215, forcing Europe to develop rational trial systems.', impact: 'Trial by ordeal was a sincere attempt to achieve justice through divine intervention. Its abolition forced the creation of jury trials and evidence-based law — the foundation of modern justice.' },

  { slug: 'medieval-stocks-pillory', name: 'Stocks, Pillory & Public Humiliation', era: 'medieval', category: 'public', subcategory: 'Community Shaming', origin: 'Europe', civilization: 'European', yearIntroduced: '~600 CE', description: 'Minor criminals were locked in stocks (feet restrained) or pillory (head and hands restrained) in the town square for hours or days. Townspeople threw rotten food, mud, and stones. The punishment wasn\'t just pain — it was social death. Everyone saw your shame. For small communities, this was devastating.', impact: 'Public humiliation was cheap, effective, and required no prison. It weaponized community judgment against individuals — a principle that social media has accidentally resurrected.' },

  { slug: 'inquisition', name: 'The Inquisition (Religious Tribunals)', era: 'medieval', category: 'religious', subcategory: 'Heresy Prosecution', origin: 'Europe', civilization: 'Catholic Christian', yearIntroduced: '1184 CE', description: 'The Papal Inquisition (1184), Spanish Inquisition (1478), and Roman Inquisition (1542) prosecuted heresy, witchcraft, and blasphemy. Methods included imprisonment, confiscation of property, public penance, and burning at the stake. The Spanish Inquisition was not abolished until 1834 — 650 years of religious prosecution.', impact: 'The Inquisition established the template for ideological persecution that secular totalitarian states later copied. It demonstrated that institutions designed to enforce belief inevitably become instruments of terror.' },

  { slug: 'flogging', name: 'Flogging & Whipping', era: 'medieval', category: 'corporal', subcategory: 'Beating as Punishment', origin: 'Global', civilization: 'Various', yearIntroduced: '~500 CE', description: 'The most universal corporal punishment in human history. Roman soldiers were flogged with the flagellum (metal-tipped whip). Medieval courts prescribed specific numbers of lashes. British naval discipline used the cat-o\'-nine-tails — 250 lashes could kill. Flogging was used on slaves, soldiers, prisoners, and schoolchildren worldwide.', impact: 'Flogging spans every civilization and era. It persisted in British schools until 1987, in US prisons until the mid-20th century, and remains legal in several countries today.' },

  { slug: 'wergild', name: 'Wergild — The Price of a Human Life', era: 'medieval', category: 'legal', subcategory: 'Compensatory Justice', origin: 'Germanic Europe', civilization: 'Anglo-Saxon / Germanic', yearIntroduced: '~500 CE', description: 'Germanic law set a specific monetary value (wergild) for every person based on rank. Killing a nobleman cost 1,200 shillings; a peasant, 200. Murderers paid the victim\'s family — avoiding blood feuds. Even body parts had prices: an eye, a hand, a tooth. The system converted violence into economics.', impact: 'Wergild is the ancestor of modern civil damages and wrongful death lawsuits. The idea that harm can be measured in money — and that payment replaces revenge — underlies all modern tort law.' },

  // ═══════════════════════════════════════════════════════
  // EARLY MODERN — 1500 – 1800 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'slavery-punishment', name: 'Slave Punishment Systems', era: 'earlyModern', category: 'corporal', subcategory: 'Enslaved People\'s Suffering', origin: 'Americas / Global', civilization: 'Colonial / American', yearIntroduced: '~1500 CE', description: 'Enslaved people faced whipping, branding, amputation, iron collars, salt in wounds, and forced family separation as systematic punishment. The Slave Codes legalized unlimited violence against enslaved people. Louisiana\'s Code Noir (1724) specified punishments by offense. The brutality was not incidental — it was the system.', impact: 'Slave punishment systems were among the most brutal in human history. Their legacy persists in racial disparities in modern criminal justice — the 13th Amendment explicitly permits forced labor as punishment for crime.' },

  { slug: 'guillotine', name: 'The Guillotine', era: 'earlyModern', category: 'execution', subcategory: 'Mechanized Execution', origin: 'France', civilization: 'French', yearIntroduced: '1792 CE', description: 'Dr. Joseph-Ignace Guillotin proposed a humane, egalitarian execution device — the same quick death for noble and commoner. During the Terror (1793–1794), the guillotine beheaded 16,594 people including Louis XVI and Marie Antoinette. "Madame Guillotine" became the symbol of revolutionary justice. France used it until 1977.', impact: 'The guillotine was designed as humanitarian reform — instant death instead of prolonged torture. It became instead a symbol of state terror, proving that "efficient" killing enables mass execution.' },

  { slug: 'transportation-penal', name: 'Penal Transportation (Exile Colonies)', era: 'earlyModern', category: 'imprisonment', subcategory: 'Colonial Exile', origin: 'Britain / France', civilization: 'British / French', yearIntroduced: '~1600 CE', description: 'Britain transported 162,000 convicts to Australia (1788–1868), thousands more to the American colonies. France sent prisoners to Devil\'s Island (French Guiana). Convicts provided cheap labor for colonial expansion. Transportation solved two problems: overcrowded prisons and labor-starved colonies.', impact: 'Australia\'s entire European settlement began as a prison colony. Penal transportation reveals how criminal justice and colonialism were deeply entangled.' },

  { slug: 'public-execution', name: 'Public Execution as Social Event', era: 'earlyModern', category: 'public', subcategory: 'Execution Spectacle', origin: 'Europe / Global', civilization: 'European', yearIntroduced: '~1500 CE', description: 'Public hangings drew crowds of thousands. London\'s Tyburn Tree executions were holidays — vendors sold food, pamphleteers hawked "last confessions," pickpockets worked the crowd. Drawings and quarterings were elaborate theatrical events. The condemned were expected to give a speech and die bravely.', impact: 'Public execution was the ultimate demonstration of state power. Its gradual abolition (19th–20th centuries) marks a fundamental shift in how societies conceive of justice and human dignity.' },

  { slug: 'enlightenment-reform', name: 'Beccaria\'s "On Crimes and Punishments"', era: 'earlyModern', category: 'reform', subcategory: 'Enlightenment Reform', origin: 'Italy', civilization: 'Italian / European', yearIntroduced: '1764 CE', description: 'Cesare Beccaria argued that punishment should be proportional, consistent, and aimed at deterrence — not revenge. He opposed torture, the death penalty, and secret trials. His book influenced the US Bill of Rights, the French Declaration of Rights, and every modern criminal justice system.', impact: 'The single most influential text in criminal justice history. Beccaria\'s ideas — due process, proportionality, humane punishment — are the foundation of modern human rights law.' },

  // ═══════════════════════════════════════════════════════
  // MODERN — 1800 – 1945 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'penitentiary-system', name: 'The Modern Prison (Penitentiary System)', era: 'modern', category: 'imprisonment', subcategory: 'Institutional Confinement', origin: 'United States / Britain', civilization: 'Anglo-American', yearIntroduced: '1829 CE', description: 'Eastern State Penitentiary (Philadelphia, 1829) pioneered solitary confinement as rehabilitation — prisoners lived alone in cells, reflecting on their sins (hence "penitentiary"). The Auburn System (New York) used silent group labor by day and solitary cells by night. Both systems drove many prisoners insane.', impact: 'The modern prison replaced execution and corporal punishment as the default punishment. But the reformers\' dream of rehabilitation through isolation proved psychologically devastating.' },

  { slug: 'abolition-corporal-schools', name: 'Abolition of School Corporal Punishment', era: 'modern', category: 'reform', subcategory: 'Child Protection', origin: 'Europe', civilization: 'European', yearIntroduced: '~1900 CE', description: 'For millennia, beating children was considered essential education — "spare the rod, spoil the child." Poland banned school corporal punishment in 1783 (the first country). Sweden banned all corporal punishment of children in 1979. As of 2024, 65 countries have banned it entirely. The US still permits it in 17 states.', impact: 'The abolition of hitting children is one of the most fundamental shifts in human social norms. A practice that was universal for 5,000+ years is now considered abuse in most developed nations.' },

  { slug: 'electric-chair', name: 'The Electric Chair', era: 'modern', category: 'execution', subcategory: 'Electrocution', origin: 'United States', civilization: 'American', yearIntroduced: '1890 CE', description: 'William Kemmler was the first person executed by electric chair (1890, New York). Edison promoted electrocution using Tesla\'s AC current to discredit his rival. The first execution was botched — Kemmler had to be shocked twice. Over 4,300 people were electrocuted in the US. The chair was called "Old Sparky."', impact: 'The electric chair was promoted as humane progress — technology making death painless. It instead demonstrated that "modern" and "humane" are not synonyms, anticipating debates over lethal injection.' },

  { slug: 'concentration-camps', name: 'Concentration & Forced Labor Camps', era: 'modern', category: 'imprisonment', subcategory: 'Mass Incarceration & Genocide', origin: 'Global', civilization: 'Various', yearIntroduced: '1896 CE', description: 'Spain created the first modern concentration camps in Cuba (1896). Britain used them in the Boer War (1900–1902, 28,000 deaths). Nazi Germany industrialized them — 6 million Jews and millions of others murdered. Soviet gulags held 18 million prisoners (1930–1953). Japan, China, and others operated similar systems.', impact: 'Concentration camps represent the ultimate perversion of the punishment system — punishment without crime, targeting identity rather than behavior. The Holocaust forced the creation of international human rights law.' },

  // ═══════════════════════════════════════════════════════
  // CONTEMPORARY — 1945 CE – Present
  // ═══════════════════════════════════════════════════════

  { slug: 'universal-declaration', name: 'Universal Declaration of Human Rights', era: 'contemporary', category: 'modern', subcategory: 'International Human Rights', origin: 'United Nations', civilization: 'Global', yearIntroduced: '1948 CE', description: 'Article 5: "No one shall be subjected to torture or to cruel, inhuman or degrading treatment or punishment." Drafted after the Holocaust, the UDHR established that some punishments violate human dignity regardless of the crime. It is the foundation of all modern anti-torture law.', impact: 'The first global consensus that punishment has limits. The UDHR created the legal framework for prosecuting torture, abolishing cruel punishment, and protecting prisoner rights worldwide.' },

  { slug: 'death-penalty-abolition', name: 'Global Death Penalty Abolition Movement', era: 'contemporary', category: 'reform', subcategory: 'Capital Punishment Abolition', origin: 'Europe / Global', civilization: 'Global', yearIntroduced: '~1960 CE', description: 'As of 2024, 112 countries have abolished the death penalty. The EU requires abolition for membership. The US retains it in 27 states but executions have declined 80% since the 1990s. China, Iran, Saudi Arabia, Egypt, and the US carry out the most executions. The trend is clearly toward abolition.', impact: 'The death penalty abolition movement represents the most fundamental shift in punishment philosophy in human history — the idea that the state should never kill its own citizens.' },

  { slug: 'mass-incarceration-us', name: 'US Mass Incarceration Crisis', era: 'contemporary', category: 'imprisonment', subcategory: 'Prison-Industrial Complex', origin: 'United States', civilization: 'American', yearIntroduced: '~1970 CE', description: 'The US has 2 million prisoners — 25% of the world\'s incarcerated population despite being 4% of global population. The prison population grew 500% between 1972 and 2009, driven by the "War on Drugs" and mandatory minimums. Black Americans are incarcerated at 5x the rate of white Americans. Private prisons profit from imprisonment.', impact: 'The US incarceration rate is the highest in the world — higher than Russia, China, or any authoritarian regime. Mass incarceration is widely recognized as the civil rights crisis of our era.' },

  { slug: 'restorative-justice', name: 'Restorative Justice Movement', era: 'contemporary', category: 'reform', subcategory: 'Alternative Justice', origin: 'New Zealand / Global', civilization: 'Global', yearIntroduced: '~1989 CE', description: 'New Zealand\'s Children, Young Persons, and Their Families Act (1989) incorporated Māori traditions of community-based conflict resolution. Restorative justice brings victims, offenders, and community together to repair harm rather than simply punish. Rwanda used gacaca courts to process 1.9 million genocide cases.', impact: 'Restorative justice challenges the 5,000-year assumption that punishment must mean pain. It asks: what if justice means repair instead of revenge?' },

  { slug: 'solitary-confinement-debate', name: 'Solitary Confinement Under Scrutiny', era: 'contemporary', category: 'reform', subcategory: 'Prisoner Rights', origin: 'United States / Global', civilization: 'Global', yearIntroduced: '~2010 CE', description: 'An estimated 80,000 US prisoners are in solitary confinement at any time — 22-24 hours daily in a cell the size of a parking space. The UN considers prolonged solitary confinement (15+ days) to be torture. Research shows it causes psychosis, hallucinations, and permanent brain damage. Kalief Browder\'s case (3 years at Rikers, 2 in solitary, for allegedly stealing a backpack) galvanized reform.', impact: 'Solitary confinement is being recognized as psychological torture. Its widespread use in the US represents one of the largest ongoing human rights debates in the developed world.' },
]
