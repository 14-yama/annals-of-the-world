import React from 'react'
import { Box, SimpleGrid, Text, Flex, Heading } from '@chakra-ui/react'
import { Globe, Waves, Sun, TreePine, Compass, Anchor } from 'lucide-react'
import { StatCard, InsightCard, DataTable, SectionHeading } from '../components/DataCards'
import Breadcrumb from '../components/Breadcrumb'

/* ── Static data — Oceania (skeleton, expanding with research) ── */

const KEY_STATS = [
  { value: '14', label: 'Nations', detail: 'Plus numerous territories and dependencies', color: '#38B2AC' },
  { value: '45M', label: 'Population', detail: '0.5% of humanity', color: '#D4AF37' },
  { value: '65,000', label: 'Years', detail: 'Aboriginal Australians — longest continuous culture', color: '#8B3A3A' },
  { value: '25,000+', label: 'Islands', detail: 'Scattered across the vast Pacific Ocean', color: '#4A90D9' },
  { value: '1,300+', label: 'Languages', detail: 'Papua New Guinea alone has 840+', color: '#805AD5' },
  { value: '80%', label: 'Unique Species', detail: 'Australian species found nowhere else', color: '#38A169' },
]

const DEMOGRAPHICS_TABLE = {
  title: 'Oceania Demographics',
  headers: ['Metric', 'Australia/NZ', 'Pacific Islands', 'Global'],
  rows: [
    ['Population', '31M', '14M', '8.1B'],
    ['Median Age', '37.5', '23.0', '30.5'],
    ['Urbanization', '87%', '35%', '56%'],
    ['Life Expectancy', '83.0 yrs', '65–72 yrs', '73.4 yrs'],
    ['GDP Per Capita', '$55,000+', '$2,000–$5,000', '$12,700'],
  ],
}

const ECONOMIC_TABLE = {
  title: 'Economies of Oceania',
  headers: ['Country', 'GDP (Nominal)', 'GDP Per Capita', 'Key Sector'],
  rows: [
    ['Australia', '$1.7T', '$65,100', 'Mining, finance, services'],
    ['New Zealand', '$250B', '$48,800', 'Agriculture, tourism, film'],
    ['Papua New Guinea', '$31B', '$3,000', 'Mining, oil, palm oil'],
    ['Fiji', '$5B', '$5,500', 'Tourism, sugar, remittances'],
    ['Guam (US)', '$6B', '$36,000', 'US military, tourism'],
    ['New Caledonia (FR)', '$10B', '$37,000', 'Nickel mining (10% global)'],
  ],
}

const ENVIRONMENTAL_TABLE = {
  title: 'Climate & Environmental Vulnerability',
  headers: ['Threat', 'Impact', 'Most Affected'],
  rows: [
    ['Sea Level Rise', '1m rise = 6 nations underwater', 'Tuvalu, Kiribati, Marshall Islands'],
    ['Coral Bleaching', 'Great Barrier Reef: 50% lost', 'Australia, Fiji, Palau'],
    ['Cyclones', 'Increasing intensity & frequency', 'Vanuatu, Fiji, Tonga'],
    ['Ocean Acidification', 'Threatens fisheries & food security', 'All Pacific nations'],
    ['Biodiversity Loss', 'Highest extinction rate globally', 'Australia, New Zealand, Hawaii'],
  ],
}

const NAVIGATION_TABLE = {
  title: 'Pacific Navigation — The Greatest Maritime Achievement',
  headers: ['Feat', 'Detail'],
  rows: [
    ['Distance', 'Polynesian navigators sailed 16,000+ km across open ocean'],
    ['Method', 'Star navigation, wave patterns, bird migration observation'],
    ['Period', '1500 BCE – 1200 CE'],
    ['Vessels', 'Double-hulled canoes (waka hourua) up to 30m long'],
    ['Scope', 'Colonized every habitable island in the Pacific triangle'],
  ],
}

const HIDDEN_PATTERNS = [
  {
    title: 'The Language Supercontinent',
    insight: 'Papua New Guinea (10M people) has 840+ languages — 12% of all languages on Earth. More linguistic diversity than all of Europe, all of the Americas, and all of Africa combined. Most have fewer than 1,000 speakers and are disappearing.',
    source: 'Ethnologue, 24th edition',
  },
  {
    title: 'Climate Canaries',
    insight: 'Pacific island nations like Tuvalu (highest point: 4.6m), Kiribati, and the Marshall Islands face literal extinction from sea level rise. These nations contribute 0.03% of global emissions but will be the first to disappear. Tuvalu has already purchased land in Fiji as a backup.',
    source: 'IPCC AR6; Pacific Islands Forum',
    accent: '#C53030',
  },
  {
    title: 'Aboriginal Astronomical Knowledge',
    insight: 'Aboriginal Australians developed sophisticated astronomical knowledge systems 35,000+ years before Galileo. They identified planets, predicted eclipses, and used stellar navigation. The Yolngu people mapped tidal patterns to star movements. This is the oldest scientific tradition on Earth.',
    source: 'Duane Hamacher, "First Astronomers" (2022)',
    accent: '#8B3A3A',
  },
  {
    title: 'The ANZUS Paradox',
    insight: 'Australia is geographically in Asia but culturally aligned with the West. It\'s the only continent-nation in the world, with 86% of its population in just 5 cities on the coast. 90% of the interior (the Outback) is effectively uninhabited — making Australia the emptiest populated continent.',
    source: 'ABS Census, 2021',
    accent: '#4A90D9',
  },
  {
    title: 'New Zealand\'s Governance Innovation',
    insight: 'New Zealand was: first country to give women the vote (1893), first to introduce the 8-hour workday, first to have a transgender MP, and gave legal personhood to a river (Whanganui, 2017). It consistently ranks in the top 3 globally for "least corrupt" and "most free."',
    source: 'Transparency International; Freedom House',
    accent: '#38A169',
  },
  {
    title: 'Pacific Geopolitics Heating Up',
    insight: 'China signed a security pact with Solomon Islands in 2022 — the first of its kind in the Pacific. The US, Australia, and France are scrambling to maintain influence. Tiny Pacific nations are now the frontline of US-China great power competition, just as they were in WWII.',
    source: 'IISS Strategic Survey; Pacific Islands Forum communiqués',
    accent: '#805AD5',
  },
]

const REGIONAL_HIGHLIGHTS = [
  {
    region: 'Australia',
    countries: 'Australia (1 nation, 6 states, 2 territories)',
    highlight: 'The world\'s smallest continent and largest island. Aboriginal Australians have 65,000 years of continuous culture. Today: $1.7T economy, 26M people, 80% live within 50km of the coast. World\'s largest exporter of iron ore, coal, and LNG.',
  },
  {
    region: 'Melanesia',
    countries: 'Papua New Guinea, Fiji, Solomon Islands, Vanuatu, New Caledonia',
    highlight: 'The most culturally diverse region on Earth. PNG alone has 840+ languages and 1,000+ tribal groups. Fiji is the regional hub. Vanuatu is ranked world\'s most at-risk country for natural disasters. New Caledonia holds 10% of global nickel reserves.',
  },
  {
    region: 'Polynesia',
    countries: 'New Zealand, Samoa, Tonga, Tuvalu, Cook Islands, French Polynesia',
    highlight: 'Masters of ocean navigation — Polynesian sailors colonized the Pacific triangle (Hawaii-Easter Island-New Zealand) using only stars and waves. The Māori of New Zealand developed complex governance (iwi) and warfare (haka).',
  },
  {
    region: 'Micronesia',
    countries: 'FSM, Palau, Marshall Islands, Kiribati, Nauru, Guam',
    highlight: 'Tiny nations with outsized geopolitical significance. The Marshall Islands was the US nuclear testing ground (67 tests, 1946-1958). Palau banned commercial fishing in 80% of its waters. Nauru was the world\'s richest country per capita (phosphate) — now one of the poorest.',
  },
]

export default function OceaniaDashboard() {
  return (
    <Box>
      <Breadcrumb items={[{ label: 'Continents' }, { label: 'Oceania' }]} />
      {/* Page Header */}
      <Box mb={8}>
        <Flex align="center" gap={3} mb={2}>
          <Globe size={28} color="#38B2AC" />
          <Heading fontFamily='"Cinzel", serif' fontSize="3xl" fontWeight={700} color="#2D2A24">
            Oceania
          </Heading>
        </Flex>
        <Text fontFamily='"Cormorant Garamond", serif' fontSize="lg" color="#524E44" maxW="700px">
          The world's last frontier — where the oldest continuous civilization (65,000 years)
          meets the planet's youngest nations. 14 countries across 25,000+ islands, home to{' '}
          <Text as="span" fontStyle="italic" fontWeight={600}>1,300 languages</Text> and the
          greatest maritime navigators in human history.
        </Text>
        <Box h="3px" bg="#38B2AC" w="80px" mt={4} />
      </Box>

      {/* Key Stats */}
      <SectionHeading title="Key Indicators" subtitle="Oceania at a glance — 14 nations, 45 million people" />
      <SimpleGrid columns={{ base: 2, md: 3 }} gap={4} mb={8}>
        {KEY_STATS.map(s => <StatCard key={s.label} {...s} />)}
      </SimpleGrid>

      {/* Data Tables */}
      <SectionHeading title="Comparative Data" subtitle="The vast Pacific in numbers" />
      <SimpleGrid columns={{ base: 1, lg: 2 }} gap={5} mb={8}>
        <DataTable {...DEMOGRAPHICS_TABLE} />
        <DataTable {...ECONOMIC_TABLE} />
      </SimpleGrid>
      <SimpleGrid columns={{ base: 1, lg: 2 }} gap={5} mb={8}>
        <DataTable {...ENVIRONMENTAL_TABLE} />
        <DataTable {...NAVIGATION_TABLE} />
      </SimpleGrid>

      {/* Hidden Patterns */}
      <SectionHeading title="Hidden Patterns" subtitle="Non-obvious insights from Oceania analysis" />
      <SimpleGrid columns={{ base: 1, md: 2 }} gap={5} mb={8}>
        {HIDDEN_PATTERNS.map(p => <InsightCard key={p.title} {...p} />)}
      </SimpleGrid>

      {/* Regional Highlights */}
      <SectionHeading title="Regional Breakdown" subtitle="4 distinct Pacific worlds" />
      <SimpleGrid columns={{ base: 1, md: 2 }} gap={4} mb={8}>
        {REGIONAL_HIGHLIGHTS.map(r => (
          <Box key={r.region} bg="white" border="1px solid" borderColor="#E4E2DC" borderRadius="lg" p={5}>
            <Text fontFamily='"Cinzel", serif' fontSize="lg" fontWeight={700} color="#38B2AC">{r.region}</Text>
            <Text fontSize="xs" color="#96770B" mt={1}>{r.countries}</Text>
            <Text fontSize="sm" color="#524E44" mt={3} lineHeight={1.6}>{r.highlight}</Text>
          </Box>
        ))}
      </SimpleGrid>

      {/* Source Attribution */}
      <Box bg="#F5F4F0" borderRadius="lg" p={5} border="1px solid" borderColor="#E4E2DC">
        <Text fontSize="xs" color="#9E9A90" fontWeight={600}>Data Sources</Text>
        <Text fontSize="xs" color="#9E9A90" mt={1}>
          ABS, Stats NZ, Pacific Islands Forum, IPCC AR6, World Bank, UNDP, Freedom House,
          Ethnologue, IISS, CIA Factbook. Skeleton data pending full country-level research.
        </Text>
      </Box>
    </Box>
  )
}
