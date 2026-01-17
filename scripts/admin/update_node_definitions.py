#!/usr/bin/env python3
"""
Systematically update node description/definition fields in cluster JSON files.

Rules per docs/nodes/node-attribute-registry.md:
- Place nodes: is_generic=true, atemporal description (free of time/space)
- Idea/Institution/Movement: prefer `definition` (concise, ≤160 chars)
- Person/Event/Text/Artifact: prefer `description` (contextual)

For Place nodes: definitions must be generic geographic/topographical facts,
not tied to any historical period.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────────────
# PLACE NODE DEFINITIONS (timeless, free of space/time)
# ─────────────────────────────────────────────────────────────────────────────
PLACE_DEFINITIONS = {
    "Cambridge": "University city in eastern England on the River Cam; historic center of learning and scholarship.",
    "Canterbury": "City in southeast England; traditional seat of the senior bishop of the Church of England.",
    "Cornwall": "Southwestern peninsula county of England, bounded by the Atlantic Ocean and English Channel.",
    "Devon": "County in southwest England between Cornwall and Dorset; varied landscape of moors, coasts, and farmland.",
    "Douai": "City in northern France; historic center for English-language Catholic scholarship and publishing.",
    "East_Anglia": "Region of eastern England comprising Norfolk, Suffolk, and parts of Cambridgeshire and Essex.",
    "England": "Country forming the southern portion of Great Britain; bounded by Scotland, Wales, and surrounding seas.",
    "London": "Capital city of England on the River Thames; historic center of commerce, government, and culture.",
    "Oxford": "University city in south-central England on the River Thames; historic center of learning and theology.",
    "Rome": "City in central Italy on the Tiber River; historic seat of the papacy and center of the Roman Catholic Church.",
    "York": "City in northern England at the confluence of the Rivers Ouse and Foss; historic ecclesiastical and political center.",
}

# ─────────────────────────────────────────────────────────────────────────────
# IDEA/INSTITUTION/MOVEMENT DEFINITIONS (concise, ≤160 chars)
# ─────────────────────────────────────────────────────────────────────────────
IDEA_DEFINITIONS = {
    # Archbishop/clergy roles
    "Archbishop_enforcing_conformity": "Episcopal authority requiring adherence to established liturgical and doctrinal standards.",
    "Archbishop_shaping_annulment_and_liturgy": "Archiepiscopal role in adjudicating royal marriage cases and revising worship forms.",
    "Archbishop_shaping_the_settlement_and_articles": "Archiepiscopal role in formulating doctrinal standards and church governance.",
    "Archbishop_with_cautious_stance_toward_prophesyings": "Episcopal position balancing clerical education exercises against perceived disorder.",
    
    # Texts and Bibles
    "Author_of_Acts_and_Monuments_chronicling_martyrs": "Compiler of martyrological records documenting religious persecution.",
    "Authorized_Elizabethan_Bible": "Officially sanctioned English Scripture translation for church use.",
    "Authorized_English_Bible_for_churches": "Vernacular Scripture authorized for public reading in parish worship.",
    "Authorized_sermons_for_instruction": "Official homilies prescribed for clerical use in parish teaching.",
    
    # Persons/roles as ideas
    "Bishop_martyred_during_Marian_persecutions": "Protestant bishop executed for heresy during the Marian restoration.",
    "Boy_king_under_Protestant_reforms": "Minor monarch under regency during which Protestant reforms advanced.",
    
    # Campaigns and movements
    "Campaigns_against_Protestant_dissent_under_Mary": "Prosecutorial efforts against Protestant belief during the Marian restoration.",
    "Catholic_English_translation_with_annotations": "English Scripture translation with Catholic interpretive apparatus.",
    "Catholic_hierarchy_and_institutions": "Ecclesiastical structures maintaining communion with the papacy.",
    "Catholic_practice_under_legal_penalties": "Recusancy: continued Catholic worship despite statutory prohibitions.",
    "Congregational_separation_from_established_church": "Separatism: withdrawal from the national church to form independent congregations.",
    "Consolidation_of_monarchs_authority_over_the_church": "Royal supremacy: crown authority over ecclesiastical governance.",
    "Continental_Reformations": "Protestant reform movements originating in German, Swiss, and French territories.",
    "Continental_seminary_city_for_English_clergy": "Overseas institution training Catholic clergy for English mission work.",
    
    # Courts and councils
    "Council_court_involved_in_censorshipenforcement": "Prerogative court exercising jurisdiction over press and publication.",
    "Court_of_Augmentations": "Tudor administrative body managing revenues from dissolved monasteries.",
    "Courts_handling_ecclesiastical_matters": "Church courts exercising jurisdiction over spiritual and moral cases.",
    
    # Decisions and decrees
    "Decision_enabling_annulment_proceedings": "Canonical ruling permitting ecclesiastical review of a royal marriage.",
    "Decrees_facilitating_reconciliation_with_Rome": "Legislative acts restoring papal jurisdiction over the English church.",
    "Deployment_of_seminary_clergy_into_England": "Mission: dispatch of trained priests from continental seminaries.",
    "Directives_mandating_English_Bible_placement": "Injunctions requiring vernacular Scripture in parish churches.",
    "Dispute_over_clerical_vestments": "Vestiarian controversy: conflict over liturgical dress requirements.",
    
    # Doctrinal statements
    "Doctrinal_articles_under_Edward_VI": "Confessional formulary defining Protestant doctrine during the Edwardian era.",
    "Doctrinal_articles_under_Elizabeth_I": "Thirty-Nine Articles: confessional standard of the Elizabethan church.",
    "Doctrinal_claim_of_supreme_papal_authority_in_the_church": "Papal supremacy: doctrine that the pope holds universal jurisdiction.",
    "Doctrinal_reaffirmations_under_Henry_VIII": "Six Articles: conservative doctrinal statement affirming traditional practices.",
    "Doctrinal_statement_under_Henry_VIII": "Ten Articles: early Henrician doctrinal formulary.",
    
    # Early reform
    "Early_Edwardian_reform_directives": "Royal injunctions implementing Protestant changes early in Edward VI's reign.",
    "Eastern_English_county": "Administrative division in East Anglia.",
    
    # Ecclesiastical bodies
    "Ecclesiastical_commission_enforcing_conformity": "High Commission: royal tribunal enforcing religious uniformity.",
    "Editortranslator_of_English_Bibles": "Scholar producing or revising vernacular Scripture editions.",
    
    # Edward and regents
    "Edward_Seymour_Somerset": "Duke of Somerset; Lord Protector during early Edwardian reforms.",
    "Efforts_to_reshape_church_polity_along_presbyterian_lines": "Presbyterian reform: movement to replace episcopacy with elder governance.",
    
    # Elizabethan settlement
    "Enactment_of_the_Elizabethan_settlement": "Parliamentary legislation establishing the Elizabethan religious framework.",
    "Enforcement_of_penalties_for_nonattendance": "Recusancy laws: fines and penalties for absence from parish worship.",
    "English_Bible_translator_influencing_reforms": "Scholar whose vernacular translation shaped Protestant devotion.",
    "English_Realm": "The kingdom of England as a sovereign political entity.",
    "English_Reformation": "Religious transformation separating the English church from papal authority.",
    "English_capital_and_legislative_center": "London as seat of Parliament and royal government.",
    "English_university_shaping_clergy_and_thought": "Academic institution training clergy and developing theological scholarship.",
    "Episodes_of_image_removal_in_reform": "Iconoclasm: destruction of religious images during Protestant reform.",
    
    # Executions and foreign policy
    "Execution_impacting_Catholic_and_foreign_policy": "State execution affecting relations with Catholic powers.",
    "Executions_of_Latimer_Ridley_and_Cranmer": "Oxford Martyrs: Protestant bishops burned during the Marian restoration.",
    "Executive_advisory_body": "Privy Council: royal advisory board overseeing administration.",
    
    # First liturgy
    "First_English_liturgy_book": "Book of Common Prayer (1549): first vernacular service book.",
    
    # Hooker
    "Hookers_defense_of_the_settlement": "Laws of Ecclesiastical Polity: apologetic for the Elizabethan church order.",
    
    # Humanist/intellectual
    "Humanist_statesman_opposing_royal_supremacy": "Learned official who resisted crown authority over the church.",
    "Intellectual_currents_shaping_reformers_and_opponents": "Renaissance humanism and scholasticism influencing religious debate.",
    
    # Issuance
    "Issuance_of_doctrinal_articles": "Promulgation of confessional standards by convocation or crown.",
    "Issuance_of_the_ThirtyNine_Articles": "Adoption of the Elizabethan doctrinal formulary.",
    
    # Jesuits
    "Jesuit_missionary_to_England": "Member of the Society of Jesus engaged in English mission work.",
    "Jesuit_order_coordinating_missions": "Society of Jesus: Catholic religious order directing missionary activity.",
    "Jesuit_organizer_of_English_mission": "Jesuit superior directing priests sent to England.",
    "John_Dudley_Northumberland": "Duke of Northumberland; regent advancing Protestant reform.",
    "John_Foxes_martyrology": "Acts and Monuments: record of Protestant martyrs.",
    
    # Legal/legislative
    "Legal_and_ecclesiastical_process_to_end_Henrys_marriage": "Annulment proceedings: canonical process dissolving a royal marriage.",
    "Legal_framework_enabling_prosecutions": "Heresy laws: statutes permitting prosecution for heterodox belief.",
    "Legislative_body_enacting_religious_statutes": "Parliament: bicameral assembly passing ecclesiastical legislation.",
    "Legislative_enactment_of_royal_supremacy": "Acts of Supremacy: statutes declaring crown headship of the church.",
    "Liturgical_revision_during_Edwardian_era": "Prayer book revision: reform of public worship under Edward VI.",
    
    # Lord Protector
    "Lord_Protector_leading_early_reforms": "Regent governing during a minority and implementing religious change.",
    
    # Marian era
    "Marianera_episcopal_leadership": "Bishops appointed during Mary I's reign to restore Catholicism.",
    "Measures_restoring_Catholic_structures": "Marian legislation reversing Henrician and Edwardian reforms.",
    "Middle_way_balancing_Protestant_and_Catholic_elements": "Via media: moderate religious position avoiding extremes.",
    "Minister_administering_dissolution_and_reform": "Royal minister overseeing monastic suppression and church policy.",
    "Monarchical_governance_apparatus": "Tudor Crown: royal executive authority and administration.",
    "National_church_reconfigured_under_the_Tudors": "Church of England as reformed national institution.",
    
    # Northern
    "Northern_earls_revolt_with_religious_dimension": "Rising of the North: rebellion with Catholic and feudal grievances.",
    "Northern_ecclesiastical_and_political_center": "York as seat of the northern province and regional governance.",
    "Northern_uprising_against_policies_including_dissolution": "Pilgrimage of Grace: northern protest against Henrician reforms.",
    
    # Office/organization
    "Office_managing_monastic_properties_postdissolution": "Court of Augmentations: body administering former monastic lands.",
    "Organized_Jesuit_mission_to_England": "English Mission: coordinated Jesuit pastoral activity in England.",
    "Organized_missionary_activity_by_Jesuits": "Mission: systematic dispatch of priests to Catholic communities.",
    "Overseas_seminaries_training_English_clergy": "Continental colleges preparing priests for the English mission.",
    
    # Pamphlet/papal
    "Pamphlet_war_critical_of_bishops": "Marprelate Controversy: satirical attacks on episcopacy.",
    "Papal_bull_excommunicating_Elizabeth_I": "Regnans in Excelsis: papal decree deposing Elizabeth I.",
    "Papal_legate_and_archbishop_under_Mary": "Cardinal Pole: papal representative reconciling England to Rome.",
    "Placement_of_English_Bibles_in_parish_churches": "Bible provision: requirement to furnish vernacular Scripture.",
    "Politicalecclesiastical_rupture_from_papal_authority": "Break with Rome: severance of English church from papal jurisdiction.",
    "Pope_involved_in_annulment_diplomacy": "Clement VII: pope presiding over Henry VIII's annulment case.",
    "Popular_English_Bible_with_notes": "Geneva Bible: widely used Protestant translation with marginal commentary.",
    
    # Preacher/principal
    "Preacher_reformer_later_martyred": "Protestant clergyman executed for heresy.",
    "Principal_minister_guiding_governance": "Chief minister: leading royal adviser directing policy.",
    "Prosecutions_for_heresy_under_Mary": "Marian persecutions: trials and executions for Protestant belief.",
    "Protestant_teachings_adopted_in_England": "Reformed doctrine: Protestant theology received in the English church.",
    "Push_to_render_scripture_in_English": "Vernacular Bible movement: effort to translate Scripture into English.",
    
    # Queens as ideas
    "Queen_contesting_the_annulment_proceedings": "Catherine of Aragon's canonical defense of her marriage.",
    "Queen_establishing_the_Elizabethan_settlement": "Elizabeth I's religious policy creating moderate Protestantism.",
    "Queen_influencing_the_break_with_Rome": "Anne Boleyn's marriage precipitating royal supremacy.",
    "Queen_restoring_Catholicism": "Mary I's policy reversing Protestant reforms.",
    
    # Reform
    "Reform_directives_to_clergy_and_laity": "Royal injunctions: administrative orders implementing religious change.",
    "Reform_movement_seeking_further_changes": "Puritanism: movement pressing for more thorough Protestant reform.",
    "Reformer_advocating_further_changes": "Puritan: Protestant seeking additional reform beyond the settlement.",
    "Regency_governance_under_Edward_VI": "Protectorate: minority government directing Edwardian reforms.",
    "Regent_advancing_Protestant_policies": "Lord Protector or councillor promoting religious change.",
    "Reinstatement_of_Catholic_practices_and_structures": "Marian restoration: return to papal communion and Catholic rites.",
    "Resistance_to_Prayer_Book_and_reforms_in_the_West": "Western Rising: rebellion against the 1549 Prayer Book.",
    "Restoration_of_communion_with_Papacy": "Reconciliation: formal return of England to papal obedience.",
    
    # Additional concept placeholders
    "Revised_English_liturgy_book": "Revised Book of Common Prayer used in Edwardian reforms.",
    "Rising_against_Marian_regime_and_Spanish_match": "Wyatt's Rebellion: uprising against Mary I's Spanish marriage.",
    "Rival_claimant_whose_execution_affected_policy": "Catholic claimant whose execution reshaped English policy.",
    "Seat_of_the_Archbishop_of_Canterbury": "Canterbury: metropolitan see of the Archbishop of Canterbury.",
    "Second_book_of_homilies": "Second Book of Homilies (1571), authorized sermons for instruction.",
    "Social_and_religious_unrest_in_Norfolk": "Social and religious unrest in Norfolk during the Reformation era.",
    "Southwestern_English_county": "County in southwest England.",
    "Spanish_naval_campaign_against_England": "Spanish Armada: naval invasion attempt against England (1588).",
    "Statute_asserting_royal_supremacy_over_the_church": "Act of Supremacy (1534) asserting royal supremacy.",
    "Statute_enforcing_liturgical_conformity": "Act of Uniformity requiring use of the Book of Common Prayer.",
    "Statute_reasserting_royal_supremacy": "Act of Supremacy (1559) restoring royal supremacy.",
    "Suppression_and_redistribution_of_monastic_houses": "Dissolution of the Monasteries: suppression and redistribution of houses.",
    "Suppression_of_chantries_and_endowments": "Suppression of chantries and guild endowments under Edward VI.",
    "Survey_of_ecclesiastical_wealth": "Valor Ecclesiasticus: survey of church wealth commissioned by Henry VIII.",
    "The_Institution_of_a_Christian_Man": "Bishops' Book (1537), doctrinal manual of the English church.",
    "Theologian_articulating_via_media": "Theologian articulating a moderate Anglican via media.",
    "Tudor_monarch_initiating_royal_supremacy": "Tudor monarch asserting royal supremacy over the English church.",
    "University_city_and_site_of_martyrdoms": "Oxford: university city and site of Protestant martyrdoms.",
    "University_city_shaping_clergy_and_thought": "Cambridge: university shaping clergy and reformist thought.",
    "Western_English_county": "County in western England.",
}

# ─────────────────────────────────────────────────────────────────────────────
# PERSON DESCRIPTIONS (contextual, biographical)
# ─────────────────────────────────────────────────────────────────────────────
PERSON_DESCRIPTIONS = {
    "Anne_Boleyn": "Queen of England 1533-1536. Second wife of Henry VIII. Her marriage to the king required the break with papal authority. Mother of Elizabeth I. Executed 1536.",
    "Catherine_of_Aragon": "Queen of England 1509-1533. First wife of Henry VIII. Spanish princess and daughter of Ferdinand and Isabella. Her contested annulment precipitated the English Reformation.",
    "Edmund_Campion": "Jesuit priest and missionary. Led the 1580 English Jesuit mission with Robert Parsons; executed for treason in 1581.",
    "Edmund_Grindal": "Archbishop of Canterbury 1575-1583. Refused to suppress prophesyings and was sequestered by Elizabeth I. Earlier served as Bishop of London and Archbishop of York.",
    "Edward_VI": "King of England 1547-1553. Son of Henry VIII and Jane Seymour. His minority reign saw significant Protestant reforms under the protectorates of Somerset and Northumberland.",
    "Elizabeth_I": "Queen of England 1558-1603. Daughter of Henry VIII and Anne Boleyn. Established the Elizabethan Settlement, creating a moderate Protestant church.",
    "Henry_VIII": "King of England 1509-1547. Broke with papal authority to annul his marriage to Catherine of Aragon and marry Anne Boleyn. Declared Supreme Head of the Church of England.",
    "Hugh_Latimer": "Bishop of Worcester and Protestant preacher. Resigned his see in 1539 over the Six Articles. Burned at the stake in Oxford 1555 during the Marian persecutions.",
    "John_Hooper": "Protestant reformer and Bishop of Gloucester. Advocate of further reform; executed for heresy in 1555.",
    "John_Foxe": "Protestant martyrologist. Author of Acts and Monuments (1563), documenting Protestant persecution. His work shaped English Protestant identity for generations.",
    "John_Jewel": "Bishop of Salisbury 1560-1571. Author of the Apology of the Church of England (1562), a foundational defense of the Elizabethan Settlement.",
    "John_Whitgift": "Archbishop of Canterbury 1583-1604. Enforced conformity against Puritans. Supported royal supremacy and episcopal authority.",
    "Mary_I": "Queen of England 1553-1558. Daughter of Henry VIII and Catherine of Aragon. Restored papal authority and Catholic practice; oversaw the Marian persecutions.",
    "Mary_Queen_of_Scots": "Queen of Scots (1542-1567) and Catholic claimant to the English throne. Executed in 1587 for treason.",
    "Miles_Coverdale": "Bible translator and bishop. Produced the first complete printed English Bible (1535); later Bishop of Exeter.",
    "Matthew_Parker": "Archbishop of Canterbury 1559-1575. First Elizabethan archbishop. Supervised the Bishops' Bible translation and defended the via media.",
    "Nicholas_Ridley": "Bishop of London. Protestant reformer who helped draft the 1552 Prayer Book. Burned at the stake in Oxford 1555 with Hugh Latimer.",
    "Pope_Clement_VII": "Pope from 1523 to 1534. His handling of Henry VIII's annulment request helped precipitate the Break with Rome.",
    "Reginald_Pole": "Cardinal and Archbishop of Canterbury 1556-1558. Papal legate who reconciled England to Rome under Mary I. Last Catholic Archbishop of Canterbury.",
    "Richard_Hooker": "Theologian and apologist. Author of Of the Laws of Ecclesiastical Polity, defending the Elizabethan church order against Puritan criticism.",
    "Robert_Parsons": "Jesuit priest. Co-leader with Edmund Campion of the 1580 Jesuit mission to England. Later directed seminary training from the continent.",
    "Stephen_Gardiner": "Bishop of Winchester. Conservative churchman who accepted royal supremacy but opposed Protestant doctrine. Lord Chancellor under Mary I.",
    "Thomas_Cartwright": "Puritan theologian and advocate for presbyterian church government. His Cambridge lectures sparked the Admonition Controversy.",
    "Thomas_Cranmer": "Archbishop of Canterbury 1533-1556. Principal architect of the English Reformation. Authored the Book of Common Prayer. Burned at the stake in Oxford 1556.",
    "Thomas_Cromwell": "Chief minister to Henry VIII 1532-1540. Orchestrated the dissolution of the monasteries and the administrative break with Rome. Executed 1540.",
    "Thomas_More": "Lord Chancellor 1529-1532. Humanist scholar and author of Utopia. Refused to accept royal supremacy. Executed 1535; later canonized.",
    "William_Cecil": "Lord Burghley. Principal Secretary and Lord Treasurer under Elizabeth I. Chief architect of Elizabethan religious and foreign policy.",
    "William_Tyndale": "Scholar and translator. Produced the first printed English New Testament (1526). His translations influenced later English Bibles. Executed for heresy 1536.",
}

# ─────────────────────────────────────────────────────────────────────────────
# EVENT DESCRIPTIONS (contextual, with dates)
# ─────────────────────────────────────────────────────────────────────────────
EVENT_DESCRIPTIONS = {
    "Act_of_Supremacy_Passage": "Parliamentary passage of the Act of Supremacy (1534), declaring Henry VIII Supreme Head of the Church of England.",
    "Annulment_Proceedings": "Henry VIII's efforts (1527-1533) to obtain papal annulment of his marriage to Catherine of Aragon. The papacy's refusal led to the Break with Rome.",
    "Articles_Promulgation": "Official promulgation of doctrinal articles defining the faith of the Church of England.",
    "Break_with_Rome": "The separation of the Church of England from papal authority (1532-1534), accomplished through parliamentary statutes including the Act of Supremacy.",
    "Doctrinal_Articles_Promulgation": "Promulgation of doctrinal articles establishing official teaching for the English church.",
    "Dissolution_of_the_Monasteries": "Crown seizure of monastic properties (1536-1541), dissolving religious houses and transferring their wealth to the crown.",
    "Elizabethan_Settlement": "Religious settlement of 1559 establishing a moderate Protestant Church of England through the Acts of Supremacy and Uniformity.",
    "Execution_of_Mary_Queen_of_Scots_1587": "Execution of Mary, Queen of Scots (1587) at Fotheringhay Castle for treason.",
    "Heresy_Persecutions": "Prosecutions and executions for heresy, especially during the Marian restoration (1555-1558).",
    "Jesuit_Mission_1580s": "Jesuit mission to England in the 1580s, led by Edmund Campion and Robert Parsons.",
    "Ketts_Rebellion_1549": "Kett's Rebellion (1549), popular uprising in Norfolk against enclosure and local grievances.",
    "Martin_Marprelate_Controversy_1588_1589": "Pamphlet war (1588-1589) attacking episcopal governance in the Church of England.",
    "Northern_Rebellion_1569": "Rising of the North (1569), Catholic rebellion led by northern earls.",
    "Oxford_Martyrs_1555_1556": "Executions of Latimer, Ridley (1555), and Cranmer (1556) at Oxford during the Marian persecutions.",
    "Parish_Bible_Installations": "Installation of authorized English Bibles in parish churches following royal injunctions.",
    "Marian_Persecutions": "Trials and executions of Protestants (1555-1558) during Mary I's reign. Nearly 300 people were burned for heresy.",
    "Oxford_Martyrdoms": "Executions of Protestant bishops Latimer, Ridley (1555), and Cranmer (1556) at Oxford during the Marian persecutions.",
    "Pilgrimage_of_Grace": "Northern uprising (1536-1537) protesting the dissolution of the monasteries and religious changes. Suppressed by royal forces.",
    "Pilgrimage_of_Grace_1536": "Northern rebellion (1536) against monastic dissolution and royal religious policy.",
    "Prayer_Book_Reform": "Introduction and revision of the English Book of Common Prayer (1549, 1552).",
    "Reconciliation_with_Rome": "Reconciliation of England with the papacy under Mary I (1554-1555).",
    "Recusancy_Fines_Regime": "System of fines and penalties for nonattendance at Church of England services.",
    "Regnans_in_Excelsis_1570": "Papal bull (1570) excommunicating Elizabeth I and releasing subjects from obedience.",
    "Seminary_Priests_Mission_1580s": "Mission of seminary-trained priests to England in the 1580s to sustain Catholic communities.",
    "Settlement_Passage": "Parliamentary passage of the 1559 Acts of Supremacy and Uniformity establishing the Elizabethan Settlement.",
    "Spanish_Armada_1588": "Spanish Armada campaign (1588) against England, defeated by English forces and weather.",
    "Vestiarian_Controversy_1566": "Dispute (1566) over clerical vestments, exposing tensions between conformists and Puritans.",
    "Western_Rebellion_1549": "Prayer Book Rebellion (Western Rising) in Devon and Cornwall against the 1549 Prayer Book.",
    "Wyatts_Rebellion_1554": "Wyatt's Rebellion (1554), uprising against Mary I's proposed marriage to Philip of Spain.",
    "Prayer_Book_Rebellion": "Western Rising (1549) in Devon and Cornwall against the imposition of the English-language Prayer Book.",
    "Regnans_in_Excelsis": "Papal bull (1570) excommunicating Elizabeth I and releasing her subjects from allegiance.",
    "Rising_of_the_North": "Rebellion (1569) by northern earls seeking to restore Catholicism and free Mary, Queen of Scots.",
    "Vestiarian_Controversy": "Dispute (1560s) over required clerical vestments, exposing tensions between conformists and Puritans.",
}

# ─────────────────────────────────────────────────────────────────────────────
# TEXT DESCRIPTIONS
# ─────────────────────────────────────────────────────────────────────────────
TEXT_DESCRIPTIONS = {
    "Act_of_Supremacy_1534": "Parliamentary statute declaring the monarch Supreme Head of the Church of England, severing ties with papal Rome.",
    "Act_of_Supremacy_1559": "Elizabethan statute re-establishing royal supremacy over the Church of England. Styled the monarch as Supreme Governor.",
    "Act_of_Uniformity_1559": "Elizabethan statute requiring the use of the Book of Common Prayer in all churches.",
    "Acts_and_Monuments_1563": "John Foxe's martyrology documenting Protestant persecution, popularly known as the 'Book of Martyrs.'",
    "Apology_of_the_Church_of_England": "John Jewel's defense (1562) of the Elizabethan church against Roman Catholic criticism.",
    "Bishops_Bible": "English translation (1568) authorized by Archbishop Parker for use in churches.",
    "Bishops_Bible_1568": "English Bible authorized by the bishops under Archbishop Matthew Parker (1568).",
    "Bishops_Book_1537": "Bishops' Book (The Institution of a Christian Man), doctrinal manual issued in 1537.",
    "Book_of_Common_Prayer_1549": "First English-language liturgical book, compiled by Thomas Cranmer.",
    "Book_of_Common_Prayer_1552": "Revised Prayer Book with more Protestant character, replacing the 1549 version.",
    "Book_of_Common_Prayer_1559": "Elizabethan Prayer Book combining elements of the 1549 and 1552 versions.",
    "Book_of_Homilies": "Official collection of sermons prescribed for use when clergy could not preach.",
    "Book_of_Homilies_1547": "First Book of Homilies (1547), authorized sermons for parish instruction under Edward VI.",
    "Book_of_Homilies_1571": "Second Book of Homilies (1571), authorized sermons reaffirming Elizabethan doctrine.",
    "Catholic_Restoration_Decrees": "Marian-era decrees restoring papal jurisdiction and Catholic worship in England.",
    "Chantries_Act_1547": "Act dissolving chantries and guilds, transferring endowments to the Crown (1547).",
    "Coverdale_Bible": "First complete printed English Bible (1535), translated by Miles Coverdale.",
    "Cranmer_Annulment_Decree": "Archiepiscopal decree (1533) declaring Henry VIII's marriage to Catherine of Aragon invalid.",
    "Forty-Two_Articles_1553": "Forty-Two Articles of Religion (1553), doctrinal statement under Edward VI.",
    "Forty_Two_Articles_1553": "Forty-Two Articles of Religion (1553), doctrinal statement under Edward VI.",
    "Geneva_Bible_1560": "Geneva Bible (1560), influential English translation with Calvinist annotations.",
    "Great_Bible_1539": "Great Bible (1539), authorized for public reading in every parish church.",
    "Heresy_Acts": "Statutes defining heresy and penalties in Tudor England.",
    "Injunctions_1547": "Royal Injunctions of 1547, reform directives issued at the start of Edward VI's reign.",
    "Douay_Rheims_Bible": "Catholic English translation produced at continental seminaries (NT 1582, OT 1609-1610).",
    "Geneva_Bible": "Protestant English translation (1560) with Calvinist annotations; widely popular.",
    "Great_Bible": "Authorized English Bible (1539) required in every parish church.",
    "Laws_of_Ecclesiastical_Polity": "Richard Hooker's theological defense of the Elizabethan church order.",
    "Of_the_Laws_of_Ecclesiastical_Polity": "Richard Hooker's treatise defending the theology and polity of the Elizabethan church.",
    "Pole_Reconciliation_Decrees": "Legatine decrees under Cardinal Pole reconciling England to Rome (1554-1555).",
    "Rheims_New_Testament_1582": "Catholic English New Testament published at Rheims in 1582.",
    "Royal_Injunctions_1536": "Henrician Injunctions of 1536 ordering reforms and visitation in the English church.",
    "Royal_Injunctions_1538": "Henrician Injunctions of 1538 requiring Bible provision and regulating images and relics.",
    "Six_Articles_1539": "Act of Six Articles (1539), reaffirming traditional doctrine and sacramental practice.",
    "Ten_Articles_1536": "Ten Articles (1536), early Henrician doctrinal statement blending reform and tradition.",
    "Valor_Ecclesiasticus_1535": "Crown survey of ecclesiastical wealth commissioned by Henry VIII in 1535.",
    "Six_Articles": "Conservative doctrinal statute (1539) reaffirming traditional practices.",
    "Ten_Articles": "Early Henrician doctrinal statement (1536) combining Catholic and Protestant elements.",
    "Thirty_Nine_Articles": "Doctrinal formulary (1563/1571) defining the faith of the Church of England.",
    "Tyndale_Bible": "William Tyndale's English New Testament (1526) and Pentateuch (1530), basis for later translations.",
}

# ─────────────────────────────────────────────────────────────────────────────
# INSTITUTION DEFINITIONS
# ─────────────────────────────────────────────────────────────────────────────
INSTITUTION_DEFINITIONS = {
    "Church_of_England": "National church of England, separated from papal authority and under royal supremacy since the 1530s.",
    "Convocation": "Provincial assembly of clergy of the Church of England, meeting in Canterbury and York.",
    "Court_of_High_Commission": "Ecclesiastical tribunal enforcing religious uniformity under royal authority.",
    "House_of_Commons": "Lower chamber of the English Parliament, representing boroughs and shires.",
    "House_of_Lords": "Upper chamber of Parliament comprising bishops and temporal peers.",
    "Parliament": "Bicameral legislature of England consisting of the House of Lords and House of Commons.",
    "Privy_Council": "Principal advisory body to the monarch, overseeing administration and policy.",
    "Society_of_Jesus": "Jesuit order: Catholic religious society founded by Ignatius of Loyola, active in missions and education.",
    "Star_Chamber": "Prerogative court handling cases without jury, used for censorship and political control.",
    "Tudor_Crown": "Royal government of the Tudor dynasty; executive authority and administration.",
}

# ─────────────────────────────────────────────────────────────────────────────
# MOVEMENT DEFINITIONS
# ─────────────────────────────────────────────────────────────────────────────
MOVEMENT_DEFINITIONS = {
    "Anglicanism": "Tradition of the Church of England and its communion, balancing Catholic and Protestant elements.",
    "English_Recusancy": "Refusal to attend Church of England services; Catholic resistance to Protestant establishment.",
    "Puritanism": "Movement within the Church of England seeking further Protestant reform beyond the Elizabethan Settlement.",
    "Separatism": "Movement withdrawing from the established church to form independent congregations.",
}


def normalize_slug(slug: str) -> str:
    """Normalize slug for matching."""
    return slug.replace("-", "_").replace(" ", "_")


def get_definition_for_node(node: dict) -> tuple[str | None, str | None, bool]:
    """
    Return (description, definition, is_generic) for a node based on its label and slug.
    Returns None for fields that should not be changed.
    """
    slug = normalize_slug(node.get("slug", ""))
    label = node.get("label", "")
    current_desc = node.get("description", "")
    
    # Skip nodes that already have good descriptions (not auto-generated or cluster stubs)
    is_stub = "Auto-generated stub" in current_desc or current_desc.endswith("cluster")
    
    # Place nodes: always update to be generic
    if label == "Place":
        if slug in PLACE_DEFINITIONS:
            return PLACE_DEFINITIONS[slug], None, True
        # Generate generic definition from name
        name = node.get("name", slug.replace("_", " "))
        return f"Geographic location: {name}.", None, True
    
    # Person nodes
    if label == "Person":
        if slug in PERSON_DESCRIPTIONS:
            return PERSON_DESCRIPTIONS[slug], None, False
        if is_stub:
            name = node.get("name", slug.replace("_", " "))
            return f"Historical figure associated with the English Reformation period.", None, False
        return None, None, False
    
    # Event nodes
    if label == "Event":
        if slug in EVENT_DESCRIPTIONS:
            return EVENT_DESCRIPTIONS[slug], None, False
        if is_stub:
            name = node.get("name", slug.replace("_", " "))
            return f"Event in the history of the English Reformation.", None, False
        return None, None, False
    
    # Text nodes
    if label == "Text":
        if slug in TEXT_DESCRIPTIONS:
            return TEXT_DESCRIPTIONS[slug], None, False
        if is_stub:
            return f"Historical text or document from the English Reformation period.", None, False
        return None, None, False
    
    # Institution nodes
    if label == "Institution":
        if slug in INSTITUTION_DEFINITIONS:
            return None, INSTITUTION_DEFINITIONS[slug], False
        if is_stub:
            name = node.get("name", slug.replace("_", " "))
            return None, f"Institution active during the English Reformation period.", False
        return None, None, False
    
    # Movement nodes
    if label == "Movement":
        if slug in MOVEMENT_DEFINITIONS:
            return None, MOVEMENT_DEFINITIONS[slug], False
        if is_stub:
            return None, f"Religious or political movement of the Reformation era.", False
        return None, None, False
    
    # Idea nodes: prefer definition
    if label == "Idea":
        if slug in IDEA_DEFINITIONS:
            defn = IDEA_DEFINITIONS[slug]
            return defn, defn, False  # Set both for ideas
        if is_stub:
            name = node.get("name", slug.replace("_", " "))
            # Generate a reasonable definition from the name
            defn = f"Concept related to the English Reformation: {name.lower()}."
            return defn, defn, False
        return None, None, False
    
    return None, None, False


def update_nodes_file(filepath: Path, dry_run: bool = False) -> int:
    """Update all nodes in a JSON file. Returns count of updated nodes."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    nodes = data.get("nodes", [])
    updated_count = 0
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    
    for node in nodes:
        desc, defn, is_generic = get_definition_for_node(node)
        
        changed = False
        
        if desc is not None and node.get("description") != desc:
            node["description"] = desc
            changed = True
        
        if defn is not None and node.get("definition") != defn:
            node["definition"] = defn
            changed = True
        
        if is_generic and not node.get("is_generic"):
            node["is_generic"] = True
            changed = True
        
        if changed:
            node["modified_at"] = now
            node["modified_by"] = "curator:systematic_definitions_update"
            updated_count += 1
    
    if not dry_run and updated_count > 0:
        # Update metadata
        data["_meta"]["last_updated"] = now
        data["_meta"]["definitions_update_notes"] = f"Systematic update of {updated_count} node descriptions/definitions per registry guidelines"
        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")
    
    return updated_count


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Update node descriptions/definitions systematically")
    parser.add_argument("--cluster", default="English_Reformation", help="Cluster name")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be changed without modifying files")
    args = parser.parse_args()
    
    # Find the nodes file
    base = Path(__file__).resolve().parent.parent.parent
    nodes_file = base / "data" / "Nodes" / f"nodes.{args.cluster}.json"
    
    if not nodes_file.exists():
        print(f"Error: {nodes_file} not found")
        sys.exit(1)
    
    print(f"Processing {nodes_file}...")
    count = update_nodes_file(nodes_file, dry_run=args.dry_run)
    
    if args.dry_run:
        print(f"Would update {count} nodes (dry run)")
    else:
        print(f"Updated {count} nodes")


if __name__ == "__main__":
    main()
