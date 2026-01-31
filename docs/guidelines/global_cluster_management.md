---
title: Global Cluster Management Guidelines
status: ACTIVE
version: 1.0
created_at: 2026-01-31
summary: Comprehensive guide for managing clusters at all hierarchical levels—from continent to thematic sub-clusters—with integration into the timeframe classification system.
---

# Global Cluster Management Guidelines

## 1. Purpose

This document establishes best practices for managing **clusters** (curated subgraphs/containers) at every level of the geographic and thematic hierarchy. It ensures curators can:

1. Navigate the vast codebase efficiently via a consistent container taxonomy
2. View events/nodes grouped by **Timeframe** (920–960) and **Cluster** simultaneously
3. Maintain uniformity across all country-level containers
4. Scale the system as new thematic clusters (e.g., WWII, Renaissance) are added

---

## 2. Cluster Hierarchy Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           GLOBAL CLUSTER TREE                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 0: CORPUS / TRADITION (Class 10)                                     │
│  ├── Hebrew_Tradition, Islamic_Golden_Age, Greco_Roman, etc.                │
│                                                                             │
│  Level 1: CONTINENT (Class 4.410)                                           │
│  ├── Europe, Asia, Africa, Americas, Oceania, Antarctica                    │
│                                                                             │
│  Level 2: REGION (Class 4.420)                                              │
│  ├── Northern_Europe, Central_Asia, North_Africa, etc.                      │
│                                                                             │
│  Level 3: COUNTRY (Class 4.430)                                             │
│  ├── united-kingdom, germany, france, egypt, india, etc.                    │
│  │                                                                          │
│  │   Level 4: THEMATIC CLUSTER (within country)                             │
│  │   ├── English_Reformation (930 Medieval / 940 Early Modern)              │
│  │   ├── British_Industrial_Revolution (950 Modern)                         │
│  │   ├── British_WWII_Home_Front (960 Contemporary)                         │
│  │   └── Tudor_Dynasty (940 Early Modern)                                   │
│  │                                                                          │
│  │       Level 5: SUB-CLUSTER (episode/focus)                               │
│  │       ├── Henry_VIII_Annulment_1527_1536                                 │
│  │       ├── Elizabethan_Settlement_1558_1603                               │
│  │       └── Dissolution_of_Monasteries_1536_1541                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Timeframe Integration

All clusters and nodes integrate with the **Timeframe Classification** (Class 9):

| Division | Period           | Approximate Years     | Example Clusters                                    |
|----------|------------------|-----------------------|-----------------------------------------------------|
| **910**  | Prehistoric      | Before 3000 BCE       | Stonehenge_Construction, Megalithic_Britain         |
| **920**  | Classical        | 3000 BCE – 500 CE     | Roman_Britain, Early_Christianity                   |
| **930**  | Medieval         | 500 – 1500 CE         | Norman_Conquest, Magna_Carta_Era, Black_Death       |
| **940**  | Early Modern     | 1500 – 1800 CE        | English_Reformation, Tudor_Dynasty, Glorious_Rev    |
| **950**  | Modern           | 1800 – 1945 CE        | Industrial_Revolution, Victorian_Era, WWI_Britain   |
| **960**  | Contemporary     | 1945 – Present        | Post_WWII_Britain, Decolonization, Brexit           |

### Cross-Reference Matrix

Every thematic cluster MUST declare:
- **Primary Timeframe**: The dominant period (e.g., 940 for English_Reformation)
- **Secondary Timeframes**: Overlapping periods (e.g., 930 for pre-Reformation context)

```json
{
  "cluster": "English_Reformation",
  "timeframes": {
    "primary": "940",
    "secondary": ["930"]
  },
  "year_range": [1527, 1603]
}
```

---

## 4. Directory Structure

### 4.1 Geographic Registry (geo-registry/)

```
geo-registry/
├── places/
│   └── countries/
│       └── <country-slug>/
│           ├── places.json          # Country + cities Place nodes
│           ├── events.json          # Events that OCCURS_IN this country
│           ├── people.json          # Persons BORN_IN / DIED_IN / ACTIVE_IN
│           ├── institutions.json    # Institutions LOCATED_IN this country
│           ├── artifacts.json       # Artifacts FOUND_IN / CREATED_IN
│           ├── texts.json           # Texts WRITTEN_IN / PUBLISHED_IN
│           ├── ideas.json           # Ideas ORIGINATED_IN (rare)
│           ├── movements.json       # Movements CENTERED_IN
│           ├── evidence.json        # Evidence sources
│           ├── frameworks.json      # Historian frameworks
│           └── timeframes.json      # Country-specific period definitions
```

### 4.2 Thematic Cluster Registry (docs/clusters/)

```
docs/clusters/
├── <cluster-slug>/
│   ├── README.md                    # Main cluster documentation
│   ├── nodes.csv                    # Node inventory (optional)
│   ├── edges.csv                    # Edge inventory (optional)
│   └── sub-clusters/                # Episode-level sub-clusters
│       └── <sub-cluster-slug>/
│           └── README.md
```

### 4.3 Relationship Data (data/Relationships/)

```
data/Relationships/
├── relationships.<cluster-slug>.json    # Edges for thematic clusters
└── relationships.<country-slug>.json    # Edges for country containers (future)
```

---

## 5. Cluster Metadata Schema

Every cluster (country or thematic) MUST include a `_meta` block:

### 5.1 Country Container Metadata

```json
{
  "_meta": {
    "container_type": "country",
    "country_slug": "united-kingdom",
    "region": "Northern_Europe",
    "continent": "Europe",
    "iso3166_alpha2": "GB",
    "iso3166_alpha3": "GBR",
    "timeframe_coverage": ["910", "920", "930", "940", "950", "960"],
    "thematic_clusters": [
      {
        "slug": "English_Reformation",
        "timeframe_primary": "940",
        "year_range": [1527, 1603],
        "doc_path": "docs/clusters/English_Reformation/README.md"
      },
      {
        "slug": "British_Industrial_Revolution",
        "timeframe_primary": "950",
        "year_range": [1760, 1840],
        "doc_path": "docs/clusters/British_Industrial_Revolution/README.md"
      }
    ],
    "created_at": "2026-01-31T00:00:00Z",
    "updated_at": "2026-01-31T00:00:00Z"
  }
}
```

### 5.2 Thematic Cluster Metadata

```json
{
  "_meta": {
    "container_type": "thematic_cluster",
    "cluster": "English_Reformation",
    "parent_cluster": "European_Reformations",
    "geographic_scope": {
      "primary_country": "united-kingdom",
      "secondary_countries": ["holy-see", "germany", "switzerland"],
      "primary_region": "Northern_Europe",
      "continent": "Europe"
    },
    "timeframe": {
      "primary": "940",
      "secondary": ["930"],
      "year_range": [1527, 1603]
    },
    "sub_clusters": [
      "Henry_VIII_Annulment_1527_1536",
      "Edwardian_Reformation_1547_1553",
      "Marian_Restoration_1553_1558",
      "Elizabethan_Settlement_1558_1603"
    ],
    "interfaces": [
      "Roman_Catholic_Church",
      "Continental_Reformations",
      "English_Parliament"
    ]
  }
}
```

---

## 6. Node Grouping Strategy

### 6.1 Primary Grouping: By Timeframe

Query all events in a country by timeframe:

```cypher
// All UK events in Early Modern period (940)
MATCH (e:Event)-[:OCCURS_IN]->(p:Place {slug: 'united-kingdom'})
WHERE e.startYear >= 1500 AND e.startYear < 1800
RETURN e.slug, e.name, e.startYear, e.endYear, '940' AS timeframe
ORDER BY e.startYear
```

### 6.2 Secondary Grouping: By Cluster

Query all events in a country by thematic cluster:

```cypher
// All events in English_Reformation cluster
MATCH (e:Event)-[:BELONGS_TO_CLUSTER]->(c:Cluster {slug: 'English_Reformation'})
RETURN e.slug, e.name, e.startYear, e.endYear
ORDER BY e.startYear
```

### 6.3 Combined View: Timeframe × Cluster Matrix

```cypher
// Matrix view: UK events grouped by timeframe AND cluster
MATCH (e:Event)-[:OCCURS_IN]->(p:Place {slug: 'united-kingdom'})
OPTIONAL MATCH (e)-[:BELONGS_TO_CLUSTER]->(c:Cluster)
WITH e, c,
  CASE 
    WHEN e.startYear < -3000 THEN '910'
    WHEN e.startYear < 500 THEN '920'
    WHEN e.startYear < 1500 THEN '930'
    WHEN e.startYear < 1800 THEN '940'
    WHEN e.startYear < 1945 THEN '950'
    ELSE '960'
  END AS timeframe
RETURN timeframe, 
       coalesce(c.slug, 'UNASSIGNED') AS cluster,
       collect(e.name) AS events
ORDER BY timeframe, cluster
```

---

## 7. Cluster Assignment Rules

### 7.1 Mandatory Assignments

Every node in a country container SHOULD have:

1. **Geographic Edge**: `OCCURS_IN`, `LOCATED_IN`, `BORN_IN`, etc. → Country Place
2. **Timeframe Property**: `startYear`, `endYear` → determines timeframe division
3. **Cluster Edge** (optional but recommended): `BELONGS_TO_CLUSTER` → Thematic Cluster

### 7.2 Cluster Property on Nodes

Add `cluster` property to nodes for fast filtering without traversing edges:

```json
{
  "slug": "Act_of_Supremacy_1534_Passed",
  "name": "Act of Supremacy (1534) Passed",
  "label": "Event",
  "cluster": "English_Reformation",
  "timeframe": "940",
  "startYear": 1534,
  "endYear": 1534
}
```

### 7.3 Multi-Cluster Membership

A node CAN belong to multiple clusters when historically appropriate:

```json
{
  "slug": "Henry_VIII",
  "name": "Henry VIII",
  "label": "Person",
  "clusters": ["English_Reformation", "Tudor_Dynasty", "Anglo_French_Wars"],
  "primary_cluster": "English_Reformation"
}
```

---

## 8. Creating a New Thematic Cluster

### 8.1 Checklist

When creating a new cluster (e.g., `British_WWII_Home_Front`):

- [ ] **Scope Definition**
  - Geographic scope: Country, region, or multi-country?
  - Timeframe: Primary (960) + secondary timeframes
  - Year range: [1939, 1945]
  
- [ ] **Parent Assignment**
  - Movement or Category parent (e.g., `World_War_II`)
  - Country container (e.g., `united-kingdom`)
  
- [ ] **Directory Setup**
  - Create `docs/clusters/British_WWII_Home_Front/README.md`
  - Create `data/Relationships/relationships.British_WWII_Home_Front.json`
  
- [ ] **Node Inventory**
  - Extract relevant nodes from country container
  - Assign `cluster` property
  - Create `BELONGS_TO_CLUSTER` edges
  
- [ ] **Cross-References**
  - Link to parent cluster (World_War_II)
  - Link to sibling clusters (US_WWII_Pacific, German_WWII_Eastern_Front)
  - Update country container metadata

### 8.2 Naming Convention

```
<Geographic_Scope>_<Theme>_<Optional_SubFocus>_<Year_Range>

Examples:
- English_Reformation                    # Country + theme
- British_Industrial_Revolution          # Country + theme  
- British_WWII_Home_Front                # Country + theme + focus
- Tudor_Dynasty                          # Country + theme (dynastic)
- Henry_VIII_Annulment_1527_1536         # Person + event + years (sub-cluster)
```

### 8.3 README Template

```markdown
# <Cluster_Name>

## Cluster Overview

[One paragraph description]

### Scope
- **Geographic**: [Country/Region]
- **Timeframe**: [Primary division] (Secondary: [list])
- **Year Range**: [start] – [end]
- **Parent Cluster**: [parent slug]

### Statistics (Updated YYYY-MM)

| Category | Count |
|----------|-------|
| **Total Nodes** | N |
| **Total Relationships** | N |

### Key Periods

1. **[Period 1]**: [Description]
2. **[Period 2]**: [Description]

### Most Connected Nodes

| Node | Type | Edges |
|------|------|-------|

---

### Sub-Clusters

| Slug | Year Range | Focus |
|------|------------|-------|

---

### Interfaces (Cross-Cluster Links)

- [Parent/sibling cluster 1]
- [Parent/sibling cluster 2]

---

### Change Log

| Date | Change | Author |
|------|--------|--------|
```

---

## 9. Country Container Index File

Each country SHOULD have an `index.json` that catalogs all thematic clusters:

### 9.1 File: `geo-registry/places/countries/<slug>/index.json`

```json
{
  "_meta": {
    "country_slug": "united-kingdom",
    "last_updated": "2026-01-31T00:00:00Z"
  },
  "thematic_clusters": {
    "930": [
      {
        "slug": "Norman_Conquest_Cluster",
        "name": "Norman Conquest & Early Norman England",
        "year_range": [1066, 1154],
        "status": "PLANNED"
      },
      {
        "slug": "Magna_Carta_Era",
        "name": "Magna Carta and Early Parliamentary Development",
        "year_range": [1215, 1295],
        "status": "PLANNED"
      }
    ],
    "940": [
      {
        "slug": "English_Reformation",
        "name": "English Reformation",
        "year_range": [1527, 1603],
        "status": "ACTIVE",
        "doc_path": "docs/clusters/English_Reformation/README.md",
        "relationships_path": "data/Relationships/relationships.English_Reformation.json"
      },
      {
        "slug": "Tudor_Dynasty",
        "name": "Tudor Dynasty",
        "year_range": [1485, 1603],
        "status": "PLANNED"
      },
      {
        "slug": "Elizabethan_Era",
        "name": "Elizabethan Era",
        "year_range": [1558, 1603],
        "status": "PLANNED"
      }
    ],
    "950": [
      {
        "slug": "British_Industrial_Revolution",
        "name": "British Industrial Revolution",
        "year_range": [1760, 1840],
        "status": "PLANNED"
      },
      {
        "slug": "Victorian_Era",
        "name": "Victorian Era",
        "year_range": [1837, 1901],
        "status": "PLANNED"
      },
      {
        "slug": "British_WWI",
        "name": "Britain in World War I",
        "year_range": [1914, 1918],
        "status": "PLANNED"
      }
    ],
    "960": [
      {
        "slug": "British_WWII",
        "name": "Britain in World War II",
        "year_range": [1939, 1945],
        "status": "PLANNED"
      },
      {
        "slug": "British_Decolonization",
        "name": "British Decolonization",
        "year_range": [1947, 1997],
        "status": "PLANNED"
      }
    ]
  },
  "unassigned_events": {
    "count": 5,
    "note": "Events not yet assigned to a thematic cluster"
  }
}
```

---

## 10. Global Cluster Registry

### 10.1 File: `docs/registry/global_cluster_registry.md`

Maintain a master registry of ALL clusters across all countries:

```markdown
# Global Cluster Registry

## By Continent → Region → Country → Cluster

### Europe

#### Northern Europe

##### United Kingdom
| Timeframe | Cluster Slug | Status | Nodes | Edges |
|-----------|--------------|--------|-------|-------|
| 930 | Norman_Conquest_Cluster | PLANNED | - | - |
| 940 | English_Reformation | ACTIVE | 182 | 423 |
| 940 | Tudor_Dynasty | PLANNED | - | - |
| 950 | British_Industrial_Revolution | PLANNED | - | - |
| 960 | British_WWII | PLANNED | - | - |

##### Ireland
| Timeframe | Cluster Slug | Status | Nodes | Edges |
|-----------|--------------|--------|-------|-------|
| 930 | Norman_Ireland | PLANNED | - | - |
| 940 | Irish_Reformation | PLANNED | - | - |

#### Western Europe

##### Germany
| Timeframe | Cluster Slug | Status | Nodes | Edges |
|-----------|--------------|--------|-------|-------|
| 940 | German_Reformation | ACTIVE | 156 | 312 |
| 950 | German_Unification | PLANNED | - | - |
| 960 | Third_Reich | PLANNED | - | - |

...
```

---

## 11. Cypher Queries for Cluster Management

### 11.1 Create Cluster Node

```cypher
CREATE (c:Cluster {
  slug: 'British_WWII',
  name: 'Britain in World War II',
  container_type: 'thematic_cluster',
  parent_cluster: 'World_War_II',
  primary_country: 'united-kingdom',
  timeframe_primary: '960',
  year_start: 1939,
  year_end: 1945,
  status: 'PLANNED',
  created_at: datetime()
})
RETURN c
```

### 11.2 Link Events to Cluster

```cypher
// Assign existing UK WWII events to cluster
MATCH (e:Event)-[:OCCURS_IN]->(p:Place {slug: 'united-kingdom'})
WHERE e.startYear >= 1939 AND e.endYear <= 1945
  AND e.name CONTAINS 'WWII' OR e.name CONTAINS 'War'
MATCH (c:Cluster {slug: 'British_WWII'})
MERGE (e)-[:BELONGS_TO_CLUSTER]->(c)
RETURN e.slug, c.slug
```

### 11.3 View Cluster Hierarchy

```cypher
// Full hierarchy: Continent → Region → Country → Clusters
MATCH (cont:Place {kind: 'region', region: cont.name})
  -[:CONTAINS]->(reg:Place {kind: 'region'})
  -[:CONTAINS]->(cntry:Place {kind: 'country'})
OPTIONAL MATCH (cntry)<-[:PRIMARY_COUNTRY]-(clust:Cluster)
RETURN cont.name AS continent, 
       reg.name AS region,
       cntry.name AS country,
       collect(clust.slug) AS clusters
ORDER BY cont.name, reg.name, cntry.name
```

### 11.4 Timeframe × Cluster Matrix for Country

```cypher
// UK events by timeframe and cluster
MATCH (e:Event)-[:OCCURS_IN]->(p:Place {slug: 'united-kingdom'})
OPTIONAL MATCH (e)-[:BELONGS_TO_CLUSTER]->(c:Cluster)
WITH e, c,
  CASE 
    WHEN e.startYear < 500 THEN '920 Classical'
    WHEN e.startYear < 1500 THEN '930 Medieval'
    WHEN e.startYear < 1800 THEN '940 Early Modern'
    WHEN e.startYear < 1945 THEN '950 Modern'
    ELSE '960 Contemporary'
  END AS timeframe
RETURN timeframe,
       coalesce(c.slug, '[Unassigned]') AS cluster,
       count(e) AS event_count,
       collect(e.name)[0..5] AS sample_events
ORDER BY timeframe, cluster
```

---

## 11.5 Example: Global Weapons/Artifacts Origin (Americas + Asia)

**Goal**: Curator wants to view weapons/artifacts that **originated in the Americas and Asia**, grouped by region and timeframe.

**Best Practice**:
- Create a **cross‑domain thematic cluster** (non‑geographic): `Weapons_Global`
- Use `ORIGINATED_IN` (or `CREATED_IN` when provenance is clearer) edges to Places
- Tag artifacts with `cluster: "Weapons_Global"` and `timeframe` derived from `startYear`

**Suggested cluster layout**:
- docs/clusters/Weapons_Global/README.md
- data/Relationships/relationships.Weapons_Global.json

**Example Cypher (Artifacts origin filter)**

```cypher
MATCH (a:Artifact)-[:ORIGINATED_IN]->(p:Place {kind:'country'})
WHERE p.region IN ['Americas','Asia']
OPTIONAL MATCH (a)-[:BELONGS_TO_CLUSTER]->(c:Cluster {slug:'Weapons_Global'})
WITH a, p, c,
  CASE 
    WHEN a.startYear < 500 THEN '920 Classical'
    WHEN a.startYear < 1500 THEN '930 Medieval'
    WHEN a.startYear < 1800 THEN '940 Early Modern'
    WHEN a.startYear < 1945 THEN '950 Modern'
    ELSE '960 Contemporary'
  END AS timeframe
RETURN p.region AS continent,
       p.name AS country,
       timeframe,
       coalesce(c.slug,'Weapons_Global') AS cluster,
       collect(a.name)[0..10] AS artifacts
ORDER BY continent, country, timeframe
```

**Example country index entry (Mexico)**

```json
{
  "slug": "Weapons_Artifacts_Mesoamerica",
  "name": "Weapons & Artifacts of Mesoamerica",
  "year_range": [-1500, 1600],
  "status": "PLANNED",
  "cross_domain_clusters": ["Weapons_Global"]
}
```

---

## 11.6 Example: WWII Cluster for Germany and Allies

**Goal**: Curator wants to view WWII clusters for **Germany and its allies**, with a coherent cross‑national structure.

**Best Practice**:
- Create a **global parent cluster**: `World_War_II` (cross‑domain)
- Create **country clusters** for each Axis power:
  - Germany → `German_WWII`
  - Italy → `Italian_WWII`
  - Japan → `Japanese_WWII`
  - Romania → `Romanian_WWII`
  - Hungary → `Hungarian_WWII`
  - Bulgaria → `Bulgarian_WWII`
  - Finland → `Finnish_WWII` (co‑belligerent)

**Recommended structure**:

```
docs/clusters/World_War_II/README.md
docs/clusters/German_WWII/README.md
docs/clusters/Italian_WWII/README.md
docs/clusters/Japanese_WWII/README.md
data/Relationships/relationships.World_War_II.json
data/Relationships/relationships.German_WWII.json
...
```

**Country index entry (Germany)**

```json
{
  "slug": "German_WWII",
  "name": "Germany in World War II",
  "year_range": [1933, 1945],
  "status": "PLANNED",
  "parent_cluster": "World_War_II",
  "key_events": [
    "Invasion_of_Poland_1939",
    "Operation_Barbarossa_1941",
    "Battle_of_Stalingrad_1942_1943",
    "Battle_of_Berlin_1945"
  ]
}
```

**Example Cypher (Axis cluster matrix)**

```cypher
MATCH (e:Event)-[:BELONGS_TO_CLUSTER]->(c:Cluster)
WHERE c.slug IN ['German_WWII','Italian_WWII','Japanese_WWII','Romanian_WWII','Hungarian_WWII','Bulgarian_WWII','Finnish_WWII']
OPTIONAL MATCH (e)-[:OCCURS_IN]->(p:Place {kind:'country'})
RETURN c.slug AS cluster,
       coalesce(p.name,'Unknown') AS country,
       count(e) AS event_count,
       collect(e.name)[0..5] AS sample_events
ORDER BY cluster, country
```

---

## 12. Workflow: Adding WWII Cluster to UK

### Step 1: Update Country Index

Add to `geo-registry/places/countries/united-kingdom/index.json`:

```json
{
  "slug": "British_WWII",
  "name": "Britain in World War II",
  "year_range": [1939, 1945],
  "status": "ACTIVE"
}
```

### Step 2: Create Cluster Documentation

Create `docs/clusters/British_WWII/README.md` using the template above.

### Step 3: Create Relationships File

Create `data/Relationships/relationships.British_WWII.json`:

```json
{
  "_meta": {
    "cluster": "British_WWII",
    "parent_cluster": "World_War_II",
    "geographic_scope": "united-kingdom",
    "timeframe_primary": "960",
    "year_range": [1939, 1945],
    "generated_at": "2026-01-31T00:00:00Z"
  },
  "relationships": []
}
```

### Step 4: Add Events to Country Container

Update `geo-registry/places/countries/united-kingdom/events.json`:

```json
{
  "slug": "Dunkirk_Evacuation_1940",
  "name": "Dunkirk Evacuation (1940)",
  "label": "Event",
  "cluster": "British_WWII",
  "timeframe": "960",
  "startYear": 1940,
  "endYear": 1940,
  "description": "Evacuation of Allied forces from Dunkirk beaches."
}
```

### Step 5: Run Cluster Wiring Script

```bash
python scripts/admin/wire_cluster.py --cluster British_WWII --country united-kingdom
```

---

## 13. Visual Dashboard Spec (Future)

The curator dashboard should support:

1. **Continent Bird's Eye**: Expandable tree of regions → countries
2. **Country View**: List all thematic clusters with status badges
3. **Timeframe Filter**: Toggle timeframes (930, 940, 950, etc.)
4. **Cluster Drill-Down**: View nodes/edges within selected cluster
5. **Unassigned Queue**: Events not yet assigned to any cluster

---

## 14. Quality Checklist

Before merging a new cluster:

- [ ] **Scope**: Clear geographic + temporal boundaries
- [ ] **Parent**: Assigned to country container AND thematic parent
- [ ] **Index Updated**: Country `index.json` includes new cluster
- [ ] **Registry Updated**: Global cluster registry updated
- [ ] **Nodes Tagged**: All nodes have `cluster` property
- [ ] **Edges Created**: `BELONGS_TO_CLUSTER` relationships exist
- [ ] **Documentation**: README.md created with required sections
- [ ] **Relationships File**: JSON file created in `data/Relationships/`

---

## 15. Summary

| Level | Container Type | Location | Example |
|-------|----------------|----------|---------|
| 0 | Corpus/Tradition | `docs/clusters/` | Hebrew_Tradition |
| 1 | Continent | `geo-registry/` | Europe |
| 2 | Region | `geo-registry/` | Northern_Europe |
| 3 | Country | `geo-registry/places/countries/<slug>/` | united-kingdom |
| 4 | Thematic Cluster | `docs/clusters/<slug>/` + country index | English_Reformation |
| 5 | Sub-Cluster | `docs/clusters/<parent>/sub-clusters/` | Henry_VIII_Annulment_1527_1536 |

**Key Principles**:
1. Every node has a **geographic anchor** (country Place)
2. Every node has a **temporal anchor** (startYear → timeframe division)
3. Thematic clusters are **opt-in** but strongly recommended for curation
4. The **country index.json** is the single source of truth for what clusters exist
5. Cross-cluster links use **INTERFACES_WITH** relationships

---

## Appendix A: Timeframe Division Reference

| Division | Name | Years | Mnemonic |
|----------|------|-------|----------|
| 910 | Prehistoric | Before 3000 BCE | "Before writing" |
| 920 | Classical | 3000 BCE – 500 CE | "Ancient empires" |
| 930 | Medieval | 500 – 1500 CE | "Middle Ages" |
| 940 | Early Modern | 1500 – 1800 CE | "Reformation to Enlightenment" |
| 950 | Modern | 1800 – 1945 CE | "Industrial to WWII" |
| 960 | Contemporary | 1945 – Present | "Post-war" |

---

## Appendix B: Cluster Status Values

| Status | Meaning |
|--------|---------|
| `PLANNED` | Cluster identified, not yet populated |
| `IN_PROGRESS` | Actively being curated |
| `ACTIVE` | Curated and maintained |
| `ARCHIVED` | Superseded or deprecated |

---

## Appendix C: Related Documentation

- [cluster_hierarchy.md](./cluster_hierarchy.md) — Original cluster hierarchy design
- [classification.md](./classification.md) — Call number system
- [call_number_subject_heading_system.md](./call_number_subject_heading_system.md) — Full classification guide
- [curator_workflow.md](./curator_workflow.md) — Curator task workflow
- [geo_naming.md](./geo_naming.md) — Geographic naming conventions
