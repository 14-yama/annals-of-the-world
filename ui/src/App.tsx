import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import Home from './pages/Home'
import AfricaDashboard from './pages/AfricaDashboard'
import AsiaDashboard from './pages/AsiaDashboard'
import EuropeDashboard from './pages/EuropeDashboard'
import AmericasDashboard from './pages/AmericasDashboard'
import OceaniaDashboard from './pages/OceaniaDashboard'
import EraExplorer from './pages/EraExplorer'
import EraDetail from './pages/EraDetail'
import QuizPage from './pages/QuizPage'
import CaseStudyExplorer from './pages/CaseStudyExplorer'
import HumanStory from './pages/HumanStory'
import Curator from './pages/Curator'
import WeaponsPage from './pages/WeaponsPage'
import IdeasPage from './pages/IdeasPage'
import About from './pages/About'
import EntityPage from './pages/EntityPage'
import CatalogPage from './pages/CatalogPage'
import GraphExplorer from './pages/GraphExplorer'

export default function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route path="/" element={<Home />} />
        <Route path="/continents/africa" element={<AfricaDashboard />} />
        <Route path="/continents/asia" element={<AsiaDashboard />} />
        <Route path="/continents/europe" element={<EuropeDashboard />} />
        <Route path="/continents/americas" element={<AmericasDashboard />} />
        <Route path="/continents/oceania" element={<OceaniaDashboard />} />
        <Route path="/explore" element={<EraExplorer />} />
        <Route path="/explore/:eraId" element={<EraDetail />} />
        <Route path="/quiz" element={<QuizPage />} />
        <Route path="/case-studies" element={<CaseStudyExplorer />} />
        <Route path="/human-story" element={<HumanStory />} />
        <Route path="/curator" element={<Curator />} />
        <Route path="/weapons" element={<WeaponsPage />} />
        <Route path="/ideas" element={<IdeasPage />} />
        <Route path="/graph" element={<GraphExplorer />} />
        <Route path="/about" element={<About />} />
        <Route path="/demo" element={<EntityPage />} />
        <Route path="/entity/:slug" element={<EntityPage />} />
        <Route path="/catalog" element={<CatalogPage />} />
        <Route path="/cat/:callNumber" element={<CatalogPage />} />
      </Route>
    </Routes>
  )
}
