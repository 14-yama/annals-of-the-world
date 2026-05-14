#!/usr/bin/env python3
"""
Batch 63 — 8 entities: Ralph de Warneville, Jean-Pierre-André Amar,
Ray Greene, Nathaniel Boyden, Calvin Willey, Jakob Edvard Colbjørnsen,
Marie-Jean Hérault de Séchelles, Jules Armand Dufaure
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

    ("ralph-de-warneville", {
        "summary": (
            "Ralph de Warneville (died 1183) was "
            "an Anglo-Norman churchman and royal "
            "administrator who served as Lord "
            "Chancellor of England (1173–1180) "
            "under Henry II — one of the most "
            "important administrative positions "
            "in the Angevin empire at a moment "
            "when Henry II was rebuilding "
            "royal authority after the trauma "
            "of Thomas Becket's murder (1170) "
            "and the great rebellion of 1173–1174 "
            "by his own sons.\n\n"
            "De Warneville served in the "
            "chancery tradition — the royal "
            "writing office that produced "
            "the king's writs, charters, "
            "and administrative documents. "
            "Henry II's chancery was one "
            "of the most sophisticated "
            "administrative machines in "
            "twelfth-century Europe, and "
            "the Chancellor occupied the "
            "second most important position "
            "in the royal government after "
            "the king himself.\n\n"
            "His chancellorship came in "
            "the shadow of Thomas Becket's "
            "martyrdom — the murder in "
            "Canterbury Cathedral that had "
            "transformed the former Chancellor "
            "into a saint and had forced "
            "Henry II to perform public "
            "penance at Becket's tomb. "
            "De Warneville's administration "
            "of the chancery represented "
            "the post-Becket normalization "
            "of Henry II's government.\n\n"
            "He was also elected Bishop of "
            "Ely in 1173 but never consecrated."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Lord Chancellor of England (1173–1180) under Henry II; administered the Angevin royal chancery during the post-Becket period and after Henry's sons' great rebellion; elected but unconsecrated Bishop of Ely; central figure in the normalization of Henry II's government.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Henry II's need for administrative continuity after the twin crises of Becket's murder (1170) and his sons' great rebellion (1173–1174) — which had devastated the king's reputation and tested his government — created the demand for capable administrators like De Warneville to restore normal royal governance",
            "The development of the Angevin administrative machine under Henry II — the most sophisticated royal government in twelfth-century Europe, with its systematized exchequer, its common law courts, and its prolific chancery — created the institutional framework in which De Warneville's chancellorship operated",
            "The tradition of using senior churchmen as royal chancellors — combining ecclesiastical income and status with administrative service — provided the career model that De Warneville followed, though his election to Ely without consecration illustrated the occasional awkwardness of the church-state combination"
        ],
        "effects": [
            "His chancellorship contributed to the restoration of Angevin administrative normality after the post-Becket crisis — managing the royal writing office through the period when Henry II was rebuilding his authority and reputation",
            "His administration of the chancery contributed to the development of the English common law tradition — the systematic production of royal writs that Henry II's government used to extend royal jurisdiction at the expense of baronial and ecclesiastical courts",
            "The post-Becket administrative normalization that De Warneville's chancellorship represented contributed to Henry II's legacy as the greatest administrative king of the twelfth century — despite the Becket scandal, his government continued to function effectively",
            "His unconsecrated election to Ely illustrated the ongoing tensions between royal wishes and ecclesiastical canonical procedures that the Becket controversy had highlighted — even after the martyrdom, church-state relations in England remained complex"
        ],
        "relationships": [
            {"target": "lord-chancellor-england", "verb": "SERVES_AS", "note": "Lord Chancellor 1173–1180"},
            {"target": "henry-ii-england", "verb": "SERVES", "note": "Royal administrator under the Angevin king"},
            {"target": "thomas-becket", "verb": "SUCCEEDS_AFTER", "note": "Chancellor after Becket's martyrdom transformed the office"},
            {"target": "angevin-administrative-machine", "verb": "OPERATES", "note": "Managed Henry II's sophisticated royal chancery"},
            {"target": "bishop-of-ely", "verb": "ELECTED_BUT_NOT_CONSECRATED", "note": "Elected 1173 but never consecrated as bishop"}
        ]
    }),

    ("jean-pierre-andré-amar", {
        "summary": (
            "Jean-Pierre-André Amar (1755–1816) "
            "was a French revolutionary politician "
            "who served on the Committee of "
            "General Security — one of the two "
            "governing committees of the "
            "Committee of Public Safety system "
            "— and was a leading member of "
            "the Montagnard faction during "
            "the Terror. A lawyer from Grenoble "
            "who was elected to the National "
            "Convention, Amar became one "
            "of the most aggressive "
            "prosecutors of the Revolution's "
            "enemies, playing a key role "
            "in the arrest of the Girondins "
            "in June 1793.\n\n"
            "Amar became notorious for his "
            "report against the Girondins "
            "that led to their trial and "
            "execution — a document that "
            "helped consolidate Montagnard "
            "dominance over the Convention "
            "and the Committee of General "
            "Security's power to arrest "
            "and imprison political enemies.\n\n"
            "He was also responsible for "
            "the report denying women "
            "the right to form political "
            "clubs (1793) — one of the "
            "key moments in the Revolution's "
            "exclusion of women from "
            "formal political participation.\n\n"
            "After Thermidor he was accused "
            "and briefly imprisoned but "
            "survived to live into the "
            "Restoration, dying in 1816."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French revolutionary politician and Committee of General Security member; key prosecutor of the Girondins (1793); authored the report suppressing women's political clubs (1793); Montagnard Terror participant who survived Thermidor; represented the Revolution's authoritarian suppression of political diversity.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French Revolution's radicalization in 1792–1793 — the fall of the monarchy, the Brunswick Manifesto's threat to Paris, the September Massacres, and the Girondins' resistance to the Montagnards' centralizing agenda — created the conditions for the Terror and the Committee of General Security's expansion of political repression",
            "The Montagnards' struggle against the Girondins — the contest between the more radical Paris-based Montagnards and the more federalist Girondins for control of the National Convention — provided the political context for Amar's role as a Girondin prosecutor",
            "The Revolution's gender politics — the tension between the rhetoric of universal rights and the reality of women's exclusion from formal political participation — created the context for Amar's 1793 report suppressing women's political clubs, a key moment in the Revolution's hardening attitudes toward female political agency"
        ],
        "effects": [
            "His report against the Girondins — which led to the arrest, trial, and execution of the Girondin leaders — consolidated Montagnard dominance over the Convention and accelerated the Terror's most intensive phase",
            "His 1793 report suppressing women's political clubs — formally denying women the right to form political associations — was one of the most consequential gender-political decisions of the Revolution, contributing to the century-long exclusion of French women from formal political life",
            "His Thermidorian survival — despite his role in the Terror's most extreme phase — illustrated the pragmatic nature of Thermidorian justice, which targeted some terrorists while allowing others to survive and return to private life",
            "His career illustrated the Committee of General Security's function as the Terror's enforcement mechanism — the committee that directed the Revolutionary Tribunal's prosecutions and that was responsible for the political violence against the Revolution's enemies both real and imagined"
        ],
        "relationships": [
            {"target": "committee-of-general-security", "verb": "SERVES_ON", "note": "Member of the Terror's law enforcement committee"},
            {"target": "girondins", "verb": "PROSECUTES", "note": "Key prosecutor whose report led to Girondin executions"},
            {"target": "montagnards", "verb": "MEMBER_OF", "note": "Leading Montagnard in the National Convention"},
            {"target": "reign-of-terror", "verb": "PERPETRATES", "note": "Active participant in the Terror's repressive apparatus"},
            {"target": "women-french-revolution", "verb": "EXCLUDES", "note": "Authored 1793 report suppressing women's political clubs"}
        ]
    }),

    ("ray-greene", {
        "summary": (
            "Ray Greene (1765–1849) was an "
            "American Federalist politician "
            "from Rhode Island who served "
            "as Attorney General of Rhode "
            "Island and as a U.S. Senator "
            "(1797–1801) during the critical "
            "years of the Adams administration "
            "— the Quasi-War with France, "
            "the XYZ Affair, the Alien and "
            "Sedition Acts, and the political "
            "crisis that produced the "
            "'Revolution of 1800' bringing "
            "Thomas Jefferson to power.\n\n"
            "Greene was a Federalist in "
            "the mold of New England "
            "commercial interests — Rhode "
            "Island's mercantile economy "
            "and its connections to "
            "British trade made Federalism "
            "the natural political home "
            "for many of the state's "
            "commercial elite. His Senate "
            "service coincided with "
            "Federalism's last moment "
            "of national political power "
            "before Jefferson's victory "
            "decisively shifted control "
            "of the federal government "
            "to the Democratic-Republicans.\n\n"
            "His Senate tenure included "
            "the debates over the Alien "
            "and Sedition Acts — the "
            "controversial Federalist "
            "measures that criminalized "
            "political opposition to "
            "the Adams administration "
            "and that Jefferson and "
            "Madison challenged with "
            "the Virginia and Kentucky Resolutions.\n\n"
            "He lived until 1849, "
            "witnessing the entire Jacksonian era."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Rhode Island Federalist Senator (1797–1801) during the Quasi-War and Alien and Sedition Acts; served through Federalism's final years of national power before the Revolution of 1800; Attorney General of Rhode Island; long-lived witness (1765–1849) to the full transformation of American politics.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Rhode Island's mercantile economy and Federalist political tradition — the state's commercial ties to Britain and the Atlantic trade network, its merchant elite's interests in a strong national commercial policy, and its suspicion of French radicalism — created the political constituency for Greene's Federalist Senate career",
            "The Quasi-War crisis with France (1798–1800) — the undeclared naval war that followed the XYZ Affair and galvanized Federalist opinion against French revolutionary aggression — provided the political environment that made the Alien and Sedition Acts seem defensible to Federalists like Greene",
            "The Adams administration's political strategy — using the Quasi-War emergency to strengthen federal power, silence political opposition through the Sedition Act, and build up military strength — created the controversial context in which Greene's Senate service operated"
        ],
        "effects": [
            "His Senate vote on the Alien and Sedition Acts — among the most controversial legislation in early American history — placed him in the Federalist majority that passed these measures, contributing to the political backlash that helped end Federalism's national political dominance",
            "His Senate service contributed to the Federalist coalition's management of the Quasi-War crisis — supporting the Adams administration's naval build-up, the new army, and the measures to prepare the country for possible war with France",
            "His defeat in 1801 — as Jefferson's Revolution of 1800 transformed American politics — illustrated the scale of the political transformation that ended Federalism's national political power and began the Jeffersonian-Democratic-Republican era",
            "His long life (1765–1849) made him a living witness to the full political transformation from the Federalist era through Jacksonian Democracy — one of the last survivors of the generation that had known the Adams administration from the inside"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Rhode Island Senator 1797–1801"},
            {"target": "alien-and-sedition-acts", "verb": "VOTES_FOR", "note": "Federalist senator supporting the controversial acts"},
            {"target": "john-adams", "verb": "SUPPORTS", "note": "Federalist senator supporting the Adams administration"},
            {"target": "quasi-war", "verb": "SERVES_DURING", "note": "In Senate during the Quasi-War with France"},
            {"target": "federalist-party", "verb": "MEMBER_OF", "note": "Rhode Island Federalist politician"}
        ]
    }),

    ("nathaniel-boyden", {
        "summary": (
            "Nathaniel Boyden (1796–1873) was "
            "an American Whig and Republican "
            "politician from North Carolina "
            "who served in the U.S. House "
            "of Representatives (1847–1849) "
            "and briefly in the post-Civil "
            "War Reconstruction Congress "
            "(1868–1869). His career spanned "
            "the full arc of the antebellum "
            "political system — from the "
            "Whig Party through the "
            "sectional crisis to the Civil "
            "War's aftermath.\n\n"
            "Boyden was born in Massachusetts "
            "but settled in North Carolina — "
            "building a legal career in "
            "Salisbury that placed him "
            "in the Whig political tradition "
            "of the state's western Piedmont "
            "region. North Carolina's Whig "
            "Party drew support from the "
            "state's commercial and professional "
            "classes, its tobacco planters, "
            "and its western counties that "
            "felt underrepresented in a "
            "state dominated by eastern "
            "plantation interests.\n\n"
            "His 1847–1849 House service "
            "during the Mexican-American "
            "War period coincided with "
            "the Wilmot Proviso debates — "
            "the congressional controversy "
            "over whether slavery should "
            "be excluded from territories "
            "acquired from Mexico that "
            "deepened the sectional crisis.\n\n"
            "His 1868–1869 Reconstruction "
            "service placed him among the "
            "Southern Unionists who returned "
            "to Congress after the war."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "North Carolina Whig Congressman (1847–1849) during the Wilmot Proviso debates; Massachusetts-born lawyer who settled in North Carolina's Whig Piedmont; returned to Congress during Reconstruction (1868–1869) as a Southern Unionist; career spanned Whig era through Civil War aftermath.",
            "significanceCategory": "regional"
        },
        "causes": [
            "North Carolina's Whig Party tradition in the Piedmont — the western counties' commercial and professional classes who opposed eastern plantation Democratic dominance — provided the political constituency for Boyden's 1847 congressional election",
            "The Mexican-American War's political consequences — particularly the Wilmot Proviso controversy over whether slavery could expand into Mexican cession territories — defined the major political debate of Boyden's first House term and deepened the sectional crisis that would eventually destroy the Whig Party",
            "The Civil War's aftermath and Reconstruction — the congressional effort to restore Southern states to the Union while protecting African American rights — created the political context for Boyden's return to Congress as a Southern Unionist in 1868"
        ],
        "effects": [
            "His 1847–1849 House service contributed North Carolina's Whig perspective to the Wilmot Proviso debates — representing the Piedmont's distinct political tradition in the congressional controversy over slavery's expansion",
            "His political career illustrated the Whig Party's trajectory — from viability as a national coalition in the late 1840s to collapse in the 1850s as the slavery controversy made it impossible to maintain a coalition of Northern moral reformers and Southern slaveholders",
            "His 1868–1869 Reconstruction service represented the Southern Unionist perspective in post-war Congress — the relatively small minority of white Southerners who had opposed secession and sought to work within the Republican Reconstruction framework",
            "His Massachusetts birth and North Carolina career illustrated the movement of Northern-born professionals to the South in the antebellum period — a pattern that created complex political loyalties when the sectional crisis forced a choice"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "North Carolina Congressman 1847–1849 and 1868–1869"},
            {"target": "wilmot-proviso", "verb": "DEBATES", "note": "Whig congressman during the slavery expansion controversy"},
            {"target": "whig-party", "verb": "MEMBER_OF", "note": "North Carolina Whig in the Piedmont tradition"},
            {"target": "reconstruction", "verb": "SERVES_DURING", "note": "Southern Unionist in Reconstruction Congress"},
            {"target": "north-carolina", "verb": "REPRESENTS", "note": "North Carolina congressman from Salisbury"}
        ]
    }),

    ("calvin-willey", {
        "summary": (
            "Calvin Willey (1776–1858) was "
            "an American Democratic politician "
            "from Connecticut who served "
            "as a U.S. Senator (1825–1844) — "
            "an exceptionally long tenure "
            "of nearly twenty years that "
            "placed him at the center of "
            "American politics through "
            "the entire Jacksonian era. "
            "His Senate career encompassed "
            "the political transformation "
            "from the Era of Good Feelings "
            "through the Bank War, nullification "
            "crisis, the emergence of "
            "the Whig opposition, and the "
            "beginnings of the slavery "
            "controversy's penetration "
            "of national politics.\n\n"
            "Connecticut was one of the "
            "New England states where "
            "Jacksonian Democracy made "
            "significant inroads among "
            "artisans, workers, and small "
            "farmers who saw Jacksonian "
            "rhetoric about the 'money power' "
            "as speaking to their economic "
            "concerns. Willey's long Senate "
            "tenure represented this "
            "Connecticut Democratic tradition "
            "against the more dominant "
            "Whig commercial elite.\n\n"
            "His nearly two-decade Senate "
            "career made him one of "
            "Connecticut's most significant "
            "political figures of the "
            "Jacksonian era — a reliable "
            "Democratic vote through "
            "the entire period of "
            "the second American party "
            "system's formation.\n\n"
            "He was a quiet but reliable "
            "Jacksonian party loyalist."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Connecticut Democratic Senator (1825–1844) for nearly twenty years; served through the entire Jacksonian era from the Era of Good Feelings through the Bank War, nullification, and early slavery debates; reliable Democratic vote representing Connecticut's minority Democratic tradition against Whig commercial dominance.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Connecticut's manufacturing and commercial economy's political division — the state's artisans and workers who responded to Jacksonian populism against the Whig commercial elite created the Democratic minority that sustained Willey's long Senate career",
            "Andrew Jackson's political coalition and the second American party system's formation — the Democratic-Whig competition that replaced the collapsed Era of Good Feelings consensus — provided the partisan structure within which Willey served as a reliable Democratic vote",
            "Connecticut's rotation of Senate seats through party control — the state's two-party competition that occasionally gave Democrats enough leverage to elect senators like Willey — created the political opportunity for his nearly twenty-year tenure"
        ],
        "effects": [
            "His nearly twenty-year Senate tenure contributed Connecticut's Democratic vote to virtually every major legislative battle of the Jacksonian era — the Bank War, the Force Act against South Carolina, and the Senate's debates over slavery petitions",
            "His long service contributed to Connecticut's Democratic Party development — representing the minority tradition that kept Democratic organization alive in a state dominated by Whig commercial interests",
            "His reliability as a Jackson-Van Buren loyalist made him one of the most consistent Democratic votes in the Senate — contributing to the Democratic majorities that sustained Jackson's second-term agenda and Van Buren's presidency",
            "His career illustrated the character of the Jacksonian era's Democratic Party — built on coalition of diverse constituencies united by anti-monopoly rhetoric and anti-aristocratic populism, capable of winning elections even in commercially oriented New England states"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Connecticut Senator 1825–1844"},
            {"target": "andrew-jackson", "verb": "SUPPORTS", "note": "Reliable Jacksonian Democratic senator"},
            {"target": "bank-war", "verb": "VOTES_IN", "note": "Senate votes during the Bank War"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Connecticut Democratic Party loyalist"},
            {"target": "connecticut", "verb": "REPRESENTS", "note": "Long-serving Connecticut Democratic senator"}
        ]
    }),

    ("jakob-edvard-colbjørnsen", {
        "summary": (
            "Jakob Edvard Colbjørnsen (1791–1868) "
            "was a Norwegian lawyer, judge, and "
            "politician who served in senior "
            "judicial positions in Norway "
            "during the formative decades "
            "of Norwegian national institutions "
            "following the 1814 Constitution "
            "that created Norway as a "
            "constitutional monarchy. "
            "His career bridged the colonial "
            "Danish period, the brief Swedish "
            "conquest and union of 1814, "
            "and the long period of "
            "Norwegian autonomous governance "
            "under the Swedish crown "
            "that lasted until 1905.\n\n"
            "The 1814 Norwegian Constitution — "
            "one of the most liberal constitutions "
            "in early nineteenth-century Europe "
            "— created a constitutional "
            "monarchy with a representative "
            "Storting (parliament), an "
            "independent judiciary, and "
            "extensive civil liberties. "
            "The legal institutions that "
            "Colbjørnsen helped staff "
            "were building the Norwegian "
            "legal tradition on these "
            "constitutional foundations.\n\n"
            "His father Christian Colbjørnsen "
            "had been a prominent Danish-Norwegian "
            "jurist and reformer — giving "
            "Jakob a distinguished legal "
            "family background in the "
            "Nordic legal tradition.\n\n"
            "His long career contributed "
            "to Norway's judicial independence "
            "and legal tradition development."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Norwegian judge and politician who helped build Norway's judicial institutions after the 1814 Constitution; son of prominent jurist Christian Colbjørnsen; career spanned Danish colonial period, 1814 constitutional moment, and the long Norwegian-Swedish union; contributor to Norway's emerging national legal tradition.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Norwegian Constitution of 1814 — one of Europe's most liberal constitutions, drafted at Eidsvoll in April-May 1814 before Norway was forced into union with Sweden — created the constitutional framework that established Norway's independent judiciary and representative Storting that Colbjørnsen served",
            "The Nordic legal tradition and his father Christian Colbjørnsen's prominent judicial career — which included major legal reforms in Danish-Norwegian governance in the late eighteenth century — provided the intellectual formation and family prestige that shaped Jakob's legal career",
            "Norway's nation-building project under the Swedish crown (1814–1905) — the Norwegian political and cultural project of developing national institutions, Norwegian language and culture, and eventual full independence — provided the national context for the legal institution-building that Colbjørnsen's career contributed to"
        ],
        "effects": [
            "His senior judicial service contributed to the development of Norway's independent judiciary — one of the key institutions of Norwegian constitutional governance that the 1814 constitution created and that legal professionals like Colbjørnsen helped staff and develop",
            "His career contributed to the establishment of Norwegian legal traditions distinct from Danish legal heritage — part of the broader Norwegian nation-building project of developing distinctively Norwegian institutions during the union period",
            "His service contributed to the Norwegian Storting's institutional development — the parliamentary culture and governance practices that made Norway's constitutional monarchy function as an effective limited government",
            "His family's legal legacy — his father's major reforms and his own judicial service — illustrated the multigenerational contribution of the Nordic legal families to the development of Scandinavian legal institutions"
        ],
        "relationships": [
            {"target": "norway", "verb": "SERVES", "note": "Senior Norwegian judge and politician"},
            {"target": "norwegian-constitution-1814", "verb": "SERVES_UNDER", "note": "Career built on the 1814 constitutional framework"},
            {"target": "christian-colbjørnsen", "verb": "SON_OF", "note": "Son of the prominent Danish-Norwegian jurist and reformer"},
            {"target": "storting", "verb": "CONTRIBUTES_TO", "note": "Part of Norway's constitutional governance"},
            {"target": "swedish-norwegian-union", "verb": "SERVES_DURING", "note": "Career under the Swedish-Norwegian union 1814–1868"}
        ]
    }),

    ("marie-jean-hérault-de-séchelles", {
        "summary": (
            "Marie-Jean Hérault de Séchelles "
            "(1759–1794) was a French aristocrat, "
            "lawyer, and revolutionary politician "
            "who became one of the most "
            "brilliant and tragic figures "
            "of the radical Revolution. "
            "A member of the old nobility "
            "who dramatically abandoned "
            "his class to embrace radical "
            "republicanism, he served as "
            "president of the National "
            "Convention (1793) and was "
            "one of the drafters of the "
            "French Constitution of 1793 "
            "— the most democratic constitution "
            "the Revolution produced, "
            "though never implemented "
            "due to the emergency government "
            "of the Committee of Public Safety.\n\n"
            "Hérault had been an Avocat "
            "Général at the Paris Parlement "
            "under the Ancien Régime — "
            "one of the crown's own "
            "senior legal officers — "
            "before converting to "
            "revolutionary radicalism. "
            "He served on the Committee "
            "of Public Safety before "
            "being accused of treason "
            "by Robespierre.\n\n"
            "He was guillotined on "
            "5 April 1794 in the same "
            "batch as Georges Danton "
            "and his associates — "
            "falling victim to the "
            "Terror that he himself "
            "had helped construct.\n\n"
            "His fate exemplified the "
            "Revolution devouring its own children."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "French aristocrat turned radical revolutionary; President of the National Convention (1793); co-drafter of the democratic French Constitution of 1793; Committee of Public Safety member; guillotined with Danton on 5 April 1794 — the Terror consuming its own architects; his career embodied the Revolution's self-destructive radicalism.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French Revolution's social radicalization — the process by which aristocrats like Hérault de Séchelles converted to revolutionary republicanism, abandoning their class privileges and embracing the principles of liberty and equality that the Revolution proclaimed — created the ideological journey that transformed a crown lawyer into a radical Jacobin",
            "The Jacobin-Girondin struggle for control of the Convention and the radical wing's victory — which established the Committee of Public Safety and the Terror's emergency government — placed Hérault in a leadership position that both gave him power and made him a target",
            "Robespierre's paranoid search for traitors within the revolutionary leadership — the logic of the Terror that consumed first its enemies, then its moderates (the Dantonists), and eventually even the Robespierrists themselves — created the accusation of treason that sent Hérault to the guillotine"
        ],
        "effects": [
            "His co-authorship of the Constitution of 1793 — the most democratic of the Revolution's constitutions, with universal male suffrage, the right to work, and popular recall of representatives — created the most radical constitutional document of the revolutionary era, though it was suspended and never implemented",
            "His execution with Danton (April 1794) — the guillotining of the moderate Dantonist faction by Robespierre — was one of the Terror's most consequential moments, eliminating the moderate voice within the radical revolution and accelerating the Terror's most extreme phase",
            "His trajectory from Ancien Régime crown lawyer to revolutionary leader to Terror victim illustrated the Revolution's relentless self-consumption — the logic by which today's revolutionaries became tomorrow's counter-revolutionaries in the eyes of the even more radical faction",
            "His aristocratic background and radical conversion became a symbol of the Revolution's social transformation — the process by which the old ruling class's members who embraced the Revolution most enthusiastically were often among those consumed by it most completely"
        ],
        "relationships": [
            {"target": "national-convention", "verb": "PRESIDES", "note": "President of the National Convention 1793"},
            {"target": "french-constitution-1793", "verb": "DRAFTS", "note": "Co-drafter of the most democratic revolutionary constitution"},
            {"target": "committee-of-public-safety", "verb": "SERVES_ON", "note": "Member of the Terror's governing committee"},
            {"target": "georges-danton", "verb": "EXECUTED_WITH", "note": "Guillotined with Danton on 5 April 1794"},
            {"target": "reign-of-terror", "verb": "VICTIM_OF", "note": "Consumed by the Terror he helped construct"}
        ]
    }),

    ("jules-armand-dufaure", {
        "summary": (
            "Jules Armand Stanislas Dufaure "
            "(1798–1881) was a French lawyer, "
            "statesman, and jurist who had "
            "one of the longest and most "
            "distinguished careers of "
            "nineteenth-century French politics. "
            "Serving under multiple regimes "
            "— the July Monarchy, the Second "
            "Republic, the Second Empire "
            "(in partial opposition), and "
            "the Third Republic — he served "
            "as Minister of the Interior "
            "(1839–1840, 1848–1849), Minister "
            "of Justice multiple times, "
            "and Prime Minister of France "
            "(1876–1877, 1877–1879) during "
            "the critical years of the "
            "Third Republic's consolidation.\n\n"
            "Dufaure was the quintessential "
            "French liberal-conservative "
            "lawyer-statesman — a figure "
            "committed to parliamentary "
            "government, the rule of law, "
            "and moderate liberalism against "
            "both revolutionary radicalism "
            "and reactionary royalism. "
            "His legal career made him "
            "one of the most distinguished "
            "advocates of the French bar.\n\n"
            "His Third Republic prime "
            "ministerships came during "
            "the 'Seize Mai' crisis (1877) "
            "— President MacMahon's "
            "attempt to restore monarchist "
            "dominance that the republicans "
            "defeated in the elections, "
            "establishing republican "
            "parliamentary supremacy.\n\n"
            "He served as President of "
            "the Conseil d'État in his "
            "final years."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "French Prime Minister (1876–1877, 1877–1879) during the Third Republic's consolidation; Minister of the Interior and Justice under multiple regimes; key figure in defeating MacMahon's 1877 Seize Mai crisis and establishing republican parliamentary supremacy; quintessential French liberal-conservative lawyer-statesman across six decades of political life.",
            "significanceCategory": "continental"
        },
        "causes": [
            "France's long nineteenth-century political instability — the succession of regimes (Restoration, July Monarchy, Second Republic, Second Empire, Third Republic) that made political careers across regimes possible for figures like Dufaure who combined legal expertise with moderate liberal politics",
            "The July Monarchy's parliamentary culture — the constitutional monarchy of Louis-Philippe that developed the parliamentary institutions and political culture within which Dufaure first achieved ministerial office",
            "The Third Republic's foundational crisis of 1877 (the Seize Mai) — President MacMahon's dismissal of the republican premier Jules Simon and attempt to restore conservative monarchist governance, which republican politicians like Dufaure successfully defeated by winning the subsequent elections and establishing parliamentary supremacy"
        ],
        "effects": [
            "His prime ministerships during the Seize Mai crisis contributed to the permanent establishment of republican parliamentary supremacy in France — defeating MacMahon's attempt to restore executive dominance over parliament and establishing the Third Republic's parliamentary character",
            "His long ministerial career across multiple regimes contributed to the institutional continuity of French governance — maintaining the professional administrative culture and legal tradition through the political disruptions of the nineteenth century",
            "His legal career — one of the most distinguished at the French bar in the nineteenth century — contributed to the development of French civil law and legal culture, combining his advocacy practice with his governmental service",
            "His career as the paradigmatic French liberal-conservative — committed to parliamentary government, civil liberties, and moderate reform against both radical revolution and reactionary royalism — made him a model for the centrist republican political tradition that dominated the Third Republic"
        ],
        "relationships": [
            {"target": "france", "verb": "SERVES_AS_PRIME_MINISTER", "note": "French PM 1876–1877 and 1877–1879"},
            {"target": "seize-mai-crisis-1877", "verb": "DEFEATS", "note": "Key republican who defeated MacMahon's constitutional coup"},
            {"target": "third-republic-france", "verb": "CONSOLIDATES", "note": "PM during Third Republic's critical consolidation years"},
            {"target": "french-bar", "verb": "LEADS", "note": "One of France's most distinguished advocates"},
            {"target": "conseil-detat-france", "verb": "PRESIDES", "note": "President of the Conseil d'État in final years"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 63 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
