#!/usr/bin/env python3
"""
Batch 67c — Create/update Text & related entities referenced by Jesus and Ussher
Creates entity files for slugs that don't yet exist.
Updates existing ones where summary is thin (< 500c).
"""
import json, os, datetime, glob

NOW = datetime.datetime.utcnow().isoformat() + "+00:00"
EDITOR = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION = "vscode-batch-67-may2026"
BASE = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities"

# ── helpers ──────────────────────────────────────────────────────────────────

def load(path):
    with open(path) as f:
        return json.load(f)

def save(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  Saved: {path}")


def find_entity(slug):
    """Return (filepath, index) if entity with slug exists, else (None, None)."""
    for fpath in glob.glob(f"{BASE}/**/*.json", recursive=True):
        try:
            d = load(fpath)
            for i, e in enumerate(d.get("entities", [])):
                if e.get("slug") == slug:
                    return fpath, i
        except:
            pass
    return None, None


def patch_or_create(slug, class_code, label, name, era, era_slug, era_div_code,
                    region, continent, summary, rels, texts, evidence, timeline,
                    places, causes, effects, frameworks, subjects, subject_headings,
                    call_number, significance, born=None, died=None, period=None,
                    wikipedia_url=None, wikidata_qid=None, quote=None, alt_names=None,
                    thumbnail_url=None, importance_score=5, extra_top=None):
    """Update existing entity if thin, or create new entity file."""
    fpath, idx = find_entity(slug)
    details = {
        "summary": summary,
        "causes": causes,
        "effects": effects,
        "relationships": rels,
        "texts": texts,
        "evidence": evidence,
        "timeline": timeline,
        "places": places,
        "quote": quote or "",
        "externalLinks": [],
        "frameworks": frameworks,
        "sessionId": SESSION,
        "enrichedBy": EDITOR,
        "enrichedAt": NOW,
        "_editLog": [],
    }
    if significance:
        details["historicalSignificance"] = significance

    if fpath:
        # Entity exists — patch if summary thin
        d = load(fpath)
        e = d["entities"][idx]
        raw = e.get("detailsJson", "{}")
        dj = json.loads(raw) if isinstance(raw, str) else (raw or {})
        existing_summary = dj.get("summary", "") or e.get("summary", "") or ""
        if len(existing_summary) >= 800:
            print(f"  SKIP {slug}: already {len(existing_summary)}c")
            return
        # Merge
        dj.update(details)
        d["entities"][idx]["detailsJson"] = json.dumps(dj, ensure_ascii=False)
        d["entities"][idx]["_unsyncedEdits"] = True
        for k, v in (extra_top or {}).items():
            d["entities"][idx][k] = v
        if subjects:
            d["entities"][idx]["subjects"] = subjects
        if subject_headings:
            d["entities"][idx]["subjectHeadings"] = subject_headings
        if frameworks:
            d["entities"][idx]["frameworks"] = frameworks
        if alt_names is not None:
            d["entities"][idx]["altNames"] = alt_names
        if importance_score:
            d["entities"][idx]["importanceScore"] = importance_score
        if thumbnail_url:
            d["entities"][idx]["thumbnailUrl"] = thumbnail_url
        save(fpath, d)
        print(f"  Updated {slug}: OK")
        return

    # Create new entity file
    dir_name = f"{class_code}-Class-{class_code}"
    dir_path = os.path.join(BASE, dir_name)
    file_name = f"{class_code}{slug}.json"
    full_path = os.path.join(dir_path, file_name)

    entity = {
        "slug": slug,
        "name": name,
        "label": label,
        "callNumber": call_number,
        "summary": summary[:300] + "..." if len(summary) > 300 else summary,
        "era": era,
        "eraSlug": era_slug,
        "eraDivision": era,
        "eraDivisionCode": era_div_code,
        "region": region,
        "continent": continent,
        "status": "Published",
        "born": born or "",
        "died": died or "",
        "founded": "",
        "period": period or "",
        "wikidataQid": wikidata_qid or "",
        "wikipediaUrl": wikipedia_url or "",
        "imageUrl": "",
        "thumbnailUrl": thumbnail_url or "",
        "quote": quote or "",
        "importanceScore": importance_score,
        "altNames": alt_names or [],
        "subjectHeadings": subject_headings or [],
        "subjects": subjects or [],
        "frameworks": frameworks or [],
        "startDate": None,
        "endDate": None,
        "detailsJson": json.dumps(details, ensure_ascii=False),
        "_unsyncedEdits": True,
    }
    if extra_top:
        entity.update(extra_top)

    data = {
        "_meta": {
            "classCode": class_code,
            "divisionCode": f"{class_code}{slug}",
            "count": 1,
            "exportedAt": NOW
        },
        "entities": [entity]
    }
    save(full_path, data)
    print(f"  Created {slug}: OK")


# ── 1. Annales Veteris Testamenti ────────────────────────────────────────────
patch_or_create(
    slug="annales-veteris-testamenti",
    class_code="780",
    label="Text",
    name="Annales Veteris Testamenti",
    era="Early Modern", era_slug="early-modern", era_div_code="940",
    region="Western Europe", continent="Europe",
    call_number="780.annales-veteris-testamenti",
    summary=(
        "Annales Veteris Testamenti, a Prima Mundi Origine Deducti ('Annals of the Old "
        "Testament, Deduced from the First Origins of the World') is a 1650 work by "
        "Archbishop James Ussher of Armagh, representing the most comprehensive biblical "
        "chronology ever attempted. Drawing on the Hebrew Bible, Septuagint, ancient Near "
        "Eastern sources, Josephus, and Scaligerian chronological methodology, Ussher "
        "calculated that Creation occurred at nightfall preceding Sunday, 23 October 4004 BCE "
        "— in the Julian calendar. The work covered every major Old Testament event from "
        "Creation through the death of Nebuchadnezzar, correlating each with a precise "
        "astronomical and civil date.\n\n"
        "The Annales was not a fundamentalist polemic but a serious work of humanist scholarship. "
        "Ussher cross-referenced Ptolemy's canon of kings, Eusebius's Chronicle, the Syriac "
        "Peshitta, and Arabic astronomical tables alongside the Hebrew text. His methodology "
        "was rigorous by seventeenth-century standards — he made explicit astronomical "
        "calculations to identify the Julian dates corresponding to biblical events, and "
        "carefully weighted different manuscript traditions.\n\n"
        "The work's extraordinary cultural impact came in 1701, when Bishop William Lloyd "
        "inserted Ussher's dates in the margins of a new edition of the Authorised King James "
        "Bible. This edition was reprinted for over 250 years, making 4004 BCE the de facto "
        "Protestant creation date. Scientists from Hutton to Darwin explicitly framed their "
        "deep-time discoveries as refutations of Ussher's timeline, making the Annales "
        "an unintended catalyst of the geological and biological revolutions."
    ),
    rels=[
        {"verb": "AUTHORS", "targetSlug": "james-ussher", "targetName": "James Ussher",
         "context": "Ussher authored the Annales, publishing it in London in 1650 after decades of manuscript research"},
        {"verb": "INFLUENCES", "targetSlug": "king-james-bible", "targetName": "King James Bible",
         "context": "Ussher's dates were inserted in KJV margins from 1701 by Bishop Lloyd, distributing the chronology to millions of Protestant readers"},
        {"verb": "INFLUENCES", "targetSlug": "charles-darwin", "targetName": "Charles Darwin",
         "context": "Darwin invoked Ussher's 4004 BCE to dramatise the contrast with deep geological time in On the Origin of Species"},
        {"verb": "INFLUENCES", "targetSlug": "charles-lyell", "targetName": "Charles Lyell",
         "context": "Lyell's Principles of Geology was understood as a refutation of the Ussher timescale"},
        {"verb": "INFLUENCES", "targetSlug": "scientific-revolution", "targetName": "Scientific Revolution",
         "context": "The Annales represented the summit of the seventeenth-century programme to construct a universal chronology from scripture"},
    ],
    texts=[
        {"slug": "annalium-pars-posterior", "name": "Annalium Pars Posterior", "year": "1654",
         "role": "Ussher's sequel continuing the timeline from Solomon to the New Testament"},
        {"slug": "king-james-bible", "name": "King James Bible (1701 edition)", "year": "1701",
         "role": "The 1701 edition which first printed Ussher's dates in the margins"},
    ],
    evidence=[
        {"tier": "A", "citation": "Ussher, James. Annales Veteris Testamenti. London: Flesher & Robinson, 1650. The complete primary text."},
        {"tier": "B", "citation": "Barr, James. 'Why the World Was Created in 4004 BC.' Bulletin of the John Rylands Library 67 (1985): 575–608."},
        {"tier": "B", "citation": "Gould, Stephen Jay. 'Fall in the House of Ussher.' Natural History, November 1991."},
    ],
    timeline=[
        {"year": "1650", "event": "Published in London by Flesher and Robinson; immediately recognised as the definitive biblical chronology"},
        {"year": "1654", "event": "Sequel Annalium Pars Posterior published, completing the timeline through the New Testament"},
        {"year": "1701", "event": "Bishop William Lloyd inserts Ussher's dates in the margins of the Authorised KJV Bible"},
        {"year": "1859", "event": "Darwin's On the Origin of Species explicitly references Ussher's timescale as the framework being overturned"},
    ],
    places=[{"name": "London, England", "role": "place of first publication (1650)"}],
    causes=[
        "Scaliger's De emendatione temporum (1583) established the technical chronological framework Ussher extended",
        "Ussher's access to rare Syriac, Arabic, and Hebrew manuscripts through his vast private library",
        "Protestant demand for a definitive alternative to Roman Catholic chronological traditions",
    ],
    effects=[
        "Made 4004 BCE the de facto Protestant creation date for 250 years via KJV margins",
        "Served as the intellectual target that Hutton, Lyell, and Darwin's deep-time discoveries implicitly refuted",
        "Established the most complete biblical chronological framework produced by any scholar",
    ],
    frameworks=["RELIGIOUS_THOUGHT", "INTELLECTUAL_HISTORY", "PRINT_CULTURE_AND_KNOWLEDGE", "CAUSE_AND_EFFECT"],
    subjects=["biblical chronology", "Early Modern Europe", "Ireland", "Protestant Reformation",
              "chronology", "James Ussher", "scientific revolution", "King James Bible"],
    subject_headings=["Annales Veteris Testamenti — Biblical Chronology — Ireland — Early Modern"],
    significance={"significanceScore": 7, "significanceCategory": "continental",
                  "significanceNarrative": "The Annales Veteris Testamenti defined Protestant chronological thinking for 250 years and became the implicit reference point for the geological and biological revolutions of the 18th and 19th centuries."},
    importance_score=7,
    period="Published 1650",
    wikipedia_url="https://en.wikipedia.org/wiki/Ussher_chronology",
)

# ── 2. Irish Articles (1615) ─────────────────────────────────────────────────
patch_or_create(
    slug="irish-articles-1615",
    class_code="012",
    label="Text",
    name="Irish Articles (1615)",
    era="Early Modern", era_slug="early-modern", era_div_code="940",
    region="Western Europe", continent="Europe",
    call_number="012.irish-articles-1615",
    summary=(
        "The Irish Articles of 1615 were a confession of faith adopted by the Church of "
        "Ireland Convocation and drafted primarily by the 34-year-old James Ussher. "
        "Consisting of 104 articles, they were the first national confession of faith in "
        "the British Isles to explicitly endorse high-Calvinist double predestination — "
        "the doctrine that God has decreed from eternity both the salvation of the elect "
        "and the damnation of the reprobate. In this, the Irish Articles were considerably "
        "more precise than the Thirty-Nine Articles of the Church of England (1563), which "
        "had deliberately left the question of predestination ambiguous.\n\n"
        "The Irish Articles drew on the English Thirty-Nine Articles, the Lambeth Articles "
        "of 1595, and the theological tradition of William Perkins and the Cambridge Puritans. "
        "Their influence extended far beyond Ireland: when the Westminster Assembly of Divines "
        "met in 1643–53 to draft a new confession for the churches of England, Scotland, and "
        "Ireland, the Irish Articles served as the most important single documentary source. "
        "The Westminster Confession of Faith (1647), modelled substantially on Ussher's work, "
        "became the doctrinal standard of Presbyterian churches worldwide.\n\n"
        "The Irish Articles were superseded in Ireland by the Westminster Confession after "
        "the Cromwellian period but represent a crucial transitional document in the "
        "development of Reformed theology — the clearest statement of high-Calvinist "
        "orthodoxy produced in early modern Britain."
    ),
    rels=[
        {"verb": "AUTHORS", "targetSlug": "james-ussher", "targetName": "James Ussher",
         "context": "Ussher drafted the Irish Articles at the 1615 Church of Ireland Convocation"},
        {"verb": "INFLUENCES", "targetSlug": "westminster-confession-of-faith", "targetName": "Westminster Confession of Faith",
         "context": "The Irish Articles were the primary documentary source for the Westminster Confession (1647)"},
        {"verb": "INFLUENCES", "targetSlug": "protestant-reformation", "targetName": "Protestant Reformation",
         "context": "The Irish Articles represent the clearest statement of high-Calvinist orthodoxy in early modern Britain"},
        {"verb": "INFLUENCES", "targetSlug": "church-of-ireland", "targetName": "Church of Ireland",
         "context": "The Irish Articles were the official confessional standard of the Church of Ireland (1615–1647)"},
    ],
    texts=[
        {"slug": "westminster-confession-of-faith", "name": "Westminster Confession of Faith", "year": "1647",
         "role": "The Westminster Confession substantially followed the Irish Articles' structure and doctrinal commitments"},
    ],
    evidence=[
        {"tier": "A", "citation": "Irish Articles of Religion (1615). In Philip Schaff, Creeds of Christendom, vol. 3. New York: Harper, 1877, pp. 526–544."},
        {"tier": "B", "citation": "Ford, Alan. James Ussher: Theology, History and Politics in Early-Modern Ireland and England. Oxford: OUP, 2007."},
    ],
    timeline=[
        {"year": "1615", "event": "Adopted at the Church of Ireland Convocation; Ussher's draft endorsed as the official confession"},
        {"year": "1647", "event": "Westminster Confession published, substantially following the Irish Articles' template"},
        {"year": "1649", "event": "Westminster Confession adopted in Ireland, superseding the Irish Articles"},
    ],
    places=[{"name": "Dublin, Ireland", "role": "Church of Ireland Convocation where the Irish Articles were adopted"}],
    causes=["Protestant need for a precise Calvinist confessional standard in Ireland",
            "Archbishop Ussher's theological expertise and drive to codify Reformed doctrine"],
    effects=["Provided the template for the Westminster Confession, now the standard for Reformed churches worldwide",
             "Established high-Calvinist predestinarianism as the official doctrine of the Church of Ireland"],
    frameworks=["RELIGIOUS_THOUGHT", "REFORMATION_AND_CONFESSIONALISM"],
    subjects=["Church of Ireland", "Calvinism", "Protestant Reformation", "confessional theology",
              "James Ussher", "Early Modern Europe", "predestination"],
    subject_headings=["Irish Articles 1615 — Confessional Theology — Ireland — Early Modern"],
    significance={"significanceScore": 6, "significanceCategory": "regional",
                  "significanceNarrative": "The Irish Articles were the primary source for the Westminster Confession, making them the hidden foundation of global Reformed theology."},
    importance_score=6,
    period="1615",
)

# ── 3. Britannicarum Ecclesiarum Antiquitates ─────────────────────────────────
patch_or_create(
    slug="britannicarum-ecclesiarum-antiquitates",
    class_code="780",
    label="Text",
    name="Britannicarum Ecclesiarum Antiquitates",
    era="Early Modern", era_slug="early-modern", era_div_code="940",
    region="Western Europe", continent="Europe",
    call_number="780.britannicarum-ecclesiarum-antiquitates",
    summary=(
        "Britannicarum Ecclesiarum Antiquitates ('Antiquities of the British Churches') "
        "is a 1639 historical study by James Ussher arguing that the ancient churches of "
        "Britain and Ireland had existed and flourished before the Roman papal mission of "
        "Augustine of Canterbury (597 CE). Drawing on patristic, medieval, and manuscript "
        "evidence assembled over forty years, Ussher traced the British church's origins to "
        "apostolic times — specifically suggesting Joseph of Arimathea founded a church at "
        "Glastonbury — and argued that it had maintained an independent, 'pure' Christianity "
        "before submission to Roman authority.\n\n"
        "The work served as the scholarly foundation for Anglican claims of apostolic "
        "independence from Rome — the argument that the Church of England's authority "
        "derived not from papal grant but from an unbroken apostolic succession predating "
        "the papacy's British influence. Ussher used his mastery of Syriac, Armenian, and "
        "Coptic patristic texts alongside Latin and Greek sources to build his case.\n\n"
        "The Britannicarum Ecclesiarum Antiquitates also contained pioneering scholarship "
        "on early Irish Christianity, documenting the Patrician mission, the Columban "
        "monastic tradition, and the distinctive 'Celtic' liturgical practices that had "
        "differed from Roman usage. It remains a foundational source for the history of "
        "early medieval Christianity in the British Isles."
    ),
    rels=[
        {"verb": "AUTHORS", "targetSlug": "james-ussher", "targetName": "James Ussher",
         "context": "Ussher published Britannicarum Ecclesiarum Antiquitates in 1639 after forty years of manuscript research"},
        {"verb": "INFLUENCES", "targetSlug": "anglican-church", "targetName": "Anglican Church",
         "context": "The work provided the scholarly foundation for Anglican claims of apostolic independence from Rome"},
        {"verb": "INFLUENCES", "targetSlug": "protestant-reformation", "targetName": "Protestant Reformation",
         "context": "Ussher's argument that the pre-Roman British church was 'pure' and Protestant-like supported the Reformation's claim to restore original Christianity"},
    ],
    texts=[],
    evidence=[
        {"tier": "A", "citation": "Ussher, James. Britannicarum Ecclesiarum Antiquitates. Dublin, 1639."},
        {"tier": "B", "citation": "Ford, Alan. James Ussher: Theology, History and Politics. Oxford: OUP, 2007."},
    ],
    timeline=[
        {"year": "1639", "event": "Published in Dublin; immediately recognised as the definitive history of the early British church"},
        {"year": "1687", "event": "Included in Ussher's collected works, ensuring continued scholarly access"},
    ],
    places=[{"name": "Dublin, Ireland", "role": "place of publication (1639)"}],
    causes=["Anglican need for a historical argument against Roman papal authority",
            "Ussher's extraordinary manuscript collection of patristic and medieval sources"],
    effects=["Provided the scholarly foundation for Anglican apostolic independence claims",
             "Pioneered the historical study of early Irish and British Christianity"],
    frameworks=["RELIGIOUS_THOUGHT", "INTELLECTUAL_HISTORY", "REFORMATION_AND_CONFESSIONALISM"],
    subjects=["Anglican Church", "Church of Ireland", "British church history", "Early Modern Europe",
              "James Ussher", "patristics", "apostolic succession"],
    subject_headings=["Britannicarum Ecclesiarum — Church History — Ireland — Early Modern"],
    significance={"significanceScore": 6, "significanceCategory": "regional",
                  "significanceNarrative": "Ussher's Britannicarum Ecclesiarum Antiquitates provided the historical argument that grounded Anglican apostolic independence from Rome."},
    importance_score=6,
    period="Published 1639",
)

# ── 4. Sermon on the Mount ────────────────────────────────────────────────────
patch_or_create(
    slug="sermon-on-the-mount",
    class_code="780",
    label="Text",
    name="Sermon on the Mount",
    era="Classical", era_slug="classical", era_div_code="920",
    region="Middle East", continent="Asia",
    call_number="780.sermon-on-the-mount",
    summary=(
        "The Sermon on the Mount (Matthew 5–7) is Jesus of Nazareth's foundational ethical "
        "discourse, delivered on a hillside in Galilee during his public ministry (c. 27–30 CE). "
        "It is the longest continuous teaching ascribed to Jesus in any Gospel and the most "
        "studied ethical text in Western history. The sermon opens with the Beatitudes "
        "('Blessed are the poor in spirit... Blessed are the peacemakers') — eight pronouncements "
        "of divine favour upon the humble, the grieving, and the persecuted that inverted the "
        "social hierarchies of Roman Palestine.\n\n"
        "The discourse includes the Lord's Prayer — the model prayer that has been recited "
        "daily by billions across two millennia — the Golden Rule ('Do unto others as you "
        "would have them do unto you'), the command to love enemies and pray for persecutors, "
        "warnings against hypocrisy and public piety, the prohibition of divorce (with limited "
        "exceptions), and the injunction not to 'lay up treasures on earth.' Jesus frames "
        "these teachings not as a rejection of the Torah but as its radical deepening: "
        "'You have heard it said... but I say to you.'\n\n"
        "The parallel version in Luke 6:20–49 (the Sermon on the Plain) is shorter and more "
        "starkly class-conscious ('Blessed are the poor... Woe to you who are rich'). Modern "
        "scholarship debates whether the two represent the same speech, variant traditions, "
        "or distinct occasions. The Sermon's ethic of non-violence and enemy-love directly "
        "inspired Tolstoy, Gandhi, and Martin Luther King Jr."
    ),
    rels=[
        {"verb": "AUTHORS", "targetSlug": "jesus-christ", "targetName": "Jesus Christ",
         "context": "Jesus delivered the Sermon on the Mount in Galilee; recorded in Matthew 5–7 and partially in Luke 6"},
        {"verb": "INFLUENCES", "targetSlug": "gospel-of-matthew", "targetName": "Gospel of Matthew",
         "context": "Matthew 5–7 is the primary textual record of the Sermon on the Mount"},
        {"verb": "INFLUENCES", "targetSlug": "christianity", "targetName": "Christianity",
         "context": "The Sermon on the Mount is the foundational ethical discourse of Christianity"},
        {"verb": "INFLUENCES", "targetSlug": "liberation-theology", "targetName": "Liberation Theology",
         "context": "Liberation theologians drew on the Beatitudes' preferential option for the poor as their theological mandate"},
        {"verb": "INFLUENCES", "targetSlug": "gandhi", "targetName": "Mahatma Gandhi",
         "context": "Gandhi cited the Sermon on the Mount — especially the command to love enemies — as a direct inspiration for satyagraha non-violent resistance"},
    ],
    texts=[
        {"slug": "gospel-of-matthew", "name": "Gospel of Matthew", "year": "c. 80–90 CE",
         "role": "Primary text containing the Sermon on the Mount (chapters 5–7)"},
        {"slug": "gospel-of-luke", "name": "Gospel of Luke (Sermon on the Plain)", "year": "c. 80–90 CE",
         "role": "Luke 6:20–49 contains the parallel Sermon on the Plain"},
    ],
    evidence=[
        {"tier": "A", "citation": "Matthew 5–7, New Testament, c. 80–90 CE. Primary text."},
        {"tier": "A", "citation": "Luke 6:20–49, New Testament, c. 80–90 CE. Parallel tradition."},
        {"tier": "C", "citation": "Jeremias, Joachim. The Sermon on the Mount. London: Athlone, 1961."},
        {"tier": "C", "citation": "Stott, John R. W. The Message of the Sermon on the Mount. Downers Grove: IVP, 1978."},
    ],
    timeline=[
        {"year": "c. 27–30 CE", "event": "Jesus delivers the Sermon on a hillside in Galilee"},
        {"year": "c. 80–90 CE", "event": "Matthew's Gospel records the Sermon in its canonical form (chapters 5–7)"},
        {"year": "401 CE", "event": "Augustine of Hippo writes the first systematic commentary on the Sermon on the Mount"},
        {"year": "1894", "event": "Tolstoy's The Kingdom of God Is Within You draws on the Sermon's non-violence ethic"},
        {"year": "1948", "event": "Gandhi credits the Sermon's love-of-enemies teaching as formative for his satyagraha movement"},
    ],
    places=[{"name": "Galilee, Israel", "role": "traditional location of the sermon's delivery, on a hillside above Capernaum"}],
    causes=["Jesus's deep engagement with the Hebrew prophetic tradition of justice and covenant faithfulness",
            "The social context of Roman-occupied Galilee — poverty, oppression, messianic expectation"],
    effects=["Provided the ethical core of Christianity — the Beatitudes, Lord's Prayer, Golden Rule",
             "Inspired Tolstoy's Christian anarchism, Gandhi's satyagraha, and King's non-violent civil rights movement",
             "The most quoted single text in the history of Western ethics and political thought"],
    frameworks=["RELIGIOUS_THOUGHT", "SOCIAL_REVOLUTION", "LIBERATION_THEOLOGY", "CAUSE_AND_EFFECT"],
    subjects=["Jesus Christ", "Christianity", "ethics", "New Testament", "Galilee", "Matthew",
              "Beatitudes", "Lord's Prayer", "non-violence"],
    subject_headings=["Sermon on the Mount — Christian Ethics — Galilee — Classical Era"],
    significance={"significanceScore": 9, "significanceCategory": "world-changing",
                  "significanceNarrative": "The Sermon on the Mount is the most cited ethical text in Western history, inspiring Christian moral theology, non-violent resistance movements, and political philosophy across two millennia."},
    importance_score=9,
    period="c. 27–30 CE",
    wikipedia_url="https://en.wikipedia.org/wiki/Sermon_on_the_Mount",
)

# ── 5. Nicene Creed ───────────────────────────────────────────────────────────
patch_or_create(
    slug="nicene-creed",
    class_code="012",
    label="Idea",
    name="Nicene Creed",
    era="Classical", era_slug="classical", era_div_code="920",
    region="Global", continent="Global",
    call_number="012.nicene-creed",
    summary=(
        "The Nicene Creed is the foundational doctrinal statement of Christian orthodoxy, "
        "first formulated at the First Council of Nicaea (325 CE) and expanded at the "
        "First Council of Constantinople (381 CE). It defines Jesus Christ as 'God from "
        "God, Light from Light, true God from true God, begotten not made, of one substance "
        "(homoousios) with the Father' — the formula that resolved the Arian controversy "
        "by asserting Christ's full and co-equal divinity.\n\n"
        "The Creed is the most universally accepted statement of Christian belief, recited "
        "in Catholic, Orthodox, Anglican, and most Protestant liturgies worldwide. Its "
        "development at Nicaea under Constantine I was the first time the Roman state "
        "sponsored the definition of Christian doctrine, permanently linking imperial power "
        "and theological orthodoxy. The insertion of the Latin word filioque ('and the Son') "
        "by the Western church — asserting that the Holy Spirit proceeds from both Father "
        "and Son — was the primary theological cause of the Great Schism of 1054 between "
        "Eastern and Western Christianity."
    ),
    rels=[
        {"verb": "INFLUENCES", "targetSlug": "jesus-christ", "targetName": "Jesus Christ",
         "context": "The Nicene Creed defines orthodox doctrine about who Jesus Christ is"},
        {"verb": "INFLUENCES", "targetSlug": "constantine-i", "targetName": "Constantine I",
         "context": "Constantine convened and presided over the Council of Nicaea (325 CE) that produced the creed"},
        {"verb": "INFLUENCES", "targetSlug": "christianity", "targetName": "Christianity",
         "context": "The Nicene Creed became the defining doctrinal standard for all branches of Christianity"},
    ],
    texts=[],
    evidence=[
        {"tier": "A", "citation": "Council of Nicaea (325 CE). Creedal formula. In Philip Schaff, Creeds of Christendom, vol. 2. New York: Harper, 1877."},
        {"tier": "B", "citation": "Hanson, R. P. C. The Search for the Christian Doctrine of God. Edinburgh: T&T Clark, 1988."},
    ],
    timeline=[
        {"year": "325 CE", "event": "First Council of Nicaea; first version of the Nicene Creed formulated"},
        {"year": "381 CE", "event": "First Council of Constantinople; Nicene Creed expanded to its present form"},
        {"year": "1054 CE", "event": "Great Schism: Western church's filioque addition becomes the theological flashpoint"},
    ],
    places=[{"name": "Nicaea, Bithynia", "role": "site of the First Council of Nicaea (325 CE)"}],
    causes=["Arian controversy (c. 318 CE) threatening to split the church over Christ's divine nature",
            "Constantine's desire for theological unity across the empire"],
    effects=["Defined orthodox Christology — Christ as fully divine and co-equal with the Father",
             "Established the template for all subsequent ecumenical councils",
             "The filioque addition became the theological cause of the 1054 Great Schism"],
    frameworks=["RELIGIOUS_THOUGHT", "EMPIRE_AND_COLONIALISM", "IDEAS_AND_WORLDVIEWS"],
    subjects=["Christianity", "Christology", "Council of Nicaea", "Constantine", "orthodoxy", "creed"],
    subject_headings=["Nicene Creed — Christian Doctrine — Roman Empire — Classical Era"],
    significance={"significanceScore": 8, "significanceCategory": "world-changing",
                  "significanceNarrative": "The Nicene Creed defined the theological core of Christianity and has been recited by billions across 1,700 years."},
    importance_score=8,
    period="325 CE",
    wikipedia_url="https://en.wikipedia.org/wiki/Nicene_Creed",
)

# ── 6. John the Baptist (update — thin at 252c) ───────────────────────────────
patch_or_create(
    slug="john-the-baptist",
    class_code="251",
    label="Person",
    name="John the Baptist",
    era="Classical", era_slug="classical", era_div_code="920",
    region="Middle East", continent="Asia",
    call_number="251.john-the-baptist",
    summary=(
        "John the Baptist (c. 6 BCE – c. 28–30 CE) was a Jewish prophet and ascetic who "
        "preached repentance and baptism by immersion in the Jordan River as preparation "
        "for an imminent divine judgement. The New Testament identifies him as the immediate "
        "precursor of Jesus Christ, and all four Gospels open the narrative of Jesus's "
        "ministry with John's baptism of him. The Jewish historian Josephus (Antiquities "
        "XVIII.5.2) independently confirms John's existence and execution, making him one "
        "of the best-attested figures in early Christian history.\n\n"
        "John emerged from the desert of Judea, wearing camel's hair and eating locusts and "
        "wild honey — imagery deliberately evoking the prophet Elijah. He preached at the "
        "Jordan River, baptising Jewish people who confessed their sins. His baptism of Jesus "
        "(c. 27–29 CE) inaugurated Jesus's public ministry. John was arrested by Herod "
        "Antipas, tetrarch of Galilee, for publicly condemning Herod's marriage to his "
        "brother's wife Herodias; he was subsequently beheaded at the request of Herodias's "
        "daughter Salome.\n\n"
        "John's movement of water-baptism as a one-time initiatory rite became one of the "
        "structural foundations of Christianity. Islam venerates him as Yahya, a prophet "
        "mentioned in the Quran. The Mandaeans — an ancient Gnostic religion — regard John "
        "as their supreme prophet, greater than Jesus, with baptism at the centre of their "
        "practice to this day."
    ),
    rels=[
        {"verb": "INFLUENCES", "targetSlug": "jesus-christ", "targetName": "Jesus Christ",
         "context": "John baptised Jesus in the Jordan River, publicly inaugurating his ministry and identifying him as 'the one who comes after me'"},
        {"verb": "INFLUENCES", "targetSlug": "christianity", "targetName": "Christianity",
         "context": "John's baptism ritual became the model for Christian baptism — the foundational initiation rite of the church"},
        {"verb": "INFLUENCES", "targetSlug": "islam", "targetName": "Islam",
         "context": "Islam venerates John as the prophet Yahya, mentioned in Quran 3:39 as a messenger sent to prepare the way"},
        {"verb": "OCCURS_IN", "targetSlug": "jordan-river", "targetName": "Jordan River",
         "context": "John conducted his baptism ministry at the Jordan River, the symbolic boundary of the Promised Land"},
    ],
    texts=[
        {"slug": "gospel-of-mark", "name": "Gospel of Mark", "year": "c. 65–70 CE",
         "role": "Mark opens with John's baptising ministry (chapter 1)"},
        {"slug": "josephus-antiquities", "name": "Josephus, Antiquities XVIII.5.2", "year": "c. 93 CE",
         "role": "Josephus independently confirms John's ministry and execution by Herod Antipas"},
    ],
    evidence=[
        {"tier": "A", "citation": "Mark 1:1–11; Matthew 3; Luke 3; John 1:19–36. Four canonical gospel accounts."},
        {"tier": "B", "citation": "Josephus, Flavius. Antiquities of the Jews XVIII.5.2, c. 93 CE. Confirms John's execution by Herod Antipas."},
        {"tier": "C", "citation": "Meier, John P. A Marginal Jew, vol. 2. Chapters 12–14. Detailed historical analysis of John the Baptist."},
    ],
    timeline=[
        {"year": "c. 6 BCE", "event": "Birth to Zechariah (a Temple priest) and Elizabeth (a kinswoman of Mary); announced by the angel Gabriel (Luke 1)"},
        {"year": "c. 27–29 CE", "event": "Begins his desert preaching and baptising ministry on the Jordan River"},
        {"year": "c. 27–29 CE", "event": "Baptises Jesus; inaugurates the beginning of Jesus's public ministry"},
        {"year": "c. 28–30 CE", "event": "Arrested by Herod Antipas for condemning the king's marriage to Herodias"},
        {"year": "c. 28–30 CE", "event": "Beheaded in the fortress of Machaerus; his head presented to Herodias's daughter Salome"},
    ],
    places=[
        {"name": "Jordan River, Judea", "role": "site of John's baptism ministry"},
        {"name": "Judean Desert", "role": "John's ascetic home base"},
        {"name": "Fortress of Machaerus", "role": "site of John's imprisonment and execution by Herod Antipas"},
    ],
    causes=["Jewish prophetic tradition calling for repentance and preparation for God's judgement",
            "Roman occupation intensifying Jewish messianic and apocalyptic expectation"],
    effects=["His baptism of Jesus inaugurated the most consequential ministry in world history",
             "His baptism ritual became the foundational initiation rite of Christianity",
             "His condemnation of Herod Antipas established the prophetic tradition of speaking truth to power"],
    frameworks=["RELIGIOUS_THOUGHT", "CAUSE_AND_EFFECT", "SOCIAL_REVOLUTION"],
    subjects=["Christianity", "Judaism", "baptism", "prophet", "Jesus Christ", "Classical era",
              "Roman Empire", "Galilee", "Josephus"],
    subject_headings=["John the Baptist — Jewish Prophetic Tradition — Judea — Classical Era"],
    significance={"significanceScore": 7, "significanceCategory": "continental",
                  "significanceNarrative": "John the Baptist was the immediate precursor of Jesus Christ, the originator of Christian baptism, and the first figure in the New Testament narrative to be independently confirmed by Josephus."},
    importance_score=7,
    born="c. 6 BCE",
    died="c. 28–30 CE",
    wikipedia_url="https://en.wikipedia.org/wiki/John_the_Baptist",
    wikidata_qid="Q128285",
)

# ── 7. Westminster Confession of Faith (update — thin at 118c) ────────────────
patch_or_create(
    slug="westminster-confession-of-faith",
    class_code="012",
    label="Idea",
    name="Westminster Confession of Faith",
    era="Early Modern", era_slug="early-modern", era_div_code="940",
    region="Western Europe", continent="Europe",
    call_number="012.westminster-confession-of-faith",
    summary=(
        "The Westminster Confession of Faith (1647) is the primary doctrinal standard "
        "of the Reformed and Presbyterian churches worldwide. Produced by the Westminster "
        "Assembly of Divines — 121 theologians convened by the English Parliament in "
        "1643 — the Confession defined orthodox Calvinism across 33 chapters covering "
        "Scripture, the Trinity, predestination, covenant theology, the church, and the "
        "sacraments. It was adopted by the Church of Scotland in 1647 and by English "
        "Presbyterians in 1648, and continues to serve as the confessional standard of "
        "Presbyterian churches in the US, UK, Australia, South Korea, and worldwide.\n\n"
        "The Confession's theological structure was substantially indebted to James "
        "Ussher's Irish Articles of 1615 — the most directly formative documentary "
        "source. It endorsed covenant theology (the idea that God relates to humanity "
        "through successive covenants), the infallibility of scripture, and the "
        "predestination of the elect to salvation and the reprobate to damnation. "
        "Chapter 1 ('Of the Holy Scripture') provided the most precise Protestant "
        "definition of biblical authority, with its doctrine of Scripture's "
        "self-authentication (autopistia) becoming the cornerstone of Reformed epistemology.\n\n"
        "The Westminster Confession, together with the Larger and Shorter Catechisms, "
        "constitutes the 'Westminster Standards' — the doctrinal package adopted by "
        "most Presbyterian denominations and widely used in Reformed theological education."
    ),
    rels=[
        {"verb": "INFLUENCES", "targetSlug": "james-ussher", "targetName": "James Ussher",
         "context": "Ussher's Irish Articles (1615) were the primary documentary source for the Westminster Confession"},
        {"verb": "INFLUENCES", "targetSlug": "protestant-reformation", "targetName": "Protestant Reformation",
         "context": "The Confession represents the fullest doctrinal achievement of the Calvinist wing of the Reformation"},
        {"verb": "INFLUENCES", "targetSlug": "church-of-ireland", "targetName": "Church of Ireland",
         "context": "The Westminster Confession superseded the Irish Articles as the confessional standard of the Church of Ireland"},
        {"verb": "INFLUENCES", "targetSlug": "reformed-theology", "targetName": "Reformed Theology",
         "context": "The Confession remains the primary doctrinal standard of Reformed and Presbyterian churches worldwide"},
    ],
    texts=[
        {"slug": "irish-articles-1615", "name": "Irish Articles (1615)", "year": "1615",
         "role": "The primary documentary source Ussher's Irish Articles provided for the Westminster Confession's structure"},
    ],
    evidence=[
        {"tier": "A", "citation": "Westminster Confession of Faith (1647). In Philip Schaff, Creeds of Christendom, vol. 3. New York: Harper, 1877, pp. 600–673."},
        {"tier": "B", "citation": "Mitchell, Alexander F. The Westminster Assembly: Its History and Standards. London: Nisbet, 1883."},
        {"tier": "C", "citation": "Letham, Robert. The Westminster Assembly: Reading Its Theology in Historical Context. Phillipsburg, NJ: P&R, 2009."},
    ],
    timeline=[
        {"year": "1643", "event": "Westminster Assembly convened by the English Parliament; 121 divines begin deliberations"},
        {"year": "1647", "event": "Westminster Confession of Faith completed; adopted by the Church of Scotland"},
        {"year": "1648", "event": "Adopted by English Presbyterians; the Westminster Standards (Confession + Catechisms) distributed widely"},
        {"year": "1788", "event": "American Presbyterians adopt a revised version as the constitution of the Presbyterian Church (USA)"},
    ],
    places=[{"name": "Westminster, London", "role": "location of the Westminster Assembly (1643–53) at Westminster Abbey and Chapel"}],
    causes=["The English Civil War's demand for doctrinal clarity in the established church",
            "Scottish insistence on Presbyterian church government as the price for military alliance with Parliament",
            "James Ussher's Irish Articles providing the theological template"],
    effects=["Became the doctrinal standard for Presbyterian churches worldwide",
             "Defined the Reformed doctrine of Scripture's authority (autopistia)",
             "Shaped Reformed theological education across Britain, the US, South Korea, and beyond"],
    frameworks=["RELIGIOUS_THOUGHT", "REFORMATION_AND_CONFESSIONALISM", "INTELLECTUAL_HISTORY"],
    subjects=["Protestant Reformation", "Calvinism", "Reformed theology", "Presbyterianism",
              "confessional theology", "Westminster Assembly", "James Ussher", "Early Modern Europe"],
    subject_headings=["Westminster Confession — Reformed Theology — England/Scotland — Early Modern"],
    significance={"significanceScore": 8, "significanceCategory": "continental",
                  "significanceNarrative": "The Westminster Confession is the defining doctrinal statement of global Presbyterianism and Reformed theology, directly shaped by Ussher's Irish Articles and used by hundreds of denominations worldwide."},
    importance_score=8,
    period="1647",
    wikipedia_url="https://en.wikipedia.org/wiki/Westminster_Confession_of_Faith",
)

# ── 8. Trinity College Dublin (update — thin at 97c) ──────────────────────────
patch_or_create(
    slug="trinity-college-dublin",
    class_code="350",
    label="Institution",
    name="Trinity College Dublin",
    era="Early Modern", era_slug="early-modern", era_div_code="940",
    region="Western Europe", continent="Europe",
    call_number="350.trinity-college-dublin",
    summary=(
        "Trinity College Dublin (TCD) — formally the College of the Holy and Undivided "
        "Trinity of Queen Elizabeth near Dublin — was founded in 1592 by Queen Elizabeth I "
        "as Ireland's first university, modelled on Cambridge colleges. Its founding charter "
        "aimed to provide Protestant education in Ireland and to prevent Irish students from "
        "receiving Catholic education abroad. James Ussher was among the first students "
        "admitted (1594) and became a co-founder in the sense that he helped establish its "
        "curriculum and library — donating his 10,000-volume manuscript collection that "
        "became the nucleus of the TCD Library.\n\n"
        "TCD's Library is home to the Book of Kells — the illuminated 9th-century Gospel "
        "manuscript, one of the most celebrated medieval artefacts in the world — as well "
        "as the oldest surviving harp in Ireland. The library's Long Room (1732) is one of "
        "the world's great baroque library interiors, containing 200,000 of the oldest books "
        "in TCD's collection.\n\n"
        "Among TCD's notable alumni are Jonathan Swift (author of Gulliver's Travels), "
        "Edmund Burke (political philosopher), Wolfe Tone (revolutionary), Oscar Wilde "
        "(playwright), and Samuel Beckett (Nobel laureate). The college remained exclusively "
        "Protestant until 1873 and continued to ban Catholics from attending without special "
        "dispensation until 1970."
    ),
    rels=[
        {"verb": "INFLUENCES", "targetSlug": "james-ussher", "targetName": "James Ussher",
         "context": "Ussher was among TCD's first students (1594) and later its Chancellor; donated his library as the founding collection"},
        {"verb": "INFLUENCES", "targetSlug": "protestant-reformation", "targetName": "Protestant Reformation",
         "context": "TCD was founded as a Protestant university to counter Catholic education in Ireland"},
        {"verb": "CONTAINS", "targetSlug": "book-of-kells", "targetName": "Book of Kells",
         "context": "The TCD Library has housed the Book of Kells since 1661 — the world's most famous illuminated manuscript"},
    ],
    texts=[
        {"slug": "book-of-kells", "name": "Book of Kells", "year": "c. 800 CE",
         "role": "Housed in TCD Library since 1661; the most visited exhibit in Ireland"},
    ],
    evidence=[
        {"tier": "A", "citation": "Charter of Foundation, 1592. Trinity College Dublin Archives."},
        {"tier": "C", "citation": "McDowell, R. B. and D. A. Webb. Trinity College Dublin 1592–1952. Cambridge: CUP, 1982."},
    ],
    timeline=[
        {"year": "1592", "event": "Founded by Queen Elizabeth I; first provost William Doily appointed"},
        {"year": "1594", "event": "James Ussher admitted as one of the first students"},
        {"year": "1661", "event": "Book of Kells transferred from Kells to the TCD Library for safekeeping"},
        {"year": "1732", "event": "Long Room library building completed — now one of the world's great baroque library interiors"},
        {"year": "1873", "event": "Religious tests abolished; non-Protestants formally admitted"},
        {"year": "1970", "event": "Catholic Church lifts its ban on Catholics attending TCD"},
    ],
    places=[{"name": "Dublin, Ireland", "role": "location of Trinity College Dublin; founded 1592"}],
    causes=["Queen Elizabeth I's policy of Protestant education in Ireland to counter Catholic influence",
            "Irish Protestant desire for a university without requiring travel to England"],
    effects=["Became Ireland's premier university; produced Swift, Burke, Wilde, Beckett",
             "Ussher's donated library became one of the great manuscript collections in Europe",
             "The TCD Library's Book of Kells is now the most visited cultural site in Ireland"],
    frameworks=["INTELLECTUAL_HISTORY", "REFORMATION_AND_CONFESSIONALISM", "PRINT_CULTURE_AND_KNOWLEDGE"],
    subjects=["Ireland", "education", "Protestant Reformation", "Early Modern Europe",
              "James Ussher", "manuscript", "Book of Kells", "Dublin"],
    subject_headings=["Trinity College Dublin — University — Ireland — Early Modern"],
    significance={"significanceScore": 6, "significanceCategory": "regional",
                  "significanceNarrative": "Trinity College Dublin was Ireland's first university and the intellectual home of James Ussher; its library houses the Book of Kells and Ussher's donated manuscript collection."},
    importance_score=6,
    period="Founded 1592",
    wikipedia_url="https://en.wikipedia.org/wiki/Trinity_College_Dublin",
)

print("\nBatch 67c complete. Created/updated: Annales Veteris Testamenti, Irish Articles,")
print("Britannicarum, Sermon on the Mount, Nicene Creed, John the Baptist (updated),")
print("Westminster Confession (updated), Trinity College Dublin (updated).")
