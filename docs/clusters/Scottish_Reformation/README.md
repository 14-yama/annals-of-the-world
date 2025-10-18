# Scottish_Reformation (Presbyterian stream)

A curated cluster covering the Scottish Reformation from early evangelical currents through the 1560 settlement and kirk consolidation.

- Root and Periods (D)
	- Scottish_Reformation (D)
		- Pre-Reformation_Currents_(1520s–1559) (D)
		- Reformation_Parliament_and_Settlement_1560 (D)
		- Kirk_Consolidation_and_Conflicts_(1560–1603) (D)

- Pre-Reformation_Currents_(1520s–1559) (D)
	- Persons (P): John_Knox; George_Wishart; Cardinal_David_Beaton; Mary_of_Guise; Lords_of_the_Congregation; John_Willum; John_Calvin (interface)
	- Institutions (I): University_of_St_Andrews; Scottish_Regency_Council; Papacy
	- Texts (T): Wishart_Sermons; Knox_Writings_1558_The_First_Blast
	- Movements (M): Evangelical_Currents_in_Scotland; Presbyterianism; Iconoclasm_Waves
	- Events (E): Wishart_Execution_1546; Siege_of_St_Andrews_Castle_1546_1547; Congregation_Risings_1559
	- Places (L): St_Andrews; Edinburgh; Perth

	- Wiring
		- P/I → E
			- (Cardinal_David_Beaton) CENSORS (Evangelical_Currents_in_Scotland)
			- (Scottish_Regency_Council) ORGANIZES (Congregation_Risings_1559) — suppression response
		- T ↔ M
			- (Knox_Writings_1558_The_First_Blast) FRAMES (Presbyterianism)
		- P ↔ M
			- (John_Knox) ENDORSES (Presbyterianism)
		- E → L
			- (Wishart_Execution_1546) OCCURS_IN (St_Andrews)
			- (Congregation_Risings_1559) OCCURS_IN (Perth)

- Reformation_Parliament_and_Settlement_1560 (D)
	- Persons (P): John_Knox; James_Stewart_(Earl_of_Moray); William_Maitland; Mary_Queen_of_Scots; English_Aid_Commanders (interface)
	- Institutions (I): Scottish_Parliament; Lords_of_the_Congregation; General_Assembly_of_the_Kirk; Privy_Council_of_Scotland
	- Texts (T): Scots_Confession_1560; First_Book_of_Discipline_1560; Book_of_Common_Order
	- Movements (M): Presbyterianism; Royal_Supremacy_(Scotland); Via_Media_(England_interface)
	- Events (E): Reformation_Parliament_1560; Ratification_of_Scots_Confession_1560; First_General_Assembly_1560
	- Places (L): Edinburgh

	- Wiring
		- I → T/D/E
			- (Scottish_Parliament) PROMULGATES (Scots_Confession_1560)
			- (General_Assembly_of_the_Kirk) PROMULGATES (First_Book_of_Discipline_1560)
		- P/I → E
			- (Lords_of_the_Congregation) ORGANIZES (Reformation_Parliament_1560)
		- T ↔ M
			- (Scots_Confession_1560) STANDARDIZES (Presbyterianism)
			- (Book_of_Common_Order) TRANSMITS (Presbyterianism)
		- E → L
			- (Reformation_Parliament_1560) OCCURS_IN (Edinburgh)

- Kirk_Consolidation_and_Conflicts_(1560–1603) (D)
	- Persons (P): John_Knox; Andrew_Melville; James_VI; Regent_Moray; John_Whitgift (interface)
	- Institutions (I): General_Assembly_of_the_Kirk; Privy_Council_of_Scotland; Scottish_Parliament
	- Texts (T): Second_Book_of_Discipline_1578; Black_Acts_1584; Golden_Act_1592
	- Movements (M): Presbyterianism; Episcopacy_in_Scotland; Covenanter_Precursors
	- Events (E): Mary_Queen_of_Scots_Deposition_1567; Ruthven_Raid_1582; Black_Acts_Passage_1584; Golden_Act_Passage_1592
	- Places (L): Edinburgh; St_Andrews; Glasgow

	- Wiring
		- I/T → M
			- (Second_Book_of_Discipline_1578) STANDARDIZES (Presbyterianism)
			- (Black_Acts_1584) CENSORS (Presbyterianism)
			- (Golden_Act_1592) STANDARDIZES (Presbyterianism)
		- P ↔ M
			- (Andrew_Melville) ENDORSES (Presbyterianism)
			- (James_VI) ENDORSES (Episcopacy_in_Scotland)
		- E → L
			- (Ruthven_Raid_1582) OCCURS_IN (Edinburgh)

## Descriptions (one‑liners)

#### Root and Periods (D)

| Node | G/C | Description |
| --- | --- | --- |
| Scottish_Reformation | G | Curated view of the Scottish Presbyterian Reformation. |
| Pre-Reformation_Currents_(1520s–1559) | C | Evangelical agitation under regency. |
| Reformation_Parliament_and_Settlement_1560 | C | Settlement via parliament and kirk structures. |
| Kirk_Consolidation_and_Conflicts_(1560–1603) | C | Consolidation and jurisdictional contests. |

#### Persons (P)

| Node | G/C | Description |
| --- | --- | --- |
| John_Knox | C | Leading preacher and organizer of the settlement. |
| George_Wishart | C | Martyr preacher influencing Knox. |
| Cardinal_David_Beaton | C | Prelate opposing evangelical currents. |
| Mary_of_Guise | C | Regent navigating French/Scottish politics. |
| Lords_of_the_Congregation | C | Noble coalition advancing reform. |
| John_Willum | C | Early evangelical actor in Scotland. |
| John_Calvin | C | Geneva reformer advising Scots (interface). |
| James_Stewart_(Earl_of_Moray) | C | Regent and reform ally. |
| William_Maitland | C | Statesman shaping settlement politics. |
| Mary_Queen_of_Scots | C | Monarch whose reign intersected reform. |
| English_Aid_Commanders | C | English intervention leaders (interface). |
| Andrew_Melville | C | Theologian of presbyterian polity. |
| James_VI | C | Monarch favoring episcopal structures. |
| Regent_Moray | C | Regent during early kirk consolidation. |

#### Institutions (I)

| Node | G/C | Description |
| --- | --- | --- |
| University_of_St_Andrews | C | Academic and clerical training center. |
| Scottish_Regency_Council | C | Governance during minority/regency. |
| Papacy | C | Roman see and curial authority. |
| Scottish_Parliament | C | Legislature enacting reformation statutes. |
| Lords_of_the_Congregation | C | Noble coalition acting as proto-institution. |
| General_Assembly_of_the_Kirk | C | Representative body governing the kirk. |
| Privy_Council_of_Scotland | C | Executive council implementing policy. |

#### Texts/Artifacts (T)

| Node | G/C | Description |
| --- | --- | --- |
| Wishart_Sermons | C | Preaching texts fueling evangelical sentiment. |
| Knox_Writings_1558_The_First_Blast | C | Polemical tract against female rule. |
| Scots_Confession_1560 | C | Doctrinal basis of the settlement. |
| First_Book_of_Discipline_1560 | C | Polity/discipline framework for the kirk. |
| Book_of_Common_Order | C | Liturgical book for worship. |
| Second_Book_of_Discipline_1578 | C | Mature presbyterian polity treatise. |
| Black_Acts_1584 | C | Statutes favoring royal/episcopal control. |
| Golden_Act_1592 | C | Statute recognizing presbyterian structures. |

#### Movements (M)

| Node | G/C | Description |
| --- | --- | --- |
| Evangelical_Currents_in_Scotland | C | Early reform preaching and circles. |
| Presbyterianism | C | Church polity emphasizing elders and assemblies. |
| Iconoclasm_Waves | C | Episodes of image removal. |
| Royal_Supremacy_(Scotland) | C | Crown’s claim to church governance. |
| Via_Media_(England_interface) | C | English middle way as comparative referent. |
| Episcopacy_in_Scotland | C | Bishops’ governance model. |
| Covenanter_Precursors | C | Early roots of later covenanting. |

#### Events (E)

| Node | G/C | Description |
| --- | --- | --- |
| Wishart_Execution_1546 | C | Execution of George Wishart. |
| Siege_of_St_Andrews_Castle_1546_1547 | C | Siege following Wishart’s martyrdom. |
| Congregation_Risings_1559 | C | Mobilizations pressing for reform. |
| Reformation_Parliament_1560 | C | Parliament enacting the settlement. |
| Ratification_of_Scots_Confession_1560 | C | Doctrinal ratification by parliament. |
| First_General_Assembly_1560 | C | Inaugural kirk assembly. |
| Mary_Queen_of_Scots_Deposition_1567 | C | Abdication under political pressure. |
| Ruthven_Raid_1582 | C | Seizure of the king by nobles. |
| Black_Acts_Passage_1584 | C | Statutes curtailing kirk autonomy. |
| Golden_Act_Passage_1592 | C | Statute affirming presbyterian governance. |

#### Places (L)

| Node | G/C | Description |
| --- | --- | --- |
| St_Andrews | G | University/episcopal city and early hotspot. |
| Edinburgh | G | Scottish capital and parliamentary seat. |
| Perth | G | Burgh involved in early risings. |
| Glasgow | G | Urban center with kirk activity. |
