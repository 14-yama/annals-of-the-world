/* ─── Ancient Trade Routes — Annals of the World ─── */
/* Major historical trade routes with coordinate paths for map visualization */

export interface TradeRoute {
  id: string
  name: string
  period: string
  era: string
  color: string
  description: string
  goods: string[]
  coordinates: [number, number][] // [lng, lat] pairs for polyline
}

export const TRADE_ROUTES: TradeRoute[] = [
  {
    id: 'silk-road',
    name: 'Silk Road',
    period: '200 BCE – 1450 CE',
    era: 'classical',
    color: '#C53030',
    description: 'The most famous overland trade route connecting China to the Mediterranean. Silk, spices, paper, and gunpowder flowed west; gold, glass, and wool flowed east.',
    goods: ['Silk', 'Spices', 'Paper', 'Gunpowder', 'Porcelain'],
    coordinates: [
      [116.4, 39.9], [109.9, 36.3], [103.8, 36.0], [98.5, 36.8], [93.5, 37.0],
      [87.6, 43.8], [75.0, 41.3], [69.3, 41.3], [66.9, 39.7], [58.4, 37.9],
      [51.4, 35.7], [44.4, 33.3], [36.3, 33.5], [35.5, 33.9], [29.0, 41.0],
    ],
  },
  {
    id: 'spice-route',
    name: 'Maritime Spice Route',
    period: '100 CE – 1600 CE',
    era: 'medieval',
    color: '#D69E2E',
    description: 'Sea route connecting the Spice Islands (Moluccas) to Europe via India, Arabia, and East Africa. Drove European Age of Exploration.',
    goods: ['Pepper', 'Cinnamon', 'Cloves', 'Nutmeg', 'Cardamom'],
    coordinates: [
      [127.4, -0.5], [110.0, -7.6], [104.0, -6.2], [98.6, 3.1], [80.2, 7.0],
      [73.0, 12.0], [55.0, 23.6], [45.0, 12.8], [43.1, 11.6], [39.5, 15.6],
      [32.5, 29.9], [29.9, 31.2],
    ],
  },
  {
    id: 'trans-saharan',
    name: 'Trans-Saharan Trade',
    period: '300 BCE – 1600 CE',
    era: 'classical',
    color: '#D4AF37',
    description: 'Camel caravans crossed the Sahara connecting sub-Saharan gold and salt mines to Mediterranean markets. Created the great empires of Mali, Songhai, and Ghana.',
    goods: ['Gold', 'Salt', 'Slaves', 'Ivory', 'Kola nuts'],
    coordinates: [
      [3.1, 36.7], [2.6, 32.0], [0.0, 27.0], [-1.0, 22.0], [-3.0, 17.0],
      [-4.0, 14.0], [-8.0, 12.6], [-8.0, 11.0],
    ],
  },
  {
    id: 'incense-route',
    name: 'Incense Route',
    period: '700 BCE – 200 CE',
    era: 'classical',
    color: '#805AD5',
    description: 'Connected the frankincense and myrrh producing regions of Southern Arabia (modern Yemen/Oman) to the Mediterranean civilizations. Worth more than gold.',
    goods: ['Frankincense', 'Myrrh', 'Spices', 'Textiles'],
    coordinates: [
      [49.0, 14.5], [45.8, 15.3], [44.2, 15.4], [39.8, 21.5],
      [36.6, 28.0], [34.8, 31.5], [35.5, 33.9],
    ],
  },
  {
    id: 'amber-road',
    name: 'Amber Road',
    period: '1600 BCE – 500 CE',
    era: 'classical',
    color: '#ED8936',
    description: 'Connected the Baltic Sea amber deposits to the Mediterranean. Amber was valued like gold in ancient Rome and Egypt.',
    goods: ['Amber', 'Furs', 'Honey', 'Roman goods'],
    coordinates: [
      [20.5, 54.7], [19.9, 50.1], [16.4, 48.2], [14.5, 46.1],
      [13.8, 45.6], [12.3, 45.4], [12.5, 41.9],
    ],
  },
  {
    id: 'austronesian-trade',
    name: 'Austronesian Maritime Network',
    period: '1500 BCE – 1400 CE',
    era: 'medieval',
    color: '#3182CE',
    description: 'The world\'s first transoceanic trade network connecting Madagascar to the Pacific Islands. Austronesian sailors traveled 15,000 km across open ocean.',
    goods: ['Obsidian', 'Pottery', 'Taro', 'Shell jewelry', 'Breadfruit'],
    coordinates: [
      [121.0, 23.0], [121.0, 14.6], [110.0, -7.6], [106.8, -6.2],
      [80.0, 7.0], [49.0, -18.9],
    ],
  },
  {
    id: 'tin-route',
    name: 'Tin Route (Bronze Age)',
    period: '2500 BCE – 800 BCE',
    era: 'classical',
    color: '#718096',
    description: 'Connected tin mines of Cornwall (Britain) and Iberia to bronze-making centers of the Eastern Mediterranean. Without tin, no bronze; without bronze, no Bronze Age empires.',
    goods: ['Tin', 'Copper', 'Bronze goods', 'Pottery'],
    coordinates: [
      [-5.5, 50.3], [-5.0, 47.0], [-1.5, 43.5], [0.0, 38.0],
      [3.0, 36.7], [10.0, 37.0], [15.0, 37.5], [24.0, 35.0],
      [29.0, 31.2], [32.5, 29.9],
    ],
  },
]
