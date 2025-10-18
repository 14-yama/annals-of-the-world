---
title: Cluster Hierarchy Guidelines — Cross-Domain (Reformations, Weapons, etc.)
status: ACTIVE
version: 1.0
summary: How to design, name, and organize cluster hierarchies across themes (e.g., Reformations) and material culture (e.g., Weapons), using only canonical verbs and existing node types.
---

# Purpose
Provide a consistent way to define cluster hierarchies across the project, so contributors model subgraphs with clear scope, parents, and interfaces while using the canonical verb set.

# Core Concepts
- Cluster (curated subgraph): A bounded set of nodes and edges with a purpose, timeframe, and geography.
- Parent cluster: The thematic or categorical container (e.g., English_Reformation; Weapons).
- Interfaces: Cross-links to other clusters; document them explicitly.

# When to Create a Cluster
- The narrative requires sustained focus (≥ 10–20 edges) within a coherent window.
- The subgraph is reusable by others (not a one‑off note).
- There’s a clear parent theme or category to attach it under.

# What to Use as the Parent
- Socio‑religious, political, intellectual themes → Movement (M)
  - Example: European_Reformations (M) → English_Reformation (M)
  - Subclusters: Henry_VIII_Annulment_and_Royal_Supremacy_1527_1536 (curated under English_Reformation)

- Technology / material culture families → Concept/Category (use Doctrine/Idea (D) for taxonomy), instances as Text/Artifact (T)
  - Example: Weapons (D) → Firearms (D) → Matchlock_Firearms (D)
  - Subclusters: Adoption_of_Matchlock_in_Japan_1540s (curated under Matchlock_Firearms)
  - Concrete items/models/patterns: T nodes (e.g., AK_47, Katana_Sword)

- Person‑centric episodes → Subcluster under the appropriate Movement or Category
  - Example: Henry VIII annulment sits under English_Reformation (M), not under Henry (P).

# Naming & IDs
- Title: <Theme/Subtheme — Focus (Years)>
- Slug: kebab or snake case. Example: english_reformation_henry_annulment_1527_1536
- Optional ID tag: C-<TOPIC>-<SUB>-<YY>–<YY> (e.g., C-REF-EN-HEN-1527–1536)

# Directory & Files
- docs/clusters/<slug>/README.md — main cluster doc
- docs/clusters/<slug>/nodes.csv (optional) — node listing/extract
- docs/clusters/<slug>/edges.csv (optional) — edge triples extract
- docs/case-studies/ — short illustrative cases (not full clusters)

# Required Sections in a Cluster Doc
- Header: title, status, summary, scope (theme, timeframe, geography)
- Nodes: list P, I, T, D, M, E, L (and V when promoted)
- Edges: canonical only (from relations_vocabulary.md); include direction and brief notes
- Evidence: short refs and tiers; promote reused refs to Evidence nodes
- Interfaces: list cross‑cluster links (parents/siblings)
- Change log: key edits for auditability

# Canonical Verbs (by common domain)
- Reformations (socio‑religious):
  - I→P: EXCOMMUNICATES; APPOINTS; DEPOSES; ORDAINS; PARDONS; IMPRISONS
  - I→T/D: CANONIZES; STANDARDIZES; PROMULGATES; CENSORS; APPROVES
  - P↔P: DIVORCES; MARRIES; TEACHES; STUDIES_UNDER; ENDORSES
  - P/I→E: PARTICIPATES_IN; LEADS; ORGANIZES; DECLARES
  - D/T ↔ D/T: INTERPRETS; COMMENTATES_ON; TRANSLATES; TRANSMITS; EXEMPLIFIES
  - Causality/location: CAUSES; ENABLES; TRANSFORMS; OCCURS_IN

- Weapons / Material culture:
  - D (category) ↔ T (instances): EXEMPLIFIES; SYMBOLIZES (when explicit);
  - P/I → T: PRODUCES; DESIGNS; INVENTS; DISTRIBUTES; USES (activity context)
  - P/I → D: STANDARDIZES (patterns/specs); PROMULGATES (ordinances)
  - Diffusion: DIFFUSES (to L); ADOPTS/REJECTS (doctrinal or practice policies)
  - Events: ENABLES/CAUSES (technology enabling events), OCCURS_IN (tests, battles)

# Interfaces (Cross‑links)
- Always point subclusters to their parent Movement or Category (D).
- If edges span clusters (e.g., Papacy in Henry’s cluster), add a “References other cluster” note.

# Quality Checklist (pre‑merge)
- Scope: clear theme + timeframe + geography
- Parent: Movement (M) or Category (D) chosen by domain
- Verbs: canonical only; prefer specific over INFLUENCES
- Evidence: present, tiered; repeated refs promoted to V nodes
- Interfaces: parents/siblings listed
- Audit: entry added to docs/governance/audit_log.md

# Example Trees
- Reformations
  - European_Reformations (M)
    - English_Reformation (M)
      - Henry_VIII_Annulment_and_Royal_Supremacy_1527_1536 (cluster)
    - German_Reformation (M)
      - Luther_95_Theses_and_Aftermath_1517_1525 (cluster)

- Weapons
  - Weapons (D)
    - Firearms (D)
      - Matchlock_Firearms (D)
        - Adoption_of_Matchlock_in_Japan_1540s (cluster)
    - Bladed_Weapons (D)
      - Swords (D)
        - Development_of_Katana_Muromachi_to_Edo (cluster)

## Hebrew_Tradition Cluster Tree
This tree has moved to the dedicated cluster doc:
- ../clusters/Hebrew_Tradition/README.md

See also
- ../clusters/Early_Christianity/README.md
- ../clusters/Jewish-Islamic_Exchange/README.md

## Comprehensive Weapons Cluster Tree (Taxonomy as Doctrine/Idea)
Note: Use Doctrine/Idea (D) nodes for categories/subcategories and Text/Artifact (T) nodes for concrete exemplars/models. Technical specs (caliber, gauge, materials) should be properties on T nodes. Use EXEMPLIFIES for D ↔ T examples when needed.

- Weapons (D)
  - Bladed_Weapons (D)
    - Swords (D)
      - Straight_Double_Edged_Swords (D)
        - Examples (T): Gladius; Spatha; Arming_Sword; Longsword
      - Curved_Swords (D)
        - Examples (T): Katana; Saber; Shamshir; Tulwar; Scimitar
      - Single_Edged_Straight_Swords (D)
        - Examples (T): Falchion; Messer
      - Short_Swords_Daggers (D)
        - Examples (T): Dagger; Dirk; Pugio; Seax; Jambiya
    - Knives (D)
      - Examples (T): Bowie_Knife; Kukri; Tanto
    - Axes (D)
      - Examples (T): Battle_Axe; Dane_Axe; Tomahawk
    - Polearms (D)
      - Examples (T): Halberd; Glaive; Naginata; Yari; Pike; Partisan; Poleaxe
    - Spears (D)
      - Examples (T): Javelin; Hasta; Assegai
    - Flexible_Weapons (D)
      - Examples (T): Flail; Chain_Whip
  - Impact_Weapons (D)
    - Clubs (D)
      - Examples (T): Cudgel; Truncheon
    - Maces (D)
      - Examples (T): Flanged_Mace; Morningstar
    - War_Hammers (D)
      - Examples (T): Lucerne_Hammer; Bec_de_Corbin
  - Ranged_Weapons (pre‑firearm) (D)
    - Thrown (D)
      - Examples (T): Throwing_Axe; Throwing_Knife; Boomerang; Plumbata
    - Bows (D)
      - Examples (T): Longbow; Composite_Bow; Recurve_Bow
    - Crossbows (D)
      - Examples (T): Crossbow; Arbalest; Repeating_Crossbow
    - Siege_Engines (D)
      - Examples (T): Ballista; Catapult; Trebuchet; Battering_Ram
  - Firearms (D)
    - By_Ignition_System (D)
      - Matchlock (D)
        - Examples (T): Tanegashima_Matchlock; Arquebus
      - Wheellock (D)
        - Examples (T): Wheellock_Pistol
      - Flintlock (D)
        - Examples (T): Brown_Bess_Musket; Charleville_Musket; Flintlock_Pistol
      - Percussion (D)
        - Examples (T): Percussion_Cap_Rifle; Caplock_Pistol
      - Cartridge_Centerfire (D)
        - Examples (T): Mauser_98; Lee_Enfield; AK_47; AR_15
    - By_Action (D)
      - Single_Shot (D)
      - Revolver (D)
      - Bolt_Action (D)
      - Lever_Action (D)
      - Pump_Action (D)
      - Semi_Automatic (D)
      - Automatic (D)
    - By_Form_Factor/Role (D)
      - Handguns (D)
        - Examples (T): Service_Pistol; Revolver_Model_1895
      - Long_Guns (D)
        - Examples (T): Musket; Rifle; Carbine; Shotgun
      - Submachine_Guns (D)
        - Examples (T): MP40; Thompson
      - Machine_Guns (D)
        - Examples (T): Bren; MG42; M2_Browning (HMG)
      - Assault_Rifles (D)
        - Examples (T): AK_47; StG_44; M16
      - Battle_Rifles (D)
        - Examples (T): FN_FAL; G3
      - PDWs (D)
        - Examples (T): P90; MP7
    - Shotgun_Ammunition_Types (D)
      - Examples (T): Buckshot; Birdshot; Slug (as T-types or properties)
  - Explosives & Ordnance (D)
    - Grenades (D)
      - Examples (T): Fragmentation_Grenade; Incendiary_Grenade; Smoke_Grenade
    - Mines (D)
      - Examples (T): Anti_Personnel_Mine; Anti_Tank_Mine
    - Rockets (D)
      - Examples (T): Unguided_Rocket; RPG_7
    - Missiles (D)
      - Examples (T): Guided_Missile; MANPADS
    - Artillery (D)
      - Examples (T): Cannon; Howitzer; Mortar; Field_Gun
    - Air_Delivered_Bombs (D)
      - Examples (T): General_Purpose_Bomb; Incendiary_Bomb
    - Naval_Ordnance (D)
      - Examples (T): Torpedo; Naval_Gun; Depth_Charge
  - Non_Lethal_Weapons (D)
    - Examples (T): Baton; Taser; Pepper_Spray; Tear_Gas_Dispenser

Suggested clusters under this tree (illustrative)
- Adoption_of_Matchlock_in_Japan_1540s (cluster) — parent: Matchlock (D)
- Longbow_in_Hundred_Years_War (cluster) — parent: Bows (D)
- Rise_of_Assault_Rifles_1940s_1960s (cluster) — parent: Assault_Rifles (D)
