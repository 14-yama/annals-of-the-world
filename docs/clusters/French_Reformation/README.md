# French_Reformation (Huguenot movement)

A curated cluster for the French Reformation from early evangelical shocks to the Edict of Nantes, with interfaces to Geneva and wider Reformed networks.

- Root and Periods (D)
	- French_Reformation (D)
		- Early_Evangelical_Currents_(1510s–1534) (D)
		- Organization_and_Persecutions_(1534–1562) (D)
		- Wars_of_Religion_and_Settlement_(1562–1598) (D)

- Early_Evangelical_Currents_(1510s–1534) (D)
	- Persons (P): Marguerite_de_Navarre; Jacques_Lefevre_d’Etaples; Guillaume_Farel (interface); John_Calvin (interface); King_Francis_I; Sorbonne_Theologians
	- Institutions (I): Sorbonne; Parlement_of_Paris; Royal_Court_of_France; Geneva_Consistory (interface)
	- Texts (T): Meaux_Bible_Circle_Writings; Royal_Edicts_on_Heresy
	- Movements (M): Evangelical_Humanism_in_France; Reformed_Tradition (interface)
	- Events (E): Evangelical_Preachings_Meaux; Affair_of_the_Placards_1534
	- Places (L): Paris; Meaux

	- Wiring
		- P/I → E
			- (Parlement_of_Paris) CENSORS (Evangelical_Humanism_in_France)
			- (Royal_Court_of_France) RESPONDS_TO (Affair_of_the_Placards_1534)
		- T ↔ M
			- (Meaux_Bible_Circle_Writings) TRANSMITS (Evangelical_Humanism_in_France)
		- E → L
			- (Affair_of_the_Placards_1534) OCCURS_IN (Paris)

- Organization_and_Persecutions_(1534–1562) (D)
	- Persons (P): John_Calvin; Pierre_Viret; Theodore_Beza; Admiral_Gaspard_de_Coligny; Catherine_de_Medici; Duke_of_Guise
	- Institutions (I): National_Synods_of_France; Huguenot_Consistories; Parlement_of_Paris; Catholic_League
	- Texts (T): French_Confession_of_Faith_1559; Edict_of_Saint-Germain_1562
	- Movements (M): Huguenot_Movement; Catholic_League_Movement; Politiques
	- Events (E): Formation_of_French_Consistories; First_National_Synod_1559; Edict_of_Saint-Germain_Passage_1562
	- Places (L): Paris; La_Rochelle; Lyon

	- Wiring
		- I/T → D/M
			- (French_Confession_of_Faith_1559) STANDARDIZES (Huguenot_Movement)
			- (Edict_of_Saint-Germain_1562) ENABLES (Huguenot_Movement)
		- P/I → E
			- (National_Synods_of_France) ORGANIZES (First_National_Synod_1559)
			- (Parlement_of_Paris) CENSORS (Huguenot_Movement)
		- E → L
			- (Formation_of_French_Consistories) OCCURS_IN (La_Rochelle)

- Wars_of_Religion_and_Settlement_(1562–1598) (D)
	- Persons (P): Admiral_Gaspard_de_Coligny; Catherine_de_Medici; Henry_IV; Henry_of_Guise; Theodore_Beza; Duke_of_Anjou
	- Institutions (I): Catholic_League; Royal_Court_of_France; National_Synods_of_France; Huguenot_Consistories; Paris_Parlement
	- Texts (T): Edict_of_Beauvais_1577; Edict_of_Nantes_1598
	- Movements (M): Huguenot_Movement; Catholic_League_Movement; Politiques
	- Events (E): First_War_of_Religion_1562_1563; St_Bartholomews_Day_Massacre_1572; Day_of_the_Barricades_1588; Edict_of_Nantes_Passage_1598
	- Places (L): Paris; La_Rochelle; Nimes

	- Wiring
		- P/I → E
			- (Catholic_League) ORGANIZES (Day_of_the_Barricades_1588)
			- (Royal_Court_of_France) PROMULGATES (Edict_of_Nantes_1598)
		- T ↔ M
			- (Edict_of_Nantes_1598) STANDARDIZES (Politiques)
		- E → L
			- (St_Bartholomews_Day_Massacre_1572) OCCURS_IN (Paris)
			- (Edict_of_Nantes_Passage_1598) OCCURS_IN (Nimes)

## Descriptions (one‑liners)

#### Root and Periods (D)

| Node | G/C | Description |
| --- | --- | --- |
| French_Reformation | G | Curated view of the Huguenot Reformation in France. |
| Early_Evangelical_Currents_(1510s–1534) | C | Evangelical humanism and shocks of 1534. |
| Organization_and_Persecutions_(1534–1562) | C | Consistorial networks and pressures. |
| Wars_of_Religion_and_Settlement_(1562–1598) | C | Civil wars culminating in the Edict of Nantes. |

#### Persons (P)

| Node | G/C | Description |
| --- | --- | --- |
| Marguerite_de_Navarre | C | Royal patron fostering evangelical circles. |
| Jacques_Lefevre_d’Etaples | C | Humanist translator and exegete. |
| Guillaume_Farel | C | Evangelist linking French and Swiss reforms. |
| John_Calvin | C | Reformer whose networks shaped French churches. |
| King_Francis_I | C | Monarch managing early evangelical tensions. |
| Sorbonne_Theologians | C | Theological faculty opposing innovations. |
| Pierre_Viret | C | Evangelist/organizer aiding French congregations. |
| Theodore_Beza | C | Theologian and leader liaising with France. |
| Admiral_Gaspard_de_Coligny | C | Huguenot leader and royal advisor. |
| Catherine_de_Medici | C | Royal figure seeking balances amid conflicts. |
| Duke_of_Guise | C | Catholic magnate opposing Huguenots. |
| Henry_IV | C | Monarch issuing the Edict of Nantes. |
| Henry_of_Guise | C | Catholic League leader in late wars. |
| Duke_of_Anjou | C | Royal actor during wars of religion. |

#### Institutions (I)

| Node | G/C | Description |
| --- | --- | --- |
| Sorbonne | C | Theological faculty shaping condemnations. |
| Parlement_of_Paris | C | Judicial body enforcing religious policy. |
| Royal_Court_of_France | C | Monarchical governance structures. |
| Geneva_Consistory | C | Ecclesiastical discipline body (interface). |
| National_Synods_of_France | C | Representative assemblies of Reformed churches. |
| Huguenot_Consistories | C | Local governing bodies of Reformed congregations. |
| Catholic_League | C | Catholic confederation resisting Huguenots. |
| Paris_Parlement | C | Judicial body in Paris (duplicate naming clarified). |

#### Texts/Artifacts (T)

| Node | G/C | Description |
| --- | --- | --- |
| Meaux_Bible_Circle_Writings | C | Early evangelical writings associated with Meaux. |
| Royal_Edicts_on_Heresy | C | Edicts regulating/penalizing heresy. |
| French_Confession_of_Faith_1559 | C | Confession adopted by French churches. |
| Edict_of_Saint-Germain_1562 | C | Limited toleration enabling worship. |
| Edict_of_Beauvais_1577 | C | Royal pronouncement during late wars. |
| Edict_of_Nantes_1598 | C | Settlement granting limited rights to Huguenots. |

#### Movements (M)

| Node | G/C | Description |
| --- | --- | --- |
| Evangelical_Humanism_in_France | C | Humanist‑driven evangelical currents. |
| Reformed_Tradition | C | Swiss/Calvinist doctrinal and ecclesial reforms. |
| Huguenot_Movement | C | French Reformed communities and politics. |
| Catholic_League_Movement | C | Catholic coalition mobilization. |
| Politiques | C | Moderates prioritizing civil peace. |

#### Events (E)

| Node | G/C | Description |
| --- | --- | --- |
| Evangelical_Preachings_Meaux | C | Early evangelical activities around Meaux. |
| Affair_of_the_Placards_1534 | C | Anti‑mass placards crisis provoking repression. |
| Formation_of_French_Consistories | C | Organization of Reformed congregations. |
| First_National_Synod_1559 | C | First nationwide synod of French churches. |
| Edict_of_Saint-Germain_Passage_1562 | C | Enactment of limited toleration. |
| First_War_of_Religion_1562_1563 | C | Outbreak of civil conflict over religion. |
| St_Bartholomews_Day_Massacre_1572 | C | Mass killings of Huguenots in Paris. |
| Day_of_the_Barricades_1588 | C | Paris uprising led by the League. |
| Edict_of_Nantes_Passage_1598 | C | Formalization of settlement by Henry IV. |

#### Places (L)

| Node | G/C | Description |
| --- | --- | --- |
| Paris | G | Royal and ecclesiastical capital. |
| Meaux | G | Site of early evangelical circle. |
| La_Rochelle | G | Huguenot stronghold and port. |
| Lyon | G | Commercial city with Reformed presence. |
| Nimes | G | Southern city notable in conflicts. |
