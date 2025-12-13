```mermaid
flowchart TD
  %% Top-down cluster extract: Reformations -> Dutch_Reformation
  Reformations["Reformations"]

  Reformations -->|IS_PART_OF (has part)| English_Reformation["English Reformation"]
  Reformations -->|IS_PART_OF (has part)| German_Reformation["German Reformation"]
  Reformations -->|IS_PART_OF (has part)| Swiss_Reformation["Swiss Reformation"]
  Reformations -->|IS_PART_OF (has part)| Radical_Reformation["Radical Reformation"]
  Reformations -->|IS_PART_OF (has part)| Scottish_Reformation["Scottish Reformation"]
  Reformations -->|IS_PART_OF (has part)| French_Reformation["French Reformation"]
  Reformations -->|IS_PART_OF (has part)| Dutch_Reformation["Dutch Reformation"]
  Reformations -->|IS_PART_OF (has part)| Scandinavian_Reformations["Scandinavian Reformations"]
  Reformations -->|IS_PART_OF (has part)| Bohemian_Moravian_Reformation["Bohemian / Moravian Reformation"]
  Reformations -->|IS_PART_OF (has part)| Polish_Lithuanian_Reformation["Polish-Lithuanian Reformation"]
  Reformations -->|IS_PART_OF (has part)| Catholic_Reformation["Catholic Reformation"]

  %% Expand Dutch_Reformation as a subgraph with representative nodes & edges
  subgraph DutchCluster ["Dutch Reformation cluster"]
    direction TB
    Dutch_Reformation["Dutch Reformation"]
    Dutch_Reformed["Dutch Reformed"]
    Belgic_Confession_1561["Belgic Confession (1561)"]
    Heidelberg_Catechism_1563["Heidelberg Catechism (1563)"]
    Church_Order_of_Dort_1619["Church Order of Dort (1619)"]
    Canons_of_Dort_1619["Canons of Dort (1619)"]
    Remonstrance_1610["Remonstrance (1610)"]
    Arminian_Remonstrant["Arminian Remonstrant"]
    Contra_Remonstrant["Contra-Remonstrant"]
    Synod_of_Dordt_1618_1619["Synod of Dordt (1618–1619)"]
    Dordrecht["Dordrecht"]
    Synod_of_Emden_1571["Synod of Emden (1571)"]
    Emden["Emden"]
    Union_of_Utrecht_1579["Union of Utrecht (1579)"]
    Utrecht["Utrecht"]
    States_General["States General"]
    Reformed_Church_of_the_Netherlands["Reformed Church of the Netherlands"]
    Provincial_Synods["Provincial Synods"]

    %% parent/child connective (note: relationships stored child->parent as IS_PART_OF; diagram uses parent->child for readability)
    Dutch_Reformation -->|has part (IS_PART_OF)| Dutch_Reformed

    %% Representative intra-cluster relationships (type labels shown)
    Belgic_Confession_1561 -->|STANDARDIZES| Dutch_Reformed
    Heidelberg_Catechism_1563 -->|TRANSMITS| Dutch_Reformed
    Church_Order_of_Dort_1619 -->|STANDARDIZES| Dutch_Reformed
    Canons_of_Dort_1619 -->|STANDARDIZES| Contra_Remonstrant
    Remonstrance_1610 -->|DEFINES| Arminian_Remonstrant
    Synod_of_Dordt_1618_1619 -->|OCCURS_IN| Dordrecht
    Synod_of_Emden_1571 -->|OCCURS_IN| Emden
    Union_of_Utrecht_1579 -->|OCCURS_IN| Utrecht
    States_General -->|ORGANIZES| Union_of_Utrecht_1579
    States_General -->|DECLARES| Oldenbarnevelt_Execution_1619["Oldenbarnevelt Execution (1619)"]
    Reformed_Church_of_the_Netherlands -->|ORGANIZES| Provincial_Synods
    Provincial_Synods -->|C| Regional_synods_coordinating_doctrine["Regional synods coordinating doctrine"]

    %% note: full node + relationship JSON available in the repo files
  end

  %% Cross-link: cluster-level assignment found in relationships.Dutch_Reformation.json (Dutch_Reformation -> European_Reformations)
  Dutch_Reformation -->|IS_PART_OF (parent)| European_Reformations["European Reformations"]

``` 

**Files**:

- Full Dutch Reformation nodes: `data/Nodes/nodes.Dutch_Reformation.json`
- Full Dutch Reformation relationships: `data/Relationships/relationships.Dutch_Reformation.json`
- Reformations cluster nodes: `data/Nodes/nodes.Reformations.json`
- Reformations cluster relationships: `data/Relationships/relationships.Reformations.json`

Render this Mermaid on GitHub, GitLab or at https://mermaid.live to see the top-down diagram.

If you want every single intra-cluster relationship expanded into the diagram (all ~60+ edges), tell me and I will generate a full-edge Mermaid file and commit it.

