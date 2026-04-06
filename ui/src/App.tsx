import React, { useEffect } from 'react'
import { Routes, Route, useLocation } from 'react-router-dom'
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
import LanguagesPage from './pages/LanguagesPage'
import ArchitecturePage from './pages/ArchitecturePage'
import MedicinePage from './pages/MedicinePage'
import AgriculturePage from './pages/AgriculturePage'
import NavigationPage from './pages/NavigationPage'
import TribesPage from './pages/TribesPage'
import TransportationPage from './pages/TransportationPage'
import ClothingPage from './pages/ClothingPage'
import MarriagePage from './pages/MarriagePage'
import CustomsPage from './pages/CustomsPage'
import PunishmentPage from './pages/PunishmentPage'
import IdeasPage from './pages/IdeasPage'
import About from './pages/About'
import EntityPage from './pages/EntityPage'
import CatalogPage from './pages/CatalogPage'
import GraphExplorer from './pages/GraphExplorer'
import BiblicalCorpusPage from './pages/BiblicalCorpusPage'
import CorpusPage from './pages/CorpusPage'
import CorpusHub from './pages/CorpusHub'
import TopicsHub from './pages/TopicsHub'
import DocsPage from './pages/DocsPage'
import AuditDashboard from './pages/curator/AuditDashboard'
import TriageSystem from './pages/curator/TriageSystem'
import PeopleHub from './pages/curator/PeopleHub'
import DivisionDetail from './pages/curator/DivisionDetail'
import AuditGuide from './pages/curator/AuditGuide'

/** Reset scroll to top on every route change */
function ScrollToTop() {
  const { pathname } = useLocation()
  useEffect(() => {
    window.scrollTo(0, 0)
    // Also scroll the main content container (Layout uses overflowY="auto")
    document.getElementById('main-content')?.scrollTo(0, 0)
  }, [pathname])
  return null
}

export default function App() {
  return (
    <>
      <ScrollToTop />
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
        <Route path="/curator/audit" element={<AuditDashboard />} />
        <Route path="/curator/triage" element={<TriageSystem />} />
        <Route path="/curator/people" element={<PeopleHub />} />
        <Route path="/curator/people/:div" element={<DivisionDetail />} />
        <Route path="/curator/audit/guide" element={<AuditGuide />} />
        <Route path="/weapons" element={<WeaponsPage />} />
        <Route path="/languages" element={<LanguagesPage />} />
        <Route path="/architecture" element={<ArchitecturePage />} />
        <Route path="/medicine" element={<MedicinePage />} />
        <Route path="/agriculture" element={<AgriculturePage />} />
        <Route path="/navigation" element={<NavigationPage />} />
        <Route path="/tribes" element={<TribesPage />} />
        <Route path="/transportation" element={<TransportationPage />} />
        <Route path="/clothing" element={<ClothingPage />} />
        <Route path="/marriage" element={<MarriagePage />} />
        <Route path="/customs" element={<CustomsPage />} />
        <Route path="/punishment" element={<PunishmentPage />} />
        <Route path="/ideas" element={<IdeasPage />} />
        <Route path="/graph" element={<GraphExplorer />} />
        <Route path="/about" element={<About />} />
        <Route path="/demo" element={<EntityPage />} />
        <Route path="/entity/:slug" element={<EntityPage />} />
        <Route path="/catalog" element={<CatalogPage />} />
        <Route path="/cat/:callNumber" element={<CatalogPage />} />
        <Route path="/corpus" element={<CorpusHub />} />
        <Route path="/corpus/biblical" element={<BiblicalCorpusPage />} />
        <Route path="/corpus/:corpusSlug" element={<CorpusPage />} />
        <Route path="/topics" element={<TopicsHub />} />
        <Route path="/docs" element={<DocsPage />} />
      </Route>
      </Routes>
    </>
  )
}
