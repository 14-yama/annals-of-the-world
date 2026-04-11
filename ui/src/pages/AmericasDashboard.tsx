import React from 'react'
import { Box, SimpleGrid, Text, Flex, Heading } from '@chakra-ui/react'
import { Globe, Mountain, Wheat, Ship, Users, TrendingUp } from 'lucide-react'
import { StatCard, InsightCard, DataTable, SectionHeading } from '../components/DataCards'
import Breadcrumb from '../components/Breadcrumb'
import { useGlobalCounts } from '../hooks/useGlobalCounts'

/* ── Static data — Americas (skeleton, expanding with research) ── */

const KEY_STATS = [
  { value: '35', label: 'Nations', detail: 'North, Central, South America + Caribbean', color: '#38A169' },
  { value: '1.0B', label: 'Population', detail: '13% of humanity', color: '#D4AF37' },
  { value: '~33%', label: 'Global GDP', detail: 'USA alone is 25% of world GDP', color: '#2F855A' },
  { value: '31.0', label: 'Median Age', detail: 'Younger than Europe, older than Africa', color: '#4A90D9' },
  { value: '1,000+', label: 'Languages', detail: 'Including 600+ indigenous languages', color: '#805AD5' },
  { value: '42.5M', label: 'Land Area (km²)', detail: 'Second largest combined continent', color: '#8B3A3A' },
]

const DEMOGRAPHICS_TABLE = {
  title: 'Americas Demographics',
  headers: ['Metric', 'North America', 'Latin America', 'Global'],
  rows: [
    ['Population', '380M', '660M', '8.1B'],
    ['Median Age', '38.6', '29.5', '30.5'],
    ['Urbanization', '82%', '81%', '56%'],
    ['Fertility Rate', '1.6', '2.0', '2.3'],
    ['Life Expectancy', '78.9 yrs', '75.2 yrs', '73.4 yrs'],
  ],
}

const ECONOMIC_TABLE = {
  title: 'Top Economies of the Americas',
  headers: ['Country', 'GDP (Nominal)', 'GDP Per Capita', 'Highlight'],
  rows: [
    ['United States', '$25.5T', '$76,300', 'Largest economy on Earth'],
    ['Canada', '$2.1T', '$52,700', '2nd-largest country by area'],
    ['Brazil', '$1.9T', '$8,900', 'Largest economy in S. America'],
    ['Mexico', '$1.3T', '$10,800', 'Manufacturing hub, USMCA'],
    ['Argentina', '$640B', '$13,700', 'Chronic inflation, commodity-rich'],
    ['Colombia', '$340B', '$6,600', 'Post-conflict growth'],
  ],
}

const GOVERNANCE_TABLE = {
  title: 'Freedom House Scores — Americas',
  headers: ['Country', 'Score', 'Status'],
  rows: [
    ['Canada', '98', 'Free'],
    ['Uruguay', '97', 'Free'],
    ['Costa Rica', '91', 'Free'],
    ['United States', '83', 'Free'],
    ['Brazil', '73', 'Free'],
    ['Mexico', '60', 'Partly Free'],
    ['Haiti', '32', 'Not Free'],
    ['Venezuela', '14', 'Not Free'],
    ['Cuba', '12', 'Not Free'],
    ['Nicaragua', '11', 'Not Free'],
  ],
}

const HEALTH_TABLE = {
  title: 'Health Indicators — Americas',
  headers: ['Metric', 'North America', 'Latin America', 'Global'],
  rows: [
    ['Life Expectancy', '78.9 yrs', '75.2 yrs', '73.4 yrs'],
    ['Maternal Mortality (per 100k)', '21', '88', '223'],
    ['Infant Mortality (per 1k)', '5.4', '14.0', '27'],
    ['Physicians per 10k', '26', '20', '15'],
    ['Obesity Rate', '36%', '24%', '13%'],
  ],
}

const INDIGENOUS_TABLE = {
  title: 'Pre-Columbian Civilizations',
  headers: ['Civilization', 'Region', 'Peak Period', 'Achievement'],
  rows: [
    ['Maya', 'Mesoamerica', '250–900 CE', 'Writing system, astronomy, zero'],
    ['Aztec', 'Central Mexico', '1325–1521 CE', 'Tenochtitlan: 200k+ population'],
    ['Inca', 'Andes', '1438–1533 CE', 'Road network: 40,000 km, quipu'],
    ['Mississippian', 'N. America', '800–1600 CE', 'Cahokia: 20k+ people'],
    ['Muisca', 'Colombia', '600–1600 CE', 'Origin of El Dorado legend'],
  ],
}

const HIDDEN_PATTERNS = [
  {
    title: 'The Columbian Genocide',
    insight: 'When Columbus arrived in 1492, the Americas had ~50–100 million people. By 1600, 90% were dead — primarily from European diseases (smallpox, measles), but also enslavement and warfare. This is the largest population collapse in recorded history.',
    source: 'Charles Mann, "1491"; Denevan, 1992',
  },
  {
    title: 'The Two Americas',
    insight: 'North America\'s GDP per capita is ~$60,000. Latin America\'s is ~$8,000. The dividing line traces exactly to the colonial powers: Britain\'s colonies (institutions-first) vs Spain/Portugal\'s (extraction-first). 500 years later, the colonial blueprint still determines wealth.',
    source: 'Acemoglu & Robinson, "Why Nations Fail"',
    accent: '#C53030',
  },
  {
    title: 'Brazil: The Sleeping Giant',
    insight: 'Brazil is the 7th-largest economy, has the Amazon (60% of world\'s remaining rainforest), 20% of global freshwater, and more arable land than any country. Yet GDP per capita is lower than Mexico\'s. Brazil has been "the country of the future" for 100 years.',
    source: 'World Bank; Stefan Zweig, "Brazil: A Land of the Future" (1941)',
    accent: '#38A169',
  },
  {
    title: 'Immigration Patterns Mirror Colonial Routes',
    insight: 'The US has 45M immigrants — more than any country in history. But immigration to the Americas follows colonial/economic routes: Mexicans to the US, Brazilians to Portugal, Argentines to Spain. People move along the paths of historical power.',
    source: 'UNDESA International Migration Report, 2024',
    accent: '#4A90D9',
  },
  {
    title: 'The Caribbean Laboratory',
    insight: 'Caribbean islands were the first European colonies (1492), first slave economies, first independence movements (Haiti, 1804). These tiny nations experienced every phase of colonialism in concentrated form — extraction, slavery, independence, neo-colonialism, remittance dependency.',
    source: 'Eric Williams, "Capitalism and Slavery"',
    accent: '#805AD5',
  },
  {
    title: 'Latin America\'s Inequality Crisis',
    insight: 'Latin America is the most unequal region on Earth. Brazil\'s Gini (53), Colombia\'s (51), and Mexico\'s (46) reflect a pattern: colonial-era land distribution was never corrected. The same families that owned land in 1800 still dominate economies today.',
    source: 'World Bank Gini Index; UNDP, 2024',
    accent: '#8B3A3A',
  },
]

const REGIONAL_HIGHLIGHTS = [
  {
    region: 'North America',
    countries: 'United States, Canada, Mexico',
    highlight: 'The US is the world\'s largest economy and military. Canada has more lakes than the rest of the world combined. Mexico is the 15th-largest economy and a bridge between Anglo and Latin America.',
  },
  {
    region: 'Central America',
    countries: 'Guatemala, Honduras, El Salvador, Nicaragua, Costa Rica, Panama, Belize',
    highlight: 'The Northern Triangle (Guatemala, Honduras, El Salvador) drives migration to the US. Costa Rica has no army (abolished 1948) and runs on 99% renewable energy. Panama\'s canal handles 5% of world trade.',
  },
  {
    region: 'Caribbean',
    countries: 'Cuba, Haiti, Jamaica, Trinidad, Dominican Republic, Barbados + others',
    highlight: 'Haiti was the first Black republic (1804) and first successful slave revolution. Cuba remains the last Communist state in the Western hemisphere. Barbados became a republic in 2021, removing the British monarchy.',
  },
  {
    region: 'South America — Andean',
    countries: 'Colombia, Peru, Ecuador, Bolivia, Venezuela',
    highlight: 'Home to the Inca Empire\'s legacy. Peru\'s Machu Picchu draws 1.5M visitors/year. Venezuela has the world\'s largest oil reserves but economic collapse. Bolivia has the world\'s largest lithium deposits.',
  },
  {
    region: 'South America — Southern Cone',
    countries: 'Brazil, Argentina, Chile, Uruguay, Paraguay',
    highlight: 'Brazil is 8.5M km² (5th largest country). Argentina experienced 100%+ annual inflation in 2024. Chile leads Latin America in innovation. Uruguay has universal healthcare and legalized cannabis.',
  },
]

export default function AmericasDashboard() {
  const { byContinent } = useGlobalCounts()
  const americasNodes = (byContinent['North America'] || 0) + (byContinent['South America'] || 0)
  return (
    <Box>
      <Breadcrumb items={[{ label: 'Continents' }, { label: 'Americas' }]} />
      {/* Page Header */}
      <Box mb={8}>
        <Flex align="center" gap={3} mb={2}>
          <Globe size={28} color="#38A169" />
          <Heading fontFamily='"Cinzel", serif' fontSize="3xl" fontWeight={700} color="#2D2A24">
            Americas
          </Heading>
        </Flex>
        <Text fontFamily='"Cormorant Garamond", serif' fontSize="lg" color="#524E44" maxW="700px">
          Two continents, one hemisphere — from the Maya and Inca to the American Revolution and Silicon Valley.
          35 nations shaped by indigenous civilizations, European colonization, African diaspora, and waves of{' '}
          <Text as="span" fontStyle="italic" fontWeight={600}>global immigration</Text>.
        </Text>
        <Box h="3px" bg="#38A169" w="80px" mt={4} />
      </Box>

      {/* Key Stats */}
      <SectionHeading title="Key Indicators" subtitle="The Americas at a glance — 35 nations, 1 billion people" />
      <SimpleGrid columns={{ base: 2, md: 3 }} gap={4} mb={8}>
        {KEY_STATS.map(s => <StatCard key={s.label} {...s} />)}
      </SimpleGrid>

      {/* Data Tables */}
      <SectionHeading title="Comparative Data" subtitle="The Americas in detail" />
      <SimpleGrid columns={{ base: 1, lg: 2 }} gap={5} mb={8}>
        <DataTable {...DEMOGRAPHICS_TABLE} />
        <DataTable {...ECONOMIC_TABLE} />
      </SimpleGrid>
      <SimpleGrid columns={{ base: 1, lg: 2 }} gap={5} mb={8}>
        <DataTable {...GOVERNANCE_TABLE} />
        <DataTable {...INDIGENOUS_TABLE} />
      </SimpleGrid>
      <SimpleGrid columns={{ base: 1, lg: 2 }} gap={5} mb={8}>
        <DataTable {...HEALTH_TABLE} />
      </SimpleGrid>

      {/* Hidden Patterns */}
      <SectionHeading title="Hidden Patterns" subtitle="Non-obvious insights across the Western Hemisphere" />
      <SimpleGrid columns={{ base: 1, md: 2 }} gap={5} mb={8}>
        {HIDDEN_PATTERNS.map(p => <InsightCard key={p.title} {...p} />)}
      </SimpleGrid>

      {/* Regional Highlights */}
      <SectionHeading title="Regional Breakdown" subtitle="5 distinct Americas" />
      <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={4} mb={8}>
        {REGIONAL_HIGHLIGHTS.map(r => (
          <Box key={r.region} bg="white" border="1px solid" borderColor="#E4E2DC" borderRadius="lg" p={5}>
            <Text fontFamily='"Cinzel", serif' fontSize="lg" fontWeight={700} color="#38A169">{r.region}</Text>
            <Text fontSize="xs" color="#96770B" mt={1}>{r.countries}</Text>
            <Text fontSize="sm" color="#524E44" mt={3} lineHeight={1.6}>{r.highlight}</Text>
          </Box>
        ))}
      </SimpleGrid>

      {/* Source Attribution */}
      {/* Knowledge Graph Coverage */}
      <SectionHeading
        title="Knowledge Graph Coverage"
        subtitle={`${americasNodes.toLocaleString()} nodes across 35 nations — 6 eras of American history`}
      />
      <SimpleGrid columns={{ base: 2, md: 3, lg: 6 }} gap={4} mb={5}>
        <StatCard value="1,305" label="Events" detail="Wars, revolutions, discoveries" color="#C5963A" />
        <StatCard value="227" label="Movements" detail="Independence, civil rights, reform" color="#6B3FA0" />
        <StatCard value="132" label="People" detail="Presidents, liberators, activists" color="#3A7D44" />
        <StatCard value="109" label="Texts" detail="Constitutions, treaties, declarations" color="#5A2222" />
        <StatCard value="87" label="Institutions" detail="Empires, republics, organizations" color="#8B3A3A" />
        <StatCard value={americasNodes.toLocaleString()} label="Total Nodes" detail="Across all 6 eras" color="#D4AF37" />
      </SimpleGrid>
      <DataTable
        title="Top Countries by Knowledge Graph Nodes"
        headers={['Country', 'Event Windows', 'People', 'Institutions', 'Movements', 'Total']}
        rows={[
          ['United States', '200', '22', '25', '30', '301'],
          ['Mexico', '55', '8', '7', '9', '83'],
          ['Canada', '45', '7', '6', '7', '69'],
          ['Brazil', '40', '7', '6', '8', '67'],
          ['Peru', '44', '6', '5', '7', '66'],
        ]}
      />

      {/* Source Attribution */}
      <Box bg="#F5F4F0" borderRadius="lg" p={5} border="1px solid" borderColor="#E4E2DC">
        <Text fontSize="xs" color="#9E9A90" fontWeight={600}>Data Sources</Text>
        <Text fontSize="xs" color="#9E9A90" mt={1}>
          World Bank, IMF, UNDP, Freedom House, ECLAC, Inter-American Development Bank, CIA Factbook,
          UNDESA Migration. Skeleton data pending full country-level research.
        </Text>
      </Box>
    </Box>
  )
}
