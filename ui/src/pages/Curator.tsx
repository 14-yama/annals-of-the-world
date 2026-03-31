/* ─── Curator Page — Annals of the World ─── */
/* Personal chronicle: the magnitude of the project, comparison to Ussher, academic equivalency */
import React from 'react'
import { Box, Flex, Heading, Text, SimpleGrid } from '@chakra-ui/react'
import { SectionHeading, StatCard, InsightCard } from '../components/DataCards'
import Breadcrumb from '../components/Breadcrumb'
import {
  BookOpen, Brain, Globe2, Clock, Database, Code2, Network,
  GraduationCap, Scroll, Target, Layers, Microscope,
  BarChart3, Users, Map, Cpu, TrendingUp, CheckCircle2,
} from 'lucide-react'

/* ─── Constants ─── */
const USSHER_STATS = [
  { value: '~1,600', label: 'Manuscripts Consulted', icon: Scroll, color: '#8B3A3A' },
  { value: '10+', label: 'Languages Mastered', icon: BookOpen, color: '#96770B' },
  { value: '40', label: 'Years of Scholarship', icon: Clock, color: '#645E52' },
  { value: '1', label: 'Output: Annales (1650)', icon: Database, color: '#D4AF37' },
  { value: '~4004 BCE', label: 'Temporal Scope Start', icon: Clock, color: '#4A310D' },
  { value: 'Biblical', label: 'Primary Framework', icon: Layers, color: '#9E9A90' },
]

const PROJECT_STATS = [
  { value: '199', label: 'Countries Profiled', icon: Globe2, color: '#4A90D9' },
  { value: '1,000,000', label: 'Target Knowledge Nodes', icon: Network, color: '#6B3FA0' },
  { value: '10,580', label: 'Actors in Annals Catalog', icon: CheckCircle2, color: '#2F855A' },
  { value: '10+', label: 'Interpretive Frameworks', icon: Layers, color: '#D4AF37' },
  { value: '6', label: 'Canonical Eras', icon: BarChart3, color: '#C53030' },
  { value: '127', label: 'Weapons Catalogued', icon: Target, color: '#8B3A3A' },
  { value: '67', label: 'Ideas Catalogued', icon: Brain, color: '#6B3FA0' },
  { value: '72,000', label: 'Years of History Modeled', icon: Clock, color: '#DD6B20' },
]

const ACADEMIC_EQUIVALENCE = [
  {
    discipline: 'Data Science & Ontology Design',
    level: 'PhD-equivalent',
    detail: 'Building a million-node Neo4j knowledge graph with Pydantic models, Cypher queries, 10 interpretive frameworks, and 11 core node labels is a dissertation-level ontology engineering project.',
    icon: Database,
    color: '#4A90D9',
  },
  {
    discipline: 'Digital Humanities',
    level: 'PhD-equivalent',
    detail: 'Digitizing 72,000 years of history across 199 countries with scholarly citations, evidence chains, and curator workflows parallels the most ambitious digital humanities initiatives at Stanford, Oxford, or the Max Planck Institute.',
    icon: BookOpen,
    color: '#6B3FA0',
  },
  {
    discipline: 'Computational History / Chronology',
    level: 'PhD-equivalent',
    detail: 'Formalizing temporal relationships (OCCURS_DURING, CAUSES, TRANSFORMS) with evidence-backed edges and active-voice governance directly extends Ussher\'s chronological methodology using computational tools.',
    icon: Clock,
    color: '#D4AF37',
  },
  {
    discipline: 'Full-Stack Software Engineering',
    level: 'Senior-level portfolio',
    detail: 'React 18 + TypeScript + Vite + Chakra UI frontend, Python + Neo4j + Pydantic backend, D3.js visualizations, GitHub CI/CD — a production-grade application demonstrating T-shaped expertise.',
    icon: Code2,
    color: '#2F855A',
  },
  {
    discipline: 'Geographic Information Systems',
    level: 'Masters-equivalent',
    detail: 'Choropleth maps, geo-registries with 1,500+ places, historical border tracking, and multi-layer geospatial visualization across all inhabited continents.',
    icon: Map,
    color: '#C53030',
  },
  {
    discipline: 'Comparative Religion & Philosophy',
    level: 'Masters-equivalent',
    detail: 'Mapping doctrinal development, textual transmission, and ritual standardization across Christianity, Islam, Buddhism, Hinduism, Judaism, and indigenous traditions with framework-based analysis.',
    icon: Scroll,
    color: '#8B3A3A',
  },
]

const TEN_YEAR_MILESTONES = [
  { years: '1–2', title: 'Foundation', nodes: '50,000', detail: 'Schema design, ontology, frameworks, core graph, curator workflow, MVP frontend' },
  { years: '3–4', title: 'Continental Depth', nodes: '200,000', detail: 'Full coverage of Africa, Asia, Europe — all countries with event windows, evidence, and relationships' },
  { years: '5–6', title: 'Global Completion', nodes: '500,000', detail: 'Americas, Oceania complete. Trade routes, migrations, linguistic evolution fully modeled' },
  { years: '7–8', title: 'Academic Integration', nodes: '750,000', detail: 'Wikidata integration, scholarly API, peer review, open dataset publications' },
  { years: '9–10', title: 'Million-Node Graph', nodes: '1,000,000', detail: 'Complete knowledge graph with real-time querying, advanced visualizations, and community contributions' },
]

/* ─── Live Node Census ─── */
const TARGET_NODES = 1_000_000

const NODE_CENSUS_BY_TYPE = [
  { label: 'Event',       count: 5754,  color: '#C53030' },
  { label: 'Person',      count: 2002,  color: '#4A90D9' },
  { label: 'Movement',    count: 1092,  color: '#D4AF37' },
  { label: 'Institution', count: 659,   color: '#2F855A' },
  { label: 'Text',        count: 621,   color: '#8B3A3A' },
  { label: 'Idea',        count: 318,   color: '#6B3FA0' },
  { label: 'Place',       count: 93,    color: '#DD6B20' },
  { label: 'Evidence',    count: 41,    color: '#718096' },
]

const NODE_CENSUS_SOURCES = [
  { source: 'Geo-Registry (199 countries × 6 eras)',    count: 9380, color: '#2F855A',
    detail: 'Auto-generated from country index files. Each entity enriched with causes, effects, relationships, frameworks, and places. EventWindow (5,467), Person (1,858), Movement (935), Institution (626), Text (441), Idea (53).' },
  { source: 'Topic Catalog (12 topic collections)',      count: 622, color: '#6B3FA0',
    detail: 'Weapons (127), Tribes (66), Languages (65), Transportation (50), Architecture (48), Agriculture (48), Medicine (46), Clothing (45), Navigation (42), Marriage (30), Customs (28), Punishment (27).' },
  { source: 'Hand-Curated Era & Special Catalogs',       count: 455, color: '#4A90D9',
    detail: 'Prehistoric (15), Classical (48), Medieval (37), Early Modern (38), Modern (43), Contemporary (35), Biblical (97), Reformation (23), Division Enrichment (119).' },
  { source: 'Corpus Catalog (13 scholarly collections)',  count: 176, color: '#8B3A3A',
    detail: 'Mesopotamian (24), Egyptian (19), Judaic-Rabbinic (8), Graeco-Roman (15), Canon Law (4), Iran & Central Asia (21), South & SE Asia (17), East Asia (15), Africa (8), Americas (7), Europe (28), Science & Tech (10).' },
]

/* Annals Catalog total: 10,633 pre-dedup → 10,580 unique actors across 7 eras (source of truth) */
const TOTAL_NODES = 10_580
const PROGRESS_PCT = ((TOTAL_NODES / TARGET_NODES) * 100).toFixed(2)

export default function Curator() {
  return (
    <Box>
      <Breadcrumb items={[{ label: 'Curator' }]} />
      {/* ─── Hero ─── */}
      <Box mb={10} textAlign="center" py={8} bg="linear-gradient(135deg, #FAFAF8 0%, #FDF8ED 50%, #E8F0FE 100%)"
        borderRadius="2xl" border="1px solid #E4E2DC">
        <Heading fontFamily='"Cinzel", serif' fontSize={{ base: '2xl', md: '4xl' }} fontWeight={700}
          color="#2D2A24" mb={3}>
          The Curator's Chronicle
        </Heading>
        <Text fontFamily='"Cormorant Garamond", serif' fontSize={{ base: 'lg', md: 'xl' }} color="#524E44"
          maxW="700px" mx="auto" lineHeight={1.8} mb={4}>
          Continuing the work Archbishop James Ussher began in 1650 —<br />
          with 21st-century tools, global scope, and computational power.
        </Text>
        <Flex justify="center" gap={6} flexWrap="wrap">
          <Flex align="center" gap={2}>
            <Brain size={18} color="#D4AF37" />
            <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#9E9A90">
              AI-AUGMENTED RESEARCH
            </Text>
          </Flex>
          <Flex align="center" gap={2}>
            <Database size={18} color="#4A90D9" />
            <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#9E9A90">
              NEO4J KNOWLEDGE GRAPH
            </Text>
          </Flex>
          <Flex align="center" gap={2}>
            <Target size={18} color="#6B3FA0" />
            <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#9E9A90">
              10-YEAR COMMITMENT
            </Text>
          </Flex>
        </Flex>
      </Box>

      {/* ─── Node Progress Dashboard ─── */}
      <Box mb={10}>
        <SectionHeading
          title="Progress Toward 1,000,000 Nodes"
          subtitle="Live census of every documented node across all data sources"
        />

        {/* Grand Total Bar */}
        <Box mt={6} p={6} bg="#082340" borderRadius="xl" mb={6}>
          <Flex justify="space-between" align="flex-end" mb={3}>
            <Box>
              <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#4A90D9" textTransform="uppercase" mb={1}>
                Total Documented Nodes
              </Text>
              <Heading fontFamily='"Cinzel", serif' fontSize={{ base: '3xl', md: '5xl' }} color="#D4AF37">
                {TOTAL_NODES.toLocaleString()}
              </Heading>
            </Box>
            <Box textAlign="right">
              <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#E8F0FE">
                of 1,000,000 target
              </Text>
              <Text fontFamily='"Cinzel", serif' fontSize="2xl" color="#D4AF37">
                {PROGRESS_PCT}%
              </Text>
            </Box>
          </Flex>
          {/* Progress bar */}
          <Box w="100%" h="12px" bg="#1A3A5C" borderRadius="full" overflow="hidden">
            <Box h="100%" w={`${Math.max(parseFloat(PROGRESS_PCT), 0.5)}%`} bg="linear-gradient(90deg, #D4AF37, #4A90D9)"
              borderRadius="full" transition="width 0.5s" />
          </Box>
          <Flex justify="space-between" mt={2}>
            <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096">0</Text>
            <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096">250K</Text>
            <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096">500K</Text>
            <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096">750K</Text>
            <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096">1M</Text>
          </Flex>
        </Box>

        {/* By Source */}
        <SimpleGrid columns={{ base: 1, md: 2 }} gap={4} mb={6}>
          {NODE_CENSUS_SOURCES.map(s => (
            <Box key={s.source} p={5} bg="#FDFAF5" border="1px solid #E4E2DC" borderRadius="xl"
              borderLeft="4px solid" borderLeftColor={s.color}>
              <Flex justify="space-between" align="center" mb={2}>
                <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#2D2A24">
                  {s.source}
                </Text>
                <Text fontFamily='"Cinzel", serif' fontSize="xl" fontWeight={700} color={s.color}>
                  {s.count.toLocaleString()}
                </Text>
              </Flex>
              <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#524E44" lineHeight={1.6}>
                {s.detail}
              </Text>
              {/* Mini bar */}
              <Box mt={2} w="100%" h="4px" bg="#E4E2DC" borderRadius="full" overflow="hidden">
                <Box h="100%" w={`${(s.count / TOTAL_NODES) * 100}%`} bg={s.color} borderRadius="full" />
              </Box>
            </Box>
          ))}
        </SimpleGrid>

        {/* By Node Type */}
        <Box p={5} bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="xl">
          <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#2D2A24" mb={4}>
            Nodes by Schema Label
          </Text>
          {NODE_CENSUS_BY_TYPE.map(t => (
            <Flex key={t.label} align="center" gap={3} mb={2}>
              <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color={t.color}
                minW="90px" fontWeight={600}>
                {t.label}
              </Text>
              <Box flex={1} h="16px" bg="#E4E2DC" borderRadius="md" overflow="hidden">
                <Box h="100%" bg={t.color} w={`${(t.count / 6000) * 100}%`}
                  borderRadius="md" transition="width 0.3s" />
              </Box>
              <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#524E44" minW="45px" textAlign="right">
                {t.count.toLocaleString()}
              </Text>
            </Flex>
          ))}
          <Text fontSize="10px" fontFamily='"JetBrains Mono", monospace' color="#718096" mt={3} textAlign="right">
            Annals Catalog — 10,580 unique actors across 7 eras (source of truth)
          </Text>
        </Box>
      </Box>

      {/* ─── Ussher vs Project Comparison ─── */}
      <Box mb={10}>
        <SectionHeading
          title="Standing on the Shoulders of Giants"
          subtitle="Archbishop Ussher's achievement — and how this project extends it"
        />
        <SimpleGrid columns={{ base: 1, lg: 2 }} gap={6} mt={6}>
          {/* Ussher Column */}
          <Box>
            <Flex align="center" gap={2} mb={4}>
              <Scroll size={22} color="#8B3A3A" />
              <Heading fontFamily='"Cormorant Garamond", serif' fontSize="xl" fontWeight={700} color="#8B3A3A">
                James Ussher (1581–1656)
              </Heading>
            </Flex>
            <Box bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="xl" p={5} mb={4}>
              <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" lineHeight={1.8}>
                Archbishop of Armagh, Primate of All Ireland, and one of the most learned scholars of the 17th century.
                Ussher spent <strong>40 years</strong> correlating biblical genealogies, Babylonian king-lists, Roman consular dates,
                and astronomical references to produce <em>Annales Veteris Testamenti</em> (1650) — a continuous chronology
                from Creation to 70 CE. He mastered Hebrew, Greek, Latin, Chaldean, Syriac, Arabic, Persian, Ethiopic,
                and Armenian to cross-reference primary sources directly.
              </Text>
            </Box>
            <SimpleGrid columns={2} gap={3}>
              {USSHER_STATS.map(s => (
                <StatCard key={s.label} value={s.value} label={s.label} color={s.color} />
              ))}
            </SimpleGrid>
          </Box>

          {/* Project Column */}
          <Box>
            <Flex align="center" gap={2} mb={4}>
              <Network size={22} color="#4A90D9" />
              <Heading fontFamily='"Cormorant Garamond", serif' fontSize="xl" fontWeight={700} color="#4A90D9">
                Annals of the World (2024–2034)
              </Heading>
            </Flex>
            <Box bg="#E8F0FE" border="1px solid #B8D4FE" borderRadius="xl" p={5} mb={4}>
              <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#2D2A24" lineHeight={1.8}>
                This project continues Ussher's vision using <strong>AI-augmented research, graph databases, and interactive
                visualization</strong>. Where Ussher worked alone with quill and parchment, we use Neo4j, Python, TypeScript,
                D3.js, and large language models. Where he covered Creation to 70 CE through a biblical lens, we cover
                <strong> 72,000 years</strong> across <strong>199 countries</strong> through <strong>10 interpretive frameworks</strong>.
                The ambition is not to replace Ussher — it is to honor his methodology by extending it with tools he could never have imagined.
              </Text>
            </Box>
            <SimpleGrid columns={2} gap={3}>
              {PROJECT_STATS.map(s => (
                <StatCard key={s.label} value={s.value} label={s.label} color={s.color} />
              ))}
            </SimpleGrid>
          </Box>
        </SimpleGrid>
      </Box>

      {/* ─── Scale Comparison ─── */}
      <Box mb={10} bg="#FDF8ED" border="1px solid #D4AF37" borderRadius="xl" p={6}>
        <SectionHeading
          title="The Magnitude Comparison"
          subtitle="Quantifying the difference between 17th-century and 21st-century chronology"
        />
        <SimpleGrid columns={{ base: 1, md: 3 }} gap={6} mt={6}>
          <Box p={5} bg="white" borderRadius="lg" border="1px solid #E4E2DC">
            <Heading fontFamily='"Cinzel", serif' fontSize="3xl" color="#D4AF37" mb={2}>12×</Heading>
            <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#2D2A24" mb={1}>
              Temporal Coverage
            </Text>
            <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#524E44" lineHeight={1.6}>
              Ussher: ~6,000 years (4004 BCE–70 CE). This project: 72,000 years (70,000 BCE–Present).
              We model 12× the chronological span, including Prehistory and the Modern era.
            </Text>
          </Box>
          <Box p={5} bg="white" borderRadius="lg" border="1px solid #E4E2DC">
            <Heading fontFamily='"Cinzel", serif' fontSize="3xl" color="#4A90D9" mb={2}>625×</Heading>
            <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#2D2A24" mb={1}>
              Knowledge Density
            </Text>
            <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#524E44" lineHeight={1.6}>
              Ussher: ~1,600 referenced manuscripts → single narrative. This project: 1,000,000 planned nodes ×
              multiple relationships = a graph 625× denser than Ussher's citation network.
            </Text>
          </Box>
          <Box p={5} bg="white" borderRadius="lg" border="1px solid #E4E2DC">
            <Heading fontFamily='"Cinzel", serif' fontSize="3xl" color="#6B3FA0" mb={2}>10×</Heading>
            <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#2D2A24" mb={1}>
              Interpretive Breadth
            </Text>
            <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#524E44" lineHeight={1.6}>
              Ussher: 1 framework (Biblical chronology). This project: 10 frameworks including Cause & Effect,
              Cultural Diffusion, Doctrine Development, Geopolitical Linkage, and Temporal Linkage.
            </Text>
          </Box>
        </SimpleGrid>
      </Box>

      {/* ─── Academic Equivalency ─── */}
      <Box mb={10}>
        <SectionHeading
          title="Academic Equivalency Analysis"
          subtitle="What a 10-year commitment to this project represents in academic terms"
        />
        <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" lineHeight={1.8} mt={2} mb={6} maxW="800px">
          This is not a hobby project. Building a million-node knowledge graph that models all of documented human history
          across 199 countries — with scholarly citations, 10 interpretive frameworks, a production frontend, and a Neo4j
          backend — is a body of work that spans multiple academic disciplines. Here is what this project represents
          if submitted for formal evaluation:
        </Text>
        <SimpleGrid columns={{ base: 1, md: 2 }} gap={5}>
          {ACADEMIC_EQUIVALENCE.map(a => {
            const Icon = a.icon
            return (
              <Box key={a.discipline} p={6} bg="#FDFAF5" border="1px solid #E4E2DC" borderRadius="xl"
                borderLeft="4px solid" borderLeftColor={a.color}>
                <Flex align="center" gap={3} mb={3}>
                  <Box p={2} bg={`${a.color}15`} borderRadius="lg">
                    <Icon size={20} color={a.color} />
                  </Box>
                  <Box>
                    <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#2D2A24">
                      {a.discipline}
                    </Text>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="11px" fontWeight={600}
                      color={a.color} textTransform="uppercase">
                      {a.level}
                    </Text>
                  </Box>
                </Flex>
                <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" lineHeight={1.7}>
                  {a.detail}
                </Text>
              </Box>
            )
          })}
        </SimpleGrid>
        <Box mt={6} p={5} bg="#082340" borderRadius="xl" textAlign="center">
          <Heading fontFamily='"Cinzel", serif' fontSize="2xl" color="#D4AF37" mb={2}>
            Cumulative Equivalent
          </Heading>
          <Text fontFamily='"Inter", sans-serif' fontSize="md" color="#E8F0FE" lineHeight={1.8}>
            3 PhD-equivalents + 2 Masters-equivalents + Senior Engineering Portfolio
          </Text>
          <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#4A90D9" mt={2}>
            ≈ 15–20 years of formal academic work compressed into a 10-year independent research program
          </Text>
        </Box>
      </Box>

      {/* ─── 10-Year Roadmap ─── */}
      <Box mb={10}>
        <SectionHeading
          title="The 10-Year Arc"
          subtitle="From schema to a million-node knowledge graph"
        />
        <Box mt={6}>
          {TEN_YEAR_MILESTONES.map((m, i) => (
            <Flex key={m.years} gap={4} mb={i < TEN_YEAR_MILESTONES.length - 1 ? 0 : undefined}>
              {/* Timeline track */}
              <Flex direction="column" align="center" minW="50px">
                <Box w="12px" h="12px" borderRadius="full" bg={i === 0 ? '#D4AF37' : '#E4E2DC'}
                  border="2px solid" borderColor={i === 0 ? '#D4AF37' : '#D6D3CC'} zIndex={1} />
                {i < TEN_YEAR_MILESTONES.length - 1 && (
                  <Box w="2px" flex={1} bg="#E4E2DC" minH="60px" />
                )}
              </Flex>
              {/* Content */}
              <Box pb={6} flex={1}>
                <Flex align="center" gap={3} mb={1}>
                  <Text fontFamily='"JetBrains Mono", monospace' fontSize="sm" fontWeight={700}
                    color="#D4AF37" bg="#FDF8ED" px={2} py={0.5} borderRadius="md">
                    Years {m.years}
                  </Text>
                  <Heading fontFamily='"Cormorant Garamond", serif' fontSize="lg" fontWeight={700} color="#2D2A24">
                    {m.title}
                  </Heading>
                </Flex>
                <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" lineHeight={1.7}>
                  {m.detail}
                </Text>
                <Text fontFamily='"JetBrains Mono", monospace' fontSize="11px" color="#9E9A90" mt={1}>
                  Target: {m.nodes} nodes
                </Text>
              </Box>
            </Flex>
          ))}
        </Box>
      </Box>

      {/* ─── Knowledge Consolidation ─── */}
      <Box mb={10}>
        <SectionHeading
          title="Knowledge Consolidated"
          subtitle="What the curator will have mastered upon completion"
        />
        <SimpleGrid columns={{ base: 2, md: 3, lg: 4 }} gap={4} mt={6}>
          {[
            { label: 'Neo4j / Cypher', cat: 'Technology' },
            { label: 'Python / Pydantic', cat: 'Technology' },
            { label: 'React / TypeScript', cat: 'Technology' },
            { label: 'D3.js Visualization', cat: 'Technology' },
            { label: 'Graph Theory', cat: 'Data Science' },
            { label: 'Ontology Engineering', cat: 'Data Science' },
            { label: 'Temporal Modeling', cat: 'Data Science' },
            { label: 'Geospatial Analysis', cat: 'Data Science' },
            { label: 'Ancient History', cat: 'Humanities' },
            { label: 'Medieval Studies', cat: 'Humanities' },
            { label: 'Modern World History', cat: 'Humanities' },
            { label: 'Comparative Religion', cat: 'Humanities' },
            { label: 'Philosophy of History', cat: 'Humanities' },
            { label: 'Historical Linguistics', cat: 'Humanities' },
            { label: 'Scholarly Citation', cat: 'Research' },
            { label: 'Data Governance', cat: 'Research' },
          ].map(k => (
            <Box key={k.label} p={3} bg="#FDFAF5" border="1px solid #E4E2DC" borderRadius="lg" textAlign="center">
              <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#9E9A90" textTransform="uppercase">
                {k.cat}
              </Text>
              <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={600} color="#2D2A24" mt={1}>
                {k.label}
              </Text>
            </Box>
          ))}
        </SimpleGrid>
      </Box>

      {/* ─── Closing Statement ─── */}
      <Box bg="#082340" borderRadius="2xl" p={8} textAlign="center" mb={8}>
        <Heading fontFamily='"Cinzel", serif' fontSize={{ base: 'xl', md: '2xl' }} color="#D4AF37" mb={4}>
          "History is not the past. It is the present.<br />
          We carry it within us. We are our history."
        </Heading>
        <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#E8F0FE" mb={4} lineHeight={1.8} maxW="600px" mx="auto">
          James Baldwin understood that history isn't an archive — it's an operating system.
          This project is an attempt to read that code, to trace every thread, and to honor
          the architects of yesterday by building something worthy of tomorrow.
        </Text>
        <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#4A90D9">
          Annals of the World · A 10-Year Research Program · CC0 Public Domain
        </Text>
      </Box>
    </Box>
  )
}
