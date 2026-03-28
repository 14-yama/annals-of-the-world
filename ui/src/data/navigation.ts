/* ─── Navigation & Exploration — Charting the Unknown ─── */

export interface Navigation {
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

export const NAVIGATION_CATEGORIES = [
  { id: 'instruments', label: 'Instruments & Tools',   color: '#D4AF37', icon: 'compass' },
  { id: 'ships',       label: 'Ships & Vessels',       color: '#3182CE', icon: 'ship' },
  { id: 'routes',      label: 'Routes & Trade Networks', color: '#C53030', icon: 'route' },
  { id: 'cartography', label: 'Maps & Cartography',    color: '#38A169', icon: 'map' },
  { id: 'expeditions', label: 'Expeditions & Voyages', color: '#8B4513', icon: 'flag' },
  { id: 'aerospace',   label: 'Aviation & Space',      color: '#6B3FA0', icon: 'rocket' },
] as const

export type NavigationCategory = (typeof NAVIGATION_CATEGORIES)[number]['id']

export const ERA_LABELS: Record<string, { label: string; color: string; period: string }> = {
  prehistoric:  { label: 'Prehistoric',     color: '#6B4D1B', period: 'Before 3,000 BCE' },
  ancient:      { label: 'Ancient World',   color: '#8B4513', period: '3,000 BCE – 500 CE' },
  medieval:     { label: 'Medieval',        color: '#A67C2E', period: '500 – 1500 CE' },
  earlyModern:  { label: 'Early Modern',    color: '#C5963A', period: '1500 – 1800 CE' },
  modern:       { label: 'Modern',          color: '#4A90D9', period: '1800 – 1945 CE' },
  contemporary: { label: 'Contemporary',    color: '#6B3FA0', period: '1945 CE – Present' },
}

export const NAVIGATION: Navigation[] = [
  /* ═══════════ PREHISTORIC ═══════════ */
  {
    slug: 'austronesian-ocean-crossing', name: 'Austronesian Ocean Crossings', era: 'prehistoric',
    category: 'expeditions', subcategory: 'Open-Ocean Migration',
    origin: 'Taiwan → Pacific', civilization: 'Austronesian',
    yearIntroduced: '~3,000 BCE',
    description: 'The Austronesians navigated thousands of miles of open Pacific ocean using stars, currents, wave patterns, and bird behavior. They colonized islands from Madagascar to Easter Island — the greatest migration in human history.',
    impact: 'Proved humans could navigate oceans without instruments. Settled every habitable island in the Pacific.',
  },
  {
    slug: 'outrigger-canoe', name: 'Outrigger Canoe', era: 'prehistoric',
    category: 'ships', subcategory: 'Ocean-Going Vessels',
    origin: 'Southeast Asia', civilization: 'Austronesian',
    yearIntroduced: '~3,000 BCE',
    description: 'The outrigger stabilizer allowed narrow canoes to handle ocean swells. Double-hulled catamarans could carry 80+ people with supplies. The most seaworthy vessels of the ancient world.',
    impact: 'Enabled the Polynesian colonization of the Pacific. The catamaran design is still used today.',
  },
  {
    slug: 'star-navigation', name: 'Celestial Navigation (Polynesian)', era: 'prehistoric',
    category: 'instruments', subcategory: 'Stellar Wayfinding',
    origin: 'Pacific Islands', civilization: 'Polynesian',
    yearIntroduced: '~3,000 BCE',
    description: 'Polynesian navigators memorized the positions of 220+ stars, their rising and setting points, and seasonal variations. Combined with wave piloting and bird observation, they could navigate 2,500+ miles of open ocean.',
    impact: 'The most sophisticated non-instrument navigation system ever developed. Modern revival by the Polynesian Voyaging Society.',
  },
  {
    slug: 'dugout-canoe', name: 'Dugout Canoe', era: 'prehistoric',
    category: 'ships', subcategory: 'River & Coastal Vessels',
    origin: 'Global', civilization: 'Multiple',
    yearIntroduced: '~8,000 BCE',
    description: 'Hollowed-out tree trunks were the first true boats, found independently in Europe, Africa, Asia, and the Americas. The Pesse canoe (Netherlands, ~8,000 BCE) is the oldest known boat.',
    impact: 'Opened rivers and coastlines as highways. Made fishing, trade, and migration dramatically easier.',
  },

  /* ═══════════ ANCIENT ═══════════ */
  {
    slug: 'phoenician-navigation', name: 'Phoenician Mediterranean Navigation', era: 'ancient',
    category: 'routes', subcategory: 'Maritime Trade Routes',
    origin: 'Lebanon', civilization: 'Phoenician',
    yearIntroduced: '~1,200 BCE',
    description: 'The Phoenicians established trading posts across the entire Mediterranean, navigating by the North Star (which the Greeks called "the Phoenician star"). They may have circumnavigated Africa around 600 BCE.',
    impact: 'Created the first maritime commercial network. Spread the alphabet across the Mediterranean world.',
  },
  {
    slug: 'silk-road', name: 'The Silk Road', era: 'ancient',
    category: 'routes', subcategory: 'Overland Trade Network',
    origin: 'China → Mediterranean', civilization: 'Chinese / Parthian / Roman',
    yearIntroduced: '~130 BCE',
    description: 'A 4,000-mile network of trade routes connecting Chang\'an (Xi\'an) to Rome. Silk, spices, ideas, religions, and diseases traveled along it. No single trader traveled the full route.',
    impact: 'The backbone of Eurasian civilization for 1,500 years. Spread Buddhism, Islam, and the Black Death.',
  },
  {
    slug: 'roman-roads', name: 'Roman Road System', era: 'ancient',
    category: 'routes', subcategory: 'Overland Infrastructure',
    origin: 'Roman Empire', civilization: 'Roman',
    yearIntroduced: '~312 BCE',
    description: 'The Via Appia was the first of 250,000 miles of paved roads connecting every corner of the empire. "All roads lead to Rome" — engineered with drainage, foundations, and milestones.',
    impact: 'Enabled rapid military deployment, trade, mail, and cultural unification. Many European roads still follow Roman routes.',
  },
  {
    slug: 'trireme-warship', name: 'Greek Trireme', era: 'ancient',
    category: 'ships', subcategory: 'War Galleys',
    origin: 'Greece', civilization: 'Greek',
    yearIntroduced: '~700 BCE',
    description: 'Three banks of oars powered by 170 rowers made the trireme the fastest warship in the ancient world. At Salamis (480 BCE), Greek triremes defeated the Persian fleet and saved Western civilization.',
    impact: 'Naval power determined who controlled the Mediterranean. Athens built democracy on trireme-powered trade.',
  },
  {
    slug: 'ptolemaic-world-map', name: 'Ptolemy\'s Geography', era: 'ancient',
    category: 'cartography', subcategory: 'Mathematical Cartography',
    origin: 'Alexandria, Egypt', civilization: 'Greco-Roman',
    yearIntroduced: '~150 CE',
    description: 'Claudius Ptolemy compiled the first atlas with latitude and longitude coordinates for 8,000 locations. His projections and grid systems remained the basis of cartography for 1,400 years.',
    impact: 'Founded mathematical cartography. Columbus used Ptolemy\'s (underestimated) world size to justify his voyage.',
  },
  {
    slug: 'monsoon-trade-winds', name: 'Monsoon Wind Navigation', era: 'ancient',
    category: 'instruments', subcategory: 'Wind Pattern Knowledge',
    origin: 'Indian Ocean', civilization: 'Indian / Arab / Greek',
    yearIntroduced: '~100 BCE',
    description: 'Hippalus (or his Arab/Indian predecessors) mastered the predictable monsoon wind reversals, enabling direct sailing across the Indian Ocean rather than coastal hugging. Summer winds blew east, winter winds blew west.',
    impact: 'Created the Indian Ocean trade network connecting Rome, India, and Southeast Asia. Maritime commerce boomed.',
  },
  {
    slug: 'eratosthenes-earth-size', name: 'Eratosthenes Measures the Earth', era: 'ancient',
    category: 'cartography', subcategory: 'Geodesy',
    origin: 'Alexandria, Egypt', civilization: 'Greek',
    yearIntroduced: '~240 BCE',
    description: 'Using shadow angles at Alexandria and Syene during the summer solstice, Eratosthenes calculated Earth\'s circumference to within 2% accuracy. Pure geometry, no instruments beyond a stick.',
    impact: 'Proved the Earth was round and measurable. His figure was used by navigators for centuries.',
  },

  /* ═══════════ MEDIEVAL ═══════════ */
  {
    slug: 'magnetic-compass', name: 'Magnetic Compass', era: 'medieval',
    category: 'instruments', subcategory: 'Direction Finding',
    origin: 'China', civilization: 'Chinese (Song Dynasty)',
    yearIntroduced: '~1040 CE',
    description: 'Magnetized needles floating in water bowls pointed north. Chinese navigators used compasses for ocean voyages by the 11th century. The technology reached Europe by the 12th century.',
    impact: 'The most important navigation instrument ever invented. Made reliable ocean navigation possible in any weather.',
  },
  {
    slug: 'viking-longship', name: 'Viking Longship', era: 'medieval',
    category: 'ships', subcategory: 'Ocean-Going Vessels',
    origin: 'Scandinavia', civilization: 'Norse / Viking',
    yearIntroduced: '~800 CE',
    description: 'Clinker-built with shallow draft, longships could cross the Atlantic and navigate rivers. They carried 60-80 warriors at 15 knots under sail. The most versatile vessels of the Middle Ages.',
    impact: 'Enabled Viking exploration of Iceland, Greenland, and North America — 500 years before Columbus.',
  },
  {
    slug: 'portolan-charts', name: 'Portolan Charts', era: 'medieval',
    category: 'cartography', subcategory: 'Nautical Charts',
    origin: 'Italian City-States', civilization: 'Genoese / Venetian',
    yearIntroduced: '~1275 CE',
    description: 'The first accurate nautical charts, based on compass bearings and estimated distances between ports. The Carta Pisana (~1275) is the oldest surviving example. They made Mediterranean trade reliable.',
    impact: 'Transformed navigation from oral tradition to written science. Essential for the Age of Exploration.',
  },
  {
    slug: 'astrolabe-maritime', name: 'Mariner\'s Astrolabe', era: 'medieval',
    category: 'instruments', subcategory: 'Celestial Measurement',
    origin: 'Islamic World → Europe', civilization: 'Arab / Portuguese',
    yearIntroduced: '~1200 CE',
    description: 'Simplified from the planispheric astrolabe, the mariner\'s version measured the altitude of the sun or Polaris to determine latitude at sea. Heavy brass construction resisted wind on deck.',
    impact: 'Gave navigators their north-south position. Essential tool for all European exploration voyages.',
  },
  {
    slug: 'zheng-he-voyages', name: 'Zheng He\'s Treasure Voyages', era: 'medieval',
    category: 'expeditions', subcategory: 'State-Sponsored Exploration',
    origin: 'China', civilization: 'Chinese (Ming Dynasty)',
    yearIntroduced: '1405 CE',
    description: 'Admiral Zheng He led seven massive fleets (300+ ships, 27,000 crew) across the Indian Ocean to Arabia and East Africa. His flagship was 400 feet long — the largest wooden ship ever built.',
    impact: 'Demonstrated Chinese naval supremacy. When the voyages stopped, China turned inward — the great "what if" of history.',
  },
  {
    slug: 'al-idrisi-world-map', name: 'Al-Idrisi\'s World Map (Tabula Rogeriana)', era: 'medieval',
    category: 'cartography', subcategory: 'World Maps',
    origin: 'Sicily', civilization: 'Arab / Norman',
    yearIntroduced: '1154 CE',
    description: 'Commissioned by Roger II of Sicily, al-Idrisi created the most accurate world map of the medieval period. Compiled from interviews with travelers, it remained the best world map for 300 years.',
    impact: 'Bridged Islamic and European geographical knowledge. Used by navigators across both civilizations.',
  },
  {
    slug: 'dhow-sailing-vessel', name: 'Arabian Dhow', era: 'medieval',
    category: 'ships', subcategory: 'Trading Vessels',
    origin: 'Arabian Peninsula', civilization: 'Arab',
    yearIntroduced: '~600 CE',
    description: 'Lateen-rigged dhows could sail closer to the wind than square-rigged European ships. They dominated Indian Ocean trade for a millennium, carrying spices, slaves, gold, and ideas.',
    impact: 'Connected East Africa, Arabia, India, and Southeast Asia into one trade network. Spread Islam across the Indian Ocean.',
  },

  /* ═══════════ EARLY MODERN ═══════════ */
  {
    slug: 'caravel', name: 'Portuguese Caravel', era: 'earlyModern',
    category: 'ships', subcategory: 'Exploration Vessels',
    origin: 'Portugal', civilization: 'Portuguese',
    yearIntroduced: '~1450 CE',
    description: 'The caravel combined lateen and square sails, allowing it to sail upwind and downwind. Light, fast, and maneuverable — the perfect exploration vessel. Columbus\'s Niña and Pinta were caravels.',
    impact: 'The ship that launched the Age of Exploration. Enabled European discovery of the Americas and the sea route to India.',
  },
  {
    slug: 'columbus-atlantic-crossing', name: 'Columbus\'s Atlantic Crossing', era: 'earlyModern',
    category: 'expeditions', subcategory: 'Transoceanic Voyage',
    origin: 'Spain', civilization: 'Spanish',
    yearIntroduced: '1492 CE',
    description: 'Three ships, 90 men, 10 weeks sailing into the unknown. Columbus didn\'t discover America — millions already lived there — but he connected two hemispheres permanently.',
    impact: 'The most consequential voyage in human history. Launched the Columbian Exchange, colonialism, and the modern world.',
  },
  {
    slug: 'mercator-projection', name: 'Mercator Projection', era: 'earlyModern',
    category: 'cartography', subcategory: 'Map Projections',
    origin: 'Flanders (Belgium)', civilization: 'Flemish',
    yearIntroduced: '1569 CE',
    description: 'Gerardus Mercator created a cylindrical map projection where lines of constant compass bearing appear as straight lines. Essential for navigation, but distorts size at high latitudes.',
    impact: 'The standard navigation chart for 450 years. Still used in web maps today (Google Maps). Shaped how we see the world.',
  },
  {
    slug: 'chronometer', name: 'Marine Chronometer (Harrison)', era: 'earlyModern',
    category: 'instruments', subcategory: 'Timekeeping',
    origin: 'England', civilization: 'British',
    yearIntroduced: '1761 CE',
    description: 'John Harrison\'s H4 clock solved the "longitude problem" — keeping accurate time at sea allowed sailors to calculate east-west position. It took him 31 years and a king\'s intervention to claim his prize.',
    impact: 'Solved the deadliest problem in navigation. Accurate longitude determination saved thousands of ships and lives.',
  },
  {
    slug: 'magellan-circumnavigation', name: 'Magellan\'s Circumnavigation', era: 'earlyModern',
    category: 'expeditions', subcategory: 'Global Voyage',
    origin: 'Spain (Portuguese captain)', civilization: 'Spanish / Portuguese',
    yearIntroduced: '1519 CE',
    description: 'Five ships and 270 men set out. Three years later, one ship and 18 men returned. Magellan died in the Philippines, but Elcano completed the first circumnavigation of Earth.',
    impact: 'Proved the Earth was round and the oceans connected. Demonstrated the true scale of the planet.',
  },
  {
    slug: 'sextant', name: 'Sextant', era: 'earlyModern',
    category: 'instruments', subcategory: 'Celestial Measurement',
    origin: 'England', civilization: 'British',
    yearIntroduced: '1731 CE',
    description: 'John Hadley\'s reflecting sextant measured the angle between a celestial body and the horizon with unprecedented accuracy. Compact, reliable, and usable in rough seas.',
    impact: 'The definitive navigation instrument for 250 years. Used until GPS made it redundant in the 1990s.',
  },
  {
    slug: 'cook-pacific-voyages', name: 'Captain Cook\'s Pacific Voyages', era: 'earlyModern',
    category: 'expeditions', subcategory: 'Scientific Exploration',
    origin: 'United Kingdom', civilization: 'British',
    yearIntroduced: '1768 CE',
    description: 'Three voyages mapped the Pacific, charted New Zealand and Australia, and searched for the Southern Continent. Cook carried Harrison\'s chronometer, proving longitude could be measured at sea.',
    impact: 'Completed the European mapping of the Pacific. Established the model for scientific exploration expeditions.',
  },
  {
    slug: 'galleon-trade', name: 'Manila Galleon Trade', era: 'earlyModern',
    category: 'routes', subcategory: 'Transpacific Trade',
    origin: 'Philippines → Mexico', civilization: 'Spanish',
    yearIntroduced: '1565 CE',
    description: 'The Manila Galleon route connected Asia to the Americas via the Pacific — the first regular transpacific trade. Chinese silk and porcelain traveled to Mexico; Mexican silver flowed to China.',
    impact: 'Created a truly global economy for the first time. Mexican silver became the world\'s currency.',
  },

  /* ═══════════ MODERN ═══════════ */
  {
    slug: 'steamship', name: 'Steamship', era: 'modern',
    category: 'ships', subcategory: 'Powered Vessels',
    origin: 'United Kingdom / United States', civilization: 'British / American',
    yearIntroduced: '1819 CE',
    description: 'The SS Savannah made the first Atlantic crossing using steam power (partially). By 1840, regular transatlantic steam service began. Ships no longer depended on wind.',
    impact: 'Revolutionized global trade and migration. Cut transatlantic crossing from 6 weeks to 6 days.',
  },
  {
    slug: 'suez-canal', name: 'Suez Canal', era: 'modern',
    category: 'routes', subcategory: 'Maritime Infrastructure',
    origin: 'Egypt', civilization: 'French / Egyptian',
    yearIntroduced: '1869 CE',
    description: 'A 120-mile canal connecting the Mediterranean to the Red Sea, eliminating the 6,000-mile voyage around Africa. 1.5 million forced laborers took 10 years to build it.',
    impact: 'Reshaped global trade. 12% of world commerce still passes through the Suez Canal today.',
  },
  {
    slug: 'panama-canal', name: 'Panama Canal', era: 'modern',
    category: 'routes', subcategory: 'Maritime Infrastructure',
    origin: 'Panama', civilization: 'American (with French origins)',
    yearIntroduced: '1914 CE',
    description: 'A 50-mile canal with locks lifting ships 85 feet above sea level. The most expensive construction project in history at the time. 25,000 workers died during French and American construction.',
    impact: 'Eliminated the 8,000-mile voyage around South America. Created a two-ocean US Navy.',
  },
  {
    slug: 'radio-navigation', name: 'Radio Navigation', era: 'modern',
    category: 'instruments', subcategory: 'Electronic Navigation',
    origin: 'Multiple Countries', civilization: 'Global',
    yearIntroduced: '1907 CE',
    description: 'Radio direction finders allowed ships to locate shore-based transmitters. Radio beacons, LORAN, and radar followed. For the first time, navigation worked in fog, storms, and darkness.',
    impact: 'Ended the era of "dead reckoning." Made navigation independent of visibility and weather conditions.',
  },
  {
    slug: 'wright-brothers-flight', name: 'Wright Brothers\' First Flight', era: 'modern',
    category: 'aerospace', subcategory: 'Powered Flight',
    origin: 'United States', civilization: 'American',
    yearIntroduced: '1903 CE',
    description: '12 seconds, 120 feet, and the world changed forever. Orville and Wilbur Wright achieved the first controlled, sustained, powered heavier-than-air flight at Kitty Hawk, North Carolina.',
    impact: 'Launched the aviation age. Within 66 years, humans would walk on the moon.',
  },
  {
    slug: 'transatlantic-flight', name: 'Lindbergh\'s Transatlantic Flight', era: 'modern',
    category: 'aerospace', subcategory: 'Long-Distance Aviation',
    origin: 'United States → France', civilization: 'American',
    yearIntroduced: '1927 CE',
    description: 'Solo, nonstop flight from New York to Paris in 33.5 hours. Charles Lindbergh\'s Spirit of St. Louis proved that aviation could connect continents. Aviation mania swept the world.',
    impact: 'Catalyzed the commercial aviation industry. Investment in airlines and airports exploded.',
  },
  {
    slug: 'northwest-passage', name: 'Northwest Passage (Amundsen)', era: 'modern',
    category: 'expeditions', subcategory: 'Polar Exploration',
    origin: 'Norway', civilization: 'Norwegian',
    yearIntroduced: '1906 CE',
    description: 'Roald Amundsen completed the first navigation of the Northwest Passage after a 3-year voyage. Centuries of failed attempts had killed thousands. He later became the first to reach the South Pole.',
    impact: 'Completed one of exploration\'s great quests. Climate change now makes the passage routinely navigable.',
  },
  {
    slug: 'sonar-development', name: 'Sonar', era: 'modern',
    category: 'instruments', subcategory: 'Underwater Detection',
    origin: 'United Kingdom / France', civilization: 'British / French',
    yearIntroduced: '1914 CE',
    description: 'Sound navigation and ranging detected underwater objects using acoustic pulses. Developed to counter the U-boat threat, sonar later mapped the ocean floor, revealing mid-ocean ridges and plate tectonics.',
    impact: 'Made submarine warfare and underwater navigation possible. Revealed the geography of the deep ocean.',
  },

  /* ═══════════ CONTEMPORARY ═══════════ */
  {
    slug: 'gps-system', name: 'GPS (Global Positioning System)', era: 'contemporary',
    category: 'instruments', subcategory: 'Satellite Navigation',
    origin: 'United States', civilization: 'American',
    yearIntroduced: '1978 CE',
    description: '24 satellites orbiting at 12,550 miles provide position accuracy within 3 feet anywhere on Earth. Originally military, GPS was opened to civilians in 1983 after Korean Air 007 was shot down.',
    impact: 'Made every person with a smartphone a navigator. Transformed logistics, agriculture, military, and daily life.',
  },
  {
    slug: 'apollo-moon-landing', name: 'Apollo 11 Moon Landing', era: 'contemporary',
    category: 'aerospace', subcategory: 'Space Exploration',
    origin: 'United States', civilization: 'American',
    yearIntroduced: '1969 CE',
    description: 'Neil Armstrong and Buzz Aldrin walked on the moon while the world watched. The navigation computer had less power than a modern calculator. "One small step for man, one giant leap for mankind."',
    impact: 'The greatest exploration achievement in human history. Proved that no destination is beyond human reach.',
  },
  {
    slug: 'international-space-station', name: 'International Space Station', era: 'contemporary',
    category: 'aerospace', subcategory: 'Orbital Habitation',
    origin: 'Multiple Countries', civilization: 'Global',
    yearIntroduced: '1998 CE',
    description: 'A 420-ton laboratory orbiting at 17,500 mph, continuously inhabited since November 2000. 15 nations collaborated to build it. The most expensive single object ever constructed ($150 billion).',
    impact: 'Proved long-term human habitation in space is possible. A model for international cooperation.',
  },
  {
    slug: 'mars-rovers', name: 'Mars Rover Exploration', era: 'contemporary',
    category: 'aerospace', subcategory: 'Planetary Exploration',
    origin: 'United States', civilization: 'American',
    yearIntroduced: '2004 CE',
    description: 'Spirit and Opportunity (2004), Curiosity (2012), and Perseverance (2021) have explored Mars remotely. Perseverance carries the Ingenuity helicopter — first powered flight on another planet.',
    impact: 'Extending exploration beyond Earth. Searching for evidence of past microbial life on Mars.',
  },
  {
    slug: 'voyager-interstellar', name: 'Voyager Interstellar Mission', era: 'contemporary',
    category: 'expeditions', subcategory: 'Interstellar Exploration',
    origin: 'United States', civilization: 'American',
    yearIntroduced: '1977 CE',
    description: 'Voyager 1 and 2 were launched to study Jupiter and Saturn. They\'re now in interstellar space — the farthest human-made objects from Earth. Each carries a Golden Record for alien civilizations.',
    impact: 'The most distant human exploration. Voyager 1 is 15 billion miles from Earth and still transmitting.',
  },
  {
    slug: 'google-maps', name: 'Digital Mapping (Google Maps)', era: 'contemporary',
    category: 'cartography', subcategory: 'Digital Cartography',
    origin: 'United States', civilization: 'Global',
    yearIntroduced: '2005 CE',
    description: 'Google Maps put the entire world\'s geography in everyone\'s pocket. Street View, satellite imagery, real-time traffic, and turn-by-turn navigation — cartography went from expert craft to everyday utility.',
    impact: 'Democratized navigation completely. Over 1 billion monthly users. Changed how humans perceive and interact with space.',
  },
  {
    slug: 'james-webb-telescope', name: 'James Webb Space Telescope', era: 'contemporary',
    category: 'aerospace', subcategory: 'Deep Space Observation',
    origin: 'United States / ESA / CSA', civilization: 'Global',
    yearIntroduced: '2021 CE',
    description: 'Orbiting 1 million miles from Earth, JWST\'s infrared vision peers back 13.5 billion years — to the first galaxies after the Big Bang. Its 6.5-meter mirror unfolds in space like origami.',
    impact: 'Rewriting our understanding of cosmic history. The deepest view of the universe ever achieved.',
  },
  {
    slug: 'autonomous-navigation', name: 'Autonomous Vehicle Navigation', era: 'contemporary',
    category: 'instruments', subcategory: 'AI Navigation',
    origin: 'United States / Global', civilization: 'Global',
    yearIntroduced: '~2015 CE',
    description: 'LiDAR, computer vision, and machine learning enable vehicles to navigate without human input. Tesla, Waymo, and others are making self-driving cars a reality. Ships and aircraft are following.',
    impact: 'May eliminate human navigation errors (which cause 94% of car crashes). The next revolution in transportation.',
  },
]
