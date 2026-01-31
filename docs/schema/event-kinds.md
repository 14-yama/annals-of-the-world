# Event Kind Vocabulary

This document defines the canonical `kind` values for `:Event` nodes. Every Event node **must** have a `kind` property.

## Purpose

The `kind` property categorizes events by their nature (e.g., Battle, Council, Execution), enabling:
- Filtering and faceted search (e.g., "show all Councils")
- Event-specific queries (e.g., all Battles in a timeframe)
- Consistent data modeling across clusters
- Visualization by event type

## Canonical Event Kinds

| Kind | Description | Examples |
|------|-------------|----------|
| **Battle** | Armed military engagement | `Battle_of_White_Mountain_1620`, `Kappel_Wars_1529_1531` |
| **Council** | Ecclesiastical or political assembly/synod | `Council_of_Trent_Sessions_*`, `Council_of_Constance_1414_1418`, `Synod_of_Dordt_1618_1619` |
| **Controversy** | Theological or political dispute/debate | `Arminius_Controversy_1603_1609`, `Vestiarian_Controversy_1566`, `Martin_Marprelate_Controversy_1588_1589` |
| **Covenant** | Divine/legal covenant or treaty | `Abrahamic_Covenant`, `Sinai_Covenant` |
| **Debate** | Formal theological disputation | `Leipzig_Debate_1519`, `Marburg_Colloquy_1529`, `Zurich_Disputations_1523`, `Bern_Disputation_1528` |
| **Decree** | Official proclamation, edict, or law | `Edict_of_Milan_313`, `Edict_of_Nantes_Passage_1598`, `Antiochus_IV_Decrees`, `Nuremberg_Laws_1935` |
| **Execution** | State-sanctioned killing of an individual | `Execution_of_Anne_Boleyn_1536`, `Hus_Execution_1415`, `Servetus_Execution_1553` |
| **Exile** | Forced displacement of a population | `Babylonian_Exile`, `Expulsion_from_Spain_1492`, `Exile_of_Socinians_1658` |
| **Founding** | Establishment of an institution or organization | `Founding_of_Society_of_Jesus_1540`, `Founding_of_Unitas_Fratrum_1457`, `Academy_Founding_1559` |
| **Legislative** | Parliamentary/assembly passage of laws | `Act_of_Supremacy_1534`, `Settlement_Passage`, `Golden_Act_Passage_1592` |
| **Marriage** | Union of two persons | `Marriage_Anne_Boleyn_Henry_VIII`, `Marriage_Mary_I_Philip_II_of_Spain` |
| **Martyrdom** | Death for religious beliefs (non-state or early church) | `Oxford_Martyrs_1555_1556`, `Ignatian_Martyrdom`, `Martyrdoms_in_Lyons_177` |
| **Migration** | Mass movement of peoples | `Almohad_Pressures_and_Migration`, `Hutterite_Migrations_16c`, `Mennonite_Organizing_1550s_1570s` |
| **Mission** | Evangelistic or diplomatic mission | `Jesuit_Mission_1580s`, `Seminary_Priests_Mission_1580s`, `Pauline_Mission_Journeys` |
| **Persecution** | Systematic oppression of a group | `Decian_Persecution_250`, `Diocletianic_Persecution_303`, `Heresy_Persecutions`, `Black_Death_Persecutions_1348_1351` |
| **Plot** | Conspiracy or failed coup | `Babington_Plot_1586`, `Ridolfi_Plot_1571`, `Throckmorton_Plot_1583` |
| **Publication** | Major text publication or translation project | `Kralice_Bible_Publication_1579_1593`, `Wartburg_Translation_1521_1522`, `Printing_Revolution` |
| **Rebellion** | Armed uprising against authority | `Pilgrimage_of_Grace_1536`, `Munster_Rebellion_1534_1535`, `Northern_Rebellion_1569`, `Bar_Kokhba_Revolt` |
| **Reform** | Religious or institutional reform program | `Basel_Reform_1529`, `Hezekiah_Reforms`, `Josiah_Reforms`, `Yavneh_Reform` |
| **Reign** | Period of rule or regency | `Lady_Jane_Grey_Reign_1553` |
| **Rite** | Religious ceremony or ritual practice | `Temple_Rituals`, `First_Adult_Baptisms_Zurich_1525`, `Abolition_of_the_Mass_Zurich_1525` |
| **Sacred** | Miraculous/divine event in religious narrative | `Exodus`, `Crucifixion`, `Resurrection_Proclamations`, `Pentecost`, `Binding_of_Isaac` |
| **Siege** | Military encirclement of a place | `Assyrian_Siege_of_Jerusalem_701_BCE`, `Babylonian_Siege_597_BCE`, `Siege_of_St_Andrews_Castle_1546_1547` |
| **Trial** | Legal proceeding against an individual | `Trial_of_Mary_Queen_of_Scots_1586`, `Eichmann_Trial_1961` |
| **War** | Extended military conflict | `Hussite_Wars_1419_1434`, `Schmalkaldic_War_1546_1547`, `Counts_War_1534_1536`, `First_War_of_Religion_1562_1563` |

## Selecting a Kind

1. **Prefer specificity**: Use `Execution` over `Persecution` for a single individual's death; use `Rebellion` over `War` for internal uprisings.
2. **One kind per event**: If an event spans multiple categories, choose the dominant aspect.
3. **Consult examples**: Match your event to similar ones in the table above.

## Usage in Data

```json
{
  "slug": "Diet_of_Worms_1521",
  "name": "Diet of Worms 1521",
  "label": "Event",
  "kind": "Council",
  "description": "Imperial assembly where Luther defended his writings..."
}
```

## Cypher Queries

```cypher
// Count events by kind
MATCH (e:Event)
RETURN e.kind AS kind, count(*) AS n
ORDER BY n DESC;

// Find all Councils
MATCH (e:Event {kind: "Council"})
RETURN e.slug, e.name, e.cluster
ORDER BY e.slug;

// Events missing kind
MATCH (e:Event) WHERE e.kind IS NULL
RETURN e.slug, e.cluster LIMIT 50;
```

## Adding New Kinds

New kinds require governance approval. Propose via PR with:
- Kind name (PascalCase, singular)
- Clear definition
- At least 3 example events
- Justification for why existing kinds don't fit

---
_Last updated: 2026-01-23_
