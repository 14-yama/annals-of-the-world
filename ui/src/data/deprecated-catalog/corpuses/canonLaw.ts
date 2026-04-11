/**
 * Canon Law Corpus — Gratian's Decretum, papal decretals, conciliar acts
 *
 * Covers: Church legal tradition from apostolic constitutions through the
 * Corpus Iuris Canonici, spanning c. 100 CE – 1917 CE.
 */
import type { Entity } from '../../entityTypes'

export const CANON_LAW_ENTITIES: Entity[] = [
  {
    slug: 'canon_law_corpus',
    name: 'The Canon Law Corpus',
    label: 'Text',
    callNumber: '730.06-canon-law-corpus',
    subjectHeadings: ['Artifacts & Texts — Legal Texts — Ecclesiastical Law'],
    subjects: ['Canon Law', 'Gratian', 'Decretum', 'Papal Decretals', 'Church Law', 'Conciliar Acts', 'Corpus Iuris Canonici'],
    summary: 'The Canon Law Corpus encompasses the legal tradition of the Christian Church from the Apostolic Constitutions (c. 375 CE) through the Corpus Iuris Canonici (1582) and its modern successors. Its centerpiece is Gratian\'s Decretum (Concordia Discordantium Canonum, c. 1140), a systematic reconciliation of nearly 4,000 canonical texts — papal decretals, conciliar canons, Church Fathers, and Roman law — that became the foundation of European ecclesiastical jurisprudence. The canon law tradition shaped marriage law, contract theory, criminal procedure, corporate law, and international law across medieval and early modern Europe, parallel to and deeply intertwined with the Roman civil law tradition. The 1917 and 1983 Codes of Canon Law codified this tradition for the modern Catholic Church.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 100 CE – 1917 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT'],
    causes: [
      { title: 'Early Church needs rules for governance, discipline, and doctrine', type: 'Institution', year: 'c. 100 CE' },
      { title: 'Roman legal categories provide framework for systematic church law', type: 'Text', year: 'c. 500 CE' },
    ],
    effects: [
      { title: 'Gratian\'s Decretum creates systematic ecclesiastical jurisprudence', type: 'Text', year: 'c. 1140 CE', slug: 'decretum_gratiani' },
      { title: 'Canon law shapes European marriage law, contracts, and procedure', type: 'Idea', year: 'c. 1200 CE' },
      { title: 'Influences development of international law and human rights concepts', type: 'Idea', year: 'c. 1500 CE' },
    ],
    relationships: [
      { sourceSlug: 'canon_law_corpus', sourceName: 'The Canon Law Corpus', verb: 'CONTAINS', targetSlug: 'decretum_gratiani', targetName: 'Decretum Gratiani', context: 'Foundation of systematic canon law' },
      { sourceSlug: 'canon_law_corpus', sourceName: 'The Canon Law Corpus', verb: 'CONTAINS', targetSlug: 'liber_extra', targetName: 'Liber Extra', context: 'Papal decretal collection' },
    ],
    places: [
      { name: 'Rome', role: 'Papal seat and center of canonistic tradition', slug: 'rome_city' },
      { name: 'Bologna', role: 'University center where Gratian compiled the Decretum' },
    ],
    texts: [],
  },
  {
    slug: 'decretum_gratiani',
    name: 'Decretum Gratiani',
    label: 'Text',
    callNumber: '730.70-decretum-gratiani',
    subjectHeadings: ['Artifacts & Texts — Legal Texts — Medieval Canon Law'],
    subjects: ['Gratian', 'Canon Law', 'Bologna', 'Concordia Discordantium Canonum', 'Scholastic Method', 'Church Law'],
    summary: 'The Concordia Discordantium Canonum ("Concord of Discordant Canons"), compiled by the monk Gratian at Bologna c. 1140 CE, is the foundational text of systematic canon law. Gratian collected nearly 4,000 authoritative texts — papal decretals, conciliar canons, patristic writings, penitential literature, and fragments of Roman law — and organized them topically into 101 "distinctions" and 36 "causes," providing his own commentary (dicta) to harmonize contradictions. Using the scholastic dialectical method (sic et non), the Decretum created a coherent legal system from centuries of disparate sources. It was the most heavily glossed text in medieval Europe after the Bible and became the first part of the Corpus Iuris Canonici.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 1140 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT'],
    causes: [
      { title: 'Investiture Controversy necessitates systematic church law', type: 'Event', year: 'c. 1075 CE' },
      { title: 'Revival of Roman law at Bologna provides methodological model', type: 'Text', year: 'c. 1100 CE' },
    ],
    effects: [
      { title: 'Foundation of university canon law education across Europe', type: 'Institution', year: 'c. 1150 CE' },
      { title: 'Shapes medieval marriage law, procedural law, and corporate theory', type: 'Idea', year: 'c. 1200 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Bologna', role: 'Compiled at the University of Bologna' },
    ],
    texts: [],
  },
  {
    slug: 'liber_extra',
    name: 'Liber Extra (Decretals of Gregory IX)',
    label: 'Text',
    callNumber: '730.71-liber-extra',
    subjectHeadings: ['Artifacts & Texts — Legal Texts — Papal Decretals'],
    subjects: ['Gregory IX', 'Raymond of Peñafort', 'Decretals', 'Papal Law', 'Medieval Law'],
    summary: 'An authoritative collection of papal decretals compiled by Raymond of Peñafort at the command of Pope Gregory IX, promulgated in 1234 CE. Organized into five books (judex, judicium, clerus, connubia, crimen), the Liber Extra gathered post-Gratian papal legislation and became the second major component of the Corpus Iuris Canonici. It standardized Church legal procedure, marital law, clerical discipline, and criminal procedure, and was the first officially promulgated papal legal code that superseded all prior collections not specifically preserved.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Europe',
    continent: 'Europe',
    status: 'Published',
    period: '1234 CE',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [],
    effects: [
      { title: 'Standardizes papal legal authority across Christendom', type: 'Idea', year: '1234 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Rome', role: 'Promulgated by papal authority' },
    ],
    texts: [],
  },

  // PERSON
  {
    slug: 'gratian_jurist',
    name: 'Gratian',
    label: 'Person',
    callNumber: '250.35-gratian',
    subjectHeadings: ['People — Medieval Scholars — Canon Lawyers'],
    subjects: ['Canon Law', 'Bologna', 'Decretum', 'Monk', 'Legal Systematizer', 'Twelfth Century'],
    summary: 'A Camaldolese monk and jurist active in Bologna in the mid-12th century, Gratian (fl. c. 1130–1150) compiled the Concordia Discordantium Canonum (the Decretum), which became the foundational text of systematic canon law and the first part of the Corpus Iuris Canonici. Almost nothing is known of his personal life — he is one of history\'s most influential scholars about whom the fewest biographical facts survive. His method of dialectical reconciliation of contradictory authorities became the standard methodology for legal education and influenced both canon and civil law scholarship for centuries.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Europe',
    continent: 'Europe',
    status: 'Published',
    born: 'c. 1100 CE',
    died: 'c. 1160 CE',
    frameworks: ['DOCTRINE_DEVELOPMENT'],
    causes: [],
    effects: [
      { title: 'Decretum Gratiani becomes foundation of canon law', type: 'Text', year: 'c. 1140 CE', slug: 'decretum_gratiani' },
    ],
    relationships: [
      { sourceSlug: 'gratian_jurist', sourceName: 'Gratian', verb: 'AUTHORS', targetSlug: 'decretum_gratiani', targetName: 'Decretum Gratiani', context: 'Compiled the foundational canon law text' },
    ],
    places: [
      { name: 'Bologna', role: 'Compiled the Decretum here' },
    ],
    texts: [],
  },
]
