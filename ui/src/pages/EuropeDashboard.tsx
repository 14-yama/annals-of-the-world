import React from 'react'
import { Box, SimpleGrid, Text, Flex, Heading } from '@chakra-ui/react'
import { Globe, Landmark, Scale, Lightbulb, Palette, TrendingUp } from 'lucide-react'
import { StatCard, InsightCard, DataTable, SectionHeading } from '../components/DataCards'
import Breadcrumb from '../components/Breadcrumb'

/* ── Static data — Europe (skeleton, expanding with research) ── */

const KEY_STATS = [
  { value: '44', label: 'Nations', detail: '27 in the European Union', color: '#3182CE' },
  { value: '750M', label: 'Population', detail: '9% of humanity', color: '#D4AF37' },
  { value: '~22%', label: 'Global GDP', detail: '$23 trillion combined', color: '#2F855A' },
  { value: '42.5', label: 'Median Age', detail: 'Oldest continent by population', color: '#D44' },
  { value: '200+', label: 'Languages', detail: '24 official EU languages', color: '#805AD5' },
  { value: '84%', label: 'Colonized World', detail: 'European powers colonized 84% of Earth', color: '#8B3A3A' },
]

const DEMOGRAPHICS_TABLE = {
  title: 'European Demographics',
  headers: ['Metric', 'Europe', 'Global Average'],
  rows: [
    ['Median Age', '42.5', '30.5'],
    ['Fertility Rate', '1.5', '2.3'],
    ['Population Growth', '-0.1%/yr', '0.8%/yr'],
    ['Urbanization', '75%', '56%'],
    ['Life Expectancy', '78.5 yrs', '73.4 yrs'],
  ],
}

const ECONOMIC_TABLE = {
  title: 'Economic Powerhouses',
  headers: ['Country', 'GDP (Nominal)', 'GDP Per Capita', 'Key Sector'],
  rows: [
    ['Germany', '$4.3T', '$51,200', 'Manufacturing, Automotive'],
    ['United Kingdom', '$3.1T', '$45,800', 'Finance, Services'],
    ['France', '$2.9T', '$42,300', 'Luxury goods, Aerospace'],
    ['Italy', '$2.0T', '$34,100', 'Fashion, Agriculture'],
    ['Spain', '$1.4T', '$29,600', 'Tourism, Renewable energy'],
    ['Netherlands', '$1.0T', '$57,000', 'Trade, Agriculture tech'],
  ],
}

const GOVERNANCE_TABLE = {
  title: 'Freedom House Scores — Europe',
  headers: ['Country', 'Score', 'Status'],
  rows: [
    ['Norway', '100', 'Free'],
    ['Finland', '100', 'Free'],
    ['Sweden', '100', 'Free'],
    ['Germany', '94', 'Free'],
    ['France', '90', 'Free'],
    ['Hungary', '66', 'Partly Free'],
    ['Turkey', '32', 'Not Free'],
    ['Russia', '16', 'Not Free'],
    ['Belarus', '8', 'Not Free'],
  ],
}

const HEALTH_TABLE = {
  title: 'Health Indicators — Europe',
  headers: ['Metric', 'Western Europe', 'Eastern Europe', 'Global'],
  rows: [
    ['Life Expectancy', '82.0 yrs', '74.5 yrs', '73.4 yrs'],
    ['Maternal Mortality (per 100k)', '5', '18', '223'],
    ['Infant Mortality (per 1k)', '3.0', '7.5', '27'],
    ['Physicians per 10k', '40', '32', '15'],
    ['Mental Health Burden', '18% of DALYs', '15% of DALYs', '13% of DALYs'],
  ],
}

const EU_TABLE = {
  title: 'European Union at a Glance',
  headers: ['Metric', 'Value'],
  rows: [
    ['Member States', '27 countries'],
    ['Combined GDP', '~$18 trillion'],
    ['Schengen Area', '27 countries, passport-free travel'],
    ['Euro Currency', '20 nations (Eurozone)'],
    ['Founded', '1993 (Maastricht Treaty)'],
    ['Predecessors', 'ECSC (1951), EEC (1957)'],
  ],
}

const HIDDEN_PATTERNS = [
  {
    title: 'The Democratic Origin Paradox',
    insight: 'Europe invented democracy in Athens (508 BCE) — then spent the next 2,300 years perfecting autocracy. European democracy only became widespread after 1945, largely because the US insisted on it as a condition for Marshall Plan reconstruction.',
    source: 'Freedom House; Historical records',
  },
  {
    title: 'The Colonial Boomerang',
    insight: 'Europe colonized 84% of Earth\'s surface at its peak. Today, 14% of EU residents are foreign-born, many from former colonies. The demographic patterns of immigration mirror the exact routes of colonial extraction — people follow the wealth that was taken from them.',
    source: 'Eurostat, 2024; Historical colonial records',
    accent: '#C53030',
  },
  {
    title: 'The Aging Catastrophe',
    insight: 'Europe is the only continent with negative population growth. By 2050, there will be 2 retirees for every 3 workers. Italy and Germany already have more deaths than births annually. Without immigration, the EU labor force would shrink by 20% by 2060.',
    source: 'UN Population Division; Eurostat projections',
    accent: '#D44',
  },
  {
    title: 'Small-Country Outperformance',
    insight: 'The top-performing European nations by nearly every metric (HDI, innovation, governance, happiness) are all small: Norway, Denmark, Finland, Switzerland, Iceland, Luxembourg. Large nations (France, UK, Italy, Spain) consistently underperform relative to resources.',
    source: 'UNDP HDI, World Happiness Report, WIPO Innovation Index',
    accent: '#2F855A',
  },
  {
    title: 'The North-South Divide',
    insight: 'Germany\'s GDP per capita is 3x Greece\'s. Northern Europe dominates innovation, governance, and wealth — while Southern and Eastern Europe lag. This north-south gradient has been persistent for centuries and the EU has not closed it despite decades of structural funds.',
    source: 'Eurostat Regional GDP, World Bank',
    accent: '#4A90D9',
  },
  {
    title: 'Energy Dependency Trap',
    insight: 'Europe generates only 40% of its energy domestically. Before 2022, 40% of EU gas came from Russia. The Ukraine war exposed this vulnerability: energy prices tripled overnight. Europe is now racing toward renewables — not out of idealism, but survival.',
    source: 'IEA, Eurostat Energy Statistics, 2024',
    accent: '#805AD5',
  },
]

const REGIONAL_HIGHLIGHTS = [
  {
    region: 'Western Europe',
    countries: 'France, Germany, UK, Netherlands, Belgium, Austria, Switzerland',
    highlight: 'Economic core of the continent. Germany alone produces 25% of EU GDP. Switzerland (not in EU) has the highest wealth per adult on Earth. The Netherlands feeds 2nd-most food exports globally from a tiny landmass.',
  },
  {
    region: 'Northern Europe',
    countries: 'Norway, Sweden, Denmark, Finland, Iceland',
    highlight: 'The Nordic model: highest quality of life, strongest social safety nets, most gender-equal societies. Norway\'s sovereign wealth fund ($1.4T) is the world\'s largest — built on oil revenues invested for future generations.',
  },
  {
    region: 'Southern Europe',
    countries: 'Italy, Spain, Portugal, Greece, Malta, Cyprus',
    highlight: 'Mediterranean civilizational cradle. Greece invented democracy, Rome built the legal foundation of the West. Today: tourism-dependent economies, aging populations, periodic debt crises (Greece 2010, Italy ongoing).',
  },
  {
    region: 'Eastern Europe',
    countries: 'Poland, Czech Republic, Romania, Bulgaria, Hungary, Slovakia',
    highlight: 'Post-Soviet transformation: 30 years from planned economies to EU members. Poland\'s GDP grew 800% since 1990. Hungary drifts toward autocracy. Romania and Bulgaria remain EU\'s poorest members.',
  },
  {
    region: 'Balkans & Southeast',
    countries: 'Serbia, Croatia, Bosnia, Albania, North Macedonia, Kosovo, Montenegro',
    highlight: 'The fault line of empires — Ottoman, Habsburg, and Soviet legacies overlap. Yugoslavia dissolved into 7 nations in the 1990s. Several aspire to EU membership but face governance and ethnic challenges.',
  },
]

export default function EuropeDashboard() {
  return (
    <Box>
      <Breadcrumb items={[{ label: 'Continents' }, { label: 'Europe' }]} />
      {/* Page Header */}
      <Box mb={8}>
        <Flex align="center" gap={3} mb={2}>
          <Globe size={28} color="#3182CE" />
          <Heading fontFamily='"Cinzel", serif' fontSize="3xl" fontWeight={700} color="#2D2A24">
            Europe
          </Heading>
        </Flex>
        <Text fontFamily='"Cormorant Garamond", serif' fontSize="lg" color="#524E44" maxW="700px">
          The continent that shaped modernity — for better and worse. Europe invented democracy,
          the printing press, and the scientific method — but also colonialism, industrial warfare,
          and the Holocaust. 44 nations on 10.2M km² with a{' '}
          <Text as="span" fontStyle="italic" fontWeight={600}>shrinking</Text> population.
        </Text>
        <Box h="3px" bg="#3182CE" w="80px" mt={4} />
      </Box>

      {/* Key Stats */}
      <SectionHeading title="Key Indicators" subtitle="Europe at a glance — 44 nations, 750 million people" />
      <SimpleGrid columns={{ base: 2, md: 3 }} gap={4} mb={8}>
        {KEY_STATS.map(s => <StatCard key={s.label} {...s} />)}
      </SimpleGrid>

      {/* Data Tables */}
      <SectionHeading title="Comparative Data" subtitle="European data in global context" />
      <SimpleGrid columns={{ base: 1, lg: 2 }} gap={5} mb={8}>
        <DataTable {...DEMOGRAPHICS_TABLE} />
        <DataTable {...ECONOMIC_TABLE} />
      </SimpleGrid>
      <SimpleGrid columns={{ base: 1, lg: 2 }} gap={5} mb={8}>
        <DataTable {...GOVERNANCE_TABLE} />
        <DataTable {...EU_TABLE} />
      </SimpleGrid>
      <SimpleGrid columns={{ base: 1, lg: 2 }} gap={5} mb={8}>
        <DataTable {...HEALTH_TABLE} />
      </SimpleGrid>

      {/* Hidden Patterns */}
      <SectionHeading title="Hidden Patterns" subtitle="Non-obvious insights from European analysis" />
      <SimpleGrid columns={{ base: 1, md: 2 }} gap={5} mb={8}>
        {HIDDEN_PATTERNS.map(p => <InsightCard key={p.title} {...p} />)}
      </SimpleGrid>

      {/* Regional Highlights */}
      <SectionHeading title="Regional Breakdown" subtitle="5 Europes within Europe" />
      <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={4} mb={8}>
        {REGIONAL_HIGHLIGHTS.map(r => (
          <Box key={r.region} bg="white" border="1px solid" borderColor="#E4E2DC" borderRadius="lg" p={5}>
            <Text fontFamily='"Cinzel", serif' fontSize="lg" fontWeight={700} color="#3182CE">{r.region}</Text>
            <Text fontSize="xs" color="#96770B" mt={1}>{r.countries}</Text>
            <Text fontSize="sm" color="#524E44" mt={3} lineHeight={1.6}>{r.highlight}</Text>
          </Box>
        ))}
      </SimpleGrid>

      {/* Source Attribution */}
      {/* Knowledge Graph Coverage */}
      <SectionHeading
        title="Knowledge Graph Coverage"
        subtitle="2,062 nodes across 45 nations — 6 eras of European history"
      />
      <SimpleGrid columns={{ base: 2, md: 3, lg: 6 }} gap={4} mb={5}>
        <StatCard value="1,144" label="Events" detail="Wars, elections, discoveries" color="#C5963A" />
        <StatCard value="278" label="Movements" detail="Reformation, Enlightenment, Revolutions" color="#6B3FA0" />
        <StatCard value="220" label="Institutions" detail="Empires, parliaments, churches" color="#8B3A3A" />
        <StatCard value="212" label="People" detail="Monarchs, philosophers, scientists" color="#3A7D44" />
        <StatCard value="195" label="Texts" detail="Treaties, constitutions, codes" color="#5A2222" />
        <StatCard value="2,062" label="Total Nodes" detail="Across all 6 eras" color="#D4AF37" />
      </SimpleGrid>
      <DataTable
        title="Top Countries by Knowledge Graph Nodes"
        headers={['Country', 'Event Windows', 'People', 'Institutions', 'Movements', 'Total']}
        rows={[
          ['United Kingdom', '142', '30', '40', '40', '288'],
          ['France', '43', '9', '10', '11', '76'],
          ['Spain', '40', '8', '9', '9', '70'],
          ['Germany', '35', '4', '8', '5', '67'],
          ['Italy', '40', '6', '7', '8', '66'],
        ]}
      />

      {/* Source Attribution */}
      <Box bg="#F5F4F0" borderRadius="lg" p={5} border="1px solid" borderColor="#E4E2DC">
        <Text fontSize="xs" color="#9E9A90" fontWeight={600}>Data Sources</Text>
        <Text fontSize="xs" color="#9E9A90" mt={1}>
          Eurostat, World Bank, IMF, UNDP, Freedom House, IEA, WIPO Global Innovation Index,
          World Happiness Report, UN Population Division. Continent dashboard — skeleton data
          pending full country-level research.
        </Text>
      </Box>
    </Box>
  )
}
