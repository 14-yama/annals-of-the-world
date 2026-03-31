/* ─── Case Studies — Annals of the World ─── */
/* Interactive causal chain visualizations using the 16 interpretive frameworks */
import type { CaseStudy } from '../types'

export const CASE_STUDIES: CaseStudy[] = [
  /* ═══════════════════════════════════════════════════════════
   * CASE STUDY 1: Quest for a Route to India
   * Why did Europeans bypass the Silk Road and sail west?
   * Frameworks: CAUSE_AND_EFFECT, GEOPOLITICAL_LINKAGE, CULTURAL_DIFFUSION
   * ═══════════════════════════════════════════════════════════ */
  {
    id: 'route-to-india',
    title: 'The Quest for a Route to India',
    subtitle: 'Why Europeans Bypassed the Silk Road and Sailed West',
    description:
      'The fall of Constantinople (1453) and Ottoman control of overland trade routes made spices prohibitively expensive. ' +
      'European powers — Portugal and Spain — invested in maritime technology to bypass the Silk Road. ' +
      'Columbus sailed west expecting India but found the Americas. This cascade reshaped the world.',
    era: 'early-modern',
    region: 'Western Europe',
    frameworks: ['CAUSE_AND_EFFECT', 'GEOPOLITICAL_LINKAGE', 'CULTURAL_DIFFUSION'],
    keyInsight:
      'The Ottoman capture of Constantinople didn\'t just end the Byzantine Empire — it severed Europe\'s overland spice route, ' +
      'triggering a maritime revolution that accidentally connected the Old and New Worlds.',
    nodes: [
      {
        id: 'silk-road-trade',
        title: 'Silk Road Prosperity',
        year: 1200,
        description:
          'For centuries, the Silk Road connected China and India to Mediterranean markets. ' +
          'Spices, silk, and precious goods flowed through Central Asian and Middle Eastern middlemen.',
        era: 'medieval',
        region: 'Central Asia',
        framework: 'GEOPOLITICAL_LINKAGE',
      },
      {
        id: 'mongol-pax',
        title: 'Pax Mongolica Facilitates Trade',
        year: 1260,
        description:
          'The Mongol Empire unified the Silk Road under one authority (1206–1368), making overland trade safer and cheaper. ' +
          'Marco Polo traveled to China during this era.',
        era: 'medieval',
        region: 'Central Asia',
        framework: 'GEOPOLITICAL_LINKAGE',
      },
      {
        id: 'mongol-collapse',
        title: 'Mongol Empire Fragments',
        year: 1368,
        description:
          'The collapse of the Mongol Empire fragmented the Silk Road into competing khanates and sultanates.' +
          ' Trade become more dangerous and expensive.',
        era: 'medieval',
        region: 'Central Asia',
        framework: 'CONFLICT_AND_RESOLUTION',
      },
      {
        id: 'ottoman-rise',
        title: 'Ottoman Empire Controls Trade Routes',
        year: 1400,
        description:
          'The rising Ottoman Empire progressively controlled key chokepoints along overland trade routes to Asia. ' +
          'They imposed tariffs on goods passing through their territory.',
        era: 'medieval',
        region: 'West Asia',
        framework: 'GEOPOLITICAL_LINKAGE',
      },
      {
        id: 'constantinople-falls',
        title: 'Fall of Constantinople',
        year: 1453,
        description:
          'Sultan Mehmed II conquers Constantinople, ending the Byzantine Empire. ' +
          'The Ottomans now control the gateway between Europe and Asia. ' +
          'Spice prices in European markets skyrocket 300-400%.',
        era: 'medieval',
        region: 'Eastern Europe',
        framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'spice-demand',
        title: 'European Spice Crisis',
        year: 1460,
        description:
          'Pepper, cinnamon, cloves, and nutmeg were essential for food preservation, medicine, and trade. ' +
          'With the Ottoman toll, European merchants needed an alternative route.',
        era: 'early-modern',
        region: 'Western Europe',
        framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'portuguese-navigation',
        title: 'Portuguese Maritime Innovation',
        year: 1420,
        description:
          'Prince Henry the Navigator invests in caravel ships, astrolabe navigation, and systematic coastal exploration. ' +
          'Portugal becomes the first European power to explore the African coast.',
        era: 'early-modern',
        region: 'Western Europe',
        framework: 'ADAPTATION',
      },
      {
        id: 'bartholomeu-dias',
        title: 'Dias Rounds the Cape of Good Hope',
        year: 1488,
        description:
          'Bartholomeu Dias sails around the southern tip of Africa, proving a sea route to the Indian Ocean exists.',
        era: 'early-modern',
        region: 'Southern Africa',
        framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'columbus-voyage',
        title: 'Columbus Sails West',
        year: 1492,
        description:
          'Sponsored by Spain (which couldn\'t compete with Portugal\'s African route), ' +
          'Columbus sails west believing he can reach India. He lands in the Caribbean and calls the people "Indians."',
        era: 'early-modern',
        region: 'Americas',
        framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'vasco-da-gama',
        title: 'Vasco da Gama Reaches India',
        year: 1498,
        description:
          'Da Gama completes the sea route to India via the Cape of Good Hope. ' +
          'Returns with spices worth 60× the cost of the voyage. The Silk Road\'s monopoly is broken.',
        era: 'early-modern',
        region: 'South Asia',
        framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'columbian-exchange',
        title: 'The Columbian Exchange',
        year: 1500,
        description:
          'The accidental discovery of the Americas triggers massive ecological, demographic, and cultural exchange. ' +
          'Potatoes, tomatoes, and maize go east; horses, wheat, and diseases go west. ' +
          '90% of indigenous Americans die from Old World diseases.',
        era: 'early-modern',
        region: 'Americas',
        framework: 'CULTURAL_DIFFUSION',
      },
    ],
    edges: [
      { source: 'silk-road-trade', target: 'mongol-pax', verb: 'ENABLES', framework: 'GEOPOLITICAL_LINKAGE', evidence: 'B: Abu-Lughod 1989', description: 'Mongol unification facilitates existing trade networks' },
      { source: 'mongol-pax', target: 'mongol-collapse', verb: 'PRECEDES', framework: 'TEMPORAL_LINKAGE', evidence: 'B: Weatherford 2004', description: 'Pax Mongolica collapses as empire fragments' },
      { source: 'mongol-collapse', target: 'ottoman-rise', verb: 'ENABLES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Findley 2005', description: 'Power vacuum allows Ottoman expansion' },
      { source: 'ottoman-rise', target: 'constantinople-falls', verb: 'CAUSES', framework: 'CAUSE_AND_EFFECT', evidence: 'A: Runciman 1965', description: 'Ottoman expansion culminates in conquest' },
      { source: 'constantinople-falls', target: 'spice-demand', verb: 'TRIGGERS', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Crowley 2005', description: 'Loss of trade gateway creates European spice crisis' },
      { source: 'spice-demand', target: 'portuguese-navigation', verb: 'ENABLES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Diffie & Winius 1977', description: 'Demand for alternative routes funds maritime innovation' },
      { source: 'portuguese-navigation', target: 'bartholomeu-dias', verb: 'ENABLES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Russell-Wood 1998', description: 'Decades of exploration lead to the Cape' },
      { source: 'bartholomeu-dias', target: 'vasco-da-gama', verb: 'ENABLES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Subrahmanyam 1997', description: 'Proof of concept enables the India voyage' },
      { source: 'spice-demand', target: 'columbus-voyage', verb: 'TRIGGERS', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Phillips & Phillips 1992', description: 'Spain sponsors westward route as alternative' },
      { source: 'columbus-voyage', target: 'columbian-exchange', verb: 'TRIGGERS', framework: 'CULTURAL_DIFFUSION', evidence: 'B: Crosby 2003', description: 'Contact between hemispheres begins massive exchange' },
      { source: 'vasco-da-gama', target: 'columbian-exchange', verb: 'ENABLES', framework: 'CULTURAL_DIFFUSION', evidence: 'B: Subrahmanyam 1997', description: 'Maritime routes accelerate global exchange' },
    ],
  },

  /* ═══════════════════════════════════════════════════════════
   * CASE STUDY 2: Singapore's Rise — From Fishing Village to $82k GDP
   * Historical causation chain showing past→present correlation
   * Frameworks: CAUSE_AND_EFFECT, GEOPOLITICAL_LINKAGE, ADAPTATION
   * ═══════════════════════════════════════════════════════════ */
  {
    id: 'singapore-rise',
    title: 'Singapore\'s Rise',
    subtitle: 'From Fishing Village to $82,000 GDP per Capita',
    description:
      'Singapore\'s extraordinary economic rise didn\'t happen overnight. It is a product of 200 years of compounding advantages: ' +
      'strategic geography, British colonial infrastructure, forced independence, visionary governance, and relentless adaptation.',
    era: 'contemporary',
    region: 'Southeast Asia',
    frameworks: ['CAUSE_AND_EFFECT', 'GEOPOLITICAL_LINKAGE', 'ADAPTATION', 'TEMPORAL_LINKAGE'],
    keyInsight:
      'Singapore\'s GDP didn\'t materialize from nothing — it was built on a chain: Straits of Malacca geography → ' +
      'British free port → wartime destruction → painful independence → survival-driven governance → education investment → ' +
      'financial hub status. Each link was causally necessary.',
    nodes: [
      {
        id: 'sg-geography',
        title: 'Strategic Location on Strait of Malacca',
        year: 1300,
        description:
          'Located at the narrowest point of the Strait of Malacca, through which 25% of global shipping passes. ' +
          'The Srivijaya and Majapahit empires recognized this advantage centuries before the British.',
        era: 'medieval',
        region: 'Southeast Asia',
        framework: 'GEOPOLITICAL_LINKAGE',
      },
      {
        id: 'sg-raffles',
        title: 'Stamford Raffles Founds Modern Singapore',
        year: 1819,
        description:
          'Sir Stamford Raffles establishes Singapore as a British free port — zero tariffs. ' +
          'Within 5 years it becomes the busiest port in Southeast Asia, attracting Chinese, Malay, Indian, and Arab merchants.',
        era: 'modern',
        region: 'Southeast Asia',
        framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'sg-entrepot',
        title: 'Entrepôt Trade Hub',
        year: 1860,
        description:
          'Singapore becomes the world\'s premier entrepôt (re-export) center. ' +
          'Rubber, tin, and spices from the Malay Archipelago flow through Singapore to global markets. ' +
          'The port builds the infrastructure, institutions, and merchant class that will persist for 160 years.',
        era: 'modern',
        region: 'Southeast Asia',
        framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'sg-ww2',
        title: 'Japanese Occupation (1942–1945)',
        year: 1942,
        description:
          'Japan captures Singapore in Britain\'s worst military defeat. 3.5 years of brutal occupation. ' +
          'This shattered the myth of British invincibility and catalyzed independence movements across Asia.',
        era: 'modern',
        region: 'Southeast Asia',
        framework: 'CONFLICT_AND_RESOLUTION',
      },
      {
        id: 'sg-self-govt',
        title: 'Self-Government and Merger with Malaysia',
        year: 1959,
        description:
          'Lee Kuan Yew\'s PAP wins elections. Singapore achieves self-governance, then merges with Malaysia (1963) ' +
          'seeking economic security and a hinterland.',
        era: 'contemporary',
        region: 'Southeast Asia',
        framework: 'GEOPOLITICAL_LINKAGE',
      },
      {
        id: 'sg-independence',
        title: 'Forced Independence from Malaysia',
        year: 1965,
        description:
          'Racial tensions lead Malaysia to expel Singapore. Lee Kuan Yew weeps on national television. ' +
          'A tiny island (719 km²) with no natural resources, no military, and no hinterland must survive alone.',
        era: 'contemporary',
        region: 'Southeast Asia',
        framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'sg-survival',
        title: 'Survival-Driven Governance',
        year: 1966,
        description:
          'Lee Kuan Yew\'s government implements radical policies: mandatory national service, ' +
          'public housing for 80% of population (HDB), bilingual education (English + mother tongue), ' +
          'anti-corruption bureau (CPIB), and export-oriented industrialization.',
        era: 'contemporary',
        region: 'Southeast Asia',
        framework: 'ADAPTATION',
      },
      {
        id: 'sg-education',
        title: 'Education and Human Capital Investment',
        year: 1970,
        description:
          'Singapore invests 20% of budget in education. Creates a world-class education system (consistently #1 in PISA). ' +
          'Shifts from labor-intensive manufacturing to knowledge economy. NUS, NTU become top-50 global universities.',
        era: 'contemporary',
        region: 'Southeast Asia',
        framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'sg-finance',
        title: 'Financial Hub Strategy',
        year: 1980,
        description:
          'Singapore positions itself as Asia\'s financial center — attracting banks, hedge funds, and tech firms. ' +
          'Rule of law, English-language courts, low corruption (Transparency International: consistently top 5). ' +
          'The port advantage from 1819 now translates to capital flows.',
        era: 'contemporary',
        region: 'Southeast Asia',
        framework: 'ADAPTATION',
      },
      {
        id: 'sg-tech-hub',
        title: 'Tech and Innovation Economy',
        year: 2000,
        description:
          'Singapore invests in biomedical sciences, semiconductors (chip fabs), fintech, and AI. ' +
          'Attracted by stability, infrastructure, and talent — Google, Meta, and Dyson set up regional HQ.',
        era: 'contemporary',
        region: 'Southeast Asia',
        framework: 'ADAPTATION',
      },
      {
        id: 'sg-today',
        title: 'GDP per Capita: $82,808 (2024)',
        year: 2024,
        description:
          '$82,808 GDP per capita (PPP) — 3rd highest globally. From a fishing village with no resources to one of the wealthiest nations. ' +
          '6 million people on 733 km². Higher life expectancy (84 years) than the US, UK, or Japan.',
        era: 'contemporary',
        region: 'Southeast Asia',
        framework: 'TEMPORAL_LINKAGE',
      },
    ],
    edges: [
      { source: 'sg-geography', target: 'sg-raffles', verb: 'ENABLES', framework: 'GEOPOLITICAL_LINKAGE', evidence: 'B: Turnbull 2009', description: 'Strategic location attracted colonial interest' },
      { source: 'sg-raffles', target: 'sg-entrepot', verb: 'CAUSES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Turnbull 2009', description: 'Free port policy creates trade hub' },
      { source: 'sg-entrepot', target: 'sg-ww2', verb: 'PRECEDES', framework: 'TEMPORAL_LINKAGE', evidence: 'B: Bayly & Harper 2004', description: 'Strategic value makes Singapore a Japanese target' },
      { source: 'sg-ww2', target: 'sg-self-govt', verb: 'TRIGGERS', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Lee Kuan Yew 1998', description: 'Occupation shatters colonial legitimacy' },
      { source: 'sg-self-govt', target: 'sg-independence', verb: 'CAUSES', framework: 'CAUSE_AND_EFFECT', evidence: 'A: Separation Agreement 1965', description: 'Merger fails due to racial politics' },
      { source: 'sg-independence', target: 'sg-survival', verb: 'TRIGGERS', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Lee Kuan Yew 1998', description: 'Existential crisis drives radical governance' },
      { source: 'sg-survival', target: 'sg-education', verb: 'ENABLES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Yew 2011', description: 'Governance framework prioritizes human capital' },
      { source: 'sg-education', target: 'sg-finance', verb: 'ENABLES', framework: 'ADAPTATION', evidence: 'B: Schein 1996', description: 'Educated workforce attracts financial sector' },
      { source: 'sg-finance', target: 'sg-tech-hub', verb: 'ENABLES', framework: 'ADAPTATION', evidence: 'B: Chia 2011', description: 'Financial infrastructure supports tech ecosystem' },
      { source: 'sg-tech-hub', target: 'sg-today', verb: 'CAUSES', framework: 'CAUSE_AND_EFFECT', evidence: 'D: World Bank 2024', description: 'Innovation economy produces world-class GDP' },
      { source: 'sg-geography', target: 'sg-today', verb: 'IS_ANTECEDENT_TO', framework: 'TEMPORAL_LINKAGE', evidence: 'B: Turnbull 2009', description: 'Geography remains the enduring advantage across 700 years' },
    ],
  },

  /* ═══════════════════════════════════════════════════════════
   * CASE STUDY 3: Origins of the World Wars
   * Why did industrialized nations destroy themselves twice?
   * Frameworks: CAUSE_AND_EFFECT, CONFLICT_AND_RESOLUTION, GEOPOLITICAL_LINKAGE
   * ═══════════════════════════════════════════════════════════ */
  {
    id: 'world-wars-origins',
    title: 'Origins of the World Wars',
    subtitle: 'How Imperial Rivalries Ignited Two Global Conflagrations',
    description:
      'WWI and WWII were not separate events — they form one continuous arc of destruction rooted in ' +
      'imperial competition, industrial weaponry, failed peace, economic collapse, and ideological extremism. ' +
      'Understanding the causal chain from 1871 to 1945 reveals how easily civilization can unravel.',
    era: 'modern',
    region: 'Europe',
    frameworks: ['CAUSE_AND_EFFECT', 'CONFLICT_AND_RESOLUTION', 'GEOPOLITICAL_LINKAGE'],
    keyInsight:
      'The Treaty of Versailles did not end WWI\'s causes — it transformed them. Germany\'s humiliation, ' +
      'combined with the Great Depression, created the exact conditions for fascism. WWII was not a new war; ' +
      'it was the unfinished business of the first.',
    nodes: [
      {
        id: 'ww-unification',
        title: 'German Unification under Bismarck',
        year: 1871,
        description:
          'Prussia unifies Germany after defeating France. The new German Empire is industrializing rapidly, ' +
          'disrupting the European balance of power that had held since 1815.',
        era: 'modern',
        region: 'Western Europe',
        framework: 'GEOPOLITICAL_LINKAGE',
      },
      {
        id: 'ww-alliances',
        title: 'Alliance System Crystallizes',
        year: 1907,
        description:
          'Europe splits into two armed camps: Triple Alliance (Germany, Austria-Hungary, Italy) vs ' +
          'Triple Entente (France, Russia, Britain). Any local conflict will trigger a continental war.',
        era: 'modern',
        region: 'Europe',
        framework: 'GEOPOLITICAL_LINKAGE',
      },
      {
        id: 'ww-arms-race',
        title: 'Naval Arms Race & Colonial Tensions',
        year: 1898,
        description:
          'Kaiser Wilhelm II challenges British naval supremacy with massive shipbuilding. ' +
          'Germany demands colonial territories ("a place in the sun"). Britain feels threatened.',
        era: 'modern',
        region: 'Europe',
        framework: 'CONFLICT_AND_RESOLUTION',
      },
      {
        id: 'ww-sarajevo',
        title: 'Assassination at Sarajevo',
        year: 1914,
        description:
          'Archduke Franz Ferdinand of Austria-Hungary is assassinated by Gavrilo Princip, a Bosnian Serb nationalist. ' +
          'Austria issues an ultimatum to Serbia. Russia mobilizes. The alliance system fires like dominoes.',
        era: 'modern',
        region: 'Eastern Europe',
        framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'ww-industrialized',
        title: 'Industrialized Trench Warfare',
        year: 1916,
        description:
          'At the Somme, 1 million casualties in 5 months for 10 km of mud. Machine guns, poison gas, ' +
          'and artillery turn the Western Front into a meat grinder. Industrial production amplifies killing.',
        era: 'modern',
        region: 'Western Europe',
        framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'ww-versailles',
        title: 'Treaty of Versailles',
        year: 1919,
        description:
          'Germany loses 13% of territory, all colonies, and must pay 132 billion gold marks in reparations. ' +
          'Article 231 ("War Guilt Clause") assigns sole blame. Germans call it the "Diktat." ' +
          'Economist Keynes warns the terms will destroy European stability.',
        era: 'modern',
        region: 'Western Europe',
        framework: 'CONFLICT_AND_RESOLUTION',
      },
      {
        id: 'ww-hyperinflation',
        title: 'Weimar Hyperinflation',
        year: 1923,
        description:
          'German mark collapses to 4.2 trillion marks per dollar. Workers\' life savings become worthless overnight. ' +
          'Middle class is destroyed, breeding resentment against the Weimar Republic and the Versailles order.',
        era: 'modern',
        region: 'Western Europe',
        framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'ww-depression',
        title: 'Great Depression Hits Germany',
        year: 1929,
        description:
          'Wall Street crash triggers global depression. US banks recall German loans. German unemployment hits 30%. ' +
          'Democratic parties seem helpless. Voters turn to extremes: Nazis and Communists.',
        era: 'modern',
        region: 'Western Europe',
        framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'ww-hitler-rise',
        title: 'Hitler Becomes Chancellor',
        year: 1933,
        description:
          'Adolf Hitler\'s Nazi Party wins the largest share of votes. President Hindenburg appoints him Chancellor. ' +
          'Within 18 months: Reichstag fire, Enabling Act, all other parties banned, rearmament begins.',
        era: 'modern',
        region: 'Western Europe',
        framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'ww-appeasement',
        title: 'Appeasement Fails',
        year: 1938,
        description:
          'Britain and France allow Hitler to annex Austria and Czechoslovakia\'s Sudetenland, hoping to avoid war. ' +
          'Churchill warns: "You were given the choice between war and dishonour. You chose dishonour, and you will have war."',
        era: 'modern',
        region: 'Western Europe',
        framework: 'GEOPOLITICAL_LINKAGE',
      },
      {
        id: 'ww-wwii-begins',
        title: 'World War II Erupts',
        year: 1939,
        description:
          'Germany invades Poland on September 1. Britain and France declare war. ' +
          'By 1945: 70–85 million dead (3% of world population), the Holocaust, two atomic bombs, ' +
          'and the complete reordering of global power.',
        era: 'modern',
        region: 'Europe',
        framework: 'CONFLICT_AND_RESOLUTION',
      },
    ],
    edges: [
      { source: 'ww-unification', target: 'ww-arms-race', verb: 'TRIGGERS', framework: 'GEOPOLITICAL_LINKAGE', evidence: 'B: Clark 2012', description: 'Unified Germany seeks global power status' },
      { source: 'ww-arms-race', target: 'ww-alliances', verb: 'CAUSES', framework: 'GEOPOLITICAL_LINKAGE', evidence: 'B: Clark 2012', description: 'Arms racing drives nations into defensive blocs' },
      { source: 'ww-alliances', target: 'ww-sarajevo', verb: 'ENABLES', framework: 'CAUSE_AND_EFFECT', evidence: 'A: MacMillan 2013', description: 'Alliance system turns assassination into continental war' },
      { source: 'ww-sarajevo', target: 'ww-industrialized', verb: 'TRIGGERS', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Keegan 1998', description: 'Declaration of war unleashes industrial warfare' },
      { source: 'ww-industrialized', target: 'ww-versailles', verb: 'CAUSES', framework: 'CONFLICT_AND_RESOLUTION', evidence: 'B: MacMillan 2001', description: 'Devastating war demands punitive peace' },
      { source: 'ww-versailles', target: 'ww-hyperinflation', verb: 'CAUSES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Fergusson 1975', description: 'Reparations crush German economy' },
      { source: 'ww-hyperinflation', target: 'ww-depression', verb: 'ENABLES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Kindleberger 1973', description: 'Weakened economy collapses under global pressure' },
      { source: 'ww-depression', target: 'ww-hitler-rise', verb: 'CAUSES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Kershaw 1998', description: 'Economic despair fuels extremist movements' },
      { source: 'ww-hitler-rise', target: 'ww-appeasement', verb: 'TRIGGERS', framework: 'GEOPOLITICAL_LINKAGE', evidence: 'B: Faber 2008', description: 'Democracies try to accommodate aggressor' },
      { source: 'ww-appeasement', target: 'ww-wwii-begins', verb: 'ENABLES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Bouverie 2019', description: 'Failed appeasement emboldens further expansion' },
      { source: 'ww-versailles', target: 'ww-wwii-begins', verb: 'IS_ANTECEDENT_TO', framework: 'TEMPORAL_LINKAGE', evidence: 'B: Keynes 1919', description: 'Punitive peace sows seeds of second conflict' },
    ],
  },

  /* ═══════════════════════════════════════════════════════════
   * CASE STUDY 4: Mesopotamian Social Stratification
   * Why every civilization adopted hierarchical class systems
   * Frameworks: CAUSE_AND_EFFECT, CULTURAL_DIFFUSION, LEGAL_INTERPRETATION
   * ═══════════════════════════════════════════════════════════ */
  {
    id: 'mesopotamian-stratification',
    title: 'Mesopotamian Social Stratification',
    subtitle: 'Why Every Civilization Adopted Hierarchical Class Systems',
    description:
      'When Mesopotamian farmers learned to control the Tigris and Euphrates through irrigation, they created food surpluses ' +
      'that freed some people from farming. This seemingly simple innovation — growing more than you need — created ' +
      'priests, kings, scribes, soldiers, and slaves. Every subsequent civilization copied this template.',
    era: 'classical',
    region: 'West Asia',
    frameworks: ['CAUSE_AND_EFFECT', 'CULTURAL_DIFFUSION', 'LEGAL_INTERPRETATION'],
    keyInsight:
      'Social stratification is not natural — it was invented. It required three preconditions that first converged in Sumer: ' +
      'agricultural surplus (to free non-farmers), record-keeping (to track debts and tribute), and codified law ' +
      '(to enforce inequality). Once this pattern proved stable, every growing society reinvented or borrowed it.',
    nodes: [
      {
        id: 'ms-irrigation',
        title: 'Irrigation Agriculture in Sumer',
        year: -5000,
        description:
          'Sumerian farmers build canals to redirect Tigris-Euphrates floodwaters. ' +
          'Irrigated fields produce 3-5× more grain than rain-fed agriculture. ' +
          'For the first time in history, a community can grow more food than it needs.',
        era: 'prehistoric',
        region: 'West Asia',
        framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'ms-surplus',
        title: 'Agricultural Surplus',
        year: -4500,
        description:
          'Surplus grain must be stored, distributed, and defended. Granaries become the first public buildings. ' +
          'Whoever controls the granary controls the community. The seed of inequality is planted.',
        era: 'prehistoric',
        region: 'West Asia',
        framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'ms-temples',
        title: 'Temple Complexes & Priest Class',
        year: -4000,
        description:
          'Temples claim to mediate between gods and harvest. Priests manage grain distribution, ' +
          'becoming the first non-farming elite. Citizens pay tribute (grain, labor) for divine protection.',
        era: 'classical',
        region: 'West Asia',
        framework: 'RITUAL_STANDARDIZATION',
      },
      {
        id: 'ms-writing',
        title: 'Invention of Cuneiform Writing',
        year: -3400,
        description:
          'Scribes develop cuneiform to track grain debts, tribute payments, and temple accounts. ' +
          'Writing was invented not for poetry — but for accounting. Literacy becomes a class marker.',
        era: 'classical',
        region: 'West Asia',
        framework: 'TEXTUAL_TRANSMISSION',
      },
      {
        id: 'ms-kingship',
        title: 'Rise of Kingship',
        year: -3000,
        description:
          'War leaders (lugal) become permanent kings. The Sumerian King List documents "kingship descending from heaven." ' +
          'Military command + religious legitimacy = divine right of kings. A template copied for 5,000 years.',
        era: 'classical',
        region: 'West Asia',
        framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'ms-hammurabi',
        title: 'Code of Hammurabi',
        year: -1754,
        description:
          '282 laws carved in stone. Punishments vary by social class: a free man\'s eye is worth a free man\'s eye, ' +
          'but a slave\'s eye is worth only silver. Law codifies inequality as divine order.',
        era: 'classical',
        region: 'West Asia',
        framework: 'LEGAL_INTERPRETATION',
      },
      {
        id: 'ms-egypt-adopts',
        title: 'Egypt Develops Parallel Stratification',
        year: -3100,
        description:
          'Nile Valley agriculture produces similar surpluses. Egypt develops pharaohs (god-kings), ' +
          'a priest class (at Karnak, Heliopolis), scribes (hieroglyphics), and a massive slave/corvée labor system. ' +
          'Same pattern, independent invention.',
        era: 'classical',
        region: 'North Africa',
        framework: 'CULTURAL_DIFFUSION',
      },
      {
        id: 'ms-indus-adopts',
        title: 'Indus Valley Stratification',
        year: -2600,
        description:
          'Harappa and Mohenjo-daro show clear evidence of social hierarchy: large granaries, citadels, ' +
          'standardized weights (trade bureaucracy), and differentiated housing. ' +
          'Later the Vedic caste system (varna) formalizes stratification into religious doctrine.',
        era: 'classical',
        region: 'South Asia',
        framework: 'CULTURAL_DIFFUSION',
      },
      {
        id: 'ms-china-adopts',
        title: 'Chinese Mandate of Heaven',
        year: -1046,
        description:
          'The Zhou dynasty claims the "Mandate of Heaven" — divine right to rule based on virtue. ' +
          'Confucius later codifies social hierarchy: ruler/subject, father/son, husband/wife. ' +
          'Stratification becomes moral philosophy.',
        era: 'classical',
        region: 'East Asia',
        framework: 'DOCTRINE_DEVELOPMENT',
      },
      {
        id: 'ms-rome-adopts',
        title: 'Roman Class System',
        year: -509,
        description:
          'Rome institutionalizes patricians vs plebeians, senators vs equestrians, citizens vs slaves. ' +
          'Roman law (Twelve Tables) codifies class difference. This legal framework shapes Western ' +
          'civilization through medieval feudalism to modern capitalism.',
        era: 'classical',
        region: 'Southern Europe',
        framework: 'LEGAL_INTERPRETATION',
      },
      {
        id: 'ms-universal',
        title: 'Universal Pattern of Stratification',
        year: 500,
        description:
          'By 500 CE, every major civilization on Earth — Mesoamerican, Sub-Saharan African, Southeast Asian — ' +
          'has independently developed or adopted social stratification. The Sumerian template proves universal: ' +
          'surplus → specialization → hierarchy → law → permanence.',
        era: 'medieval',
        region: 'Global',
        framework: 'CULTURAL_DIFFUSION',
      },
    ],
    edges: [
      { source: 'ms-irrigation', target: 'ms-surplus', verb: 'CAUSES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Scott 2017', description: 'Controlled farming creates food excess' },
      { source: 'ms-surplus', target: 'ms-temples', verb: 'ENABLES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Nissen 1988', description: 'Surplus frees people from farming, creating specialist classes' },
      { source: 'ms-temples', target: 'ms-writing', verb: 'TRIGGERS', framework: 'TEXTUAL_TRANSMISSION', evidence: 'A: Schmandt-Besserat 1996', description: 'Temple accounting needs drive invention of writing' },
      { source: 'ms-surplus', target: 'ms-kingship', verb: 'ENABLES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Postgate 1992', description: 'Control of surplus enables permanent political power' },
      { source: 'ms-writing', target: 'ms-hammurabi', verb: 'ENABLES', framework: 'LEGAL_INTERPRETATION', evidence: 'B: Roth 1997', description: 'Written law requires literacy technology' },
      { source: 'ms-kingship', target: 'ms-hammurabi', verb: 'CAUSES', framework: 'LEGAL_INTERPRETATION', evidence: 'B: Van De Mieroop 2005', description: 'Royal authority codifies social order into law' },
      { source: 'ms-surplus', target: 'ms-egypt-adopts', verb: 'INFLUENCES', framework: 'CULTURAL_DIFFUSION', evidence: 'B: Trigger 2003', description: 'Nile surplus produces parallel stratification' },
      { source: 'ms-surplus', target: 'ms-indus-adopts', verb: 'INFLUENCES', framework: 'CULTURAL_DIFFUSION', evidence: 'B: Kenoyer 1998', description: 'Agricultural surplus enables Indus hierarchy' },
      { source: 'ms-hammurabi', target: 'ms-china-adopts', verb: 'IS_ANTECEDENT_TO', framework: 'TEMPORAL_LINKAGE', evidence: 'B: Creel 1970', description: 'Similar pattern independently emerges in China' },
      { source: 'ms-hammurabi', target: 'ms-rome-adopts', verb: 'INFLUENCES', framework: 'LEGAL_INTERPRETATION', evidence: 'B: Watson 1995', description: 'Near Eastern legal traditions reach Mediterranean' },
      { source: 'ms-rome-adopts', target: 'ms-universal', verb: 'ENABLES', framework: 'CULTURAL_DIFFUSION', evidence: 'B: Trigger 2003', description: 'Roman template spreads through empire and successors' },
      { source: 'ms-egypt-adopts', target: 'ms-universal', verb: 'ENABLES', framework: 'CULTURAL_DIFFUSION', evidence: 'B: Trigger 2003', description: 'Egyptian model influences Africa and Mediterranean' },
    ],
  },

  /* ═══════════════════════════════════════════════════════════
   * CASE STUDY 5: The Great Oceania Migration
   * Austronesian expansion — the greatest maritime migration in history
   * Frameworks: CAUSE_AND_EFFECT, ADAPTATION, CULTURAL_DIFFUSION
   * ═══════════════════════════════════════════════════════════ */
  {
    id: 'oceania-migration',
    title: 'The Great Oceania Migration',
    subtitle: 'How Austronesian Peoples Colonized Half the Planet by Canoe',
    description:
      'Between 3000 BCE and 1200 CE, Austronesian-speaking peoples spread from Taiwan across 15,000 km of open ocean — ' +
      'to the Philippines, Indonesia, Madagascar, and every island in the Pacific. They navigated by stars, swells, and bird flights, ' +
      'without compass or charts. It is the greatest maritime migration in human history.',
    era: 'prehistoric',
    region: 'Oceania',
    frameworks: ['CAUSE_AND_EFFECT', 'ADAPTATION', 'CULTURAL_DIFFUSION'],
    keyInsight:
      'The Austronesian expansion was not random wandering — it was systematic colonization driven by population pressure, ' +
      'outrigger canoe technology, and a cultural imperative to settle new lands. They carried a "transported landscape" ' +
      '(taro, breadfruit, pigs, chickens) that allowed them to colonize any tropical island.',
    nodes: [
      {
        id: 'om-taiwan',
        title: 'Proto-Austronesians in Taiwan',
        year: -3000,
        description:
          'Linguistic and genetic evidence traces all Austronesian peoples to Taiwan. ' +
          'Population growth and competition for arable land push groups to build boats and explore southward.',
        era: 'prehistoric',
        region: 'East Asia',
        framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'om-outrigger',
        title: 'Outrigger Canoe Innovation',
        year: -2500,
        description:
          'The outrigger canoe — a hull with a stabilizing float — allows open-ocean sailing. ' +
          'Later, the double-hulled voyaging canoe can carry 60+ people, animals, and crops across thousands of km.',
        era: 'prehistoric',
        region: 'Southeast Asia',
        framework: 'ADAPTATION',
      },
      {
        id: 'om-philippines',
        title: 'Settlement of the Philippines',
        year: -2000,
        description:
          'Austronesian settlers reach the Philippines, bringing rice agriculture, pigs, and pottery. ' +
          'They develop the "transported landscape" — a portable ecosystem that sustains colonization.',
        era: 'prehistoric',
        region: 'Southeast Asia',
        framework: 'CULTURAL_DIFFUSION',
      },
      {
        id: 'om-indonesia',
        title: 'Expansion Through Indonesia',
        year: -1500,
        description:
          'Austronesian speakers spread across the Indonesian archipelago (17,000 islands). ' +
          'They absorb or displace earlier Papuan-speaking populations. Maritime trade networks form.',
        era: 'prehistoric',
        region: 'Southeast Asia',
        framework: 'CULTURAL_DIFFUSION',
      },
      {
        id: 'om-lapita',
        title: 'Lapita Culture Reaches Melanesia',
        year: -1350,
        description:
          'The Lapita people — Austronesians with distinctive ceramic art — reach Papua New Guinea, ' +
          'Solomon Islands, Vanuatu, New Caledonia, and Fiji. Their pottery is the archaeological fingerprint ' +
          'of exploration.',
        era: 'prehistoric',
        region: 'Oceania',
        framework: 'CULTURAL_DIFFUSION',
      },
      {
        id: 'om-navigation',
        title: 'Polynesian Wayfinding System',
        year: -1000,
        description:
          'Polynesians develop the most sophisticated non-instrument navigation ever created: star compasses, ' +
          'ocean swell patterns, cloud formations, bird migration routes, phosphorescent plankton. ' +
          'This knowledge is memorized and transmitted orally, navigator to navigator.',
        era: 'classical',
        region: 'Oceania',
        framework: 'ADAPTATION',
      },
      {
        id: 'om-tonga-samoa',
        title: 'Settlement of Tonga & Samoa',
        year: -900,
        description:
          'Tonga and Samoa become the "cradle of Polynesia." Here, Polynesian culture, language, and social ' +
          'structures crystallize over centuries before the next wave of exploration eastward.',
        era: 'classical',
        region: 'Oceania',
        framework: 'CULTURAL_DIFFUSION',
      },
      {
        id: 'om-madagascar',
        title: 'Austronesians Reach Madagascar',
        year: 500,
        description:
          'Austronesian sailors cross 6,400 km of open Indian Ocean from Indonesia to Madagascar — ' +
          'the longest open-ocean crossing in pre-modern history. Malagasy language is Austronesian, not African. ' +
          'They carry rice, bananas, and the outrigger canoe tradition.',
        era: 'medieval',
        region: 'East Africa',
        framework: 'ADAPTATION',
      },
      {
        id: 'om-hawaii',
        title: 'Discovery of Hawai\'i',
        year: 800,
        description:
          'Polynesian voyagers discover Hawai\'i — 3,800 km from the nearest inhabited island. ' +
          'They navigate by the star Arcturus (Hōkūleʻa). Double-hulled canoes carry 30-60 settlers ' +
          'with taro, sweet potato, chickens, and pigs.',
        era: 'medieval',
        region: 'Oceania',
        framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'om-easter-island',
        title: 'Rapa Nui (Easter Island) Settled',
        year: 1000,
        description:
          'The most remote inhabited island on Earth — 3,500 km from South America. ' +
          'Polynesian settlers build the famous moai statues. They also reach South America, ' +
          'bringing back the sweet potato (genetic evidence confirms pre-Columbian contact).',
        era: 'medieval',
        region: 'Oceania',
        framework: 'ADAPTATION',
      },
      {
        id: 'om-aotearoa',
        title: 'Settlement of Aotearoa (New Zealand)',
        year: 1250,
        description:
          'The last major landmass to be settled by humans. Polynesian Māori arrive from eastern Polynesia. ' +
          'New Zealand\'s temperate climate forces adaptation: kumara (sweet potato) replaces taro, ' +
          'hunting replaces fishing as primary protein source.',
        era: 'medieval',
        region: 'Oceania',
        framework: 'ADAPTATION',
      },
    ],
    edges: [
      { source: 'om-taiwan', target: 'om-outrigger', verb: 'TRIGGERS', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Bellwood 2017', description: 'Population pressure drives maritime technology' },
      { source: 'om-outrigger', target: 'om-philippines', verb: 'ENABLES', framework: 'ADAPTATION', evidence: 'B: Bellwood 2017', description: 'Canoe technology enables island-hopping' },
      { source: 'om-philippines', target: 'om-indonesia', verb: 'ENABLES', framework: 'CULTURAL_DIFFUSION', evidence: 'B: Bellwood 2017', description: 'Colonization pattern repeats through archipelago' },
      { source: 'om-indonesia', target: 'om-lapita', verb: 'ENABLES', framework: 'CULTURAL_DIFFUSION', evidence: 'B: Kirch 2000', description: 'Expansion continues into Remote Oceania' },
      { source: 'om-lapita', target: 'om-navigation', verb: 'TRIGGERS', framework: 'ADAPTATION', evidence: 'B: Lewis 1972', description: 'Vast ocean distances require advanced navigation' },
      { source: 'om-lapita', target: 'om-tonga-samoa', verb: 'ENABLES', framework: 'CULTURAL_DIFFUSION', evidence: 'B: Kirch 2000', description: 'Lapita expands to Polynesian heartland' },
      { source: 'om-tonga-samoa', target: 'om-hawaii', verb: 'ENABLES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Kirch 2012', description: 'Polynesian homeland launches northward voyages' },
      { source: 'om-tonga-samoa', target: 'om-easter-island', verb: 'ENABLES', framework: 'ADAPTATION', evidence: 'B: Hunt & Lipo 2011', description: 'Eastern Polynesian expansion reaches remotest island' },
      { source: 'om-tonga-samoa', target: 'om-aotearoa', verb: 'ENABLES', framework: 'ADAPTATION', evidence: 'B: Anderson 2014', description: 'Final Polynesian expansion reaches New Zealand' },
      { source: 'om-indonesia', target: 'om-madagascar', verb: 'ENABLES', framework: 'ADAPTATION', evidence: 'B: Beaujard 2012', description: 'Indonesian sailors cross Indian Ocean to Africa' },
      { source: 'om-navigation', target: 'om-hawaii', verb: 'ENABLES', framework: 'ADAPTATION', evidence: 'B: Finney 1994', description: 'Star navigation enables discovery of remote islands' },
    ],
  },

  /* ═══════════════════════════════════════════════════════════
   * CASE STUDY 6: The Mansa Musa Effect
   * How Mali's golden emperor reshaped global trade and perception of Africa
   * Frameworks: CAUSE_AND_EFFECT, CULTURAL_DIFFUSION, GEOPOLITICAL_LINKAGE
   * ═══════════════════════════════════════════════════════════ */
  {
    id: 'mansa-musa-effect',
    title: 'The Mansa Musa Effect',
    subtitle: 'How Africa\'s Golden Emperor Reshaped Global Trade',
    description:
      'Mansa Musa of Mali (r. 1312–1337) was likely the wealthiest person in human history. His 1324 hajj to Mecca — ' +
      'with 60,000 men, 12,000 slaves, and 80 camels carrying 300 pounds of gold each — crashed gold prices across ' +
      'the Mediterranean. This case traces how Saharan gold, trans-Saharan trade, and Islamic scholarship converged ' +
      'to create an African superpower that European cartographers couldn\'t ignore.',
    era: 'medieval',
    region: 'West Africa',
    frameworks: ['CAUSE_AND_EFFECT', 'CULTURAL_DIFFUSION', 'GEOPOLITICAL_LINKAGE'],
    keyInsight:
      'European maps after Musa\'s pilgrimage placed Mali prominently — the 1375 Catalan Atlas shows him holding ' +
      'a gold nugget. Africa wasn\'t "discovered" by Europeans; it had been a center of wealth and learning for centuries. ' +
      'The narrative of African backwardness is a colonial invention that erases Timbuktu, Ghana, and Mali.',
    nodes: [
      {
        id: 'mm-ghana',
        title: 'Kingdom of Ghana Controls Gold Trade',
        year: 750,
        description:
          'The Soninke kingdom of Ghana (not modern Ghana) controls trans-Saharan gold and salt trade. ' +
          'Arab geographers call it "the land of gold." Taxation of trade creates enormous state wealth.',
        era: 'medieval', region: 'West Africa', framework: 'GEOPOLITICAL_LINKAGE',
      },
      {
        id: 'mm-almoravid',
        title: 'Almoravid Conquest Weakens Ghana',
        year: 1076,
        description:
          'Berber Almoravids from the north weaken Ghana\'s dominance, disrupting trade networks. ' +
          'Power vacuum opens space for successor states.',
        era: 'medieval', region: 'West Africa', framework: 'CONFLICT_AND_RESOLUTION',
      },
      {
        id: 'mm-sundiata',
        title: 'Sundiata Keita Founds Mali Empire',
        year: 1235,
        description:
          'Sundiata defeats the Sosso at the Battle of Kirina, founding the Mali Empire. ' +
          'The Manden Charter (Kurukan Fuga) establishes governance principles including free speech and abolition of slavery.',
        era: 'medieval', region: 'West Africa', framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'mm-gold-mines',
        title: 'Mali Controls Sub-Saharan Gold Mines',
        year: 1280,
        description:
          'Mali controls the Bambuk and Bure goldfields — producing roughly half of the Old World\'s gold supply. ' +
          'Gold flows north across the Sahara in exchange for salt, textiles, and horses.',
        era: 'medieval', region: 'West Africa', framework: 'GEOPOLITICAL_LINKAGE',
      },
      {
        id: 'mm-musa-reign',
        title: 'Mansa Musa Ascends to Throne',
        year: 1312,
        description:
          'Musa becomes emperor of Mali, inheriting an empire spanning modern Mali, Senegal, Gambia, Guinea, ' +
          'Mauritania, and parts of Niger. Population: ~20 million.',
        era: 'medieval', region: 'West Africa', framework: 'TEMPORAL_LINKAGE',
      },
      {
        id: 'mm-hajj',
        title: 'Musa\'s Golden Hajj to Mecca',
        year: 1324,
        description:
          '60,000 men, 12,000 slaves in silk, 80 camels with 300 lbs of gold each. Musa\'s caravan crosses ' +
          'the Sahara and stops in Cairo, where his lavish spending crashes gold prices for a decade.',
        era: 'medieval', region: 'North Africa', framework: 'CULTURAL_DIFFUSION',
      },
      {
        id: 'mm-timbuktu',
        title: 'Timbuktu Becomes a Center of Learning',
        year: 1330,
        description:
          'Musa commissions the Djinguereber Mosque and University of Sankore. Timbuktu houses 700,000 manuscripts — ' +
          'making it one of the world\'s great centers of Islamic scholarship, mathematics, and jurisprudence.',
        era: 'medieval', region: 'West Africa', framework: 'CULTURAL_DIFFUSION',
      },
      {
        id: 'mm-catalan-atlas',
        title: 'Catalan Atlas Features Mansa Musa',
        year: 1375,
        description:
          'Abraham Cresques\' Catalan Atlas — the most important map of the late medieval period — depicts ' +
          'Mansa Musa seated on a throne holding a gold nugget. Africa enters European geographic consciousness.',
        era: 'medieval', region: 'Western Europe', framework: 'CULTURAL_DIFFUSION',
      },
    ],
    edges: [
      { source: 'mm-ghana', target: 'mm-almoravid', verb: 'PRECEDES', framework: 'TEMPORAL_LINKAGE', evidence: 'B: Levtzion 1973', description: 'Ghana\'s wealth attracts conquerers' },
      { source: 'mm-almoravid', target: 'mm-sundiata', verb: 'ENABLES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Niane 1965', description: 'Ghana\'s fall creates power vacuum for Mali' },
      { source: 'mm-sundiata', target: 'mm-gold-mines', verb: 'ENABLES', framework: 'GEOPOLITICAL_LINKAGE', evidence: 'B: Levtzion 1973', description: 'Mali\'s expansion captures goldfields' },
      { source: 'mm-gold-mines', target: 'mm-musa-reign', verb: 'ENABLES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Gomez 2018', description: 'Gold wealth funds imperial administration' },
      { source: 'mm-musa-reign', target: 'mm-hajj', verb: 'TRIGGERS', framework: 'CAUSE_AND_EFFECT', evidence: 'A: al-Umari 1340', description: 'Emperor fulfills Islamic duty with unprecedented display' },
      { source: 'mm-hajj', target: 'mm-timbuktu', verb: 'TRIGGERS', framework: 'CULTURAL_DIFFUSION', evidence: 'B: Hunwick 1999', description: 'Musa brings back scholars and architects from Mecca' },
      { source: 'mm-hajj', target: 'mm-catalan-atlas', verb: 'CAUSES', framework: 'CULTURAL_DIFFUSION', evidence: 'B: Crone 1937', description: 'European awareness of Mali transforms cartography' },
      { source: 'mm-gold-mines', target: 'mm-hajj', verb: 'ENABLES', framework: 'GEOPOLITICAL_LINKAGE', evidence: 'B: Gomez 2018', description: 'Gold wealth makes the display possible' },
    ],
  },

  /* ═══════════════════════════════════════════════════════════
   * CASE STUDY 7: The Maya Collapse
   * What happened to one of the Americas' greatest civilizations?
   * Frameworks: CAUSE_AND_EFFECT, ADAPTATION, CONFLICT_AND_RESOLUTION
   * ═══════════════════════════════════════════════════════════ */
  {
    id: 'maya-collapse',
    title: 'The Maya Collapse',
    subtitle: 'What Destroyed One of the Americas\' Greatest Civilizations?',
    description:
      'Between 800 and 1000 CE, the Classic Maya civilization — builders of Tikal, Palenque, and Copán — ' +
      'experienced a catastrophic collapse. Populations dropped 90%, cities were abandoned, and monumental construction stopped. ' +
      'The causes remain debated, but the best evidence points to a devastating cycle of drought, overpopulation, ' +
      'deforestation, warfare, and political fragmentation.',
    era: 'medieval',
    region: 'Americas',
    frameworks: ['CAUSE_AND_EFFECT', 'ADAPTATION', 'CONFLICT_AND_RESOLUTION'],
    keyInsight:
      'The Maya didn\'t "vanish" — 6 million Maya people live today. What collapsed was their political system and urban centers. ' +
      'The Classic Maya collapse is a case study in how environmental stress + political rigidity + inequality = civilizational failure. ' +
      'It carries urgent lessons for modern climate change.',
    nodes: [
      {
        id: 'mc-classic',
        title: 'Classic Maya Golden Age',
        year: 250,
        description:
          'Maya civilization reaches its zenith: Tikal, Calakmul, Palenque, and Copán flourish. ' +
          'Population reaches 10–15 million. Advanced writing, astronomy, mathematics (concept of zero), and monumental architecture.',
        era: 'ancient', region: 'Americas', framework: 'TEMPORAL_LINKAGE',
      },
      {
        id: 'mc-population',
        title: 'Population Pressure Intensifies',
        year: 700,
        description:
          'Rapid population growth outstrips sustainable agriculture. Slash-and-burn farming exhausts tropical soils. ' +
          'Maya cities grow denser, requiring more food from increasingly degraded land.',
        era: 'medieval', region: 'Americas', framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'mc-deforestation',
        title: 'Massive Deforestation',
        year: 750,
        description:
          'Pollen cores show 95% forest clearance around major cities. Limestone plaster for temples required ' +
          'burning enormous quantities of wood. Deforestation increased soil erosion and reduced rainfall.',
        era: 'medieval', region: 'Americas', framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'mc-drought',
        title: 'Megadroughts Strike the Yucatán',
        year: 810,
        description:
          'Stalagmite and lake sediment records show severe droughts in 810, 860, and 910 CE — the driest period ' +
          'in 7,000 years. Deforestation likely worsened drought by disrupting local water cycles.',
        era: 'medieval', region: 'Americas', framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'mc-warfare',
        title: 'Inter-City Warfare Escalates',
        year: 800,
        description:
          'As resources shrink, warfare intensifies. Calakmul vs. Tikal conflicts escalate from ritual combat ' +
          'to total war. Captive sacrifice increases. Trade networks fracture.',
        era: 'medieval', region: 'Americas', framework: 'CONFLICT_AND_RESOLUTION',
      },
      {
        id: 'mc-elite-failure',
        title: 'Political Elite Lose Legitimacy',
        year: 850,
        description:
          'Divine kings who claimed to control rain and harvests cannot deliver. Monumental construction stops. ' +
          'Last dated stelae appear at city after city. The social contract between rulers and ruled breaks down.',
        era: 'medieval', region: 'Americas', framework: 'CAUSE_AND_EFFECT',
      },
      {
        id: 'mc-abandonment',
        title: 'Cities Abandoned',
        year: 900,
        description:
          'By 900 CE, most major southern lowland cities are abandoned. Population drops 90%. ' +
          'The jungle reclaims Tikal, Palenque, and Copán. Survivors migrate north to Chichén Itzá and coastal areas.',
        era: 'medieval', region: 'Americas', framework: 'ADAPTATION',
      },
      {
        id: 'mc-post-classic',
        title: 'Post-Classic Maya Adaptation',
        year: 1000,
        description:
          'Maya civilization doesn\'t end — it adapts. Northern Yucatán cities like Chichén Itzá and Mayapan flourish. ' +
          'Coastal trade replaces inland agriculture. The Maya survive, but the Classic political system is gone forever.',
        era: 'medieval', region: 'Americas', framework: 'ADAPTATION',
      },
    ],
    edges: [
      { source: 'mc-classic', target: 'mc-population', verb: 'CAUSES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Webster 2002', description: 'Success drives population growth beyond carrying capacity' },
      { source: 'mc-population', target: 'mc-deforestation', verb: 'CAUSES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Lentz et al. 2014', description: 'More people require more farmland and fuel' },
      { source: 'mc-deforestation', target: 'mc-drought', verb: 'AMPLIFIES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Medina-Elizalde & Rohling 2012', description: 'Forest loss disrupts local rainfall patterns' },
      { source: 'mc-drought', target: 'mc-warfare', verb: 'TRIGGERS', framework: 'CONFLICT_AND_RESOLUTION', evidence: 'B: Kennett et al. 2012', description: 'Scarcity drives competition between city-states' },
      { source: 'mc-warfare', target: 'mc-elite-failure', verb: 'CAUSES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Demarest 2004', description: 'Endless war delegitimizes divine kingship' },
      { source: 'mc-elite-failure', target: 'mc-abandonment', verb: 'TRIGGERS', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Webster 2002', description: 'Without political order, urban life becomes unsustainable' },
      { source: 'mc-abandonment', target: 'mc-post-classic', verb: 'ENABLES', framework: 'ADAPTATION', evidence: 'B: Masson & Freidel 2012', description: 'Survivors rebuild in more sustainable locations' },
      { source: 'mc-population', target: 'mc-warfare', verb: 'AMPLIFIES', framework: 'CONFLICT_AND_RESOLUTION', evidence: 'B: Webster 2002', description: 'Population pressure increases inter-city competition' },
    ],
  },

  /* ═══════════════════════════════════════════════════════════
   * CASE STUDY 8: The Silk Road's Cultural Highway
   * How trade routes transmitted ideas, religions, and technologies
   * Frameworks: CULTURAL_DIFFUSION, TEXTUAL_TRANSMISSION, GEOPOLITICAL_LINKAGE
   * ═══════════════════════════════════════════════════════════ */
  {
    id: 'silk-road-culture',
    title: 'The Silk Road\'s Cultural Highway',
    subtitle: 'How Trade Routes Transmitted Ideas, Religions, and Technologies',
    description:
      'The Silk Road wasn\'t just about silk. For 1,500 years, it served as the primary conduit for ideas, religions, ' +
      'technologies, and languages between East and West. Buddhism traveled from India to China. Islam spread from Arabia ' +
      'to Central Asia. Paper moved from China to Europe. The Silk Road was the internet of the ancient world.',
    era: 'ancient',
    region: 'Central Asia',
    frameworks: ['CULTURAL_DIFFUSION', 'TEXTUAL_TRANSMISSION', 'GEOPOLITICAL_LINKAGE'],
    keyInsight:
      'Goods were the excuse — ideas were the payload. Every caravan that carried silk and spices also carried ' +
      'missionaries, manuscripts, artistic motifs, and mathematical concepts. The Silk Road proves that trade ' +
      'is the most powerful vehicle for cultural exchange in human history.',
    nodes: [
      {
        id: 'sr-han',
        title: 'Han Dynasty Opens Western Trade',
        year: -130,
        description:
          'Zhang Qian\'s diplomatic missions to Central Asia establish regular trade routes. Chinese silk reaches ' +
          'Rome, where it becomes a luxury obsession. The "Silk Road" name comes from German geographer Richthofen (1877).',
        era: 'ancient', region: 'East Asia', framework: 'GEOPOLITICAL_LINKAGE',
      },
      {
        id: 'sr-buddhism-spread',
        title: 'Buddhism Travels the Silk Road',
        year: 100,
        description:
          'Buddhist monks and merchants carry the dharma from Gandhara (modern Pakistan/Afghanistan) along trade ' +
          'routes to Central Asia and China. The Kushan Empire facilitates this — Gandharan art fuses Greek and Indian styles.',
        era: 'ancient', region: 'Central Asia', framework: 'CULTURAL_DIFFUSION',
      },
      {
        id: 'sr-paper',
        title: 'Chinese Papermaking Reaches West',
        year: 751,
        description:
          'At the Battle of Talas (751), Arab forces capture Chinese papermakers. Within decades, paper mills ' +
          'appear in Samarkand, Baghdad, Cairo, and eventually Spain. Paper replaces papyrus and parchment, enabling the Islamic Golden Age.',
        era: 'medieval', region: 'Central Asia', framework: 'TEXTUAL_TRANSMISSION',
      },
      {
        id: 'sr-islam-spread',
        title: 'Islam Spreads Along Trade Routes',
        year: 800,
        description:
          'Muslim merchants carry Islam to Central Asia, the Malay Archipelago, and East Africa. ' +
          'Unlike Christianity\'s imperial spread, Islam often followed trade — merchants were missionaries.',
        era: 'medieval', region: 'Central Asia', framework: 'CULTURAL_DIFFUSION',
      },
      {
        id: 'sr-mathematics',
        title: 'Indian Mathematics Enters the Islamic World',
        year: 820,
        description:
          'Al-Khwarizmi translates Indian numerals and the concept of zero into Arabic at Baghdad\'s House of Wisdom. ' +
          'His work "al-jabr" gives us the word "algebra." These concepts later reach Europe.',
        era: 'medieval', region: 'West Asia', framework: 'TEXTUAL_TRANSMISSION',
      },
      {
        id: 'sr-mongol-pax',
        title: 'Pax Mongolica Unifies the Road',
        year: 1260,
        description:
          'The Mongol Empire creates the safest trade corridor in Silk Road history. Marco Polo, Ibn Battuta, ' +
          'and countless merchants traverse the entire route. Ideas, technologies, and diseases flow freely.',
        era: 'medieval', region: 'Central Asia', framework: 'GEOPOLITICAL_LINKAGE',
      },
      {
        id: 'sr-gunpowder',
        title: 'Gunpowder Reaches Europe',
        year: 1280,
        description:
          'Chinese gunpowder technology — originally used for fireworks — travels west through Mongol armies ' +
          'and Arab merchants. By 1350, European cannon transform siege warfare and end the age of castles.',
        era: 'medieval', region: 'Western Europe', framework: 'CULTURAL_DIFFUSION',
      },
      {
        id: 'sr-plague',
        title: 'Black Death Travels the Silk Road',
        year: 1347,
        description:
          'Yersinia pestis bacteria follow trade routes from Central Asia to the Black Sea, then to Europe. ' +
          'The Silk Road\'s greatest unintended cargo: a pandemic that kills 30-60% of Europe\'s population.',
        era: 'medieval', region: 'Central Asia', framework: 'CAUSE_AND_EFFECT',
      },
    ],
    edges: [
      { source: 'sr-han', target: 'sr-buddhism-spread', verb: 'ENABLES', framework: 'CULTURAL_DIFFUSION', evidence: 'B: Liu 2010', description: 'Trade infrastructure provides routes for religious transmission' },
      { source: 'sr-buddhism-spread', target: 'sr-paper', verb: 'PRECEDES', framework: 'TEMPORAL_LINKAGE', evidence: 'B: Hansen 2012', description: 'Buddhist scribal culture creates demand for writing materials' },
      { source: 'sr-paper', target: 'sr-mathematics', verb: 'ENABLES', framework: 'TEXTUAL_TRANSMISSION', evidence: 'B: Bloom 2001', description: 'Paper makes mathematical texts widely reproducible' },
      { source: 'sr-islam-spread', target: 'sr-mathematics', verb: 'ENABLES', framework: 'CULTURAL_DIFFUSION', evidence: 'B: Saliba 2007', description: 'Islamic scholarly networks translate and advance Indian math' },
      { source: 'sr-han', target: 'sr-mongol-pax', verb: 'PRECEDES', framework: 'TEMPORAL_LINKAGE', evidence: 'B: Frankopan 2015', description: 'Han routes form the infrastructure Mongols later unify' },
      { source: 'sr-mongol-pax', target: 'sr-gunpowder', verb: 'ENABLES', framework: 'CULTURAL_DIFFUSION', evidence: 'B: May 2012', description: 'Mongol conquest accelerates gunpowder transmission' },
      { source: 'sr-mongol-pax', target: 'sr-plague', verb: 'ENABLES', framework: 'CAUSE_AND_EFFECT', evidence: 'B: Aberth 2011', description: 'United trade routes become disease superhighways' },
      { source: 'sr-mathematics', target: 'sr-gunpowder', verb: 'PRECEDES', framework: 'TEMPORAL_LINKAGE', evidence: 'B: Frankopan 2015', description: 'Intellectual exchange precedes military technology transfer' },
    ],
  },
]
