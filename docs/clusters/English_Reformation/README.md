# English_Reformation (Cluster Tree)

Parent root: European_Reformations (M)
Scope: c. 1520s–1600s; England and realms
Boundary: Standalone cluster tree; interfaces to Roman_Catholic_Church, Continental_Reformations, English_Parliament.

## Comprehensive English_Reformation Cluster Tree (Periods, Institutions, Texts, Movements, Events)

- English_Reformation (M)
	- Periods (D)
		- Henrician_Reformation_(c._1527–1547) (D)
			- Persons (P): Henry_VIII; Catherine_of_Aragon; Anne_Boleyn; Thomas_Cranmer; Thomas_More; Pope_Clement_VII
			- Institutions (I): Church_of_England; Papacy; English_Parliament; Ecclesiastical_Courts_England; Royal_Court
			- Texts (T): Act_of_Supremacy_1534; Cranmer_Annulment_Decree; Ten_Articles_1536; Bishops_Book_1537
			- Movements (M): Royal_Supremacy; Humanism_in_England
			- Events (E): Annulment_Proceedings; Break_with_Rome; Act_of_Supremacy_Passage; Dissolution_of_the_Monasteries
			- Places (L): London; Rome
			- Suggested clusters: Henry_VIII_Annulment_and_Royal_Supremacy_1527_1536; Dissolution_of_the_Monasteries_1536_1541
			- Edges (canonical triples)
				- P/I → E
					- (Henry_VIII) PETITIONS (Papacy) — Annulment_Proceedings
					- (Thomas_Cranmer) DECLARES (Annulment_Proceedings)
					- (English_Parliament) PROMULGATES (Act_of_Supremacy_1534)
					- (Royal_Court) ORGANIZES (Dissolution_of_the_Monasteries)
				- I → P
					- (Papacy) EXCOMMUNICATES (Henry_VIII)
				- E → I/D
					- (Act_of_Supremacy_Passage) TRANSFORMS (Church_of_England)
					- (Church_of_England) STANDARDIZES (Royal_Supremacy)
				- D/T ↔ D/T
					- (Royal_Supremacy) REJECTS (Papal_Supremacy)
					- (Ten_Articles_1536) DEFINES (Royal_Supremacy)
				- T ↔ E
					- (Act_of_Supremacy_1534) ENABLES (Act_of_Supremacy_Passage)
				- E → L
					- (Act_of_Supremacy_Passage) OCCURS_IN (London)

		- Edwardian_Reformation_(1547–1553) (D)
			- Persons (P): Edward_VI; Thomas_Cranmer; John_Dudley_(Northumberland)
			- Institutions (I): Church_of_England; Privy_Council
			- Texts (T): Book_of_Common_Prayer_1549; Book_of_Common_Prayer_1552; Forty-Two_Articles_1553
			- Movements (M): Protestant_Doctrine_in_England
			- Events (E): Prayer_Book_Reform; Doctrinal_Articles_Promulgation
			- Places (L): London
			- Suggested clusters: Cranmer_Liturgy_and_Doctrine; Edwardian_Articles
			- Edges (canonical triples)
				- I → T/D
					- (Church_of_England) PROMULGATES (Book_of_Common_Prayer_1549)
					- (Church_of_England) PROMULGATES (Book_of_Common_Prayer_1552)
					- (Church_of_England) PROMULGATES (Forty-Two_Articles_1553)
				- P/I → E
					- (Thomas_Cranmer) LEADS (Prayer_Book_Reform)
					- (Privy_Council) ORGANIZES (Doctrinal_Articles_Promulgation)
				- T ↔ D
					- (Book_of_Common_Prayer_1552) STANDARDIZES (Protestant_Doctrine_in_England)

		- Marian_Restoration_(1553–1558) (D)
			- Persons (P): Mary_I; Reginald_Pole
			- Institutions (I): Roman_Catholic_Church; Church_of_England
			- Texts (T): Heresy_Acts; Pole_Reconciliation_Decrees
			- Movements (M): Catholic_Restoration
			- Events (E): Reconciliation_with_Rome; Heresy_Persecutions
			- Places (L): London; Rome
			- Suggested clusters: Marian_Restoration_and_Persecutions
			- Edges (canonical triples)
				- I → P/T
					- (Roman_Catholic_Church) PARDONS (English_Realm) — reconciliation formula
					- (Roman_Catholic_Church) CENSORS (Protestant_Doctrine_in_England)
				- P/I → E
					- (Mary_I) DECLARES (Reconciliation_with_Rome)
					- (Reginald_Pole) ORGANIZES (Reconciliation_with_Rome)
				- E → D/I
					- (Reconciliation_with_Rome) TRANSFORMS (Church_of_England)
					- (Heresy_Persecutions) CENSORS (Protestant_Doctrine_in_England)

		- Elizabethan_Settlement_(1558–1603) (D)
			- Persons (P): Elizabeth_I; Matthew_Parker
			- Institutions (I): Church_of_England; English_Parliament
			- Texts (T): Act_of_Supremacy_1559; Act_of_Uniformity_1559; Thirty-Nine_Articles_1563
			- Movements (M): Via_Media; Puritan_Movement (interface)
			- Events (E): Settlement_Passage; Articles_Promulgation
			- Places (L): London
			- Suggested clusters: Elizabethan_Settlement_1559; Thirty_Nine_Articles_1563
			- Edges (canonical triples)
				- I → T/D/E
					- (English_Parliament) PROMULGATES (Act_of_Supremacy_1559)
					- (English_Parliament) PROMULGATES (Act_of_Uniformity_1559)
					- (Church_of_England) PROMULGATES (Thirty-Nine_Articles_1563)
				- T ↔ E/D
					- (Act_of_Uniformity_1559) ENABLES (Settlement_Passage)
					- (Thirty-Nine_Articles_1563) STANDARDIZES (Via_Media)

## Interfaces to other clusters
- Roman_Catholic_Church (Papacy, Curia; justice/ordinances)
- Continental_Reformations (Lutheran/Reformed influences)
- English_Parliament (Institutions/Law)

## Typical canonical verbs used
- I → P: EXCOMMUNICATES; PARDONS
- I → T/D: PROMULGATES; CENSORS; APPROVES; STANDARDIZES
- P ↔ P: DIVORCES; ENDORSES; DEBATES; CORRESPONDS_WITH
- P/I → E: ORGANIZES; LEADS; DECLARES; PARTICIPATES_IN
- D/T ↔ D/T: REJECTS; DEFINES; ENABLES; STANDARDIZES
- E → L/I/D: OCCURS_IN; TRANSFORMS; CENSORS

## Data hygiene
- Reuse global nodes (persons, institutions, texts); no duplication.
- Keep interfaces explicit; tag crosslinks where supported (crosslink=true, interface="Reformations").
- Use only verbs from `../../guidelines/relations_vocabulary.md`.

## Change log (cluster‑local)
- 2025‑10‑18: Added comprehensive hierarchical tree, persons, and example edges; interfaces and hygiene sections.

## Cases
- cases/henry_viii_annulment_royal_supremacy_1527_1536.md — Person-centered annulment leading to institutional/doctrinal reconfiguration.

## Suggested subclusters (illustrative)
- Henry_VIII_Annulment_and_Royal_Supremacy_1527_1536
- Dissolution_of_the_Monasteries_1536_1541
- Elizabethan_Settlement_1559

## See also
- ../Early_Christianity/README.md (interface patterns for institutions/law)
- ../Hebrew_Tradition/README.md (ritual/doctrine modeling patterns)
