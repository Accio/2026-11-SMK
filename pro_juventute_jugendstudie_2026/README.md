# Sorgen Jugendlicher in der Schweiz: Themen- und Lösungsnetzwerk
 
Jitao David Zhang, Analyse mit Hilfe von Claude: https://claude.ai/share/9f4e55d6-bce8-4845-b171-d01a36114894

**Methodik, Daten und Referenzen zu Netzwerk A (Themen), Netzwerk B (Ansätze) und Netzwerk B-interdisziplinär (Fachgebiete → Ansätze → Themen)**
 
Stand: 1. November 2026
 
---
 
## 1. Überblick
 
| | Netzwerk A | Netzwerk B | Netzwerk B-interdisziplinär |
|---|---|---|---|
| Inhalt | Verbindungen zwischen 21 Sorgen-Themen | 6 Ansätze → 6 Themencluster | 14 Fachgebiete → 7 interdisziplinäre Ansätze → 6 Themencluster |
| Datei | `netzwerk_A_themen_5x5.pdf` | `netzwerk_B_ansaetze_5x5.pdf` | `netzwerk_B_interdisziplinaer_5x5.pdf` |
| Skript | `netzwerk_a_5x5.py` | `netzwerk_b_5x5.py` | `netzwerk_b_interdisziplinaer_5x5.py` |
| Format | 5 × 5 Zoll, PDF | 5 × 5 Zoll, PDF | 5 × 5 Zoll, PDF, ohne Legende |
| Knotengrösse | % «ziemlich» oder «sehr» besorgt, pro Thema | mittlerer % pro Cluster | Fachgebiete: Anzahl Ansätze; Cluster: mittlerer % |
| Linienstärke | Evidenz für den Zusammenhang | Evidenz für die Wirkung des Ansatzes | Ansatz → Thema: Evidenz; Fachgebiet → Ansatz: einheitlich grau |
 
**Wichtig:** Nur die Knotengrössen stammen aus den Studiendaten. Die Verbindungen sind eine inhaltliche Einschätzung, die anschliessend an Fachliteratur und Berichten geprüft wurde. Die Jugendstudie veröffentlicht keine Korrelationen zwischen den einzelnen Sorgen-Items.
 
---
 
## 2. Datengrundlage
 
### 2.1 Quelle
 
Pro Juventute (2026). *Pro Juventute Jugendstudie 2026. Umgang mit Stress, Krisen, Mediennutzung und Resilienz bei Jugendlichen und jungen Erwachsenen in der Schweiz.* In Zusammenarbeit mit der Kinder- und Jugendpsychiatrie der Psychiatrischen Universitätsklinik Zürich (KJPP) und YouGov Schweiz. Veröffentlicht am 16.03.2026.
 
- **Stichprobe:** 960 gültige Interviews, 14 bis 25 Jahre, Deutschschweiz, Westschweiz und Tessin
- **Erhebung:** 26.08.2025 bis 02.10.2025, online, YouGov-Schweiz-Panel
- **Gewichtung:** nach Region und Geschlecht, repräsentativ für die Altersgruppe
- **Verwendete Daten:** Abbildung 4 (S. 14), Gesamtgruppe. Gezählt sind die Antworten «ziemlich» und «sehr» auf die Frage, worüber man sich in den letzten sechs Monaten Sorgen gemacht hat.
### 2.2 Kontrolle der Werte
 
Alle 21 Werte aus Abbildung 4 wurden mit Tabelle 5 (S. 16) verglichen, indem die Spalten «ziemlich» und «sehr» addiert wurden. Die Abweichungen betragen höchstens 0.1 Prozentpunkte und erklären sich durch Rundung.
 
### 2.3 Themen, Kurzbezeichnungen und Cluster
 
| Kurzbezeichnung | Originalformulierung (gekürzt) | % | Cluster |
|---|---|---|---|
| Kriege | Kriege auf der Welt (Ukraine, Gaza etc.) | 39.7 | Krieg & Sicherheit |
| Kriminalität, Gewalt | Steigende Kriminalität/Gewaltzunahme | 29.6 | Krieg & Sicherheit |
| Flüchtlingskrise | Flüchtlingskrise, Flüchtlinge | 20.6 | Krieg & Sicherheit |
| Unsicherheit CH | Zunehmende Unsicherheit in der Schweiz bei Krisen in der Welt | 19.6 | Krieg & Sicherheit |
| Weltpolitik, Krisen | Politische Entwicklungen in der Welt, Krisen | 35.4 | Politik & Demokratie |
| Antidemokratisch | Antidemokratische Entwicklungen, Terrorismus, Rechtsextremismus | 29.9 | Politik & Demokratie |
| Polarisierung CH | Menschen mit anderer Meinung können nicht mehr miteinander reden | 23.3 | Politik & Demokratie |
| Politik Schweiz | Politische Entwicklung in der Schweiz | 15.1 | Politik & Demokratie |
| Ungerechtigkeit | Ungerechtigkeit auf der Welt, Schere zwischen Arm und Reich | 30.7 | Gerechtigkeit & Toleranz |
| Sexismus | Sexismus, Benachteiligung oder Gewalt gegenüber Frauen | 29.2 | Gerechtigkeit & Toleranz |
| Rassismus | Rassismus | 23.7 | Gerechtigkeit & Toleranz |
| Fehlende Toleranz | Fehlende Toleranz für Menschen, die anders denken oder fühlen | 20.0 | Gerechtigkeit & Toleranz |
| Fake News, KI | Verfälschung (z. B. Fake News, KI) | 30.0 | Digitale Welt |
| Digitale Macht | Zunehmende Macht der digitalen Welt | 20.9 | Digitale Welt |
| Zukunft allgemein | Zukunft allgemein | 35.8 | Wirtschaft & Zukunft |
| Wohnkosten | Fehlender Wohnraum/Wohnkosten in der Schweiz | 22.6 | Wirtschaft & Zukunft |
| Wirtschaft, Inflation | Wirtschaftskrisen, Inflation | 20.3 | Wirtschaft & Zukunft |
| Renten | Rentensystem / unsichere Rente für junge Menschen | 18.9 | Wirtschaft & Zukunft |
| Klimawandel | Klimawandel (Erderwärmung, Naturkatastrophen) | 31.6 | Umwelt & Gesundheit |
| Artensterben | Artensterben, Naturschutz | 25.5 | Umwelt & Gesundheit |
| Pandemien | Rückkehr von COVID-19 oder neue Pandemien | 4.7 | Umwelt & Gesundheit |
 
**Labels in Netzwerk A (5 × 5):** Wegen des kleineren Formats sind die Labels in Netzwerk A weiter gekürzt: Politik Schweiz → Politik CH, Polarisierung CH → Polarisierung, Weltpolitik, Krisen → Weltpolitik, Antidemokratisch → Extremismus, Unsicherheit CH → Unsicherheit, Flüchtlingskrise → Flüchtlinge, Kriminalität, Gewalt → Gewalt, Fehlende Toleranz → Intoleranz, Wirtschaft, Inflation → Inflation, Zukunft allgemein → Zukunft. In den Tabellen dieses Dokuments stehen weiterhin die längeren Kurzbezeichnungen.
 
**Clusterbildung:** Die 21 Themen wurden nach inhaltlicher Ähnlichkeit von Hand in 6 Cluster gruppiert. Es wurde kein statistisches Verfahren verwendet, weil keine Daten auf Personenebene vorliegen. Zwei Zuordnungen sind Ermessenssache: die Flüchtlingskrise hätte auch zu «Politik & Demokratie» passen können, und «Zukunft allgemein» hätte ein eigenes Cluster sein können.
 
**Cluster-Mittelwerte**, ungewichtetes Mittel der Themen, verwendet für die Knotengrösse in Netzwerk B:
 
| Cluster | Mittelwert % |
|---|---|
| Krieg & Sicherheit | 27.4 |
| Politik & Demokratie | 25.9 |
| Gerechtigkeit & Toleranz | 25.9 |
| Digitale Welt | 25.5 |
| Wirtschaft & Zukunft | 24.4 |
| Umwelt & Gesundheit | 20.6 |
 
---
 
## 3. Methodik
 
### 3.1 Vorgehen
 
1. **Daten extrahieren:** Die Werte aus Abbildung 4 wurden übernommen und mit Tabelle 5 abgeglichen.
2. **Cluster bilden:** Die Themen wurden nach Inhalt in 6 Cluster gruppiert.
3. **Erste Fassung der Verbindungen:** Die Verbindungen zwischen Themen (Netzwerk A) und zwischen Ansätzen und Clustern (Netzwerk B) wurden zuerst aus inhaltlichem Wissen entworfen.
4. **Faktencheck:** Jede Verbindung wurde mit Web-Recherche geprüft. Gesucht wurde nach Meta-Analysen, systematischen Reviews, Berichten internationaler Gremien (IPCC, IPBES, UNHCR, EZB, V-Dem) sowie Quellen von Bund, Kantonen, Hochschulen und anerkannten Fachstellen in der Schweiz.
5. **Evidenz einstufen:** Jede Verbindung erhielt eine Stufe auf einer vierstufigen Skala (siehe 3.2).
6. **Überarbeiten:** Verbindungen wurden je nach Ergebnis abgeschwächt, umbenannt oder neu aufgenommen. Wo die Literatur eine umgekehrte Richtung nahelegt, ist das in Abschnitt 4 vermerkt.
### 3.2 Evidenzskala
 
| Stufe | Bedeutung | Darstellung |
|---|---|---|
| **stark** | Meta-Analyse experimenteller Studien, Bewertung eines internationalen Gremiums mit hoher Sicherheit, oder amtliche Statistik, die den Zusammenhang direkt zeigt | dicke dunkle Linie |
| **mittel** | Meta-Analyse mit schwächeren oder uneinheitlichen Effekten, systematischer Review mit gemischter Kausalität, Modellrechnung oder wiederholte Befragung | mittlere dunkle Linie |
| **schwach** | einzelne Beobachtungs- oder Querschnittsstudie, Einschätzung einer Fachstelle ohne Ursachenanalyse, oder gemeinsames Muster in den Daten der Jugendstudie | dünne dunkle Linie |
| **ungeprüft** | plausibel oder inhaltlich überlappend, im Faktencheck aber nicht eigens belegt | dünne graue Linie |
 
**Grenze dieser Skala:** Die Einstufung ist eine qualitative Einschätzung, kein formales Verfahren wie GRADE. Sie wurde von einer Person vorgenommen, ohne unabhängige Zweitbeurteilung.
 
### 3.3 Darstellung
 
- **Software:** Python 3, matplotlib 3.11; Schrift Liberation Sans (metrisch wie Arial)
- **Format:** alle drei Netzwerke 5 × 5 Zoll, nur PDF mit eingebetteter, editierbarer Schrift (TrueType, `pdf.fonttype: 42`)
- **Schriftgrösse:** mindestens 12 pt für alle Texte
- **Stil:** angelehnt an ggplot2 `theme_minimal`
- **Farben:** ColorBrewer **Set2**, eine Farbe pro Cluster, in allen Grafiken gleich:
| Cluster | Farbe |
|---|---|
| Krieg & Sicherheit | #66C2A5 |
| Politik & Demokratie | #FC8D62 |
| Gerechtigkeit & Toleranz | #8DA0CB |
| Digitale Welt | #E78AC3 |
| Wirtschaft & Zukunft | #A6D854 |
| Umwelt & Gesundheit | #FFD92F |
 
- **Knotenfläche:** proportional zum Prozentwert (Fläche in pt² = 7 × % in Netzwerk A, 10 × % in Netzwerk B, 8 × % in Netzwerk B-interdisziplinär)
- **Lesbarkeit:** In Netzwerk A sind die Clustertitel dunkel statt farbig, weil gelbe und hellgrüne Schrift auf Weiss schlecht lesbar ist. In Netzwerk B sind die «ungeprüften» Linien weniger transparent, damit helle Set2-Farben sichtbar bleiben.
---
 
## 4. Netzwerk A: Verbindungen zwischen den Themen
 
32 Verbindungen: 8 stark, 8 mittel, 10 schwach, 6 ungeprüft. Drei Verbindungen kamen durch den Faktencheck neu dazu (mit **neu** markiert).
 
| Verbindung | Evidenz | Begründung | Quelle |
|---|---|---|---|
| Kriege – Flüchtlingskrise | stark | Ende 2025 waren 117.8 Mio. Menschen vertrieben, vor allem durch Konflikt, Verfolgung und Gewalt | [1] |
| Kriege – Wirtschaft, Inflation | stark | Energie und Nahrung machten 2022 mehr als zwei Drittel der Rekordinflation im Euroraum aus; der Krieg hat sie stark verschärft | [2] |
| Klimawandel – Artensterben | stark | gemeinsame menschliche Treiber | [3] |
| Klimawandel – Ungerechtigkeit | stark | Klimafolgen treffen marginalisierte Gruppen überproportional (hohe Sicherheit) | [4] |
| Klimawandel – Zukunft allgemein | stark | 75 % der 16- bis 25-Jährigen in 10 Ländern finden die Zukunft beängstigend (rund 10'000 Befragte) | [5] |
| Klimawandel – Pandemien (**neu**) | stark | Was Klimawandel und Biodiversitätsverlust antreibt, treibt auch das Pandemierisiko | [3] |
| Artensterben – Pandemien | stark | Landnutzungswandel erhöht den Kontakt zwischen Wildtieren, Nutztieren und Menschen | [3] |
| Sexismus – Kriminalität, Gewalt | stark | 2025: 34 Tötungen im häuslichen Bereich, rund drei Viertel der Opfer Frauen; das Item umfasst ausdrücklich Gewalt gegen Frauen | [6] |
| Kriege – Weltpolitik, Krisen | mittel | Nur 18 % sind optimistisch für die Weltpolitik, der tiefste Wert seit 2015; die Studie führt das auf die Kriege in der Ukraine und in Gaza zurück | [7] |
| Kriege – Unsicherheit CH | mittel | wie oben; trotzdem fühlen sich 92 % in der Schweiz sicher | [7] |
| Weltpolitik – Unsicherheit CH | mittel | wie oben | [7] |
| Weltpolitik – Antidemokratisch | mittel | Fast ein Viertel der Länder wird autokratischer, darunter etablierte Demokratien | [8] |
| Polarisierung CH – Digitale Macht | mittel | Review über fast 500 Arbeiten: digitale Medien gehen in etablierten Demokratien mit mehr Polarisierung und Populismus und weniger Vertrauen einher | [9] |
| Ungerechtigkeit – Wirtschaft, Inflation | mittel | Das ärmste Einkommensfünftel hatte eine um rund 1.1 Prozentpunkte höhere Teuerung (Modellrechnung) | [10] |
| Wirtschaft, Inflation – Wohnkosten | mittel | Höherer Referenzzinssatz plus Teuerung: Mieten bis April 2024 um bis zu 7 % höher | [11] |
| Kriminalität, Gewalt – Unsicherheit CH | mittel | Mehr Opfererfahrungen; nachts allein im Quartier fühlen sich 83.1 % sicher (2022: 87.6 %) | [12] |
| Klimawandel – Flüchtlingskrise | schwach | **abgeschwächt:** Umweltmigration findet meist innerhalb des Landes oder der Region statt, nicht als grenzüberschreitende Flucht | [13] |
| Polarisierung CH – Fake News, KI | schwach | **Richtung fraglich:** Polarisierung und Misstrauen gelten eher als Ursache von Desinformation denn als deren Folge | [14] |
| Antidemokratisch – Fake News, KI | schwach | Desinformation ist im Pressetext von V-Dem nicht erwähnt; die Wirkung von Desinformation wird oft überschätzt | [8], [14] |
| Polarisierung CH – Fehlende Toleranz | schwach | Der Zusammenhang zwischen Polarisierung und Demokratieabbau ist unklar | [15] |
| Polarisierung CH – Politik Schweiz | schwach | Die Fraktionsgeschlossenheit ist seit 2003 gestiegen, die Polarisierung zuletzt nur moderat | [16] |
| Polarisierung CH – Rassismus (**neu**) | schwach | 1'211 gemeldete Rassismusfälle 2024 (fast +40 %); die Fachstellen nennen Polarisierung als Hauptgrund | [17] |
| Kriege – Rassismus (**neu**) | schwach | wie oben; als zweiter Grund wird die geopolitische Lage genannt | [17] |
| Renten – Zukunft allgemein | schwach | Gemeinsames Altersmuster in der Jugendstudie: beide Sorgen steigen mit dem Alter (Tabelle A2) | [0] |
| Wohnkosten – Zukunft allgemein | schwach | wie oben | [0] |
| Sexismus – Rassismus | schwach | Beide Sorgen sind bei jungen Frauen und bei Jugendlichen mit Migrationshintergrund häufiger (Tabellen 5 und B5) | [0] |
| Antidemokratisch – Rassismus | ungeprüft | inhaltlich überlappend | – |
| Antidemokratisch – Fehlende Toleranz | ungeprüft | inhaltlich überlappend | – |
| Fake News, KI – Digitale Macht | ungeprüft | inhaltlich überlappend | – |
| Rassismus – Fehlende Toleranz | ungeprüft | inhaltlich überlappend | – |
| Ungerechtigkeit – Wohnkosten | ungeprüft | plausibel, nicht geprüft | – |
| Wirtschaft, Inflation – Renten | ungeprüft | plausibel, nicht geprüft | – |
 
**Gestrichen** gegenüber der ersten Fassung: «Polarisierung CH – Flüchtlingskrise» und «Renten – Politik Schweiz». Beide wurden schon beim Layout entfernt, weil die Linien sehr lang waren und keinen eigenständigen Zusammenhang abbildeten.
 
---
 
## 5. Netzwerk B: Ansätze und Themencluster
 
### 5.1 Kodierung
 
- **Ebene des Ansatzes** (Quadrat): Politik (schwarz), Schule (grau), Individuum/Umfeld (weiss)
- **Art der Wirkung:** durchgezogen = setzt am Thema an; gestrichelt = stärkt den Umgang mit der Sorge
- **Linienstärke:** Evidenzskala wie in Abschnitt 3.2
### 5.2 Verbindungen
 
| Ansatz | Ebene | Cluster | Art | Evidenz | Befund | Quelle |
|---|---|---|---|---|---|---|
| Medien- und KI-Kompetenz | Schule | Digitale Welt | Thema | stark | Meta-Analyse über 49 Experimente (N > 81'000): Widerstandskraft gegen Desinformation d = 0.60, stärker bei mehreren Sitzungen. Medienkompetenz ist auch ein Schwerpunkt des BAG | [18], [19] |
| Antidiskriminierung, Begegnung | Politik | Gerechtigkeit & Toleranz | Thema | mittel | 27 randomisierte Studien: Kontakt baut Vorurteile meist ab, bei ethnischen und rassistischen Vorurteilen deutlich schwächer | [20] |
| Politische Bildung, Mitsprache | Schule | Politik & Demokratie | Thema | schwach | Panelstudie: politische Bildung geht mit mehr Beteiligung einher, am stärksten durch Mitarbeit im Schülerrat. Wirkung auf Sorgen nicht untersucht | [21] |
| Dosierter News-Konsum | Individuum | Krieg & Sicherheit | Umgang | schwach | Die AAP empfiehlt, Push-Meldungen abzuschalten und Quellen bewusst zu wählen; sie stützt sich auf korrelative Studien. Konstruktive Nachrichten verbessern in 13 von 14 Experimenten die Stimmung | [22], [23] |
| Dosierter News-Konsum | Individuum | Umwelt & Gesundheit | Umgang | schwach | Mehr COVID-News über Social Media hängt mit Depression und Angst bei 10- bis 24-Jährigen zusammen (systematischer Review, zitiert bei der AAP) | [22] |
| Kollektives Engagement | Individuum | Umwelt & Gesundheit | Umgang | schwach | **umbenannt:** Nur kollektives, nicht individuelles Handeln schwächt den Zusammenhang zwischen Klimaangst und Depression ab (n = 284, Querschnitt). Ein Scoping-Review (10 Studien) nennt die Evidenz zu bürgerschaftlichem Engagement vorläufig | [24], [25] |
| Wohnraum, Lehrstellen, Vorsorge | Politik | Wirtschaft & Zukunft | Thema | schwach | Die EKKJ fordert strukturelle Massnahmen an den Lebensbedingungen. In der Jugendstudie korrelieren finanzielle Sorgen mit schlechterem Befinden (r = −0.40). Wirkungsstudien wurden keine gefunden | [26], [0] |
| Dosierter News-Konsum | Individuum | Politik & Demokratie | Umgang | ungeprüft | – | – |
| Kollektives Engagement | Individuum | Gerechtigkeit & Toleranz | Thema | ungeprüft | – | – |
| Kollektives Engagement | Individuum | Krieg & Sicherheit | Thema | ungeprüft | – | – |
| Politische Bildung, Mitsprache | Schule | Wirtschaft & Zukunft | Thema | ungeprüft | – | – |
| Politische Bildung, Mitsprache | Schule | Umwelt & Gesundheit | Thema | ungeprüft | – | – |
| Antidiskriminierung, Begegnung | Politik | Politik & Demokratie | Thema | ungeprüft | – | – |
| Antidiskriminierung, Begegnung | Politik | Krieg & Sicherheit | Thema | ungeprüft | – | – |
| Medien- und KI-Kompetenz | Schule | Politik & Demokratie | Thema | ungeprüft | – | – |
| Medien- und KI-Kompetenz | Schule | Gerechtigkeit & Toleranz | Thema | ungeprüft | – | – |
 
### 5.3 Geprüft, aber nicht in der Grafik
 
Diese Ansätze wirken auf alle Cluster gleichermassen. Sie wurden aus der Grafik genommen, damit sie übersichtlich bleibt.
 
| Ansatz | Evidenz | Befund | Quelle |
|---|---|---|---|
| Psychotherapie | stark | 447 Studien, über 30'000 Jugendliche: mittlerer Effekt von 0.46, nach rund 11 Monaten noch 0.36 | [27] |
| Schulische Präventionsprogramme | mittel | 118 Studien: kleine Effekte auf Depression (g = 0.21) und Angst (g = 0.18); gezielte Programme für Risikogruppen wirken besser als Programme für alle | [28] |
| Elternbeziehung | schwach | Jugendstudie: Korrelation mit psychischer Gesundheit r = .45 und mit Befinden r = .52; die Ursache-Wirkungs-Richtung ist offen | [0] |
| Telefonberatung (z. B. 147) | nicht bewertet | Es gibt eine systematische Übersicht zu Jugend-Helplines, deren Schlussfolgerungen nicht abgerufen werden konnten | [29] |
 
**Kontext Schweiz:** In der UNICEF-Studie (2021 erhoben) sprachen 29.1 % der 14- bis 19-Jährigen mit niemandem über ihre Probleme. 54.3 % derjenigen mit Anzeichen von Angst oder Depression hatten im Vorjahr keine Fachperson aufgesucht [30].
 
---
 
## 5b. Netzwerk B-interdisziplinär: Fachgebiete, Ansätze und Themen
 
### 5b.1 Auswahl der Ansätze
 
Gesucht wurden Ansätze, die mindestens zwei Fachgebiete verbinden und an mindestens einem Themencluster ansetzen. Jeder Ansatz wurde wie in Abschnitt 3 an Fachliteratur und Schweizer Quellen geprüft.
 
### 5b.2 Ansätze, Fachgebiete und Verbindungen
 
| Ansatz | Fachgebiete | Cluster (Evidenz) | Befund | Quelle |
|---|---|---|---|---|
| Prebunking (Inokulation) | Psychologie, Kommunikation, Informatik | Digitale Welt (stark); Politik & Demokratie, Umwelt & Gesundheit (ungeprüft) | 7 Experimente mit fast 30'000 Personen: 90-Sekunden-Videos verbesserten das Erkennen von Manipulationstechniken deutlich; YouTube-Feldversuch mit 5.4 Mio. erreichten Nutzenden: Erkennung +5 % | [31] |
| Bürgerräte, Deliberation | Politikwissenschaft, Kommunikation | Politik & Demokratie (mittel); Umwelt & Gesundheit (ungeprüft) | Feldexperiment mit über 500 US-Wählenden und Kontrollgruppe: starker Rückgang der Abneigung zwischen politischen Lagern. Schweiz: Bürger:innenrat für Ernährungspolitik 2022 (100 ausgeloste Personen), ohne veröffentlichte Wirkungsevaluation | [32], [41] |
| Grüne Quartiere | Stadtplanung, Ökologie/Klima, Kriminologie, Medizin/Public Health | Krieg & Sicherheit (mittel); Umwelt & Gesundheit (ungeprüft) | Cluster-randomisierte Studie mit 541 Brachflächen in Philadelphia: Begrünung senkte Schüsse um 6.8 %; Anwohnende fühlten sich weniger niedergeschlagen und wertlos | [33], [34] |
| Bystander-Programme | Psychologie, Pädagogik, Gender Studies | Gerechtigkeit & Toleranz (mittel); Krieg & Sicherheit (schwach) | Campbell-Review: mehr Eingreifen, Effekt nimmt nach 6 Monaten ab; kein Effekt auf sexuelle Übergriffe selbst. Schweiz: Aktionsplan Istanbul-Konvention 2022–2026, Massnahme 11 (Projekte an Schulen) | [35], [36] |
| One Health | Tiermedizin, Agrarwissenschaft, Medizin/Public Health, Ökologie/Klima | Umwelt & Gesundheit (schwach) | Von IPBES empfohlen; in der Schweiz koordiniert das BLV ein One-Health-Gremium. Ein Review (29 Studien) findet keine gemessenen Wirkungen auf Zoonosen | [3], [37], [38] |
| Klimabildung (BNE) | Ökologie/Klima, Pädagogik, Psychologie | Umwelt & Gesundheit (schwach, «Umgang»); Gerechtigkeit & Toleranz, Wirtschaft & Zukunft (ungeprüft) | Review über 15 Studien: Bildung, die Wissen, Gefühle und Handeln verbindet, hilft beim Verarbeiten von Klimaangst; gemeinsames Handeln wirkt besser als individuelles | [39] |
| Integrationsagenda Schweiz | Pädagogik, Soziale Arbeit, Ökonomie | Krieg & Sicherheit (schwach); Gerechtigkeit & Toleranz, Wirtschaft & Zukunft (ungeprüft) | Kohorte 2020: 53 % nach fünf Jahren erwerbstätig, 12 Prozentpunkte mehr als Kohorte 2018; keine Vergleichsgruppe, Wirtschaftslage wirkt mit | [40] |
 
**Bewusst nicht verbunden:** «Grüne Quartiere» → Wirtschaft & Zukunft, weil Begrünung die Mieten erhöhen kann (Gentrifizierung).
 
### 5b.3 Fachgebiete
 
14 Fachgebiete, teils zusammengefasst: «Medizin, PH» (Humanmedizin und Public Health) und «Ökologie, Klima» (Ökologie und Klimawissenschaft). «Moderation/Fachexpertise» bei Bürgerräten ist unter Kommunikation eingeordnet. Die Knotengrösse zeigt die Anzahl beteiligter Ansätze; Psychologie, Pädagogik und Ökologie/Klima sind mit je drei Ansätzen die stärksten Brücken.
 
Die Zuordnung der Fachgebiete ist eine inhaltliche Einschätzung und nicht eigens an Quellen geprüft.
 
### 5b.4 Darstellung
 
Keine Legende. Die Ansätze stehen als Kästchen in der Mitte. Einige Linien laufen hinter Kästchen durch, ohne mit ihnen verbunden zu sein (z. B. Prebunking → Umwelt & Gesundheit). Die Linienstärke Ansatz → Thema folgt der Evidenzskala aus Abschnitt 3.2; das sollte in der Bildunterschrift erwähnt werden.
 
---
 
## 6. Grenzen
 
1. **Keine Daten auf Personenebene:** Die Verbindungen sind nicht aus den Antworten der 960 Befragten berechnet. Ein datenbasiertes Netzwerk, etwa mit Korrelationen zwischen allen 21 Items, würde die Einzeldaten von Pro Juventute, KJPP oder YouGov voraussetzen.
2. **Andere Zielgrössen:** Die meisten Studien messen etwas anderes als die Sorge selbst, zum Beispiel Inflation, Vorurteile oder Depression. Ob ein Zusammenhang auch die *Sorgen* Jugendlicher verbindet, ist meist nicht direkt untersucht.
3. **Übertragbarkeit:** Viele Wirkungsstudien stammen aus den USA, Grossbritannien oder dem Euroraum. Schweizer Quellen sind überwiegend Bestandesaufnahmen und Strategien ohne eigene Wirkungsnachweise.
4. **Sekundärquellen:** Einige Befunde stammen aus Zusammenfassungen, Medienberichten oder Pressemitteilungen statt aus den Originalpublikationen, zum Beispiel [5], [7], [11], [16] und [17].
5. **Nicht zugänglich:** Der Bericht 9 von Gesundheitsförderung Schweiz (2022) und einige PubMed-Central-Artikel waren wegen Zugangssperren nicht lesbar.
6. **Interdisziplinäre Ansätze:** Mehrere Befunde stammen aus einzelnen Studien in den USA (Philadelphia, US-Wählende). Die Übertragbarkeit auf die Schweiz ist offen.
7. **Einstufung:** Die Evidenzstufen beruhen auf der Einschätzung einer Person, nicht auf einem formalen Bewertungsverfahren.
---
 
## 7. Referenzen
 
**[0]** Pro Juventute (2026). *Pro Juventute Jugendstudie 2026: Umgang mit Stress, Krisen, Mediennutzung und Resilienz bei Jugendlichen und jungen Erwachsenen in der Schweiz.* Zürich: Stiftung Pro Juventute, mit KJPP (PUK, UZH) und YouGov Schweiz. https://www.projuventute.ch
 
**[1]** UNHCR (2026). *Global Trends: Forced Displacement in 2025.* https://www.unhcr.org/sites/default/files/2026-06/global-trends-report-2025.pdf
 
**[2]** Europäische Zentralbank (2023). *The impact of the war in Ukraine on euro area energy and food prices* (ECB Blog, 24.02.2023). https://www.ecb.europa.eu/press/blog/date/2023/html/ecb.blog20230224~3b75362af3.en.html
 
**[3]** IPBES (2020). *Workshop Report on Biodiversity and Pandemics* (Pressemitteilung, 29.10.2020). https://www.cbd.int/doc/press/2020/pr-2020-10-29-ipbes-en.pdf
 
**[4]** IPCC (2022). *Sixth Assessment Report, Working Group II, Chapter 8: Poverty, Livelihoods and Sustainable Development.* https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-8/
 
**[5]** Hickman, C. et al. (2021). Climate anxiety in children and young people and their beliefs about government responses to climate change: a global survey. *The Lancet Planetary Health*, 5(12). Zusammenfassung: https://grist.org/article/climate-anxiety-study-young-people-think-humanity-is-doomed/
 
**[6]** Bundesamt für Statistik (2026). *Polizeiliche Kriminalstatistik 2025.* Bericht: https://www.srf.ch/news/schweiz/kriminalstatistik-des-bundes-femizide-toetungen-vergewaltigungen-hier-steigen-die-zahlen
 
**[7]** Militärakademie & Center for Security Studies, ETH Zürich (2024). *Sicherheit 2024.* Bericht: https://www.blick.ch/politik/sicherheitsstudie-der-eth-zuerich-zeigt-schweizer-sehen-schwarz-fuer-die-welt-wegen-putin-und-co-id19575498.html
 
**[8]** V-Dem Institute (2026). *Democracy Report 2026* (Pressemitteilung). https://v-dem.net/news/press-release-democratic-backsliding-reaches-western-democracies-with-us-decline-unprecedented/
 
**[9]** Lorenz-Spreen, P., Oswald, L., Lewandowsky, S. & Hertwig, R. (2022). A systematic review of worldwide causal and correlational evidence on digital media and democracy. *Nature Human Behaviour*, 7, 74–101. https://www.mpg.de/19475420/how-dangerous-is-digital-media-for-democracy
 
**[10]** VoxEU/CEPR (2022). The uneven effects of rising energy and consumer prices on poverty and social exclusion in the EU. *VoxEU/CEPR.* https://cepr.org/voxeu/columns/uneven-effects-rising-energy-and-consumer-prices-poverty-and-social-exclusion-eu
 
**[11]** Blick (01.06.2023). Referenzzinssatz steigt erstmals seit 15 Jahren. https://www.blick.ch/wirtschaft/referenzzinssatz-steigt-erstmals-seit-15-jahren-jetzt-hagelts-happige-miet-erhoehungen-id18626520.html
 
**[12]** ZHAW & Universität St. Gallen (2026). *Crime Survey 2025.* https://www.zhaw.ch/de/ueber-uns/aktuell/news/detailansicht-news/event-news/crime-survey-2025-mehr-menschen-in-der-schweiz-erleben-straftaten
 
**[13]** Hoffmann, R., Dimitrova, A., Muttarak, R., Crespo Cuaresma, J. & Peisker, J. (2020). A meta-analysis of country-level studies on environmental change and migration. *Nature Climate Change*, 10, 904–912. Zusammenfassung: https://www.oeaw.ac.at/news/environmental-migration-how-climate-change-increases-migration
 
**[14]** Altay, S., Berriche, M. & Acerbi, A. (2023). Misinformation on Misinformation: Conceptual and Methodological Challenges. *Social Media + Society*, 9(1). Zusammenfassung: https://www.psypost.org/new-research-highlights-the-misinformation-on-misinformation-research
 
**[15]** Druckman, J. N. & Levy, J. (2021). *Affective Polarization in the American Public.* IPR Working Paper WP-21-27, Northwestern University. https://www.ipr.northwestern.edu/our-work/working-papers/2021/wp-21-27.html
 
**[16]** Le News (20.02.2026). Political polarisation on the rise in Switzerland since 1990. https://lenews.ch/2026/02/20/political-polarisation-on-the-rise-in-switzerland-since-1990/
 
**[17]** EKR, humanrights.ch & Beratungsnetz für Rassismusopfer (2025). *Rassismusvorfälle 2024.* Bericht: https://www.srf.ch/news/schweiz/rassismus-in-der-schweiz-rassismus-meldungen-steigen-2024-sprunghaft-an
 
**[18]** Huang, G., Jia, W. & Yu, W. (2024). Media literacy interventions improve resilience to misinformation: A meta-analytic investigation of overall effect and moderating factors. *Communication Research*, 53(7), 899–926. https://research.polyu.edu.hk/en/publications/media-literacy-interventions-improve-resilience-to-misinformation/
 
**[19]** Bundesamt für Gesundheit. *Psychische Gesundheit von Kindern und Jugendlichen.* https://www.bag.admin.ch/de/psychische-gesundheit-von-kindern-und-jugendlichen
 
**[20]** Paluck, E. L., Green, S. A. & Green, D. P. (2019). The contact hypothesis re-evaluated. *Behavioural Public Policy*, 3(2), 129–158. https://ideas.repec.org/a/cup/bpubpo/v3y2019i02p129-158_00.html
 
**[21]** Dassonneville, R., Quintelier, E., Hooghe, M. & Claes, E. (2012). The relation between civic education and political attitudes and behavior: A two-year panel study among Belgian late adolescents. *Applied Developmental Science*, 16(3), 140–150. https://chairedemocratie.openum.ca/fr/publications/the-relation-between-civic-education-and-political-attitudes-and-behavior/
 
**[22]** American Academy of Pediatrics. *Current events and social media* (Center of Excellence on Social Media and Youth Mental Health). https://aap.org/en/patient-care/media-and-children/center-of-excellence-on-social-media-and-youth-mental-health/qa-portal/qa-portal-library/qa-portal-library-questions/current-events-and-social-media
 
**[23]** Constructive Institute. *Constructive Journalism Works: Research overview.* https://constructiveinstitute.org/research-overview-effects/
 
**[24]** Schwartz, S. E. O., Benoit, L., Clayton, S., Parnes, M. F., Swenson, L. & Lowe, S. R. (2022). Climate change anxiety and mental health: Environmental activism as buffer. *Current Psychology.* https://www.paris-iea.fr/en/fellows/climate-change-anxiety-and-mental-health-environmental-activism-as-buffer-2
 
**[25]** Oubiña López, M. & Gómez-Baya, D. (2025). Interventions to Promote Civic Engagement Among Youth and Its Outcomes on Mental Health: A Scoping Review. *Children (Basel).* https://www.uloyola.es/en/research-transfer/publications/interventions-to-promote-civic-engagement-among-youth-and-its-outcomes-on-mental-health-a-scoping-review-review
 
**[26]** Eidgenössische Kommission für Kinder- und Jugendfragen EKKJ (2024). Positionspapier zur psychischen Gesundheit von Jugendlichen (Medienmitteilung, 21.03.2024). https://www.admin.ch/gov/de/start/dokumentation/medienmitteilungen.msg-id-100482.html
 
**[27]** Weisz, J. R. et al. (2017). What five decades of research tells us about the effects of youth psychological therapy: A multilevel meta-analysis and implications for science and practice. *American Psychologist*, 72(2), 79–117. https://chaamplab.sdsu.edu/_resources/files/weisz-2017.pdf
 
**[28]** Werner-Seidler, A. et al. (2021). School-based depression and anxiety prevention programs: An updated systematic review and meta-analysis. *Clinical Psychology Review*, 89. https://openresearch-repository.anu.edu.au/items/f894e732-2981-4864-b78f-eafbf446aba1
 
**[29]** Mathieu, S. L. et al. (2021). Systematic Review: The State of Research Into Youth Helplines. *Journal of the American Academy of Child and Adolescent Psychiatry*, 60(10), 1190–1233. https://dro.deakin.edu.au/articles/journal_contribution/Systematic_Review_The_State_of_Research_Into_Youth_Helplines/20679568
 
**[30]** UNICEF Schweiz und Liechtenstein (2023). *Studie zur psychischen Gesundheit von Jugendlichen in der Schweiz und Liechtenstein* (Präsentation, BAG). https://www.bag.admin.ch/dam/bag/de/dokumente/npp/kad-ril/kad_2023/KAD_Studie_Mental_Health_UNICEF_2023.pdf.download.pdf/KAD_Studie_Mental_Health_UNICEF_2023.pdf
 
**[31]** Roozenbeek, J., van der Linden, S., Goldberg, B., Rathje, S. & Lewandowsky, S. (2022). Psychological inoculation improves resilience against misinformation on social media. *Science Advances*, 8(34). Zusammenfassung: https://www.cam.ac.uk/stories/inoculateexperiment
 
**[32]** Fishkin, J., Siu, A., Diamond, L. & Bradburn, N. (2021). Is Deliberation an Antidote to Extreme Partisan Polarization? Reflections on «America in One Room». *American Political Science Review*, 115(4). https://deliberation.stanford.edu/publications/journal-articles/deliberation-antidote-extreme-partisan-polarization-reflections
 
**[33]** Branas, C. C. et al. (2018). Citywide cluster randomized trial to restore blighted vacant land and its effects on violence, crime, and fear. *Proceedings of the National Academy of Sciences*, 115(12). Zusammenfassung: https://publichealthpost.org/research/the-greening-of-vacant-lots
 
**[34]** South, E. C. et al. (2018). Effect of greening vacant land on mental health of community-dwelling adults: A cluster randomized trial. *JAMA Network Open*, 1(3). https://eepro.naaee.org/research/eeresearch/effect-greening-vacant-land-mental-health-community-dwelling-adults-cluster
 
**[35]** Kettrey, H. H., Marx, R. A. & Tanner-Smith, E. E. (2019). Effects of bystander programs on the prevention of sexual assault among adolescents and college students: A systematic review. *Campbell Systematic Reviews*, 15(1–2). Zusammenfassung: https://wiareport.com/2021/06/are-campus-bystander-intervention-programs-effective-in-reducing-sexual-assault
 
**[36]** Eidgenössisches Büro für die Gleichstellung von Frau und Mann EBG (2024). *Nationaler Aktionsplan zur Umsetzung der Istanbul-Konvention 2022–2026: Zwischenbericht.* https://www.ebg.admin.ch/dam/en/sd-web/w57ia0s5VTtX/NAP%20IK-Zwischenbericht%2025.11.2025.pdf
 
**[37]** Arredondo-Rivera, M., Barois, Z., Monti, G. E., Steketee, J. & Daburon, A. (2024). Bridging Food Systems and One Health: A key to preventing future pandemics? *One Health*, 18, 100727. https://doaj.org/article/4fc9105ef2c84e02b54b3b701e059411
 
**[38]** Bundesamt für Lebensmittelsicherheit und Veterinärwesen BLV. *One Health.* https://www.blv.admin.ch/de/one-health-de
 
**[39]** Olsen, E. K., Lawson, D. F., McClain, L. R. & Plummer, J. D. (2024). Heads, hearts, and hands: a systematic review of empirical studies about eco/climate anxiety and environmental education. *Environmental Education Research.* https://eepro.naaee.org/research/eeresearch/heads-hearts-and-hands-systematic-review-empirical-studies-about-ecoclimate
 
**[40]** Staatssekretariat für Migration SEM. *Erwerbssituation von vorläufig Aufgenommenen und Flüchtlingen* (Monitoring Integrationsagenda Schweiz). https://www.sem.admin.ch/sem/de/home/integration-einbuergerung/integrationsfoerderung/monitoring/erwerb-va-fl.html
 
**[41]** Biovision, SDSN Schweiz & Landwirtschaft mit Zukunft (2022). *Bürger:innenrat für Ernährungspolitik* (Medienmitteilung, 17.05.2022). https://www.demoscope.ch/fileadmin/files/Medienberichte/Buergerrat_Medienmitteilung.pdf
 
---
 
*Hinweis:* Bei einigen Referenzen wurden Jahrgang, Heft oder Autorennamen ergänzt, ohne sie an der Originalpublikation zu prüfen, insbesondere [5], [9], [13], [14], [24], [31], [32], [33], [34] und [35]. Für eine Publikation bitte gegenprüfen.
