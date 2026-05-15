#!/usr/bin/env python3
"""
Batch 75 — 8 entities: Theodorus Bailey, William Dunn Moseley, Ezra Butler,
Perry Smith, François Scheffer, Jacques Defermon, John Stafford, Andrés Quintana Roo
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()


def enrich_entity(slug, data):
    fname = os.path.join(FOLDER, f"230{slug}.json")
    if not os.path.exists(fname):
        print(f"  SKIP (not found): {fname}"); return
    with open(fname, "r", encoding="utf-8") as f:
        doc = json.load(f)
    entity = doc["entities"][0]
    det = json.loads(entity.get("detailsJson", "{}"))
    edit_log = det.get("_editLog", [])
    for field in ("summary", "importanceScore", "historicalSignificance"):
        if field in data:
            old = entity.get(field)
            entity[field] = data[field]
            edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                             "oldValue": str(old)[:300], "newValue": str(data[field])[:300]})
    for field in ("causes", "effects", "relationships"):
        if field in data:
            old = det.get(field, [])
            det[field] = data[field]
            edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                             "oldValue": json.dumps(old)[:300], "newValue": json.dumps(data[field])[:300]})
    det["_editLog"] = edit_log
    det["_unsyncedEdits"] = True
    entity["_unsyncedEdits"] = True
    entity["detailsJson"] = json.dumps(det, ensure_ascii=False)
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    slen = len(entity.get("summary", ""))
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes',[]))} "
          f"e={len(det.get('effects',[]))}")


ENTITIES = [

    ("theodorus-bailey", {
        "summary": (
            "Theodorus Bailey (1758–1828) "
            "was an American Democratic-Republican "
            "politician from New York "
            "who served in the U.S. "
            "House (1793–1797 and 1799–1803) "
            "and as U.S. Senator "
            "(1803–1804). He was "
            "also the Postmaster "
            "of New York City "
            "(1804–1817) — one of "
            "the most politically "
            "significant patronage "
            "positions in early "
            "America, since the "
            "New York City post "
            "office was the "
            "busiest and most "
            "important in the "
            "United States.\n\n"
            "Bailey served during "
            "the critical period "
            "of New York's political "
            "transformation — the "
            "years when Aaron Burr's "
            "faction, the Clintonians, "
            "and the Livingstons "
            "were competing for "
            "control of New York "
            "Democratic-Republican "
            "politics.\n\n"
            "His congressional "
            "service spanned the "
            "Jay Treaty controversy, "
            "the quasi-war with "
            "France, and the "
            "beginning of the "
            "Jefferson era.\n\n"
            "His postmastership "
            "gave him significant "
            "patronage influence "
            "in New York's "
            "political machine."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "New York Democratic-Republican Congressman (1793–1797, 1799–1803), Senator (1803–1804), and NYC Postmaster (1804–1817); served during Jay Treaty controversy, quasi-war, and Jefferson era; NYC Postmaster was one of the most significant patronage posts in early America; navigated New York's complex Burr-Clinton-Livingston factional politics.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New York's fractious Democratic-Republican politics — the competition between the Burr faction, the Clintonians, and the Livingstons for control of New York's Democratic-Republican party — created the complex political environment Bailey navigated",
            "The New York City Postmaster position's significance — the control of the most important postal hub in America gave the postmaster significant patronage, information, and political influence — created the institutional basis for Bailey's long post-congressional career",
            "The Jay Treaty and quasi-war controversies — the foreign policy crises of the mid-1790s that defined the Federalist-Republican party division — created the major political context for Bailey's early congressional terms"
        ],
        "effects": [
            "His thirteen-year NYC Postmastership contributed to the operation of the nation's most important postal hub — managing communications through one of the most politically and commercially significant cities in America during the early Republic",
            "His congressional service contributed New York's Democratic-Republican perspective to the Jay Treaty, quasi-war, and early Jefferson administration debates — the founding generation's critical foreign policy and constitutional controversies",
            "His career contributed to the patronage tradition of American politics — the system by which party loyalists received significant government positions as rewards for political support that would become the spoils system",
            "His navigation of New York factional politics contributed to the Democratic-Republican party's complex internal dynamics — the struggles that would eventually produce the Albany Regency and Van Buren's systematic political organization"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New York Congressman 1793–1797 and 1799–1803"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "New York Senator 1803–1804"},
            {"target": "us-postal-service", "verb": "LEADS", "note": "NYC Postmaster 1804–1817"},
            {"target": "jay-treaty", "verb": "SERVES_DURING", "note": "Congressman during the Jay Treaty controversy"},
            {"target": "new-york", "verb": "REPRESENTS", "note": "New York Democratic-Republican political figure"}
        ]
    }),

    ("william-dunn-moseley", {
        "summary": (
            "William Dunn Moseley "
            "(1795–1863) was an American "
            "Democratic politician who "
            "served as the first "
            "Governor of Florida "
            "(1845–1849) — elected "
            "when Florida was admitted "
            "to the Union on March "
            "3, 1845, as the 27th "
            "state. Moseley's governorship "
            "was therefore literally "
            "Florida's founding "
            "executive term — the "
            "first government of "
            "a territory that had "
            "been under Spanish, "
            "British, and finally "
            "American control.\n\n"
            "Florida's admission "
            "was paired with the "
            "admission of Iowa "
            "as a free state "
            "to maintain the "
            "slave-free state "
            "balance — the "
            "political balancing "
            "act that had governed "
            "territorial admissions "
            "since the Missouri "
            "Compromise (1820).\n\n"
            "As first governor, "
            "Moseley had to "
            "build Florida's "
            "state government "
            "from scratch — "
            "creating the institutions, "
            "appointing officials, "
            "and establishing "
            "the practices of "
            "a new American state "
            "from the foundation.\n\n"
            "He was born in "
            "North Carolina before "
            "moving to Florida."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "First Governor of Florida (1845–1849); Florida admitted to the Union March 3, 1845 as the 27th state paired with Iowa to maintain slave-free balance; Moseley literally founded Florida's state government and institutions; served during the Mexican-American War; his term established the foundations of Florida statehood.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Florida's territorial development — the growth of Florida's population and economy after the Second Seminole War (1835–1842) cleared much of the territory of Native American resistance — created the conditions for statehood and Moseley's election",
            "The slave-free state balance requirement — the political necessity of pairing each new slave state with a new free state to maintain Senate balance — created the specific political context for Florida's admission alongside Iowa",
            "The Democratic Party's territorial expansion policy — Polk's expansionist agenda that was acquiring California and the Southwest from Mexico while also admitting new states — created the broader context for Florida's statehood"
        ],
        "effects": [
            "His founding governorship established Florida's state government from scratch — creating the executive institutions, appointing the first state officials, and establishing the administrative practices that would govern Florida for generations",
            "His term governed Florida through the Mexican-American War — managing a new frontier state while the nation was at war and acquiring vast new territories that would reopen the slavery extension controversy",
            "His first-governor status gave him historical significance disproportionate to the short duration and modest achievements of his term — the founding executive of a state has inherent historical importance as an institution-builder",
            "His Democratic alignment contributed Florida to the Southern Democratic bloc — the slave state that would remain in the Democratic column until the Civil War and then through the Solid South era to the Civil Rights era's political realignment"
        ],
        "relationships": [
            {"target": "florida", "verb": "GOVERNS_AS_FIRST", "note": "First Governor of Florida 1845–1849"},
            {"target": "florida-statehood", "verb": "INAUGURATES", "note": "Governor at Florida's admission to the Union"},
            {"target": "iowa", "verb": "ADMITTED_WITH", "note": "Florida paired with Iowa to balance slave-free admissions"},
            {"target": "james-k-polk", "verb": "SERVES_DURING", "note": "Governor during Polk's expansionist presidency"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Florida Democrat establishing state government"}
        ]
    }),

    ("ezra-butler", {
        "summary": (
            "Ezra Butler (1763–1838) "
            "was an American Democratic-Republican "
            "politician and Congregationalist "
            "minister from Vermont who "
            "served as Governor of "
            "Vermont (1826–1828) during "
            "the final years of the "
            "Era of Good Feelings "
            "and the opening of the "
            "Jacksonian democratic "
            "realignment. Butler "
            "represented Vermont's "
            "distinctive civic "
            "tradition — the "
            "combination of Congregationalist "
            "Protestantism, New England "
            "educational values, "
            "and democratic republican "
            "politics that made "
            "Vermont one of the "
            "most intellectually "
            "and morally distinguished "
            "small states in the Union.\n\n"
            "His gubernatorial "
            "term coincided with "
            "the contested 1824 "
            "and 1828 presidential "
            "elections — the "
            "end of one-party "
            "Democratic-Republican "
            "dominance and the "
            "emergence of the "
            "Adams-Jackson competition "
            "that would reshape "
            "American party politics.\n\n"
            "Vermont's small size "
            "but moral weight "
            "in antislavery "
            "politics gave its "
            "governors a significance "
            "beyond their state's "
            "population.\n\n"
            "He died in 1838 "
            "after a long ministry."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Governor of Vermont (1826–1828) and Congregationalist minister; served during the transition from the Era of Good Feelings to the Jacksonian realignment; represented Vermont's distinctive combination of Protestant civic culture and democratic republicanism; governor during the contested 1828 election that brought Jackson to power.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Vermont's Congregationalist civic tradition — the established Protestant educational and moral culture that linked church, school, and republican civic life in a way unique to New England — created the environment for Butler's dual career as minister and politician",
            "The Era of Good Feelings' breakdown — the collapse of one-party Democratic-Republican dominance into the Adams-Jackson factional competition of 1824–1828 — created the political transition that Butler's governorship bridged",
            "Vermont's antislavery political culture — the state's early and strong opposition to slavery that would eventually make it the most reliably antislavery in the Union — informed the moral dimension of Butler's civic and political career"
        ],
        "effects": [
            "His governorship contributed to Vermont's governance during the political transition from Monroe's Era of Good Feelings to Jackson's populist democracy — managing a state whose civic traditions were deeply resistant to Jacksonian demagoguery",
            "His combined ministry and politics illustrated Vermont's distinctive civic tradition — the way Protestant moral values and democratic republican politics were more thoroughly integrated in Vermont than anywhere else in America",
            "His career contributed to the Vermont political tradition that would eventually produce the state's consistent antislavery Whig and then Republican alignment — the moral politics that made Vermont the Union's most principled antislavery state",
            "His death in 1838 placed him among the founding generation who built Vermont's distinguished civic tradition but did not live to see its antislavery politics' fulfillment in the Civil War"
        ],
        "relationships": [
            {"target": "vermont", "verb": "GOVERNS", "note": "Governor of Vermont 1826–1828"},
            {"target": "congregationalist-church", "verb": "SERVES_IN", "note": "Vermont Congregationalist minister"},
            {"target": "era-of-good-feelings", "verb": "GOVERNS_DURING", "note": "Governor during Monroe era's final years"},
            {"target": "andrew-jackson", "verb": "GOVERNS_DURING", "note": "Governor during the 1828 Jacksonian realignment"},
            {"target": "vermont-antislavery-tradition", "verb": "CONTRIBUTES_TO", "note": "Part of Vermont's moral-civic political tradition"}
        ]
    }),

    ("perry-smith", {
        "summary": (
            "Perry Smith (1783–1852) "
            "was an American Democratic "
            "politician from Connecticut "
            "who served in the U.S. "
            "Senate (1837–1843) during "
            "the Van Buren and Tyler "
            "administrations — the "
            "Panic of 1837 and its "
            "political aftermath. "
            "As a Connecticut Democrat, "
            "Smith represented a "
            "minority position in "
            "the most reliably "
            "Federalist and then "
            "Whig state in New "
            "England — Connecticut's "
            "Standing Order tradition "
            "made it one of the "
            "most Federalist-friendly "
            "states, and Connecticut "
            "Democrats were often "
            "fighting against the "
            "dominant Whig political "
            "culture.\n\n"
            "His Senate tenure "
            "coincided with the "
            "most economically "
            "disruptive period "
            "of the antebellum "
            "era — the Panic "
            "of 1837's depression "
            "and the political "
            "battles over the "
            "Independent Treasury "
            "that Van Buren and "
            "his supporters advocated "
            "as the Democratic "
            "response.\n\n"
            "Connecticut's manufacturing "
            "economy — the early "
            "industrialization "
            "that was transforming "
            "the state — created "
            "complex economic "
            "interests that shaped "
            "Smith's Senate position.\n\n"
            "He was a lawyer "
            "before entering politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Connecticut Democratic Senator (1837–1843); minority Democrat in a reliably Whig-Federalist state; served during the Panic of 1837 and the Independent Treasury debates; represented Connecticut's manufacturing interests in the Senate; navigated the Van Buren and Tyler administrations' economic controversies.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Connecticut's complex politics — the tension between the state's dominant Federalist-Whig Standing Order tradition and the minority Democratic constituency among laborers, immigrants, and those hostile to the religious establishment — created the challenging political environment for Smith's Democratic career",
            "The Panic of 1837 — the severe economic depression that devastated Van Buren's presidency — created the major economic crisis that dominated Smith's entire Senate tenure",
            "Connecticut's early industrialization — the factory system developing in the Connecticut River valley and along the coast — created the manufacturing constituency whose economic interests Smith had to represent alongside the state's commercial and agricultural interests"
        ],
        "effects": [
            "His Senate service contributed Connecticut's minority Democratic votes to the Van Buren and Tyler era's economic policy debates — supporting the Independent Treasury as the Democratic response to the Panic of 1837",
            "His career contributed to the development of Connecticut Democratic politics — the minority party that challenged the Whig establishment and eventually built the working-class immigrant coalition that would make Connecticut a Democratic state by the mid-20th century",
            "His Senate tenure illustrated the competitive political dynamics of Connecticut — a state with genuine two-party competition despite its Whig-leaning tradition",
            "His death in 1852 placed him among the Jacksonian Democrats who saw the beginnings of the slavery extension crisis that would transform both parties"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Connecticut Senator 1837–1843"},
            {"target": "martin-van-buren", "verb": "SUPPORTS", "note": "Democrat serving during Van Buren presidency"},
            {"target": "independent-treasury", "verb": "SUPPORTS", "note": "Senate support for Democratic economic policy"},
            {"target": "panic-of-1837", "verb": "SERVES_DURING", "note": "Senator through the economic depression"},
            {"target": "connecticut", "verb": "REPRESENTS", "note": "Minority Democrat in Whig-dominated Connecticut"}
        ]
    }),

    ("françois-scheffer", {
        "summary": (
            "François Scheffer (1796–1839) "
            "was a Dutch-born French "
            "painter of the Romantic "
            "era, younger brother "
            "of the more famous "
            "Ary Scheffer. Though "
            "less celebrated than "
            "his brother, François "
            "Scheffer contributed "
            "to the Dutch-French "
            "artistic exchange "
            "of the Restoration "
            "and July Monarchy "
            "periods — the era "
            "when Romantic painting's "
            "emotional intensity "
            "and literary subjects "
            "were transforming "
            "European art. Both "
            "brothers were born "
            "in Dordrecht and "
            "moved to Paris, "
            "where they became "
            "part of the French "
            "Romantic movement "
            "while retaining Dutch "
            "artistic sensibilities.\n\n"
            "The Romantic movement "
            "in painting — associated "
            "with Géricault, "
            "Delacroix, and in "
            "Germany with Friedrich "
            "— emphasized emotional "
            "power, historical "
            "and literary subjects, "
            "and the sublime over "
            "the Neoclassical "
            "restraint and classical "
            "subjects that had "
            "dominated.\n\n"
            "François Scheffer "
            "worked in Paris during "
            "the Napoleon-Restoration-"
            "July Monarchy transition.\n\n"
            "He died young at 43, "
            "limiting his potential impact."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Dutch-born French Romantic painter (1796–1839); younger brother of Ary Scheffer; contributed to Dutch-French artistic exchange in the Restoration and July Monarchy era; part of the Romantic painting movement transforming European art; died young at 43.",
            "significanceCategory": "local"
        },
        "causes": [
            "The Romantic movement in European art — the reaction against Neoclassicism that emphasized emotional power, literary subjects, and historical drama — created the artistic movement within which François Scheffer worked",
            "The Scheffer family's Dutch-French artistic identity — the brothers' upbringing in Dordrecht and relocation to Paris where they encountered the French Romantic movement while retaining Dutch artistic sensibilities — created the distinctive cross-cultural perspective of François's work",
            "The July Monarchy's cultural flourishing — Louis-Philippe's patronage of the arts and the cultural excitement of Paris in the 1830s, when Romanticism was at its height — created the artistic environment of Scheffer's most productive years"
        ],
        "effects": [
            "His paintings contributed to the Dutch-French artistic exchange — the transmission of Dutch artistic traditions and sensibilities into the French Romantic movement that his brother Ary more prominently embodied",
            "His career contributed to the Paris artistic scene of the 1830s — the cultural moment when Romantic painting was at its height and the city was the world's artistic capital",
            "His early death limited his potential contribution — his 43 years cut short a career that might have developed distinctive achievements comparable to his brother Ary's celebrated religious and literary paintings",
            "His career illustrated the pattern of artistic families in the Romantic era — the brothers, apprenticeships, and family connections that characterized how artistic training and identity were transmitted"
        ],
        "relationships": [
            {"target": "ary-scheffer", "verb": "FAMILY_OF", "note": "Younger brother of the more famous Romantic painter"},
            {"target": "romantic-movement", "verb": "CONTRIBUTES_TO", "note": "French Romantic painter in the Géricault-Delacroix era"},
            {"target": "july-monarchy", "verb": "WORKS_DURING", "note": "Painter during Louis-Philippe's cultural patronage"},
            {"target": "french-painting", "verb": "CONTRIBUTES_TO", "note": "Dutch-born French Romantic artist"},
            {"target": "paris", "verb": "WORKS_IN", "note": "Based in Paris during Romantic movement's height"}
        ]
    }),

    ("jacques-defermon", {
        "summary": (
            "Jacques Defermon des Chapeliéres "
            "(1752–1831) was a French "
            "Revolutionary and Napoleonic "
            "administrator who served "
            "as a member of the Council "
            "of Five Hundred, the "
            "Council of State, and "
            "as a Count of the Empire. "
            "He was one of the "
            "administrators and "
            "legislators who served "
            "across the entire arc "
            "of Revolutionary, "
            "Consular, and Imperial "
            "France — the rare figures "
            "who survived and served "
            "across all phases of "
            "the political transformation "
            "from 1789 to 1815.\n\n"
            "Defermon was particularly "
            "associated with financial "
            "administration — "
            "contributing to the "
            "Napoleonic era's "
            "systematic reconstruction "
            "of French state finances "
            "after the Revolutionary "
            "chaos. The Napoleonic "
            "system's extraordinary "
            "effectiveness in "
            "mobilizing French "
            "resources for war "
            "depended on competent "
            "financial administration "
            "of the kind Defermon "
            "contributed.\n\n"
            "His elevation to Count "
            "of the Empire reflected "
            "Napoleon's policy of "
            "creating a new nobility "
            "from Revolutionary "
            "administrators who "
            "had demonstrated competence.\n\n"
            "He survived the "
            "Restoration and lived "
            "until 1831."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French Revolutionary and Napoleonic administrator (1752–1831); member of the Council of Five Hundred, Council of State, and Count of the Empire; served across Revolutionary, Consular, and Imperial France; contributed to Napoleonic financial administration that mobilized French resources for war; survived the Restoration.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French Revolution — the political upheaval that destroyed the old regime and created the opportunities for new administrators like Defermon to rise based on competence rather than birth — created the institutional vacuum within which his career developed",
            "Napoleon's administrative revolution — the systematic reconstruction of French state institutions, financial administration, and governance after the Revolutionary chaos — created the demand for competent, loyal administrators that Defermon provided",
            "The Council of State's role in Napoleonic governance — Napoleon's advisory and administrative council that coordinated the vast project of legal and institutional reconstruction — created the institutional home for Defermon's service"
        ],
        "effects": [
            "His financial administration contributions helped sustain the Napoleonic war machine — the extraordinary French military capacity that dominated Europe for fifteen years depended on effective extraction and mobilization of French economic resources",
            "His Council of State service contributed to the development of the Napoleonic administrative state — the centralized, rational bureaucracy that Napoleon built and that outlasted his empire, becoming a model for 19th-century European state-building",
            "His elevation to the counts of the Empire illustrated Napoleon's deliberate policy of creating a new service nobility — rewarding administrative competence with noble titles to create a loyal ruling class",
            "His survival through the Restoration (dying 1831) illustrated the pragmatism of post-Napoleonic French politics — the way many Napoleonic administrators were retained by the Bourbon restoration because their administrative skills were indispensable"
        ],
        "relationships": [
            {"target": "council-of-five-hundred", "verb": "SERVES_IN", "note": "Member of the Revolutionary legislative council"},
            {"target": "council-of-state-france", "verb": "SERVES_IN", "note": "Napoleonic Council of State member"},
            {"target": "napoleon-bonaprte", "verb": "SERVES_UNDER", "note": "Napoleonic administrator elevated to Count of the Empire"},
            {"target": "french-revolutionary-administration", "verb": "CONTRIBUTES_TO", "note": "Served across Revolutionary, Consular, and Imperial France"},
            {"target": "napoleonic-financial-system", "verb": "ADMINISTERS", "note": "Contributed to French financial administration"}
        ]
    }),

    ("john-stafford", {
        "summary": (
            "John Stafford (1768–1823) "
            "was an American Federalist "
            "politician from New York "
            "who served in the U.S. "
            "House of Representatives "
            "(1813–1815) during the "
            "War of 1812 — one of "
            "the most divisive "
            "and controversial wars "
            "in American history, "
            "bitterly opposed by "
            "the New England Federalists "
            "whose commercial ties "
            "to Britain were disrupted "
            "by the conflict. As "
            "a New York Federalist, "
            "Stafford occupied "
            "the opposition benches "
            "during the war — "
            "a minority position "
            "as New York was "
            "gradually shifting "
            "from its Federalist "
            "tradition toward "
            "Democratic-Republicanism.\n\n"
            "The War of 1812 "
            "House debates were "
            "among the most "
            "contentious in early "
            "American history — "
            "Federalist members "
            "from New England "
            "and New York questioning "
            "the war's causes, "
            "conduct, and costs.\n\n"
            "The Hartford Convention "
            "(December 1814) — "
            "the New England "
            "Federalists' anti-war "
            "meeting — was the "
            "most dramatic expression "
            "of this opposition.\n\n"
            "He died young at 55 "
            "in 1823."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "New York Federalist Congressman (1813–1815) during the War of 1812; minority war opponent as Federalists challenged the war's conduct; served during the Hartford Convention protests; part of the dying New York Federalism as the state shifted to Democratic-Republicanism.",
            "significanceCategory": "local"
        },
        "causes": [
            "The War of 1812 — the declaration of war against Britain that the Federalists bitterly opposed as damaging to New England commerce and constitutionally overreaching — created the defining controversy of Stafford's congressional service",
            "New York's Federalist minority — the remnant Federalist constituency in New York state, primarily merchants and professionals tied to British trade, that maintained anti-war opposition — created the political base for Stafford's election",
            "The Madison administration's war leadership — the controversial conduct of the war, including the British burning of Washington and the near-fall of Baltimore — created the Federalist critique that Stafford contributed to in the House"
        ],
        "effects": [
            "His House service contributed New York's Federalist anti-war votes to the War of 1812 debates — maintaining the opposition voice that challenged the Madison administration's conduct of the conflict",
            "His career contributed to the last phase of New York Federalism — the minority party that was being driven from New York politics by the Clintonian and Tammany Democratic-Republican coalitions",
            "His service illustrated the geographic pattern of anti-war sentiment — concentrated in the commercial northeast where British trade ties were strongest and the disruption of maritime commerce most acute",
            "His death in 1823 placed him among the Federalists who did not live to see the complete transformation of American politics into the Jacksonian era that obliterated Federalism entirely"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New York Congressman 1813–1815"},
            {"target": "federalist-party-united-states", "verb": "MEMBER_OF", "note": "New York Federalist anti-war congressman"},
            {"target": "war-of-1812", "verb": "OPPOSES", "note": "Federalist opponent of the war's conduct"},
            {"target": "hartford-convention", "verb": "CONTEMPORANEOUS_WITH", "note": "Congressman during New England's anti-war protests"},
            {"target": "new-york", "verb": "REPRESENTS", "note": "New York's minority Federalist constituency"}
        ]
    }),

    ("andrés-quintana-roo", {
        "summary": (
            "Andrés Quintana Roo "
            "(1787–1851) was a Mexican "
            "patriot, lawyer, journalist, "
            "and poet who played a "
            "significant role in "
            "Mexico's independence "
            "movement (1810–1821) "
            "and the founding of "
            "the Mexican Republic. "
            "He served as a prominent "
            "propagandist and publicist "
            "for the independence "
            "movement — his journalistic "
            "work, particularly "
            "the newspaper 'El "
            "Ilustrador Americano' "
            "(1812–1813), helped "
            "articulate the "
            "independence cause "
            "to Spanish colonial "
            "society. The Mexican "
            "state of Quintana "
            "Roo — on the Yucatán "
            "Peninsula — is named "
            "in his honor.\n\n"
            "He was married to "
            "Leona Vicario — "
            "one of Mexico's "
            "most celebrated "
            "independence heroines "
            "who used her family "
            "wealth to fund the "
            "independence movement "
            "and whose image "
            "appears on the "
            "Mexican 200-peso bill.\n\n"
            "His subsequent career "
            "contributed to the "
            "Mexican Republic's "
            "political development "
            "— he served in "
            "Congress and in "
            "various governmental "
            "positions.\n\n"
            "A state named "
            "after him honors "
            "his memory."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Mexican independence patriot, journalist, and poet (1787–1851); editor of 'El Ilustrador Americano' (1812–1813) propagandizing for independence; married to independence heroine Leona Vicario; the Mexican state of Quintana Roo is named in his honor; contributed to founding the Mexican Republic; significant figure in Mexican national identity.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Mexico's independence movement — the armed struggle beginning with Hidalgo's 1810 Grito de Dolores that sought to overthrow Spanish colonial rule — created the political cause for which Quintana Roo served as journalist and propagandist",
            "The revolutionary journalism tradition — the use of clandestine newspapers and pamphlets to spread independence ideas and counter Spanish propaganda — created the role in which Quintana Roo made his distinctive contribution to the independence cause",
            "Leona Vicario's revolutionary engagement — her willingness to use her family's wealth to fund the independence movement and her marriage to Quintana Roo — created the family dimension of their joint contribution to Mexican independence"
        ],
        "effects": [
            "His 'El Ilustrador Americano' journalism contributed to articulating the independence cause — spreading independence ideas among the literate classes of colonial Mexico and countering Spanish colonial propaganda",
            "His marriage to Leona Vicario combined two of the independence movement's most significant contributors — creating a household that was both intellectually and financially central to the patriot cause",
            "His post-independence career contributed to building the Mexican Republic's institutions — the Congress service and governmental work that helped establish the new nation's political system",
            "His lasting memorialization in the naming of Quintana Roo state confirmed his place in Mexican national identity — the posthumous honor that placed him among the most celebrated figures of Mexican independence"
        ],
        "relationships": [
            {"target": "mexican-independence", "verb": "ADVOCATES_FOR", "note": "Independence journalist and publicist"},
            {"target": "leona-vicario", "verb": "MARRIED_TO", "note": "Husband of Mexico's independence heroine"},
            {"target": "el-ilustrador-americano", "verb": "EDITS", "note": "Editor of independence newspaper 1812–1813"},
            {"target": "mexico", "verb": "HELPS_FOUND", "note": "Contributor to founding the Mexican Republic"},
            {"target": "quintana-roo-state", "verb": "NAMED_FOR", "note": "Mexican state named in his honor"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 75 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
