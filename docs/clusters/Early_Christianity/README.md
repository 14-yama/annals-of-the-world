## Comprehensive Early_Christianity Cluster Tree (Periods, Institutions, Texts, Movements, Events)
Parent root: Christian_Tradition (D)
Scope: ca. 30–325 CE (optionally to 451 CE for Late Antique interfaces)
Boundary: Standalone cluster tree; interfaces to Hebrew_Tradition (Second_Temple), Roman_Empire (Institutions/Law), Hellenistic_Philosophy, and Late_Antique_Christianity.

- Early_Christianity (D)
  - Periods (D)
    - Apostolic_Age_(c._30–70_CE) (D)
  - Persons (P): Jesus_of_Nazareth; Peter; Paul; James_the_Just; John; Barnabas; Stephen
      - Institutions (I): Jerusalem_Church; Apostolic_Leadership; Synagogue_Context
      - Texts (T): Synoptic_Traditions_(source_strata); Early_Pauline_Epistles; Acts_(early_narratives)
      - Movements (M): Jesus_Movement; Pauline_Communities
      - Events (E): Crucifixion; Resurrection_Proclamations; Pentecost; Council_of_Jerusalem_(c._49_CE); Temple_Destruction_70_CE
      - Places (L): Judea; Galilee; Jerusalem; Antioch
      - Suggested clusters: Jerusalem_Church_and_Apostolic_Leadership; Pauline_Mission_and_Gentile_Inclusion; Council_of_Jerusalem
      - Edges (canonical triples)
        - P/I → E
          - (Jerusalem_Church) ORGANIZES (Council_of_Jerusalem_(c._49_CE))
          - (Peter) LEADS (Council_of_Jerusalem_(c._49_CE))
          - (Paul) PARTICIPATES_IN (Council_of_Jerusalem_(c._49_CE))
        - E → L
          - (Crucifixion) OCCURS_IN (Jerusalem)
          - (Pentecost) OCCURS_IN (Jerusalem)
        - T ↔ E/M
          - (Acts_(early_narratives)) FRAMES (Pentecost)
          - (Early_Pauline_Epistles) TRANSMITS (Pauline_Communities)
        - T ↔ T
          - (Synoptic_Traditions_(source_strata)) TRANSMITS (Synoptic_Gospels)
        - P ↔ P/M
          - (Paul) DEBATES (Peter)
          - (Barnabas) CORRESPONDS_WITH (Paul)
    - Subapostolic_Age_(c._70–100_CE) (D)
  - Persons (P): Clement_of_Rome; Ignatius_of_Antioch; Polycarp; John_(trad.); Author_of_Didache
      - Institutions (I): Emerging_Episcopal_Structure; Local_Churches
      - Texts (T): Synoptic_Gospels; Gospel_of_John; Didache; 1_Clement
      - Movements (M): Proto‑Orthodox_Formations; Johannine_Community
      - Events (E): Post_70_Reconfiguration; Early_Regional_Synods
      - Suggested clusters: Johannine_Community_and_Texts; Synoptic_Source_Trajectories
      - Edges (canonical triples)
        - I → E
          - (Emerging_Episcopal_Structure) ORGANIZES (Early_Regional_Synods)
        - P ↔ I/M
          - (Ignatius_of_Antioch) CORRESPONDS_WITH (Local_Churches)
          - (Clement_of_Rome) ENDORSES (Emerging_Episcopal_Structure)
        - T ↔ T
          - (1_Clement) CITES (Synoptic_Gospels)
          - (Gospel_of_John) INTERPRETS (Synoptic_Traditions_(source_strata))
        - E → L
          - (Early_Regional_Synods) OCCURS_IN (Asia_Minor)
    - Ante‑Nicene_Period_(c._100–325_CE) (D)
  - Persons (P): Justin_Martyr; Irenaeus; Tertullian; Origen; Clement_of_Alexandria; Hippolytus; Cyprian
      - Institutions (I): Rome_Church; Alexandria; Antioch; Early_Synods
      - Texts (T): Ignatian_Letters; Shepherd_of_Hermas; Apologists_(Justin,_Tertullian,_Origen); Muratorian_Fragment
      - Movements (M): Proto‑Orthodox; Gnostic_Schools; Marcionite; Montanism; Apologetic_Tradition
      - Events (E): Persecutions_(Neronian,_Decian,_Diocletianic); Edict_of_Milan_313
      - Places (L): Rome; Alexandria; Asia_Minor; Carthage
      - Suggested clusters: Apologists_and_Hellenistic_Engagement; Gnostic_and_Proto‑Orthodox_Debates; Persecution_Phases; Emergence_of_Episcopal_Structure; Canon_Formation
      - Edges (canonical triples)
        - I → E/T/D
          - (Rome_Church) ORGANIZES (Early_Synods)
        - P ↔ M/T
          - (Justin_Martyr) COMMENTATES_ON (Gospel_of_John)
          - (Origen) COMMENTATES_ON (Gospel_of_John)
          - (Irenaeus) CITES (Muratorian_Fragment)
        - M ↔ M
          - (Proto‑Orthodox) DEBATES (Gnostic_Schools)
          - (Proto‑Orthodox) DISPUTES (Marcionite)
        - T ↔ M
          - (Shepherd_of_Hermas) EXEMPLIFIES (Proto‑Orthodox)
        - E → L
          - (Persecutions_(Neronian,_Decian,_Diocletianic)) OCCURS_IN (Rome)
          - (Persecutions_(Neronian,_Decian,_Diocletianic)) OCCURS_IN (Carthage)

## Interfaces to other clusters
- Hebrew_Tradition (Second_Temple interface): INTERPRETS; CITES; DEBATES; PARTICIPATES_IN/LEADS (Temple/Synagogue contexts); OCCURS_IN (E→L)
- Roman_Empire (Institutions/Law): TRIED_BY/IMPRISONS/EXECUTES (I→P via justice verbs); DECLARES/EDICTS (I→E/T); OCCURS_IN (E→L)
- Hellenistic_Philosophy: ENGAGES_WITH/DEBATES/REFUTES (P/M↔D/T); CITES; TRANSLATES
- Late_Antique_Christianity: CONVENES_COUNCIL (I→E); PROMULGATES_CANON (I→T/D); CENSORS/APPROVES; INTERPRETS

## Typical canonical verbs used
- P ↔ P/M: TEACHES; STUDIES_UNDER; DEBATES; ENDORSES; CORRESPONDS_WITH
- I → P: ORDAINS; APPOINTS; DEPOSES; EXCOMMUNICATES; PARDONS; IMPRISONS
- I → T/D: CANONIZES; PROMULGATES; STANDARDIZES; CENSORS; APPROVES
- T/D ↔ T/D: INTERPRETS; COMMENTATES_ON; CITES; TRANSLATES; TRANSMITS
- P/I → E: PARTICIPATES_IN; LEADS; ORGANIZES; DECLARES
- E → L: OCCURS_IN

## Data hygiene
- Reuse global nodes (persons, texts, institutions). Don’t duplicate nodes across clusters.
- Keep cross‑cluster edges here (or in a dedicated interfaces file); tag where supported (crosslink=true, interface="Second_Temple").

## Change log (cluster‑local)
- 2025‑10‑18: Restructured into hierarchical tree model; interfaces and verb palette retained.
