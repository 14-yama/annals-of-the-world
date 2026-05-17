#!/usr/bin/env python3
"""
VS Code Batch 09 — 8 high-importance stub EventWindows + Institutions.
Targets classic world-history milestones with 22–40c summaries.
Avoids limit errors: uses existing-doc lookup before create.
"""
import json, glob, os, hashlib, time, urllib.request, urllib.error, urllib.parse, pathlib

ENDPOINT  = "https://fra.cloud.appwrite.io/v1"
PROJECT   = "66509ba7003618a05af6"
DB        = "annals_world_db"
API_KEY   = os.environ.get("APPWRITE_API_KEY", "")
COLLECTION = "entities"
BASE      = pathlib.Path("data/appwrite-export/entities")


def slug_to_id(slug: str) -> str:
    return hashlib.sha256(slug.encode()).hexdigest()[:20]


def _headers() -> dict:
    return {
        "Content-Type": "application/json",
        "X-Appwrite-Project": PROJECT,
        "X-Appwrite-Key": API_KEY,
    }


def get_doc(doc_id: str) -> dict | None:
    url = f"{ENDPOINT}/databases/{DB}/collections/{COLLECTION}/documents/{doc_id}"
    req = urllib.request.Request(url, headers=_headers())
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError:
        return None


def find_doc_by_slug(slug: str) -> str | None:
    q = json.dumps({"method": "equal", "attribute": "slug", "values": [slug]})
    url = (f"{ENDPOINT}/databases/{DB}/collections/{COLLECTION}/documents"
           f"?queries[]={urllib.parse.quote(q)}&limit=1")
    req = urllib.request.Request(url, headers=_headers())
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            docs = json.loads(r.read()).get("documents", [])
            return docs[0]["$id"] if docs else None
    except Exception:
        return None


def create_doc(doc_id: str, data: dict) -> bool:
    url = f"{ENDPOINT}/databases/{DB}/collections/{COLLECTION}/documents"
    body = json.dumps({"documentId": doc_id, "data": data}).encode()
    req = urllib.request.Request(url, data=body, headers=_headers(), method="POST")
    try:
        with urllib.request.urlopen(req, timeout=15) as _:
            return True
    except urllib.error.HTTPError as e:
        print(f"    CREATE ERROR {e.code}: {e.read().decode()[:200]}")
        return False


def update_doc(doc_id: str, data: dict) -> bool:
    url = f"{ENDPOINT}/databases/{DB}/collections/{COLLECTION}/documents/{doc_id}"
    body = json.dumps({"data": data}).encode()
    req = urllib.request.Request(url, data=body, headers=_headers(), method="PATCH")
    try:
        with urllib.request.urlopen(req, timeout=15) as _:
            return True
    except urllib.error.HTTPError as e:
        print(f"    UPDATE ERROR {e.code}: {e.read().decode()[:200]}")
        return False


def save_local(slug: str, entity_data: dict) -> None:
    """Mirror entity to local export JSON so sync_gateway can audit it."""
    call = entity_data.get("callNumber", "")
    prefix = call.split("-")[0] if call else "000"
    division = "".join(c for c in prefix if c.isdigit())[:3] or "000"
    class_code = division[:3]
    class_dir = BASE / f"{class_code}-Class-{class_code}"
    class_dir.mkdir(parents=True, exist_ok=True)
    out_file = class_dir / f"{class_code}{slug}.json"
    # Load existing
    if out_file.exists():
        existing = json.loads(out_file.read_text())
    else:
        existing = {"entities": []}
    entities = existing.get("entities", [])
    # Replace or append
    updated = False
    for i, e in enumerate(entities):
        if e.get("slug") == slug:
            entities[i] = entity_data
            updated = True
            break
    if not updated:
        entities.append(entity_data)
    existing["entities"] = entities
    out_file.write_text(json.dumps(existing, indent=2, ensure_ascii=False))


# ═══════════════════════════════════════════════════════════════════════════
# BATCH 09 ENRICHMENTS — 8 world-history milestones
# ═══════════════════════════════════════════════════════════════════════════

ENRICHMENTS = {
    # ── 1. Magna Carta ───────────────────────────────────────────────────
    "magna-carta-1215": {
        "name": "Magna Carta (1215)",
        "label": "EventWindow",
        "callNumber": "930.06-magna-carta-1215",
        "era": "Medieval",
        "eraSlug": "medieval",
        "eraDivision": "Medieval History",
        "eraDivisionCode": "930",
        "region": "Western Europe",
        "continent": "Europe",
        "status": "confirmed",
        "period": "1215 CE",
        "summary": (
            "The Magna Carta (Great Charter), sealed by King John of England on 15 June 1215 at Runnymede, "
            "is one of the most consequential legal documents in world history. Forced upon the king by rebellious "
            "barons threatening civil war, it established for the first time that the monarch was subject to the "
            "rule of law — not above it. Its 63 clauses addressed feudal grievances, reformed the legal system, "
            "and guaranteed the right to a fair trial and freedom from arbitrary imprisonment.\n\n"
            "Clause 39 — 'No free man shall be seized, imprisoned, dispossessed, outlawed, exiled or in any way "
            "ruined… except by the lawful judgement of his peers or by the law of the land' — became the "
            "foundation of habeas corpus and due process. Though initially annulled by Pope Innocent III and "
            "repeatedly revised, it was reissued by Henry III in 1225 and became a permanent part of English "
            "constitutional law in 1297.\n\n"
            "Its legacy transcended England: the U.S. Constitution's Bill of Rights, the Universal Declaration "
            "of Human Rights (1948), and constitutional law across the Commonwealth all trace their lineage to "
            "this meadow by the Thames. 'The right to a fair trial is so engrained in our culture,' wrote "
            "lawyer Geoffrey Robertson, 'that we forget it was not always so — and might not have been.'"
        ),
        "causes": [
            "King John's extortionate taxation and arbitrary abuse of feudal rights",
            "Military defeat in France (Battle of Bouvines, 1214) that humiliated the crown",
            "Archbishop Stephen Langton's mediation between barons and the king",
        ],
        "effects": [
            "Established the principle that the monarch is subject to law, not above it",
            "Created the legal foundation for habeas corpus and due process",
            "Inspired constitutional frameworks across the English-speaking world",
            "Led to the development of Parliament as a check on royal power",
        ],
        "relationships": [
            {"sourceSlug": "magna-carta-1215", "sourceName": "Magna Carta (1215)",
             "verb": "CONSTRAINS", "targetSlug": "king-john-of-england", "targetName": "King John of England",
             "context": "Charter forced king to accept rule of law, 1215"},
            {"sourceSlug": "magna-carta-1215", "sourceName": "Magna Carta (1215)",
             "verb": "INFLUENCES", "targetSlug": "bill-of-rights-1689", "targetName": "Bill of Rights (1689)",
             "context": "Constitutional tradition descended directly from Magna Carta"},
            {"sourceSlug": "magna-carta-1215", "sourceName": "Magna Carta (1215)",
             "verb": "INFLUENCES", "targetSlug": "united-states-constitution", "targetName": "United States Constitution",
             "context": "Habeas corpus and due process clauses echoed in US Bill of Rights"},
        ],
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "The Magna Carta is the foundational document of constitutional governance worldwide. Its principle that power must be constrained by law underpins every modern democracy.",
            "significanceCategory": "world-changing",
        },
        "subjects": ["England", "Constitutional Law", "Medieval", "Human Rights", "Democracy"],
        "subjectHeadings": ["EventWindow — Legal — England — Medieval"],
        "frameworks": ["political", "legal"],
    },

    # ── 2. Storming of the Bastille ───────────────────────────────────────
    "storming-of-the-bastille": {
        "name": "Storming of the Bastille (1789)",
        "label": "EventWindow",
        "callNumber": "940.06-storming-of-the-bastille",
        "era": "Early Modern",
        "eraSlug": "early-modern",
        "eraDivision": "Early Modern History",
        "eraDivisionCode": "940",
        "region": "Western Europe",
        "continent": "Europe",
        "status": "confirmed",
        "period": "14 July 1789",
        "summary": (
            "The storming of the Bastille fortress on 14 July 1789 was the opening act of the French Revolution "
            "and remains one of history's most iconic moments of popular insurrection against tyranny. The Bastille "
            "— a medieval Paris fortress serving as a royal prison — had long symbolised despotic royal authority. "
            "When Louis XVI dismissed popular finance minister Jacques Necker on 11 July, Parisians feared a royalist "
            "crackdown and took to the streets.\n\n"
            "On the morning of 14 July, a crowd of several hundred Parisians — artisans, tradespeople, and soldiers "
            "who had defected — stormed the fortress after a brief siege. The governor, the Marquis de Launay, was "
            "killed and his head paraded through the streets. Although only seven prisoners were actually held "
            "inside, the symbolic impact was enormous: the 'invincible' symbol of royal power had fallen to the people.\n\n"
            "The National Assembly was saved from royal dissolution, and the fall of the Bastille radicalised the "
            "Revolution across France. Nobles fled in the Great Fear; serfdom and feudal privileges were abolished "
            "on 4 August. The Declaration of the Rights of Man followed on 26 August. 14 July became Bastille Day "
            "— France's national holiday — celebrating the birth of popular sovereignty."
        ),
        "causes": [
            "Louis XVI's dismissal of Finance Minister Necker, triggering fear of royal crackdown",
            "Bread shortages and economic crisis radicalising the Parisian underclass",
            "The Estates-General deadlock that had paralysed France since May 1789",
        ],
        "effects": [
            "Saved the National Assembly from royal dissolution and accelerated the Revolution",
            "Triggered the Great Fear across rural France and abolition of feudalism",
            "Established popular sovereignty as a legitimate political force",
            "Became the founding symbol of republican democracy, celebrated as Bastille Day",
        ],
        "relationships": [
            {"sourceSlug": "storming-of-the-bastille", "sourceName": "Storming of the Bastille (1789)",
             "verb": "TRIGGERS", "targetSlug": "french-revolution", "targetName": "French Revolution",
             "context": "Bastille's fall on 14 July 1789 launched the revolutionary phase"},
            {"sourceSlug": "storming-of-the-bastille", "sourceName": "Storming of the Bastille (1789)",
             "verb": "TRANSFORMS", "targetSlug": "declaration-of-the-rights-of-man", "targetName": "Declaration of the Rights of Man",
             "context": "Revolutionary momentum led to the Declaration issued August 1789"},
        ],
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "The fall of the Bastille launched the French Revolution and introduced popular sovereignty as an irresistible political force that would reshape all of Europe.",
            "significanceCategory": "world-changing",
        },
        "subjects": ["France", "French Revolution", "Early Modern", "Democracy", "Popular Sovereignty"],
        "subjectHeadings": ["EventWindow — Revolution — France — Early Modern"],
        "frameworks": ["political", "social"],
    },

    # ── 3. Slave Trade Act 1807 ───────────────────────────────────────────
    "slave-trade-act-1807": {
        "name": "Slave Trade Act 1807",
        "label": "EventWindow",
        "callNumber": "950.06-slave-trade-act-1807",
        "era": "Modern",
        "eraSlug": "modern",
        "eraDivision": "Modern History",
        "eraDivisionCode": "950",
        "region": "Western Europe",
        "continent": "Europe",
        "status": "confirmed",
        "period": "25 March 1807",
        "summary": (
            "The Slave Trade Act of 25 March 1807 abolished the transatlantic slave trade throughout the British "
            "Empire — the most decisive legislative blow against one of history's greatest crimes. Passed after "
            "more than two decades of campaigning led by William Wilberforce, Thomas Clarkson, and the Clapham "
            "Sect, the Act made it illegal for British subjects to engage in the slave trade and imposed fines "
            "of £100 per enslaved person found on a British vessel.\n\n"
            "The passage marked the culmination of a moral campaign unprecedented in its popular organisation: "
            "300,000 people had signed abolitionist petitions, boycotts of slave-produced sugar had spread "
            "across Britain, and freed Africans such as Olaudah Equiano had published searing first-hand "
            "testimony. William Pitt the Younger had supported the cause for years; his death in 1806 made "
            "passage easier under a new coalition government.\n\n"
            "The Act did not free enslaved people already held — that required the Slavery Abolition Act of 1833 "
            "— but it dealt a structural blow to the trade's economics. The Royal Navy's West Africa Squadron "
            "intercepted hundreds of slave ships after 1808. Britain's diplomatic weight forced treaty after "
            "treaty on other powers, making abolition a cornerstone of 19th-century international law. "
            "Wilberforce's verdict: 'Thank God that I have lived to witness a day in which England is willing "
            "to give twenty millions sterling for the abolition of Slavery.'"
        ),
        "causes": [
            "Twenty-year abolitionist campaign led by Wilberforce, Clarkson, and the Society for Effecting the Abolition of the Slave Trade",
            "Shift in moral philosophy treating enslaved people as full human beings with natural rights",
            "Economic arguments that free labour was ultimately more productive than slave labour",
        ],
        "effects": [
            "Ended Britain's dominant role in the transatlantic slave trade",
            "Inspired abolitionist movements worldwide including in the United States",
            "Led to the Slavery Abolition Act (1833) freeing enslaved people across the British Empire",
            "Established a template for humanitarian international law and treaty-making",
        ],
        "relationships": [
            {"sourceSlug": "slave-trade-act-1807", "sourceName": "Slave Trade Act 1807",
             "verb": "INFLUENCES", "targetSlug": "slavery-abolition-act-1833", "targetName": "Slavery Abolition Act 1833",
             "context": "1807 Act set the precedent and created the abolitionist coalition that achieved full emancipation in 1833"},
        ],
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "The 1807 Act dealt the decisive structural blow to the British slave trade and launched the global abolitionist movement that would end chattel slavery across the Western world.",
            "significanceCategory": "world-changing",
        },
        "subjects": ["Britain", "Abolition", "Slavery", "Modern", "Human Rights", "Atlantic Trade"],
        "subjectHeadings": ["EventWindow — Law — Britain — Modern"],
        "frameworks": ["moral", "political", "economic"],
    },

    # ── 4. Union of Lublin ────────────────────────────────────────────────
    "union-of-lublin": {
        "name": "Union of Lublin (1569)",
        "label": "EventWindow",
        "callNumber": "940.06-union-of-lublin",
        "era": "Early Modern",
        "eraSlug": "early-modern",
        "eraDivision": "Early Modern History",
        "eraDivisionCode": "940",
        "region": "Eastern Europe",
        "continent": "Europe",
        "status": "confirmed",
        "period": "1 July 1569",
        "summary": (
            "The Union of Lublin, signed on 1 July 1569, merged the Kingdom of Poland and the Grand Duchy of "
            "Lithuania into the Polish-Lithuanian Commonwealth — one of the largest and most powerful states in "
            "16th-century Europe and an extraordinary experiment in multi-ethnic, constitutionally constrained "
            "monarchy. The Union was negotiated under King Sigismund II Augustus, who died without an heir and "
            "used the crisis of succession to forge a permanent bond.\n\n"
            "The Commonwealth stretched from the Baltic to the Black Sea, encompassing Poles, Lithuanians, "
            "Ruthenians (Ukrainians and Belarusians), Jews, Germans, Tartars, and Armenians. Its constitution "
            "established an elected monarchy, a bicameral Sejm (parliament) with a liberum veto — any single "
            "nobleman could block legislation — and extraordinary religious tolerance during the Reformation "
            "era through the Warsaw Confederation (1573).\n\n"
            "At its height, the Commonwealth was a European great power that repelled Ottoman, Muscovite, and "
            "Swedish invasions. Its unique political culture planted the seeds of later parliamentary democracy, "
            "while the liberum veto that protected noble freedoms ultimately paralysed the state and contributed "
            "to its partition in the late 18th century. The Union is remembered today as a foundational moment "
            "for Polish, Lithuanian, Ukrainian, and Belarusian historical memory."
        ),
        "causes": [
            "Sigismund II Augustus's lack of male heirs creating urgency to merge the two states permanently",
            "Threat from Muscovite Russia (Livonian War) requiring combined military response",
            "Lithuanian nobility's desire for equal privileges with Polish szlachta",
        ],
        "effects": [
            "Created the Polish-Lithuanian Commonwealth, one of Europe's largest states for two centuries",
            "Established elected monarchy and the liberum veto system, precursors to parliamentary democracy",
            "Enabled extraordinary religious toleration during Europe's wars of religion",
            "Shaped modern Polish, Lithuanian, Ukrainian and Belarusian national identities",
        ],
        "relationships": [
            {"sourceSlug": "union-of-lublin", "sourceName": "Union of Lublin (1569)",
             "verb": "CREATES", "targetSlug": "polish-lithuanian-commonwealth", "targetName": "Polish-Lithuanian Commonwealth",
             "context": "The Union formally established the Commonwealth as a single state"},
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "The Union of Lublin created one of the largest multi-ethnic states in European history and pioneered elected monarchy and religious tolerance at the height of the Reformation.",
            "significanceCategory": "continental",
        },
        "subjects": ["Poland", "Lithuania", "Early Modern", "Constitutional Law", "Commonwealth"],
        "subjectHeadings": ["EventWindow — Union — Poland — Early Modern"],
        "frameworks": ["political", "constitutional"],
    },

    # ── 5. Battle of Culloden ─────────────────────────────────────────────
    "battle-of-culloden-1746": {
        "name": "Battle of Culloden (1746)",
        "label": "EventWindow",
        "callNumber": "940.06-battle-of-culloden-1746",
        "era": "Early Modern",
        "eraSlug": "early-modern",
        "eraDivision": "Early Modern History",
        "eraDivisionCode": "940",
        "region": "Western Europe",
        "continent": "Europe",
        "status": "confirmed",
        "period": "16 April 1746",
        "summary": (
            "The Battle of Culloden, fought on 16 April 1746 on a bleak moorland near Inverness, was the last "
            "pitched battle on British soil and the final catastrophic defeat of the Jacobite cause — the "
            "Stuart dynasty's fifty-year struggle to reclaim the British throne. Bonnie Prince Charlie's "
            "Highland army of some 5,000–7,000 was annihilated in under an hour by the Duke of Cumberland's "
            "disciplined government forces, ending the Jacobite Rising of 1745 ('The '45').\n\n"
            "The battle was brief but the massacre that followed was not. Cumberland earned the title 'Butcher' "
            "for authorising the slaughter of wounded Jacobite soldiers and the destruction of Highland culture "
            "that followed: the Disarming Act banned the wearing of tartan and bearing of arms; clan chieftains "
            "lost their jurisdictions; and brutal pacification drove tens of thousands from the glens.\n\n"
            "Culloden permanently shattered the Highland clan system, accelerating the transformation of Scotland "
            "and fuelling the first waves of Highland emigration to the Americas. Paradoxically, within a generation "
            "the Highlands were romanticised by Robert Burns and Sir Walter Scott, and the tartan culture that had "
            "been outlawed became the defining symbol of Scottish identity. The battlefield remains Scotland's most "
            "visited historic site."
        ),
        "causes": [
            "Charles Edward Stuart's ('Bonnie Prince Charlie') bid to reclaim the British throne for the House of Stuart",
            "Highland loyalty to the Stuart cause combined with Catholic and Episcopalian religious grievances",
            "Overextension of the Jacobite march into England and retreat to Scotland that exhausted the army",
        ],
        "effects": [
            "Permanent end of the Jacobite cause and Stuart claim to the British throne",
            "Destruction of the Highland clan system through the Disarming Act and Heritable Jurisdictions Act",
            "Mass Highland emigration to the Americas, shaping Scottish diaspora",
            "Paradoxical romanticisation of Highland culture by Burns and Scott that created modern Scottish national identity",
        ],
        "relationships": [
            {"sourceSlug": "battle-of-culloden-1746", "sourceName": "Battle of Culloden (1746)",
             "verb": "ENDS", "targetSlug": "jacobite-rising-1745", "targetName": "Jacobite Rising (1745)",
             "context": "Culloden was the decisive military defeat that crushed the '45 Rising"},
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Culloden ended the Jacobite cause and accelerated the destruction of the Highland clan system, fundamentally reshaping Scottish society and seeding the Scottish diaspora worldwide.",
            "significanceCategory": "regional",
        },
        "subjects": ["Scotland", "Britain", "Early Modern", "Jacobites", "Clans", "Warfare"],
        "subjectHeadings": ["EventWindow — Battle — Scotland — Early Modern"],
        "frameworks": ["political", "military"],
    },

    # ── 6. Battle of Poitiers 1356 ────────────────────────────────────────
    "battle-of-poitiers-1356": {
        "name": "Battle of Poitiers (1356)",
        "label": "EventWindow",
        "callNumber": "930.06-battle-of-poitiers-1356",
        "era": "Medieval",
        "eraSlug": "medieval",
        "eraDivision": "Medieval History",
        "eraDivisionCode": "930",
        "region": "Western Europe",
        "continent": "Europe",
        "status": "confirmed",
        "period": "19 September 1356",
        "summary": (
            "The Battle of Poitiers, fought on 19 September 1356 near Maupertuis south of Poitiers, was the second "
            "great English victory of the Hundred Years' War. Edward the Black Prince commanded an English-Gascon "
            "force of roughly 6,000–8,000 men that decimated a French army of 11,000–20,000 under King John II — "
            "and captured the French king himself, the most prestigious prisoner-of-war since antiquity.\n\n"
            "As at Crécy (1346), the English longbowmen proved decisive, cutting down charging French cavalry and "
            "infantry alike on a hillside hedged with vineyards and thickets. The Black Prince's tactical skill "
            "in choosing his ground and timing a counter-charge when the French attack stalled turned a desperate "
            "defensive stand into a rout. John II was taken to London and held for a ransom of three million gold "
            "écus — nearly four times France's annual revenue.\n\n"
            "The Treaty of Brétigny (1360) followed, granting England sovereignty over vast French territories "
            "including Aquitaine. France's humiliation shattered royal authority, sparked the Jacquerie peasant "
            "revolt of 1358, and demonstrated the decisive superiority of English archers over French heavy cavalry "
            "that would remain a tactical lesson of European warfare for generations."
        ),
        "causes": [
            "Edward III's claim to the French throne continuing the dynastic conflict of the Hundred Years' War",
            "The Black Prince's chevauchée raid through southern France drawing the French army to intercept",
            "French tactical over-confidence repeating the cavalry charge mistakes of Crécy (1346)",
        ],
        "effects": [
            "Capture of King John II of France, the most prestigious prisoner since antiquity",
            "Treaty of Brétigny (1360): England gained sovereignty over Aquitaine and massive war indemnity",
            "Jacquerie peasant uprising (1358) sparked by France's military and fiscal collapse",
            "Confirmed English longbow superiority, reshaping European military tactics",
        ],
        "relationships": [
            {"sourceSlug": "battle-of-poitiers-1356", "sourceName": "Battle of Poitiers (1356)",
             "verb": "FOLLOWS", "targetSlug": "battle-of-crecy-1346", "targetName": "Battle of Crécy (1346)",
             "context": "Second major English victory using longbow tactics to defeat French cavalry"},
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Poitiers was a pivotal Hundred Years' War victory that captured the French king, restructured Anglo-French territorial claims, and confirmed the dominance of the English longbow in European warfare.",
            "significanceCategory": "regional",
        },
        "subjects": ["France", "England", "Medieval", "Hundred Years War", "Warfare"],
        "subjectHeadings": ["EventWindow — Battle — France — Medieval"],
        "frameworks": ["military", "political"],
    },

    # ── 7. Khmelnytsky Uprising ───────────────────────────────────────────
    "khmelnytsky-uprising-begins": {
        "name": "Khmelnytsky Uprising (1648)",
        "label": "Movement",
        "callNumber": "940.06-khmelnytsky-uprising-begins",
        "era": "Early Modern",
        "eraSlug": "early-modern",
        "eraDivision": "Early Modern History",
        "eraDivisionCode": "940",
        "region": "Eastern Europe",
        "continent": "Europe",
        "status": "confirmed",
        "period": "1648–1657 CE",
        "summary": (
            "The Khmelnytsky Uprising (1648–1657) was a Cossack and peasant revolt that tore apart the "
            "Polish-Lithuanian Commonwealth and permanently reshaped Eastern Europe. Led by Hetman Bohdan "
            "Khmelnytsky of the Zaporozhian Cossacks, it began as a revolt against Polish noble oppression "
            "and the subordination of the Orthodox Church, and rapidly became a war of Ukrainian nation-formation. "
            "Khmelnytsky allied with Crimean Tatar Khan Islam Giray III and inflicted a series of catastrophic "
            "defeats on the Commonwealth: Zhovti Vody (April 1648), Korsun (May 1648), and the annihilating "
            "Battle of Batih (1652).\n\n"
            "The revolt's scale was extraordinary. Massacres of Polish nobles and — notoriously — Jewish "
            "communities swept the region; the Chmielnicki massacres killed between 100,000 and 500,000 Jewish "
            "people and rank among the worst anti-Jewish atrocities before the 20th century. The Hetmanate "
            "created the proto-state Cossack Hetmanate on the east bank of the Dnipro.\n\n"
            "Unable to consolidate alone, Khmelnytsky signed the Treaty of Pereyaslav (1654) placing the "
            "Hetmanate under Muscovite protection — a fateful decision still contested by historians as "
            "'union' or 'subjection.' The uprising planted the seeds of modern Ukrainian national consciousness "
            "and drew Russia irrevocably into European power politics."
        ),
        "causes": [
            "Polish noble oppression of Cossack communities and withdrawal of the Cossack register",
            "Subordination of the Orthodox Church to Catholic Polish authority sparking religious revolt",
            "Personal grievances of Hetman Khmelnytsky whose estate was seized by a Polish nobleman",
        ],
        "effects": [
            "Destruction of Polish-Lithuanian Commonwealth's eastern provinces and long-term decline",
            "Cossack Hetmanate proto-state established as the first organised Ukrainian polity",
            "Treaty of Pereyaslav (1654) drew Muscovite Russia into Eastern European power politics",
            "Chmielnicki massacres — among the worst anti-Jewish atrocities before the Holocaust",
        ],
        "relationships": [
            {"sourceSlug": "khmelnytsky-uprising-begins", "sourceName": "Khmelnytsky Uprising (1648)",
             "verb": "DESTABILISES", "targetSlug": "polish-lithuanian-commonwealth", "targetName": "Polish-Lithuanian Commonwealth",
             "context": "Uprising permanently weakened the Commonwealth's military and territorial control"},
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "The Khmelnytsky Uprising created the conditions for modern Ukrainian national consciousness, weakened the Polish-Lithuanian Commonwealth, and drew Russia into European geopolitics.",
            "significanceCategory": "continental",
        },
        "subjects": ["Ukraine", "Poland", "Russia", "Early Modern", "Cossacks", "Warfare"],
        "subjectHeadings": ["Movement — Revolt — Ukraine — Early Modern"],
        "frameworks": ["political", "military", "religious"],
    },

    # ── 8. Charles University Founded ────────────────────────────────────
    "charles-university-founded": {
        "name": "Charles University Founded (1348)",
        "label": "Institution",
        "callNumber": "930.07-charles-university-founded",
        "era": "Medieval",
        "eraSlug": "medieval",
        "eraDivision": "Medieval History",
        "eraDivisionCode": "930",
        "region": "Central Europe",
        "continent": "Europe",
        "status": "confirmed",
        "period": "1348 CE",
        "summary": (
            "Charles University in Prague, founded by Holy Roman Emperor Charles IV on 7 April 1348, is the "
            "oldest university in Central Europe and one of the most significant intellectual institutions of "
            "the medieval world. Charles founded it to end the need for Bohemian scholars to travel to Paris, "
            "Oxford, or Bologna, and to make Prague — his imperial capital — a centre of European learning.\n\n"
            "The university was modelled on Bologna and Paris, with four faculties: theology, law, medicine, "
            "and the liberal arts. It was international from birth, drawing scholars from German, Czech, "
            "Bavarian, Saxon, and Polish 'nations' under the imperial charter. By 1409, the Kutná Hora Decree "
            "transferred voting power to the Bohemian nation — triggering an exodus of German scholars who "
            "founded Leipzig University — and installed Jan Hus as rector.\n\n"
            "Hus used the university as his pulpit to preach church reform, anticipating the Protestant "
            "Reformation by a century. His execution in 1415 sparked the Hussite Wars. Charles University "
            "thus stands at the intersection of two transformations: the institutionalisation of medieval "
            "learning and the birth of European religious reform. It has educated generations of Czech "
            "leaders and today enrols over 50,000 students."
        ),
        "causes": [
            "Charles IV's ambition to make Prague the intellectual capital of the Holy Roman Empire",
            "Bohemia's need for trained clergy and administrators without dependence on foreign universities",
            "Papal bull granted by Clement VI enabling the university's canonical establishment",
        ],
        "effects": [
            "Became the oldest university in Central Europe, shaping regional intellectual life for seven centuries",
            "Hosted Jan Hus whose reform preaching launched the Hussite movement, precursor to the Reformation",
            "Kutná Hora Decree triggered the founding of Leipzig University (1409)",
            "Created the institutional infrastructure for Bohemian national identity and culture",
        ],
        "relationships": [
            {"sourceSlug": "charles-university-founded", "sourceName": "Charles University Founded (1348)",
             "verb": "HOSTS", "targetSlug": "jan-hus", "targetName": "Jan Hus",
             "context": "Hus served as rector 1409–1410 and used the university as his platform for reform"},
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Charles University catalysed Central European intellectual life for seven centuries and incubated the Hussite movement — the most significant church reform before Luther.",
            "significanceCategory": "continental",
        },
        "subjects": ["Bohemia", "Czech Republic", "Medieval", "Education", "Reformation"],
        "subjectHeadings": ["Institution — University — Bohemia — Medieval"],
        "frameworks": ["intellectual", "religious", "political"],
    },
}


# ═══════════════════════════════════════════════════════════════════════════
# RUN
# ═══════════════════════════════════════════════════════════════════════════

def run() -> None:
    if not API_KEY:
        print("ERROR: APPWRITE_API_KEY env var not set. Run:\n  export APPWRITE_API_KEY=$(grep APPWRITE_API_KEY .env | cut -d= -f2)")
        return

    ok = err = 0
    for slug, enrichment in ENRICHMENTS.items():
        print(f"\n[{slug}]")
        doc_id = slug_to_id(slug)

        # Resolve actual Appwrite doc ID (might differ from sha256)
        existing_id = get_doc(doc_id)
        if existing_id is None:
            found_id = find_doc_by_slug(slug)
        else:
            found_id = doc_id

        # Build detailsJson payload
        dj: dict = {}
        for k in ("causes", "effects", "relationships", "places", "subjects", "subjectHeadings",
                  "frameworks", "historicalSignificance"):
            if k in enrichment:
                dj[k] = enrichment.pop(k)
        enrichment["detailsJson"] = json.dumps(dj, ensure_ascii=False)

        if found_id:
            print(f"  → UPDATE {found_id[:12]}…")
            success = update_doc(found_id, enrichment)
        else:
            print(f"  → CREATE {doc_id[:12]}…")
            enrichment["slug"] = slug
            success = create_doc(doc_id, enrichment)
            found_id = doc_id

        if success:
            print(f"  ✓ synced to Appwrite ({len(enrichment.get('summary',''))}c summary)")
            ok += 1
        else:
            err += 1

        time.sleep(0.3)

    print(f"\n{'='*55}")
    print(f"Batch 09 complete: {ok} synced  {err} errors")


if __name__ == "__main__":
    run()
