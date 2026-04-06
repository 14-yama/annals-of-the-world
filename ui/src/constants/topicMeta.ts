/**
 * Topic Metadata — lightweight display config for civilization-shaping topics.
 * No entity arrays — purely route, icon, color, and description.
 */
export interface TopicMeta {
  slug: string
  name: string
  shortName: string
  description: string
  color: string
  icon: string
  route: string
}

export const TOPIC_META: TopicMeta[] = [
  { slug: 'weapons', name: 'Arms & Warfare', shortName: 'Weapons', description: 'From stone axes to hypersonic missiles — every weapon that shaped the battlefield.', color: '#8B3A3A', icon: 'Swords', route: '/weapons' },
  { slug: 'medicine', name: 'Medicine & Healing', shortName: 'Medicine', description: 'From herbal remedies to gene therapy — the medical breakthroughs that extended human life.', color: '#2F855A', icon: 'Heart', route: '/medicine' },
  { slug: 'architecture', name: 'Architecture & Monuments', shortName: 'Architecture', description: "From Göbekli Tepe to parametric skyscrapers — humanity's built environment.", color: '#C5963A', icon: 'Building2', route: '/architecture' },
  { slug: 'agriculture', name: 'Agriculture & Food', shortName: 'Agriculture', description: 'From wild grain gathering to vertical farms — how we learned to feed 8 billion.', color: '#38A169', icon: 'Wheat', route: '/agriculture' },
  { slug: 'navigation', name: 'Navigation & Exploration', shortName: 'Navigation', description: 'From star-guided canoes to GPS satellites — charting the unknown.', color: '#3182CE', icon: 'Compass', route: '/navigation' },
  { slug: 'languages', name: 'Languages & Scripts', shortName: 'Languages', description: 'From cave paintings to Unicode — the evolution of human communication.', color: '#6B3FA0', icon: 'BookOpen', route: '/languages' },
  { slug: 'tribes', name: 'Tribes & Peoples', shortName: 'Tribes', description: 'From the San Bushmen to the Mongol hordes — every tribe that shaped human history.', color: '#8B6914', icon: 'Users', route: '/tribes' },
  { slug: 'transportation', name: 'Transportation', shortName: 'Transport', description: 'From dugout canoes to spacecraft — every breakthrough in human mobility.', color: '#3182CE', icon: 'TrainFront', route: '/transportation' },
  { slug: 'clothing', name: 'Clothing & Textiles', shortName: 'Clothing', description: 'From animal hides to smart fabrics — every fiber and fashion revolution.', color: '#9B2C6E', icon: 'Shirt', route: '/clothing' },
  { slug: 'marriage', name: 'Marriage & Union', shortName: 'Marriage', description: 'From pair bonding to same-sex marriage — every form of union across 12,000 years.', color: '#C53D6E', icon: 'Heart', route: '/marriage' },
  { slug: 'customs', name: 'Customs & Traditions', shortName: 'Customs', description: 'From burial rites to digital etiquette — the rituals and social rules that defined civilizations.', color: '#B8860B', icon: 'Crown', route: '/customs' },
  { slug: 'punishment', name: 'Corporal Punishment & Justice', shortName: 'Punishment', description: 'From blood feud to restorative justice — how civilizations punished and reformed.', color: '#B22222', icon: 'Gavel', route: '/punishment' },
  { slug: 'ideas', name: 'Ideas & Thought', shortName: 'Ideas', description: 'From animism to artificial intelligence — the transformative ideas that reshaped civilization across every era.', color: '#6B3FA0', icon: 'Lightbulb', route: '/ideas' },
]

export function getTopicMeta(slug: string): TopicMeta | undefined {
  return TOPIC_META.find(t => t.slug === slug)
}
