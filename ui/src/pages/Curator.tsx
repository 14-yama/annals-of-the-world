/* ─── Curator Page — Annals of the World ─── */
/* Personal chronicle: the magnitude of the project, comparison to Ussher, academic equivalency */
import React from 'react'
import { Box, Flex, Heading, Text, SimpleGrid, Spinner } from '@chakra-ui/react'
import { SectionHeading, StatCard } from '../components/DataCards'
import Breadcrumb from '../components/Breadcrumb'
import { useGlobalCounts } from '../hooks/useGlobalCounts'
import {
  BookOpen, Brain, Globe2, Clock, Database, Code2, Network,
  GraduationCap, Scroll, Target, Layers, Microscope,
  BarChart3, Map, Cpu, TrendingUp, CheckCircle2,
  Scale, Library, Sparkles, BookMarked,
  HardDrive, Users, Landmark, Building2, MapPin,
  Lightbulb, Wrench, Swords, Flag, CalendarRange,
  FileText, Server, Zap, ShieldCheck, Gem,
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

const PROJECT_STATS_TEMPLATE = [
  { value: '199', label: 'Countries Profiled', icon: Globe2, color: '#4A90D9' },
  { value: '1,000,000', label: 'Target Knowledge Nodes', icon: Network, color: '#6B3FA0' },
  { value: 'LIVE', label: 'Actors in Annals Backend', icon: CheckCircle2, color: '#2F855A' },
  { value: '16', label: 'Interpretive Frameworks', icon: Layers, color: '#D4AF37' },
  { value: '6', label: 'Canonical Eras', icon: BarChart3, color: '#C53030' },
  { value: '127', label: 'Weapons Catalogued', icon: Target, color: '#8B3A3A' },
  { value: '67', label: 'Ideas Catalogued', icon: Brain, color: '#6B3FA0' },
  { value: '72,000', label: 'Years of History Modeled', icon: Clock, color: '#DD6B20' },
]

const ACADEMIC_EQUIVALENCE = [
  {
    discipline: 'World History & Interdisciplinary Studies',
    level: 'Strong Masters-equivalent',
    detail: 'Six years of daily immersion across 382,000+ entities spanning 72,000 years and 199 countries — reading scholarly articles, curating causal chains, and cross-referencing civilizations. The breadth exceeds most single-discipline PhD holders, though it lacks the methodological depth and peer-reviewed publication record that a PhD requires. This is polymathic knowledge: wide, interconnected, and experientially deep.',
    icon: Globe2,
    color: '#4A90D9',
  },
  {
    discipline: 'Data Science & Knowledge Engineering',
    level: 'Masters-equivalent',
    detail: 'Designing and maintaining a 381,000+ node knowledge graph with 10 node classes, 287 divisions, 55+ relationship verbs, 16 interpretive frameworks, and Dewey-inspired call numbers. Practical mastery of ontology design, graph modeling, and data pipelines — but without the novel algorithmic contributions or peer-reviewed publications a PhD demands.',
    icon: Database,
    color: '#6B3FA0',
  },
  {
    discipline: 'Digital Humanities',
    level: 'Masters-equivalent',
    detail: 'Building a production-grade digital humanities platform that exceeds the scale of most funded DH initiatives. The curator workflow, evidence tiers, and multi-framework analysis demonstrate genuine scholarly infrastructure design — comparable to a strong Masters thesis in Digital Humanities.',
    icon: BookOpen,
    color: '#D4AF37',
  },
  {
    discipline: 'Full-Stack Software Engineering',
    level: 'Senior-level portfolio',
    detail: 'React 18 + TypeScript + Vite + Chakra UI frontend, Python + Appwrite + Pydantic backend, D3.js visualizations, GitHub CI/CD — a production-grade application built and maintained over 6 years. This is a genuine senior engineering portfolio.',
    icon: Code2,
    color: '#2F855A',
  },
  {
    discipline: 'Geographic & Cultural Pattern Recognition',
    level: 'Advanced practitioner',
    detail: '3,000+ hours of nature and culture documentaries, combined with daily entity reading across all continents. Can identify geographic regions by soil color, ocean water by coastline, tribal groups by facial features, and building traditions by material use. This is applied observational knowledge built through thousands of hours of intentional study — not academic GIS, but genuine practical expertise.',
    icon: Map,
    color: '#C53030',
  },
  {
    discipline: 'Comparative Religion & Philosophy',
    level: 'Advanced undergraduate',
    detail: 'Broad survey knowledge across Christianity, Islam, Buddhism, Hinduism, Judaism, and indigenous traditions through entity curation and documentary study. Strong on connections between traditions but without primary-language scholarship (Hebrew, Greek, Arabic, Sanskrit) that graduate study requires.',
    icon: Scroll,
    color: '#8B3A3A',
  },
]

const TEN_YEAR_MILESTONES = [
  { years: '1–2 (2020–2022)', title: 'Foundation', nodes: '50,000', detail: 'Schema design, ontology, 16 interpretive frameworks, core graph structure, curator workflow, MVP frontend, Neo4j backend', completed: true },
  { years: '3–4 (2022–2024)', title: 'Continental Depth', nodes: '200,000', detail: 'Full coverage of Africa (55 nations), Asia (48 nations), Europe (44 nations) — all countries with event windows, evidence tiers, and causal relationships', completed: true },
  { years: '5–6 (2024–2026)', title: 'Global Completion', nodes: '392,210', detail: 'Americas & Oceania complete. 392K entities seeded to Appwrite cloud backend. Wikidata SPARQL integration (273K Person entities + 118K others). 199 countries profiled. Migration to production infrastructure', completed: 'current' },
  { years: '7–8 (2026–2028)', title: 'Academic Integration', nodes: '750,000', detail: 'Scholarly API, peer review, open dataset publications, scholarly writing practice, community contributions', completed: false },
  { years: '9–10 (2028–2030)', title: 'Million-Node Graph', nodes: '1,000,000', detail: 'Complete knowledge graph with real-time querying, advanced visualizations, scholarly publications, and the curator\'s magnum opus', completed: false },
]

/* ─── Constants ─── */
const TARGET_NODES = 1_000_000

const LABEL_COLORS: Record<string, string> = {
  EventWindow: '#C53030', Person: '#4A90D9', Movement: '#D4AF37',
  Institution: '#2F855A', Text: '#8B3A3A', Idea: '#6B3FA0',
  Place: '#DD6B20', Evidence: '#718096',
}

const LABEL_ORDER = ['EventWindow', 'Person', 'Movement', 'Text', 'Institution', 'Idea', 'Place', 'Evidence']

/* ─── Encyclopedia Comparisons ─── */
const ENCYCLOPEDIA_COMPARISONS = [
  {
    name: 'Wikipedia (English)',
    nodes: '6,800,000+',
    rawCount: 6_800_000,
    type: 'Flat articles',
    coverage: 'General',
    model: 'Crowd-sourced wiki',
    strength: 'Breadth, accessibility, 300+ language editions',
    limitation: 'No causal chains, no interpretive frameworks, no knowledge graph structure',
    icon: Globe2,
    color: '#636363',
  },
  {
    name: 'Encyclopædia Britannica',
    nodes: '~120,000',
    rawCount: 120_000,
    type: 'Expert-authored articles',
    coverage: 'General',
    model: 'Editorial board + paid authors',
    strength: 'Scholarly authority, editorial rigor, 250+ year legacy',
    limitation: 'Proprietary, no structured data export, no causal modeling, no computational querying',
    icon: Library,
    color: '#003366',
  },
  {
    name: 'Stanford Encyclopedia of Philosophy',
    nodes: '~1,800',
    rawCount: 1_800,
    type: 'Peer-reviewed entries',
    coverage: 'Philosophy only',
    model: 'Academic peer review',
    strength: 'Gold-standard scholarship, deep argumentative analysis',
    limitation: 'Philosophy-only scope, no graph structure, no temporal modeling, cannot cross-reference events',
    icon: GraduationCap,
    color: '#8C1515',
  },
  {
    name: 'World History Encyclopedia',
    nodes: '~20,000',
    rawCount: 20_000,
    type: 'Educational articles',
    coverage: 'World history',
    model: 'Expert-contributed, peer-reviewed',
    strength: 'Accessible, well-illustrated, educational focus',
    limitation: 'No knowledge graph, no frameworks, no computational querying, limited causal analysis',
    icon: BookMarked,
    color: '#8B4513',
  },
  {
    name: 'Wikidata',
    nodes: '~108,000,000',
    rawCount: 108_000_000,
    type: 'Structured data items',
    coverage: 'General (machine-readable)',
    model: 'Community knowledge base',
    strength: 'Massive structured data, SPARQL-queryable, linked open data',
    limitation: 'No interpretive frameworks, no evidence tiers, no causal chains, breadth over depth',
    icon: Database,
    color: '#006699',
  },
  {
    name: 'Annals of the World',
    nodes: 'LIVE', // replaced at render time
    rawCount: 0,  // replaced at render time
    type: 'Knowledge graph nodes',
    coverage: '72,000 years · 199 countries',
    model: 'Curator-verified, AI-augmented',
    strength: 'Causal chains, 16 frameworks, evidence tiers, call numbers, computationally queryable',
    limitation: 'Year 6 of 10 — 381K+ nodes seeded, growing toward 1M',
    icon: Network,
    color: '#D4AF37',
  },
]

/* ─── Wikidata Fetch Census ─── */
interface WikidataFileStats {
  name: string
  classNumber: number
  count: number
  sizeMB: number
  icon: React.ElementType
  color: string
  divisions: number
  eraBreakdown: Record<string, number>
  significance: Record<string, number>
}

const WIKIDATA_CENSUS: WikidataFileStats[] = [
  { name: 'People', classNumber: 2, count: 238_466, sizeMB: 797.9, icon: Users, color: '#4A90D9', divisions: 34,
    eraBreakdown: { Classical: 6845, Contemporary: 90419, 'Early Modern': 22467, Medieval: 8564, Modern: 110160, Prehistoric: 11 },
    significance: { Landmark: 1597, Major: 20057, Notable: 99270, Moderate: 117119, Minor: 423 } },
  { name: 'Institutions', classNumber: 3, count: 36_738, sizeMB: 62.6, icon: Building2, color: '#2F855A', divisions: 41,
    eraBreakdown: { Classical: 7401, Contemporary: 14999, 'Early Modern': 2448, Medieval: 2965, Modern: 8924, Prehistoric: 1 },
    significance: { Landmark: 19, Major: 336, Notable: 1500, Moderate: 11783, Minor: 23100 } },
  { name: 'Places', classNumber: 4, count: 25_768, sizeMB: 38.3, icon: MapPin, color: '#DD6B20', divisions: 25,
    eraBreakdown: { Classical: 17907, Contemporary: 2400, 'Early Modern': 1192, Medieval: 1571, Modern: 2628, Prehistoric: 70 },
    significance: { Landmark: 477, Major: 1279, Notable: 4123, Moderate: 10864, Minor: 9025 } },
  { name: 'Ideas', classNumber: 1, count: 21_689, sizeMB: 30.8, icon: Lightbulb, color: '#6B3FA0', divisions: 54,
    eraBreakdown: { Classical: 15696, Contemporary: 4029, 'Early Modern': 292, Medieval: 192, Modern: 1475, Prehistoric: 5 },
    significance: { Landmark: 5, Major: 455, Notable: 1015, Moderate: 3837, Minor: 16377 } },
  { name: 'Artifacts', classNumber: 7, count: 17_328, sizeMB: 26.4, icon: Wrench, color: '#8B3A3A', divisions: 32,
    eraBreakdown: { Classical: 10545, Contemporary: 2574, 'Early Modern': 1055, Medieval: 697, Modern: 2359, Prehistoric: 98 },
    significance: { Landmark: 26, Major: 722, Notable: 1728, Moderate: 3741, Minor: 11111 } },
  { name: 'Events', classNumber: 5, count: 12_894, sizeMB: 17.7, icon: Swords, color: '#C53030', divisions: 28,
    eraBreakdown: { Classical: 5254, Contemporary: 2125, 'Early Modern': 1456, Medieval: 1188, Modern: 2870, Prehistoric: 1 },
    significance: { Landmark: 1, Major: 94, Notable: 348, Moderate: 2351, Minor: 10100 } },
  { name: 'Evidence', classNumber: 8, count: 8_282, sizeMB: 13.1, icon: ShieldCheck, color: '#718096', divisions: 18,
    eraBreakdown: { Classical: 6447, Contemporary: 454, 'Early Modern': 183, Medieval: 317, Modern: 810, Prehistoric: 71 },
    significance: { Landmark: 3, Major: 43, Notable: 225, Moderate: 1328, Minor: 6683 } },
  { name: 'Movements', classNumber: 6, count: 8_084, sizeMB: 10.8, icon: Flag, color: '#D4AF37', divisions: 42,
    eraBreakdown: { Classical: 23, Contemporary: 2515, 'Early Modern': 104, Medieval: 52, Modern: 5368 },
    significance: { Landmark: 1, Major: 143, Notable: 501, Moderate: 2039, Minor: 5378 } },
  { name: 'Timeframes', classNumber: 9, count: 3_529, sizeMB: 4.5, icon: CalendarRange, color: '#96770B', divisions: 13,
    eraBreakdown: { Classical: 3093, Contemporary: 47, 'Early Modern': 60, Medieval: 93, Modern: 91, Prehistoric: 145 },
    significance: { Landmark: 5, Major: 45, Notable: 432, Moderate: 789, Minor: 2258 } },
]

const WIKIDATA_TOTAL = WIKIDATA_CENSUS.reduce((s, f) => s + f.count, 0)
const WIKIDATA_TOTAL_SIZE_GB = (WIKIDATA_CENSUS.reduce((s, f) => s + f.sizeMB, 0) / 1024).toFixed(2)

const ERA_ORDER = ['Prehistoric', 'Classical', 'Medieval', 'Early Modern', 'Modern', 'Contemporary']
const ERA_COLORS: Record<string, string> = {
  Prehistoric: '#6B4D1B', Classical: '#8B4513', Medieval: '#A67C2E',
  'Early Modern': '#C5963A', Modern: '#4A90D9', Contemporary: '#6B3FA0',
}
const SIG_ORDER = ['Landmark', 'Major', 'Notable', 'Moderate', 'Minor']
const SIG_COLORS: Record<string, string> = {
  Landmark: '#D4AF37', Major: '#4A90D9', Notable: '#2F855A', Moderate: '#718096', Minor: '#A0AEC0',
}

/* ─── Big Data Dimensions (5 V's) ─── */
const BIG_DATA_DIMENSIONS = [
  {
    v: 'Volume',
    icon: HardDrive,
    color: '#4A90D9',
    current: `392,210 entities · ${WIKIDATA_TOTAL_SIZE_GB} GB raw data · ~1.96M projected edges`,
    target: '1,000,000 nodes · 5M+ edges · 10+ GB structured graph data',
    score: 37, // % toward big data threshold
  },
  {
    v: 'Variety',
    icon: Layers,
    color: '#6B3FA0',
    current: '10 node classes · 287 divisions · 55+ relationship verbs · 16 frameworks · 6 evidence tiers',
    target: 'Full ontology operational — heterogeneous, multi-modal knowledge graph',
    score: 85,
  },
  {
    v: 'Veracity',
    icon: ShieldCheck,
    color: '#2F855A',
    current: '6-tier evidence hierarchy · curator-verified · Wikidata-sourced QIDs · Wikipedia cross-references',
    target: 'All interpretive edges citation-backed with FRAMED_BY evidence chains',
    score: 70,
  },
  {
    v: 'Velocity',
    icon: Zap,
    color: '#D4AF37',
    current: 'Batch ingest: 392K entities in 9 automated SPARQL pipelines. Cursor-verified count: 392,210 entities',
    target: 'Streaming ingest from Wikidata/SPARQL + live curator submissions',
    score: 40,
  },
  {
    v: 'Value',
    icon: Gem,
    color: '#C53030',
    current: 'Causal chains, multi-framework analysis, Dewey call numbers, cross-civilization pattern detection',
    target: 'Computationally queryable knowledge graph powering research, AI, and education',
    score: 75,
  },
]

/* ─── Knowledge Graph Comparisons ─── */
const GRAPH_COMPARISONS = [
  { name: 'DBpedia', nodes: '~6.8M', edges: '~1.3B', scope: 'Wikipedia structured data' },
  { name: 'YAGO', nodes: '~64M', edges: '~200M', scope: 'Wikipedia + WordNet + GeoNames' },
  { name: 'Wikidata', nodes: '~108M', edges: '~1.5B', scope: 'Community knowledge base' },
  { name: 'Google KG', nodes: '~500B', edges: 'N/A', scope: 'Web-scale entity graph' },
  { name: 'Annals (current)', nodes: '392,210', edges: '~1.96M est.', scope: '72,000 years · 199 countries' },
  { name: 'Annals (target)', nodes: '1,000,000', edges: '~5M est.', scope: 'Complete human history graph' },
]

/* ─── Scholarly Impact Dimensions ─── */
const SCHOLARLY_IMPACT = [
  {
    title: 'Digital Humanities Infrastructure',
    detail: 'Provides a reusable ontology (11 node labels, 55+ relationship verbs, 6 evidence tiers) that other digital humanities projects can adopt. The Dewey-inspired call number system enables interoperability with library science standards.',
    icon: Layers,
    color: '#4A90D9',
  },
  {
    title: 'Computational History Methodology',
    detail: 'Demonstrates that history can be modeled as a knowledge graph with causal chains, enabling pattern detection across civilizations. Scholars can query "what caused X?" or "what did Y influence?" computationally — something no encyclopedia currently supports.',
    icon: Cpu,
    color: '#6B3FA0',
  },
  {
    title: 'Multi-Framework Analysis',
    detail: '16 interpretive frameworks (Cause & Effect, Cultural Diffusion, Empire & Colonialism, etc.) applied systematically across all nodes. This addresses a persistent critique in historiography: that narratives are imprisoned by a single lens.',
    icon: Microscope,
    color: '#D4AF37',
  },
  {
    title: 'Evidence-Based Audit Trail',
    detail: '6-tier evidence hierarchy (Primary Sources → Oral/Quantitative) with mandatory citations for interpretive edges. Every claim is auditable — a standard that sets this apart from crowd-sourced encyclopedias.',
    icon: Scale,
    color: '#2F855A',
  },
  {
    title: 'Open Data for AI & NLP Research',
    detail: 'CC0 public domain license means the entire knowledge graph is available as training data for large language models, historical NLP, and educational AI. Structured causal chains provide ground truth for reasoning benchmarks.',
    icon: Sparkles,
    color: '#C53030',
  },
  {
    title: 'Cross-Civilizational Pattern Detection',
    detail: 'By modeling 199 countries across 72,000 years with consistent schema, the graph enables macro-historical analysis: rise and fall patterns, technology diffusion rates, institutional convergence, and civilizational interaction networks.',
    icon: TrendingUp,
    color: '#DD6B20',
  },
]

export default function Curator() {
  const { total: totalNodes, byLabel, loading } = useGlobalCounts()

  const labelCounts = LABEL_ORDER
    .map(label => ({ label, count: byLabel[label] || 0, color: LABEL_COLORS[label] || '#718096' }))
    .sort((a, b) => b.count - a.count)

  const error: string | null = null

  const progressPct = totalNodes ? ((totalNodes / TARGET_NODES) * 100).toFixed(2) : '0.00'
  const maxLabelCount = labelCounts.length ? Math.max(...labelCounts.map(l => l.count)) : 6000

  const PROJECT_STATS = PROJECT_STATS_TEMPLATE.map(s =>
    s.value === 'LIVE'
      ? { ...s, value: totalNodes ? totalNodes.toLocaleString() : '…' }
      : s
  )

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
          subtitle="Live census from the Appwrite backend"
        />

        {/* Grand Total Bar */}
        <Box mt={6} p={6} bg="#082340" borderRadius="xl" mb={6}>
          {loading ? (
            <Flex justify="center" align="center" py={8}>
              <Spinner color="#D4AF37" size="lg" />
              <Text ml={3} fontFamily='"JetBrains Mono", monospace' fontSize="sm" color="#4A90D9">
                Fetching live stats from Appwrite…
              </Text>
            </Flex>
          ) : error ? (
            <Box py={6} textAlign="center">
              <Text fontFamily='"JetBrains Mono", monospace' fontSize="sm" color="#C53030">
                ⚠ {error}
              </Text>
            </Box>
          ) : (
            <>
              <Flex justify="space-between" align="flex-end" mb={3}>
                <Box>
                  <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#4A90D9" textTransform="uppercase" mb={1}>
                    Total Documented Nodes (Live)
                  </Text>
                  <Heading fontFamily='"Cinzel", serif' fontSize={{ base: '3xl', md: '5xl' }} color="#D4AF37">
                    {totalNodes?.toLocaleString()}
                  </Heading>
                </Box>
                <Box textAlign="right">
                  <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#E8F0FE">
                    of 1,000,000 target
                  </Text>
                  <Text fontFamily='"Cinzel", serif' fontSize="2xl" color="#D4AF37">
                    {progressPct}%
                  </Text>
                </Box>
              </Flex>
              {/* Progress bar */}
              <Box w="100%" h="12px" bg="#1A3A5C" borderRadius="full" overflow="hidden">
                <Box h="100%" w={`${Math.max(parseFloat(progressPct), 0.5)}%`} bg="linear-gradient(90deg, #D4AF37, #4A90D9)"
                  borderRadius="full" transition="width 0.5s" />
              </Box>
              <Flex justify="space-between" mt={2}>
                <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096">0</Text>
                <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096">250K</Text>
                <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096">500K</Text>
                <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096">750K</Text>
                <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096">1M</Text>
              </Flex>
            </>
          )}
        </Box>

        {/* By Node Type — Live from Appwrite */}
        <Box p={5} bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="xl">
          <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#2D2A24" mb={4}>
            Nodes by Schema Label — Live Backend Data
          </Text>
          {loading ? (
            <Flex justify="center" py={4}><Spinner color="#D4AF37" /></Flex>
          ) : (
            labelCounts.map(t => (
              <Flex key={t.label} align="center" gap={3} mb={2}>
                <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color={t.color}
                  minW="100px" fontWeight={600}>
                  {t.label}
                </Text>
                <Box flex={1} h="16px" bg="#E4E2DC" borderRadius="md" overflow="hidden">
                  <Box h="100%" bg={t.color} w={`${(t.count / maxLabelCount) * 100}%`}
                    borderRadius="md" transition="width 0.3s" />
                </Box>
                <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#524E44" minW="50px" textAlign="right">
                  {t.count.toLocaleString()}
                </Text>
              </Flex>
            ))
          )}
          <Text fontSize="10px" fontFamily='"JetBrains Mono", monospace' color="#718096" mt={3} textAlign="right">
            Annals Backend — {totalNodes?.toLocaleString() ?? '…'} entities · Appwrite Cloud
          </Text>
        </Box>
      </Box>

      {/* ─── Wikidata Fetch Census ─── */}
      <Box mb={10}>
        <SectionHeading
          title="Wikidata Fetch Census"
          subtitle={`${WIKIDATA_TOTAL.toLocaleString()} entities harvested across 9 automated SPARQL pipelines — ${WIKIDATA_TOTAL_SIZE_GB} GB raw data`}
        />

        {/* Grand totals row */}
        <SimpleGrid columns={{ base: 1, md: 3 }} gap={4} mt={6} mb={6}>
          <StatCard value={WIKIDATA_TOTAL.toLocaleString()} label="Total Wikidata Entities" color="#4A90D9" />
          <StatCard value={`${WIKIDATA_TOTAL_SIZE_GB} GB`} label="Raw JSON Data Volume" color="#6B3FA0" />
          <StatCard value="9" label="Fetch Pipelines (10 Classes)" color="#2F855A" />
        </SimpleGrid>

        {/* Per-file breakdown bars */}
        <Box p={5} bg="#082340" borderRadius="xl" mb={6}>
          <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#D4AF37" mb={4}>
            Entities by Node Class
          </Text>
          {WIKIDATA_CENSUS.map(f => {
            const Icon = f.icon
            const pct = (f.count / WIKIDATA_TOTAL * 100)
            return (
              <Flex key={f.name} align="center" gap={3} mb={3}>
                <Flex align="center" gap={2} minW="130px">
                  <Icon size={14} color={f.color} />
                  <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color={f.color} fontWeight={600}>
                    {f.name}
                  </Text>
                </Flex>
                <Box flex={1} h="18px" bg="#1A3A5C" borderRadius="md" overflow="hidden">
                  <Box h="100%" bg={f.color} w={`${(f.count / WIKIDATA_CENSUS[0].count) * 100}%`}
                    borderRadius="md" transition="width 0.3s" />
                </Box>
                <Flex align="baseline" gap={2} minW="150px" justify="flex-end">
                  <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#E8F0FE" fontWeight={600}>
                    {f.count.toLocaleString()}
                  </Text>
                  <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096">
                    ({pct.toFixed(1)}%)
                  </Text>
                </Flex>
              </Flex>
            )
          })}
          <Flex justify="space-between" mt={4} pt={3} borderTop="1px solid #1A3A5C">
            <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#D4AF37" fontWeight={700}>
              TOTAL
            </Text>
            <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#D4AF37" fontWeight={700}>
              {WIKIDATA_TOTAL.toLocaleString()} entities · {WIKIDATA_CENSUS.reduce((s, f) => s + f.divisions, 0)} divisions
            </Text>
          </Flex>
        </Box>

        {/* Era Distribution */}
        <SimpleGrid columns={{ base: 1, lg: 2 }} gap={6} mb={6}>
          <Box p={5} bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="xl">
            <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#2D2A24" mb={4}>
              Era Distribution — All Classes Combined
            </Text>
            {(() => {
              const eraTotals: Record<string, number> = {}
              WIKIDATA_CENSUS.forEach(f =>
                Object.entries(f.eraBreakdown).forEach(([era, n]) => { eraTotals[era] = (eraTotals[era] || 0) + n })
              )
              const maxEra = Math.max(...Object.values(eraTotals))
              return ERA_ORDER.map(era => {
                const count = eraTotals[era] || 0
                return (
                  <Flex key={era} align="center" gap={3} mb={2}>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color={ERA_COLORS[era]}
                      minW="100px" fontWeight={600}>{era}</Text>
                    <Box flex={1} h="14px" bg="#E4E2DC" borderRadius="md" overflow="hidden">
                      <Box h="100%" bg={ERA_COLORS[era]} w={`${(count / maxEra) * 100}%`} borderRadius="md" />
                    </Box>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#524E44" minW="55px" textAlign="right">
                      {count.toLocaleString()}
                    </Text>
                  </Flex>
                )
              })
            })()}
            <Text fontSize="10px" fontFamily='"JetBrains Mono", monospace' color="#718096" mt={3}>
              Prehistoric entities are rare — a sign of genuine scholarly depth
            </Text>
          </Box>

          {/* Significance Distribution */}
          <Box p={5} bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="xl">
            <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#2D2A24" mb={4}>
              Historical Significance — All Classes Combined
            </Text>
            {(() => {
              const sigTotals: Record<string, number> = {}
              WIKIDATA_CENSUS.forEach(f =>
                Object.entries(f.significance).forEach(([sig, n]) => { sigTotals[sig] = (sigTotals[sig] || 0) + n })
              )
              const maxSig = Math.max(...Object.values(sigTotals))
              return SIG_ORDER.map(sig => {
                const count = sigTotals[sig] || 0
                const pct = (count / WIKIDATA_TOTAL * 100)
                return (
                  <Flex key={sig} align="center" gap={3} mb={2}>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color={SIG_COLORS[sig]}
                      minW="80px" fontWeight={600}>{sig}</Text>
                    <Box flex={1} h="14px" bg="#E4E2DC" borderRadius="md" overflow="hidden">
                      <Box h="100%" bg={SIG_COLORS[sig]} w={`${(count / maxSig) * 100}%`} borderRadius="md" />
                    </Box>
                    <Flex minW="100px" justify="flex-end" gap={2}>
                      <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#524E44">
                        {count.toLocaleString()}
                      </Text>
                      <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096">
                        ({pct.toFixed(1)}%)
                      </Text>
                    </Flex>
                  </Flex>
                )
              })
            })()}
            <Text fontSize="10px" fontFamily='"JetBrains Mono", monospace' color="#718096" mt={3}>
              Pyramid distribution: few Landmarks, wide Moderate base — healthy knowledge graph
            </Text>
          </Box>
        </SimpleGrid>

        {/* Per-class detail grid */}
        <Box p={5} bg="#FDF8ED" border="1px solid #D4AF37" borderRadius="xl">
          <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#4A310D" mb={4}>
            Per-Class Breakdown — Divisions, Size & Top Era
          </Text>
          <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={4}>
            {WIKIDATA_CENSUS.map(f => {
              const Icon = f.icon
              const topEra = Object.entries(f.eraBreakdown).sort((a, b) => b[1] - a[1])[0]
              const topSig = Object.entries(f.significance).sort((a, b) => b[1] - a[1])[0]
              return (
                <Box key={f.name} p={4} bg="white" borderRadius="lg" border="1px solid #E4E2DC"
                  borderLeft="4px solid" borderLeftColor={f.color}>
                  <Flex align="center" gap={2} mb={2}>
                    <Icon size={16} color={f.color} />
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="sm" fontWeight={700} color={f.color}>
                      Class {f.classNumber} — {f.name}
                    </Text>
                  </Flex>
                  <SimpleGrid columns={2} gap={1}>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096">Entities</Text>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#2D2A24" fontWeight={600}>
                      {f.count.toLocaleString()}
                    </Text>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096">Divisions</Text>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#2D2A24" fontWeight={600}>
                      {f.divisions}
                    </Text>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096">Data Size</Text>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#2D2A24" fontWeight={600}>
                      {f.sizeMB} MB
                    </Text>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096">Top Era</Text>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color={ERA_COLORS[topEra[0]]} fontWeight={600}>
                      {topEra[0]} ({topEra[1].toLocaleString()})
                    </Text>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096">Mode Tier</Text>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color={SIG_COLORS[topSig[0]]} fontWeight={600}>
                      {topSig[0]} ({topSig[1].toLocaleString()})
                    </Text>
                  </SimpleGrid>
                </Box>
              )
            })}
          </SimpleGrid>
        </Box>
      </Box>

      {/* ─── Big Data Analysis ─── */}
      <Box mb={10}>
        <SectionHeading
          title="Big Data Readiness Assessment"
          subtitle="Evaluating the Annals knowledge graph against the 5 V's of Big Data"
        />
        <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" lineHeight={1.8} mt={2} mb={6} maxW="800px">
          At <strong>{WIKIDATA_TOTAL.toLocaleString()} entities</strong> across{' '}
          <strong>{WIKIDATA_TOTAL_SIZE_GB} GB</strong> of structured data, Annals of the World is a{' '}
          <strong>medium-scale knowledge graph</strong> — larger than most academic datasets, though not yet at the
          petabyte thresholds of industry "big data." However, when counting projected relationship edges (~1.86M),
          interpretive framework assignments, and the target of 1M nodes / 5M+ edges, the project is on a clear
          trajectory toward <strong>large-scale graph computing</strong>.
        </Text>

        {/* 5 V's Progress Bars */}
        <Box p={5} bg="#082340" borderRadius="xl" mb={6}>
          <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#D4AF37" mb={4}>
            The 5 V's of Big Data — Current Status
          </Text>
          {BIG_DATA_DIMENSIONS.map(d => {
            const Icon = d.icon
            return (
              <Box key={d.v} mb={5}>
                <Flex align="center" gap={2} mb={1}>
                  <Icon size={16} color={d.color} />
                  <Text fontFamily='"Cinzel", serif' fontSize="sm" fontWeight={700} color={d.color}>
                    {d.v}
                  </Text>
                  <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096" ml="auto">
                    {d.score}%
                  </Text>
                </Flex>
                <Box w="100%" h="10px" bg="#1A3A5C" borderRadius="full" overflow="hidden" mb={2}>
                  <Box h="100%" w={`${d.score}%`} bg={d.color} borderRadius="full" transition="width 0.5s" />
                </Box>
                <SimpleGrid columns={{ base: 1, md: 2 }} gap={2}>
                  <Box>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#4A90D9" mb={1}>CURRENT</Text>
                    <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#B8D4FE" lineHeight={1.6}>
                      {d.current}
                    </Text>
                  </Box>
                  <Box>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#D4AF37" mb={1}>TARGET</Text>
                    <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#B8D4FE" lineHeight={1.6}>
                      {d.target}
                    </Text>
                  </Box>
                </SimpleGrid>
              </Box>
            )
          })}
          <Flex justify="space-between" mt={4} pt={3} borderTop="1px solid #1A3A5C">
            <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#D4AF37" fontWeight={700}>
              COMPOSITE SCORE
            </Text>
            <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#D4AF37" fontWeight={700}>
              {Math.round(BIG_DATA_DIMENSIONS.reduce((s, d) => s + d.score, 0) / BIG_DATA_DIMENSIONS.length)}% — Medium-Scale Knowledge Graph
            </Text>
          </Flex>
        </Box>

        {/* Knowledge Graph Comparisons */}
        <Box p={5} bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="xl" mb={6}>
          <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#2D2A24" mb={4}>
            Knowledge Graph Scale Comparison
          </Text>
          <Box overflowX="auto">
            <Box as="table" w="100%" fontSize="xs" fontFamily='"JetBrains Mono", monospace'>
              <Box as="thead">
                <Box as="tr" bg="#082340">
                  {['Graph', 'Nodes', 'Edges', 'Scope'].map(h => (
                    <Box as="th" key={h} p={2} textAlign="left" color="#D4AF37" fontWeight={700} fontSize="10px">
                      {h}
                    </Box>
                  ))}
                </Box>
              </Box>
              <Box as="tbody">
                {GRAPH_COMPARISONS.map((g, i) => (
                  <Box as="tr" key={g.name} bg={i % 2 === 0 ? 'white' : '#FDF8ED'}
                    fontWeight={g.name.includes('Annals') ? 700 : 400}
                    color={g.name.includes('Annals') ? '#D4AF37' : '#524E44'}>
                    <Box as="td" p={2}>{g.name}</Box>
                    <Box as="td" p={2}>{g.nodes}</Box>
                    <Box as="td" p={2}>{g.edges}</Box>
                    <Box as="td" p={2}>{g.scope}</Box>
                  </Box>
                ))}
              </Box>
            </Box>
          </Box>
        </Box>

        {/* Verdict */}
        <Box p={5} bg="#FDF8ED" border="1px solid #D4AF37" borderRadius="xl">
          <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#4A310D" mb={3}>
            The Verdict: Not Yet "Big Data" — But Structurally Significant
          </Text>
          <SimpleGrid columns={{ base: 1, md: 3 }} gap={4}>
            <Box p={4} bg="white" borderRadius="lg" border="1px solid #E4E2DC">
              <Text fontFamily='"JetBrains Mono", monospace' fontSize="11px" color="#C53030" fontWeight={700} mb={2}>
                BY INDUSTRY STANDARDS
              </Text>
              <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#524E44" lineHeight={1.6}>
                Big data typically means petabytes (PB) of data processed across distributed systems.
                At ~1 GB / 392K nodes, Annals is a <strong>medium-scale dataset</strong> — large for
                academic humanities, modest by tech industry metrics.
              </Text>
            </Box>
            <Box p={4} bg="white" borderRadius="lg" border="1px solid #E4E2DC">
              <Text fontFamily='"JetBrains Mono", monospace' fontSize="11px" color="#2F855A" fontWeight={700} mb={2}>
                BY KNOWLEDGE GRAPH STANDARDS
              </Text>
              <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#524E44" lineHeight={1.6}>
                392K nodes with ~5 relationships each = ~1.96M edges. This is a <strong>serious research graph</strong>,
                comparable in depth (not breadth) to early DBpedia. At 1M nodes / 5M edges,
                Annals enters <strong>large-scale graph territory</strong>.
              </Text>
            </Box>
            <Box p={4} bg="white" borderRadius="lg" border="1px solid #E4E2DC">
              <Text fontFamily='"JetBrains Mono", monospace' fontSize="11px" color="#4A90D9" fontWeight={700} mb={2}>
                BY DIGITAL HUMANITIES STANDARDS
              </Text>
              <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#524E44" lineHeight={1.6}>
                This is <strong>among the largest structured historical datasets</strong> in existence.
                Most DH projects work with thousands of entities. At 392K entities across 10 classes,
                199 countries, and 72,000 years, Annals exceeds the scale of most funded DH initiatives.
              </Text>
            </Box>
          </SimpleGrid>
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
                Annals of the World (2020–2030)
              </Heading>
            </Flex>
            <Box bg="#E8F0FE" border="1px solid #B8D4FE" borderRadius="xl" p={5} mb={4}>
              <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#2D2A24" lineHeight={1.8}>
                This project continues Ussher's vision using <strong>AI-augmented research, graph databases, and interactive
                visualization</strong>. Where Ussher worked alone with quill and parchment, we use Neo4j, Python, TypeScript,
                D3.js, and large language models. Where he covered Creation to 70 CE through a biblical lens, we cover
                <strong> 72,000 years</strong> across <strong>199 countries</strong> through <strong>16 interpretive frameworks</strong>.
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
              Ussher: 1 framework (Biblical chronology). This project: 16 frameworks including Cause & Effect,
              Cultural Diffusion, Doctrine Development, Geopolitical Linkage, Temporal Linkage, Economic Systems,
              Political Systems, Comparative Religion, Empire & Colonialism, Environmental History, and Innovation & Technology.
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
          This project began on <strong>April 5, 2020</strong> — now in its <strong>sixth year</strong> of continuous development.
          Building a 381,000+ node knowledge graph that models all of documented human history across 199 countries
          — with scholarly citations, 16 interpretive frameworks, a production frontend, and an Appwrite cloud backend
          — is a body of work that spans multiple academic disciplines. Here is an honest assessment of what this
          project represents if submitted for formal evaluation — separating AI-augmented tooling from the curator's
          personal knowledge acquisition:
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
            3 Masters-equivalents + Senior Engineering Portfolio + Polymathic Breadth
          </Text>
          <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#4A90D9" mt={2}>
            ≈ 6+ years of autodidactic immersion · 20+ years of broad self-education · A rare polymathic knowledge base that no single degree program produces
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
                <Box w="12px" h="12px" borderRadius="full"
                  bg={m.completed === 'current' ? '#D4AF37' : m.completed ? '#2F855A' : '#E4E2DC'}
                  border="2px solid"
                  borderColor={m.completed === 'current' ? '#D4AF37' : m.completed ? '#2F855A' : '#D6D3CC'}
                  zIndex={1} />
                {i < TEN_YEAR_MILESTONES.length - 1 && (
                  <Box w="2px" flex={1} bg={m.completed ? '#2F855A' : '#E4E2DC'} minH="60px" />
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
                  {m.completed === true && (
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#2F855A" fontWeight={700}
                      bg="#F0FFF4" px={2} py={0.5} borderRadius="md">✓ COMPLETED</Text>
                  )}
                  {m.completed === 'current' && (
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#D4AF37" fontWeight={700}
                      bg="#FDF8ED" px={2} py={0.5} borderRadius="md">● CURRENT</Text>
                  )}
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

      {/* ─── Encyclopedia Comparison ─── */}
      <Box mb={10}>
        <SectionHeading
          title="How Annals Compares to the World's Encyclopedias"
          subtitle="Not a competitor — a new category of knowledge infrastructure"
        />
        <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" lineHeight={1.8} mt={2} mb={6} maxW="800px">
          Traditional encyclopedias store <strong>flat articles</strong>. Annals of the World stores
          <strong> structured knowledge nodes</strong> with causal chains, evidence tiers, interpretive frameworks,
          and computational queryability. This is not "another encyclopedia" — it is a <strong>knowledge graph</strong> designed
          for the age of AI, graph databases, and computational humanities.
        </Text>
        <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={5}>
          {ENCYCLOPEDIA_COMPARISONS.map(enc => {
            const Icon = enc.icon
            const isAnnals = enc.name === 'Annals of the World'
            const displayCount = isAnnals
              ? (totalNodes ? totalNodes.toLocaleString() : '…')
              : enc.nodes
            return (
              <Box key={enc.name} p={5}
                bg={isAnnals ? '#FDF8ED' : '#FAFAF8'}
                border={isAnnals ? '2px solid #D4AF37' : '1px solid #E4E2DC'}
                borderRadius="xl" position="relative"
                _hover={{ shadow: 'md' }} transition="all 0.2s">
                {isAnnals && (
                  <Text fontFamily='"JetBrains Mono", monospace' fontSize="9px" color="#D4AF37"
                    position="absolute" top={2} right={3} textTransform="uppercase" fontWeight={700}>
                    This Project
                  </Text>
                )}
                <Flex align="center" gap={3} mb={3}>
                  <Box p={2} bg={`${enc.color}15`} borderRadius="lg">
                    <Icon size={20} color={enc.color} />
                  </Box>
                  <Box>
                    <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#2D2A24">
                      {enc.name}
                    </Text>
                    <Text fontFamily='"Cinzel", serif' fontSize="lg" fontWeight={700} color={enc.color}>
                      {displayCount}
                    </Text>
                  </Box>
                </Flex>
                <Box mb={2}>
                  <Flex gap={2} flexWrap="wrap" mb={2}>
                    <Text as="span" fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096"
                      bg="#F0EDE5" px={2} py={0.5} borderRadius="md">{enc.type}</Text>
                    <Text as="span" fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#718096"
                      bg="#F0EDE5" px={2} py={0.5} borderRadius="md">{enc.coverage}</Text>
                  </Flex>
                  <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#524E44" lineHeight={1.6} mb={1}>
                    <strong>Model:</strong> {enc.model}
                  </Text>
                  <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#2F855A" lineHeight={1.5} mb={1}>
                    ✓ {enc.strength}
                  </Text>
                  <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#C53030" lineHeight={1.5}>
                    ✗ {enc.limitation}
                  </Text>
                </Box>
              </Box>
            )
          })}
        </SimpleGrid>

        {/* Differentiator Summary */}
        <Box mt={6} p={5} bg="#082340" borderRadius="xl">
          <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#D4AF37" mb={3}>
            What Makes Annals Structurally Different
          </Text>
          <SimpleGrid columns={{ base: 1, md: 2, lg: 4 }} gap={3}>
            {[
              { feature: 'Causal Chains', desc: 'Every node has causes and effects — queryable' },
              { feature: '16 Frameworks', desc: 'Multi-lens analysis vs single-narrative articles' },
              { feature: '6 Evidence Tiers', desc: 'Primary → Oral with audit trail' },
              { feature: 'Call Numbers', desc: 'Dewey-inspired classification for all 16K+ nodes' },
              { feature: 'Knowledge Graph', desc: 'Neo4j-backed, not flat text articles' },
              { feature: 'CC0 License', desc: 'Public domain — free for AI, research, education' },
              { feature: '199 Countries', desc: 'Global scope, not Western-centric' },
              { feature: 'Computationally Queryable', desc: 'Cypher/API not keyword search' },
            ].map(d => (
              <Box key={d.feature} p={3} bg="#0A2E52" borderRadius="lg" border="1px solid #1A3A5C">
                <Text fontFamily='"JetBrains Mono", monospace' fontSize="11px" fontWeight={700} color="#D4AF37">
                  {d.feature}
                </Text>
                <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#B8D4FE" mt={1}>
                  {d.desc}
                </Text>
              </Box>
            ))}
          </SimpleGrid>
        </Box>
      </Box>

      {/* ─── Scholarly Impact Analysis ─── */}
      <Box mb={10}>
        <SectionHeading
          title="Scholarly Impact Analysis"
          subtitle="How this project advances academic research and public knowledge"
        />
        <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" lineHeight={1.8} mt={2} mb={6} maxW="800px">
          Annals of the World addresses a gap no existing reference work fills: a <strong>computationally queryable,
          multi-framework, evidence-tiered knowledge graph</strong> covering all of documented human history.
          Here is how this project can impact the scholarly community:
        </Text>
        <SimpleGrid columns={{ base: 1, md: 2 }} gap={5}>
          {SCHOLARLY_IMPACT.map(s => {
            const Icon = s.icon
            return (
              <Box key={s.title} p={6} bg="#FDFAF5" border="1px solid #E4E2DC" borderRadius="xl"
                borderLeft="4px solid" borderLeftColor={s.color}>
                <Flex align="center" gap={3} mb={3}>
                  <Box p={2} bg={`${s.color}15`} borderRadius="lg">
                    <Icon size={20} color={s.color} />
                  </Box>
                  <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#2D2A24">
                    {s.title}
                  </Text>
                </Flex>
                <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" lineHeight={1.7}>
                  {s.detail}
                </Text>
              </Box>
            )
          })}
        </SimpleGrid>

        {/* Gap Analysis */}
        <Box mt={6} p={5} bg="#FDF8ED" border="1px solid #D4AF37" borderRadius="xl">
          <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#4A310D" mb={3}>
            The Gap This Project Fills
          </Text>
          <SimpleGrid columns={{ base: 1, md: 3 }} gap={4}>
            <Box p={4} bg="white" borderRadius="lg" border="1px solid #E4E2DC">
              <Text fontFamily='"JetBrains Mono", monospace' fontSize="11px" color="#C53030" fontWeight={700} mb={2}>
                PROBLEM
              </Text>
              <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#524E44" lineHeight={1.6}>
                No existing dataset combines structured temporal data + causal chains + multi-framework analysis
                across all civilizations. Wikipedia has breadth but no graph structure. Wikidata has structure but no
                interpretive depth. Academic databases are siloed by discipline.
              </Text>
            </Box>
            <Box p={4} bg="white" borderRadius="lg" border="1px solid #E4E2DC">
              <Text fontFamily='"JetBrains Mono", monospace' fontSize="11px" color="#2F855A" fontWeight={700} mb={2}>
                SOLUTION
              </Text>
              <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#524E44" lineHeight={1.6}>
                Annals provides a unified knowledge graph where every node has causes, effects, evidence,
                frameworks, and geographic context. Scholars can traverse causal paths, compare civilizations,
                and apply 16 interpretive lenses computationally — across 72,000 years and 199 countries.
              </Text>
            </Box>
            <Box p={4} bg="white" borderRadius="lg" border="1px solid #E4E2DC">
              <Text fontFamily='"JetBrains Mono", monospace' fontSize="11px" color="#4A90D9" fontWeight={700} mb={2}>
                USE CASES
              </Text>
              <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#524E44" lineHeight={1.6}>
                Digital humanities research · Comparative history coursework · AI reasoning benchmarks ·
                Historical NLP training data · Policy analysis (historical precedent) · Educational visualization
                · Cross-civilizational pattern detection · Interdisciplinary thesis research
              </Text>
            </Box>
          </SimpleGrid>
        </Box>
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
          Annals of the World · Inception: April 5, 2020 · Year 6 of 10 · CC0 Public Domain
        </Text>
      </Box>
    </Box>
  )
}
