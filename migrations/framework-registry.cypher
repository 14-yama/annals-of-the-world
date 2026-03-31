// =============================================================
//  Annals of the World — Framework Registry
//  Version: v4 + v5-ready (2025)
//  Author: Curator System
//  Purpose: Seed canonical interpretive frameworks as first-class nodes.
// =============================================================

// ---------- v4 Core Frameworks (historian frameworks) ----------
UNWIND [
  {
    code:'CAUSE_EFFECT',
    name:'Cause & Effect',
    category:'Causation',
    definition:'Direct causal linkage between events, actions, or conditions.',
    notes:'Used to model cause–effect relationships (e.g., Reformation → CAUSED → Counter-Reformation).'
  },
  {
    code:'CONTINUITY_CHANGE',
    name:'Continuity & Change',
    category:'Temporality',
    definition:'Tracks persistence and transformation across time.',
    notes:'Shows how structures, ideas, or institutions evolve or remain stable.'
  },
  {
    code:'CULTURAL_DIFFUSION',
    name:'Cultural Diffusion',
    category:'Exchange',
    definition:'Spread of ideas, practices, or technologies between societies or regions.',
    notes:'E.g., Buddhism → SPREAD_TO → China.'
  },
  {
    code:'PRECEDENT',
    name:'Precedent',
    category:'Influence',
    definition:'Earlier pattern or event shaping later developments.',
    notes:'E.g., Roman Law → PRECEDED → Napoleonic Code.'
  },
  {
    code:'SYMBOLISM',
    name:'Symbolism',
    category:'Meaning',
    definition:'Symbolic or representational significance in culture or religion.',
    notes:'E.g., The Cross → SYMBOLIZES → Redemption.'
  },
  {
    code:'INFLUENCE',
    name:'Influence',
    category:'Impact',
    definition:'Indirect or diffuse effect exerted by one entity on another.',
    notes:'E.g., Aristotle → INFLUENCES → Thomas Aquinas.'
  },
  {
    code:'CONFLICT',
    name:'Conflict',
    category:'Interaction',
    definition:'Opposition or tension driving change or resolution.',
    notes:'E.g., Church → OPPOSES → State.'
  },
  {
    code:'TEMPORAL_LINKAGE',
    name:'Temporal Linkage',
    category:'Chronology',
    definition:'Sequential or overlapping relation across time.',
    notes:'E.g., World War I → PRECEDED → World War II.'
  },
  {
    code:'GEOPOLITICAL_LINKAGE',
    name:'Geopolitical Linkage',
    category:'Space/Power',
    definition:'Connections between regions or powers through geography or political order.',
    notes:'E.g., Silk Road → CONNECTED → East and West.'
  },
  {
    code:'ADAPTATION',
    name:'Adaptation',
    category:'Reception',
    definition:'Reinterpretation or reuse of older ideas in new contexts.',
    notes:'E.g., Greek Philosophy → ADAPTED_BY → Early Christian Theology.'
  }
] AS fw
MERGE (f:Framework {code:fw.code})
SET
  f.name        = fw.name,
  f.category    = fw.category,
  f.definition  = fw.definition,
  f.notes       = fw.notes,
  f.created_at  = datetime(),
  f.created_by  = 'curator_system',
  f.version     = 4
;

// ---------- v5 Governance & Analytical Extensions ----------
UNWIND [
  {
    code:'POLICY_IMPLEMENTATION',
    name:'Policy Implementation',
    category:'Governance',
    definition:'Conversion of ideas or philosophies into formal policies or administrative action.',
    notes:'E.g., Universal Suffrage → IMPLEMENTED_IN → Reform Act.'
  },
  {
    code:'IDEA_EVOLUTION',
    name:'Idea Evolution',
    category:'Conceptual Development',
    definition:'Historical transformation or maturation of ideas across periods.',
    notes:'E.g., Feudalism → EVOLVED_INTO → Constitutional Monarchy.'
  },
  {
    code:'LEGAL_FOUNDATION',
    name:'Legal Foundation',
    category:'Law',
    definition:'Codification of principles within legal or constitutional frameworks.',
    notes:'E.g., Natural Rights → CODIFIED_INTO → Magna Carta.'
  },
  {
    code:'CULTURAL_TRANSMISSION',
    name:'Cultural Transmission',
    category:'Exchange',
    definition:'Transmission of values or ideas through art, education, or literature.',
    notes:'E.g., Humanism → TRANSMITTED_VIA → Renaissance Education.'
  },
  {
    code:'TECHNOLOGICAL_DISRUPTION',
    name:'Technological Disruption',
    category:'Innovation',
    definition:'Systemic change caused by technological advancement.',
    notes:'E.g., Printing Press → DISRUPTED → Church Authority.'
  },
  {
    code:'CONFLICT_RESOLUTION',
    name:'Conflict & Resolution',
    category:'Interaction',
    definition:'Reconciliation or outcome resulting from ideological or political struggle.',
    notes:'E.g., Civil Rights Movement → RESOLVED_BY → Voting Rights Act.'
  }
] AS fw
MERGE (f:Framework {code:fw.code})
SET
  f.name        = fw.name,
  f.category    = fw.category,
  f.definition  = fw.definition,
  f.notes       = fw.notes,
  f.created_at  = datetime(),
  f.created_by  = 'curator_system',
  f.version     = 5
;

// ---------- v6 Expanded Analytical Frameworks ----------
UNWIND [
  {
    code:'ECONOMIC_SYSTEMS',
    name:'Economic Systems',
    category:'Economics',
    definition:'Analyzes modes of production, trade networks, fiscal policy, monetary systems, and the material basis of civilizations.',
    notes:'Verbs: TRADES_WITH, PRODUCES, FINANCES, DISTRIBUTES. Related: CAUSE_AND_EFFECT, POLITICAL_SYSTEMS, INNOVATION_AND_TECHNOLOGY.'
  },
  {
    code:'POLITICAL_SYSTEMS',
    name:'Political Systems',
    category:'Governance',
    definition:'Examines structures of governance, sovereignty, statecraft, constitutionalism, and the evolution of political authority.',
    notes:'Verbs: GOVERNS, LEGISLATES, ADMINISTERS, DELEGATES. Related: LEGAL_INTERPRETATION, CONFLICT_AND_RESOLUTION, ECONOMIC_SYSTEMS.'
  },
  {
    code:'COMPARATIVE_RELIGION',
    name:'Comparative Religion',
    category:'Religion',
    definition:'Compares doctrines, practices, institutions, and histories across religious traditions to reveal shared patterns and distinct trajectories.',
    notes:'Verbs: COMPARES, SYNCRETIZES, DIFFERENTIATES, CONVERTS. Related: DOCTRINE_DEVELOPMENT, RITUAL_STANDARDIZATION, CULTURAL_DIFFUSION.'
  },
  {
    code:'EMPIRE_AND_COLONIALISM',
    name:'Empire & Colonialism',
    category:'Imperial History',
    definition:'Focuses on imperial expansion, colonial administration, resistance movements, decolonization, and postcolonial legacies.',
    notes:'Verbs: COLONIZES, ADMINISTERS, RESISTS, DECOLONIZES. Related: GEOPOLITICAL_LINKAGE, CONFLICT_AND_RESOLUTION, ECONOMIC_SYSTEMS.'
  },
  {
    code:'ENVIRONMENTAL_HISTORY',
    name:'Environmental History',
    category:'Environment',
    definition:'Examines the interaction between human societies and the natural environment: climate, ecology, resource use, and environmental change.',
    notes:'Verbs: EXPLOITS, CONSERVES, DEPLETES, ADAPTS_TO. Related: ADAPTATION, ECONOMIC_SYSTEMS, INNOVATION_AND_TECHNOLOGY.'
  },
  {
    code:'INNOVATION_AND_TECHNOLOGY',
    name:'Innovation & Technology',
    category:'Technology',
    definition:'Tracks invention, diffusion, and impact of technologies, engineering achievements, and scientific breakthroughs on societies.',
    notes:'Verbs: INVENTS, INNOVATES, DISRUPTS, MECHANIZES. Related: CAUSE_AND_EFFECT, ECONOMIC_SYSTEMS, CULTURAL_DIFFUSION.'
  }
] AS fw
MERGE (f:Framework {code:fw.code})
SET
  f.name        = fw.name,
  f.category    = fw.category,
  f.definition  = fw.definition,
  f.notes       = fw.notes,
  f.created_at  = datetime(),
  f.created_by  = 'curator_system',
  f.version     = 6
;

// ---------- Optional validation query ----------
MATCH (f:Framework)
RETURN f.code, f.name, f.category
ORDER BY f.code;
