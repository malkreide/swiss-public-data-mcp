# swiss-public-data-mcp

![Aktive Server](https://img.shields.io/badge/aktive%20Server-34-blue)
![Production Ready](https://img.shields.io/badge/production--ready-34-brightgreen)
![Auditierte MCP-Repos](https://img.shields.io/badge/auditierte%20MCP--Repos-35-purple)
![Legacy](https://img.shields.io/badge/legacy-1-lightgrey)
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

Zuletzt geprüft: **2026-06-04**

| Kennzahl | Aktueller Wert |
|---|---:|
| Aktive Portfolio-Server | 34 |
| Production-ready aktive Server | 34 |
| MCP-Server-Repos mit mindestens einem Audit | 35 |
| Legacy / abgelöste MCP-Server-Repos | 1 |
| Audit-Tooling-Repos | 1 |
| `opendata.swiss`-Datensätze | 14'551 via `package_search?rows=0` |
| Maschinenlesbare Quelle der Wahrheit | [`portfolio.json`](portfolio.json) |
| Pflicht-Topic für Auffindbarkeit | [`swiss-public-data-mcp`](https://github.com/topics/swiss-public-data-mcp) |
| MCP-Spec-Baseline für neue Audits | [`2025-11-25`](https://modelcontextprotocol.io/specification/versioning) |

Alle entwickelten MCP-Server-Repositories in diesem Inventar haben mindestens ein Audit durchlaufen. Alle aktiven Portfolio-Server sind production ready; der Legacy-Server bleibt als production-ready Migrationskandidat gelistet. Das Portfolio unterscheidet bewusst zwischen **Kernservern für Schweizer öffentliche Daten** und **angrenzenden Kontextservern**. Kontextserver wie globale Bildungsdaten oder Tech-Signal-Monitoring sind in kombinierten Workflows nützlich, werden aber nicht als Schweizer Verwaltungsdaten ausgegeben.

---

## Warum es dieses Portfolio gibt

`opendata.swiss` listet rund 14'500 öffentliche Datensätze. Dazu kommt eine breitere Schweizer Datenlandschaft: GeoAdmin, Fedlex, SNB-Datenportal, BAFU, BFS PxWeb, swisstopo, parlamentarisches OData, kantonale Gesetzessammlungen, städtische Open-Data-Portale und sektorspezifische APIs. Für KI-Agenten bleibt diese Landschaft faktisch unerreichbar, solange jede Quelle eine eigene Integration braucht.

Dieses Portfolio schliesst diese letzte Meile. Jeder Server übersetzt eine öffentliche Datenquelle oder eine kohärente Quellenfamilie in kleine, typisierte und dokumentierte MCP-Tools, die Clients wie Claude Desktop, VS Code + Continue, Cursor, Windsurf oder eigene Agenten direkt aufrufen können.

Der Wert liegt in der Kombination: ÖV plus Strassenmobilität wird zur multimodalen Routenplanung; Statistik plus Geodaten ermöglicht räumliche Analyse; Bildung plus Recht plus Parlamentsdaten unterstützt Policy-Recherche.

---

## Strategischer Kontext

Das Portfolio entstand bottom-up aus Integrationsbedarf, nicht top-down aus einem Strategiepapier. Trotzdem passen die technischen Entscheidungen zu mehreren Digitalstrategien:

| Strategie | Beitrag des Portfolios |
|---|---|
| [Strategien Zürich 2040](https://www.stadt-zuerich.ch/de/politik-und-verwaltung/politik-und-recht/strategie-politikfelder/zuerich-2040.html) | Macht aus veröffentlichten offenen Daten agenten-nutzbare offene Daten. |
| [Digitalisierungsstrategie Stadt Zürich 2024](https://www.stadt-zuerich.ch/content/dam/web/de/politik-verwaltung/stadtverwaltung/fd/digitalisierungsstrategie.pdf) | Unterstützt nutzungsorientierte digitale Services, Informationsaustausch und verantwortungsvolle Datennutzung, ohne bestehende APIs neu zu bauen. |
| [SB021 - Strategie Einsatz von KI-Systemen in der Bundesverwaltung](https://www.bk.admin.ch/bk/de/home/digitale-transformation-ikt-lenkung/vorgaben/sb021-strategie-einsatz-von-ki-systemen-in-der-bundesverwaltung.html) | Bietet ein öffentlich lesbares Kompetenzartefakt mit expliziter Audit- und Risikomethodik. |
| [Strategie Digitale Schweiz 2026](https://www.eda.admin.ch/de/newnsb/d6evGIoTYTmY4VMGk0-v0) | Erhöht den praktischen Nutzen öffentlicher digitaler Infrastruktur, indem Datenquellen über ein gemeinsames Protokoll LLM-konsumierbar werden. |

Diese Links sind Kontext, keine Autorisierung. Das Repository bleibt ein privates Open-Source-Projekt.

---

## Qualität & Audit-Tooling

Die Auditmethodik ist jetzt mit dem öffentlichen [`mcp-audit-skill`](https://github.com/malkreide/mcp-audit-skill) verknüpft, statt als interner Katalog beschrieben zu werden. Der Skill dokumentiert aktuell **68 Checks in acht Kategorien**:

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

Jede aktive Server-Zeile verlinkt in der Spalte `Audit` jetzt direkt auf das entsprechende GitHub-Audit-Verzeichnis. Die meisten Repositories verwenden `audits/`; `swiss-culture-mcp` verwendet `audit/`, `bag-epl-mcp` und `swiss-food-safety-mcp` verwenden `docs/audit/`. Das archivierte Legacy-Patent-Repository bleibt separat als Migrationskandidat gelistet.

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

**Status-Legende:** ✅ Production ready und mindestens einmal auditiert · 🔐 API-Credentials nötig · 🧭 angrenzende Kontextquelle · 🗄️ Legacy oder abgelöst

### 🚆 Transport & Mobilität

| Server | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|
| [swiss-transport-mcp](https://github.com/malkreide/swiss-transport-mcp) | OJP 2.0 Journey Planning, SIRI-SX-Störungen, Auslastung, Tarife, Zugformation | *"Frühester Zug Zürich -> Bern morgen um 8 Uhr?"* | ✅ | [audits/](https://github.com/malkreide/swiss-transport-mcp/tree/main/audits) |
| [swiss-road-mobility-mcp](https://github.com/malkreide/swiss-road-mobility-mcp) | GBFS Sharing-Mobilität, EV-Ladestationen, DATEX-II-Verkehr, Park & Rail | *"Freie E-Bikes nahe Zürich HB jetzt?"* | ✅ | [audits/](https://github.com/malkreide/swiss-road-mobility-mcp/tree/main/audits) |
| [sbb-opendata-mcp](https://github.com/malkreide/sbb-opendata-mcp) | SBB Open Data via OpenDataSoft | *"Pünktlichkeitsstatistik für IC 1 im letzten Monat?"* | ✅ | [audits/](https://github.com/malkreide/sbb-opendata-mcp/tree/main/audits) |

### ⚡ Energie & Infrastruktur

| Server | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|
| [swiss-energy-mcp](https://github.com/malkreide/swiss-energy-mcp) | Schweizer Energiedaten via BFE/SFOE und GeoAdmin REST APIs | *"Welche Wasserkraftwerke liegen nahe Wädenswil?"* | ✅ | [audits/](https://github.com/malkreide/swiss-energy-mcp/tree/main/audits) |
| [swiss-electricity-mcp](https://github.com/malkreide/swiss-electricity-mcp) | BFE-Energiedashboard, ElCom-Tarife, öffentliche Verbrauchsdaten | *"Wie haben sich ewz-Stromtarife für Kategorie C3 seit 2019 entwickelt?"* | ✅ | [audits/](https://github.com/malkreide/swiss-electricity-mcp/tree/main/audits) |

### 🌿 Umwelt & Klima

| Server | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|
| [swiss-environment-mcp](https://github.com/malkreide/swiss-environment-mcp) | BAFU-Umweltdaten, NABEL-Luftqualität, Hydrologie | *"PM2.5-Werte in Zürich in den letzten 7 Tagen?"* | ✅ | [audits/](https://github.com/malkreide/swiss-environment-mcp/tree/main/audits) |
| [wsl-envidat-mcp](https://github.com/malkreide/wsl-envidat-mcp) | WSL / EnviDat-Umweltforschungsdaten via CKAN | *"Datensätze zu alpinem Permafrost von WSL?"* | ✅ | [audits/](https://github.com/malkreide/wsl-envidat-mcp/tree/main/audits) |
| [meteoswiss-mcp](https://github.com/malkreide/meteoswiss-mcp) | MeteoSwiss Open Data für Wetter, Klimanormwerte, Warnungen | *"War die Bise in Zürich letzten Winter ungewöhnlich stark?"* | ✅ | [audits/](https://github.com/malkreide/meteoswiss-mcp/tree/main/audits) |

### ⚖️ Recht, Gerichte & Regulierung

| Server | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|
| [fedlex-mcp](https://github.com/malkreide/fedlex-mcp) | Bundesrecht via Fedlex SPARQL Endpoint | *"Was sagt Art. 62 BV über öffentliche Bildung?"* | ✅ | [audits/](https://github.com/malkreide/fedlex-mcp/tree/main/audits) |
| [openlex-mcp](https://github.com/malkreide/openlex-mcp) | Zürcher Gesetzessammlung via ZH-Lex mit Volltextsuche und Artikelextraktion | *"Welche Zürcher Gesetze regeln Schulzuständigkeiten?"* | ✅ | [audits/](https://github.com/malkreide/openlex-mcp/tree/master/audits) |
| [swiss-courts-mcp](https://github.com/malkreide/swiss-courts-mcp) | Schweizer Gerichtsentscheide via entscheidsuche.ch, inklusive Bundes- und Kantonsgerichte | *"Neue Bundesgerichtsentscheide zu Schultransport?"* | ✅ | [audits/](https://github.com/malkreide/swiss-courts-mcp/tree/master/audits) |
| [register-mcp](https://github.com/malkreide/register-mcp) | Zefix-Handelsregister und UID-Lookup | *"Aktive IT-Firmen in Zürich Kreis 5?"* | ✅ | [audits/](https://github.com/malkreide/register-mcp/tree/main/audits) |
| [swiss-ip-mcp](https://github.com/malkreide/swiss-ip-mcp) | IGE/IPI Swissreg: Marken, Patente, SPCs | *"Aktive Schweizer Marken mit 'Zurich' in Klasse 41?"* | ✅ 🔐 | [audits/](https://github.com/malkreide/swiss-ip-mcp/tree/main/audits) |

### 📊 Statistik & Geodaten

| Server | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|
| [swiss-statistics-mcp](https://github.com/malkreide/swiss-statistics-mcp) | BFS STAT-TAB PxWeb API für amtliche Schweizer Statistik | *"Bevölkerung der Schweizer Gemeinden nach Kanton, 2023?"* | ✅ | [audits/](https://github.com/malkreide/swiss-statistics-mcp/tree/main/audits) |
| [zurich-opendata-mcp](https://github.com/malkreide/zurich-opendata-mcp) | Stadt Zürich: Wetter, Luftqualität, Parkierung, Geodaten, Gemeinderat, Tourismus | *"Welche Schulgebäude in Zürich haben noch keine Glasfaser?"* | ✅ | [audits/](https://github.com/malkreide/zurich-opendata-mcp/tree/main/audits) |
| [swisstopo-mcp](https://github.com/malkreide/swisstopo-mcp) | Bundesgeodaten: Geocoding, Höhe, STAC, WMTS, ÖREB und mehr | *"Wie sieht das Höhenprofil zwischen Zürich HB und Uetliberg aus?"* | ✅ | [audits/](https://github.com/malkreide/swisstopo-mcp/tree/master/audits) |

### 🎓 Bildung & Forschung

| Server | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|
| [global-education-mcp](https://github.com/malkreide/global-education-mcp) | UNESCO UIS und OECD Education at a Glance. Angrenzende internationale Kontextquelle. | *"Sek-II-Abschlussquoten CH vs. OECD-Durchschnitt?"* | ✅ 🧭 | [audits/](https://github.com/malkreide/global-education-mcp/tree/main/audits) |
| [zh-education-mcp](https://github.com/malkreide/zh-education-mcp) | Bildungsdaten von Kanton und Stadt Zürich: Schulen, Statistik, Infrastruktur | *"Wie verteilen sich Schülerzahlen auf die sieben Zürcher Schulkreise?"* | ✅ | [audits/](https://github.com/malkreide/zh-education-mcp/tree/main/audits) |
| [swiss-academic-libraries-mcp](https://github.com/malkreide/swiss-academic-libraries-mcp) | swisscovery, e-rara, e-periodica, e-manuscripta via SRU/OAI-PMH | *"Digitalisierte Schweizer Karten des 18. Jahrhunderts in e-rara?"* | ✅ | [audits/](https://github.com/malkreide/swiss-academic-libraries-mcp/tree/main/audits) |
| [eth-library-mcp](https://github.com/malkreide/eth-library-mcp) | ETH Library Discovery und Persons APIs | *"ETH-Publikationen zu urbanen Hitzeinseln seit 2020?"* | ✅ | [audits/](https://github.com/malkreide/eth-library-mcp/tree/main/audits) |

### 💰 Wirtschaft & Finanzen

| Server | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|
| [swiss-snb-mcp](https://github.com/malkreide/swiss-snb-mcp) | SNB-Datenportal: Wechselkurse, Bilanz, Leitzins, SARON, Geldmengen | *"EUR/CHF seit 2015 und aktueller SNB-Leitzins?"* | ✅ | [audits/](https://github.com/malkreide/swiss-snb-mcp/tree/main/audits) |
| [seco-labor-mcp](https://github.com/malkreide/seco-labor-mcp) | SECO-Arbeitsmarkt: Arbeitslosigkeit, offene Stellen, Erwerbsindikatoren | *"Arbeitslosenquote Kanton Zürich vs. Schweiz in den letzten 12 Monaten?"* | ✅ | [audits/](https://github.com/malkreide/seco-labor-mcp/tree/main/audits) |

### 🎭 Kultur & Medien

| Server | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|
| [swiss-culture-mcp](https://github.com/malkreide/swiss-culture-mcp) | BAK-Kulturerbe, ISOS, lebendige Traditionen, RSS | *"UNESCO-gelistete lebendige Traditionen im Kanton Zürich?"* | ✅ | [audit/](https://github.com/malkreide/swiss-culture-mcp/tree/main/audit) |
| [swiss-cultural-heritage-mcp](https://github.com/malkreide/swiss-cultural-heritage-mcp) | Kulturerbe-Inventare, Denkmallisten, archäologische Register | *"Geschützte Baudenkmäler in Zürich Kreis 6?"* | ✅ | [audits/](https://github.com/malkreide/swiss-cultural-heritage-mcp/tree/main/audits) |
| [bakom-mcp](https://github.com/malkreide/bakom-mcp) | BAKOM Open Data zu Telekommunikation und Medien | *"Welche Gemeinden haben noch keine 100 Mbit/s Breitbandabdeckung?"* | ✅ | [audits/](https://github.com/malkreide/bakom-mcp/tree/main/audits) |
| [srgssr-mcp](https://github.com/malkreide/srgssr-mcp) | SRG SSR: Wetter, Video, Audio, EPG, Polis | *"Neuste SRF-Beiträge zur Bildungspolitik?"* | ✅ | [audits/](https://github.com/malkreide/srgssr-mcp/tree/main/audits) |
| [news-monitor-mcp](https://github.com/malkreide/news-monitor-mcp) | Aggregiertes News-Monitoring über Schweizer Public-Media-RSS. Angrenzende Kontextquelle. | *"Top drei bildungspolitische Schweizer Medienstories diese Woche?"* | ✅ 🧭 | [audits/](https://github.com/malkreide/news-monitor-mcp/tree/main/audits) |

### 🏥 Gesundheit

| Server | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|
| [bag-health-mcp](https://github.com/malkreide/bag-health-mcp) | BAG Public-Health Open Data: Indikatoren, Programme, Statistik | *"Impfquote nach Kanton für die letzte Berichtsperiode?"* | ✅ | [audits/](https://github.com/malkreide/bag-health-mcp/tree/main/audits) |
| [bag-epl-mcp](https://github.com/malkreide/bag-epl-mcp) | BAG EPL: Spezialitätenliste, Medikamente, Vergütungsdaten | *"Welche Medikamente kamen in den letzten sechs Monaten auf die Spezialitätenliste?"* | ✅ | [docs/audit/](https://github.com/malkreide/bag-epl-mcp/tree/main/docs/audit) |

### 🍽️ Lebensmittelsicherheit

| Server | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|
| [swiss-food-safety-mcp](https://github.com/malkreide/swiss-food-safety-mcp) | BLV Open Data zu Lebensmittelsicherheit und Veterinärkontrollen | *"Aktuelle Lebensmittelrückrufe in der Schweiz?"* | ✅ | [docs/audit/](https://github.com/malkreide/swiss-food-safety-mcp/tree/main/docs/audit) |

### 🗳️ Demokratie & Transparenz

| Server | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|
| [swiss-democracy-mcp](https://github.com/malkreide/swiss-democracy-mcp) | Parlaments-OData, Swissvotes, Referenden, Abstimmungsresultate | *"Welche hängigen parlamentarischen Vorstösse betreffen KI in der Bildung?"* | ✅ | [audits/](https://github.com/malkreide/swiss-democracy-mcp/tree/main/audits) |
| [parlament-mcp](https://github.com/malkreide/parlament-mcp) | Curia-Vista-OData-API des Schweizer Parlaments | *"Welche Vorstösse zu KI in der Schule sind hängig?"* | ✅ | [audits/](https://github.com/malkreide/parlament-mcp/tree/main/audits) |
| [lobbywatch-mcp](https://github.com/malkreide/lobbywatch-mcp) | Lobbywatch.ch-Transparenzdaten zu Parlamentsmitgliedern, Interessenbindungen, Zutrittsbadges | *"Welche WBK-Mitglieder haben Bezüge zu privaten Bildungsanbietern?"* | ✅ 🧭 | [audits/](https://github.com/malkreide/lobbywatch-mcp/tree/main/audits) |

### 🛰️ Tech Intelligence

| Server | Beschreibung | Anchor Query | Status | Audit |
|---|---|---|---|---|
| [hn-tech-signal-mcp](https://github.com/malkreide/hn-tech-signal-mcp) | Hacker-News-Signalextraktion für Technologie-Trendmonitoring. Angrenzende Kontextquelle. | *"Welche AI-Infrastrukturthemen werden diese Woche am meisten diskutiert?"* | ✅ 🧭 | [audits/](https://github.com/malkreide/hn-tech-signal-mcp/tree/main/audits) |

### 🗄️ Legacy / Abgelöst

| Server | Behandlung | Grund |
|---|---|---|
| [MCP-Server-for-patent-research-](https://github.com/malkreide/MCP-Server-for-patent-research-) | Production-ready Legacy / Migrationskandidat | Älterer auditierter Patentrecherche-Server mit breitem EPO/Swissreg-Scope und Namensinkonsistenzen. Auffindbar lassen, aber für das aktuelle Portfolio `swiss-ip-mcp` bevorzugen, solange der alte Repo nicht umbenannt und an die aktuellen Portfolio-Konventionen angepasst ist. |

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

```text
malkreide/
├── swiss-public-data-mcp                 ← dieser Index
├── mcp-audit-skill                       ← Auditmethodik, kein Server
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
│   └── swiss-ip-mcp
│
├── Statistik & Geodaten
│   ├── swiss-statistics-mcp
│   ├── zurich-opendata-mcp
│   └── swisstopo-mcp
│
├── Bildung & Forschung
│   ├── global-education-mcp
│   ├── zh-education-mcp
│   ├── swiss-academic-libraries-mcp
│   └── eth-library-mcp
│
├── Wirtschaft & Finanzen
│   ├── swiss-snb-mcp
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
    └── MCP-Server-for-patent-research-
```

---

## Maintenance-Roadmap

Die früheren Roadmap-Punkte für Zürcher kantonales Recht, Schweizer Gerichte und tiefere swisstopo-Geodaten sind ins Inventar gewandert, weil `openlex-mcp`, `swiss-courts-mcp` und `swisstopo-mcp` inzwischen existieren.

Aktuelle Portfolio-Prioritäten:

- Alle verlinkten Audit-Verzeichnisse mit Report-Metadaten, Findings und Remediation Notes aktuell halten.
- Falls das archivierte Legacy-Patent-Repository wieder geöffnet wird, dort ein `audits/`-Verzeichnis ergänzen oder die Audit-Evidence in `swiss-ip-mcp` migrieren.
- `mcp-audit-skill` und künftige Berichte auf MCP-Spec `2025-11-25` ausrichten; ältere Spec-Versionen in Audit-Metadaten erhalten.
- Entscheiden, ob `parlament-mcp` als spezialisierter Server bleibt oder in `swiss-democracy-mcp` aufgeht.
- Entscheiden, ob `MCP-Server-for-patent-research-` umbenannt, archiviert oder in `swiss-ip-mcp` migriert wird.
- README-Tabellen in einem späteren Automationsschritt aus `portfolio.json` generieren.

---

## Mitwirken

Bugreports und Feature Requests sind auf den jeweiligen Server-Repositories willkommen. Wer einen neuen MCP-Server für Schweizer offene Daten baut und hier listen möchte, sollte einen Issue mit kurzer Beschreibung, Repo-Link, Datenquellen und geplantem Auditprofil eröffnen.

---

## Lizenz

MIT License - siehe [LICENSE](LICENSE)

---

## Autor

**Hayal Oezkan** · [github.com/malkreide](https://github.com/malkreide)

> Erinnerung: Dies ist ein privates Open-Source-Projekt. Institutionelle Zugehörigkeiten in anderen öffentlichen Profilen des Autors sind für dieses Repository nicht relevant.
