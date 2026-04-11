import type { Entity } from '../entityTypes'

/**
 * Division Expansion Entities — New entries for divisions 280, 290, 380, 590, 680, 780
 *
 * Military Leaders (280), Explorers & Navigators (290), Educational Institutions (380),
 * Agricultural & Economic Events (590), Trade & Navigation Movements (680),
 * Historical & Literary Texts (780).
 */
export const DIVISION_EXPANSION_ENTITIES: Entity[] = [

  // ═══════════════════════════════════════════════════════════════
  // 290 — EXPLORERS & NAVIGATORS
  // ═══════════════════════════════════════════════════════════════

  {
    slug: 'zheng_he',
    name: 'Zheng He',
    label: 'Person',
    callNumber: '290.01-zheng-he',
    subjectHeadings: ['People — Explorers & Navigators — China — Medieval'],
    subjects: ['Exploration', 'Navigation', 'Ming Dynasty', 'Treasure Fleets', 'Indian Ocean', 'Diplomacy'],
    summary: 'Chinese mariner and diplomat (1371–1433) who commanded seven massive naval expeditions across the Indian Ocean under the Ming Dynasty. His treasure fleets — the largest wooden ships ever built — reached Southeast Asia, India, the Persian Gulf, and East Africa, establishing Chinese maritime dominance decades before European exploration.',
    born: '1371, Kunyang, Yunnan',
    died: '1433, at sea (Indian Ocean)',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'East Asia',
    continent: 'Asia',
    status: 'Published',
    frameworks: ['CULTURAL_DIFFUSION', 'GEOPOLITICAL_LINKAGE', 'ECONOMIC_SYSTEMS', 'INNOVATION_AND_TECHNOLOGY'],
    causes: [
      { title: 'Ming Dynasty consolidation', type: 'EventWindow', year: '1368' },
      { title: 'Yongle Emperor\'s expansionist vision', type: 'Person', year: '1402' },
    ],
    effects: [
      { title: 'Chinese maritime trade networks expanded', type: 'Movement', year: '1405–1433' },
      { title: 'Diplomatic tributaries established across Indian Ocean', type: 'EventWindow', year: '1405–1433' },
      { title: 'Ming Haijin policy ends Chinese naval exploration', type: 'EventWindow', year: '1433' },
    ],
    relationships: [
      { sourceSlug: 'zheng_he', sourceName: 'Zheng He', verb: 'LEADS', targetSlug: 'ming-treasure-voyages', targetName: 'Ming Treasure Voyages', context: 'Commanded 7 voyages 1405–1433' },
      { sourceSlug: 'zheng_he', sourceName: 'Zheng He', verb: 'OCCURS_IN', targetSlug: 'china', targetName: 'China', context: 'Served Ming court' },
      { sourceSlug: 'zheng_he', sourceName: 'Zheng He', verb: 'INFLUENCES', targetSlug: 'indian-ocean-trade', targetName: 'Indian Ocean Trade', context: 'Established diplomatic trade routes' },
    ],
    places: [
      { name: 'Nanjing', role: 'Expedition departure port', slug: 'nanjing' },
      { name: 'Calicut', role: 'Key Indian Ocean destination' },
      { name: 'Malacca', role: 'Southeast Asian hub' },
      { name: 'Mogadishu', role: 'East African port of call' },
    ],
    texts: [
      { title: 'Yingya Shenglan (Overall Survey of the Ocean\'s Shores)', type: 'Travel account' },
      { title: 'Zheng He Navigation Charts', type: 'Navigational maps' },
    ],
  },

  {
    slug: 'ibn_battuta',
    name: 'Ibn Battuta',
    label: 'Person',
    callNumber: '290.02-ibn-battuta',
    subjectHeadings: ['People — Explorers & Navigators — Morocco — Medieval'],
    subjects: ['Exploration', 'Travel', 'Islamic World', 'Geography', 'Hajj', 'Jurisprudence'],
    summary: 'Moroccan scholar and explorer (1304–1368/69) whose travels across the Islamic world and beyond covered approximately 73,000 miles over 29 years — one of the greatest journeys of the pre-modern era. His Rihla (Travels) provides unparalleled firsthand accounts of medieval societies from West Africa to China.',
    born: '1304, Tangier, Morocco',
    died: 'c. 1368–1369, Morocco',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    frameworks: ['CULTURAL_DIFFUSION', 'COMPARATIVE_RELIGION', 'ECONOMIC_SYSTEMS', 'GEOPOLITICAL_LINKAGE'],
    causes: [
      { title: 'Hajj pilgrimage obligation', type: 'Idea', year: '1325' },
      { title: 'Expansion of Dar al-Islam', type: 'Movement', year: '7th–14th century' },
    ],
    effects: [
      { title: 'Rihla (The Travels) composed', type: 'Text', year: '1355' },
      { title: 'Detailed ethnographic record of medieval Islamic world', type: 'Evidence', year: '1355' },
    ],
    relationships: [
      { sourceSlug: 'ibn_battuta', sourceName: 'Ibn Battuta', verb: 'OCCURS_IN', targetSlug: 'morocco', targetName: 'Morocco', context: 'Born in Tangier' },
      { sourceSlug: 'ibn_battuta', sourceName: 'Ibn Battuta', verb: 'PARTICIPATES_IN', targetSlug: 'hajj', targetName: 'Hajj Pilgrimage', context: 'Initial impetus for travel in 1325' },
      { sourceSlug: 'ibn_battuta', sourceName: 'Ibn Battuta', verb: 'AUTHORS', targetSlug: 'rihla_ibn_battuta', targetName: 'Rihla (The Travels)', context: 'Dictated to Ibn Juzayy in 1355' },
    ],
    places: [
      { name: 'Tangier', role: 'Birthplace' },
      { name: 'Mecca', role: 'Hajj destination', slug: 'mecca_city' },
      { name: 'Delhi', role: 'Served as qadi under Muhammad bin Tughluq' },
      { name: 'Mali Empire', role: 'West African travels' },
      { name: 'Beijing', role: 'Easternmost reach' },
    ],
    texts: [
      { title: 'Rihla (A Gift to Those Who Contemplate the Wonders of Cities and the Marvels of Travelling)', type: 'Travel account' },
    ],
  },

  {
    slug: 'leif_erikson',
    name: 'Leif Erikson',
    label: 'Person',
    callNumber: '290.03-leif-erikson',
    subjectHeadings: ['People — Explorers & Navigators — Scandinavia — Medieval'],
    subjects: ['Exploration', 'Norse', 'Vikings', 'Vinland', 'North America', 'Navigation'],
    summary: 'Norse explorer (c. 970–c. 1020) believed to be the first European to set foot in North America, approximately 500 years before Columbus. Son of Erik the Red, he sailed from Greenland to a land he called Vinland (likely Newfoundland), establishing a brief settlement at L\'Anse aux Meadows.',
    born: 'c. 970, Iceland',
    died: 'c. 1020, Greenland',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Northern Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['CULTURAL_DIFFUSION', 'CAUSE_AND_EFFECT', 'ENVIRONMENTAL_HISTORY', 'INNOVATION_AND_TECHNOLOGY'],
    causes: [
      { title: 'Norse expansion and Viking Age', type: 'Movement', year: '793–1066' },
      { title: 'Erik the Red colonizes Greenland', type: 'EventWindow', year: 'c. 985' },
    ],
    effects: [
      { title: 'L\'Anse aux Meadows settlement (Vinland)', type: 'EventWindow', year: 'c. 1000' },
      { title: 'First documented European contact with North America', type: 'EventWindow', year: 'c. 1000' },
    ],
    relationships: [
      { sourceSlug: 'leif_erikson', sourceName: 'Leif Erikson', verb: 'OCCURS_IN', targetSlug: 'iceland', targetName: 'Iceland', context: 'Born in Iceland' },
      { sourceSlug: 'leif_erikson', sourceName: 'Leif Erikson', verb: 'PARTICIPATES_IN', targetSlug: 'norse-expansion', targetName: 'Norse Expansion', context: 'Part of Viking Age exploration' },
    ],
    places: [
      { name: 'Iceland', role: 'Birthplace' },
      { name: 'Greenland', role: 'Home base' },
      { name: 'Vinland (Newfoundland)', role: 'Discovery site, c. 1000 CE' },
    ],
    texts: [
      { title: 'Saga of Erik the Red', type: 'Norse saga' },
      { title: 'Saga of the Greenlanders', type: 'Norse saga' },
    ],
  },

  {
    slug: 'marco_polo',
    name: 'Marco Polo',
    label: 'Person',
    callNumber: '290.04-marco-polo',
    subjectHeadings: ['People — Explorers & Navigators — Italy — Medieval'],
    subjects: ['Exploration', 'Silk Road', 'Mongol Empire', 'Venice', 'Trade', 'China'],
    summary: 'Venetian merchant and explorer (1254–1324) whose 24-year journey through Asia along the Silk Road to the court of Kublai Khan produced "The Travels of Marco Polo" — one of the most influential travel accounts in history. His descriptions of Asian civilizations transformed European understanding of the East.',
    born: '1254, Venice',
    died: '1324, Venice',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Southern Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['CULTURAL_DIFFUSION', 'ECONOMIC_SYSTEMS', 'GEOPOLITICAL_LINKAGE', 'TEXTUAL_TRANSMISSION'],
    causes: [
      { title: 'Pax Mongolica enables overland travel', type: 'Movement', year: '1206–1368' },
      { title: 'Venetian merchant tradition', type: 'Movement', year: '13th century' },
    ],
    effects: [
      { title: 'The Travels of Marco Polo published', type: 'Text', year: '1300' },
      { title: 'European fascination with the East intensifies', type: 'Movement', year: '14th–15th century' },
      { title: 'Inspired Christopher Columbus', type: 'Person', year: '1492' },
    ],
    relationships: [
      { sourceSlug: 'marco_polo', sourceName: 'Marco Polo', verb: 'OCCURS_IN', targetSlug: 'italy', targetName: 'Italy', context: 'Venetian merchant' },
      { sourceSlug: 'marco_polo', sourceName: 'Marco Polo', verb: 'PARTICIPATES_IN', targetSlug: 'silk-road-trade', targetName: 'Silk Road Trade', context: 'Traveled the Silk Road to China and back' },
      { sourceSlug: 'marco_polo', sourceName: 'Marco Polo', verb: 'AUTHORS', targetSlug: 'travels_of_marco_polo', targetName: 'The Travels of Marco Polo', context: 'Dictated account of his journey' },
    ],
    places: [
      { name: 'Venice', role: 'Home city', slug: 'venice' },
      { name: 'Beijing (Khanbaliq)', role: 'Court of Kublai Khan' },
      { name: 'Hormuz', role: 'Persian Gulf port' },
    ],
    texts: [
      { title: 'The Travels of Marco Polo (Il Milione)', type: 'Travel account' },
    ],
  },

  {
    slug: 'christopher_columbus',
    name: 'Christopher Columbus',
    label: 'Person',
    callNumber: '290.05-christopher-columbus',
    subjectHeadings: ['People — Explorers & Navigators — Spain — Early Modern'],
    subjects: ['Exploration', 'Americas', 'Navigation', 'Spanish Crown', 'Columbian Exchange', 'Colonialism'],
    summary: 'Genoese navigator (1451–1506) whose 1492 transatlantic voyage under the Spanish Crown initiated sustained European contact with the Americas. His four voyages established colonial footholds in the Caribbean and unleashed the Columbian Exchange — the most consequential biological and cultural transfer in human history.',
    born: '1451, Genoa',
    died: '1506, Valladolid, Spain',
    era: 'Early Modern',
    eraSlug: 'early-modern',
    region: 'Southern Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['CAUSE_AND_EFFECT', 'EMPIRE_AND_COLONIALISM', 'CULTURAL_DIFFUSION', 'ENVIRONMENTAL_HISTORY', 'GEOPOLITICAL_LINKAGE'],
    causes: [
      { title: 'Fall of Constantinople blocks Eastern trade', type: 'EventWindow', year: '1453' },
      { title: 'Portuguese maritime exploration precedent', type: 'Movement', year: '15th century' },
      { title: 'Marco Polo\'s Travels inspires westward route', type: 'Text', year: '1300', slug: 'travels_of_marco_polo' },
    ],
    effects: [
      { title: 'Columbian Exchange begins', type: 'EventWindow', year: '1493' },
      { title: 'Spanish colonial empire established', type: 'Institution', year: '1500s' },
      { title: 'Indigenous population catastrophe', type: 'EventWindow', year: '1492–1600' },
      { title: 'Treaty of Tordesillas divides New World', type: 'EventWindow', year: '1494' },
    ],
    relationships: [
      { sourceSlug: 'christopher_columbus', sourceName: 'Christopher Columbus', verb: 'OCCURS_IN', targetSlug: 'spain', targetName: 'Spain', context: 'Sailed under Spanish crown' },
      { sourceSlug: 'christopher_columbus', sourceName: 'Christopher Columbus', verb: 'CAUSES', targetSlug: 'columbian-exchange', targetName: 'Columbian Exchange', context: '1492 voyage initiated biological transfer' },
      { sourceSlug: 'christopher_columbus', sourceName: 'Christopher Columbus', verb: 'INFLUENCES', targetSlug: 'age-of-exploration', targetName: 'Age of Exploration', context: 'Catalyzed European colonization' },
    ],
    places: [
      { name: 'Genoa', role: 'Birthplace' },
      { name: 'Hispaniola', role: 'First Caribbean settlement' },
      { name: 'San Salvador', role: 'First landing, October 1492' },
    ],
    texts: [
      { title: 'Journal of the First Voyage (Diario)', type: 'Ship\'s log / journal' },
      { title: 'Letter to Santángel (1493)', type: 'Official report' },
    ],
  },

  {
    slug: 'vasco_da_gama',
    name: 'Vasco da Gama',
    label: 'Person',
    callNumber: '290.06-vasco-da-gama',
    subjectHeadings: ['People — Explorers & Navigators — Portugal — Early Modern'],
    subjects: ['Exploration', 'Navigation', 'India', 'Spice Trade', 'Portuguese Empire', 'Cape Route'],
    summary: 'Portuguese explorer (c. 1460–1524) who completed the first direct sea voyage from Europe to India in 1498, rounding the Cape of Good Hope and reaching Calicut. His route opened a maritime highway that broke the Venetian-Arab monopoly on the spice trade and launched the Portuguese maritime empire.',
    born: 'c. 1460, Sines, Portugal',
    died: '1524, Cochin, India',
    era: 'Early Modern',
    eraSlug: 'early-modern',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['ECONOMIC_SYSTEMS', 'GEOPOLITICAL_LINKAGE', 'CULTURAL_DIFFUSION', 'EMPIRE_AND_COLONIALISM'],
    causes: [
      { title: 'Portuguese exploration under Henry the Navigator', type: 'Person', year: '1418–1460' },
      { title: 'Bartolomeu Dias rounds Cape of Good Hope', type: 'EventWindow', year: '1488' },
    ],
    effects: [
      { title: 'Portuguese maritime empire established in Indian Ocean', type: 'Institution', year: '1500s' },
      { title: 'Venetian spice trade monopoly broken', type: 'EventWindow', year: '1500s' },
    ],
    relationships: [
      { sourceSlug: 'vasco_da_gama', sourceName: 'Vasco da Gama', verb: 'OCCURS_IN', targetSlug: 'portugal', targetName: 'Portugal', context: 'Portuguese explorer' },
      { sourceSlug: 'vasco_da_gama', sourceName: 'Vasco da Gama', verb: 'CAUSES', targetSlug: 'portuguese-maritime-empire', targetName: 'Portuguese Maritime Empire', context: 'India route enabled imperial expansion' },
    ],
    places: [
      { name: 'Sines', role: 'Birthplace' },
      { name: 'Calicut', role: 'Destination, 1498' },
      { name: 'Cape of Good Hope', role: 'Key navigational waypoint' },
    ],
    texts: [
      { title: 'Roteiro (Journal of the First Voyage to India)', type: 'Ship\'s log' },
    ],
  },

  {
    slug: 'ferdinand_magellan',
    name: 'Ferdinand Magellan',
    label: 'Person',
    callNumber: '290.07-ferdinand-magellan',
    subjectHeadings: ['People — Explorers & Navigators — Portugal/Spain — Early Modern'],
    subjects: ['Exploration', 'Circumnavigation', 'Navigation', 'Pacific Ocean', 'Philippines', 'Strait of Magellan'],
    summary: 'Portuguese explorer (1480–1521) who organized the first circumnavigation of the Earth under the Spanish flag. Though killed in the Philippines in 1521, his expedition — completed by Juan Sebastián Elcano — proved the Earth\'s sphericity and revealed the vast Pacific Ocean.',
    born: '1480, Sabrosa, Portugal',
    died: '1521, Mactan, Philippines (killed in battle)',
    era: 'Early Modern',
    eraSlug: 'early-modern',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['INNOVATION_AND_TECHNOLOGY', 'GEOPOLITICAL_LINKAGE', 'CAUSE_AND_EFFECT', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Spanish-Portuguese competition for trade routes', type: 'Movement', year: '16th century' },
      { title: 'Treaty of Tordesillas divides world', type: 'EventWindow', year: '1494' },
    ],
    effects: [
      { title: 'First circumnavigation completed', type: 'EventWindow', year: '1522' },
      { title: 'Pacific Ocean dimensions revealed to Europe', type: 'EventWindow', year: '1520–1521' },
    ],
    relationships: [
      { sourceSlug: 'ferdinand_magellan', sourceName: 'Ferdinand Magellan', verb: 'OCCURS_IN', targetSlug: 'spain', targetName: 'Spain', context: 'Sailed under Spanish crown' },
      { sourceSlug: 'ferdinand_magellan', sourceName: 'Ferdinand Magellan', verb: 'PARTICIPATES_IN', targetSlug: 'age-of-exploration', targetName: 'Age of Exploration', context: 'Led first circumnavigation attempt' },
    ],
    places: [
      { name: 'Sabrosa', role: 'Birthplace' },
      { name: 'Strait of Magellan', role: 'Discovered passage, 1520' },
      { name: 'Mactan, Philippines', role: 'Died in battle, 1521' },
    ],
    texts: [
      { title: 'Pigafetta\'s Account of Magellan\'s Voyage', type: 'Travel chronicle' },
    ],
  },

  {
    slug: 'james_cook',
    name: 'James Cook',
    label: 'Person',
    callNumber: '290.08-james-cook',
    subjectHeadings: ['People — Explorers & Navigators — Britain — Modern'],
    subjects: ['Exploration', 'Pacific Ocean', 'Navigation', 'Cartography', 'Australia', 'New Zealand', 'Science'],
    summary: 'British navigator and cartographer (1728–1779) who led three Pacific voyages that mapped coastlines from New Zealand to Hawaii, charted the Great Barrier Reef, and crossed the Antarctic Circle. His scientific approach to exploration — combating scurvy and producing accurate charts — transformed maritime knowledge.',
    born: '1728, Marton, Yorkshire',
    died: '1779, Kealakekua Bay, Hawaii (killed)',
    era: 'Early Modern',
    eraSlug: 'early-modern',
    region: 'Northern Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['INNOVATION_AND_TECHNOLOGY', 'EMPIRE_AND_COLONIALISM', 'ENVIRONMENTAL_HISTORY', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'British naval supremacy expanding', type: 'Movement', year: '18th century' },
      { title: 'Royal Society sponsors Venus transit observation', type: 'Institution', year: '1768' },
    ],
    effects: [
      { title: 'European claim to Australia (New South Wales)', type: 'EventWindow', year: '1770' },
      { title: 'Accurate Pacific charts produced', type: 'Text', year: '1768–1779' },
      { title: 'Hawaiian Islands mapped', type: 'EventWindow', year: '1778' },
    ],
    relationships: [
      { sourceSlug: 'james_cook', sourceName: 'James Cook', verb: 'OCCURS_IN', targetSlug: 'united-kingdom', targetName: 'United Kingdom', context: 'British Royal Navy captain' },
      { sourceSlug: 'james_cook', sourceName: 'James Cook', verb: 'INFLUENCES', targetSlug: 'british-colonization-australia', targetName: 'British Colonization of Australia', context: 'Claimed New South Wales for Britain 1770' },
    ],
    places: [
      { name: 'Yorkshire', role: 'Birthplace' },
      { name: 'New Zealand', role: 'Circumnavigated and charted, 1769–1770' },
      { name: 'Australia', role: 'Claimed for Britain, 1770' },
      { name: 'Hawaii', role: 'Killed at Kealakekua Bay, 1779' },
    ],
    texts: [
      { title: 'A Voyage Towards the South Pole (1777)', type: 'Voyage account' },
      { title: 'Cook\'s Journals', type: 'Ship\'s logs' },
    ],
  },

  {
    slug: 'henry_the_navigator',
    name: 'Henry the Navigator',
    label: 'Person',
    callNumber: '290.09-henry-the-navigator',
    subjectHeadings: ['People — Explorers & Navigators — Portugal — Medieval'],
    subjects: ['Exploration', 'Navigation', 'Portugal', 'Atlantic', 'West Africa', 'Maritime Technology'],
    summary: 'Portuguese prince (1394–1460) who, though never a navigator himself, sponsored systematic maritime exploration of the West African coast. His school of navigation at Sagres advanced cartography, shipbuilding (the caravel), and navigational techniques, launching the European Age of Discovery.',
    born: '1394, Porto, Portugal',
    died: '1460, Sagres, Portugal',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['INNOVATION_AND_TECHNOLOGY', 'ECONOMIC_SYSTEMS', 'EMPIRE_AND_COLONIALISM', 'CAUSE_AND_EFFECT'],
    causes: [
      { title: 'Portuguese Reconquista success at Ceuta', type: 'EventWindow', year: '1415' },
      { title: 'Desire to bypass Saharan gold trade monopoly', type: 'Idea', year: '15th century' },
    ],
    effects: [
      { title: 'Portuguese reach Cape Verde', type: 'EventWindow', year: '1444' },
      { title: 'Caravel ship design enables ocean exploration', type: 'Idea', year: '15th century' },
      { title: 'European Age of Discovery begins', type: 'Movement', year: '1419–1460' },
    ],
    relationships: [
      { sourceSlug: 'henry_the_navigator', sourceName: 'Henry the Navigator', verb: 'OCCURS_IN', targetSlug: 'portugal', targetName: 'Portugal', context: 'Portuguese prince' },
      { sourceSlug: 'henry_the_navigator', sourceName: 'Henry the Navigator', verb: 'CAUSES', targetSlug: 'age-of-exploration', targetName: 'Age of Exploration', context: 'Funded systematic maritime exploration' },
    ],
    places: [
      { name: 'Sagres', role: 'Navigation school' },
      { name: 'Porto', role: 'Birthplace' },
      { name: 'Madeira', role: 'Portuguese colony established 1420' },
    ],
    texts: [
      { title: 'Crónica dos Feitos de Guiné (Zurara)', type: 'Chronicle' },
    ],
  },

  {
    slug: 'roald_amundsen',
    name: 'Roald Amundsen',
    label: 'Person',
    callNumber: '290.10-roald-amundsen',
    subjectHeadings: ['People — Explorers & Navigators — Norway — Modern'],
    subjects: ['Exploration', 'South Pole', 'Northwest Passage', 'Arctic', 'Antarctic', 'Polar Exploration'],
    summary: 'Norwegian explorer (1872–1928) who led the first expedition to reach the South Pole (December 1911) and the first to traverse the Northwest Passage (1903–1906). His meticulous planning, use of dog sleds, and adaptation of Inuit survival techniques made him the most successful polar explorer in history.',
    born: '1872, Borge, Norway',
    died: '1928, Arctic Ocean (disappeared during rescue mission)',
    era: 'Modern',
    eraSlug: 'modern',
    region: 'Northern Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['INNOVATION_AND_TECHNOLOGY', 'ADAPTATION', 'CAUSE_AND_EFFECT', 'ENVIRONMENTAL_HISTORY'],
    causes: [
      { title: 'Age of polar exploration', type: 'Movement', year: '19th–20th century' },
      { title: 'Fridtjof Nansen\'s Arctic expeditions inspire him', type: 'Person', year: '1893–1896' },
    ],
    effects: [
      { title: 'South Pole reached first', type: 'EventWindow', year: 'December 14, 1911' },
      { title: 'Northwest Passage navigation proven feasible', type: 'EventWindow', year: '1906' },
    ],
    relationships: [
      { sourceSlug: 'roald_amundsen', sourceName: 'Roald Amundsen', verb: 'OCCURS_IN', targetSlug: 'norway', targetName: 'Norway', context: 'Norwegian explorer' },
    ],
    places: [
      { name: 'Borge', role: 'Birthplace' },
      { name: 'South Pole', role: 'First to reach, December 1911' },
      { name: 'Northwest Passage', role: 'First to navigate, 1903–1906' },
    ],
    texts: [
      { title: 'The South Pole (1912)', type: 'Expedition account' },
    ],
  },

  // ═══════════════════════════════════════════════════════════════
  // 280 — MILITARY LEADERS (hand-curated additions)
  // ═══════════════════════════════════════════════════════════════

  {
    slug: 'sun_tzu',
    name: 'Sun Tzu',
    label: 'Person',
    callNumber: '280.01-sun-tzu',
    subjectHeadings: ['People — Military Leaders & Commanders — China — Classical'],
    subjects: ['Military Strategy', 'Warfare', 'Philosophy', 'Ancient China', 'The Art of War'],
    summary: 'Chinese military strategist (c. 544–496 BCE) traditionally credited as author of The Art of War, the most influential treatise on military strategy and tactics ever written. His principles — "know your enemy and know yourself" — have been applied to warfare, business, and diplomacy for over 2,500 years.',
    born: 'c. 544 BCE, Qi or Wu',
    died: 'c. 496 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'East Asia',
    continent: 'Asia',
    status: 'Published',
    frameworks: ['CAUSE_AND_EFFECT', 'CONFLICT_AND_RESOLUTION', 'IDEAS_AND_WORLDVIEWS' as any, 'GEOPOLITICAL_LINKAGE'],
    causes: [
      { title: 'Warring States period interstate conflict', type: 'EventWindow', year: '5th century BCE' },
      { title: 'Chinese philosophical traditions', type: 'Movement', year: '6th century BCE' },
    ],
    effects: [
      { title: 'The Art of War becomes canonical military text', type: 'Text', year: 'c. 5th century BCE' },
      { title: 'Influenced military thought across East Asia', type: 'Movement', year: '5th century BCE onwards' },
    ],
    relationships: [
      { sourceSlug: 'sun_tzu', sourceName: 'Sun Tzu', verb: 'AUTHORS', targetSlug: 'art_of_war', targetName: 'The Art of War', context: 'Foundational military treatise' },
      { sourceSlug: 'sun_tzu', sourceName: 'Sun Tzu', verb: 'OCCURS_IN', targetSlug: 'china', targetName: 'China', context: 'Ancient Chinese strategist' },
    ],
    places: [
      { name: 'Kingdom of Wu', role: 'Served as military advisor' },
      { name: 'China', role: 'Lifetime' },
    ],
    texts: [
      { title: 'The Art of War (Sunzi Bingfa)', type: 'Military treatise', slug: 'art_of_war' },
    ],
  },

  {
    slug: 'hannibal_barca',
    name: 'Hannibal Barca',
    label: 'Person',
    callNumber: '280.02-hannibal-barca',
    subjectHeadings: ['People — Military Leaders & Commanders — Carthage — Classical'],
    subjects: ['Military Strategy', 'Punic Wars', 'Carthage', 'Rome', 'Alps Crossing', 'Cannae'],
    summary: 'Carthaginian general (247–c. 183 BCE) who led one of history\'s most audacious military campaigns — crossing the Alps with war elephants to invade Italy. His victory at Cannae (216 BCE) remains a textbook example of tactical genius. Though he ultimately lost the Second Punic War, he forced Rome to transform its military, shaping the Republic\'s evolution into an empire.',
    born: '247 BCE, Carthage',
    died: 'c. 183 BCE, Bithynia (suicide to avoid Roman capture)',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    frameworks: ['CONFLICT_AND_RESOLUTION', 'CAUSE_AND_EFFECT', 'GEOPOLITICAL_LINKAGE', 'INNOVATION_AND_TECHNOLOGY'],
    causes: [
      { title: 'First Punic War humiliation of Carthage', type: 'EventWindow', year: '264–241 BCE' },
      { title: 'Hamilcar Barca\'s oath of vengeance against Rome', type: 'Person', year: 'c. 237 BCE' },
    ],
    effects: [
      { title: 'Battle of Cannae — worst Roman defeat', type: 'EventWindow', year: '216 BCE' },
      { title: 'Roman military reforms (Scipio\'s adaptations)', type: 'Movement', year: '210–202 BCE' },
      { title: 'Destruction of Carthage in Third Punic War', type: 'EventWindow', year: '146 BCE' },
    ],
    relationships: [
      { sourceSlug: 'hannibal_barca', sourceName: 'Hannibal Barca', verb: 'PARTICIPATES_IN', targetSlug: 'second-punic-war', targetName: 'Second Punic War', context: 'Commander of Carthaginian forces' },
      { sourceSlug: 'hannibal_barca', sourceName: 'Hannibal Barca', verb: 'OCCURS_IN', targetSlug: 'tunisia', targetName: 'Tunisia (Carthage)', context: 'Born in Carthage' },
    ],
    places: [
      { name: 'Carthage', role: 'Birthplace' },
      { name: 'Cannae', role: 'Greatest victory, 216 BCE' },
      { name: 'Alps', role: 'Legendary crossing with elephants' },
    ],
    texts: [
      { title: 'Histories (Polybius)', type: 'Historical account' },
      { title: 'Ab Urbe Condita (Livy)', type: 'Roman history' },
    ],
  },

  {
    slug: 'genghis_khan',
    name: 'Genghis Khan',
    label: 'Person',
    callNumber: '280.03-genghis-khan',
    subjectHeadings: ['People — Military Leaders & Commanders — Mongolia — Medieval'],
    subjects: ['Mongol Empire', 'Conquest', 'Military Strategy', 'Steppe Nomads', 'Silk Road', 'Law'],
    summary: 'Founder and first Great Khan of the Mongol Empire (c. 1162–1227), which became the largest contiguous land empire in history. Born as Temüjin, he united the steppe tribes, developed revolutionary military tactics (feigned retreats, siege warfare, psychological warfare), and established the Yasa legal code. His conquests killed millions but also opened the Silk Road to unprecedented trade and cultural exchange.',
    born: 'c. 1162, Khentii Mountains, Mongolia',
    died: '1227, Western Xia (on campaign)',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Central Asia',
    continent: 'Asia',
    status: 'Published',
    frameworks: ['CONFLICT_AND_RESOLUTION', 'GEOPOLITICAL_LINKAGE', 'EMPIRE_AND_COLONIALISM', 'CAUSE_AND_EFFECT', 'ECONOMIC_SYSTEMS'],
    causes: [
      { title: 'Fractured Mongol tribal politics', type: 'Movement', year: '12th century' },
      { title: 'Khwarezmian Shah insults Mongol envoys', type: 'EventWindow', year: '1218' },
    ],
    effects: [
      { title: 'Mongol Empire spans Eurasia', type: 'Institution', year: '1206–1368' },
      { title: 'Pax Mongolica enables Silk Road trade', type: 'Movement', year: '13th–14th century' },
      { title: 'Yasa legal code established', type: 'Text', year: '1206' },
      { title: 'Destruction of Khwarezmian Empire', type: 'EventWindow', year: '1219–1221' },
    ],
    relationships: [
      { sourceSlug: 'genghis_khan', sourceName: 'Genghis Khan', verb: 'LEADS', targetSlug: 'mongol-empire', targetName: 'Mongol Empire', context: 'Founded and ruled 1206–1227' },
      { sourceSlug: 'genghis_khan', sourceName: 'Genghis Khan', verb: 'OCCURS_IN', targetSlug: 'mongolia', targetName: 'Mongolia', context: 'Born in Khentii Mountains' },
      { sourceSlug: 'genghis_khan', sourceName: 'Genghis Khan', verb: 'CAUSES', targetSlug: 'pax-mongolica', targetName: 'Pax Mongolica', context: 'Empire enabled transcontinental trade' },
    ],
    places: [
      { name: 'Karakorum', role: 'Imperial capital' },
      { name: 'Samarkand', role: 'Conquered 1220' },
      { name: 'Beijing (Zhongdu)', role: 'Conquered 1215' },
    ],
    texts: [
      { title: 'The Secret History of the Mongols', type: 'Imperial chronicle' },
    ],
  },

  // ═══════════════════════════════════════════════════════════════
  // 380 — EDUCATIONAL INSTITUTIONS (hand-curated)
  // ═══════════════════════════════════════════════════════════════

  {
    slug: 'university_of_al_qarawiyyin',
    name: 'University of al-Qarawiyyin',
    label: 'Institution',
    callNumber: '380.01-al-qarawiyyin',
    subjectHeadings: ['Institutions — Educational — Morocco — Medieval'],
    subjects: ['Education', 'Islamic Learning', 'University', 'Morocco', 'Fez', 'Theology', 'Law'],
    summary: 'Founded in 859 CE in Fez, Morocco by Fatima al-Fihri, al-Qarawiyyin is recognized by UNESCO and the Guinness World Records as the oldest existing, continually operating educational institution in the world. It began as a mosque and madrasa, evolving into a full university teaching theology, law, grammar, medicine, mathematics, and astronomy.',
    founded: '859 CE',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    frameworks: ['DOCTRINE_DEVELOPMENT', 'INNOVATION_AND_TECHNOLOGY', 'CULTURAL_DIFFUSION', 'COMPARATIVE_RELIGION'],
    causes: [
      { title: 'Spread of Islam in North Africa', type: 'Movement', year: '7th–9th century' },
      { title: 'Fatima al-Fihri\'s endowment', type: 'Person', year: '859 CE' },
    ],
    effects: [
      { title: 'Training center for Islamic scholars for 1,100+ years', type: 'Movement', year: '859–present' },
      { title: 'Influenced European university model', type: 'Idea', year: '12th–13th century' },
    ],
    relationships: [
      { sourceSlug: 'university_of_al_qarawiyyin', sourceName: 'University of al-Qarawiyyin', verb: 'OCCURS_IN', targetSlug: 'morocco', targetName: 'Morocco', context: 'Located in Fez, Morocco' },
    ],
    places: [
      { name: 'Fez', role: 'Location since 859 CE' },
    ],
    texts: [],
  },

  {
    slug: 'university_of_bologna',
    name: 'University of Bologna',
    label: 'Institution',
    callNumber: '380.02-university-of-bologna',
    subjectHeadings: ['Institutions — Educational — Italy — Medieval'],
    subjects: ['Education', 'University', 'Law', 'Italy', 'Bologna', 'Roman Law', 'Canon Law'],
    summary: 'Founded in 1088 in Bologna, Italy, it is the oldest university in the West and model for the European university system. Initially focused on the study of Roman law (the Corpus Juris Civilis), it pioneered the concept of academic freedom and student self-governance, influencing Oxford, Paris, and Cambridge.',
    founded: '1088 CE',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Southern Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['LEGAL_INTERPRETATION', 'DOCTRINE_DEVELOPMENT', 'INNOVATION_AND_TECHNOLOGY', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Rediscovery of Justinian\'s Corpus Juris Civilis', type: 'Text', year: '11th century', slug: 'corpus_iuris_civilis' },
      { title: 'Medieval urban revival in Northern Italy', type: 'Movement', year: '11th century' },
    ],
    effects: [
      { title: 'European university model established', type: 'Institution', year: '12th century' },
      { title: 'Revival of Roman law tradition in Europe', type: 'Movement', year: '11th–13th century' },
    ],
    relationships: [
      { sourceSlug: 'university_of_bologna', sourceName: 'University of Bologna', verb: 'OCCURS_IN', targetSlug: 'italy', targetName: 'Italy', context: 'Bologna, Italy' },
      { sourceSlug: 'university_of_bologna', sourceName: 'University of Bologna', verb: 'INFLUENCES', targetSlug: 'european-universities', targetName: 'European University System', context: 'Model for Oxford, Paris, Cambridge' },
    ],
    places: [
      { name: 'Bologna', role: 'Location since 1088 CE' },
    ],
    texts: [
      { title: 'Corpus Juris Civilis (studied)', type: 'Legal code', slug: 'corpus_iuris_civilis' },
    ],
  },

  {
    slug: 'library_of_alexandria',
    name: 'Library of Alexandria',
    label: 'Institution',
    callNumber: '380.03-library-of-alexandria',
    subjectHeadings: ['Institutions — Educational — Egypt — Classical'],
    subjects: ['Education', 'Library', 'Knowledge', 'Alexandria', 'Ptolemaic Egypt', 'Scholarship', 'Texts'],
    summary: 'The greatest library of the ancient world, founded under the Ptolemaic dynasty in the 3rd century BCE. At its height it housed an estimated 400,000–700,000 scrolls, attracting scholars like Euclid, Archimedes, and Eratosthenes. Its destruction — gradual rather than sudden — remains one of history\'s great intellectual losses.',
    founded: 'c. 283 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    frameworks: ['TEXTUAL_TRANSMISSION', 'INNOVATION_AND_TECHNOLOGY', 'CULTURAL_DIFFUSION', 'DOCTRINE_DEVELOPMENT'],
    causes: [
      { title: 'Ptolemaic patronage of learning', type: 'Institution', year: '3rd century BCE' },
      { title: 'Alexander the Great founds Alexandria', type: 'Person', year: '331 BCE' },
    ],
    effects: [
      { title: 'Systematic preservation of Greek knowledge', type: 'Movement', year: '3rd century BCE' },
      { title: 'Eratosthenes calculates Earth\'s circumference', type: 'EventWindow', year: 'c. 240 BCE' },
      { title: 'Septuagint translated here', type: 'Text', year: '3rd century BCE' },
    ],
    relationships: [
      { sourceSlug: 'library_of_alexandria', sourceName: 'Library of Alexandria', verb: 'OCCURS_IN', targetSlug: 'egypt', targetName: 'Egypt', context: 'Alexandria, Ptolemaic Egypt' },
    ],
    places: [
      { name: 'Alexandria', role: 'Location' },
    ],
    texts: [
      { title: 'Pinakes (catalog by Callimachus)', type: 'Library catalog' },
    ],
  },

  // ═══════════════════════════════════════════════════════════════
  // 780 — HISTORICAL & LITERARY TEXTS (hand-curated)
  // ═══════════════════════════════════════════════════════════════

  {
    slug: 'rihla_ibn_battuta',
    name: 'Rihla (The Travels of Ibn Battuta)',
    label: 'Text',
    callNumber: '780.01-rihla-ibn-battuta',
    subjectHeadings: ['Texts — Historical & Literary — Morocco — Medieval'],
    subjects: ['Travel', 'Geography', 'Islamic World', 'Ethnography', 'Medieval Society'],
    summary: 'Dictated by Ibn Battuta to Ibn Juzayy in 1355, this account of 73,000 miles of travel across the Islamic world and beyond is the most detailed eyewitness description of 14th-century societies from West Africa to China.',
    period: '1355',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    frameworks: ['CULTURAL_DIFFUSION', 'COMPARATIVE_RELIGION', 'ECONOMIC_SYSTEMS', 'TEXTUAL_TRANSMISSION'],
    causes: [
      { title: 'Ibn Battuta\'s 29-year journey', type: 'Person', year: '1325–1354', slug: 'ibn_battuta' },
    ],
    effects: [
      { title: 'Unparalleled record of medieval Islamic civilization', type: 'Evidence', year: '1355' },
    ],
    relationships: [
      { sourceSlug: 'rihla_ibn_battuta', sourceName: 'Rihla', verb: 'AUTHORED_BY', targetSlug: 'ibn_battuta', targetName: 'Ibn Battuta', context: 'Dictated to Ibn Juzayy in Fez' },
      { sourceSlug: 'rihla_ibn_battuta', sourceName: 'Rihla', verb: 'OCCURS_IN', targetSlug: 'morocco', targetName: 'Morocco', context: 'Composed in Fez' },
    ],
    places: [
      { name: 'Fez', role: 'Where dictated' },
    ],
    texts: [],
  },

  {
    slug: 'travels_of_marco_polo',
    name: 'The Travels of Marco Polo (Il Milione)',
    label: 'Text',
    callNumber: '780.02-travels-of-marco-polo',
    subjectHeadings: ['Texts — Historical & Literary — Italy — Medieval'],
    subjects: ['Travel', 'Silk Road', 'China', 'Mongol Empire', 'Trade', 'Geography'],
    summary: 'Account dictated by Marco Polo to Rustichello da Pisa in a Genoese prison (c. 1300), describing his 24-year journey through Asia. It introduced Europeans to the wealth, customs, and geography of China and Central Asia, directly inspiring Christopher Columbus and the Age of Exploration.',
    period: 'c. 1300',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Southern Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['CULTURAL_DIFFUSION', 'ECONOMIC_SYSTEMS', 'TEXTUAL_TRANSMISSION', 'GEOPOLITICAL_LINKAGE'],
    causes: [
      { title: 'Marco Polo\'s travels 1271–1295', type: 'Person', year: '1271–1295', slug: 'marco_polo' },
    ],
    effects: [
      { title: 'European fascination with the East', type: 'Movement', year: '14th–15th century' },
      { title: 'Columbus carries annotated copy on 1492 voyage', type: 'Person', year: '1492', slug: 'christopher_columbus' },
    ],
    relationships: [
      { sourceSlug: 'travels_of_marco_polo', sourceName: 'The Travels of Marco Polo', verb: 'AUTHORED_BY', targetSlug: 'marco_polo', targetName: 'Marco Polo', context: 'Dictated c. 1300' },
      { sourceSlug: 'travels_of_marco_polo', sourceName: 'The Travels of Marco Polo', verb: 'OCCURS_IN', targetSlug: 'italy', targetName: 'Italy', context: 'Composed in Genoa prison' },
    ],
    places: [
      { name: 'Genoa', role: 'Where dictated' },
    ],
    texts: [],
  },

  {
    slug: 'art_of_war',
    name: 'The Art of War (Sunzi Bingfa)',
    label: 'Text',
    callNumber: '780.03-art-of-war',
    subjectHeadings: ['Texts — Historical & Literary — China — Classical'],
    subjects: ['Military Strategy', 'Warfare', 'Philosophy', 'Leadership', 'Ancient China'],
    summary: 'The most influential military treatise in history, attributed to Sun Tzu (c. 5th century BCE). Its 13 chapters on strategy, tactics, terrain, and espionage have been applied to warfare, business, law, and diplomacy for over 2,500 years across every major civilization.',
    period: 'c. 5th century BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'East Asia',
    continent: 'Asia',
    status: 'Published',
    frameworks: ['CONFLICT_AND_RESOLUTION', 'CAUSE_AND_EFFECT', 'TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Warring States period', type: 'EventWindow', year: '5th century BCE' },
      { title: 'Sun Tzu\'s military experience', type: 'Person', year: 'c. 544–496 BCE', slug: 'sun_tzu' },
    ],
    effects: [
      { title: 'Canon of East Asian military thought', type: 'Movement', year: '5th century BCE onwards' },
      { title: 'Adopted globally as strategy text', type: 'Movement', year: '18th century onwards' },
    ],
    relationships: [
      { sourceSlug: 'art_of_war', sourceName: 'The Art of War', verb: 'AUTHORED_BY', targetSlug: 'sun_tzu', targetName: 'Sun Tzu', context: 'Traditional attribution' },
      { sourceSlug: 'art_of_war', sourceName: 'The Art of War', verb: 'OCCURS_IN', targetSlug: 'china', targetName: 'China', context: 'Composed in ancient China' },
    ],
    places: [
      { name: 'China', role: 'Origin' },
    ],
    texts: [],
  },
]
