# German_Reformation (interface to Swiss/Reformed and Radical)

A curated cluster covering the German (Lutheran) Reformation from 1517 through the Peace of Augsburg, with interfaces to Swiss/Reformed and Radical (Anabaptist) streams.

- Root and Periods (D)
	- German_Reformation (D)
		- Early_Lutheran_Phase_(1517–1521) (D)
		- Consolidation_and_Confessions_(1521–1530) (D)
		- Expansion_Conflict_and_Settlement_(1530–1555) (D)

- Early_Lutheran_Phase_(1517–1521) (D)
	- Persons (P): Martin_Luther; Johann_Tetzel; Andreas_Karlstadt; Frederick_the_Wise; Charles_V; Pope_Leo_X; Johannes_Eck; Desiderius_Erasmus (interface)
	- Institutions (I): University_of_Wittenberg; Augustinian_Order; Papacy; Roman_Curial_Courts; Holy_Roman_Empire; Imperial_Diet
	- Texts (T): Ninety-Five_Theses_1517; Leipzig_Debate_Proceedings_1519; Address_to_the_Christian_Nobility_1520; Babylonian_Captivity_of_the_Church_1520; Freedom_of_a_Christian_1520; Edict_of_Worms_1521
	- Movements (M): Lutheran_Reformation; Humanism_in_Germany; Indulgence_Critique
	- Events (E): Posting_of_Theses_1517; Leipzig_Debate_1519; Diet_of_Worms_1521
	- Places (L): Wittenberg; Leipzig; Worms; Saxony; Rome

	- Wiring
		- P/I → E
			- (Martin_Luther) DECLARES (Posting_of_Theses_1517)
			- (University_of_Wittenberg) ORGANIZES (Posting_of_Theses_1517)
			- (Johannes_Eck) DISPUTES (Leipzig_Debate_1519)
			- (Imperial_Diet) ORGANIZES (Diet_of_Worms_1521)
			- (Charles_V) DECLARES (Edict_of_Worms_1521)
		- I → P
			- (Papacy) EXCOMMUNICATES (Martin_Luther)
		- T ↔ E/D
			- (Ninety-Five_Theses_1517) FRAMES (Posting_of_Theses_1517)
			- (Address_to_the_Christian_Nobility_1520) FRAMES (Lutheran_Reformation)
			- (Babylonian_Captivity_of_the_Church_1520) DISPUTES (Papal_Supremacy)
			- (Freedom_of_a_Christian_1520) INTERPRETS (Lutheran_Reformation)
			- (Edict_of_Worms_1521) CENSORS (Lutheran_Reformation)
		- P ↔ M
			- (Martin_Luther) ENDORSES (Lutheran_Reformation)
			- (Desiderius_Erasmus) ENDORSES (Humanism_in_Germany)
		- E → L
			- (Posting_of_Theses_1517) OCCURS_IN (Wittenberg)
			- (Leipzig_Debate_1519) OCCURS_IN (Leipzig)
			- (Diet_of_Worms_1521) OCCURS_IN (Worms)

- Consolidation_and_Confessions_(1521–1530) (D)
	- Persons (P): Martin_Luther; Philipp_Melanchthon; Frederick_the_Wise; Thomas_Muenzter; Ulrich_Zwingli (interface); Johannes_Eck; Huldrych_Zwingli (interface)
	- Institutions (I): Saxon_Electorate; City_Council_Wittenberg; Papacy; City_Council_Zurich (interface)
	- Texts (T): Luther_Bible_New_Testament_1522; Luther_Bible_1534; Marburg_Articles_1529; Augsburg_Confession_1530
	- Movements (M): Lutheran_Reformation; Radical_Reformation; Anabaptist_Movement; Reformed_Tradition (interface); Iconoclasm_Waves
	- Events (E): Wartburg_Translation_1521_1522; Peasants_War_1524_1525; Marburg_Colloquy_1529; Diet_of_Augsburg_1530
	- Places (L): Wartburg; Wittenberg; Zurich; Marburg; Augsburg; Thuringia

	- Wiring
		- P/I → E
			- (Martin_Luther) TRANSLATES (Wartburg_Translation_1521_1522)
			- (Philipp_Melanchthon) ORGANIZES (Diet_of_Augsburg_1530)
			- (City_Council_Wittenberg) ORGANIZES (Iconoclasm_Waves)
			- (Ulrich_Zwingli) ORGANIZES (Marburg_Colloquy_1529)
		- T ↔ D/M/E
			- (Luther_Bible_New_Testament_1522) TRANSMITS (Lutheran_Reformation)
			- (Luther_Bible_1534) TRANSMITS (Lutheran_Reformation)
			- (Marburg_Articles_1529) DISPUTES (Lutheran_Reformation)
			- (Augsburg_Confession_1530) STANDARDIZES (Lutheran_Reformation)
		- P ↔ M
			- (Thomas_Muenzter) ENDORSES (Radical_Reformation)
			- (Philipp_Melanchthon) ENDORSES (Lutheran_Reformation)
		- M ↔ M
			- (Reformed_Tradition) DISPUTES (Lutheran_Reformation)
			- (Anabaptist_Movement) DISPUTES (Lutheran_Reformation)
		- E → L
			- (Wartburg_Translation_1521_1522) OCCURS_IN (Wartburg)
			- (Peasants_War_1524_1525) OCCURS_IN (Thuringia)
			- (Marburg_Colloquy_1529) OCCURS_IN (Marburg)
			- (Diet_of_Augsburg_1530) OCCURS_IN (Augsburg)

- Expansion_Conflict_and_Settlement_(1530–1555) (D)
	- Persons (P): Charles_V; Philipp_Melanchthon; Martin_Luther; John_Calvin (interface); John_Frederick_I_of_Saxony; Maurice_of_Saxony; Menno_Simons
	- Institutions (I): Schmalkaldic_League; Holy_Roman_Empire; Imperial_Diet; City_Council_Augsburg; Saxon_Electorate; Geneva_Consistory (interface)
	- Texts (T): Schmalkald_Articles_1537; Augsburg_Interim_1548; Peace_of_Augsburg_1555
	- Movements (M): Lutheran_Reformation; Anabaptist_Movement; Reformed_Tradition (interface); Confessionalization
	- Events (E): Princes_Protest_of_Speyer_1529; Schmalkaldic_War_1546_1547; Munster_Rebellion_1534_1535; Peace_of_Augsburg_1555
	- Places (L): Speyer; Augsburg; Muenster; Geneva (interface); Saxony; Nuremberg

	- Wiring
		- I/T → E/D
			- (Schmalkaldic_League) ORGANIZES (Schmalkaldic_War_1546_1547)
			- (Imperial_Diet) PROMULGATES (Augsburg_Interim_1548)
			- (Peace_of_Augsburg_1555) STANDARDIZES (Confessionalization)
			- (Schmalkald_Articles_1537) DEFINES (Lutheran_Reformation)
		- P ↔ M
			- (Menno_Simons) ENDORSES (Anabaptist_Movement)
			- (John_Calvin) ENDORSES (Reformed_Tradition)
		- M ↔ M
			- (Reformed_Tradition) DISPUTES (Lutheran_Reformation)
		- E → L
			- (Princes_Protest_of_Speyer_1529) OCCURS_IN (Speyer)
			- (Schmalkaldic_War_1546_1547) OCCURS_IN (Saxony)
			- (Munster_Rebellion_1534_1535) OCCURS_IN (Muenster)
			- (Peace_of_Augsburg_1555) OCCURS_IN (Augsburg)

## Descriptions (one‑liners)

#### Root and Periods (D)

| Node | G/C | Description |
| --- | --- | --- |
| German_Reformation | G | Curated view of the German (Lutheran) Reformation. |
| Early_Lutheran_Phase_(1517–1521) | C | Initiation from Theses to Worms. |
| Consolidation_and_Confessions_(1521–1530) | C | Translation, city reforms, and Augsburg Confession. |
| Expansion_Conflict_and_Settlement_(1530–1555) | C | Wars, interim, and confessional settlement at Augsburg. |

#### Persons (P)

| Node | G/C | Description |
| --- | --- | --- |
| Martin_Luther | C | Augustinian monk and theologian central to German reform. |
| Johann_Tetzel | C | Indulgence preacher triggering critique. |
| Andreas_Karlstadt | C | Wittenberg reformer engaged in early iconoclasm. |
| Frederick_the_Wise | C | Saxon elector protecting Luther. |
| Charles_V | C | Holy Roman Emperor opposing early reform. |
| Pope_Leo_X | C | Pope excommunicating Luther. |
| Johannes_Eck | C | Theologian debating Luther at Leipzig. |
| Desiderius_Erasmus | C | Humanist scholar influencing reform discourse. |
| Philipp_Melanchthon | C | Systematizer and author of the Augsburg Confession. |
| Thomas_Muenzter | C | Radical reform leader tied to the Peasants’ War. |
| Ulrich_Zwingli | C | Swiss reformer; interface to Swiss Reformation. |
| Huldrych_Zwingli | C | Alternate rendering of Zwingli used in sources. |
| John_Calvin | C | Reformed theologian interfacing via Strasbourg/Geneva. |
| John_Frederick_I_of_Saxony | C | Elector leading the Schmalkaldic League. |
| Maurice_of_Saxony | C | Saxon prince pivotal in mid‑century conflicts. |
| Menno_Simons | C | Former priest shaping Anabaptist tradition. |

#### Institutions (I)

| Node | G/C | Description |
| --- | --- | --- |
| University_of_Wittenberg | C | Academic hub for Luther and colleagues. |
| Augustinian_Order | C | Monastic order forming Luther’s early context. |
| Papacy | C | Roman see and curial authority. |
| Roman_Curial_Courts | C | Ecclesiastical legal apparatus issuing decisions. |
| Holy_Roman_Empire | C | Supra‑regional polity convening imperial diets. |
| Imperial_Diet | C | Assembly of estates deliberating imperial policy. |
| Saxon_Electorate | C | Territorial principality backing reforms. |
| City_Council_Wittenberg | C | Urban magistracy implementing reform. |
| City_Council_Zurich | C | Urban magistracy of Zurich (interface). |
| Schmalkaldic_League | C | Defensive alliance of Lutheran territories. |
| City_Council_Augsburg | C | Urban magistracy hosting imperial diets. |
| Geneva_Consistory | C | Ecclesiastical discipline body (interface). |

#### Texts/Artifacts (T)

| Node | G/C | Description |
| --- | --- | --- |
| Ninety-Five_Theses_1517 | C | Disputation points critiquing indulgences. |
| Leipzig_Debate_Proceedings_1519 | C | Records of the Leipzig disputation. |
| Address_to_the_Christian_Nobility_1520 | C | Call for reform addressing lay rulers. |
| Babylonian_Captivity_of_the_Church_1520 | C | Treatise critiquing sacramental system. |
| Freedom_of_a_Christian_1520 | C | Treatise on faith and Christian liberty. |
| Edict_of_Worms_1521 | C | Imperial edict condemning Luther’s teachings. |
| Luther_Bible_New_Testament_1522 | C | German NT translation completed at Wartburg. |
| Luther_Bible_1534 | C | Complete German Bible translation. |
| Marburg_Articles_1529 | C | Doctrinal articles from Marburg colloquy. |
| Augsburg_Confession_1530 | C | Foundational Lutheran confession at the Diet of Augsburg. |
| Schmalkald_Articles_1537 | C | Lutheran doctrinal articles by Luther. |
| Augsburg_Interim_1548 | C | Imperial interim settlement attempting compromise. |
| Peace_of_Augsburg_1555 | C | Legal settlement establishing cuius regio, eius religio. |

#### Movements (M)

| Node | G/C | Description |
| --- | --- | --- |
| Lutheran_Reformation | C | Reform stream centered on Wittenberg theology. |
| Humanism_in_Germany | C | Intellectual currents shaping reform reception. |
| Indulgence_Critique | C | Opposition to indulgence preaching and abuses. |
| Radical_Reformation | C | Diverse reform beyond magisterial boundaries. |
| Anabaptist_Movement | C | Believer’s baptism and gathered church emphasis. |
| Reformed_Tradition | C | Swiss/Calvinist doctrinal and ecclesial reforms. |
| Iconoclasm_Waves | C | Episodes of image removal during urban reforms. |
| Confessionalization | C | Territorial structuring of religious identity and practice. |
| Papal_Supremacy | C | Doctrinal claim of supreme papal authority. |

#### Events (E)

| Node | G/C | Description |
| --- | --- | --- |
| Posting_of_Theses_1517 | C | Publicating of theses sparking disputation. |
| Leipzig_Debate_1519 | C | Debate between Luther and Eck. |
| Diet_of_Worms_1521 | C | Imperial hearing culminating in the Edict of Worms. |
| Wartburg_Translation_1521_1522 | C | Luther’s seclusion producing the German NT. |
| Peasants_War_1524_1525 | C | Widespread social‑religious uprising. |
| Marburg_Colloquy_1529 | C | Colloquy seeking agreement on the Eucharist. |
| Diet_of_Augsburg_1530 | C | Imperial diet receiving the Augsburg Confession. |
| Princes_Protest_of_Speyer_1529 | C | Formal protest giving origin to the term “Protestant”. |
| Schmalkaldic_War_1546_1547 | C | Conflict between imperial and Schmalkaldic forces. |
| Munster_Rebellion_1534_1535 | C | Radical takeover establishing a theocratic commune. |
| Peace_of_Augsburg_1555 | C | Settlement legalizing Lutheranism in the empire. |

#### Places (L)

| Node | G/C | Description |
| --- | --- | --- |
| Wittenberg | G | Saxon university town and reform hub. |
| Leipzig | G | Saxon city hosting key debates. |
| Worms | G | Imperial city hosting the 1521 diet. |
| Saxony | G | Electoral territory backing reforms. |
| Rome | G | Papal city and curial center. |
| Wartburg | G | Castle where Luther translated the NT. |
| Zurich | G | Swiss urban reform center. |
| Marburg | G | Hessian city hosting the 1529 colloquy. |
| Augsburg | G | Imperial city hosting multiple diets. |
| Thuringia | G | Central German region of social unrest. |
| Speyer | G | Imperial city of the 1529 Protest. |
| Muenster | G | Westphalian city of radical takeover. |
| Geneva | G | Reformed center under Calvin. |
| Nuremberg | G | Imperial city and print hub. |
