import React from 'react'
import { Box, SimpleGrid, Text, Flex, Heading } from '@chakra-ui/react'
import { Globe, Users, Heart, Shield, Landmark, TrendingUp } from 'lucide-react'
import { StatCard, InsightCard, DataTable, SectionHeading } from '../components/DataCards'

/* ── Static data drawn from analyses/Africa_Continent_Analysis.md ── */

const KEY_STATS = [
  { value: '55', label: 'Nations', detail: '54 AU members + Western Sahara', color: '#8B3A3A' },
  { value: '1.4B', label: 'Population', detail: '18% of humanity', color: '#D4AF37' },
  { value: '~3%', label: 'Global GDP', detail: 'Despite 30% of mineral reserves', color: '#D44' },
  { value: '19.7', label: 'Median Age', detail: 'Youngest continent on Earth', color: '#2F855A' },
  { value: '2,000+', label: 'Languages', detail: '30% of world\'s linguistic diversity', color: '#4A90D9' },
  { value: '30%', label: 'Global Minerals', detail: '50% diamonds, 70% cobalt, 80% vanilla', color: '#8B3A3A' },
]

const DEMOGRAPHICS_TABLE = {
  title: 'Continental Demographics Comparison',
  headers: ['Metric', 'Africa', 'Europe', 'Asia', 'Americas'],
  rows: [
    ['Median Age', '19.7', '42.5', '31.8', '31.0'],
    ['Fertility Rate', '4.1', '1.5', '2.0', '1.9'],
    ['Population Growth', '2.5%/yr', '-0.1%/yr', '0.8%/yr', '0.8%/yr'],
    ['Projected 2050 Pop.', '2.5B', '720M', '5.3B', '1.2B'],
  ],
}

const ECONOMIC_TABLE = {
  title: 'The Economic Paradox',
  headers: ['Metric', 'Africa (55)', 'Europe (44)', 'Asia (48)', 'Americas (35)'],
  rows: [
    ['Share of Global GDP', '~3%', '~22%', '~38%', '~33%'],
    ['Share of Global Pop.', '~18%', '~9%', '~60%', '~13%'],
    ['GDP Per Capita (avg)', '~$2,200', '~$33,000', '~$8,500', '~$17,000'],
    ['Resource Share', '~30% minerals', '~5%', '~20%', '~20%'],
  ],
}

const HEALTH_TABLE = {
  title: 'Health Burden — Maternal Mortality',
  headers: ['Region', 'Per 100,000 births'],
  rows: [
    ['Sub-Saharan Africa', '545'],
    ['South Asia', '163'],
    ['Southeast Asia', '99'],
    ['Latin America', '88'],
    ['Europe', '8'],
  ],
}

const FREEDOM_TABLE = {
  title: 'Freedom House Scores',
  headers: ['Category', 'Count', 'Examples'],
  rows: [
    ['Free (70+)', '7', 'Cabo Verde (92), Ghana (80), Botswana'],
    ['Partly Free', '19', 'Senegal, Kenya, Tanzania'],
    ['Not Free (<35)', '29', 'Eritrea (1), South Sudan (2)'],
  ],
}

const HIDDEN_PATTERNS = [
  {
    title: 'The Colonial Resource Trap',
    insight: 'Africa produces 50% of the world\'s diamonds, 70% of cobalt, 70% of platinum, and 80% of vanilla — yet captures less than 5% of processing and manufacturing value. The extraction-without-industrialization pattern is a direct continuity from colonial-era economic structures.',
    source: 'Global commodity reports, 2024',
  },
  {
    title: 'HIV Follows Mining Routes',
    insight: 'The HIV prevalence belt across Southern Africa (Eswatini 26%, South Africa 18%, Lesotho 21%) maps almost exactly onto colonial-era migrant mining corridors. The disease spread along labor migration paths established by British and Boer gold/diamond operations.',
    source: 'UNAIDS, 2024; Historical mining archives',
    accent: '#C53030',
  },
  {
    title: 'Island Exception',
    insight: 'Africa\'s island nations (Mauritius, Seychelles, Cabo Verde) vastly outperform mainland countries on every governance metric. Mauritius ranks 57th globally in innovation — higher than many European nations. No arbitrary borders, no ethnic partitioning, no landlocked penalty.',
    source: 'WIPO Global Innovation Index, 2024',
    accent: '#2F855A',
  },
  {
    title: 'Mobile Money Leapfrog',
    insight: 'Africa skipped traditional banking entirely — going straight to mobile money. M-Pesa in Kenya processes more transactions than PayPal. Over 35M active mobile money accounts continent-wide. The unbanked are becoming the most financially innovative population on Earth.',
    source: 'GSMA Mobile Money Report, 2024',
    accent: '#4A90D9',
  },
  {
    title: 'The Coup Belt = The French Belt',
    insight: '9 successful coups since 2020, almost all in the Sahel — and almost all in former French colonies. Burkina Faso (2 coups in 9 months), Mali, Guinea, Niger, Chad, Sudan, Gabon. The CFA franc zone and French military presence correlate with political instability.',
    source: 'Freedom House, 2024',
  },
  {
    title: 'Straight-Line Borders, Curved Conflicts',
    insight: '84% of African borders follow latitude/longitude lines or geometric shapes drawn at the 1884 Berlin Conference. These borders cut through 177 ethnic groups. Every major African conflict since independence traces back to this partition.',
    source: 'AU Border Programme; Michalopoulos & Papaioannou, 2016',
    accent: '#8B3A3A',
  },
]

const REGIONAL_HIGHLIGHTS = [
  {
    region: 'North Africa',
    countries: 'Algeria, Egypt, Libya, Morocco, Mauritania, Sudan, Tunisia',
    highlight: 'Algeria has a Gini coefficient of 27.6 — lower than Sweden. Egypt fits 100M people on 4% of its land. Morocco is 14km from Spain and manufactures cars.',
  },
  {
    region: 'West Africa',
    countries: 'Nigeria, Ghana, Senegal, Côte d\'Ivoire, Mali + 11 more',
    highlight: 'Nigeria: 230M people, 5 active conflicts. Côte d\'Ivoire controls 40% of global cocoa. Cabo Verde scores 92 on Freedom House — highest in Africa.',
  },
  {
    region: 'East Africa',
    countries: 'Kenya, Ethiopia, Tanzania, Rwanda, Uganda + 8 more',
    highlight: 'Rwanda: 61% women in parliament — world\'s highest. Ethiopia runs on a different calendar (13 months). Kenya\'s M-Pesa revolutionized global finance.',
  },
  {
    region: 'Central Africa',
    countries: 'DR Congo, Cameroon, Gabon, Chad, CAR + 2 more',
    highlight: 'DR Congo: 2.34M km², richest mineral deposits on Earth, yet 1% rural electrification. Chad: 1,140 maternal deaths per 100k — world\'s highest.',
  },
  {
    region: 'Southern Africa',
    countries: 'South Africa, Botswana, Zambia, Zimbabwe, Mozambique + 5 more',
    highlight: 'Botswana: Diamond democracy — transformed from poorest to upper-middle income. South Africa: Gini 63 — most unequal country on Earth.',
  },
]

export default function AfricaDashboard() {
  return (
    <Box>
      {/* Page Header */}
      <Box mb={8}>
        <Flex align="center" gap={3} mb={2}>
          <Globe size={28} color="#8B3A3A" />
          <Heading
            fontFamily='"Cinzel", serif'
            fontSize="3xl"
            fontWeight={700}
            color="#2D2A24"
          >
            Africa
          </Heading>
        </Flex>
        <Text
          fontFamily='"Cormorant Garamond", serif'
          fontSize="lg"
          color="#524E44"
          maxW="700px"
        >
          Comprehensive analysis of 55 nations revealing: Africa is not poor — it is{' '}
          <Text as="span" fontStyle="italic" fontWeight={600}>
            plundered
          </Text>
          . The continent holds 30% of global mineral reserves, 60% of uncultivated arable land,
          and Earth's youngest population — yet accounts for only 3% of global GDP.
        </Text>
        <Box h="3px" bg="#8B3A3A" w="80px" mt={4} />
      </Box>

      {/* Key Stats Grid */}
      <SectionHeading title="Key Indicators" subtitle="Africa at a glance — 55 nations, 1.4 billion people" />
      <SimpleGrid columns={{ base: 2, md: 3 }} gap={4} mb={8}>
        {KEY_STATS.map((s) => (
          <StatCard key={s.label} {...s} />
        ))}
      </SimpleGrid>

      {/* Data Tables */}
      <SectionHeading title="Comparative Data" subtitle="How Africa measures against other continents" />
      <SimpleGrid columns={{ base: 1, lg: 2 }} gap={5} mb={8}>
        <DataTable {...DEMOGRAPHICS_TABLE} />
        <DataTable {...ECONOMIC_TABLE} />
      </SimpleGrid>
      <SimpleGrid columns={{ base: 1, lg: 2 }} gap={5} mb={8}>
        <DataTable {...HEALTH_TABLE} />
        <DataTable {...FREEDOM_TABLE} />
      </SimpleGrid>

      {/* Hidden Patterns */}
      <SectionHeading
        title="Hidden Patterns"
        subtitle="Non-obvious insights from 55-country deep analysis"
      />
      <SimpleGrid columns={{ base: 1, md: 2 }} gap={5} mb={8}>
        {HIDDEN_PATTERNS.map((p) => (
          <InsightCard key={p.title} {...p} />
        ))}
      </SimpleGrid>

      {/* Regional Highlights */}
      <SectionHeading
        title="Regional Breakdown"
        subtitle="5 regions, each with its own story"
      />
      <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={4} mb={8}>
        {REGIONAL_HIGHLIGHTS.map((r) => (
          <Box
            key={r.region}
            bg="white"
            border="1px solid"
            borderColor="#E4E2DC"
            borderRadius="lg"
            p={5}
          >
            <Text
              fontFamily='"Cinzel", serif'
              fontSize="lg"
              fontWeight={700}
              color="#8B3A3A"
            >
              {r.region}
            </Text>
            <Text fontSize="xs" color="#96770B" mt={1}>
              {r.countries}
            </Text>
            <Text fontSize="sm" color="#524E44" mt={3} lineHeight={1.6}>
              {r.highlight}
            </Text>
          </Box>
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
          World Bank, IMF, UNDP, WHO, FAO, Freedom House, Global Peace Index, UNESCO, ITU,
          WIPO, UNWTO, CIA Factbook, UNAIDS, GSMA, AU Border Programme. All data points
          verified against multiple sources per Project Instruction Guide (Chicago 17 citation
          standard). Country profiles contain ~319 data points each.
        </Text>
      </Box>
    </Box>
  )
}
