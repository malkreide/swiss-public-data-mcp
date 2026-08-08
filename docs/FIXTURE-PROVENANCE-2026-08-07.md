# Fixture-Herkunft im Portfolio — Bestandsaufnahme

**Stand: 2026-08-07.** Erhoben read-only über den Git-Proxy; kein Repo wurde
für diese Messung verändert.

Dieser Bericht ist eine **Momentaufnahme und altert**. Das Datum steht deshalb im
Dateinamen und hier: Ohne Zeitpunkt ist eine Bestandsaufnahme nach ein paar
Monaten von einer Vermutung nicht mehr zu unterscheiden — dieselbe Regel, die
der Bericht an den Fixtures misst, gilt für ihn selbst.

## Worum es geht

Ein handgeschriebener Mock kodiert die Annahme seines Autors und kann sie
deshalb **prinzipiell nicht widerlegen**: Produktivcode und Fixture stammen aus
demselben Kopf, derselben Stunde, derselben Lektüre der Doku. Wo beide irren,
irren beide gleich, und die Suite bleibt dauerhaft grün.

Der Katalog-Check [`OPS-009`](https://github.com/malkreide/mcp-audit-skill/blob/main/checks/OPS-009.md)
verlangt deshalb, dass eine Fixture **einmal von der Quelle kam** und dass im
Repo steht, **wann**. Ohne Datum ist «aufgezeichnet» nach zwei Jahren von
«ausgedacht» nicht mehr zu unterscheiden — die Datei sieht gleich aus. Der
Rahmen steht als Regel 5 in [`mcp-data-fidelity`](https://github.com/malkreide/mcp-data-fidelity-skill).

## Ergebnis

| | |
|---|---:|
| Server mit Testsuite | **42** |
| davon mit Aufzeichnungsskript **und** Datum | **11** |
| Inline-Payloads insgesamt | **rund 1 145** |
| mit Live-Test-Markern | 40 |
| davon an einem Zeitplan | 20 |

Zum Zeitpunkt der Erhebung hatte **kein einziger** der 42 Server eine datierte
Fixture-Herkunft. Zehn sind am selben Tag nachgezogen worden, der elfte am
2026-08-08 (siehe «Was daraus geworden ist»).

## Wie gemessen wurde

- **Inline-Payloads** — Vorkommen von `json=`, `text=` und `content=` in
  `test_*.py`. Ein Mass für **Exposition**, nicht für Risiko: Jeder Payload ist
  eine Annahme über die Quelle, die im Repo steht und nie geprüft wurde.
- **Fixture-Dateien** — `*.csv|json|xml|html` unter einem Test-/Fixture-/Datenpfad.
- **Provenienz** — nur `Skript/Datei` zählt: eine `PROVENANCE`-Datei oder ein
  Aufzeichnungsskript. Ein blosses Datum im Testcode zählt **nicht**; die
  Kalibrierung unten sagt, warum.
- **Live** — Dateien mit `pytest.mark.live`, plus ob ein Workflow mit `cron:` sie
  tatsächlich fährt.

**Testdateien und Payloads sind Erhebungswerte, Fixture-Dateien und Provenienz
sind Tagesstand.** Die Rangfolge hat nur als *ein* Messzeitpunkt eine Bedeutung;
würde man die Exposition der nachgezogenen Server nachmessen, verschöbe sich die
Liste, weil das Nachziehen selbst Tests hinzufügt. Bei `swiss-transport-mcp` wäre
das nach dem Nachziehen 17 Testdateien und 27 Payloads statt 14 und 20. Die
Spalten, die den *Zustand* melden — Fixture-Dateien, Provenienz —, stehen
dagegen auf heute; sonst wäre die Tabelle für ihren eigentlichen Zweck blind.

### Zwei Kalibrierungen, offengelegt

Der erste Detektor hat sich zweimal selbst getäuscht, und beides ist genau die
Fehlerklasse, um die es hier geht:

1. Er meldete Provenienz, sobald irgendein README das Wort «aufgezeichnet»
   enthielt. Eine Herkunftsangabe am falschen Ort ist keine.
2. Er meldete «Datum im Test» für einen Server, dessen Fixtures nachweislich
   erfunden waren — die Daten stammten aus der `Stand`-Spalte der Nutzdaten. Das
   Signal ist zurückgestuft und zählt nicht als Beleg.

Gegengeprüft wurde an `zh-education-mcp` vorher/nachher: Nur der behobene Stand
meldet `Skript/Datei`.

**Weggelassen:** eine Spalte «Hinweise auf erfundene Daten». Ihre 64 Treffer im
grössten Server waren `fake_`-Präfixe in Hilfsfunktionsnamen, keine Datenmarker.
Ein Signal, das sich nicht belegen lässt, gehört nicht in einen Befund.

## Rangfolge nach Exposition

| Server | Testdateien | Inline-Payloads | Fixture-Dateien | Provenienz | Live-Tests |
|---|---:|---:|---:|---|---|
| `srgssr-mcp` | 6 | 134 | 0 | keine | 1 Datei(en)+geplant |
| `swisstopo-mcp` | 35 | 133 | 0 | keine | 14 Datei(en)+geplant |
| `bag-health-mcp` ✅ | 3 | 72 | 9 | **datiert** | 1 Datei(en) |
| `swiss-procurement-mcp` | 20 | 72 | 0 | keine | 1 Datei(en)+geplant |
| `swiss-cultural-heritage-mcp` | 3 | 66 | 0 | keine | 1 Datei(en)+geplant |
| `amtsblatt-mcp` | 20 | 64 | 0 | keine | 2 Datei(en)+geplant |
| `swiss-environment-mcp` | 7 | 57 | 0 | keine | 4 Datei(en)+geplant |
| `seco-labor-mcp` | 4 | 47 | 0 | keine | 1 Datei(en)+geplant |
| `register-mcp` ✅ | 6 | 44 | 3 | **datiert** | 2 Datei(en) |
| `zurich-opendata-mcp` ✅ | 16 | 35 | 4 | **datiert** | 3 Datei(en) |
| `swiss-statistics-mcp` ✅ | 2 | 34 | 7 | **datiert** | 1 Datei(en) |
| `meteoswiss-mcp` ✅ | 2 | 33 | 6 | **datiert** | 1 Datei(en) |
| `zh-education-mcp` ✅ | 5 | 31 | 6 | **datiert** | 2 Datei(en)+geplant |
| `termdat-mcp` | 5 | 27 | 0 | keine | 1 Datei(en)+geplant |
| `swiss-road-mobility-mcp` | 12 | 27 | 0 | keine | 3 Datei(en)+geplant |
| `lindas-mcp` | 4 | 24 | 0 | keine | 1 Datei(en)+geplant |
| `wsl-envidat-mcp` ✅ | 5 | 24 | 5 | **datiert** | 2 Datei(en) |
| `swiss-holidays-mcp` | 11 | 21 | 0 | keine | 1 Datei(en)+geplant |
| `swiss-transport-mcp` ✅ | 14 | 20 | 2 | **datiert** | 1 Datei(en) |
| `parlament-mcp` | 5 | 20 | 0 | keine | 2 Datei(en)+geplant |
| `swiss-academic-libraries-mcp` ✅ | 5 | 18 | 10 | **datiert** | 4 Datei(en) |
| `swiss-democracy-mcp` ✅ | 2 | 18 | 3 | **datiert** | 1 Datei(en) |
| `swiss-courts-mcp` | 9 | 16 | 1 | keine | 2 Datei(en)+geplant |
| `swiss-electricity-mcp` ✅ | 8 | 15 | 9 | **datiert** | 1 Datei(en) |
| `swiss-efv-mcp` | 4 | 13 | 0 | keine | 1 Datei(en)+geplant |
| `i14y-mcp` | 4 | 11 | 0 | keine | 1 Datei(en)+geplant |
| `swiss-snb-mcp` | 4 | 11 | 0 | keine | 2 Datei(en) |
| `eth-library-mcp` | 2 | 11 | 0 | keine | keine |
| `fedlex-mcp` | 3 | 9 | 0 | keine | 1 Datei(en) |
| `hn-tech-signal-mcp` | 2 | 6 | 0 | keine | 1 Datei(en) |
| `swiss-energy-mcp` | 5 | 5 | 0 | keine | 1 Datei(en)+geplant |
| `lobbywatch-mcp` | 6 | 5 | 0 | keine | 1 Datei(en) |
| `swiss-ip-mcp` | 1 | 5 | 0 | keine | 1 Datei(en)+geplant |
| `openlex-mcp` | 8 | 4 | 0 | keine | 1 Datei(en)+geplant |
| `swiss-housing-mcp` | 1 | 4 | 0 | keine | 1 Datei(en)+geplant |
| `bag-epl-mcp` | 3 | 3 | 0 | keine | 1 Datei(en) |
| `news-monitor-mcp` | 2 | 2 | 0 | keine | 1 Datei(en) |
| `global-education-mcp` | 2 | 2 | 0 | keine | keine |
| `swiss-culture-mcp` | 1 | 1 | 2 | keine | 1 Datei(en) |
| `bakom-mcp` | 7 | 1 | 0 | keine | 1 Datei(en) |
| `sbb-opendata-mcp` | 1 | 0 | 0 | keine | 1 Datei(en) |
| `swiss-food-safety-mcp` | 1 | 0 | 0 | keine | 1 Datei(en) |

`swiss-public-data-mcp` führt keine Testsuite — es ist das Portfolio-Meta-Repo.

## Wo es am ehesten weh tut

Viele ungeprüfte Annahmen **und** kein Zeitplan, der sie gegen die Quelle hält:

| Server | Payloads | Live |
|---|---:|---|
| `swiss-electricity-mcp` ✅ | 15 | 1 Datei(en) |
| `swiss-snb-mcp` | 11 | 2 Datei(en) |

Von diesen beiden ist `swiss-electricity-mcp` inzwischen nachgezogen — und die
Liste hatte recht, wenn auch nicht aus dem Grund, den sie nennt: Alle drei
ElCom-Tarif-Werkzeuge lieferten seit einer Umstellung der Quelle nichts.
`swiss-snb-mcp` steht weiter offen.

Die Zahl misst Exposition, **nicht** Risiko. Ein Server mit 134 erfundenen
Payloads gegen eine stabile API ist harmloser als einer mit fünf gegen eine
Quelle, die ihre Kopfzeilen wechselt. Der Faktor-100-Fehler in
`zh-education-mcp` steckte in **einer Zelle einer Fixture mit drei Zeilen**.

## Was daraus geworden ist

Elf Server sind nachgezogen worden — zehn am 2026-08-07, der elfte am
2026-08-08. In **sieben** von elf hat allein das Aufzeichnen einen
ausgelieferten Fehler freigelegt:

| Server | PR | Befund |
|---|---|---|
| `zh-education-mcp` | [#41](https://github.com/malkreide/zh-education-mcp/pull/41) | Die Maturitätsquote war um **Faktor 100** zu hoch. Die Quelle publiziert die Spalte bereits in Prozent; die erfundene Fixture schrieb eine Bruchzahl hinein und liess `* 100` plausibel aussehen. |
| `bag-health-mcp` | [#55](https://github.com/malkreide/bag-health-mcp/pull/55), [#56](https://github.com/malkreide/bag-health-mcp/pull/56) | Die Sitemap-Fixture beschrieb eine Form, die es nicht gibt: vier `/de/`-URLs, von denen die Quelle **keine einzige** liefert. Deutsch kommt sprachneutral. Der Zusatzbefund «9 von 12 Indikatoren haben gar keine Datenserie» war eine Fehldeutung meiner eigenen Messung — siehe die Korrektur unten. |
| `register-mcp` | [#49](https://github.com/malkreide/register-mcp/pull/49) | Eine korrekte **HR-Suche war blockiert** — 2 279 587 Treffer über einer Schwelle von 2 000 000, die «weit über jedem plausiblen Einzelfilter» liegen sollte. |
| `zurich-opendata-mcp` | [#84](https://github.com/malkreide/zurich-opendata-mcp/pull/84) | **Kein Befund.** 246 Tests unverändert grün. Der Server sendet `rows` überall explizit; das Aufzeichnen hat es nur belegt. |
| `swiss-statistics-mcp` | [#29](https://github.com/malkreide/swiss-statistics-mcp/pull/29) | **Kein Befund am Server**, drei an den Fixtures: Ein Snapshot ist ein Zeitpunkt, die alte Fixture war zwei (BFS 133 *und* 295 in einer Datei); die Korrespondenz-Fixture beantwortete eine Anfrage mit anderen Parametern, als der Server sendet; falsche Codes und ein gekürzter Titel. |
| `meteoswiss-mcp` | [#42](https://github.com/malkreide/meteoswiss-mcp/pull/42) | **Kein Befund am Server.** Die STAC-Fixture führte 4 Assets, die Quelle liefert 16 — der Selektor, der ausdrücklich jeden Fallback ablehnt, wurde nie gegen die Historik-Dateien geprüft, gegen die es ihn gibt. |
| `wsl-envidat-mcp` | [#24](https://github.com/malkreide/wsl-envidat-mcp/pull/24) | **Kein Befund am Server**, drei an den Fixtures: Die Organisationen `wsl` und `slf` gibt es nicht (`organization_show?id=slf` → HTTP 404); Tags stehen in GROSSBUCHSTABEN statt kleingeschrieben; ein Datensatz hat 42 Felder statt 9, mit `extras`, die die Quelle nicht kennt. |
| `swiss-transport-mcp` | [#31](https://github.com/malkreide/swiss-transport-mcp/pull/31) | **Fünf Befunde am Server**, alle derselben Herkunft: Er spricht an mehreren Stellen OJP **1.0**, wo er 2.0 zu sprechen glaubt. `<n>` statt des Pflichtfelds `<Name>` in jedem `PlaceRef` — damit war jede Reise- und Abfahrtsanfrage ungültig; `<LocationName>` für Ortsnamen, die es in OJP 2.0 innerhalb eines `PlaceRef` gar nicht gibt; `<IncludeRealtimeData>` statt `UseRealtimeData`; der Standort-Parser las nur `StopPlaceName` und verwarf alles andere; Fusswege kamen ohne Start- und Zielnamen zurück. |
| `swiss-academic-libraries-mcp` | [#50](https://github.com/malkreide/swiss-academic-libraries-mcp/pull/50) | **Die Sammlungs-Übersicht meldete ein Zehntel des Bestands als Gesamtzahl.** `ListSets` ist paginiert wie `ListRecords`; gelesen wurde eine Seite. e-rara: 10 statt **105**, e-manuscripta: 10 statt **49**. Der Namensfilter lief danach über diese Reste, so dass eine Sammlung, die es gibt, als «Keine Sammlungen gefunden» zurückkam. |
| `swiss-electricity-mcp` | [#37](https://github.com/malkreide/swiss-electricity-mcp/pull/37) | **Alle drei ElCom-Tarif-Werkzeuge lieferten seit einer Umstellung der Quelle nichts.** LINDAS hat den Prädikat-Namensraum umgebaut: `.../measure/*` gibt es nicht mehr, alles steht unter `.../dimension/*`, und die cube-eigenen Namensräume sind weg. `measure/total` war Pflicht-Tripel in jeder Abfrage — das Ergebnis war deshalb kein Fehler, sondern **HTTP 200 mit null Zeilen**, für jede Gemeinde und jedes Jahr. Zürich hat 291 Beobachtungen im Cube; die Abfrage des Servers fand null. Dazu zwei weitere: vier von fünf Speicherseen-Regionen lieferten unter ihrem eigenen Namen die Schweizer Zahlen, und der Standardschnitt der Zeitreihe traf 52 Zeilen ohne eine einzige Messung, weil die Reihe in die Zukunft läuft. |
| `swiss-democracy-mcp` | [#25](https://github.com/malkreide/swiss-democracy-mcp/pull/25) | **Füllwerte wurden als Parteiparolen ausgegeben.** Swissvotes markiert Fehlendes mit `9999` und `.`; der Code übersetzte die bekannten Codes und reichte den Rest roh durch. **667 der 714 Abstimmungen** betroffen — für die Bundesverfassung von 1848 meldete das Werkzeug `{"FDP": "9999", …}` für alle zehn Parteien, von denen es damals keine gab. |

Die vier Nullbefunde gehören genauso in diese Tabelle wie die sieben Funde. Nach
drei Repos in Folge, die etwas hergaben, wäre die Versuchung gross gewesen, auch
in den übrigen etwas zu finden.

**Die Rangfolge trennt Fund und Nullbefund nicht.** Die sieben ausgelieferten
Fehler liegen auf den Plätzen 3, 9, 13, 19, 21, 22 und 24, die vier Nullbefunde
auf 10, 11, 12 und 17 — verschränkt, nicht gestaffelt. Alle elf stammen zudem aus
den obersten 24 von 42; über die untere Hälfte sagt diese Stichprobe gar nichts.
Das ist kein Mangel der Rangfolge, sondern das, was die Payload-Spalte misst:
Exposition, nicht Risiko. Sie sagt, wie viel ungeprüfte Annahme ein Server
trägt, nicht, ob eine davon falsch ist.

Die vier untersten der elf führen das vor — und alle vier tragen einen Fund.
`swiss-transport-mcp` (Platz 19): Jede Reise- und jede Abfahrtsanfrage war
ungültig. `swiss-academic-libraries-mcp` (Platz 21): Die Sammlungs-Übersicht
meldete ein Zehntel des Bestands als Gesamtzahl. `swiss-democracy-mcp`
(Platz 22): Füllwerte gingen als Parteiparolen hinaus, in 93 % der
Abstimmungen. `swiss-electricity-mcp` (Platz 24, der bisher unterste): Alle drei
Tarif-Werkzeuge antworteten mit null Zeilen — mit 15 Payloads der **kleinste**
Wert unter den elf. Keiner dieser Fehler stand in den Daten — sie standen in der
Frage, im Blättern, im Codebuch und im Namensraum. Davon kann eine
Payload-Zählung nichts wissen.

### Eine Lücke, die offen bleibt

- **Zefix in `register-mcp` ist nicht aufgezeichnet.** Die API verlangt
  `ZEFIX_USER`/`ZEFIX_PASSWORD` und antwortet ohne sie mit HTTP 401. Die Payloads
  stehen weiter als Literale im Testmodul; `PROVENANCE.md` führt sie ausdrücklich
  unter «NICHT aufgezeichnet», statt ihnen ein Datum anzuschreiben, das nicht
  stimmt. Der Zweig im Skript ist fertig.

### Eine Korrektur an diesem Bericht

Die zweite Lücke stand hier so: *«`bag-health-mcp` bietet Indikatoren an, die es
nicht ausliefern kann.»* Sie ist geschlossen
([#56](https://github.com/malkreide/bag-health-mcp/pull/56)) — und beim
Schliessen hat sich gezeigt, dass der Satz falsch war.

Gemessen war: 9 von 12 Obsan-Indikatoren antworteten auf `/g/json` **und**
`/gum/json` je 404. Die Messung stimmt. Der Schluss daraus war meiner: *Sie
haben keine Datenreihe.* Richtig ist: **Sie haben keine, die der Client fragt.**

Eine Obsan-Indikatorseite deklariert, welche API-Varianten es zu ihr gibt —
`kg` nach Kantonen, `ag` nach Altersklasse, `sd` nach sozialer Lage, `g`
national, dazu drei weitere — jeweils mit vollständiger Adresse. Der Client hat
diese Liste nie gelesen und zwei feste Endungen geraten. Über 60 Indikatoren am
2026-08-08 nachgemessen: **49** haben weder `g` noch `gum`, aber nur **8** haben
gar keine Variante. Die Differenz sind **41 Indikatoren mit Daten, die der
Server für nicht vorhanden erklärte.** Der häufigste Schnitt ist der kantonale
(50 von 60) — während die Werkzeugbeschreibung behauptete, Obsan-Indikatoren
seien national.

`obsan/lebenserwartung` stand in [#55](https://github.com/malkreide/bag-health-mcp/pull/55)
als Beispiel für «keine Serie». Er hat 4374 Datenpunkte, kantonal, seit 1998.

Das gehört hierher und nicht in eine Fussnote, weil es die Fehlerklasse dieses
Berichts wiederholt, eine Ebene höher. Eine erfundene Fixture bestätigt die
Annahme ihres Autors. Eine echte Messung kann dasselbe tun, wenn man sie unter
der Annahme liest, die man ohnehin hatte: **404 auf die einzige Adresse, die man
kennt, misst die eigene Adressliste, nicht den Bestand der Quelle.** Der
Unterschied wurde erst sichtbar, als das Aufzeichnungsskript die Erhebung selbst
zum datierten Gegenstand machte (`tests/fixtures/obsan_variant_census.json`) —
also als die Zahl aufhörte, ein Satz in einer Commit-Nachricht zu sein.

## Wenn weitergemacht wird

Das Muster liegt in elf Servern vor und ist übertragbar: ein
`scripts/record_fixtures.py`, das die Quelle abruft, Ausschnitte nach
**dokumentierter Auswahlregel** schreibt und eine `PROVENANCE.md` mit Quelle,
Datum, Regel und SHA-256 erzeugt. Dazu ein Loader in `tests/`, der einen
fehlenden Namen als Fehler behandelt statt als leere Struktur.

Sieben Dinge haben sich dabei durchgehend bewährt:

1. **Erwartungen aus der Fixture ableiten**, nicht danebenschreiben. Eine feste
   Zahl ist beim nächsten Aufzeichnen falsch, ohne dass sich etwas Geprüftes
   geändert hätte.
2. **Laut abbrechen, wenn eine Auswahlregel nichts mehr trifft.** Eine Regel, die
   ins Leere greift, ist selbst der Befund — eine leere Fixture wäre ein Test,
   der nichts prüft und Erfolg meldet.
3. **Die Gegenprobe führen.** In `bag-health-mcp` bestand die erste Fassung des
   neuen Tests auch mit zurückgedrehter Fixture: Der Befund war enthalten, aber
   von keiner Zusicherung festgehalten. Erst die zweite Fassung fiel.
4. **Abgeleitete Erwartungen brauchen eine Code-Mutation, keine
   Fixture-Mutation.** Wer die Erwartung aus der Fixture ableitet — und das ist
   richtig, siehe Punkt 1 —, kann sie nicht prüfen, indem er die Fixture
   verbiegt: Die Erwartung wandert mit, und alles bleibt grün. In
   `meteoswiss-mcp` und `wsl-envidat-mcp` ist das jeweils passiert. Geprüft
   wird stattdessen am Server (dort: «rendere die älteste statt der jüngsten
   Zeile», «melde die gezeigte statt der gefundenen Zahl»). Wer diesen
   Unterschied übersieht, hält eine Tautologie für einen Test.
5. **Wo keine Antwort aufzeichenbar ist, den Vertrag aufzeichnen.**
   `swiss-transport-mcp` hat vier Quellen, die alle einen Bearer-Token
   verlangen; CI hat keinen, also lässt sich keine Antwort ehrlich datieren.
   Aufzeichenbar war stattdessen das öffentliche XML-Schema der Norm, gegen die
   der Server spricht — und das hat fünf ausgelieferte Fehler gefunden, die
   keine Antwort-Fixture je berührt hätte. Wenn die Daten verschlossen sind, ist
   die Schnittstellendefinition der nächstbeste aufzeichenbare Gegenstand.
   Fällt auch die weg, gehört das so in die `PROVENANCE.md` — wie bei Zefix in
   `register-mcp` — statt in ein Datum, das nicht stimmt.
6. **Der Zuschnitt muss die auffällige Zeile behalten.** «Die ersten N
   Datensätze» ist eine bequeme Auswahlregel und schneidet zuverlässig genau
   das weg, wofür es die Fixture gibt. In `swiss-academic-libraries-mcp`
   zweimal am selben Tag: ex/ante liefert ein rohes Steuerzeichen mitten in
   einem Feld — es sass ausserhalb der ersten zwei Datensätze, und ohne es
   belegte die Fixture nicht mehr, wozu die XML-Reinigung da ist. sui generis
   führt seine ersten Datensätze als `status="deleted"`; eine Fixture nur aus
   Grabsteinen lässt den Parser korrekt nichts liefern und prüft damit nichts.
   Beides hat der Aufzeichnungslauf selbst gemeldet, weil die Regeln als
   Zusicherung im Skript stehen und nicht als Absicht im Kopf. Das ist nicht
   Punkt 2: Dort trifft eine Regel nichts mehr, hier trifft sie das Falsche.

   In `swiss-democracy-mcp` ein drittes Mal, und dort wird der Grund sichtbar,
   warum Aufzeichnen überhaupt etwas findet: **Was eine Fixture wertvoll macht,
   ist meist genau das, was niemand erfinden würde.** Swissvotes markiert
   Fehlendes mit `9999`. Wer eine CSV-Zeile von Hand schreibt, schreibt
   `p-fdp;1` — plausibel, sauber, und damit blind für den Fall, der in 93 % der
   Zeilen vorkommt. Ausgewählt wird deshalb nach Merkmal, nicht nach Position;
   «die ersten N Zeilen» hätte aus 714 Zeilen ausgerechnet die harmlosen
   getroffen.
7. **Die Anfrage baut der Produktivcode, nicht das Aufzeichnungsskript.** In
   `swiss-electricity-mcp` ruft das Skript die Client-Klassen auf und fängt die
   Antwort über einen httpx-Transport ab, statt die SPARQL-Abfragen daneben noch
   einmal zu tippen. Bei 40 Zeilen SPARQL ist «leicht anders» der Normalfall —
   und eine Fixture, die eine leicht andere Frage beantwortet als der Server
   stellt, belegt unauffällig die falsche Antwort. Genau daran hängt der Befund
   dieses Servers: Der Fehler stand nicht in den Daten, sondern im Namensraum
   der Frage. Eine von Hand nachgebaute Abfrage hätte ihn mit derselben
   Wahrscheinlichkeit falsch nachgebaut wie der Server selbst.

   Dasselbe eine Ebene weiter oben, aus `bag-health-mcp` (siehe die Korrektur):
   **Wenn die Antwort davon abhängt, welche Adresse man fragt, muss die Fixture
   auch die Adresse aufzeichnen** — nicht bloss die Antwort darauf. Die Quelle
   sagte dort die ganze Zeit, welche Adressen es gibt; gelesen wurde es nie.

Wo Personendaten im Spiel sind — Amtsblatt-Rubriken wie `SB` und `LS` —, bleibt
die **Struktur echt und die Werte redigiert**, mit vollständiger Liste in der
`PROVENANCE.md`. Eine Fixture, die stillschweigend weniger belegt, als sie
aussieht, wäre genau der Fehler, gegen den das Ganze angeht.
