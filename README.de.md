# swiss-public-data-mcp

![Aktive Server](https://img.shields.io/badge/aktive%20Server-42-blue)
![Production Ready](https://img.shields.io/badge/production--ready-42-brightgreen)
![Auditierte MCP-Repos](https://img.shields.io/badge/auditierte%20MCP--Repos-44-purple)
![Legacy](https://img.shields.io/badge/legacy%20%2F%20archiviert-2-lightgrey)
![Lizenz](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.11--3.13-blue)
![Protokoll](https://img.shields.io/badge/protocol-MCP-orange)
![Daten](https://img.shields.io/badge/data-Swiss%20Open%20Data-red)
![Audit](https://img.shields.io/badge/quality-mcp--audit--skill-purple)

> Ein kuratiertes Portfolio von Model-Context-Protocol-Servern (MCP), die KI-Agenten mit Schweizer öffentlichen und offenen Daten verbinden. Das Portfolio wird als auditierbares Inventar gepflegt, nicht als lose Sammlung von Experimenten.

[🇬🇧 English version](README.md)

> ⚠️ **Disclaimer - Unabhängigkeit dieses Projekts**
>
> Dies ist ein **persönliches Open-Source-Projekt** von Hayal Oezkan. Es wird privat, in privater Zeit und mit privater Infrastruktur entwickelt. Es ist **kein** offizielles Projekt der Stadt Zürich, des Schulamts, der KI-Fachgruppe der Stadtverwaltung Zürich oder einer anderen öffentlichen Institution. Verweise auf kommunale oder eidgenössische Strategien dienen nur als beschreibender Kontext. Sie bedeuten keine Empfehlung, keinen Auftrag, keine Zugehörigkeit und keinen Produktivbetrieb durch eine Institution.

---

## Aktueller Stand

Zuletzt geprüft: **2026-07-28**

| Kennzahl | Aktueller Wert |
|---|---:|
| Aktive Portfolio-Server | 42 |
| Production-ready aktive Server | 42 |
| MCP-Server-Repos mit mindestens einem Audit | 44 |
| Legacy / archivierte MCP-Server-Repos | 2 |
| Audit-Tooling-Repos | 2 |
| `opendata.swiss`-Datensätze | 14'551 via `package_search?rows=0` |
| Maschinenlesbare Quelle der Wahrheit | [`portfolio.json`](portfolio.json) |
| MCP-Registry-Einträge (generiert) | [`registry/`](registry/) |
| Publishing-Runbook | [`RUNBOOK.md`](RUNBOOK.md) |
| Promotion & Distribution | [`PROMOTION.md`](PROMOTION.md) |
| Client-Install-Snippets | [`docs/INSTALL.md`](docs/INSTALL.md) |
| `opendata.swiss`-Showcase-Eingabe | [`docs/SHOWCASE.md`](docs/SHOWCASE.md) |
| Pflicht-Topic für Auffindbarkeit | [`swiss-public-data-mcp`](https://github.com/topics/swiss-public-data-mcp) |
| MCP-Spec-Baseline für neue Audits | [`2025-11-25`](https://modelcontextprotocol.io/specification/versioning) |

Alle entwickelten MCP-Server-Repositories in diesem Inventar haben mindestens ein Audit durchlaufen, und jeder aktive Server ist production ready. Zwei Repositories sind **auf GitHub archiviert** (read-only) und stehen separat unter [Legacy / Abgelöst](#-legacy--abgelöst), damit keine aktive Tabellenzeile auf ein Repository zeigt, das keine Änderungen mehr annimmt.

Das Portfolio unterscheidet bewusst zwischen **Kernservern für Schweizer öffentliche Daten** und **angrenzenden Kontextservern**. Kontextserver wie globale Bildungsdaten oder Tech-Signal-Monitoring sind in kombinierten Workflows nützlich, werden aber nicht als Schweizer Verwaltungsdaten ausgegeben.

Jede Server-Zeile verlinkt das **offizielle Datenportal bzw. die API, die der Server liest**. Kein Server hostet, spiegelt oder republiziert Daten: Jeder ist ein schlanker, nur lesender Client für einen öffentlichen Endpunkt, und die publizierende Organisation bleibt die massgebliche Quelle.

---

## Warum es dieses Portfolio gibt

**Das Problem.** `opendata.swiss` listet rund 14'500 öffentliche Datensätze. Dazu kommt eine breitere Schweizer Datenlandschaft: GeoAdmin, Fedlex, SNB-Datenportal, BAFU, BFS PxWeb, swisstopo, parlamentarisches OData, kantonale Gesetzessammlungen, städtische Open-Data-Portale und sektorspezifische APIs. Jede spricht einen eigenen Dialekt — CKAN, PxWeb, SPARQL, OData, OGC, OpenDataSoft, individuelle REST-Schnittstellen. Das Publizieren der Daten war die erste Meile. Sie *ohne Entwicklerin oder Entwickler nutzbar* zu machen, ist die letzte Meile — und die fehlt bisher.

**Die Lücke, die geschlossen wird.** Ein KI-Assistent kann kein Portal durchblättern, kein Schema lesen und keine Query erraten. Er braucht pro Quelle eine kleine, typisierte, dokumentierte Schnittstelle. Genau das liefert dieses Portfolio: Jeder Server übersetzt eine öffentliche Datenquelle oder eine kohärente Quellenfamilie in MCP-Tools, die Clients wie Claude Desktop, VS Code + Continue, Cursor, Windsurf oder eigene Agenten direkt aufrufen. Nichts wird kopiert oder neu gehostet — jeder Server ist ein schlanker, nur lesender Client, und die publizierende Organisation bleibt die massgebliche Quelle.

**Für wen.** Öffentliche Verwaltungen, die prüfen, was Open Data in einem KI-Assistenten leisten kann; Journalistinnen und Forschende, die offizielle Quellen gegeneinander prüfen müssen; Civic-Tech-Entwickelnde, die sonst denselben API-Client zum fünften Mal schreiben; und alle, die eine Frage in normaler Sprache stellen wollen, statt vier API-Aufrufe von Hand zusammenzusetzen.

**Wie das konkret aussieht.** Die Frage *«Welche Schulhäuser der Stadt Zürich haben noch keine Glasfaser, wie verteilen sich die Schülerzahlen auf die Schulkreise, und was verlangt das kantonale Recht?»* berührt [Open Data Zürich](https://data.stadt-zuerich.ch/), die kantonale Bildungsstatistik und die Zürcher Gesetzessammlung. Ohne MCP sind das drei Integrationen und ein halber Arbeitstag. Mit MCP antworten drei Server in einem Gespräch — jeder mit Verweis auf seine offizielle Quelle.

**Warum ein Portfolio statt eines Servers.** Der Wert entsteht in der Kombination: ÖV plus Strassenmobilität wird zur multimodalen Routenplanung; Statistik plus Geodaten ermöglicht räumliche Analyse; Bildung plus Recht plus Parlamentsdaten unterstützt Policy-Recherche. Ein einzelner Monolith liesse sich weder sauber auditieren noch versionieren noch stückweise übernehmen — 42 kleine Server schon.

---

## Zürich-Fokus

Stadt und Kanton Zürich sind der am tiefsten abgedeckte Bereich des Portfolios — und sein Ausgangspunkt: Die ursprüngliche Frage war, was kommunale Open Data in einem KI-Assistenten tatsächlich leisten. Drei Server lesen direkt aus den offiziellen Zürcher Portalen.

<!-- BEGIN GENERATED: zurich-spotlight -->
| Server | Offizielles Datenportal | Abdeckung |
|---|---|---|
| [zurich-opendata-mcp](https://github.com/malkreide/zurich-opendata-mcp) | [Open Data Zürich](https://data.stadt-zuerich.ch/) | Stadt Zürich: Wetter, Luftqualität, Parkierung, Geodaten, Gemeinderat, Tourismus |
| [zh-education-mcp](https://github.com/malkreide/zh-education-mcp) | [Bildungsstatistik Kanton Zürich](https://www.zh.ch/de/bildung.html) | Bildungsdaten von Kanton und Stadt Zürich: Schulen, Statistik, Infrastruktur |
| [openlex-mcp](https://github.com/malkreide/openlex-mcp) | [Zürcher Gesetzessammlung (ZH-Lex)](https://www.zh.ch/de/politik-staat/gesetze-beschluesse.html) | Zürcher Gesetzessammlung via ZH-Lex mit Volltextsuche und Artikelextraktion |
<!-- END GENERATED: zurich-spotlight -->

Darüber hinaus fliessen [Open-Data-Zürich](https://data.stadt-zuerich.ch/)-Datensätze auch über `swiss-statistics-mcp`, `swiss-housing-mcp` und `swiss-electricity-mcp` (ewz-Tarife) ein. Ein durchgespieltes Beispiel liefert das Szenario [Schulinfrastruktur-Audit](#kombinationsszenarien).

---

## Strategischer Kontext

Das Portfolio entstand bottom-up aus Integrationsbedarf, nicht top-down aus einem Strategiepapier. Trotzdem passen die technischen Entscheidungen zu mehreren Digitalstrategien:

| Strategie | Beitrag des Portfolios |
|---|---|
| [Strategien Zürich 2040](https://www.stadt-zuerich.ch/de/politik-und-verwaltung/politik-und-recht/strategie-politikfelder/zuerich-2040.html) | Macht aus veröffentlichten offenen Daten agenten-nutzbare offene Daten. |
| [Digitalisierungsstrategie Stadt Zürich 2024](https://www.stadt-zuerich.ch/content/dam/web/de/politik-verwaltung/stadtverwaltung/fd/digitalisierungsstrategie.pdf) | Unterstützt nutzungsorientierte digitale Services, Informationsaustausch und verantwortungsvolle Datennutzung, ohne bestehende APIs neu zu bauen. |
| [SB021 - Strategie Einsatz von KI-Systemen in der Bundesverwaltung](https://www.bk.admin.ch/bk/de/home/digitale-transformation-ikt-lenkung/vorgaben/sb021-strategie-einsatz-von-ki-systemen-in-der-bundesverwaltung.html) | Bietet ein öffentlich lesbares Kompetenzartefakt mit expliziter Audit- und Risikomethodik. |
| [Strategie Digitale Schweiz 2026](https://www.admin.ch/de/newnsb/d6evGIoTYTmY4VMGk0-v0) | Erhöht den praktischen Nutzen öffentlicher digitaler Infrastruktur, indem Datenquellen über ein gemeinsames Protokoll LLM-konsumierbar werden. |

Diese Links sind Kontext, keine Autorisierung. Das Repository bleibt ein privates Open-Source-Projekt.

---

## Qualität & Audit-Tooling

Die Auditmethodik ist jetzt mit dem öffentlichen [`mcp-audit-skill`](https://github.com/malkreide/mcp-audit-skill) verknüpft, statt als interner Katalog beschrieben zu werden. Ergänzt wird sie durch [`mcp-continuous-auditor`](https://github.com/malkreide/mcp-continuous-auditor), der kontinuierliche CI-Audits gegen MCP-Server ausführt und promptfoo als deterministische Ground Truth nutzt. Der Skill dokumentiert aktuell **68 Checks in acht Kategorien**:

| Kategorie | Abdeckung |
|---|---|
| `ARCH` | Tool-Design, Annotationen, Idempotenz, Repo-Struktur, Spec-Version |
| `SDK` | FastMCP / TypeScript / Zod / Lifecycle |
| `SEC` | OAuth-Proxy-Risiken, Confused-Deputy, SSRF, Session-Hijacking, Prompt-Injection-Flächen, Secrets |
| `SCALE` | Transport, Statelessness, Containerisierung, Load Balancing, Gateway-Kompatibilität |
| `OBS` | Logging, Fehler, SIEM, Tracing, Trace-Korrelation |
| `HITL` | Sampling und Human-in-the-Loop-Verhalten |
| `CH` | Schweizer DSG / EDÖB / Public-Sector-Compliance |
| `OPS` | Teststrategie, Dokumentation, Phasenarchitektur, Release-Hygiene |

Der Audit-Skill ist **kein** Vulnerability-Scanner und **kein** Compliance-Zertifikat. Er macht Review-Methodik reproduzierbar. Architektururteile bleiben menschlich.

### Audit-Gate

Das Portfolio trennt jetzt Server-Reife von Audit-Nachweis:

| Feld | Bedeutung |
|---|---|
| Status | Laufzeit- und Dokumentationsreife des Servers. |
| Audit | Veröffentlichter Nachweis für das Audit-Gate. |

Jede aktive Server-Zeile verlinkt in der Spalte `Audit` direkt auf das entsprechende GitHub-Audit-Verzeichnis. Die meisten Repositories verwenden `audits/`; `swiss-culture-mcp` verwendet `audit/`, `bag-epl-mcp` und `swiss-food-safety-mcp` verwenden `docs/audit/`. Die beiden archivierten Repositories stehen separat unter [Legacy / Abgelöst](#-legacy--abgelöst); ihre Audit-Nachweise bleiben öffentlich, sind aber mit dem Repository eingefroren.

Jeder veröffentlichte Audit soll Metadaten wie diese enthalten:

```yaml
audit:
  server: swiss-transport-mcp
  repo: https://github.com/malkreide/swiss-transport-mcp
  audited_commit: "<commit-sha>"
  audit_skill: https://github.com/malkreide/mcp-audit-skill
  audit_skill_version: "0.1.x"
  catalogue_checks: 68
  mcp_spec_version: "2025-11-25"
  profile:
    transport: ["stdio", "streamable-http"]
    auth_model: "no-auth"
    data_class: "public-open-data"
    write_access: false
    deployment: ["local", "cloud-ready"]
  gate: "no critical/high findings open"
  audited_at: "YYYY-MM-DD"
```

---

## Server-Portfolio

<!-- BEGIN GENERATED: server-portfolio -->
**Status-Legende:** ✅ Production ready und mindestens einmal auditiert · 🔐 API-Credentials nötig · 🧭 angrenzende Kontextquelle · 🗄️ Legacy, auf GitHub archiviert oder abgelöst

### 🚆 Transport & Mobilität

| Server | Datenquelle | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|---|
| [swiss-transport-mcp](https://github.com/malkreide/swiss-transport-mcp) | [Open Data Platform Mobility Switzerland](https://opentransportdata.swiss/) | OJP 2.0 Journey Planning, SIRI-SX-Störungen, Auslastung, Tarife, Zugformation | *"Frühester Zug Zürich -> Bern morgen um 8 Uhr?"* | ✅ | [audits/](https://github.com/malkreide/swiss-transport-mcp/tree/main/audits) |
| [swiss-road-mobility-mcp](https://github.com/malkreide/swiss-road-mobility-mcp) | [Open Data Platform Mobility Switzerland / ASTRA](https://opentransportdata.swiss/) | GBFS Sharing-Mobilität, EV-Ladestationen, DATEX-II-Verkehr, Park & Rail | *"Freie E-Bikes nahe Zürich HB jetzt?"* | ✅ | [audits/](https://github.com/malkreide/swiss-road-mobility-mcp/tree/main/audits) |
| [sbb-opendata-mcp](https://github.com/malkreide/sbb-opendata-mcp) | [SBB Open Data](https://data.sbb.ch/) | SBB Open Data via OpenDataSoft | *"Pünktlichkeitsstatistik für IC 1 im letzten Monat?"* | ✅ | [audits/](https://github.com/malkreide/sbb-opendata-mcp/tree/main/audits) |

### ⚡ Energie & Infrastruktur

| Server | Datenquelle | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|---|
| [swiss-energy-mcp](https://github.com/malkreide/swiss-energy-mcp) | [BFE via GeoAdmin-API](https://api3.geo.admin.ch/) | Schweizer Energiedaten via BFE/SFOE und GeoAdmin REST APIs | *"Welche Wasserkraftwerke liegen nahe Wädenswil?"* | ✅ | [audits/](https://github.com/malkreide/swiss-energy-mcp/tree/main/audits) |
| [swiss-electricity-mcp](https://github.com/malkreide/swiss-electricity-mcp) | [BFE Energiedashboard / ElCom](https://energiedashboard.admin.ch/) | BFE-Energiedashboard, ElCom-Tarife, öffentliche Verbrauchsdaten | *"Wie haben sich ewz-Stromtarife für Kategorie C3 seit 2019 entwickelt?"* | ✅ | [audits/](https://github.com/malkreide/swiss-electricity-mcp/tree/main/audits) |

### 🌿 Umwelt & Klima

| Server | Datenquelle | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|---|
| [swiss-environment-mcp](https://github.com/malkreide/swiss-environment-mcp) | [BAFU / NABEL](https://www.bafu.admin.ch/) | BAFU-Umweltdaten, NABEL-Luftqualität, Hydrologie | *"PM2.5-Werte in Zürich in den letzten 7 Tagen?"* | ✅ | [audits/](https://github.com/malkreide/swiss-environment-mcp/tree/main/audits) |
| [wsl-envidat-mcp](https://github.com/malkreide/wsl-envidat-mcp) | [WSL EnviDat](https://www.envidat.ch/) | WSL / EnviDat-Umweltforschungsdaten via CKAN | *"Datensätze zu alpinem Permafrost von WSL?"* | ✅ | [audits/](https://github.com/malkreide/wsl-envidat-mcp/tree/main/audits) |
| [meteoswiss-mcp](https://github.com/malkreide/meteoswiss-mcp) | [MeteoSchweiz Open Data](https://opendatadocs.meteoswiss.ch/) | MeteoSwiss Open Data für Wetter, Klimanormwerte, Warnungen | *"War die Bise in Zürich letzten Winter ungewöhnlich stark?"* | ✅ | [audits/](https://github.com/malkreide/meteoswiss-mcp/tree/main/audits) |

### ⚖️ Recht, Gerichte & Regulierung

| Server | Datenquelle | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|---|
| [fedlex-mcp](https://github.com/malkreide/fedlex-mcp) | [Fedlex](https://www.fedlex.admin.ch/) | Bundesrecht via Fedlex SPARQL Endpoint | *"Was sagt Art. 62 BV über öffentliche Bildung?"* | ✅ | [audits/](https://github.com/malkreide/fedlex-mcp/tree/main/audits) |
| [openlex-mcp](https://github.com/malkreide/openlex-mcp) | [Zürcher Gesetzessammlung (ZH-Lex)](https://www.zh.ch/de/politik-staat/gesetze-beschluesse.html) | Zürcher Gesetzessammlung via ZH-Lex mit Volltextsuche und Artikelextraktion | *"Welche Zürcher Gesetze regeln Schulzuständigkeiten?"* | ✅ | [audits/](https://github.com/malkreide/openlex-mcp/tree/master/audits) |
| [swiss-courts-mcp](https://github.com/malkreide/swiss-courts-mcp) | [entscheidsuche.ch](https://entscheidsuche.ch/) | Schweizer Gerichtsentscheide via entscheidsuche.ch, inklusive Bundes- und Kantonsgerichte | *"Neue Bundesgerichtsentscheide zu Schultransport?"* | ✅ | [audits/](https://github.com/malkreide/swiss-courts-mcp/tree/master/audits) |
| [register-mcp](https://github.com/malkreide/register-mcp) | [Handelsregister (Zefix)](https://www.zefix.admin.ch/) | Zefix-Handelsregister und UID-Lookup | *"Aktive IT-Firmen in Zürich Kreis 5?"* | ✅ | [audits/](https://github.com/malkreide/register-mcp/tree/main/audits) |
| [amtsblatt-mcp](https://github.com/malkreide/amtsblatt-mcp) | [amtsblattportal.ch (SHAB)](https://www.amtsblattportal.ch/) | amtsblattportal.ch (SHAB + kantonale Amtsblätter) — Beschaffung und amtliche Bekanntmachungen, Rubriken mit Personendaten bewusst ausgeschlossen · ↔ verwandt: [`swiss-procurement-mcp`](https://github.com/malkreide/swiss-procurement-mcp) | *"Welche öffentlichen IT-Ausschreibungen wurden in den letzten drei Monaten in Basel-Stadt publiziert?"* | ✅ | [audits/](https://github.com/malkreide/amtsblatt-mcp/tree/main/audits) |
| [swiss-procurement-mcp](https://github.com/malkreide/swiss-procurement-mcp) | [simap.ch](https://www.simap.ch/) | simap.ch Beschaffungs-API: Ausschreibungen und Zuschläge aller Kantone und des Bundes, read-only · ↔ verwandt: [`amtsblatt-mcp`](https://github.com/malkreide/amtsblatt-mcp) | *"Welche Schulhaus-Ausschreibungen hat die Stadt Zürich 2026 publiziert, und welche BKP-Kategorien betreffen sie?"* | ✅ | [audits/](https://github.com/malkreide/swiss-procurement-mcp/tree/main/audits) |
| [swiss-ip-mcp](https://github.com/malkreide/swiss-ip-mcp) | [IGE/IPI Swissreg](https://www.swissreg.ch/) | IGE/IPI Swissreg: Marken, Patente, SPCs | *"Aktive Schweizer Marken mit 'Zurich' in Klasse 41?"* | ✅ 🔐 | [audits/](https://github.com/malkreide/swiss-ip-mcp/tree/main/audits) |

### 🧩 Semantik, Metadaten & Interoperabilität

| Server | Datenquelle | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|---|
| [termdat-mcp](https://github.com/malkreide/termdat-mcp) | [TERMDAT](https://www.termdat.bk.admin.ch/) | Amtliche mehrsprachige Terminologie der Bundesverwaltung (TERMDAT) | *"Wie heissen die für Bildung zuständigen Direktionen der Deutschschweizer Kantone offiziell auf Französisch und Italienisch?"* | ✅ | [audits/](https://github.com/malkreide/termdat-mcp/tree/main/audits) |
| [i14y-mcp](https://github.com/malkreide/i14y-mcp) | [I14Y-Interoperabilitätsplattform](https://www.i14y.admin.ch/) | I14Y-Interoperabilitätsplattform, nationaler Metadatenkatalog der Schweiz (DCAT-AP) | *"Welche Datensätze führt der I14Y-Katalog zur Schweizer Bildungsstatistik?"* | ✅ | [audits/](https://github.com/malkreide/i14y-mcp/tree/main/audits) |
| [lindas-mcp](https://github.com/malkreide/lindas-mcp) | [LINDAS Linked Data Service](https://lindas.admin.ch/) | LINDAS Linked-Data-Wissensgraph: ~2.000 föderale SPARQL-Datenwürfel mit aufgelösten Labels | *"Welche statistischen Datenwürfel veröffentlicht LINDAS zur Schweizer Waldfläche, und wer ist Herausgeber?"* | ✅ | [audits/](https://github.com/malkreide/lindas-mcp/tree/main/audits) |

### 📊 Statistik & Geodaten

| Server | Datenquelle | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|---|
| [swiss-statistics-mcp](https://github.com/malkreide/swiss-statistics-mcp) | [BFS STAT-TAB (PxWeb)](https://www.pxweb.bfs.admin.ch/) | BFS STAT-TAB PxWeb API für amtliche Schweizer Statistik | *"Bevölkerung der Schweizer Gemeinden nach Kanton, 2023?"* | ✅ | [audits/](https://github.com/malkreide/swiss-statistics-mcp/tree/main/audits) |
| [zurich-opendata-mcp](https://github.com/malkreide/zurich-opendata-mcp) | [Open Data Zürich](https://data.stadt-zuerich.ch/) | Stadt Zürich: Wetter, Luftqualität, Parkierung, Geodaten, Gemeinderat, Tourismus | *"Welche Schulgebäude in Zürich haben noch keine Glasfaser?"* | ✅ | [audits/](https://github.com/malkreide/zurich-opendata-mcp/tree/main/audits) |
| [swisstopo-mcp](https://github.com/malkreide/swisstopo-mcp) | [swisstopo / geo.admin.ch](https://www.swisstopo.admin.ch/) | Bundesgeodaten: Geocoding, Höhe, STAC, WMTS, ÖREB und mehr | *"Wie sieht das Höhenprofil zwischen Zürich HB und Uetliberg aus?"* | ✅ | [audits/](https://github.com/malkreide/swisstopo-mcp/tree/master/audits) |
| [swiss-housing-mcp](https://github.com/malkreide/swiss-housing-mcp) | [Eidg. Gebäude- und Wohnungsregister (GWR)](https://www.housing-stat.ch/) | GWR/RegBL eidgenössisches Gebäude- und Wohnungsregister: Gebäude, Wohnungen und Bau-Pipeline | *"Wie viele Wohnungen mit 4+ Zimmern wurden in der Stadt Zürich seit 2020 neu gebaut?"* | ✅ | [audits/](https://github.com/malkreide/swiss-housing-mcp/tree/main/audits) |

### 🎓 Bildung & Forschung

| Server | Datenquelle | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|---|
| [global-education-mcp](https://github.com/malkreide/global-education-mcp) | [UNESCO UIS / OECD](https://uis.unesco.org/) | UNESCO UIS und OECD Education at a Glance | *"Sek-II-Abschlussquoten CH vs. OECD-Durchschnitt?"* | ✅ 🧭 | [audits/](https://github.com/malkreide/global-education-mcp/tree/main/audits) |
| [zh-education-mcp](https://github.com/malkreide/zh-education-mcp) | [Bildungsstatistik Kanton Zürich](https://www.zh.ch/de/bildung.html) | Bildungsdaten von Kanton und Stadt Zürich: Schulen, Statistik, Infrastruktur | *"Wie verteilen sich Schülerzahlen auf die sieben Zürcher Schulkreise?"* | ✅ | [audits/](https://github.com/malkreide/zh-education-mcp/tree/main/audits) |
| [swiss-academic-libraries-mcp](https://github.com/malkreide/swiss-academic-libraries-mcp) | [swisscovery (SLSP)](https://swisscovery.slsp.ch/) | swisscovery, e-rara, e-periodica, e-manuscripta via SRU/OAI-PMH | *"Digitalisierte Schweizer Karten des 18. Jahrhunderts in e-rara?"* | ✅ | [audits/](https://github.com/malkreide/swiss-academic-libraries-mcp/tree/main/audits) |
| [eth-library-mcp](https://github.com/malkreide/eth-library-mcp) | [ETH-Bibliothek](https://library.ethz.ch/) | ETH Library Discovery und Persons APIs | *"ETH-Publikationen zu urbanen Hitzeinseln seit 2020?"* | ✅ | [audits/](https://github.com/malkreide/eth-library-mcp/tree/main/audits) |
| [swiss-holidays-mcp](https://github.com/malkreide/swiss-holidays-mcp) | [OpenHolidays API](https://www.openholidaysapi.org/) | openholidaysapi.org: Schul- und öffentliche Feiertage für alle 26 Kantone | *"Wann sind die Herbstferien 2025 im Kanton Zürich?"* | ✅ | [audits/](https://github.com/malkreide/swiss-holidays-mcp/tree/main/audits) |

### 💰 Wirtschaft & Finanzen

| Server | Datenquelle | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|---|
| [swiss-snb-mcp](https://github.com/malkreide/swiss-snb-mcp) | [SNB-Datenportal](https://data.snb.ch/) | SNB-Datenportal: Wechselkurse, Bilanz, Leitzins, SARON, Geldmengen | *"EUR/CHF seit 2015 und aktueller SNB-Leitzins?"* | ✅ | [audits/](https://github.com/malkreide/swiss-snb-mcp/tree/main/audits) |
| [swiss-efv-mcp](https://github.com/malkreide/swiss-efv-mcp) | [Eidg. Finanzverwaltung (EFV)](https://www.efv.admin.ch/) | Schweizer Bundesfinanzen (EFV): Haushalt, Schulden, Prognosen sowie Ausgaben nach Aufgabengebiet und Institution | *"Wie hat sich der Bundessaldo seit der SNB-Zinswende 2022 entwickelt, und in welche Aufgabengebiete floss das Ausgabenwachstum?"* | ✅ | [audits/](https://github.com/malkreide/swiss-efv-mcp/tree/main/audits) |
| [seco-labor-mcp](https://github.com/malkreide/seco-labor-mcp) | [SECO / AMSTAT](https://www.amstat.ch/) | SECO-Arbeitsmarkt: Arbeitslosigkeit, offene Stellen, Erwerbsindikatoren | *"Arbeitslosenquote Kanton Zürich vs. Schweiz in den letzten 12 Monaten?"* | ✅ | [audits/](https://github.com/malkreide/seco-labor-mcp/tree/main/audits) |

### 🎭 Kultur & Medien

| Server | Datenquelle | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|---|
| [swiss-culture-mcp](https://github.com/malkreide/swiss-culture-mcp) | [Bundesamt für Kultur (BAK)](https://www.bak.admin.ch/) | BAK-Kulturerbe, ISOS, lebendige Traditionen, RSS | *"UNESCO-gelistete lebendige Traditionen im Kanton Zürich?"* | ✅ | [audit/](https://github.com/malkreide/swiss-culture-mcp/tree/main/audit) |
| [swiss-cultural-heritage-mcp](https://github.com/malkreide/swiss-cultural-heritage-mcp) | [SIK-ISEA / Schweizerisches Nationalmuseum](https://www.sik-isea.ch/) | Kulturerbe-Inventare, Denkmallisten, archäologische Register | *"Geschützte Baudenkmäler in Zürich Kreis 6?"* | ✅ | [audits/](https://github.com/malkreide/swiss-cultural-heritage-mcp/tree/main/audits) |
| [bakom-mcp](https://github.com/malkreide/bakom-mcp) | [BAKOM](https://www.bakom.admin.ch/) | BAKOM Open Data zu Telekommunikation und Medien | *"Welche Gemeinden haben noch keine 100 Mbit/s Breitbandabdeckung?"* | ✅ | [audits/](https://github.com/malkreide/bakom-mcp/tree/main/audits) |
| [srgssr-mcp](https://github.com/malkreide/srgssr-mcp) | [SRG-SSR-Developer-Portal](https://developer.srgssr.ch/) | SRG SSR: Wetter, Video, Audio, EPG, Polis | *"Neuste SRF-Beiträge zur Bildungspolitik?"* | ✅ | [audits/](https://github.com/malkreide/srgssr-mcp/tree/main/audits) |
| [news-monitor-mcp](https://github.com/malkreide/news-monitor-mcp) | [RSS-Feeds öffentlicher Medien](https://www.srf.ch/) | Aggregiertes News-Monitoring über Schweizer Public-Media-RSS | *"Top drei bildungspolitische Schweizer Medienstories diese Woche?"* | ✅ 🧭 | [audits/](https://github.com/malkreide/news-monitor-mcp/tree/main/audits) |

### 🏥 Gesundheit

| Server | Datenquelle | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|---|
| [bag-health-mcp](https://github.com/malkreide/bag-health-mcp) | [Bundesamt für Gesundheit (BAG)](https://www.bag.admin.ch/) | BAG Public-Health Open Data: Indikatoren, Programme, Statistik | *"Impfquote nach Kanton für die letzte Berichtsperiode?"* | ✅ | [audits/](https://github.com/malkreide/bag-health-mcp/tree/main/audits) |
| [bag-epl-mcp](https://github.com/malkreide/bag-epl-mcp) | [Spezialitätenliste (BAG)](https://www.spezialitaetenliste.ch/) | BAG EPL: Spezialitätenliste, Medikamente, Vergütungsdaten | *"Welche Medikamente kamen in den letzten sechs Monaten auf die Spezialitätenliste?"* | ✅ | [docs/audit/](https://github.com/malkreide/bag-epl-mcp/tree/main/docs/audit) |

### 🍽️ Lebensmittelsicherheit

| Server | Datenquelle | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|---|
| [swiss-food-safety-mcp](https://github.com/malkreide/swiss-food-safety-mcp) | [Bundesamt für Lebensmittelsicherheit (BLV)](https://www.blv.admin.ch/) | BLV Open Data zu Lebensmittelsicherheit und Veterinärkontrollen | *"Aktuelle Lebensmittelrückrufe in der Schweiz?"* | ✅ | [docs/audit/](https://github.com/malkreide/swiss-food-safety-mcp/tree/main/docs/audit) |

### 🗳️ Demokratie & Transparenz

| Server | Datenquelle | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|---|
| [swiss-democracy-mcp](https://github.com/malkreide/swiss-democracy-mcp) | [Swissvotes](https://swissvotes.ch/) | Parlaments-OData, Swissvotes, Referenden, Abstimmungsresultate | *"Welche hängigen parlamentarischen Vorstösse betreffen KI in der Bildung?"* | ✅ | [audits/](https://github.com/malkreide/swiss-democracy-mcp/tree/main/audits) |
| [parlament-mcp](https://github.com/malkreide/parlament-mcp) | [Schweizer Parlament (Curia Vista)](https://www.parlament.ch/) | Curia-Vista-OData-API des Schweizer Parlaments | *"Welche Vorstösse zu KI in der Schule sind hängig?"* | ✅ | [audits/](https://github.com/malkreide/parlament-mcp/tree/main/audits) |
| [lobbywatch-mcp](https://github.com/malkreide/lobbywatch-mcp) | [Lobbywatch.ch](https://lobbywatch.ch/) | Lobbywatch.ch-Transparenzdaten zu Parlamentsmitgliedern, Interessenbindungen, Zutrittsbadges | *"Welche WBK-Mitglieder haben Bezüge zu privaten Bildungsanbietern?"* | ✅ 🧭 | [audits/](https://github.com/malkreide/lobbywatch-mcp/tree/main/audits) |

### 🛰️ Tech Intelligence

| Server | Datenquelle | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|---|
| [hn-tech-signal-mcp](https://github.com/malkreide/hn-tech-signal-mcp) | [Hacker News API](https://news.ycombinator.com/) | Hacker-News-Signalextraktion für Technologie-Trendmonitoring | *"Welche AI-Infrastrukturthemen werden diese Woche am meisten diskutiert?"* | ✅ 🧭 | [audits/](https://github.com/malkreide/hn-tech-signal-mcp/tree/main/audits) |

### 🗄️ Legacy / Abgelöst

| Server | Datenquelle | Behandlung | Grund |
|---|---|---|---|
| [swiss-geodata-mcp](https://github.com/malkreide/swiss-geodata-mcp) | [geo.admin.ch](https://www.geo.admin.ch/) | Auf GitHub archiviert (read-only) / abgelöst | Die Abdeckung der Bundesgeodaten wurde in `swisstopo-mcp` konsolidiert, das dieselben geo.admin.ch/swisstopo-APIs bedient. Das Repository bleibt zur Nachvollziehbarkeit öffentlich und auditiert; für neue Integrationen `swisstopo-mcp` verwenden. Abgelöst durch [`swisstopo-mcp`](https://github.com/malkreide/swisstopo-mcp). |
| [MCP-Server-for-patent-research-](https://github.com/malkreide/MCP-Server-for-patent-research-) | [EPO OPS / Espacenet](https://www.epo.org/) | Auf GitHub archiviert (read-only) / Migrationskandidat | Älterer auditierter Patentrecherche-Server mit breitem EPO/Swissreg-Scope und Namensinkonsistenzen. Auffindbar lassen, aber für das aktuelle Portfolio `swiss-ip-mcp` bevorzugen, solange der alte Repo nicht umbenannt und an die aktuellen Portfolio-Konventionen angepasst ist. Abgelöst durch [`swiss-ip-mcp`](https://github.com/malkreide/swiss-ip-mcp). |
<!-- END GENERATED: server-portfolio -->

---

## Architekturprinzipien

**No-Auth-First** - Phase 1 jedes Kernservers soll nur offene, unauthentifizierte Endpunkte verwenden. Authentifizierte APIs können später mit Graceful Degradation ergänzt werden.

**Phasenarchitektur** - Server-READMEs sollen Phase 1 No-Auth, Phase 2 Auth/Advanced und Phase 3 Production Hardening klar unterscheiden.

**Dual Transport** - Server sollen `stdio` für lokale Clients und, wo sinnvoll, Streamable HTTP für Cloud- oder Gateway-Deployment unterstützen.

**Standard-Stack** - Python-Server nutzen FastMCP, Pydantic v2, httpx, hatchling, `src/`-Layout, pytest mit `@pytest.mark.live`-Isolation, GitHub Actions CI für Python 3.11-3.13 und möglichst `uvx`-fähige Pakete.

**Zweisprachige Dokumentation** - Kernserver sollen `README.md` und `README.de.md` verlinkt aktuell halten.

**Audit-getriebene Qualität** - Production-ready-Status setzt mindestens ein abgeschlossenes Audit voraus. Aktive Server-Zeilen verlinken direkt auf ihr Audit-Evidence-Verzeichnis.

---

## Quickstart

Jeder Server ist unabhängig via `uvx` oder `pip` installierbar, sofern veröffentlicht. Exakte Paketnamen und Konfiguration stehen im jeweiligen Server-README.

Beispiel: `swiss-transport-mcp` in Claude Desktop eintragen:

```json
{
  "mcpServers": {
    "swiss-transport": {
      "command": "uvx",
      "args": ["swiss-transport-mcp"]
    }
  }
}
```

Für Server, die noch nicht auf PyPI liegen:

```bash
git clone https://github.com/malkreide/<server-name>
cd <server-name>
uv run mcp dev src/<package>/server.py
```

---

## Kombinationsszenarien

| Szenario | Benötigte Server | Beispielquery |
|---|---|---|
| Makroökonomischer Kontext | swiss-snb-mcp + swiss-statistics-mcp + seco-labor-mcp | *"CHF/EUR seit 2015 zusammen mit Schweizer BIP, CPI und Arbeitslosigkeit?"* |
| Multimodaler Pendelplaner | swiss-transport-mcp + swiss-road-mobility-mcp + sbb-opendata-mcp | *"Zug von Wädenswil nach Zürich HB, dann E-Bike zur ETH. Beste Option um 8:15 inklusive Pünktlichkeitsverlauf?"* |
| Schul-Infrastruktur-Audit | zh-education-mcp + zurich-opendata-mcp + swiss-statistics-mcp + swiss-electricity-mcp | *"Zürcher Schulen ohne Glasfaser, Schülerlast pro Schulkreis und Stromtarif-Exposition?"* |
| Bildungspolitische Recherche | global-education-mcp + fedlex-mcp + openlex-mcp + parlament-mcp + lobbywatch-mcp | *"Wie steht die Schweizer Sek-II-Quote im OECD-Vergleich, was verlangt das Recht, und welche parlamentarischen Akteure sind beteiligt?"* |
| Umweltbriefing | swiss-environment-mcp + meteoswiss-mcp + wsl-envidat-mcp + swisstopo-mcp | *"Aktuelle Luftqualität und Wetter in Zürich, plus Geodaten und WSL-Studien zu urbanen Hitzeinseln?"* |
| Gesundheitspolitischer Loop | bag-health-mcp + bag-epl-mcp + fedlex-mcp + swiss-democracy-mcp | *"Neue Einträge in der Spezialitätenliste, Impfquote nach Kanton und gesetzliche Grundlage für beides?"* |
| Energie-Standortkontext | swiss-energy-mcp + swiss-electricity-mcp + swisstopo-mcp + swiss-statistics-mcp | *"Welche Gemeinden verbinden hohes Solarpotenzial, Stromtarifdruck und Bevölkerungswachstum?"* |

---

## Repository-Map

Alle aktiven Server sollen den GitHub-Topic [`swiss-public-data-mcp`](https://github.com/topics/swiss-public-data-mcp) tragen. Das maschinenlesbare Inventar in [`portfolio.json`](portfolio.json) ist die kanonische Liste.

<!-- BEGIN GENERATED: repository-map -->
```text
malkreide/
├── swiss-public-data-mcp                 ← dieser Index
├── mcp-audit-skill                       ← Audit-Tooling, kein Server
├── mcp-continuous-auditor                ← Audit-Tooling, kein Server
│
├── Transport & Mobilität
│   ├── swiss-transport-mcp
│   ├── swiss-road-mobility-mcp
│   └── sbb-opendata-mcp
│
├── Energie & Infrastruktur
│   ├── swiss-energy-mcp
│   └── swiss-electricity-mcp
│
├── Umwelt & Klima
│   ├── swiss-environment-mcp
│   ├── wsl-envidat-mcp
│   └── meteoswiss-mcp
│
├── Recht, Gerichte & Regulierung
│   ├── fedlex-mcp
│   ├── openlex-mcp
│   ├── swiss-courts-mcp
│   ├── register-mcp
│   ├── amtsblatt-mcp
│   ├── swiss-procurement-mcp
│   └── swiss-ip-mcp
│
├── Semantik, Metadaten & Interoperabilität
│   ├── termdat-mcp
│   ├── i14y-mcp
│   └── lindas-mcp
│
├── Statistik & Geodaten
│   ├── swiss-statistics-mcp
│   ├── zurich-opendata-mcp
│   ├── swisstopo-mcp
│   └── swiss-housing-mcp
│
├── Bildung & Forschung
│   ├── global-education-mcp
│   ├── zh-education-mcp
│   ├── swiss-academic-libraries-mcp
│   ├── eth-library-mcp
│   └── swiss-holidays-mcp
│
├── Wirtschaft & Finanzen
│   ├── swiss-snb-mcp
│   ├── swiss-efv-mcp
│   └── seco-labor-mcp
│
├── Kultur & Medien
│   ├── swiss-culture-mcp
│   ├── swiss-cultural-heritage-mcp
│   ├── bakom-mcp
│   ├── srgssr-mcp
│   └── news-monitor-mcp
│
├── Gesundheit
│   ├── bag-health-mcp
│   └── bag-epl-mcp
│
├── Lebensmittelsicherheit
│   └── swiss-food-safety-mcp
│
├── Demokratie & Transparenz
│   ├── swiss-democracy-mcp
│   ├── parlament-mcp
│   └── lobbywatch-mcp
│
├── Tech Intelligence
│   └── hn-tech-signal-mcp
│
└── Legacy / Abgelöst
    ├── swiss-geodata-mcp                     ← 🗄️ auf GitHub archiviert (read-only)
    └── MCP-Server-for-patent-research-       ← 🗄️ auf GitHub archiviert (read-only)
```
<!-- END GENERATED: repository-map -->

---

## Maintenance-Roadmap

Die früheren Roadmap-Punkte für Zürcher kantonales Recht, Schweizer Gerichte und tiefere swisstopo-Geodaten sind ins Inventar gewandert, weil `openlex-mcp`, `swiss-courts-mcp` und `swisstopo-mcp` inzwischen existieren.

`swiss-geodata-mcp` und `MCP-Server-for-patent-research-` wurden auf GitHub archiviert und aus dem aktiven Inventar entfernt; ihre Nachfolger sind `swisstopo-mcp` bzw. `swiss-ip-mcp`.

Aktuelle Portfolio-Prioritäten:

- Alle verlinkten Audit-Verzeichnisse mit Report-Metadaten, Findings und Remediation Notes aktuell halten.
- Die Audit-Evidence der archivierten Repositories in die Nachfolger (`swisstopo-mcp`, `swiss-ip-mcp`) migrieren, damit die eingefrorenen Berichte nicht der einzige Nachweis bleiben.
- Das Pflicht-Topic `swiss-public-data-mcp` in allen Server-Repositories setzen; `swiss-efv-mcp` ist aktuell der einzige aktive Server ohne dieses Topic.
- In `amtsblatt-mcp` und `lobbywatch-mcp` eine explizite `LICENSE` publizieren — GitHub erkennt dort derzeit keine Standardlizenz.
- `mcp-audit-skill` und künftige Berichte auf MCP-Spec `2025-11-25` ausrichten; ältere Spec-Versionen in Audit-Metadaten erhalten.
- Entscheiden, ob `parlament-mcp` als spezialisierter Server bleibt oder in `swiss-democracy-mcp` aufgeht.
- Alle datengetriebenen README-Bereiche — Zürich-Spotlight, Server-Portfolio-Tabellen und Repository-Map — werden von [`scripts/generate_readme.py`](scripts/generate_readme.py) aus `portfolio.json` generiert; ein CI-Check (`--check`) verhindert Drift, unter anderem einen Server, der nach dem Archivieren seines Repositories noch als aktiv gelistet ist.

---

## Mitwirken

Bugreports und Feature Requests sind auf den jeweiligen Server-Repositories willkommen. Wer einen neuen MCP-Server für Schweizer offene Daten baut und hier listen möchte, sollte einen Issue mit kurzer Beschreibung, Repo-Link, Datenquellen und geplantem Auditprofil eröffnen.

Beim Ändern des Inventars [`portfolio.json`](portfolio.json) bearbeiten und `python scripts/generate_readme.py` ausführen, um die generierten README-Abschnitte zu aktualisieren. CI prüft die Synchronität via `python scripts/generate_readme.py --check`.

Siehe [`CONTRIBUTING.md`](CONTRIBUTING.md) für den vollständigen Contribution-Guide und [`SECURITY.md`](SECURITY.md) für das Melden von Sicherheitslücken.

---

## Lizenz

MIT License - siehe [LICENSE](LICENSE)

---

## Autor

**Hayal Oezkan** · [github.com/malkreide](https://github.com/malkreide)

> Erinnerung: Dies ist ein privates Open-Source-Projekt. Institutionelle Zugehörigkeiten in anderen öffentlichen Profilen des Autors sind für dieses Repository nicht relevant.
