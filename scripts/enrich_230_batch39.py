#!/usr/bin/env python3
"""
Batch 39 — 8 entities: Augustin Robespierre, Pierre de Lancre, Thomas Addis Emmet,
Archibald Bulloch, James Duane Doty, Bjarni Thorarensen, Frederick Frelinghuysen,
John Pendleton King
editorId: vscode-copilot
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

    # 1 — Augustin Robespierre
    ("augustin-robespierre", {
        "summary": (
            "Augustin Bon Joseph de Robespierre (1763–1794) — known as "
            "'Robespierre the Younger' — was a French lawyer, Jacobin "
            "politician, and the younger brother of the revolutionary "
            "leader Maximilien Robespierre. His political convictions "
            "were nearly identical to his brother's: he was an ardent "
            "Montagnard and supporter of the Terror, serving as a deputy "
            "for Pas-de-Calais in the National Convention. He is "
            "additionally notable for identifying and championing a "
            "then-obscure Corsican artillery officer — Napoleon Bonaparte "
            "— during his mission to the south of France, helping to "
            "secure Bonaparte's first significant military command.\n\n"
            "Augustin's most dramatic act came on 9 Thermidor Year II "
            "(July 27, 1794) — the coup that overthrew the Committee "
            "of Public Safety and sent Maximilien to the guillotine. "
            "When the gendarmes arrived to arrest his brother at the "
            "Hôtel de Ville, Augustin threw himself from an upstairs "
            "window rather than be taken separately from Maximilien — "
            "breaking his leg in the fall. He was dragged back, placed "
            "under arrest, and guillotined the following day alongside "
            "his brother on July 28, 1794. He was 30 years old.\n\n"
            "His identification of Napoleon during the 1793 Toulon siege "
            "operations has made him a minor but significant figure in "
            "Napoleonic history: he wrote enthusiastically to Maximilien "
            "about the young Bonaparte's abilities, contributing to his "
            "promotion and subsequent career. Had the Thermidor coup "
            "not ended Robespierre's faction, Napoleon's early career "
            "would have developed under very different patronage.\n\n"
            "'I embrace death with joy,' he reportedly said before "
            "the guillotine — a man who chose fraternal loyalty "
            "over survival."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "'Robespierre the Younger'; French Jacobin politician and Maximilien Robespierre's younger brother; threw himself from the Hôtel de Ville window on 9 Thermidor (July 27, 1794) to die with his brother — guillotined the next day at 30; identified and championed the young Napoleon Bonaparte during the Toulon operations.",
            "significanceCategory": "regional"
        },
        "causes": [
            "His profound personal identification with his brother Maximilien's political vision — and his willingness to die alongside him rather than survive without him — made 9 Thermidor the defining and final act of his life",
            "His mission to the south of France during the Revolutionary Wars — including his political supervision of the siege of Toulon in 1793 — created the context in which he encountered Napoleon Bonaparte and became the young officer's early patron",
            "The Thermidor coup's logic — the political coalition of moderates, pragmatists, and terrified Jacobins who feared they would be the next victims of the Terror — created the political force that destroyed both Robespierres simultaneously"
        ],
        "effects": [
            "His enthusiastic championing of Napoleon Bonaparte in letters to his brother — written during the Toulon campaign — contributed to Bonaparte's first significant military promotion and helped launch the career that would transform France and Europe",
            "His suicide attempt on 9 Thermidor — throwing himself from the window rather than be arrested — created one of the most vivid and widely reported individual acts of the Thermidor period, cementing the Robespierrist faction's image of fanatical commitment",
            "His death alongside Maximilien on July 28, 1794 completed the Thermidor coup's elimination of the Robespierrist inner circle — the removal of both brothers ensuring that no family member survived to rebuild the Jacobin faction",
            "His career illustrated the personal costs of close familial association with powerful revolutionary figures: political proximity to his brother elevated him rapidly, and the same proximity destroyed him instantly when Maximilien fell"
        ],
        "relationships": [
            {"entity": "Maximilien Robespierre (brother)", "relationship": "BROTHER_WHO_DIED_ALONGSIDE", "note": "Threw himself from the Hôtel de Ville window on 9 Thermidor rather than be arrested separately — guillotined the next day alongside Maximilien, choosing fraternal loyalty over survival"},
            {"entity": "9 Thermidor (July 27, 1794) / fall of the Committee of Public Safety", "relationship": "SUICIDE_ATTEMPT_AND_ARREST_ON", "note": "Broke his leg jumping from the Hôtel de Ville window on 9 Thermidor — dragged back and guillotined the next day with Maximilien"},
            {"entity": "Napoleon Bonaparte (early patron, Toulon 1793)", "relationship": "EARLIEST_REVOLUTIONARY_PATRON_OF", "note": "Identified and championed Napoleon Bonaparte's military abilities during the 1793 Toulon campaign — writing enthusiastically to Maximilien and contributing to Bonaparte's first significant promotion"},
            {"entity": "National Convention / Jacobin faction (Montagnard)", "relationship": "DEPUTY_AND_COMMITTED_MEMBER_OF", "note": "Served as a Montagnard deputy for Pas-de-Calais in the National Convention — one of the Committee of Public Safety's most committed supporters"},
            {"entity": "French Revolutionary Terror (1793–1794)", "relationship": "SUPPORTER_AND_VICTIM_OF", "note": "A committed supporter of the Terror's political violence — and one of its final victims when Thermidor ended Jacobin rule on July 28, 1794"}
        ]
    }),

    # 2 — Pierre de Lancre
    ("pierre-de-lancre", {
        "summary": (
            "Pierre de Lancre (1553–1631) — Pierre de Rosteguy de Lancre, "
            "Lord of De Lancre — was a French judge of Bordeaux and "
            "the organizer of the Labourd witch-hunt of 1609, one of "
            "the most notorious witch trials in European history. "
            "Commissioned by King Henry IV to suppress alleged "
            "witchcraft practices in the Labourd region of the "
            "French Basque country, de Lancre conducted systematic "
            "interrogations over several months that he claimed produced "
            "confessions from hundreds and sentences against approximately "
            "70 people — an extraordinary concentration of executions "
            "for a French witch trial.\n\n"
            "De Lancre's prosecutorial methodology combined genuine "
            "demonological conviction with what historians have identified "
            "as a profound cultural anxiety about the Basque people's "
            "distinctiveness: their unique language, maritime culture, "
            "and the seasonal absence of fishermen (who fished off "
            "Newfoundland for months at a time) convinced him that "
            "the region was especially susceptible to diabolism. "
            "He believed he was uncovering an organized sabbath cult "
            "of thousands involving prominent local figures — including, "
            "he claimed, many of the region's own priests.\n\n"
            "His major work 'Tableau de l'inconstance des mauvais anges "
            "et démons' (1612) — a detailed treatise on the Basque "
            "witch-hunt, demonology, and the diabolical sabbath — "
            "is one of the most vivid and revealing primary sources "
            "in the entire European witch-hunt literature: a first-person "
            "account of a witch-hunt written by its organizer.\n\n"
            "His campaign was ended by intervention from the Bishop "
            "of Bayonne — who protected the accused clergy — and by "
            "the political pressure of Basque elites."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "French judge who conducted the Labourd witch-hunt of 1609 — one of the most notorious European witch trials, with approximately 70 executions in the French Basque country; author of 'Tableau de l'inconstance des mauvais anges et démons' (1612) — a primary source classic of demonological literature.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Henry IV's commission to suppress alleged witchcraft in the Labourd region — responding to the anxieties of local elites about the social disruption caused by the fishing men's seasonal absences — created the royal authorization that gave de Lancre his extraordinary powers",
            "The Labourd region's distinctive Basque cultural characteristics — unique language, maritime culture, the sexual and moral anxieties de Lancre projected onto the women left behind while men fished in Newfoundland — created the specific cultural context that de Lancre interpreted as diabolical susceptibility",
            "The broader European witch-hunt panic of the late 16th and early 17th centuries — fueled by the Reformation-Counter-Reformation conflict and the social disruptions of early modernity — provided the intellectual and legal framework within which de Lancre's prosecutions made institutional sense"
        ],
        "effects": [
            "His 'Tableau de l'inconstance des mauvais anges et démons' (1612) became a central text in the European demonological tradition — one of the most detailed first-person accounts of a witch-hunt and a vivid primary source for historians of early modern supernaturalism",
            "His prosecution of Basque priests — claiming that the region's clergy were sabbath participants — provoked intense controversy and intervention from the Bishop of Bayonne, illustrating the limits of royal witch-hunt commissioners' powers when they challenged ecclesiastical authority",
            "The Labourd witch-hunt contributed to the broader European witch-trial literature that shaped subsequent prosecutions — de Lancre's descriptions of Basque sabbath practices were cited by later demonologists and contributed to the standardization of sabbath imagery",
            "His campaign's termination — by the intervention of ecclesiastical and elite political pressure — illustrates the mechanisms by which European witch-hunts were eventually halted: not by skepticism about witchcraft itself, but by elite resistance to overreach that threatened established social hierarchies"
        ],
        "relationships": [
            {"entity": "Labourd witch-hunt (1609) / French Basque country", "relationship": "ORGANIZER_AND_PRESIDING_JUDGE_OF", "note": "Organized and presided over the Labourd witch-hunt of 1609 — one of the most notorious European witch trials, claiming approximately 70 executions in the French Basque country"},
            {"entity": "'Tableau de l'inconstance des mauvais anges et démons' (1612)", "relationship": "AUTHOR_OF", "note": "Authored the primary source classic of the European witch-hunt literature — a first-person account of the Labourd hunt and a detailed treatise on Basque demonology"},
            {"entity": "Henry IV of France (royal commissioner)", "relationship": "ROYAL_COMMISSIONER_AUTHORIZED_BY", "note": "Authorized by Henry IV to suppress witchcraft in the Labourd region — the royal commission that gave him extraordinary judicial powers over the Basque population"},
            {"entity": "Basque culture / Labourd region social structure", "relationship": "WITCH-HUNTER_WHO_PROJECTED_DIABOLISM_ONTO", "note": "Interpreted the Basque people's distinctive language, maritime culture, and seasonal gender dynamics as evidence of special diabolical susceptibility — his cultural anxiety driving the prosecution's scale and intensity"},
            {"entity": "Bishop of Bayonne / Basque ecclesiastical protection (1609)", "relationship": "PROSECUTION_ENDED_BY_INTERVENTION_OF", "note": "His prosecution of Basque clergy provoked the Bishop of Bayonne's intervention — which protected accused priests and eventually ended the hunt, illustrating the limits of royal commissioners' powers against ecclesiastical resistance"}
        ]
    }),

    # 3 — Thomas Addis Emmet
    ("thomas-addis-emmet", {
        "summary": (
            "Thomas Addis Emmet (1764–1827) was an Irish-born American "
            "lawyer, United Irishmen leader, and one of the most celebrated "
            "advocates at the early 19th-century New York bar — the "
            "older brother of Robert Emmet, the Irish patriot executed "
            "in 1803 whose speech from the dock became one of the most "
            "celebrated texts of Irish nationalism. Born in Cork, "
            "Thomas trained as a physician at Edinburgh before turning "
            "to law in Dublin, rising to become one of the most "
            "prominent barristers of the Irish bar.\n\n"
            "In the 1790s, Thomas became a senior member of the Society "
            "of United Irishmen — the revolutionary organization seeking "
            "Irish independence from Britain through alliance with "
            "France. He was imprisoned after the failed 1798 uprising "
            "and held under the Act of Union arrangement until 1802, "
            "when he was released and exiled. He went to France, then "
            "to the United States, eventually settling permanently "
            "in New York in 1804.\n\n"
            "In New York, Emmet became one of the leading figures "
            "at the American bar — known for his powerful oratory "
            "and his mastery of commercial and maritime law. He argued "
            "before the Supreme Court in the landmark case of Gibbons v. "
            "Ogden (1824) — on the side of Livingston and Fulton against "
            "Thomas Gibbons — though he ultimately lost to Daniel Webster "
            "in the case that established Congress's power over interstate "
            "commerce.\n\n"
            "He died in 1827 — still mourning his brother Robert, "
            "whose execution and martyrdom had overshadowed his own "
            "remarkable career."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Senior member of the Society of United Irishmen (1790s); imprisoned after the 1798 uprising; in American exile became one of the leading lawyers at the New York bar; argued in Gibbons v. Ogden (1824) before the Supreme Court; older brother of Robert Emmet — the martyred Irish nationalist executed in 1803.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The United Irishmen movement's radical republican vision — inspired by the American and French Revolutions — provided the political framework that drew Emmet into revolutionary conspiracy against British rule in Ireland in the 1790s",
            "The failure of the 1798 Irish Rebellion and subsequent British repression — including the Act of Union (1800) which extinguished the Irish Parliament — forced Emmet into the exile that eventually brought him to New York and the American bar",
            "New York's rapidly developing legal marketplace in the early 19th century — with its growing commercial complexity and need for skilled advocates — provided the professional opportunity that allowed Emmet's legal talent to flourish in America as it had in Dublin"
        ],
        "effects": [
            "His prominence at the New York bar — and his advocacy before the Supreme Court in Gibbons v. Ogden (1824) — contributed to the development of American commercial and maritime law during its most formative decades",
            "His brother Robert Emmet's execution (1803) and the subsequent martyrology of the Emmet name — which Thomas helped maintain through his public identity as the martyr's surviving brother — contributed to the development of Irish nationalist memory in the United States",
            "His leadership in the Society of United Irishmen contributed to the constitutional and political planning of the 1798 uprising — though ultimately unsuccessful, the 1798 rebellion established the tradition of organized Irish republican resistance that continued through the 19th century",
            "His career as an Irish-born lawyer who became a leading figure at the American bar illustrated the potential of political exile to transplant legal talent — a pattern that enriched American law with European-trained advocates throughout the early republic"
        ],
        "relationships": [
            {"entity": "Robert Emmet (brother, Irish patriot martyr 1803)", "relationship": "OLDER_BROTHER_OF", "note": "Older brother of Robert Emmet — executed in 1803 after the failed Dublin uprising, whose 'Speech from the Dock' became one of the most celebrated texts of Irish nationalism"},
            {"entity": "Society of United Irishmen (1790s Irish revolutionary organization)", "relationship": "SENIOR_MEMBER_AND_LEADER", "note": "Senior member of the Society of United Irishmen — planning the 1798 uprising against British rule, imprisoned after its suppression, released and exiled in 1802"},
            {"entity": "Gibbons v. Ogden (US Supreme Court, 1824)", "relationship": "ARGUED_FOR_LIVINGSTON-FULTON_IN", "note": "Argued on behalf of Livingston and Fulton against Thomas Gibbons in the landmark Gibbons v. Ogden case — lost to Daniel Webster in the ruling that established Congress's power over interstate commerce"},
            {"entity": "New York legal bar (early 19th century)", "relationship": "LEADING_ADVOCATE_AT", "note": "Became one of the most celebrated advocates at the New York bar after settling in New York in 1804 — known for his oratory and mastery of commercial and maritime law"},
            {"entity": "1798 Irish Rebellion (United Irishmen uprising)", "relationship": "IMPRISONED_AFTER_SUPPRESSION_OF", "note": "Imprisoned by the British after the 1798 uprising's suppression — held under the Act of Union arrangement until 1802, then exiled to France and eventually America"}
        ]
    }),

    # 4 — Archibald Bulloch
    ("archibald-bulloch", {
        "summary": (
            "Archibald Stobo Bulloch (1730–1777) was an American lawyer, "
            "Georgia militia officer, and the 7th President (Governor) "
            "of Georgia from 1776 to 1777 — one of the state's first "
            "governors in the aftermath of the Declaration of Independence. "
            "Born in the Province of South Carolina to a family of "
            "Scottish and colonial descent, Bulloch settled in Georgia, "
            "built a legal career, and aligned firmly with the Patriot "
            "cause during the Revolutionary crisis.\n\n"
            "Bulloch served as a Georgia militia officer during the "
            "early Revolutionary War years, contributing to the defense "
            "of the Georgia coast against British naval operations, "
            "before being selected as Georgia's president-governor "
            "under the first state constitution. His tenure was brief — "
            "he died in office in 1777 — but it contributed to "
            "establishing Georgia's early republican governance during "
            "the critical opening years of the Revolution.\n\n"
            "His most striking historical significance, however, is "
            "genealogical: Archibald Bulloch was a great-great-grandfather "
            "of Theodore Roosevelt — making him the most prominent "
            "American presidential ancestor from Georgia. Through "
            "his daughter Martha Bulloch (who married Daniel Stewart), "
            "and through subsequent generations, the Bulloch-Roosevelt "
            "family connection gave Theodore Roosevelt a personal "
            "stake in Southern history that complicated his presidency's "
            "progressive reforms.\n\n"
            "His Savannah family became one of Georgia's most distinguished "
            "antebellum dynasties before the Civil War ended their world."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "7th President (Governor) of Georgia (1776–1777, died in office); Georgia militia officer in the Revolution; great-great-grandfather of Theodore Roosevelt — the earliest American presidential ancestor from Georgia; his Bulloch family became one of Georgia's most distinguished antebellum dynasties.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Georgia's Patriot political mobilization — and its need for experienced lawyers and militia officers willing to commit to the revolutionary cause against Britain's significant Loyalist presence in the colony — elevated Bulloch to the governorship in the crisis year of 1776",
            "His South Carolina birth and Georgia legal career gave him the social and professional connections that established him as a trusted Patriot leader in a colony where loyalty was actively contested",
            "Georgia's first state constitution (1777) — and its provision for a president-governor elected by the legislature — created the institutional framework within which Bulloch's brief executive tenure operated"
        ],
        "effects": [
            "His brief governorship (1776–1777) contributed to Georgia's institutional continuity as a Patriot state during the most dangerous period of the Revolutionary War on the southern coast — maintaining the revolutionary government against British naval pressure",
            "His death in office in 1777 was one of the founding losses of the Georgia revolutionary generation — a reminder of the personal costs of the revolutionary commitment",
            "The Bulloch family's subsequent history — as one of Georgia's most prominent antebellum dynasties — and the Roosevelt genealogical connection gave Archibald Bulloch a historical significance that transcended his brief governorship",
            "Theodore Roosevelt's consciousness of his Bulloch family roots — and his complex relationship to the Southern Confederate legacy through his mother Martha Bulloch Roosevelt — was one of the personal genealogical complications that shaped Roosevelt's political navigation of race and regional memory"
        ],
        "relationships": [
            {"entity": "Georgia governorship (7th President, 1776–1777, died in office)", "relationship": "7TH_GOVERNOR", "note": "Served as 7th President (Governor) of Georgia (1776–1777) — one of the state's first governors after the Declaration of Independence, dying in office"},
            {"entity": "Theodore Roosevelt (great-great-grandson)", "relationship": "GREAT-GREAT-GRANDFATHER_OF", "note": "Great-great-grandfather of Theodore Roosevelt — making him the earliest American presidential ancestor from Georgia; the Bulloch-Roosevelt connection gave TR a personal stake in Southern history"},
            {"entity": "Bulloch family (Georgia antebellum dynasty)", "relationship": "PATRIARCH_OF", "note": "The founding patriarch of the Bulloch family — one of Georgia's most distinguished antebellum dynasties before the Civil War ended their world"},
            {"entity": "Georgia militia / Revolutionary War coastal defense", "relationship": "OFFICER_IN", "note": "Served as a Georgia militia officer during the early Revolutionary War — contributing to the defense of the Georgia coast against British naval operations before his election as governor"},
            {"entity": "Georgia's first state constitution (1777) and early republican governance", "relationship": "FIRST_EXECUTIVE_UNDER", "note": "One of the first executives under Georgia's revolutionary state constitution — his brief tenure contributing to the institutional architecture of Georgia's early republican governance"}
        ]
    }),

    # 5 — James Duane Doty
    ("james-duane-doty", {
        "summary": (
            "James Duane Doty (1799–1865) was an American lawyer, "
            "land speculator, and frontier politician who served as "
            "the 2nd Governor of Wisconsin Territory (1841–1844) "
            "and later as the 5th Governor of Utah Territory (1863–1865) "
            "— two entirely different frontier territories separated "
            "by two decades and a continent. Born in New York, "
            "Doty moved west as a young man, became deeply embedded "
            "in the frontier land economy of the Great Lakes region, "
            "and built a career as one of the most active political "
            "operators in the antebellum territorial West.\n\n"
            "His Wisconsin career is particularly notable: Doty "
            "played a major role in founding Madison as the territorial "
            "capital — named after President James Madison — and in "
            "shaping Wisconsin's early territorial development through "
            "land speculation that enriched him personally while also "
            "building the infrastructure of frontier governance. "
            "He also served as Wisconsin's congressional delegate "
            "(1839–1841) before his gubernatorial appointment.\n\n"
            "His Utah appointment came during the Civil War, when "
            "Abraham Lincoln sent him to manage the complex political "
            "landscape of Brigham Young's Mormon territory — a "
            "diplomatically demanding position that required negotiating "
            "between federal authority and the Church of Jesus Christ "
            "of Latter-day Saints' institutional dominance.\n\n"
            "His career — spanning two territories, two decades, "
            "and two entirely different frontier cultures — made him "
            "one of the most geographically mobile frontier politicians "
            "in American history."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "2nd Governor of Wisconsin Territory (1841–1844) — key figure in founding Madison as territorial capital; 5th Governor of Utah Territory (1863–1865, managing Mormon-federal relations during the Civil War); Wisconsin congressional delegate (1839–1841); land speculator and frontier politician spanning two territories.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The frontier land speculation economy of the antebellum Old Northwest — in which political office and land acquisition were deeply intertwined — created the environment in which Doty's combined roles as land speculator and territorial politician were mutually reinforcing",
            "Wisconsin Territory's need for a politically connected administrator who could attract settlement and investment — and who understood both the federal patronage system and the land market's dynamics — created the role that Doty's Wisconsin career filled",
            "Lincoln's Civil War administration's need to manage the Utah Territory's delicate Mormon-federal relationship — without provoking the conflict that James Buchanan's Utah War had created — created the diplomatic demand that Doty's appointment to the Utah governorship was intended to address"
        ],
        "effects": [
            "His role in founding Madison as Wisconsin's territorial capital — named after President Madison — contributed to one of the most deliberately chosen state capital sites in American history, placed at the center of an isthmus between two lakes",
            "His land speculation activities in Wisconsin Territory — using his political position to acquire and develop land — contributed to the frontier capitalist development of the region while also generating the conflicts of interest that characterized antebellum territorial governance",
            "His Utah governorship contributed to the federal-Mormon negotiation process during the Civil War — managing the delicate balance between federal authority and LDS institutional power in a territory whose loyalty the Lincoln administration needed to secure",
            "His career spanning Wisconsin and Utah territories illustrated the remarkable mobility of antebellum frontier politicians — men who moved between territories as political opportunities arose, building careers across the continent's frontier edge"
        ],
        "relationships": [
            {"entity": "Wisconsin Territory governorship (2nd Governor, 1841–1844)", "relationship": "2ND_GOVERNOR", "note": "Served as 2nd Governor of Wisconsin Territory (1841–1844) — playing a major role in founding Madison as the territorial capital and shaping Wisconsin's early development"},
            {"entity": "Madison, Wisconsin (territorial capital founding)", "relationship": "KEY_FIGURE_IN_FOUNDING_AS_CAPITAL", "note": "Played a major role in establishing Madison — named after President Madison — as Wisconsin's territorial capital, shaped by his land speculation interests"},
            {"entity": "Utah Territory governorship (5th Governor, 1863–1865)", "relationship": "5TH_GOVERNOR", "note": "Served as 5th Governor of Utah Territory (1863–1865) — managing the delicate Mormon-federal relationship during the Civil War"},
            {"entity": "Wisconsin congressional delegate (1839–1841)", "relationship": "CONGRESSIONAL_DELEGATE", "note": "Served as Wisconsin's congressional delegate (1839–1841) — the political position he held immediately before his gubernatorial appointment"},
            {"entity": "Antebellum frontier land speculation / territorial capitalism", "relationship": "PRACTITIONER_AND_POLITICAL_OPERATOR_IN", "note": "One of the most active land speculators and frontier political operators in the antebellum West — building personal wealth through land acquisition while shaping territorial governance"}
        ]
    }),

    # 6 — Bjarni Thorarensen
    ("bjarni-thorarensen", {
        "summary": (
            "Bjarni Vigfússon Thorarensen (1786–1841) was an Icelandic "
            "poet, official, and one of the founding figures of Icelandic "
            "Romantic nationalism — a man who combined an administrative "
            "career as deputy governor (stiftamtmaður) of northern and "
            "eastern Iceland with a poetic career that made him one of "
            "the most significant Icelandic literary figures of the "
            "early 19th century. Born in northern Iceland, he was "
            "educated in Denmark — as most Icelandic intellectuals "
            "of the era were — and returned to serve in Iceland's "
            "Danish colonial administrative structure while writing "
            "poetry that celebrated Icelandic history and landscape.\n\n"
            "Thorarensen's poetry was influenced by both German "
            "classicism and Romanticism, particularly the Romantic "
            "nationalist movements that were reshaping European "
            "literary cultures in the 1820s–1840s. He brought "
            "Romantic sensibility to Icelandic verse — drawing on "
            "the Old Norse tradition while engaging with contemporary "
            "European literary currents — and is considered one of "
            "the founders of modern Icelandic Romantic poetry.\n\n"
            "Politically, Thorarensen was aligned with the Fjölnismenn "
            "— the Icelandic nationalist intellectual movement centered "
            "around the journal Fjölnir — and strongly supported the "
            "reestablishment of the Althing at Þingvellir as a symbol "
            "of Icelandic democratic tradition and national identity. "
            "His advocacy contributed to the cultural groundwork for "
            "Iceland's eventual achievement of home rule (1904) and "
            "independence (1944).\n\n"
            "He died in 1841 before the Althing was fully reconstituted, "
            "but his poetry and advocacy had helped shape the cultural "
            "imagination of Icelandic nationhood."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Icelandic Romantic poet and deputy governor; one of the founders of modern Icelandic Romantic poetry; aligned with the Fjölnismenn nationalist movement; advocated for the reestablishment of the Althing at Þingvellir; his work contributed to the cultural groundwork for Icelandic national identity and eventual independence.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Iceland's Danish colonial administration — and the Icelandic intellectual class's growing consciousness of their distinctive national identity — created the cultural and political environment in which Thorarensen's combination of official service and nationalist poetry was possible and comprehensible",
            "The European Romantic nationalist movement — and particularly German Romantic nationalism's valorization of folk culture, landscape, and historical identity — provided the literary framework that Thorarensen adapted to the Icelandic context",
            "The Fjölnismenn movement's intellectual activism — centered around the journal Fjölnir — created the institutional framework for coordinating Iceland's cultural nationalist project with which Thorarensen was aligned"
        ],
        "effects": [
            "His founding contributions to Icelandic Romantic poetry helped establish the literary tradition that subsequent Icelandic poets and writers built upon — contributing to Iceland's cultural identity formation in the critical 19th-century period",
            "His advocacy for the reestablishment of the Althing at Þingvellir — as a symbol of Iceland's ancient democratic tradition — contributed to the intellectual arguments that eventually produced the Althing's reconstitution in 1845",
            "His poetry's celebration of Icelandic landscape, history, and Norse heritage contributed to the Romantic nationalist imagination of Icelandic nationhood that informed the political movements of later decades",
            "His career as an official who was also a nationalist poet illustrated the dual position of Iceland's educated class — serving within the Danish colonial structure while simultaneously building the cultural case for Icelandic autonomy"
        ],
        "relationships": [
            {"entity": "Icelandic Romantic nationalist poetry (founding generation)", "relationship": "FOUNDING_FIGURE_OF", "note": "One of the founders of modern Icelandic Romantic poetry — bringing Romantic sensibility to Icelandic verse while drawing on the Old Norse tradition"},
            {"entity": "Fjölnismenn nationalist movement / Fjölnir journal", "relationship": "ALIGNED_INTELLECTUAL_AND_CONTRIBUTOR", "note": "Aligned with the Fjölnismenn — Iceland's nationalist intellectual movement — contributing to the cultural project of Icelandic national identity formation"},
            {"entity": "Althing reconstitution at Þingvellir (Icelandic democratic revival)", "relationship": "ADVOCATE_FOR", "note": "Advocated for the reestablishment of the Althing at Þingvellir — supporting the cultural and political project that eventually produced the Althing's reconstitution in 1845"},
            {"entity": "Deputy governor of northern and eastern Iceland", "relationship": "ADMINISTRATIVE_OFFICIAL", "note": "Served as deputy governor (stiftamtmaður) of northern and eastern Iceland — combining official service within the Danish colonial structure with nationalist cultural advocacy"},
            {"entity": "European Romantic nationalism / German Romantic influence", "relationship": "ADAPTED_TO_ICELANDIC_CONTEXT", "note": "Adapted European Romantic nationalist literary currents — particularly German Romanticism — to the Icelandic context, making Thorarensen a key conduit of Romantic ideas to Icelandic literature"}
        ]
    }),

    # 7 — Frederick Frelinghuysen
    ("frederick-frelinghuysen", {
        "summary": (
            "Frederick Frelinghuysen (1753–1804) was a New Jersey "
            "lawyer, Continental Army officer, Continental Congress "
            "delegate (1779–1781), and US Senator from New Jersey "
            "(1793–1796) — a prominent figure in the founding generation "
            "of a political dynasty that would produce prominent "
            "American statesmen across multiple generations. "
            "Educated at the College of New Jersey (now Princeton), "
            "he served in the Revolutionary War as an artillery officer, "
            "rising to the rank of colonel, and subsequently built "
            "a distinguished legal and political career in New Jersey.\n\n"
            "Frelinghuysen's Continental Congress service (1779–1781) "
            "placed him at the national level during one of the most "
            "difficult periods of the Revolutionary War — the years of "
            "Benedict Arnold's treason, the Battle of Camden, and "
            "the mounting financial crisis of the Continental government. "
            "He was later elected as a Federalist senator (1793–1796), "
            "serving during the Washington administration in the period "
            "of the Jay Treaty controversy.\n\n"
            "His significance lies partly in his own career and partly "
            "in the family dynasty he represented: his uncle Theodorus "
            "Frelinghuysen was the Great Awakening revivalist who "
            "sparked the first American evangelical movement in the "
            "1720s, and his son Theodore Frelinghuysen became Henry "
            "Clay's running mate in the 1844 presidential election — "
            "making the Frelinghuysen name one of the most continuously "
            "prominent in New Jersey political and religious history.\n\n"
            "He died in 1804 — a Federalist whose party was declining "
            "as Jeffersonian democracy transformed American politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "New Jersey Founding Father; Continental Army officer (colonel); Continental Congress delegate (1779–1781); US Senator from New Jersey (1793–1796); member of the Frelinghuysen political dynasty — nephew of Great Awakening revivalist Theodorus Frelinghuysen, father of Theodore Frelinghuysen (Henry Clay's 1844 running mate).",
            "significanceCategory": "regional"
        },
        "causes": [
            "New Jersey's position as a critical Revolutionary War theater — the site of numerous battles from Trenton to Monmouth — and its need for experienced military officers committed to the Continental cause created the environment for Frelinghuysen's military career",
            "The Frelinghuysen family's deep roots in New Jersey's Dutch Reformed and evangelical Protestant culture — and the family's educational and political prominence from Theodorus's revivalist ministry — provided the social capital that established Frederick's career",
            "The Federalist political movement's need for credentialed Revolutionary War veterans and lawyers who could represent New Jersey's commercial interests — particularly its connections to New York finance and Philadelphia trade — created the electoral context for Frelinghuysen's Senate career"
        ],
        "effects": [
            "His Continental Congress service (1779–1781) contributed to New Jersey's representation during the war's most critical period — maintaining the state's voice in the Confederation's governance at a time of military crisis",
            "His Senate career (1793–1796) contributed to the Federalist majority in Washington's second term — including the contentious Jay Treaty debate that divided American politics and shaped the emerging party system",
            "His place in the Frelinghuysen dynasty — between Theodorus (Great Awakening revivalist) and Theodore (Clay's running mate) — made him a generational link in one of the most multi-dimensional New Jersey political families, bridging the religious, Revolutionary, and antebellum eras",
            "His death as a Federalist in 1804 — as Jeffersonian democracy was completing its transformation of American politics — marked the end of the Federalist generation's dominance and the beginning of the long Jeffersonian era that his son's Whig career would eventually resist"
        ],
        "relationships": [
            {"entity": "US Senate from New Jersey (1793–1796, Federalist)", "relationship": "SENATOR", "note": "Served as Federalist US Senator from New Jersey (1793–1796) — during Washington's second term and the Jay Treaty controversy"},
            {"entity": "Continental Congress (NJ delegate, 1779–1781)", "relationship": "DELEGATE", "note": "Served as Continental Congress delegate for New Jersey (1779–1781) — representing the state during the Revolutionary War's most difficult period"},
            {"entity": "Theodorus Frelinghuysen (uncle, Great Awakening revivalist)", "relationship": "NEPHEW_OF", "note": "Nephew of Theodorus Frelinghuysen — the Dutch Reformed minister whose revivals in the 1720s sparked the first American evangelical movement, the First Great Awakening"},
            {"entity": "Theodore Frelinghuysen (son, Henry Clay's 1844 running mate)", "relationship": "FATHER_OF", "note": "Father of Theodore Frelinghuysen — who became Henry Clay's vice-presidential running mate in the 1844 presidential election, extending the dynasty into the antebellum era"},
            {"entity": "Continental Army / Revolutionary War NJ theater", "relationship": "COLONEL_IN", "note": "Served as a Continental Army artillery officer rising to colonel — one of the founding military credentials that supported his subsequent political career"}
        ]
    }),

    # 8 — John Pendleton King
    ("john-pendleton-king", {
        "summary": (
            "John Pendleton King (1799–1888) was a Virginia-born Georgia "
            "attorney, planter, and politician who served as US Senator "
            "from Georgia (1833–1837) and then as president of the "
            "Georgia Railroad and Banking Company for approximately "
            "40 years (1841–1878) — one of the longest tenures leading "
            "a major Southern railroad in American history. Born in "
            "Virginia, he migrated to Georgia, built a law practice "
            "and plantation, and was appointed to the Senate in 1833 "
            "to fill a vacancy.\n\n"
            "King's Senate tenure (1833–1837) coincided with the most "
            "turbulent period in antebellum Georgia politics: the "
            "nullification crisis, the Bank War, and the intensifying "
            "sectional tensions over slavery. He resigned in 1837 — "
            "before completing his term — to accept the presidency "
            "of the Georgia Railroad and Banking Company, a decision "
            "that was unusual for the era in prioritizing a commercial "
            "position over a Senate seat.\n\n"
            "His 40-year railroad presidency proved to be his most "
            "consequential contribution to Georgia's development. "
            "The Georgia Railroad — connecting Augusta to Atlanta "
            "(and eventually beyond) — was one of the most strategically "
            "important antebellum railroads in the South, carrying "
            "cotton to the coast and manufactured goods into the interior. "
            "King oversaw its expansion through the antebellum boom, "
            "the Civil War disruption, and the Reconstruction reconstruction "
            "— an extraordinary span of American economic history.\n\n"
            "He lived to 89, one of the longest-lived Georgia statesmen "
            "of the 19th century."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "US Senator from Georgia (1833–1837, resigned to run the Georgia Railroad); president of the Georgia Railroad and Banking Company for approximately 40 years (1841–1878) — one of the longest railroad presidencies in Southern history; oversaw the railroad through antebellum boom, Civil War, and Reconstruction.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Georgia's rapid railroad development in the 1830s–1840s — and the Georgia Railroad's strategic importance connecting Augusta and Atlanta to the broader Southern rail network — created the commercial opportunity that King chose over his Senate career",
            "His Virginia birth and Georgia legal career gave him the social networks and commercial connections that established him as a credible candidate for both the Senate appointment and the railroad presidency",
            "The antebellum Southern railroad economy's dependence on planter-class capital and political connections — and its need for presidents who could navigate both the financial markets and the political landscape — created the role that King's combination of legal, political, and commercial experience made him suited for"
        ],
        "effects": [
            "His 40-year Georgia Railroad presidency (1841–1878) contributed to the development of one of the South's most strategically important antebellum railroads — connecting Augusta to Atlanta and carrying Georgia's cotton economy to the coast",
            "His resignation from the Senate in 1837 to run the railroad illustrated the antebellum South's growing recognition that commercial infrastructure could be as important as political office — an early instance of the railroad presidency as a career peak comparable to legislative service",
            "The Georgia Railroad's survival through the Civil War — and its reconstruction after Sherman's March, which had disrupted the region's rail infrastructure — required King's long presidency to maintain institutional continuity through the most disruptive period in Southern economic history",
            "His longevity — living to 89 and serving as railroad president until 1878 — made him a living link between Georgia's antebellum commercial world and the New South era that Reconstruction created"
        ],
        "relationships": [
            {"entity": "US Senate from Georgia (1833–1837, resigned before term end)", "relationship": "SENATOR_WHO_RESIGNED_TO_TAKE_RAILROAD_PRESIDENCY", "note": "Served as US Senator from Georgia (1833–1837) — resigned before completing his term to accept the presidency of the Georgia Railroad, choosing commercial leadership over Senate service"},
            {"entity": "Georgia Railroad and Banking Company (president, ~1841–1878)", "relationship": "PRESIDENT_FOR_~40_YEARS", "note": "Served as president of the Georgia Railroad and Banking Company for approximately 40 years (1841–1878) — one of the longest railroad presidencies in Southern history"},
            {"entity": "Augusta-Atlanta railroad corridor / antebellum Southern rail network", "relationship": "EXECUTIVE_WHO_OVERSAW_DEVELOPMENT_OF", "note": "Oversaw the Georgia Railroad's expansion connecting Augusta to Atlanta — one of the most strategically important antebellum rail connections in the South, carrying cotton to the coast"},
            {"entity": "Georgia antebellum commercial and plantation economy", "relationship": "COMMERCIAL_LEADER_OF", "note": "One of Georgia's most significant commercial leaders — his railroad presidency contributing more to Georgia's economic development than his Senate career"},
            {"entity": "Sherman's March / Civil War-to-Reconstruction Georgia railroad reconstruction", "relationship": "RAILROAD_PRESIDENT_DURING_DISRUPTION_AND_RECONSTRUCTION_BY", "note": "Led the Georgia Railroad through the Civil War's disruption — including Sherman's destructive march — and its Reconstruction-era reconstruction, maintaining institutional continuity across Georgia's most economically disruptive decades"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 39)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
