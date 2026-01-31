#!/usr/bin/env python3
"""
Expand the English Reformation cluster with missing nodes and comprehensive edges.

This script adds:
- Missing key historical figures (Wolsey, Gardiner, Bonner, Fisher, etc.)
- Missing texts (Tyndale's NT, Coverdale Bible, etc.)
- Missing events (executions, plots, trials)
- Missing institutions and places
- Comprehensive relationships between all nodes

Usage:
    python scripts/admin/expand_english_reformation.py
"""

import json
from pathlib import Path
from datetime import datetime, timezone

# ============================================================================
# NEW NODES TO ADD
# ============================================================================

NEW_PERSONS = [
    {
        "slug": "Thomas_Wolsey",
        "label": "Person",
        "name": "Thomas Wolsey",
        "description": "Cardinal and Lord Chancellor (c. 1473–1530) who dominated English politics under Henry VIII until his failure to secure the royal annulment led to his downfall and death.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Stephen_Gardiner",
        "label": "Person",
        "name": "Stephen Gardiner",
        "description": "Bishop of Winchester (c. 1483–1555) who served Henry VIII as diplomat, opposed Protestant reforms under Edward VI, and became Lord Chancellor under Mary I, enforcing Catholic restoration.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Edmund_Bonner",
        "label": "Person",
        "name": "Edmund Bonner",
        "description": "Bishop of London (c. 1500–1569), known as 'Bloody Bonner,' who conducted heresy trials and ordered numerous Protestant burnings during the Marian persecutions.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "John_Fisher",
        "label": "Person",
        "name": "John Fisher",
        "description": "Bishop of Rochester (1469–1535) and humanist scholar who defended Catherine of Aragon and papal supremacy, executed for refusing to accept the Act of Supremacy.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Lady_Jane_Grey",
        "label": "Person",
        "name": "Lady Jane Grey",
        "description": "The 'Nine Days Queen' (1537–1554), great-granddaughter of Henry VII, briefly proclaimed queen in 1553 before Mary I's accession; executed for treason.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "John_Dudley_Northumberland",
        "label": "Person",
        "name": "John Dudley, Duke of Northumberland",
        "description": "Lord President of the Council (1504–1553) who dominated Edward VI's government from 1550, promoted Protestant reforms, and attempted to place Lady Jane Grey on the throne.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Edward_Seymour_Somerset",
        "label": "Person",
        "name": "Edward Seymour, Duke of Somerset",
        "description": "Lord Protector (c. 1500–1552) during Edward VI's minority who oversaw initial Protestant reforms including the first Book of Common Prayer.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Martin_Bucer",
        "label": "Person",
        "name": "Martin Bucer",
        "description": "Continental reformer (1491–1551) from Strasbourg who came to England in 1549, influenced Cranmer's theology, and was Regius Professor of Divinity at Cambridge.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Peter_Martyr_Vermigli",
        "label": "Person",
        "name": "Peter Martyr Vermigli",
        "description": "Italian Protestant reformer (1499–1562) who served as Regius Professor of Divinity at Oxford under Edward VI and influenced English eucharistic theology.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "John_Knox",
        "label": "Person",
        "name": "John Knox",
        "description": "Scottish reformer (c. 1514–1572) who served as royal chaplain under Edward VI, later led the Scottish Reformation, and influenced English Puritanism through his writings.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Philip_II_of_Spain",
        "label": "Person",
        "name": "Philip II of Spain",
        "description": "King of Spain (1527–1598) who married Mary I in 1554, supported Catholic restoration in England, and later launched the Spanish Armada against Elizabeth I.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Jane_Seymour",
        "label": "Person",
        "name": "Jane Seymour",
        "description": "Third queen consort of Henry VIII (c. 1508–1537), mother of Edward VI, whose family rose to prominence during the Protestant reforms.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Thomas_Wyatt_the_Younger",
        "label": "Person",
        "name": "Thomas Wyatt the Younger",
        "description": "English rebel (c. 1521–1554) who led Wyatt's Rebellion in 1554 against Mary I's Spanish marriage; executed for treason.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Robert_Aske",
        "label": "Person",
        "name": "Robert Aske",
        "description": "Yorkshire lawyer (c. 1500–1537) who led the Pilgrimage of Grace in 1536, the largest rebellion against Henry VIII's religious policies; executed for treason.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "William_Allen",
        "label": "Person",
        "name": "William Allen",
        "description": "English Catholic cardinal (1532–1594) who founded the English College at Douai to train missionary priests for the reconversion of England.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "John_Jewel",
        "label": "Person",
        "name": "John Jewel",
        "description": "Bishop of Salisbury (1522–1571) whose Apology of the Church of England (1562) became a foundational defense of the Elizabethan settlement.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Thomas_Cartwright",
        "label": "Person",
        "name": "Thomas Cartwright",
        "description": "Cambridge theologian (1535–1603) and leading Presbyterian who challenged the episcopal structure of the Church of England.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Walter_Travers",
        "label": "Person",
        "name": "Walter Travers",
        "description": "Puritan theologian (c. 1548–1635) who debated Richard Hooker at the Temple Church and advocated Presbyterian church government.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Robert_Browne",
        "label": "Person",
        "name": "Robert Browne",
        "description": "English Separatist (c. 1550–1633) whose writings advocating congregational independence influenced later Separatist and Congregationalist movements.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Henry_Barrow",
        "label": "Person",
        "name": "Henry Barrow",
        "description": "Separatist leader (c. 1550–1593) executed for sedition, whose writings advocated complete separation from the Church of England.",
        "cluster": "English_Reformation"
    },
]

NEW_TEXTS = [
    {
        "slug": "Tyndale_New_Testament_1526",
        "label": "Text",
        "name": "Tyndale's New Testament (1526)",
        "description": "First printed English New Testament, translated by William Tyndale from Greek and printed in Worms; formed the basis of all subsequent English Bible translations.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Coverdale_Bible_1535",
        "label": "Text",
        "name": "Coverdale Bible (1535)",
        "description": "First complete printed English Bible, translated by Miles Coverdale; dedicated to Henry VIII and Anne Boleyn.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Matthew_Bible_1537",
        "label": "Text",
        "name": "Matthew Bible (1537)",
        "description": "English Bible combining Tyndale's and Coverdale's work, edited by John Rogers under the pseudonym Thomas Matthew; the first English Bible officially authorized for public use.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Defense_of_the_Seven_Sacraments_1521",
        "label": "Text",
        "name": "Defense of the Seven Sacraments (1521)",
        "description": "Henry VIII's theological treatise against Martin Luther, for which Pope Leo X granted him the title 'Defender of the Faith.'",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Kings_Book_1543",
        "label": "Text",
        "name": "The King's Book (1543)",
        "description": "A Necessary Doctrine and Erudition for Any Christian Man, a conservative doctrinal formulary issued under Henry VIII that modified the Bishops' Book.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Apology_of_the_Church_of_England_1562",
        "label": "Text",
        "name": "Apology of the Church of England (1562)",
        "description": "John Jewel's Latin treatise defending the Church of England against Catholic criticism, foundational for Anglican ecclesiology.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Admonition_to_Parliament_1572",
        "label": "Text",
        "name": "Admonition to the Parliament (1572)",
        "description": "Puritan manifesto by John Field and Thomas Wilcox calling for Presbyterian reform of the Church of England.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Book_of_Martyrs_1563",
        "label": "Text",
        "name": "Foxe's Book of Martyrs (1563)",
        "description": "Popular name for John Foxe's Acts and Monuments; the most influential English Protestant text after the Bible.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "First_Blast_of_the_Trumpet_1558",
        "label": "Text",
        "name": "First Blast of the Trumpet Against the Monstrous Regiment of Women (1558)",
        "description": "John Knox's polemic against female rulers, written against Mary I but creating diplomatic difficulties with Elizabeth I.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Recusancy_Acts",
        "label": "Text",
        "name": "Recusancy Acts",
        "description": "Series of parliamentary statutes (1581, 1587, 1593) imposing fines and penalties on Catholics who refused to attend Church of England services.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Act_Against_Jesuits_1585",
        "label": "Text",
        "name": "Act Against Jesuits and Seminary Priests (1585)",
        "description": "Elizabethan statute making it treason for Catholic priests ordained abroad to enter England.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Bond_of_Association_1584",
        "label": "Text",
        "name": "Bond of Association (1584)",
        "description": "Document pledging signatories to execute anyone who attempted to assassinate Elizabeth I or claim the throne, aimed at Mary Queen of Scots.",
        "cluster": "English_Reformation"
    },
]

NEW_EVENTS = [
    {
        "slug": "Execution_of_Anne_Boleyn_1536",
        "label": "Event",
        "name": "Execution of Anne Boleyn (1536)",
        "description": "The beheading of Queen Anne Boleyn on May 19, 1536, on charges of adultery and treason, enabling Henry VIII to marry Jane Seymour.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Execution_of_Thomas_More_1535",
        "label": "Event",
        "name": "Execution of Thomas More (1535)",
        "description": "The beheading of Sir Thomas More on July 6, 1535, for refusing to acknowledge Henry VIII as Supreme Head of the Church of England.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Execution_of_John_Fisher_1535",
        "label": "Event",
        "name": "Execution of John Fisher (1535)",
        "description": "The beheading of Bishop John Fisher on June 22, 1535, for denying royal supremacy; he had been made cardinal by the Pope two weeks earlier.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Burning_of_William_Tyndale_1536",
        "label": "Event",
        "name": "Burning of William Tyndale (1536)",
        "description": "The execution of Bible translator William Tyndale by strangulation and burning at Vilvoorde near Brussels on October 6, 1536.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Lady_Jane_Grey_Reign_1553",
        "label": "Event",
        "name": "Lady Jane Grey's Reign (1553)",
        "description": "The nine-day reign of Lady Jane Grey (July 10-19, 1553), proclaimed queen by Northumberland before Mary I's successful claim to the throne.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Babington_Plot_1586",
        "label": "Event",
        "name": "Babington Plot (1586)",
        "description": "Catholic conspiracy to assassinate Elizabeth I and place Mary Queen of Scots on the throne, whose discovery led to Mary's trial and execution.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Throckmorton_Plot_1583",
        "label": "Event",
        "name": "Throckmorton Plot (1583)",
        "description": "Catholic conspiracy involving Francis Throckmorton to invade England with Spanish support and place Mary Queen of Scots on the throne.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Ridolfi_Plot_1571",
        "label": "Event",
        "name": "Ridolfi Plot (1571)",
        "description": "Catholic conspiracy organized by Roberto Ridolfi to replace Elizabeth I with Mary Queen of Scots, involving the Duke of Norfolk.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Trial_of_Mary_Queen_of_Scots_1586",
        "label": "Event",
        "name": "Trial of Mary Queen of Scots (1586)",
        "description": "The trial of Mary Queen of Scots at Fotheringhay Castle for complicity in the Babington Plot, resulting in her conviction and death sentence.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Fall_of_Wolsey_1529",
        "label": "Event",
        "name": "Fall of Wolsey (1529)",
        "description": "Cardinal Wolsey's dismissal as Lord Chancellor in October 1529 after failing to secure Henry VIII's annulment; died en route to trial in 1530.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Submission_of_the_Clergy_1532",
        "label": "Event",
        "name": "Submission of the Clergy (1532)",
        "description": "The English clergy's surrender of legislative independence to the Crown, a crucial step toward royal supremacy over the church.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Convocation_of_1563",
        "label": "Event",
        "name": "Convocation of 1563",
        "description": "Meeting of the Canterbury Convocation that approved the Thirty-Nine Articles and narrowly rejected further Puritan reforms.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Prophesyings_Controversy_1576",
        "label": "Event",
        "name": "Prophesyings Controversy (1576)",
        "description": "Dispute over clerical training exercises ('prophesyings') between Archbishop Grindal, who supported them, and Elizabeth I, who ordered their suppression.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Execution_of_Edmund_Campion_1581",
        "label": "Event",
        "name": "Execution of Edmund Campion (1581)",
        "description": "The hanging, drawing, and quartering of Jesuit priest Edmund Campion at Tyburn on December 1, 1581, for treason.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Act_of_Succession_1534",
        "label": "Event",
        "name": "Act of Succession (1534)",
        "description": "Parliamentary act establishing the succession through Anne Boleyn's children and requiring an oath accepting the king's supremacy.",
        "cluster": "English_Reformation"
    },
]

NEW_INSTITUTIONS = [
    {
        "slug": "Convocation_of_Canterbury",
        "label": "Institution",
        "name": "Convocation of Canterbury",
        "description": "The assembly of clergy of the province of Canterbury, the senior provincial synod of the Church of England with legislative powers over church matters.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Council_of_the_North",
        "label": "Institution",
        "name": "Council of the North",
        "description": "Administrative body based in York exercising royal authority in northern England, strengthened after the Pilgrimage of Grace.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "English_College_Rome",
        "label": "Institution",
        "name": "English College Rome",
        "description": "Seminary in Rome (founded 1579) training Catholic priests for the English mission, complementing Douai-Rheims.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Doctors_Commons",
        "label": "Institution",
        "name": "Doctors' Commons",
        "description": "London college of civil and canon lawyers who handled ecclesiastical and admiralty cases, including annulment proceedings.",
        "cluster": "English_Reformation"
    },
]

NEW_PLACES = [
    {
        "slug": "Smithfield",
        "label": "Place",
        "name": "Smithfield",
        "description": "Site in London where numerous Protestant martyrs were burned during the Marian persecutions, becoming a symbol of Protestant suffering.",
        "is_generic": True,
        "cluster": "English_Reformation"
    },
    {
        "slug": "Tower_of_London",
        "label": "Place",
        "name": "Tower of London",
        "description": "Royal fortress and prison where many figures of the Reformation were held and executed, including More, Fisher, and Anne Boleyn.",
        "is_generic": True,
        "cluster": "English_Reformation"
    },
    {
        "slug": "Fotheringhay",
        "label": "Place",
        "name": "Fotheringhay",
        "description": "Castle in Northamptonshire where Mary Queen of Scots was tried and executed in 1586-1587.",
        "is_generic": True,
        "cluster": "English_Reformation"
    },
    {
        "slug": "Wittenberg",
        "label": "Place",
        "name": "Wittenberg",
        "description": "German university town where Martin Luther initiated the Protestant Reformation, influencing English reformers through theological exchanges.",
        "is_generic": True,
        "cluster": "English_Reformation"
    },
    {
        "slug": "Geneva",
        "label": "Place",
        "name": "Geneva",
        "description": "Swiss city under John Calvin's influence where Marian exiles produced the Geneva Bible and absorbed Reformed theology.",
        "is_generic": True,
        "cluster": "English_Reformation"
    },
    {
        "slug": "Antwerp",
        "label": "Place",
        "name": "Antwerp",
        "description": "Flemish city where Tyndale printed his New Testament and other Protestant works were published for smuggling into England.",
        "is_generic": True,
        "cluster": "English_Reformation"
    },
    {
        "slug": "Strasbourg",
        "label": "Place",
        "name": "Strasbourg",
        "description": "Imperial city where Martin Bucer led reform and English exiles including Coverdale sought refuge during Mary's reign.",
        "is_generic": True,
        "cluster": "English_Reformation"
    },
]

NEW_MOVEMENTS = [
    {
        "slug": "Marian_Exile",
        "label": "Movement",
        "name": "Marian Exile",
        "definition": "The flight of approximately 800 English Protestants to continental Europe during Mary I's reign (1553-1558), many returning with more radical Reformed ideas.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Counter_Reformation_in_England",
        "label": "Movement",
        "name": "Counter-Reformation in England",
        "definition": "Catholic efforts to reverse the English Reformation through diplomatic pressure, seminary priests, Jesuit missions, and plots against Elizabeth I.",
        "cluster": "English_Reformation"
    },
    {
        "slug": "Erastianism",
        "label": "Movement",
        "name": "Erastianism",
        "definition": "The doctrine that the state has authority over the church in ecclesiastical matters, a key principle underlying royal supremacy.",
        "cluster": "English_Reformation"
    },
]

# ============================================================================
# COMPREHENSIVE RELATIONSHIPS
# ============================================================================

# Format: (start_slug, type, end_slug, description)

NEW_RELATIONSHIPS = [
    # === THOMAS WOLSEY ===
    ("Thomas_Wolsey", "SERVES", "Henry_VIII", 
     "Thomas Wolsey served as Lord Chancellor and chief minister to Henry VIII from 1515 to 1529."),
    ("Thomas_Wolsey", "FAILS_TO_OBTAIN", "Annulment_Proceedings", 
     "Thomas Wolsey failed to secure papal approval for Henry VIII's annulment, leading to his downfall."),
    ("Thomas_Wolsey", "PRECEDES", "Thomas_Cromwell", 
     "Thomas Wolsey's fall from power opened the way for Thomas Cromwell's rise."),
    ("Thomas_Wolsey", "NEGOTIATES_WITH", "Pope_Clement_VII", 
     "Thomas Wolsey negotiated with Pope Clement VII seeking the annulment."),
    ("Fall_of_Wolsey_1529", "REMOVES", "Thomas_Wolsey", 
     "The Fall of Wolsey removed the cardinal from power in 1529."),
    
    # === STEPHEN GARDINER ===
    ("Stephen_Gardiner", "OPPOSES", "Thomas_Cranmer", 
     "Stephen Gardiner opposed Cranmer's Protestant reforms throughout his career."),
    ("Stephen_Gardiner", "SERVES", "Henry_VIII", 
     "Stephen Gardiner served Henry VIII as diplomat and secretary."),
    ("Stephen_Gardiner", "ENFORCES", "Catholic_Restoration", 
     "Stephen Gardiner enforced Catholic restoration as Lord Chancellor under Mary I."),
    ("Stephen_Gardiner", "DISPUTES", "Protestant_Doctrine_in_England", 
     "Stephen Gardiner disputed Protestant doctrinal changes."),
    ("Mary_I", "APPOINTS", "Stephen_Gardiner", 
     "Mary I appointed Stephen Gardiner as Lord Chancellor."),
    
    # === EDMUND BONNER ===
    ("Edmund_Bonner", "CONDUCTS", "Heresy_Persecutions", 
     "Edmund Bonner conducted heresy trials as Bishop of London, ordering numerous burnings."),
    ("Edmund_Bonner", "SERVES", "Mary_I", 
     "Edmund Bonner served Mary I as a chief instrument of persecution."),
    ("Edmund_Bonner", "PERSECUTES", "Protestant_Doctrine_in_England", 
     "Edmund Bonner persecuted adherents of Protestant doctrine."),
    ("Marian_Episcopate", "INCLUDES", "Edmund_Bonner", 
     "The Marian Episcopate included Edmund Bonner as Bishop of London."),
    
    # === JOHN FISHER ===
    ("John_Fisher", "DEFENDS", "Catherine_of_Aragon", 
     "John Fisher defended Catherine of Aragon's marriage at the annulment hearings."),
    ("John_Fisher", "DEFENDS", "Papal_Supremacy", 
     "John Fisher defended papal supremacy against royal claims."),
    ("John_Fisher", "OPPOSES", "Royal_Supremacy", 
     "John Fisher opposed royal supremacy over the church."),
    ("Execution_of_John_Fisher_1535", "KILLS", "John_Fisher", 
     "The execution of John Fisher in 1535 killed the Bishop of Rochester."),
    ("John_Fisher", "DIES_IN", "Execution_of_John_Fisher_1535", 
     "John Fisher died in his execution on June 22, 1535."),
    ("Henry_VIII", "EXECUTES", "John_Fisher", 
     "Henry VIII ordered John Fisher's execution for denying royal supremacy."),
    
    # === LADY JANE GREY ===
    ("Lady_Jane_Grey", "PROCLAIMED_IN", "Lady_Jane_Grey_Reign_1553", 
     "Lady Jane Grey was proclaimed queen during her brief nine-day reign."),
    ("John_Dudley_Northumberland", "PROMOTES", "Lady_Jane_Grey", 
     "John Dudley promoted Lady Jane Grey's claim to prevent Catholic Mary's succession."),
    ("Lady_Jane_Grey", "OPPOSES", "Mary_I", 
     "Lady Jane Grey's succession claim opposed Mary I's rightful inheritance."),
    ("Mary_I", "EXECUTES", "Lady_Jane_Grey", 
     "Mary I executed Lady Jane Grey in 1554 after Wyatt's Rebellion."),
    ("Lady_Jane_Grey", "ENDORSES", "Protestant_Doctrine_in_England", 
     "Lady Jane Grey was a committed Protestant."),
    
    # === JOHN DUDLEY (NORTHUMBERLAND) ===
    ("John_Dudley_Northumberland", "LEADS", "Lord_Protectorate", 
     "John Dudley led the government as Lord President of the Council from 1550."),
    ("John_Dudley_Northumberland", "SUCCEEDS", "Edward_Seymour_Somerset", 
     "John Dudley succeeded Edward Seymour as the dominant figure in Edward VI's government."),
    ("John_Dudley_Northumberland", "PROMOTES", "Protestant_Doctrine_in_England", 
     "John Dudley promoted Protestant reforms during Edward VI's reign."),
    ("John_Dudley_Northumberland", "ORGANIZES", "Lady_Jane_Grey_Reign_1553", 
     "John Dudley organized the attempt to place Lady Jane Grey on the throne."),
    ("Mary_I", "EXECUTES", "John_Dudley_Northumberland", 
     "Mary I executed John Dudley for treason in August 1553."),
    
    # === EDWARD SEYMOUR (SOMERSET) ===
    ("Edward_Seymour_Somerset", "LEADS", "Lord_Protectorate", 
     "Edward Seymour served as Lord Protector during Edward VI's minority."),
    ("Edward_Seymour_Somerset", "PROMOTES", "Book_of_Common_Prayer_1549", 
     "Edward Seymour's government promoted the first Book of Common Prayer."),
    ("Edward_Seymour_Somerset", "SUPPRESSES", "Western_Rebellion_1549", 
     "Edward Seymour suppressed the Western Rebellion against the Prayer Book."),
    ("Edward_Seymour_Somerset", "BROTHER_OF", "Jane_Seymour", 
     "Edward Seymour was the brother of Queen Jane Seymour."),
    
    # === MARTIN BUCER ===
    ("Martin_Bucer", "TEACHES_AT", "University_of_Cambridge", 
     "Martin Bucer taught as Regius Professor of Divinity at Cambridge."),
    ("Martin_Bucer", "INFLUENCES", "Thomas_Cranmer", 
     "Martin Bucer influenced Thomas Cranmer's eucharistic theology."),
    ("Martin_Bucer", "ADVISES", "Book_of_Common_Prayer_1552", 
     "Martin Bucer's critiques influenced the revision of the Prayer Book in 1552."),
    ("Martin_Bucer", "COMES_FROM", "Strasbourg", 
     "Martin Bucer came from Strasbourg where he had led reform."),
    
    # === PETER MARTYR VERMIGLI ===
    ("Peter_Martyr_Vermigli", "TEACHES_AT", "University_of_Oxford", 
     "Peter Martyr Vermigli served as Regius Professor of Divinity at Oxford."),
    ("Peter_Martyr_Vermigli", "INFLUENCES", "Protestant_Doctrine_in_England", 
     "Peter Martyr Vermigli influenced English Protestant theology."),
    ("Peter_Martyr_Vermigli", "DISPUTES", "Stephen_Gardiner", 
     "Peter Martyr Vermigli disputed with Stephen Gardiner over eucharistic doctrine."),
    
    # === JOHN KNOX ===
    ("John_Knox", "WRITES", "First_Blast_of_the_Trumpet_1558", 
     "John Knox wrote The First Blast of the Trumpet Against the Monstrous Regiment of Women."),
    ("John_Knox", "SERVES", "Edward_VI", 
     "John Knox served as royal chaplain under Edward VI."),
    ("John_Knox", "INFLUENCES", "Puritan_Movement", 
     "John Knox's writings influenced the English Puritan movement."),
    ("John_Knox", "FLEES_TO", "Geneva", 
     "John Knox fled to Geneva during Mary I's reign."),
    ("First_Blast_of_the_Trumpet_1558", "OFFENDS", "Elizabeth_I", 
     "Knox's First Blast offended Elizabeth I despite being aimed at Mary I."),
    
    # === PHILIP II OF SPAIN ===
    # marriage modeled as an Event + participation edges; see MARRIAGES below
    ("Philip_II_of_Spain", "SUPPORTS", "Catholic_Restoration", 
     "Philip II supported Catholic restoration during Mary I's reign."),
    ("Philip_II_of_Spain", "LAUNCHES", "Spanish_Armada_1588", 
     "Philip II launched the Spanish Armada against England in 1588."),
    ("Philip_II_of_Spain", "OPPOSES", "Elizabeth_I", 
     "Philip II opposed Elizabeth I after her rejection of his marriage proposal."),
    ("Wyatts_Rebellion_1554", "OPPOSES", "Philip_II_of_Spain", 
     "Wyatt's Rebellion opposed Mary I's marriage to Philip II."),
    
    # === JANE SEYMOUR ===
    # marriage modeled as an Event + participation edges; see MARRIAGES below
    ("Jane_Seymour", "MOTHER_OF", "Edward_VI", 
     "Jane Seymour was the mother of Edward VI."),
    ("Jane_Seymour", "SUCCEEDS", "Anne_Boleyn", 
     "Jane Seymour succeeded Anne Boleyn as queen after her execution."),
    
    # === THOMAS WYATT THE YOUNGER ===
    ("Thomas_Wyatt_the_Younger", "LEADS", "Wyatts_Rebellion_1554", 
     "Thomas Wyatt led the rebellion against Mary I's Spanish marriage."),
    ("Thomas_Wyatt_the_Younger", "OPPOSES", "Mary_I", 
     "Thomas Wyatt opposed Mary I's Catholic policies and Spanish marriage."),
    ("Mary_I", "EXECUTES", "Thomas_Wyatt_the_Younger", 
     "Mary I executed Thomas Wyatt for leading the rebellion."),
    
    # === ROBERT ASKE ===
    ("Robert_Aske", "LEADS", "Pilgrimage_of_Grace_1536", 
     "Robert Aske led the Pilgrimage of Grace against Henry VIII's policies."),
    ("Robert_Aske", "OPPOSES", "Dissolution_of_the_Monasteries", 
     "Robert Aske opposed the dissolution of the monasteries."),
    ("Henry_VIII", "EXECUTES", "Robert_Aske", 
     "Henry VIII executed Robert Aske after the Pilgrimage of Grace."),
    ("Robert_Aske", "DEFENDS", "Papal_Supremacy", 
     "Robert Aske defended traditional religion and papal authority."),
    
    # === WILLIAM ALLEN ===
    ("William_Allen", "FOUNDS", "English_Seminaries_Douai_Rheims", 
     "William Allen founded the English College at Douai in 1568."),
    ("William_Allen", "ORGANIZES", "Seminary_Priests_Mission_1580s", 
     "William Allen organized the mission of seminary priests to England."),
    ("William_Allen", "ENDORSES", "Counter_Reformation_in_England", 
     "William Allen promoted the Counter-Reformation in England."),
    ("William_Allen", "SUPERVISES", "Rheims_New_Testament_1582", 
     "William Allen supervised production of the Rheims New Testament."),
    
    # === JOHN JEWEL ===
    ("John_Jewel", "WRITES", "Apology_of_the_Church_of_England_1562", 
     "John Jewel wrote the Apology of the Church of England."),
    ("John_Jewel", "DEFENDS", "Via_Media", 
     "John Jewel defended the Elizabethan religious settlement."),
    ("John_Jewel", "PARTICIPATES_IN", "Marian_Exile", 
     "John Jewel was among the Marian exiles who fled to the continent."),
    ("Apology_of_the_Church_of_England_1562", "DEFINES", "Church_of_England", 
     "Jewel's Apology defined Anglican ecclesiology."),
    
    # === THOMAS CARTWRIGHT ===
    ("Thomas_Cartwright", "ADVOCATES", "Presbyterian_Reform_in_England", 
     "Thomas Cartwright advocated Presbyterian church government."),
    ("Thomas_Cartwright", "OPPOSES", "Church_of_England", 
     "Thomas Cartwright opposed the episcopal structure of the Church of England."),
    ("Thomas_Cartwright", "TEACHES_AT", "University_of_Cambridge", 
     "Thomas Cartwright taught at Cambridge before his removal."),
    ("John_Whitgift", "OPPOSES", "Thomas_Cartwright", 
     "John Whitgift opposed Thomas Cartwright in the Admonition Controversy."),
    
    # === WALTER TRAVERS ===
    ("Walter_Travers", "DEBATES", "Richard_Hooker", 
     "Walter Travers debated Richard Hooker at the Temple Church."),
    ("Walter_Travers", "ENDORSES", "Presbyterian_Reform_in_England", 
     "Walter Travers endorsed Presbyterian reform."),
    ("Walter_Travers", "OPPOSES", "Via_Media", 
     "Walter Travers opposed the Elizabethan settlement's compromises."),
    
    # === ROBERT BROWNE ===
    ("Robert_Browne", "FOUNDS", "Separatist_Movement", 
     "Robert Browne's writings founded the Separatist movement."),
    ("Robert_Browne", "REJECTS", "Church_of_England", 
     "Robert Browne rejected the established Church of England entirely."),
    ("Robert_Browne", "INFLUENCES", "Puritan_Movement", 
     "Robert Browne's separatism influenced radical Puritanism."),
    
    # === HENRY BARROW ===
    ("Henry_Barrow", "ENDORSES", "Separatist_Movement", 
     "Henry Barrow endorsed complete separation from the established church."),
    ("Henry_Barrow", "DIES_IN", "Execution_of_Edmund_Campion_1581", 
     "Henry Barrow was executed for sedition in 1593."),
    ("Elizabeth_I", "EXECUTES", "Henry_Barrow", 
     "Elizabeth I's government executed Henry Barrow for seditious writings."),
    
    # === NEW TEXTS RELATIONSHIPS ===
    ("William_Tyndale", "WRITES", "Tyndale_New_Testament_1526", 
     "William Tyndale translated and published the first printed English New Testament."),
    ("Tyndale_New_Testament_1526", "PRINTED_IN", "Antwerp", 
     "Tyndale's New Testament was printed in Antwerp and Worms."),
    ("Tyndale_New_Testament_1526", "INFLUENCES", "Great_Bible_1539", 
     "Tyndale's translation formed the basis of the Great Bible."),
    ("Tyndale_New_Testament_1526", "BANNED_BY", "Church_of_England", 
     "Tyndale's New Testament was initially banned and burned in England."),
    
    ("Miles_Coverdale", "WRITES", "Coverdale_Bible_1535", 
     "Miles Coverdale produced the first complete printed English Bible."),
    ("Coverdale_Bible_1535", "DEDICATED_TO", "Henry_VIII", 
     "The Coverdale Bible was dedicated to Henry VIII."),
    ("Coverdale_Bible_1535", "PRECEDES", "Great_Bible_1539", 
     "The Coverdale Bible preceded and influenced the Great Bible."),
    
    ("Matthew_Bible_1537", "COMBINES", "Tyndale_New_Testament_1526", 
     "The Matthew Bible combined Tyndale's and Coverdale's work."),
    ("Matthew_Bible_1537", "AUTHORIZED_BY", "Henry_VIII", 
     "The Matthew Bible was the first officially authorized English Bible."),
    ("Matthew_Bible_1537", "PRECEDES", "Great_Bible_1539", 
     "The Matthew Bible preceded the Great Bible."),
    
    ("Henry_VIII", "WRITES", "Defense_of_the_Seven_Sacraments_1521", 
     "Henry VIII wrote Defense of the Seven Sacraments against Luther."),
    ("Defense_of_the_Seven_Sacraments_1521", "OPPOSES", "Continental_Reformations", 
     "Henry's Defense opposed Lutheran theology."),
    ("Defense_of_the_Seven_Sacraments_1521", "EARNS", "Henry_VIII", 
     "The Defense earned Henry the title 'Defender of the Faith' from the Pope."),
    
    ("Kings_Book_1543", "REVISES", "Bishops_Book_1537", 
     "The King's Book revised the earlier Bishops' Book in a conservative direction."),
    ("Henry_VIII", "PROMULGATES", "Kings_Book_1543", 
     "Henry VIII promulgated the King's Book as official doctrine."),
    
    ("Admonition_to_Parliament_1572", "DEMANDS", "Presbyterian_Reform_in_England", 
     "The Admonition demanded Presbyterian reform of the church."),
    ("Admonition_to_Parliament_1572", "ATTACKS", "Church_of_England", 
     "The Admonition attacked the episcopal structure."),
    ("Thomas_Cartwright", "INSPIRES", "Admonition_to_Parliament_1572", 
     "Thomas Cartwright's ideas inspired the Admonition."),
    
    ("English_Parliament", "PROMULGATES", "Recusancy_Acts", 
     "Parliament promulgated the Recusancy Acts against Catholics."),
    ("Recusancy_Acts", "ENABLES", "Recusancy_Fines_Regime", 
     "The Recusancy Acts enabled the system of fines against Catholics."),
    ("Recusancy_Acts", "PERSECUTES", "Recusant_Catholicism", 
     "The Recusancy Acts persecuted Catholic recusants."),
    
    ("English_Parliament", "PROMULGATES", "Act_Against_Jesuits_1585", 
     "Parliament promulgated the Act against Jesuits and seminary priests."),
    ("Act_Against_Jesuits_1585", "TARGETS", "Society_of_Jesus", 
     "The Act targeted Jesuits entering England."),
    ("Act_Against_Jesuits_1585", "ENABLES", "Execution_of_Edmund_Campion_1581", 
     "Similar legislation enabled Campion's prosecution."),
    
    ("Bond_of_Association_1584", "TARGETS", "Mary_Queen_of_Scots", 
     "The Bond of Association targeted Mary Queen of Scots."),
    ("William_Cecil", "DRAFTS", "Bond_of_Association_1584", 
     "William Cecil helped draft the Bond of Association."),
    
    # === NEW EVENTS RELATIONSHIPS ===
    ("Execution_of_Anne_Boleyn_1536", "KILLS", "Anne_Boleyn", 
     "The execution killed Queen Anne Boleyn."),
    ("Henry_VIII", "ORDERS", "Execution_of_Anne_Boleyn_1536", 
     "Henry VIII ordered Anne Boleyn's execution."),
    ("Execution_of_Anne_Boleyn_1536", "ENABLES", "Jane_Seymour", 
     "Anne's execution enabled Henry to marry Jane Seymour."),
    ("Execution_of_Anne_Boleyn_1536", "OCCURS_IN", "Tower_of_London", 
     "Anne Boleyn was executed at the Tower of London."),
    
    ("Execution_of_Thomas_More_1535", "KILLS", "Thomas_More", 
     "The execution killed Sir Thomas More."),
    ("Thomas_More", "DIES_IN", "Execution_of_Thomas_More_1535", 
     "Thomas More died in his execution on July 6, 1535."),
    ("Henry_VIII", "ORDERS", "Execution_of_Thomas_More_1535", 
     "Henry VIII ordered Thomas More's execution."),
    ("Execution_of_Thomas_More_1535", "OCCURS_IN", "Tower_of_London", 
     "Thomas More was executed at the Tower of London."),
    
    ("Burning_of_William_Tyndale_1536", "KILLS", "William_Tyndale", 
     "The execution killed Bible translator William Tyndale."),
    ("William_Tyndale", "DIES_IN", "Burning_of_William_Tyndale_1536", 
     "William Tyndale died in his execution on October 6, 1536."),
    ("Burning_of_William_Tyndale_1536", "OCCURS_IN", "Antwerp", 
     "Tyndale was executed near Antwerp at Vilvoorde."),
    
    ("Babington_Plot_1586", "TARGETS", "Elizabeth_I", 
     "The Babington Plot aimed to assassinate Elizabeth I."),
    ("Babington_Plot_1586", "SUPPORTS", "Mary_Queen_of_Scots", 
     "The Babington Plot sought to place Mary on the throne."),
    ("Babington_Plot_1586", "LEADS_TO", "Trial_of_Mary_Queen_of_Scots_1586", 
     "The Babington Plot led to Mary's trial."),
    ("William_Cecil", "UNCOVERS", "Babington_Plot_1586", 
     "William Cecil's intelligence network uncovered the Babington Plot."),
    
    ("Throckmorton_Plot_1583", "TARGETS", "Elizabeth_I", 
     "The Throckmorton Plot aimed to overthrow Elizabeth I."),
    ("Throckmorton_Plot_1583", "INVOLVES", "Philip_II_of_Spain", 
     "The Throckmorton Plot involved Spanish support."),
    ("Throckmorton_Plot_1583", "SUPPORTS", "Mary_Queen_of_Scots", 
     "The Throckmorton Plot sought to place Mary on the throne."),
    
    ("Ridolfi_Plot_1571", "TARGETS", "Elizabeth_I", 
     "The Ridolfi Plot aimed to replace Elizabeth I."),
    ("Ridolfi_Plot_1571", "SUPPORTS", "Mary_Queen_of_Scots", 
     "The Ridolfi Plot sought to place Mary on the throne."),
    ("Ridolfi_Plot_1571", "FOLLOWS", "Regnans_in_Excelsis_1570", 
     "The Ridolfi Plot followed the papal excommunication of Elizabeth."),
    
    ("Trial_of_Mary_Queen_of_Scots_1586", "OCCURS_IN", "Fotheringhay", 
     "Mary Queen of Scots was tried at Fotheringhay Castle."),
    ("Trial_of_Mary_Queen_of_Scots_1586", "CONVICTS", "Mary_Queen_of_Scots", 
     "The trial convicted Mary Queen of Scots."),
    ("Trial_of_Mary_Queen_of_Scots_1586", "LEADS_TO", "Execution_of_Mary_Queen_of_Scots_1587", 
     "The trial led to Mary's execution."),
    
    ("Submission_of_the_Clergy_1532", "SURRENDERS_TO", "Henry_VIII", 
     "The clergy surrendered legislative independence to Henry VIII."),
    ("Submission_of_the_Clergy_1532", "ENABLES", "Royal_Supremacy", 
     "The Submission enabled royal supremacy over the church."),
    ("Thomas_Cromwell", "ORCHESTRATES", "Submission_of_the_Clergy_1532", 
     "Thomas Cromwell orchestrated the Submission of the Clergy."),
    
    ("Convocation_of_1563", "APPROVES", "Thirty-Nine_Articles_1563", 
     "The Convocation of 1563 approved the Thirty-Nine Articles."),
    ("Convocation_of_Canterbury", "HOLDS", "Convocation_of_1563", 
     "The Convocation of Canterbury held the 1563 meeting."),
    ("Convocation_of_1563", "REJECTS", "Puritan_Movement", 
     "The Convocation narrowly rejected further Puritan reforms."),
    
    ("Prophesyings_Controversy_1576", "INVOLVES", "Edmund_Grindal", 
     "The prophesyings controversy involved Archbishop Grindal."),
    ("Elizabeth_I", "SUPPRESSES", "Prophesyings_Controversy_1576", 
     "Elizabeth I ordered suppression of the prophesyings."),
    ("Prophesyings_Controversy_1576", "CONCERNS", "Puritan_Movement", 
     "The prophesyings were associated with Puritan clergy."),
    
    ("Execution_of_Edmund_Campion_1581", "KILLS", "Edmund_Campion", 
     "The execution killed Jesuit priest Edmund Campion."),
    ("Execution_of_Edmund_Campion_1581", "OCCURS_IN", "London", 
     "Edmund Campion was executed at Tyburn in London."),
    ("Elizabeth_I", "ORDERS", "Execution_of_Edmund_Campion_1581", 
     "Elizabeth I's government ordered Campion's execution."),
    
    ("Act_of_Succession_1534", "LEGITIMIZES", "Anne_Boleyn", 
     "The Act of Succession legitimized Anne Boleyn's children."),
    ("English_Parliament", "PROMULGATES", "Act_of_Succession_1534", 
     "Parliament promulgated the Act of Succession."),
    ("Act_of_Succession_1534", "DELEGITIMIZES", "Mary_I", 
     "The Act delegitimized Mary Tudor."),
    
    # === NEW INSTITUTIONS RELATIONSHIPS ===
    ("Convocation_of_Canterbury", "GOVERNS", "Church_of_England", 
     "The Convocation of Canterbury governed church legislation."),
    ("Convocation_of_Canterbury", "SUBMITS_TO", "Henry_VIII", 
     "The Convocation submitted to royal authority in 1532."),
    
    ("Council_of_the_North", "GOVERNS", "York", 
     "The Council of the North governed from York."),
    ("Council_of_the_North", "SUPPRESSES", "Pilgrimage_of_Grace_1536", 
     "The Council was strengthened after suppressing the Pilgrimage."),
    ("Henry_VIII", "STRENGTHENS", "Council_of_the_North", 
     "Henry VIII strengthened the Council of the North."),
    
    ("English_College_Rome", "TRAINS", "Jesuit_Mission_in_England", 
     "The English College Rome trained priests for the English mission."),
    ("William_Allen", "INFLUENCES", "English_College_Rome", 
     "William Allen influenced the establishment of the English College Rome."),
    
    ("Doctors_Commons", "HANDLES", "Annulment_Proceedings", 
     "Doctors' Commons lawyers handled the annulment proceedings."),
    
    # === MARIAN EXILE RELATIONSHIPS ===
    ("Marian_Exile", "CAUSED_BY", "Mary_I", 
     "The Marian Exile was caused by Mary I's Catholic restoration."),
    ("Marian_Exile", "INCLUDES", "John_Knox", 
     "The Marian Exile included John Knox."),
    ("Marian_Exile", "INCLUDES", "John_Foxe", 
     "The Marian Exile included John Foxe."),
    ("Marian_Exile", "INCLUDES", "Miles_Coverdale", 
     "The Marian Exile included Miles Coverdale."),
    ("Marian_Exile", "PRODUCES", "Geneva_Bible_1560", 
     "The Marian exiles produced the Geneva Bible."),
    ("Marian_Exile", "RADICALIZES", "Puritan_Movement", 
     "The Marian Exile radicalized many who became Puritans."),
    ("Geneva", "HOSTS", "Marian_Exile", 
     "Geneva hosted many Marian exiles."),
    ("Strasbourg", "HOSTS", "Marian_Exile", 
     "Strasbourg hosted Marian exiles."),
    
    # === COUNTER-REFORMATION RELATIONSHIPS ===
    ("Counter_Reformation_in_England", "INCLUDES", "Jesuit_Mission_in_England", 
     "The Counter-Reformation in England included the Jesuit mission."),
    ("Counter_Reformation_in_England", "INCLUDES", "Seminary_Priests_Mission_1580s", 
     "The Counter-Reformation included the seminary priests' mission."),
    ("Counter_Reformation_in_England", "OPPOSES", "Elizabeth_I", 
     "The Counter-Reformation opposed Elizabeth I's Protestant regime."),
    ("Society_of_Jesus", "LEADS", "Counter_Reformation_in_England", 
     "The Society of Jesus led Counter-Reformation efforts in England."),
    
    # === ERASTIANISM RELATIONSHIPS ===
    ("Erastianism", "UNDERLIES", "Royal_Supremacy", 
     "Erastianism underlies the doctrine of royal supremacy."),
    ("Richard_Hooker", "DEFENDS", "Erastianism", 
     "Richard Hooker's ecclesiology defended Erastian principles."),
    
    # === PLACE RELATIONSHIPS ===
    ("Smithfield", "HOSTS", "Heresy_Persecutions", 
     "Smithfield was the site of Protestant burnings during Marian persecutions."),
    ("Heresy_Persecutions", "OCCURS_IN", "Smithfield", 
     "Many heresy burnings occurred at Smithfield."),
    
    ("Tower_of_London", "IMPRISONS", "Thomas_More", 
     "The Tower of London imprisoned Thomas More before his execution."),
    ("Tower_of_London", "IMPRISONS", "John_Fisher", 
     "The Tower of London imprisoned John Fisher before his execution."),
    ("Tower_of_London", "IMPRISONS", "Anne_Boleyn", 
     "The Tower of London imprisoned Anne Boleyn before her execution."),
    ("Tower_of_London", "IMPRISONS", "Thomas_Cranmer", 
     "The Tower of London imprisoned Thomas Cranmer."),
    
    ("Fotheringhay", "HOSTS", "Trial_of_Mary_Queen_of_Scots_1586", 
     "Fotheringhay Castle hosted Mary's trial."),
    ("Execution_of_Mary_Queen_of_Scots_1587", "OCCURS_IN", "Fotheringhay", 
     "Mary Queen of Scots was executed at Fotheringhay."),
    
    ("Wittenberg", "ORIGINATES", "Continental_Reformations", 
     "Wittenberg was where Luther originated the Protestant Reformation."),
    ("Wittenberg", "INFLUENCES", "Protestant_Doctrine_in_England", 
     "Wittenberg's Reformation influenced English Protestant thought."),
    
    ("Geneva", "PRODUCES", "Geneva_Bible_1560", 
     "Geneva produced the influential Geneva Bible."),
    ("Geneva", "INFLUENCES", "Puritan_Movement", 
     "Geneva's Reformed theology influenced English Puritanism."),
    
    ("Antwerp", "PRINTS", "Tyndale_New_Testament_1526", 
     "Antwerp was where Tyndale's works were printed."),
    ("Antwerp", "SUPPLIES", "English_Bible_Translation", 
     "Antwerp supplied smuggled English Bibles to England."),
    
    ("Strasbourg", "PRODUCES", "Martin_Bucer", 
     "Strasbourg produced reformer Martin Bucer."),
    
    # === MORE EXISTING NODE EDGES ===
    ("Thomas_Cromwell", "SUCCEEDS", "Thomas_Wolsey", 
     "Thomas Cromwell succeeded Wolsey as Henry VIII's chief minister."),
    ("Thomas_Cromwell", "ENGINEERS", "Break_with_Rome", 
     "Thomas Cromwell engineered the break with Rome through parliamentary legislation."),
    ("Thomas_Cromwell", "DRAFTS", "Act_of_Supremacy_1534", 
     "Thomas Cromwell drafted the Act of Supremacy."),
    ("Thomas_Cromwell", "ORGANIZES", "Valor_Ecclesiasticus_1535", 
     "Thomas Cromwell organized the Valor Ecclesiasticus survey."),
    ("Henry_VIII", "EXECUTES", "Thomas_Cromwell", 
     "Henry VIII executed Thomas Cromwell in 1540."),
    
    ("Anne_Boleyn", "MOTHER_OF", "Elizabeth_I", 
     "Anne Boleyn was the mother of Elizabeth I."),
    # marriage modeled as an Event + participation edges; see MARRIAGES below
    ("Anne_Boleyn", "DIES_IN", "Execution_of_Anne_Boleyn_1536", 
     "Anne Boleyn died in her execution in 1536."),
    
    # marriage modeled as an Event + participation edges; see MARRIAGES below
    ("Catherine_of_Aragon", "MOTHER_OF", "Mary_I", 
     "Catherine of Aragon was the mother of Mary I."),
    ("Catherine_of_Aragon", "DEFENDED_BY", "John_Fisher", 
     "Catherine of Aragon was defended by John Fisher at her trial."),
    
    ("Regnans_in_Excelsis_1570", "EXCOMMUNICATES", "Elizabeth_I", 
     "The papal bull Regnans in Excelsis excommunicated Elizabeth I."),
    ("Papacy", "ISSUES", "Regnans_in_Excelsis_1570", 
     "The Papacy issued Regnans in Excelsis in 1570."),
    ("Regnans_in_Excelsis_1570", "ENCOURAGES", "Recusant_Catholicism", 
     "The bull encouraged Catholic resistance to Elizabeth."),
    
    ("Oxford_Martyrs_1555_1556", "OCCURS_IN", "Smithfield", 
     "While called Oxford Martyrs, many others were burned at Smithfield."),
    
    # === THOMAS CRANMER ADDITIONAL ===
    ("Thomas_Cranmer", "IMPRISONED_IN", "Tower_of_London", 
     "Thomas Cranmer was imprisoned in the Tower before his trial."),
    ("Thomas_Cranmer", "INFLUENCED_BY", "Martin_Bucer", 
     "Thomas Cranmer was influenced by Martin Bucer's theology."),
    
    # === HENRY VIII ADDITIONAL ===
    ("Henry_VIII", "TITLED", "Defense_of_the_Seven_Sacraments_1521", 
     "Henry VIII was titled Defender of the Faith for his treatise."),
    ("Henry_VIII", "DIVORCES", "Catherine_of_Aragon", 
     "Henry VIII divorced Catherine of Aragon through Cranmer's annulment."),
    
    # === MARY I ADDITIONAL ===
    ("Mary_I", "DAUGHTER_OF", "Catherine_of_Aragon", 
     "Mary I was the daughter of Catherine of Aragon."),
    # marriage modeled as an Event + participation edges; see MARRIAGES below
    ("Mary_I", "RESTORES", "Roman_Catholic_Church", 
     "Mary I restored the Roman Catholic Church in England."),
    
    # === ELIZABETH I ADDITIONAL ===  
    ("Elizabeth_I", "DAUGHTER_OF", "Anne_Boleyn", 
     "Elizabeth I was the daughter of Anne Boleyn."),
    ("Elizabeth_I", "SUCCEEDS", "Mary_I", 
     "Elizabeth I succeeded Mary I in 1558."),
    ("Elizabeth_I", "DEFEATS", "Spanish_Armada_1588", 
     "Elizabeth I's navy defeated the Spanish Armada."),
    ("Elizabeth_I", "APPOINTS", "William_Cecil", 
     "Elizabeth I appointed William Cecil as her principal secretary."),
    
    # === EDWARD VI ADDITIONAL ===
    ("Edward_VI", "SON_OF", "Henry_VIII", 
     "Edward VI was the son of Henry VIII."),
    ("Edward_VI", "SON_OF", "Jane_Seymour", 
     "Edward VI was the son of Jane Seymour."),
    ("Edward_VI", "SUCCEEDS", "Henry_VIII", 
     "Edward VI succeeded Henry VIII in 1547."),
]

# Marriage is modeled as an Event + participation edges (not P↔P).
# Format: (spouse_a_slug, spouse_b_slug, description)
MARRIAGES = [
    ("Philip_II_of_Spain", "Mary_I", "Philip II of Spain married Mary I in 1554."),
    ("Jane_Seymour", "Henry_VIII", "Jane Seymour married Henry VIII in 1536."),
    ("Anne_Boleyn", "Henry_VIII", "Anne Boleyn married Henry VIII in 1533."),
    ("Catherine_of_Aragon", "Henry_VIII", "Catherine of Aragon was Henry VIII's first wife."),
]

# ============================================================================
# SCRIPT LOGIC
# ============================================================================

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_or_create_marriage_event(nodes_data: dict, spouse_a: str, spouse_b: str, description: str):
    a, b = sorted([spouse_a, spouse_b])
    event_slug = f"Marriage_{a}_{b}"
    existing = {n['slug'] for n in nodes_data.get('nodes', [])}
    if event_slug in existing:
        return event_slug, False

    nodes_data['nodes'].append({
        "slug": event_slug,
        "name": f"Marriage: {a} × {b}",
        "label": "Event",
        "kind": "Marriage",
        "cluster": "English_Reformation",
        "status": "PROPOSED",
        "workflow_stage": "PROPOSED",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "created_by": "expand_english_reformation.py",
        "description": description,
    })
    return event_slug, True

def main():
    nodes_path = Path('data/Nodes/nodes.English_Reformation.json')
    rels_path = Path('data/Relationships/relationships.English_Reformation.json')
    
    # Load existing data
    nodes_data = load_json(nodes_path)
    rels_data = load_json(rels_path)
    
    existing_slugs = {n['slug'] for n in nodes_data['nodes']}
    print(f"Existing nodes: {len(existing_slugs)}")
    print(f"Existing relationships: {len(rels_data['relationships'])}")
    
    # Add new nodes
    all_new_nodes = NEW_PERSONS + NEW_TEXTS + NEW_EVENTS + NEW_INSTITUTIONS + NEW_PLACES + NEW_MOVEMENTS
    
    added_nodes = 0
    for node in all_new_nodes:
        if node['slug'] not in existing_slugs:
            nodes_data['nodes'].append(node)
            existing_slugs.add(node['slug'])
            added_nodes += 1
            print(f"  + Node: {node['slug']} ({node['label']})")
    
    print(f"\nAdded {added_nodes} new nodes")
    
    # Add new relationships
    existing_rels = set()
    for r in rels_data['relationships']:
        key = (r.get('start_slug'), r.get('type'), r.get('end_slug'))
        existing_rels.add(key)
    
    next_id = max(r.get('id', 0) for r in rels_data['relationships']) + 1
    
    added_rels = 0
    skipped_missing = 0
    skipped_exists = 0
    missing_nodes = set()
    
    for start, rel_type, end, desc in NEW_RELATIONSHIPS:
        # Check nodes exist
        if start not in existing_slugs:
            missing_nodes.add(start)
            skipped_missing += 1
            continue
        if end not in existing_slugs:
            missing_nodes.add(end)
            skipped_missing += 1
            continue
        
        # Check relationship doesn't exist
        key = (start, rel_type, end)
        if key in existing_rels:
            skipped_exists += 1
            continue
        
        new_rel = {
            "id": next_id,
            "start_slug": start,
            "end_slug": end,
            "type": rel_type,
            "description": desc,
            "status": "PROPOSED",
            "evidence_url": None,
            "citation_style": "Chicago 17",
            "page_refs": None,
            "source_note": "curator:deep_expansion_2025",
            "inline_evidence": False
        }
        rels_data['relationships'].append(new_rel)
        existing_rels.add(key)
        next_id += 1
        added_rels += 1
        print(f"  + ({start})-[{rel_type}]->({end})")

    # Add marriage-as-event modeling
    marriage_nodes_added = 0
    marriage_edges_added = 0
    for spouse_a, spouse_b, desc in MARRIAGES:
        if spouse_a not in existing_slugs or spouse_b not in existing_slugs:
            continue

        marriage_slug, created = get_or_create_marriage_event(nodes_data, spouse_a, spouse_b, desc)
        if created:
            existing_slugs.add(marriage_slug)
            marriage_nodes_added += 1
            print(f"  + Node: {marriage_slug} (Event/Marriage)")

        for spouse in (spouse_a, spouse_b):
            key = (spouse, "PARTICIPATES_IN", marriage_slug)
            if key in existing_rels:
                continue
            new_rel = {
                "id": next_id,
                "start_slug": spouse,
                "end_slug": marriage_slug,
                "type": "PARTICIPATES_IN",
                "role": "spouse",
                "description": f"{spouse} participated as a spouse in {marriage_slug}.",
                "status": "PROPOSED",
                "evidence_url": None,
                "citation_style": "Chicago 17",
                "page_refs": None,
                "source_note": "curator:deep_expansion_2025",
                "inline_evidence": False
            }
            rels_data['relationships'].append(new_rel)
            existing_rels.add(key)
            next_id += 1
            marriage_edges_added += 1
            print(f"  + ({spouse})-[PARTICIPATES_IN {{role:spouse}}]->({marriage_slug})")
    
    if missing_nodes:
        print(f"\nMissing nodes (skipped): {sorted(missing_nodes)}")
    
    print(f"\n=== Summary ===")
    print(f"  Nodes added: {added_nodes}")
    print(f"  Relationships added: {added_rels}")
    print(f"  Relationships skipped (exists): {skipped_exists}")
    print(f"  Relationships skipped (missing): {skipped_missing}")
    print(f"  Marriage event nodes added: {marriage_nodes_added}")
    print(f"  Marriage participation edges added: {marriage_edges_added}")
    print(f"  Total nodes now: {len(nodes_data['nodes'])}")
    print(f"  Total relationships now: {len(rels_data['relationships'])}")
    
    # Save
    nodes_data['_meta']['last_expanded'] = datetime.now(timezone.utc).isoformat()
    rels_data['_meta']['last_expanded'] = datetime.now(timezone.utc).isoformat()
    
    save_json(nodes_path, nodes_data)
    save_json(rels_path, rels_data)
    print(f"\nSaved to {nodes_path} and {rels_path}")

if __name__ == '__main__':
    main()
