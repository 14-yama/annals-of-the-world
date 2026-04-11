import type { Entity } from '../entityTypes'

/**
 * Division 780 — Historical & Literary Texts (hand-curated expansion)
 * Foundational written works across eras and regions.
 */
export const DIV_780_ENTITIES: Entity[] = [

  {
    slug: 'muqaddimah_ibn_khaldun',
    name: 'Muqaddimah (Ibn Khaldun)',
    label: 'Text',
    callNumber: '780.04-muqaddimah-ibn-khaldun',
    subjectHeadings: ['Texts — Historical & Literary — Tunisia — Medieval'],
    subjects: ['History', 'Sociology', 'Historiography', 'Ibn Khaldun', 'Asabiyyah', 'Civilizations'],
    summary: 'Written in 1377 by the North African polymath Ibn Khaldun, the Muqaddimah ("Introduction") is widely considered the foundational work of sociology, historiography, and economic theory. It introduces the concept of \'asabiyyah (group solidarity) as the driving force of civilizational rise and decline, analyzes economic cycles, and criticizes uncritical historical methods — centuries before Enlightenment thinkers addressed the same questions.',
    period: '1377',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    frameworks: ['CAUSE_AND_EFFECT', 'ECONOMIC_SYSTEMS', 'CULTURAL_DIFFUSION', 'TEXTUAL_TRANSMISSION'],
    causes: [
      { title: 'Decline of Islamic civilization after Mongol invasions', type: 'EventWindow', year: '13th–14th century' },
      { title: 'Need for scientific approach to history', type: 'Idea', year: '14th century' },
    ],
    effects: [
      { title: 'Sociology and historiography as disciplines anticipated', type: 'Idea', year: '1377' },
      { title: 'Rediscovered by European scholars in 19th century', type: 'EventWindow', year: '1800s' },
      { title: 'Influenced Toynbee, Gellner, and modern conflict theory', type: 'Movement', year: '20th century' },
    ],
    relationships: [
      { sourceSlug: 'muqaddimah_ibn_khaldun', sourceName: 'Muqaddimah', verb: 'OCCURS_IN', targetSlug: 'tunisia', targetName: 'Tunisia', context: 'Written in Tunis, 1377' },
      { sourceSlug: 'muqaddimah_ibn_khaldun', sourceName: 'Muqaddimah', verb: 'OCCURS_IN', targetSlug: 'algeria', targetName: 'Algeria', context: 'Partly written at Qal\'at Ibn Salama' },
    ],
    places: [
      { name: 'Tunis', role: 'Place of composition' },
      { name: 'Qal\'at Ibn Salama', role: 'Fortress retreat where writing began' },
    ],
    texts: [
      { title: 'Kitab al-Ibar (Book of Lessons)', type: 'Full history for which Muqaddimah is the introduction' },
    ],
  },

  {
    slug: 'histories_herodotus',
    name: 'The Histories (Herodotus)',
    label: 'Text',
    callNumber: '780.05-histories-herodotus',
    subjectHeadings: ['Texts — Historical & Literary — Greece — Classical'],
    subjects: ['History', 'Persia', 'Greece', 'Persian Wars', 'Ethnography', 'Herodotus'],
    summary: 'Written c. 430 BCE, "The Histories" by Herodotus of Halicarnassus is the first great work of historical prose in Western literature. Covering the Greco-Persian Wars (499–479 BCE), it ranges across Egypt, Persia, Scythia, and Libya with ethnographic curiosity. Cicero called him the "Father of History" — though critics call him the "Father of Lies" for his blend of fact and fable.',
    period: 'c. 430 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Southern Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION', 'CAUSE_AND_EFFECT', 'CONFLICT_AND_RESOLUTION'],
    causes: [
      { title: 'Greco-Persian Wars demand explanation and commemoration', type: 'EventWindow', year: '499–479 BCE' },
      { title: 'Ionian intellectual tradition of inquiry (historia)', type: 'Movement', year: '6th–5th century BCE' },
    ],
    effects: [
      { title: 'Western historical writing born as a genre', type: 'Idea', year: 'c. 430 BCE' },
      { title: 'Thucydides refines method into "scientific" history', type: 'Text', year: 'c. 400 BCE' },
      { title: 'Primary source for Persian Empire, Egypt, and Scythian history', type: 'Text', year: 'c. 430 BCE' },
    ],
    relationships: [
      { sourceSlug: 'histories_herodotus', sourceName: 'The Histories', verb: 'OCCURS_IN', targetSlug: 'greece', targetName: 'Greece', context: 'Written in Greek world' },
      { sourceSlug: 'histories_herodotus', sourceName: 'The Histories', verb: 'OCCURS_IN', targetSlug: 'iran', targetName: 'Iran (Persia)', context: 'Primary subject — Persian Wars' },
      { sourceSlug: 'histories_herodotus', sourceName: 'The Histories', verb: 'OCCURS_IN', targetSlug: 'egypt', targetName: 'Egypt', context: 'Book II — extensive Egyptian ethnography' },
    ],
    places: [
      { name: 'Halicarnassus (Bodrum)', role: 'Herodotus\' birthplace' },
      { name: 'Athens', role: 'Likely where work was composed' },
      { name: 'Persepolis', role: 'Described as Persian capital' },
    ],
    texts: [],
  },

  {
    slug: 'peloponnesian_war_thucydides',
    name: 'History of the Peloponnesian War (Thucydides)',
    label: 'Text',
    callNumber: '780.06-peloponnesian-war-thucydides',
    subjectHeadings: ['Texts — Historical & Literary — Greece — Classical'],
    subjects: ['History', 'War', 'Athens', 'Sparta', 'Political Theory', 'Realism'],
    summary: 'Thucydides\' account of the Peloponnesian War (431–404 BCE) between Athens and Sparta is the first work of "scientific" history — rejecting divine causation in favor of human agency, power politics, and rational analysis. His Melian Dialogue ("the strong do what they can and the weak suffer what they must") remains the foundational text of political realism. Left incomplete at Book VIII (411 BCE).',
    period: 'c. 400 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Southern Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['CONFLICT_AND_RESOLUTION', 'GEOPOLITICAL_LINKAGE', 'CAUSE_AND_EFFECT', 'TEXTUAL_TRANSMISSION'],
    causes: [
      { title: 'Peloponnesian War (431–404 BCE) — greatest conflict in Greek world', type: 'EventWindow', year: '431–404 BCE' },
      { title: 'Herodotus establishes historical prose', type: 'Text', year: 'c. 430 BCE' },
    ],
    effects: [
      { title: 'Political realism established as analytical framework', type: 'Idea', year: 'c. 400 BCE' },
      { title: 'Foundational text for international relations theory', type: 'Text', year: 'ongoing' },
      { title: 'Model for evidence-based historical writing', type: 'Idea', year: 'c. 400 BCE' },
    ],
    relationships: [
      { sourceSlug: 'peloponnesian_war_thucydides', sourceName: 'Peloponnesian War', verb: 'OCCURS_IN', targetSlug: 'greece', targetName: 'Greece', context: 'Athens vs. Sparta' },
    ],
    places: [
      { name: 'Athens', role: 'Primary subject — Athenian empire' },
      { name: 'Sparta', role: 'Opposing power' },
      { name: 'Melos', role: 'Site of famous Melian Dialogue' },
      { name: 'Syracuse', role: 'Athenian catastrophic defeat' },
    ],
    texts: [],
  },

  {
    slug: 'ecclesiastical_history_bede',
    name: 'Ecclesiastical History of the English People (Bede)',
    label: 'Text',
    callNumber: '780.07-ecclesiastical-history-bede',
    subjectHeadings: ['Texts — Historical & Literary — England — Medieval'],
    subjects: ['History', 'England', 'Christianity', 'Anglo-Saxon', 'Monasticism', 'Dating'],
    summary: 'Completed in 731 CE by the Northumbrian monk Bede (the Venerable), this history of the English Church from Julius Caesar\'s invasion to 731 is the single most important source for early English history. Bede pioneered the AD dating system (Anno Domini), carefully cited sources, and distinguished eyewitness from hearsay evidence — earning him the title "Father of English History."',
    period: '731 CE',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Northern Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['TEXTUAL_TRANSMISSION', 'COMPARATIVE_RELIGION', 'CAUSE_AND_EFFECT', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Conversion of Anglo-Saxon England to Christianity', type: 'Movement', year: '597 CE onward' },
      { title: 'Northumbrian Golden Age of learning', type: 'Movement', year: '7th–8th century' },
    ],
    effects: [
      { title: 'AD (Anno Domini) dating system popularized', type: 'Idea', year: '731 CE' },
      { title: 'Primary source for Anglo-Saxon history for all subsequent scholars', type: 'Text', year: '731 CE' },
      { title: 'Standard for medieval historical methodology', type: 'Idea', year: '8th century' },
    ],
    relationships: [
      { sourceSlug: 'ecclesiastical_history_bede', sourceName: 'Bede\'s History', verb: 'OCCURS_IN', targetSlug: 'united-kingdom', targetName: 'England', context: 'History of the English Church' },
    ],
    places: [
      { name: 'Jarrow', role: 'Bede\'s monastery — where the work was written' },
      { name: 'Canterbury', role: 'Augustine\'s mission and English Church seat' },
    ],
    texts: [],
  },

  {
    slug: 'annals_tacitus',
    name: 'Annals (Tacitus)',
    label: 'Text',
    callNumber: '780.08-annals-tacitus',
    subjectHeadings: ['Texts — Historical & Literary — Rome — Classical'],
    subjects: ['History', 'Rome', 'Empire', 'Tyranny', 'Senate', 'Julio-Claudian'],
    summary: 'Written c. 116 CE by the Roman senator and historian Tacitus, the Annals cover the reigns of Tiberius, Caligula, Claudius, and Nero (14–68 CE). Written with devastating concision and psychological insight, they are the primary source for early imperial Rome. Tacitus\'s portrait of tyranny\'s corrosion of public virtue has influenced every subsequent generation of political writers, from Machiavelli to the American Founders.',
    period: 'c. 116 CE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Southern Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CAUSE_AND_EFFECT', 'GEOPOLITICAL_LINKAGE', 'DOCTRINE_DEVELOPMENT'],
    causes: [
      { title: 'Roman historiographical tradition (Livy, Sallust)', type: 'Movement', year: '1st century BCE' },
      { title: 'Tacitus\' experience under Domitian\'s tyranny', type: 'EventWindow', year: '81–96 CE' },
    ],
    effects: [
      { title: 'Primary source for Julio-Claudian Rome', type: 'Text', year: 'c. 116 CE' },
      { title: 'Earliest non-Christian reference to Christ (Annals 15.44)', type: 'Text', year: 'c. 116 CE' },
      { title: 'Influenced Machiavelli, Montesquieu, American Founders', type: 'Idea', year: '16th–18th century' },
    ],
    relationships: [
      { sourceSlug: 'annals_tacitus', sourceName: 'Annals of Tacitus', verb: 'OCCURS_IN', targetSlug: 'italy', targetName: 'Italy (Rome)', context: 'Written in Rome about the Roman Empire' },
    ],
    places: [
      { name: 'Rome', role: 'Subject and place of composition' },
      { name: 'Teutoburg Forest', role: 'Varus disaster described' },
    ],
    texts: [
      { title: 'Germania (Tacitus)', type: 'Companion ethnographic work' },
    ],
  },

  {
    slug: 'shiji_sima_qian',
    name: 'Records of the Grand Historian (Shiji)',
    label: 'Text',
    callNumber: '780.09-shiji-sima-qian',
    subjectHeadings: ['Texts — Historical & Literary — China — Classical'],
    subjects: ['History', 'China', 'Historiography', 'Sima Qian', 'Dynasties', 'Biography'],
    summary: 'Completed c. 94 BCE by Sima Qian, the Shiji ("Records of the Grand Historian") covers 2,000 years of Chinese history from the Yellow Emperor to Emperor Wu of Han. Its innovative structure — annals, tables, treatises, and biographies — became the model for all 24 subsequent official Chinese dynastic histories. Sima Qian endured castration rather than abandon the work, making it as much a testament to historical integrity as to Chinese civilization.',
    period: 'c. 94 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'East Asia',
    continent: 'Asia',
    status: 'Published',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CAUSE_AND_EFFECT', 'CULTURAL_DIFFUSION', 'DOCTRINE_DEVELOPMENT'],
    causes: [
      { title: 'Chinese tradition of court historiography', type: 'Movement', year: 'pre-Qin' },
      { title: 'Sima Qian inherits position from father Sima Tan', type: 'Person', year: '110 BCE' },
    ],
    effects: [
      { title: 'Model for all 24 official dynastic histories', type: 'Idea', year: 'c. 94 BCE onward' },
      { title: 'Biographical form of history established', type: 'Idea', year: 'c. 94 BCE' },
      { title: 'Primary source for Chinese history before 100 BCE', type: 'Text', year: 'c. 94 BCE' },
    ],
    relationships: [
      { sourceSlug: 'shiji_sima_qian', sourceName: 'Records of the Grand Historian', verb: 'OCCURS_IN', targetSlug: 'china', targetName: 'China', context: 'Written during Han Dynasty' },
    ],
    places: [
      { name: 'Chang\'an (Xi\'an)', role: 'Han capital, place of composition' },
    ],
    texts: [],
  },

  {
    slug: 'epic_of_gilgamesh',
    name: 'Epic of Gilgamesh',
    label: 'Text',
    callNumber: '780.10-epic-of-gilgamesh',
    subjectHeadings: ['Texts — Historical & Literary — Mesopotamia — Classical'],
    subjects: ['Literature', 'Mesopotamia', 'Epic', 'Flood', 'Mortality', 'Sumerian'],
    summary: 'The oldest known work of literature (c. 2100 BCE, Standard version c. 1200 BCE), originating in Sumerian Mesopotamia. The epic follows King Gilgamesh of Uruk on his quest for immortality after the death of his friend Enkidu. It includes a flood narrative that parallels Genesis, explores the human condition\'s fundamental themes — friendship, mortality, power — and was lost for 2,000 years until rediscovered in 1853.',
    period: 'c. 2100 BCE (earliest); c. 1200 BCE (Standard Babylonian version)',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    frameworks: ['TEXTUAL_TRANSMISSION', 'COMPARATIVE_RELIGION', 'CULTURAL_DIFFUSION', 'CAUSE_AND_EFFECT'],
    causes: [
      { title: 'Sumerian literary tradition develops cuneiform writing', type: 'Movement', year: '3rd millennium BCE' },
      { title: 'Gilgamesh — historical king of Uruk — becomes legendary', type: 'Person', year: 'c. 2700 BCE' },
    ],
    effects: [
      { title: 'Flood narrative parallels in Genesis, Greek mythology', type: 'Text', year: 'ancient' },
      { title: 'Rediscovery in 1853 revolutionizes understanding of ancient Near East', type: 'EventWindow', year: '1853' },
      { title: 'Foundational influence on all subsequent epic literature', type: 'Idea', year: 'ancient' },
    ],
    relationships: [
      { sourceSlug: 'epic_of_gilgamesh', sourceName: 'Epic of Gilgamesh', verb: 'OCCURS_IN', targetSlug: 'iraq', targetName: 'Iraq (Mesopotamia)', context: 'Sumerian/Babylonian origin' },
    ],
    places: [
      { name: 'Uruk (Warka)', role: 'City of Gilgamesh' },
      { name: 'Nineveh', role: 'Assurbanipal\'s library — tablets rediscovered' },
    ],
    texts: [],
  },

  {
    slug: 'communist_manifesto',
    name: 'The Communist Manifesto',
    label: 'Text',
    callNumber: '780.11-communist-manifesto',
    subjectHeadings: ['Texts — Historical & Literary — Germany/Global — Modern'],
    subjects: ['Politics', 'Economics', 'Communism', 'Revolution', 'Class Struggle', 'Marx'],
    summary: 'Published in 1848 by Karl Marx and Friedrich Engels, this 23-page pamphlet became one of the most influential political documents in human history. It declares that "the history of all hitherto existing society is the history of class struggles," predicts capitalism\'s collapse, and calls for proletarian revolution. Its ideas shaped the 20th century\'s most consequential political movements.',
    period: '1848',
    era: 'Modern',
    eraSlug: 'modern',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['ECONOMIC_SYSTEMS', 'CAUSE_AND_EFFECT', 'CULTURAL_DIFFUSION', 'CONFLICT_AND_RESOLUTION'],
    causes: [
      { title: 'Industrial Revolution creates urban working class', type: 'Movement', year: 'early 19th century' },
      { title: 'Revolutions of 1848 across Europe', type: 'EventWindow', year: '1848' },
    ],
    effects: [
      { title: 'Foundation for Marxism as political ideology', type: 'Movement', year: '1848 onward' },
      { title: 'Russian Revolution partly inspired by Marxist theory', type: 'EventWindow', year: '1917' },
      { title: 'Cold War ideological divide', type: 'Movement', year: '1947–1991' },
    ],
    relationships: [
      { sourceSlug: 'communist_manifesto', sourceName: 'Communist Manifesto', verb: 'OCCURS_IN', targetSlug: 'germany', targetName: 'Germany', context: 'Written by German authors' },
      { sourceSlug: 'communist_manifesto', sourceName: 'Communist Manifesto', verb: 'OCCURS_IN', targetSlug: 'united-kingdom', targetName: 'United Kingdom', context: 'Published in London, 1848' },
    ],
    places: [
      { name: 'London', role: 'Place of publication' },
      { name: 'Brussels', role: 'Where Marx was living when commissioned' },
    ],
    texts: [
      { title: 'Das Kapital (Karl Marx, 1867)', type: 'Major economic treatise expanding on Manifesto themes' },
    ],
  },

  {
    slug: 'wealth_of_nations',
    name: 'The Wealth of Nations (Adam Smith)',
    label: 'Text',
    callNumber: '780.12-wealth-of-nations',
    subjectHeadings: ['Texts — Historical & Literary — Scotland — Early Modern'],
    subjects: ['Economics', 'Free Market', 'Capitalism', 'Division of Labor', 'Invisible Hand', 'Trade'],
    summary: 'Published in 1776, Adam Smith\'s "An Inquiry into the Nature and Causes of the Wealth of Nations" is the founding text of modern economics. Its concepts — the invisible hand, division of labor, free trade, and self-interest as an engine of public good — dismantled mercantilism and provided the intellectual foundation for capitalism. Published the same year as the American Declaration of Independence.',
    period: '1776',
    era: 'Early Modern',
    eraSlug: 'early-modern',
    region: 'Northern Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['ECONOMIC_SYSTEMS', 'CAUSE_AND_EFFECT', 'INNOVATION_AND_TECHNOLOGY', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Scottish Enlightenment emphasis on moral philosophy', type: 'Movement', year: '18th century' },
      { title: 'Mercantilism\'s failures and colonial trade debates', type: 'Movement', year: '18th century' },
    ],
    effects: [
      { title: 'Free-market economics established as discipline', type: 'Idea', year: '1776' },
      { title: 'Influenced British free-trade policy (Corn Laws repeal)', type: 'EventWindow', year: '1846' },
      { title: 'Foundation for classical and neoclassical economics', type: 'Movement', year: '18th–20th century' },
    ],
    relationships: [
      { sourceSlug: 'wealth_of_nations', sourceName: 'Wealth of Nations', verb: 'OCCURS_IN', targetSlug: 'united-kingdom', targetName: 'United Kingdom (Scotland)', context: 'Written by Scottish economist' },
    ],
    places: [
      { name: 'Kirkcaldy', role: 'Smith\'s hometown, where much was written' },
      { name: 'Glasgow', role: 'Smith\'s university chair' },
      { name: 'London', role: 'Place of publication' },
    ],
    texts: [
      { title: 'The Theory of Moral Sentiments (Smith, 1759)', type: 'Companion ethical work' },
    ],
  },

  {
    slug: 'origin_of_species',
    name: 'On the Origin of Species (Darwin)',
    label: 'Text',
    callNumber: '780.13-origin-of-species',
    subjectHeadings: ['Texts — Historical & Literary — Britain — Modern'],
    subjects: ['Science', 'Evolution', 'Natural Selection', 'Biology', 'Darwin', 'Galapagos'],
    summary: 'Published on November 24, 1859, Charles Darwin\'s "On the Origin of Species by Means of Natural Selection" is arguably the most consequential scientific book ever written. It established that all species of life descended from common ancestors through natural selection — overturning millennia of creationist thought and providing the unifying theory for all modern biology.',
    period: '1859',
    era: 'Modern',
    eraSlug: 'modern',
    region: 'Northern Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['INNOVATION_AND_TECHNOLOGY', 'CAUSE_AND_EFFECT', 'ENVIRONMENTAL_HISTORY', 'DOCTRINE_DEVELOPMENT'],
    causes: [
      { title: 'Darwin\'s Beagle voyage (1831–1836) — Galápagos observations', type: 'EventWindow', year: '1831–1836' },
      { title: 'Malthus\'s population theory inspires selection mechanism', type: 'Text', year: '1838' },
      { title: 'Wallace\'s parallel discovery forces publication', type: 'Person', year: '1858' },
    ],
    effects: [
      { title: 'Evolution by natural selection accepted as scientific fact', type: 'Idea', year: '1859 onward' },
      { title: 'Unifying framework for all biology established', type: 'Idea', year: '1859' },
      { title: 'Religious and scientific worldview conflicts intensify', type: 'Movement', year: '1860s onward' },
    ],
    relationships: [
      { sourceSlug: 'origin_of_species', sourceName: 'Origin of Species', verb: 'OCCURS_IN', targetSlug: 'united-kingdom', targetName: 'United Kingdom', context: 'Written and published in England' },
      { sourceSlug: 'origin_of_species', sourceName: 'Origin of Species', verb: 'OCCURS_IN', targetSlug: 'ecuador', targetName: 'Ecuador (Galápagos)', context: 'Key observations made here' },
    ],
    places: [
      { name: 'Down House, Kent', role: 'Where Darwin worked for 20 years' },
      { name: 'Galápagos Islands', role: 'Key observations on finch variation' },
      { name: 'London', role: 'Published by John Murray' },
    ],
    texts: [
      { title: 'The Descent of Man (Darwin, 1871)', type: 'Companion work on human evolution' },
    ],
  },
]
