# Fixture-Herkunft im Portfolio — Bestandsaufnahme

**Erhebung: 2026-08-07. Zustandsspalten nachgemessen am 2026-08-08.** Erhoben
read-only über den Git-Proxy; kein Repo wurde für diese Messung verändert.

Der Bericht führt deshalb **zwei Daten**, und das ist Absicht: Die
Expositionswerte — Testdateien, Inline-Payloads, Live-Tests — stehen auf dem
Erhebungstag und dürfen sich nicht bewegen, sonst verliert die Rangfolge ihren
Bezugspunkt. Die Zustandsspalten — Fixture-Dateien, Provenienz — stehen auf dem
letzten Nachziehen. Wer nur eines der beiden Daten nennt, macht aus dem Bericht
genau die Angabe, gegen die er argumentiert.

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
| davon mit Aufzeichnungsskript **und** Datum | **21** |
| Inline-Payloads insgesamt | **rund 1 145** |
| mit Live-Test-Markern | 40 |
| davon an einem Zeitplan | 20 |

Zum Zeitpunkt der Erhebung hatte **kein einziger** der 42 Server eine datierte
Fixture-Herkunft. Zwölf sind am 2026-08-07 und 2026-08-08 nachgezogen worden,
neun weitere am 2026-08-08 (siehe «Was daraus geworden ist»). Das ist die Hälfte
des Portfolios; die andere Hälfte steht unverändert auf «keine».

**Die Zahl 21 ist gemessen, nicht mitgezählt.** Beim Nachziehen dieses Berichts
stand in der laufenden Notiz «neunzehn». Nachgemessen wurde über alle Repos
gegen den Standardzweig — Aufzeichnungsskript unter `scripts/record_fixtures.py`
**und** eine `PROVENANCE.md` unter `tests/`, die ein Datum führt. Es sind 21.
Eine mitlaufende Zählung ist genau das, wogegen dieser Bericht argumentiert:
eine Behauptung ohne Messzeitpunkt.

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

**Testdateien, Payloads und Live-Tests sind Erhebungswerte, Fixture-Dateien und
Provenienz sind Tagesstand.** Die Rangfolge hat nur als *ein* Messzeitpunkt eine
Bedeutung;
würde man die Exposition der nachgezogenen Server nachmessen, verschöbe sich die
Liste, weil das Nachziehen selbst Tests hinzufügt. Bei `swiss-transport-mcp` wäre
das nach dem Nachziehen 17 Testdateien und 27 Payloads statt 14 und 20. Die
Spalten, die den *Zustand* melden — Fixture-Dateien, Provenienz —, stehen
dagegen auf heute; sonst wäre die Tabelle für ihren eigentlichen Zweck blind.

Die Live-Spalte steht deshalb weiterhin auf dem Erhebungsstand, auch wo sie
inzwischen falsch ist: `eth-library-mcp` führt dort «keine» und hat seit dem
Nachziehen zwei Live-Tests, `sbb-opendata-mcp` und `news-monitor-mcp` haben ihre
vorhandenen erstmals zum Laufen gebracht. Wer aus dieser Spalte den heutigen
Zustand lesen will, liest die falsche Tabelle — die Befunde dazu stehen unten.

### Drei Kalibrierungen, offengelegt

Der Detektor hat sich dreimal selbst getäuscht, und alle drei Male ist es genau
die Fehlerklasse, um die es hier geht:

1. Er meldete Provenienz, sobald irgendein README das Wort «aufgezeichnet»
   enthielt. Eine Herkunftsangabe am falschen Ort ist keine.
2. Er meldete «Datum im Test» für einen Server, dessen Fixtures nachweislich
   erfunden waren — die Daten stammten aus der `Stand`-Spalte der Nutzdaten. Das
   Signal ist zurückgestuft und zählt nicht als Beleg.
3. **Beim Nachziehen auf 21**, also mit dem Bericht in der Hand, der die beiden
   ersten Fehler bereits beschreibt: Die Neumessung suchte `PROVENANCE` per
   Namensmuster über den ganzen Baum und traf in `zh-education-mcp`
   `src/zh_education_mcp/provenance.py` — eine Quelldatei für die
   Lizenz-Attribution, die mit Fixture-Herkunft nichts zu tun hat. Der Server
   erschien dadurch als «Provenienz ohne Datum», obwohl seine
   `tests/fixtures/PROVENANCE.md` in Ordnung ist. Punkt 1 in neuer Kleidung, im
   selben Repo, mit derselben Ursache: Ein Name am falschen Ort ist kein Beleg.
   Die Messung greift seither nur noch auf `tests/**/PROVENANCE.md` zu.

Ein zweiter Messfehler derselben Erhebung gehört daneben, weil er die andere
Richtung zeigt: Der erste Durchlauf meldete für 15 von 21 nachgezogenen Servern
**kein** Aufzeichnungsskript. Gemessen war nicht der Bestand der Repos, sondern
das Alter der lokalen Klone — `origin/main` war Tage alt. Dieselbe Regel wie bei
den beiden Korrekturen weiter unten, ein drittes Mal: **Eine Messung, die die
eigene Vorlage abfragt, misst die Vorlage.**

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
| `bag-health-mcp` ✅ | 3 | 72 | 14 | **datiert** | 1 Datei(en) |
| `swiss-procurement-mcp` | 20 | 72 | 0 | keine | 1 Datei(en)+geplant |
| `swiss-cultural-heritage-mcp` | 3 | 66 | 0 | keine | 1 Datei(en)+geplant |
| `amtsblatt-mcp` | 20 | 64 | 0 | keine | 2 Datei(en)+geplant |
| `swiss-environment-mcp` | 7 | 57 | 0 | keine | 4 Datei(en)+geplant |
| `seco-labor-mcp` | 4 | 47 | 0 | keine | 1 Datei(en)+geplant |
| `register-mcp` ✅ | 6 | 44 | 8 | **datiert** | 2 Datei(en) |
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
| `swiss-snb-mcp` ✅ | 4 | 11 | 11 | **datiert** | 2 Datei(en) |
| `eth-library-mcp` ✅ | 2 | 11 | 1 | **datiert** | keine |
| `fedlex-mcp` | 3 | 9 | 0 | keine | 1 Datei(en) |
| `hn-tech-signal-mcp` | 2 | 6 | 0 | keine | 1 Datei(en) |
| `swiss-energy-mcp` | 5 | 5 | 0 | keine | 1 Datei(en)+geplant |
| `lobbywatch-mcp` | 6 | 5 | 0 | keine | 1 Datei(en) |
| `swiss-ip-mcp` ✅ | 1 | 5 | 1 | **datiert** | 1 Datei(en)+geplant |
| `openlex-mcp` ✅ | 8 | 4 | 2 | **datiert** | 1 Datei(en)+geplant |
| `swiss-housing-mcp` | 1 | 4 | 0 | keine | 1 Datei(en)+geplant |
| `bag-epl-mcp` ✅ | 3 | 3 | 3 | **datiert** | 1 Datei(en) |
| `news-monitor-mcp` ✅ | 2 | 2 | 1 | **datiert** | 1 Datei(en) |
| `global-education-mcp` ✅ | 2 | 2 | 9 | **datiert** | keine |
| `swiss-culture-mcp` ✅ | 1 | 1 | 3 | **datiert** | 1 Datei(en) |
| `bakom-mcp` | 7 | 1 | 0 | keine | 1 Datei(en) |
| `sbb-opendata-mcp` ✅ | 1 | 0 | 8 | **datiert** | 1 Datei(en) |
| `swiss-food-safety-mcp` ✅ | 1 | 0 | 2 | **datiert** | 1 Datei(en) |

`swiss-public-data-mcp` führt keine Testsuite — es ist das Portfolio-Meta-Repo.

## Wo es am ehesten weh tut

Viele ungeprüfte Annahmen **und** kein Zeitplan, der sie gegen die Quelle hält:

| Server | Payloads | Live |
|---|---:|---|
| `swiss-electricity-mcp` ✅ | 15 | 1 Datei(en) |
| `swiss-snb-mcp` ✅ | 11 | 2 Datei(en) |

**Diese Liste ist abgearbeitet, und sie hatte recht** — wenn auch nicht aus dem
Grund, den sie nennt. Bei `swiss-electricity-mcp` lieferten alle drei
ElCom-Tarif-Werkzeuge seit einer Umstellung der Quelle nichts. Bei
`swiss-snb-mcp` kamen vier ausgelieferte Fehler heraus, dazu ein fünfter am
Prüfwerk selbst. Zwei von zwei, bei den beiden kleinsten Expositionswerten des
Portfolios — was die Spalte misst, ist eben nicht Risiko.

Die Zahl misst Exposition, **nicht** Risiko. Ein Server mit 134 erfundenen
Payloads gegen eine stabile API ist harmloser als einer mit fünf gegen eine
Quelle, die ihre Kopfzeilen wechselt. Der Faktor-100-Fehler in
`zh-education-mcp` steckte in **einer Zelle einer Fixture mit drei Zeilen**.

## Was daraus geworden ist

**21 Server sind nachgezogen worden** — zwölf zuerst, aus der oberen Hälfte der
Rangfolge, danach neun aus der unteren. In **16** von 21 hat allein das
Aufzeichnen einen ausgelieferten Fehler freigelegt; fünf sind Nullbefunde.

| Server | PR | Befund |
|---|---|---|
| `zh-education-mcp` | [#41](https://github.com/malkreide/zh-education-mcp/pull/41) | Die Maturitätsquote war um **Faktor 100** zu hoch. Die Quelle publiziert die Spalte bereits in Prozent; die erfundene Fixture schrieb eine Bruchzahl hinein und liess `* 100` plausibel aussehen. |
| `bag-health-mcp` | [#55](https://github.com/malkreide/bag-health-mcp/pull/55), [#56](https://github.com/malkreide/bag-health-mcp/pull/56) | Die Sitemap-Fixture beschrieb eine Form, die es nicht gibt: vier `/de/`-URLs, von denen die Quelle **keine einzige** liefert. Deutsch kommt sprachneutral. Der Zusatzbefund «9 von 12 Indikatoren haben gar keine Datenserie» war eine Fehldeutung meiner eigenen Messung — siehe die Korrektur unten. |
| `register-mcp` | [#49](https://github.com/malkreide/register-mcp/pull/49), [#50](https://github.com/malkreide/register-mcp/pull/50) | Eine korrekte **HR-Suche war blockiert** — 2 279 587 Treffer über einer Schwelle von 2 000 000, die «weit über jedem plausiblen Einzelfilter» liegen sollte. Nachgereicht in #50: **`legalSeatId` wurde über die falsche Spalte aufgelöst** — sie ist eine BFS-Nummer, und über die interne Gemeinde-`id` gelesen kommt kein Fehler heraus, sondern eine andere, echte Schweizer Gemeinde (261 ist Zürich, über `id` aber Aarwangen BE). 0 von 12 richtig. Dazu: Eine Suche ohne Treffer antwortete «Bitte EHRAID oder UID prüfen», weil Zefix die leere Menge mit HTTP 404 meldet und nicht mit 200. |
| `zurich-opendata-mcp` | [#84](https://github.com/malkreide/zurich-opendata-mcp/pull/84) | **Kein Befund.** 246 Tests unverändert grün. Der Server sendet `rows` überall explizit; das Aufzeichnen hat es nur belegt. |
| `swiss-statistics-mcp` | [#29](https://github.com/malkreide/swiss-statistics-mcp/pull/29) | **Kein Befund am Server**, drei an den Fixtures: Ein Snapshot ist ein Zeitpunkt, die alte Fixture war zwei (BFS 133 *und* 295 in einer Datei); die Korrespondenz-Fixture beantwortete eine Anfrage mit anderen Parametern, als der Server sendet; falsche Codes und ein gekürzter Titel. |
| `meteoswiss-mcp` | [#42](https://github.com/malkreide/meteoswiss-mcp/pull/42) | **Kein Befund am Server.** Die STAC-Fixture führte 4 Assets, die Quelle liefert 16 — der Selektor, der ausdrücklich jeden Fallback ablehnt, wurde nie gegen die Historik-Dateien geprüft, gegen die es ihn gibt. |
| `wsl-envidat-mcp` | [#24](https://github.com/malkreide/wsl-envidat-mcp/pull/24) | **Kein Befund am Server**, drei an den Fixtures: Die Organisationen `wsl` und `slf` gibt es nicht (`organization_show?id=slf` → HTTP 404); Tags stehen in GROSSBUCHSTABEN statt kleingeschrieben; ein Datensatz hat 42 Felder statt 9, mit `extras`, die die Quelle nicht kennt. |
| `swiss-transport-mcp` | [#31](https://github.com/malkreide/swiss-transport-mcp/pull/31) | **Fünf Befunde am Server**, alle derselben Herkunft: Er spricht an mehreren Stellen OJP **1.0**, wo er 2.0 zu sprechen glaubt. `<n>` statt des Pflichtfelds `<Name>` in jedem `PlaceRef` — damit war jede Reise- und Abfahrtsanfrage ungültig; `<LocationName>` für Ortsnamen, die es in OJP 2.0 innerhalb eines `PlaceRef` gar nicht gibt; `<IncludeRealtimeData>` statt `UseRealtimeData`; der Standort-Parser las nur `StopPlaceName` und verwarf alles andere; Fusswege kamen ohne Start- und Zielnamen zurück. |
| `swiss-academic-libraries-mcp` | [#50](https://github.com/malkreide/swiss-academic-libraries-mcp/pull/50) | **Die Sammlungs-Übersicht meldete ein Zehntel des Bestands als Gesamtzahl.** `ListSets` ist paginiert wie `ListRecords`; gelesen wurde eine Seite. e-rara: 10 statt **105**, e-manuscripta: 10 statt **49**. Der Namensfilter lief danach über diese Reste, so dass eine Sammlung, die es gibt, als «Keine Sammlungen gefunden» zurückkam. |
| `swiss-electricity-mcp` | [#37](https://github.com/malkreide/swiss-electricity-mcp/pull/37) | **Alle drei ElCom-Tarif-Werkzeuge lieferten seit einer Umstellung der Quelle nichts.** LINDAS hat den Prädikat-Namensraum umgebaut: `.../measure/*` gibt es nicht mehr, alles steht unter `.../dimension/*`, und die cube-eigenen Namensräume sind weg. `measure/total` war Pflicht-Tripel in jeder Abfrage — das Ergebnis war deshalb kein Fehler, sondern **HTTP 200 mit null Zeilen**, für jede Gemeinde und jedes Jahr. Zürich hat 291 Beobachtungen im Cube; die Abfrage des Servers fand null. Dazu zwei weitere: vier von fünf Speicherseen-Regionen lieferten unter ihrem eigenen Namen die Schweizer Zahlen, und der Standardschnitt der Zeitreihe traf 52 Zeilen ohne eine einzige Messung, weil die Reihe in die Zukunft läuft. |
| `swiss-snb-mcp` | [#35](https://github.com/malkreide/swiss-snb-mcp/pull/35) | **Vier Befunde.** Die Bankenbilanz lieferte für `frequency="monthly"` **immer** eine leere Tabelle: Die Dimensionsordnung stand als Konstante mit vier Einträgen im Code, der Monats-Cube führt fünf, und jede Reihe mit abweichender Länge wurde stumm verworfen — HTTP 200, Kopfzeile, nichts darunter. `snb_get_warehouse_metadata` war kaputt, seit es existiert: Es baute `dimensions/json/<lang>`, einen Pfad, den es nicht gibt und den data.snb.ch als Angular-App mit **HTTP 200 und `text/html`** beantwortet. Die Jahresreihe gab Total, Inland und Ausland als drei identisch beschriftete Zeilen aus, wobei Inland + Ausland das Total ergibt. Und `INR100` wurde als Währung angeboten, die es in keinem der Cubes gibt. |
| `swiss-democracy-mcp` | [#25](https://github.com/malkreide/swiss-democracy-mcp/pull/25) | **Füllwerte wurden als Parteiparolen ausgegeben.** Swissvotes markiert Fehlendes mit `9999` und `.`; der Code übersetzte die bekannten Codes und reichte den Rest roh durch. **667 der 714 Abstimmungen** betroffen — für die Bundesverfassung von 1848 meldete das Werkzeug `{"FDP": "9999", …}` für alle zehn Parteien, von denen es damals keine gab. |

### Die neun aus der unteren Hälfte

| Server | PR | Befund |
|---|---|---|
| `eth-library-mcp` | [#18](https://github.com/malkreide/eth-library-mcp/pull/18) | **Ein Werkzeug bot eine API an, die es nicht mehr gibt.** Im Code und in beiden READMEs stand seit Langem, die Persons-API gebe «aktuell HTTP 404» und die richtige URL müsse noch verifiziert werden. Es gibt keine richtige URL. Entscheidbar war das **ohne API-Schlüssel**, weil das Gateway vor der Schlüsselprüfung routet: `/discovery/v1/resources` → 401 (Route da, Schlüssel fehlt), ein erfundener Discovery-Pfad → 404, sämtliche Persons-Pfade → 404. `eth_search_persons` ist entfernt statt mit einer schöneren Fehlermeldung versehen. Damit fällt auch die Angabe «7 Tools / 3 APIs» aus beiden READMEs — es sind sechs Werkzeuge und eine API. |
| `sbb-opendata-mcp` | [#24](https://github.com/malkreide/sbb-opendata-mcp/pull/24) | **Drei von zehn Werkzeugen antworteten auf jede Anfrage mit einem Fehler.** Die Haltestellensuche wählte sieben deutsche Feldnamen aus einem Datensatz, der ausschliesslich englische führt — die Explore-API beantwortet ein unbekanntes Feld im `select` mit HTTP 400, nicht mit weniger Spalten. `sbb_list_datasets` sortierte nach `metas.default.title`, das der Katalog nicht kennt: Das Werkzeug, mit dem man herausfindet, welche Datensätze es gibt, hat nie funktioniert (es sind 61). Das dritte fragte einen Datensatz, den es nicht mehr gibt, und ist entfernt. Nebenbefund: Die DiDok-Liste schreibt «unbefristet gültig» als `9999-12-31`, bei 59 515 von 59 530 Einträgen — derselbe Füllwert, der in `swiss-democracy-mcp` als Parteiparole hinausging. |
| `global-education-mcp` | [#21](https://github.com/malkreide/global-education-mcp/pull/21) | **Drei von vier UIS-Pfaden gaben HTTP 404, und 12 der 22 angebotenen Indikator-IDs führt die Quelle nicht.** Die Suite war dabei mit 128 Tests grün: Die Mocks trugen dieselben erfundenen Feldnamen wie der Produktivcode. Der Antwortumschlag heisst `records`, gelesen wurde `observations`; der Jahresfilter hiess `startYear`/`endYear` statt `start`/`end`, und unbekannte Parameter beantwortet die Quelle mit 200 und lässt sie fallen. Die Quelle nennt einen unbekannten Ländercode im Klartext — gelesen wurde das nie, ein Tippfehler sah aus wie Datenmangel. |
| `bag-epl-mcp` | [#32](https://github.com/malkreide/bag-epl-mcp/pull/32) | **Der GgV-Rechtsverweis zeigte auf eine ELI, die das Register nicht führt** (`1986/40_40_40` statt `1986/46_46_46`). Kein Statuscode konnte das zeigen: Fedlex antwortet für **jede** ELI mit HTTP 200 und derselben Byte-Zahl. Dazu drei ausgegebene «offizielle Quellen» mit HTTP 404 — für zwei Werkzeuge war dieser Link die ganze Antwort. Und `_sl_website_suche` machte aus einem `JSONDecodeError` die Aussage «die API ist nicht öffentlich dokumentiert»; gemessen ist HTTP 200 mit `text/html`, byte-identisch zu einem frei erfundenen Pfad. |
| `news-monitor-mcp` | [#42](https://github.com/malkreide/news-monitor-mcp/pull/42) | **Die drei Live-Tests dieses Repos liefen nie.** Sie trugen `@pytest.mark.live`, aber keinen `@pytest.mark.asyncio` — im Strict-Default heisst das «async def functions are not natively supported», und die CI schliesst `-m live` aus, also meldete es niemand. Alle drei Zusicherungen trafen ausserdem nur die eigene Vorlage; eine war eine Disjunktion, deren zweiter Zweig die Ergebnis-Überschrift ist und damit immer wahr. `data.get("news", [])` machte aus einem Formfehler «0 Ergebnisse». |
| `swiss-food-safety-mcp` | [#24](https://github.com/malkreide/swiss-food-safety-mcp/pull/24) | **Sieben Werkzeuge zum ersten Mal live getrieben, sechs gaben etwas anderes aus, als sie versprachen** — und keines sah dabei nach einem Fehler aus. Die Tierseuchen-Suche hat nie Daten geliefert: Der SPARQL-Endpunkt war die Editor-Oberfläche (POST 404), die Abfrage traf eine Klasse mit null Instanzen — so viele wie eine erfundene Kontrollklasse. Ein Werkzeug gab Antibiotikadaten statt Tiergesundheitsdaten aus, eines eine Code-Legende statt Kontrollergebnissen, eines das `datapackage.json` — die *Beschreibung* der Daten, als wären es die Daten. Der UTF-8-BOM stand im Namen der ersten Spalte, weshalb jeder Jahresfilter still ins Leere lief. |
| `openlex-mcp` | [#41](https://github.com/malkreide/openlex-mcp/pull/41) | **Acht Werkzeuge, acht Live-Tests — die beste Abdeckung im Portfolio, und trotzdem ein Befund.** Er liegt nicht in der Mechanik, sondern in der Verwechslung zweier Fragen: `provenance="cache"` sagt, woher *diese Antwort* kam; gemeint ist, wie alt die *Gesetze darin* sind. Die jüngste Fassung im Datensatz stammt vom 2023-01-01, der Cache gilt derweil 24 Stunden. Ein zwischenzeitlich aufgehobenes Gesetz erscheint weiterhin als in Kraft. Neu weist jede Antwort `corpus_as_of` aus. |
| `swiss-ip-mcp` | [#37](https://github.com/malkreide/swiss-ip-mcp/pull/37) | **Nullbefund, dreifach belegt.** Jede Adresse, der Keycloak-Realm und der `client_id` sind die, die die Quelle führt. Drei unabhängige Belege, weil einer nicht getragen hätte: Der IDP unterscheidet drei Fälle (falsche Zugangsdaten → `invalid_grant`, erfundener Realm → 404, erfundener `client_id` → `invalid_client`); der Realm nennt seinen Token-Endpunkt selbst unter `.well-known/openid-configuration`; die API-Doku deklariert beide Adressen wörtlich. Der dritte Beleg ist nötig, weil die Swissreg-API selbst **nicht** unterscheidet — gebauter und erfundener Pfad antworten identisch. |
| `swiss-culture-mcp` | [#19](https://github.com/malkreide/swiss-culture-mcp/pull/19) | **Eine ausgegebene «offizielle Quelle» war tot.** `bak_isos_overview` gab einen BAK-Pfad aus, der HTTP 404 liefert — wie der ganze `kulturerbe`-Zweig. Belegt mit einer Kontrolle: Ein frei erfundener Pfad unter demselben Präfix liefert denselben 404 mit demselben Titel. Eine Ersatzadresse ist bewusst nicht geraten. Alles andere trug und ist als Nullbefund mit aufgezeichnet. |

Die **fünf** Nullbefunde gehören genauso in diese Tabellen wie die 16 Funde. Nach
drei Repos in Folge, die etwas hergaben, wäre die Versuchung gross gewesen, auch
in den übrigen etwas zu finden.

**Die Rangfolge trennt Fund und Nullbefund nicht.** Die 16 ausgelieferten Fehler
liegen auf den Plätzen 3, 9, 13, 19, 21, 22, 24, 27, 28, 34, 36, 37, 38, 39, 41
und 42, die fünf Nullbefunde auf 10, 11, 12, 17 und 33 — verschränkt, nicht
gestaffelt. Das ist kein Mangel der Rangfolge, sondern das, was die
Payload-Spalte misst: Exposition, nicht Risiko. Sie sagt, wie viel ungeprüfte
Annahme ein Server trägt, nicht, ob eine davon falsch ist.

### Die offene Frage der ersten Fassung, jetzt beantwortet

Der Bericht führte an dieser Stelle einen Vorbehalt: *«Alle zwölf stammen aus den
obersten 27 von 42; über die untere Hälfte sagt diese Stichprobe gar nichts.»*
Die untere Hälfte ist inzwischen begangen, und die Antwort fällt deutlicher aus
als erwartet — **sie zeigt nicht bloss, dass die Rangfolge nichts über Risiko
sagt, sondern dass sie in dieser Stichprobe in die falsche Richtung zeigt:**

| | nachgezogen | mit Fund | Quote |
|---|---:|---:|---:|
| obere Hälfte (Plätze 1–21) | 9 | 5 | 56 % |
| untere Hälfte (Plätze 22–42) | 12 | 11 | 92 % |

Die beiden Server mit **null** Inline-Payloads — dem kleinsten Expositionswert
des ganzen Portfolios, den Plätzen 41 und 42 — tragen beide einen Fund, und
keinen kleinen: In `sbb-opendata-mcp` antworteten drei von zehn Werkzeugen auf
jede Anfrage mit einem Fehler, darunter das Werkzeug, das auflistet, welche
Datensätze es überhaupt gibt. In `swiss-food-safety-mcp` gaben sechs von sieben
live getriebenen Werkzeugen etwas anderes aus, als sie versprachen. Ein Server
ohne einen einzigen erfundenen Payload ist eben nicht geprüft — er ist
**ungeprüft**, und die Spalte kann diese beiden Zustände nicht auseinanderhalten.

**Dieser Vergleich ist keine Statistik, und er soll keine sein.** Die 21 sind
nicht zufällig gezogen, sondern in zwei bewussten Wellen bearbeitet, und die
zweite lief mit dem Wissen aus der ersten — die Kontrollprobe, die Auswahl nach
Merkmal, der Import der Basis-URL aus dem Produktivcode waren beim zweiten
Durchgang von Anfang an da. Ein Teil der höheren Quote ist deshalb der geschärfte
Blick und nicht der schlechtere Zustand. Was der Vergleich trägt, ist die
schwächere und ausreichende Aussage: **Wer die Rangfolge von oben abarbeitet,
arbeitet nicht die gefährlichsten Server zuerst ab.** Für die Reihenfolge der
restlichen 21 heisst das, dass die Spalte als Priorisierung ausgedient hat.

Keiner der 16 Fehler stand in den Daten. Sie standen in der Frage, im Blättern,
im Codebuch, im Namensraum, in der Zahl der Dimensionen, in einer Feldsprache, in
einem Byte vor der ersten Kopfzeile und in einer URL, die seit Jahren 404 gibt.
Davon kann eine Payload-Zählung nichts wissen.

### Ein Befund anderer Art: das Prüfwerk selbst

In `swiss-snb-mcp` kam ein fünfter Befund heraus, der in keine Spalte dieser
Tabelle passt, weil er nicht den Server betrifft, sondern **das, was ihn hätte
prüfen sollen**.

Beide Live-Suiten des Servers liefen doppelt. Ihre Szenarien hiessen
`test_01_…` bis `test_20_…`, also sammelte pytest jedes einzeln ein und fuhr es
ausserhalb der Lifespan — ohne offenen HTTP-Client, also zwangsläufig rot.
Danach lief derselbe Satz noch einmal korrekt über den eigentlichen
Einstiegspunkt. Der Lauf meldete seither `Total: 40 | Bestanden: 24 |
Fehlgeschlagen: 16` bei 20 Szenarien und listete jedes Szenario einmal rot und
einmal grün.

Der Lauf war damit seit jeher rot, und deshalb stand der Job auf
`continue-on-error`. **Ein Signal, das immer Alarm gibt, ist abgeschaltet** —
und dieses hier hätte zwei der vier Befunde gefunden: Es gibt ein Live-Szenario
für die Monatsbilanz und eines für die Dimensionsmetadaten, und beide fahren
genau die Aufrufe, die nichts lieferten.

Das ist der Grund, warum das Aufzeichnen hier überhaupt etwas gefunden hat: Der
Server hatte mehr Live-Abdeckung als die meisten im Portfolio, und sie war
wirkungslos. Eine Zahl in der Live-Spalte dieser Rangfolge sagt, dass es
Live-Tests *gibt* — nicht, dass jemand ihr Ergebnis liest.

**Die untere Hälfte hat denselben Befund noch zweimal geliefert, in zwei
weiteren Gestalten.** Er ist damit kein Einzelfall dieses einen Servers,
sondern ein Muster:

- `news-monitor-mcp`: Die drei Live-Tests trugen `@pytest.mark.live`, aber
  keinen `@pytest.mark.asyncio`. Im Strict-Default ist das kein Überspringen,
  sondern ein Fehler — «async def functions are not natively supported». Weil
  die CI `-m live` ausschliesst, hat den nie jemand gesehen. Behoben wurde nicht
  die einzelne Markierung, sondern `asyncio_mode = "auto"`: Eine vergessene
  Markierung kann diesen Fehler jetzt nicht mehr erzeugen.
- `sbb-opendata-mcp`: Für **zwei der drei kaputten Werkzeuge gab es einen
  Live-Test** — `test_live_search_waedenswil` und `test_live_list_datasets`.
  Beide hätten den Fehler gemeldet. Die CI fährt nur `-m "not live"`, und einen
  Live-Job gibt es nicht. Die Abdeckung war da, der Lauf nicht.

Drei Server, drei Mechanismen, ein Ergebnis: **rot, aber nicht gelesen**
(`swiss-snb-mcp`), **fehlerhaft, aber nicht ausgeführt** (`news-monitor-mcp`),
**korrekt, aber nie gefahren** (`sbb-opendata-mcp`). In allen drei Fällen hätte
die Live-Spalte dieser Rangfolge eine Zahl grösser null gemeldet. Sie zählt
Dateien, nicht Läufe, und ein Lauf, den niemand liest, ist kein Lauf.

### Zwei Korrekturen an diesem Bericht — und beide dieselbe

Der Bericht führte zwei offene Lücken. Beide sind geschlossen, und beim
Schliessen hat sich gezeigt, dass **beide Sätze falsch waren** — auf dieselbe
Weise. Das ist der Grund, warum sie hier stehen und nicht in einer Fussnote.

#### Erste Korrektur: `bag-health-mcp`

Die Lücke stand hier so: *«`bag-health-mcp` bietet Indikatoren an, die es nicht
ausliefern kann.»* Geschlossen mit
[#56](https://github.com/malkreide/bag-health-mcp/pull/56).

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

#### Zweite Korrektur: Zefix in `register-mcp`

Die Lücke stand hier so: *«Die API verlangt `ZEFIX_USER`/`ZEFIX_PASSWORD` und
antwortet ohne sie mit HTTP 401.»* Geschlossen mit
[#50](https://github.com/malkreide/register-mcp/pull/50) — **ohne
Zugangsdaten**, weil es nie welche gebraucht hat.

Es gibt zwei Zefix-APIs unter demselben Host. Das Aufzeichnungsskript fragte
`ZefixPublicREST`; das verlangt tatsächlich Zugangsdaten. Der Server spricht mit
`ZefixREST`, und das antwortet **ohne jede Anmeldung mit HTTP 200**. Die 401 hat
also die Adressliste des Skripts gemessen, nicht den Zugang zur Quelle. Das
Aufzeichnen förderte danach zwei ausgelieferte Fehler zutage, darunter einer, der
für `legalSeatId=261` statt Zürich die Gemeinde Aarwangen (BE) benennt — ohne
Fehlermeldung, weil beide Zahlen echt sind.

#### Warum beide Sätze auf dieselbe Weise falsch waren

Eine erfundene Fixture bestätigt die Annahme ihres Autors und kann sie nicht
widerlegen. Eine **echte Messung** kann dasselbe tun, wenn man sie unter der
Annahme liest, die man ohnehin hatte:

> **404 oder 401 auf die einzige Adresse, die man kennt, misst die eigene
> Adressliste — nicht den Bestand und nicht den Zugang der Quelle.**

Beide Male stimmte die Zahl, und beide Male stand sie für etwas anderes, als im
Bericht daraus geschlossen wurde. In `bag-health-mcp` wurde der Unterschied
sichtbar, als das Aufzeichnungsskript die Erhebung selbst zum datierten
Gegenstand machte (`tests/fixtures/obsan_variant_census.json`) — also als die
Zahl aufhörte, ein Satz in einer Commit-Nachricht zu sein. In `register-mcp`
wurde er sichtbar, als das Skript die Basis-URL nicht mehr abschrieb, sondern
aus dem Produktivcode importierte. Das ist Lehre 7, von der anderen Seite: Wenn
das Aufzeichnungsskript eine andere Adresse fragt als der Server, misst es den
falschen Gegenstand — und das gilt für die Fehlschläge genauso wie für die
Antworten.

## Wenn weitergemacht wird

Das Muster liegt in 21 Servern vor und ist übertragbar: ein
`scripts/record_fixtures.py`, das die Quelle abruft, Ausschnitte nach
**dokumentierter Auswahlregel** schreibt und eine `PROVENANCE.md` mit Quelle,
Datum, Regel und SHA-256 erzeugt. Dazu ein Loader in `tests/`, der einen
fehlenden Namen als Fehler behandelt statt als leere Struktur.

Zehn Dinge haben sich dabei durchgehend bewährt. Die Punkte 1 bis 8 stammen aus
der ersten Welle, 9 und 10 aus der zweiten — die untere Hälfte der Rangfolge
besteht überwiegend aus Servern, deren Quelle Zugangsdaten verlangt oder deren
Antwort sich nicht ehrlich datieren lässt, und dort verschiebt sich der
Gegenstand des Aufzeichnens:

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

   Und in `register-mcp` derselbe Punkt an der schmerzhaftesten Stelle: Das
   Aufzeichnungsskript schrieb die Basis-URL ab, statt sie zu importieren, und
   fragte damit eine andere Zefix-API als der Server. Die 401, die daraufhin
   ein Jahr lang als «braucht Zugangsdaten» im Bericht stand, betraf einen
   Endpunkt, den der Server nie anfasst. Seit die URL aus `server.py` kommt,
   kann das nicht mehr auseinanderlaufen.
8. **Was der Server ausgibt, muss sagen, welcher Schnitt es ist.** Drei Server
   haben denselben Fehler in drei Gestalten getragen: `swiss-snb-mcp` gab
   Total, Inland und Ausland als drei identisch beschriftete Zeilen aus (Inland
   + Ausland ergibt das Total — wer summierte, verdoppelte die Bilanz);
   `bag-health-mcp` reichte eine Verteilung in % durch, wo eine standardisierte
   Rate erwartet wurde; `register-mcp` legte zwei Zahlenspalten nebeneinander,
   von denen nur eine die richtige ist. In allen drei Fällen ist die Antwort
   vollständig, plausibel und formatiert — und über etwas anderes.

   Die Regel, die daraus folgt, ist unbequem und billig: **Jede Dimension, die
   nicht eingegrenzt wurde, gehört benannt in die Ausgabe.** Eine Dimension,
   die weder gefiltert noch angezeigt wird, ist genau der Weg, auf dem mehrere
   Messgrössen unter eine Beschriftung geraten. Erfundene Fixtures zeigen das
   nie, weil sie je Fall eine Zeile führen — die Mehrdeutigkeit entsteht erst
   in der Menge.
9. **Ein Statuscode belegt nur mit Kontrolle etwas — und manchmal auch dann
   nicht.** Ein 404 auf eine Adresse, die man selbst gebaut hat, misst die
   eigene Adressliste. Erst eine **frei erfundene** Gegenprobe zeigt, ob die
   Quelle überhaupt unterscheidet. Am ETH-Gateway tut sie es sauber: bekannter
   Discovery-Pfad → 401, erfundener → 404, sämtliche Persons-Pfade → 404 — damit
   ist «die API ist weg» belegt, ohne einen einzigen Schlüssel zu besitzen. An
   anderen Quellen trägt dieselbe Messung nichts: `epl.bag.admin.ch` und
   `www.swissreg.ch` antworten auf erfundene Pfade identisch wie auf echte;
   Fedlex liefert für **jede** ELI HTTP 200 mit derselben Byte-Zahl; der
   BAK-News-Feed liefert 200 auch für eine erfundene Organisationsnummer, und
   nur die Byte-Grösse (367 gegen 344 962) trennt die Fälle. **Wo die Quelle
   nicht unterscheidet, ist der Statuscode kein Beleg, sondern eine Zahl** — dann
   braucht es eine zweite, unabhängige Quelle: die `.well-known`-Deklaration, die
   API-Doku, ein amtliches Register. In `swiss-ip-mcp` steht der Nullbefund
   deshalb auf drei Belegen und nicht auf einem.

   Der Nullbefund gehört dabei genauso aufgezeichnet wie der Fund. Ein
   Nullbefund, den niemand festhält, ist beim nächsten Durchgang keiner mehr —
   dann wird dieselbe Adresse wieder verdächtigt und wieder freigesprochen.
10. **Eine Fähigkeit anzubieten, die es nicht gibt, ist derselbe Fehler wie ein
    leeres Ergebnis — nur lauter.** Zweimal unabhängig aufgetreten:
    `eth_search_persons` stand mit Warnhinweis in der Werkzeugliste, also genau
    dort, wo ein Modell zuerst hinsieht, und die dahinterliegende API gibt es
    nicht mehr. `sbb_get_infrastructure_construction_projects` fragte einen
    Datensatz, den der Katalog nicht mehr führt und für den er keinen Nachfolger
    kennt. Beide sind **entfernt** und nicht mit einer schöneren Fehlermeldung
    versehen. Eine bessere Meldung macht das Werkzeug nur höflicher, nicht
    ehrlicher — angeboten wird es weiterhin.

    Damit fällt regelmässig auch eine Zahl in der Dokumentation: Aus «7 Tools /
    3 APIs» wurden in `eth-library-mcp` sechs Werkzeuge und eine API, in beiden
    READMEs. Wer ein Werkzeug entfernt und die Auszählung stehen lässt, hat den
    Fehler nur eine Ebene nach oben verschoben.

Wo Personendaten im Spiel sind — Amtsblatt-Rubriken wie `SB` und `LS` —, bleibt
die **Struktur echt und die Werte redigiert**, mit vollständiger Liste in der
`PROVENANCE.md`. Eine Fixture, die stillschweigend weniger belegt, als sie
aussieht, wäre genau der Fehler, gegen den das Ganze angeht.
