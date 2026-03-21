import React, { useState } from 'react'
import { Box, SimpleGrid, Text, Flex, Heading, Input } from '@chakra-ui/react'
import { Globe, TrendingUp, Zap, Clock, Shield, Search } from 'lucide-react'
import { StatCard, InsightCard, DataTable, SectionHeading } from '../components/DataCards'

/* ── Static data drawn from analyses/Asia_Continent_Analysis.md ── */

const KEY_STATS = [
  { value: '48', label: 'Nations', detail: '60% of humanity', color: '#4A90D9' },
  { value: '4.7B', label: 'Population', detail: '60% of world population', color: '#D4AF37' },
  { value: '~38%', label: 'Global GDP', detail: 'Returning to historical dominance', color: '#2F855A' },
  { value: '180', label: 'Event Windows', detail: 'Prehistory to 2025 CE', color: '#8B3A3A' },
  { value: '228:1', label: 'Wealth Gap', detail: 'Singapore ($82k) to Afghanistan ($363)', color: '#D44' },
  { value: '90%', label: 'Advanced Chips', detail: 'Taiwan produces 90% of world\'s semiconductors', color: '#6B3FA0' },
]

const CONTINENTAL_TABLE = {
  title: 'Asia in Global Context',
  headers: ['Metric', 'Asia', 'Europe', 'Africa', 'Americas'],
  rows: [
    ['Population', '4.7B (60%)', '750M (9%)', '1.4B (18%)', '1.0B (13%)'],
    ['Share of Global GDP', '~38%', '~22%', '~3%', '~33%'],
    ['GDP Per Capita (avg)', '~$8,500', '~$33,000', '~$2,200', '~$17,000'],
    ['Median Age', '31.8', '42.5', '19.7', '31.0'],
    ['Languages', '~2,300', '~300', '~2,000', '~1,000'],
  ],
}

const WEALTH_TABLE = {
  title: 'The Wealth Chasm Within Asia',
  headers: ['Country', 'GDP Per Capita', 'Context'],
  rows: [
    ['Singapore', '$82,808', 'City-state, financial hub, zero natural resources'],
    ['Qatar', '$81,400', 'Gas wealth, 88% migrant workers'],
    ['Japan', '$33,950', '3rd-largest economy, median age 49'],
    ['South Korea', '$32,255', 'War-devastated → tech superpower in 60 years'],
    ['Myanmar', '$1,095', 'Military coup 2021, ongoing civil war'],
    ['Yemen', '$585', 'Civil war since 2014, worst humanitarian crisis'],
    ['Afghanistan', '$363', 'Perpetual conflict, Taliban 2.0, 40M people'],
  ],
}

const GOVERNANCE_TABLE = {
  title: 'Governance — Freedom House Scores',
  headers: ['Country', 'Score', 'Status'],
  rows: [
    ['Japan', '96', 'Free'],
    ['Taiwan', '94', 'Free'],
    ['Mongolia', '84', 'Free'],
    ['South Korea', '83', 'Free'],
    ['Timor-Leste', '72', 'Free'],
    ['Afghanistan', '8', 'Not Free'],
    ['North Korea', '3', 'Not Free'],
    ['Turkmenistan', '2', 'Not Free'],
    ['Syria', '1', 'Not Free'],
  ],
}

const HEALTH_TABLE = {
  title: 'Health & Development Gaps',
  headers: ['Metric', 'Best (Asia)', 'Worst (Asia)', 'Gap'],
  rows: [
    ['Life Expectancy', 'Japan (84.8)', 'Afghanistan (63.2)', '21.6 years'],
    ['Infant Mortality', 'Japan (1.8/1k)', 'Afghanistan (104/1k)', '58x'],
    ['Physicians/1k', 'Georgia (7.1)', 'Bangladesh (0.6)', '12x'],
    ['Maternal Mortality', 'Japan (4/100k)', 'Afghanistan (620/100k)', '155x'],
  ],
}

const EVENT_CATEGORIES = [
  { category: 'Cultural Exchange & Diffusion', events: 7, span: '800 BCE–2025', pattern: 'Silk Road → K-Pop pipeline', color: '#D4AF37' },
  { category: 'Technological Innovation', events: 15, span: '10000 BCE–2025', pattern: 'Neolithic → AI adoption', color: '#4A90D9' },
  { category: 'Trade & Economy', events: 11, span: '500 CE–2025', pattern: 'Spice trade → e-commerce', color: '#2F855A' },
  { category: 'War & Conflict', events: 7, span: '1914–1991', pattern: '3 world wars fought in Asia', color: '#D44' },
  { category: 'Religious Expansion', events: 11, span: '1000 BCE–2020', pattern: 'Buddhism, Islam, Christianity, Hinduism', color: '#8B3A3A' },
  { category: 'Finance & Monetary', events: 12, span: '650 BCE–2025', pattern: 'Coinage → fintech', color: '#6B3FA0' },
  { category: 'Health & Pandemics', events: 6, span: '1346–2023', pattern: 'Black Death → COVID-19', color: '#C53030' },
  { category: 'Governance & Regulation', events: 9, span: '2005–2025', pattern: 'E-governance → AI safety', color: '#2563A0' },
  { category: 'Migration & Demography', events: 5, span: '70000 BCE–2025', pattern: 'Peopling of Asia → aging crisis', color: '#876322' },
  { category: 'Environment & Climate', events: 6, span: '26000 BCE–2025', pattern: 'Ice age → NDC pledges', color: '#38A169' },
  { category: 'Infrastructure & Connectivity', events: 4, span: '1970–2025', pattern: 'Containerization → Belt & Road', color: '#DD6B20' },
  { category: 'Media & Communication', events: 3, span: '1990–2025', pattern: 'Satellite TV → social media', color: '#B83280' },
  { category: 'Education & Knowledge', events: 4, span: '1500–2025', pattern: 'Print culture → EdTech', color: '#5B21B6' },
]

const HIDDEN_PATTERNS = [
  {
    title: 'The Asian Return, Not Rise',
    insight: 'Asia produced 60-70% of global GDP until ~1800. The "rise of Asia" is actually a restoration to historical baseline after 200 years of European colonial disruption. China and India alone accounted for 50% of global output for most of recorded history.',
    source: 'Angus Maddison, Historical Statistics of the World Economy',
  },
  {
    title: 'The Semiconductor Chokepoint',
    insight: 'Taiwan (TSMC) produces 90% of the world\'s advanced chips. South Korea (Samsung) produces most of the rest. A single earthquake, invasion, or drought in Taiwan could collapse the global economy. No other supply chain bottleneck has been this concentrated.',
    source: 'WIPO, Semiconductor Industry Association, 2024',
    accent: '#D44',
  },
  {
    title: 'The Youth-Age Collision',
    insight: 'Japan (median age 49), South Korea (44), China (39) age rapidly. India (28), Philippines (26), Afghanistan (18) are young. By 2050, half of Asia\'s workers will be in South Asia — but the wealth is in East Asia. This is a continental collision in slow motion.',
    source: 'UN Population Division, 2024',
    accent: '#4A90D9',
  },
  {
    title: 'Water Wars Are Already Here',
    insight: 'China\'s Three Gorges and Mekong dams control water for 60M+ people downstream. India and Pakistan share the Indus. Turkey\'s GAP project controls the Euphrates for Syria and Iraq. Every major Asian river is now a geopolitical weapon.',
    source: 'UNDP Water Governance Reports',
    accent: '#2F855A',
  },
  {
    title: 'Religion as Geopolitical Force',
    insight: 'No other continent has religion so tightly woven into modern politics: Islam shapes governance in 15+ nations, Buddhism drives identity in Myanmar, Sri Lanka, Thailand. Hinduism defines India\'s political trajectory. Judaism anchors Israeli statehood. Confucianism structures East Asian governance.',
    source: 'Pew Research Center, Freedom House',
    accent: '#8B3A3A',
  },
  {
    title: 'The AI Triad',
    insight: 'Three countries will determine Asia\'s AI future: China (state-directed, surveillance-integrated), Japan (robotics + aging society), and India (talent pipeline, 4.4M developers). Everything else is commentary.',
    source: 'Stanford AI Index, 2024',
    accent: '#6B3FA0',
  },
]

const FIVE_ASIAS = [
  {
    name: 'East Asia',
    subtitle: 'The Economic Titans',
    countries: 'China, Japan, South Korea, Taiwan, Mongolia, North Korea',
    pop: '1.7B',
    gdpShare: '~25% of global GDP',
    highlights: [
      'China: 2nd-largest economy, Belt & Road reshaping 140+ countries',
      'Japan: Most aged society on Earth (29% over 65 by 2030)',
      'South Korea: GDP/capita grew 370x since 1960 ($158 → $32,255)',
      'Taiwan: 90% of world\'s advanced semiconductors (TSMC)',
    ],
    color: '#D44',
  },
  {
    name: 'South Asia',
    subtitle: 'The Population Engine',
    countries: 'India, Pakistan, Bangladesh, Sri Lanka, Nepal, Bhutan, Maldives, Afghanistan',
    pop: '2.0B',
    gdpShare: '25% of humanity',
    highlights: [
      'India: Most populous country (1.44B), 5th-largest economy',
      'Bangladesh: Garment industry = 84% of global fast fashion',
      'Bhutan: Only carbon-negative country on Earth',
      'Maldives: Highest point 5.1m — existential climate threat',
    ],
    color: '#D4AF37',
  },
  {
    name: 'Southeast Asia',
    subtitle: 'The Diversity Belt',
    countries: 'Indonesia, Philippines, Vietnam, Thailand, Myanmar, Malaysia, Cambodia, Laos, Singapore, Timor-Leste, Brunei',
    pop: '700M',
    gdpShare: 'ASEAN = 5th-largest economy',
    highlights: [
      'Indonesia: 17,508 islands, largest Muslim-majority nation',
      'Vietnam: 8% annual GDP growth for 30 years',
      'Singapore: 734 km² → 4th-highest GDP/capita on Earth',
      'Thailand: Only SE Asian country never colonized',
    ],
    color: '#2F855A',
  },
  {
    name: 'Central Asia',
    subtitle: 'The Heartland',
    countries: 'Kazakhstan, Uzbekistan, Turkmenistan, Kyrgyzstan, Tajikistan',
    pop: '75M',
    gdpShare: 'Post-Soviet since 1991',
    highlights: [
      'Kazakhstan: 9th-largest country, more land than Western Europe',
      'Turkmenistan: 4th-largest gas reserves, most closed society',
      'All 5 gained independence in 1991 with no independence movements',
    ],
    color: '#6B3FA0',
  },
  {
    name: 'West Asia',
    subtitle: 'The Energy Nexus',
    countries: 'Saudi Arabia, Iran, Iraq, Israel, UAE, Turkey, Syria, Jordan, Lebanon, Kuwait, Oman, Bahrain, Qatar, Yemen',
    pop: '400M',
    gdpShare: '~55% of global oil reserves',
    highlights: [
      'Saudi Arabia: Vision 2030, $500B NEOM megaproject',
      'Israel: More startups per capita than any nation',
      'UAE: Dubai went from fishing village to global hub in 50 years',
      'Syria: 6.8M refugees — largest displacement since WWII',
    ],
    color: '#4A90D9',
  },
]

export default function AsiaDashboard() {
  const [eventFilter, setEventFilter] = useState('')

  const filteredCategories = EVENT_CATEGORIES.filter(
    (c) =>
      c.category.toLowerCase().includes(eventFilter.toLowerCase()) ||
      c.pattern.toLowerCase().includes(eventFilter.toLowerCase())
  )

  return (
    <Box>
      {/* Page Header */}
      <Box mb={8}>
        <Flex align="center" gap={3} mb={2}>
          <Globe size={28} color="#4A90D9" />
          <Heading
            fontFamily='"Cinzel", serif'
            fontSize="3xl"
            fontWeight={700}
            color="#2D2A24"
          >
            Asia
          </Heading>
        </Flex>
        <Text
          fontFamily='"Cormorant Garamond", serif'
          fontSize="lg"
          color="#524E44"
          maxW="700px"
        >
          Asia is not rising — it is{' '}
          <Text as="span" fontStyle="italic" fontWeight={600}>
            returning
          </Text>
          . For 18 of the last 20 centuries, Asia produced more than half the world's GDP.
          48 nations, 4.7 billion people, 2,300 languages, and 180 event windows spanning
          70,000 years of history.
        </Text>
        <Box h="3px" bg="#4A90D9" w="80px" mt={4} />
      </Box>

      {/* Key Stats Grid */}
      <SectionHeading title="Key Indicators" subtitle="Asia at a glance — 48 nations, 4.7 billion people" />
      <SimpleGrid columns={{ base: 2, md: 3 }} gap={4} mb={8}>
        {KEY_STATS.map((s) => (
          <StatCard key={s.label} {...s} />
        ))}
      </SimpleGrid>

      {/* Data Tables */}
      <SectionHeading title="Comparative Data" subtitle="Asia in global and internal context" />
      <SimpleGrid columns={{ base: 1, lg: 2 }} gap={5} mb={8}>
        <DataTable {...CONTINENTAL_TABLE} />
        <DataTable {...WEALTH_TABLE} />
      </SimpleGrid>
      <SimpleGrid columns={{ base: 1, lg: 2 }} gap={5} mb={8}>
        <DataTable {...GOVERNANCE_TABLE} />
        <DataTable {...HEALTH_TABLE} />
      </SimpleGrid>

      {/* The Five Asias */}
      <SectionHeading
        title="The Five Asias"
        subtitle="Asia is not one continent — it is at minimum five"
      />
      <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={4} mb={8}>
        {FIVE_ASIAS.map((r) => (
          <Box
            key={r.name}
            bg="white"
            border="1px solid"
            borderColor="#E4E2DC"
            borderRadius="lg"
            p={5}
            position="relative"
            overflow="hidden"
          >
            <Box
              position="absolute"
              top={0}
              left={0}
              w="100%"
              h="4px"
              bg={r.color}
            />
            <Text
              fontFamily='"Cinzel", serif'
              fontSize="lg"
              fontWeight={700}
              color={r.color}
              mt={1}
            >
              {r.name}
            </Text>
            <Text
              fontFamily='"Cormorant Garamond", serif'
              fontSize="sm"
              fontWeight={600}
              color="#2D2A24"
            >
              {r.subtitle}
            </Text>
            <Text fontSize="xs" color="#96770B" mt={1}>
              {r.countries}
            </Text>
            <Flex gap={3} mt={2} mb={2}>
              <Text fontSize="xs" fontWeight={600} color="#524E44">
                {r.pop} people
              </Text>
              <Text fontSize="xs" color="#9E9A90">
                {r.gdpShare}
              </Text>
            </Flex>
            {r.highlights.map((h, i) => (
              <Text key={i} fontSize="xs" color="#524E44" lineHeight={1.5} mt={1}>
                • {h}
              </Text>
            ))}
          </Box>
        ))}
      </SimpleGrid>

      {/* Event Windows Timeline */}
      <SectionHeading
        title="180 Event Windows"
        subtitle="Patterns across 70,000 years of Asian history — organized by category"
      />
      <Box mb={4}>
        <Flex align="center" gap={2} maxW="300px">
          <Search size={16} color="#9E9A90" />
          <Input
            placeholder="Filter categories..."
            size="sm"
            value={eventFilter}
            onChange={(e) => setEventFilter(e.target.value)}
            bg="white"
            borderColor="#E4E2DC"
            fontSize="sm"
            _focus={{ borderColor: '#4A90D9' }}
          />
        </Flex>
      </Box>
      <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={3} mb={8}>
        {filteredCategories.map((c) => (
          <Box
            key={c.category}
            bg="white"
            border="1px solid"
            borderColor="#E4E2DC"
            borderRadius="md"
            p={4}
            position="relative"
            overflow="hidden"
          >
            <Box
              position="absolute"
              top={0}
              left={0}
              w="4px"
              h="100%"
              bg={c.color}
            />
            <Flex justify="space-between" align="flex-start">
              <Text
                fontFamily='"Inter", sans-serif'
                fontSize="sm"
                fontWeight={600}
                color="#2D2A24"
              >
                {c.category}
              </Text>
              <Text
                fontSize="xs"
                fontWeight={700}
                color={c.color}
                bg={`${c.color}15`}
                px={2}
                py={0.5}
                borderRadius="full"
              >
                {c.events}
              </Text>
            </Flex>
            <Text fontSize="xs" color="#9E9A90" mt={1}>
              {c.span}
            </Text>
            <Text fontSize="xs" color="#524E44" mt={1} fontStyle="italic">
              {c.pattern}
            </Text>
          </Box>
        ))}
      </SimpleGrid>

      {/* Hidden Patterns */}
      <SectionHeading
        title="Hidden Patterns"
        subtitle="Non-obvious insights from 48-country analysis"
      />
      <SimpleGrid columns={{ base: 1, md: 2 }} gap={5} mb={8}>
        {HIDDEN_PATTERNS.map((p) => (
          <InsightCard key={p.title} {...p} />
        ))}
      </SimpleGrid>

      {/* Source Attribution */}
      <Box
        bg="#F5F4F0"
        borderRadius="lg"
        p={5}
        border="1px solid"
        borderColor="#E4E2DC"
      >
        <Text fontSize="xs" color="#9E9A90" fontWeight={600}>
          Data Sources
        </Text>
        <Text fontSize="xs" color="#9E9A90" mt={1}>
          World Bank, IMF, UNDP, WHO, FAO, Freedom House, WIPO, CIA Factbook, GSMA, UNESCO,
          IEA, UNAIDS, Pew Research Center, Stanford AI Index, Semiconductor Industry Association.
          180 event windows from Asian-Event_Window/master-events.csv. Country profiles from
          geo-registry/places/countries/. All statistics 2023-2024 unless noted.
        </Text>
      </Box>
    </Box>
  )
}
