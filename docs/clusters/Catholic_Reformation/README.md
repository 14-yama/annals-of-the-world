# Catholic_Reformation (Counter‑Reformation)

A curated cluster for Catholic renewal and response, from late medieval reform currents through Trent and post‑Tridentine consolidation, with interfaces to missions and mysticism.

- Root and Periods (D)
	- Catholic_Reformation (D)
		- Pre-Tridentine_Reform_Currents_(1490s–1545) (D)
		- Council_of_Trent_and_Implementation_(1545–1563) (D)
		- Post-Tridentine_Consolidation_(1563–1600) (D)

- Pre-Tridentine_Reform_Currents_(1490s–1545) (D)
	- Persons (P): Ignatius_of_Loyola; Francis_Xavier; Contarini; Gian_Pietro_Carafa_(Paul_IV); Teresa_of_Avila (interface)
	- Institutions (I): Papacy; Roman_Curia; Society_of_Jesus; Oratory_of_Divine_Love
	- Texts (T): Spiritual_Exercises; Regimini_Militantis_Ecclesiae_1540
	- Movements (M): Catholic_Reform; Mystical_Reform; Mission_Expansion
	- Events (E): Founding_of_Society_of_Jesus_1540; Early_Curial_Committees_for_Reform
	- Places (L): Rome; Avila (interface)

	- Wiring
		- I/T → M
			- (Regimini_Militantis_Ecclesiae_1540) ENABLES (Mission_Expansion)
			- (Spiritual_Exercises) TRANSMITS (Mystical_Reform)
		- P ↔ M
			- (Ignatius_of_Loyola) ENDORSES (Catholic_Reform)
			- (Francis_Xavier) ENDORSES (Mission_Expansion)
		- E → L
			- (Founding_of_Society_of_Jesus_1540) OCCURS_IN (Rome)

- Council_of_Trent_and_Implementation_(1545–1563) (D)
	- Persons (P): Pope_Paul_III; Charles_Borromeo; Roberto_Bellarmino; Pius_IV; Diego_Lainez
	- Institutions (I): Council_of_Trent; Papacy; Roman_Inquisition; Index_Congregation; Seminaries
	- Texts (T): Tridentine_Decrees; Index_Librorum_Prohibitorum_1559; Roman_Catechism_1566
	- Movements (M): Counter_Reformation; Confessionalization; Doctrinal_Standardization
	- Events (E): Council_of_Trent_Sessions_1545_1547; Council_of_Trent_Sessions_1551_1552; Council_of_Trent_Sessions_1562_1563
	- Places (L): Trent; Bologna; Rome

	- Wiring
		- I/T → D/M
			- (Council_of_Trent) PROMULGATES (Tridentine_Decrees)
			- (Roman_Inquisition) CENSORS (Doctrinal_Standardization)
			- (Index_Congregation) PROMULGATES (Index_Librorum_Prohibitorum_1559)
			- (Seminaries) STANDARDIZES (Clerical_Formation)
		- P ↔ M
			- (Charles_Borromeo) ENDORSES (Confessionalization)
			- (Roberto_Bellarmino) ENDORSES (Doctrinal_Standardization)
		- E → L
			- (Council_of_Trent_Sessions_1545_1547) OCCURS_IN (Trent)
			- (Council_of_Trent_Sessions_1551_1552) OCCURS_IN (Trent)
			- (Council_of_Trent_Sessions_1562_1563) OCCURS_IN (Trent)

- Post-Tridentine_Consolidation_(1563–1600) (D)
	- Persons (P): Pius_V; Charles_Borromeo; Teresa_of_Avila (interface); John_of_the_Cross (interface); Matteo_Ricci (interface)
	- Institutions (I): Society_of_Jesus; Discalced_Carmelites (interface); Roman_Curia; Diocesan_Structures
	- Texts (T): Missale_Romanum_1570; Breviarium_Romanum_1568; Constitutions_of_the_Society_of_Jesus
	- Movements (M): Catholic_Reform; Mission_Expansion; Mystical_Reform
	- Events (E): Standardization_of_Roman_Rite_1570; Seminaries_Proliferation; Jesuit_Missions_India_China
	- Places (L): Rome; Milan; Goa; Macau

	- Wiring
		- I/T → M
			- (Missale_Romanum_1570) STANDARDIZES (Catholic_Reform)
			- (Constitutions_of_the_Society_of_Jesus) STANDARDIZES (Mission_Expansion)
		- P ↔ M
			- (Pius_V) ENDORSES (Catholic_Reform)
		- E → L
			- (Standardization_of_Roman_Rite_1570) OCCURS_IN (Rome)
			- (Jesuit_Missions_India_China) OCCURS_IN (Goa)

## Descriptions (one‑liners)

#### Root and Periods (D)

| Node | G/C | Description |
| --- | --- | --- |
| Catholic_Reformation | G | Curated view of Catholic renewal and response. |
| Pre-Tridentine_Reform_Currents_(1490s–1545) | C | Currents of reform before Trent. |
| Council_of_Trent_and_Implementation_(1545–1563) | C | Council sessions and immediate enforcement. |
| Post-Tridentine_Consolidation_(1563–1600) | C | Liturgical/doctrinal consolidation and missions. |

#### Persons (P)

| Node | G/C | Description |
| --- | --- | --- |
| Ignatius_of_Loyola | C | Jesuit founder shaping Catholic renewal. |
| Francis_Xavier | C | Missionary expanding Catholic presence in Asia. |
| Contarini | C | Reformist cardinal in early curial efforts. |
| Gian_Pietro_Carafa_(Paul_IV) | C | Inquisitor/reformer and later pope. |
| Teresa_of_Avila | C | Mystic and reformer of Carmel (interface). |
| Pope_Paul_III | C | Pope convening the Council of Trent. |
| Charles_Borromeo | C | Archbishop implementing Tridentine reform. |
| Roberto_Bellarmino | C | Theologian defending post-Tridentine doctrine. |
| Pius_IV | C | Pope concluding Trent and issuing catechism. |
| Pius_V | C | Pope standardizing the Roman rite. |
| John_of_the_Cross | C | Mystic and co-reformer of Carmel (interface). |
| Matteo_Ricci | C | Jesuit missionary to China (interface). |

#### Institutions (I)

| Node | G/C | Description |
| --- | --- | --- |
| Papacy | C | Roman see and curial authority. |
| Roman_Curia | C | Administrative apparatus of the church. |
| Society_of_Jesus | C | Jesuit order coordinating missions/education. |
| Oratory_of_Divine_Love | C | Lay clerical circle seeking moral reform. |
| Council_of_Trent | C | Ecumenical council defining doctrine/discipline. |
| Roman_Inquisition | C | Tribunal addressing doctrinal offenses. |
| Index_Congregation | C | Office compiling forbidden books lists. |
| Seminaries | C | Institutions for standardized clerical formation. |
| Discalced_Carmelites | C | Reformed Carmelite branch (interface). |
| Diocesan_Structures | C | Local governance implementing reforms. |

#### Texts/Artifacts (T)

| Node | G/C | Description |
| --- | --- | --- |
| Spiritual_Exercises | C | Ignatius’s manual for discernment and formation. |
| Regimini_Militantis_Ecclesiae_1540 | C | Papal bull establishing the Society of Jesus. |
| Tridentine_Decrees | C | Doctrinal/disciplinary canons of Trent. |
| Index_Librorum_Prohibitorum_1559 | C | List of forbidden books. |
| Roman_Catechism_1566 | C | Catechism expounding Tridentine doctrine. |
| Missale_Romanum_1570 | C | Standard Roman liturgical missal. |
| Breviarium_Romanum_1568 | C | Standard Roman breviary. |
| Constitutions_of_the_Society_of_Jesus | C | Governing norms for Jesuit order. |

#### Movements (M)

| Node | G/C | Description |
| --- | --- | --- |
| Catholic_Reform | C | Renewal of discipline, doctrine, and spirituality. |
| Counter_Reformation | C | Response to Protestant expansion. |
| Mystical_Reform | C | Interior renewal via mystical practices. |
| Mission_Expansion | C | Global missionary expansion. |
| Doctrinal_Standardization | C | Harmonization of teaching and catechesis. |
| Confessionalization | C | Structuring of religious life under authorities. |
| Clerical_Formation | C | Training/standardization of clergy. |

#### Events (E)

| Node | G/C | Description |
| --- | --- | --- |
| Founding_of_Society_of_Jesus_1540 | C | Papal approval of the Jesuit order. |
| Early_Curial_Committees_for_Reform | C | Pre-Trent planning for reform. |
| Council_of_Trent_Sessions_1545_1547 | C | Opening period of the council. |
| Council_of_Trent_Sessions_1551_1552 | C | Reopened council sessions. |
| Council_of_Trent_Sessions_1562_1563 | C | Final sessions producing decrees. |
| Standardization_of_Roman_Rite_1570 | C | Missal/Breviary standardization. |
| Seminaries_Proliferation | C | Expansion of seminaries across dioceses. |
| Jesuit_Missions_India_China | C | Missionary endeavors in Asia. |

#### Places (L)

| Node | G/C | Description |
| --- | --- | --- |
| Rome | G | Papal city and curial center. |
| Avila | G | Spanish city associated with mysticism. |
| Trent | G | Alpine city hosting the council. |
| Bologna | G | Italian city where sessions convened. |
| Milan | G | Archdiocesan center of reform. |
| Goa | G | Portuguese colony and mission hub. |
| Macau | G | Chinese port and mission gateway. |
