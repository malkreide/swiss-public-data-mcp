# swiss-public-data-mcp

![Servers](https://img.shields.io/badge/servers-27-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.11--3.13-blue)
![Protocol](https://img.shields.io/badge/protocol-MCP-orange)
![Data](https://img.shields.io/badge/data-Swiss%20Open%20Data-red)
![Audit](https://img.shields.io/badge/quality-gegen%20internen%20Katalog%20auditiert-purple)

> Ein kuratiertes Portfolio von Model-Context-Protocol-(MCP-)Servern, das KI-Agenten mit Schweizer öffentlichen und offenen Daten verbindet — gebaut auf einer reproduzierbaren Qualitätsmethodik, nicht als Sammlung einmaliger Experimente.

[🇬🇧 English version](README.md)

> ⚠️ **Disclaimer — Unabhängigkeit dieses Projekts**
>
> Dies ist ein **privates Open-Source-Projekt** von Hayal Oezkan. Es entsteht in privater Funktion, in der Freizeit, mit privater Infrastruktur. Es ist **kein** offizielles Projekt der Stadt Zürich, des Schulamts, der KI-Fachgruppe der Stadtverwaltung Zürich oder einer anderen öffentlichen Institution. Die Verweise auf städtische und eidgenössische Strategien in dieser README sind deskriptiv — sie erläutern, wie das Portfolio sich zu öffentlichen digitalen Agenden verhält. Sie implizieren weder institutionelle Zustimmung noch Auftrag oder Zugehörigkeit. Alle Aussagen in diesem Repository sind privat.

---

## Wozu das Ganze

`opendata.swiss` listet rund 13'600 öffentliche Datensätze. Geo.admin.ch, Fedlex, das SNB-Datenportal, BAFU, BFS PxWeb, swisstopo, der OData-Feed des Parlaments, das Open-Data-Portal der Stadt Zürich — jede Quelle hat ihre eigene API, ihr eigenes Auth-Modell, ihre eigenen Eigenheiten. Für einen KI-Agenten ist diese Landschaft faktisch **unerreichbar**: Jeder Datensatz ist eine eigene Custom-Integration entfernt.

Dieses Portfolio schliesst diese letzte Meile. Jeder Server im Index übersetzt eine Schweizer Open-Data-Quelle in eine Handvoll sauber gestalteter, KI-konsumierbarer Tools. Jeder MCP-kompatible Client (Claude Desktop, VS Code + Continue, Cursor, Windsurf, eigene Agents) kann sie direkt aufrufen.

Das Portfolio ist bewusst **synergetisch, nicht nur additiv** angelegt: Verkehr und Strassenmobilität ergeben einen multimodalen Routing-Agent; Statistik und Geodaten ermöglichen räumliche Analyse; Bildung, Recht und Statistik zusammen tragen Politikrecherche.

---

## Verhältnis zu öffentlichen Digitalisierungsstrategien

Das Portfolio ist von unten gewachsen — aus dem praktischen Frust einer Person über kaputte Integrationen, nicht aus einem Strategiepapier. Die getroffenen Engineering-Entscheide passen aber sauber zu mehreren öffentlichen digitalen Agenden. Nützlich für die Einordnung; nie die Begründung der Arbeit selbst.

### Stadt Zürich (primärer Rahmen)

Das Portfolio operationalisiert drei Ziele aus den **Strategien Zürich 2040**, Handlungsfeld IV «Leistungsfähige Stadt», Dimension Digitalisierung:

| Strategisches Ziel der Stadt | Was das Portfolio tatsächlich leistet |
|---|---|
| SZ 4 — «Open Government Data standardmässig öffentlich zur freien Verfügung» | Schliesst die Lücke zwischen *verfügbar* und *KI-nutzbar*. Daten, die Stadt und Bund bereits publizieren, entfalten ihren vollen Wert erst, wenn Agents sie ohne Custom-Integrationsarbeit konsumieren können. |
| SZ 1 — «Stadtinterne Prozesse durchgehend digital gedacht» | Server wie `zurich-opendata-mcp`, `zh-education-mcp`, `swiss-statistics-mcp` ermöglichen agentische Workflows auf bestehender Daten-Infrastruktur — ohne sie neu zu bauen. |
| SZ 5 — «Digitalisierungskompetenzen der städtischen Angestellten» | Open-Source-Code, zweisprachig (DE/EN), öffentlich lesbar, dient als konkretes Lernartefakt. Kein Kurs, sondern etwas zum Lesen und Ausführen. |

Die **Digitalisierungsstrategie der Stadt Zürich (2024)** spiegelt sich an drei Stellen in den Designentscheiden des Portfolios:

| Fokus der Stadtstrategie | Antwort des Portfolios |
|---|---|
| Schwerpunkt 1 «Bleibender Mehrwert» / Stossrichtung B «Nutzer*innen im Fokus» | Jeder Server hat genau eine konkrete Anchor-Query, die er beantworten muss. Keine Anchor-Query, kein Server. |
| Schwerpunkt 3 «Vernetzte Zusammenarbeit» / Stossrichtung E «Informationen teilen» | Open Source vom ersten Tag. Zweisprachige Dokumentation. GitHub-Topic für Portfolio-weite Auffindbarkeit. |
| Schwerpunkt 4 «Verantwortungsvoller Technologieeinsatz» / Stossrichtung I «Datenbestände nutzen» | No-Auth-First-Architektur ist «Open by Default» in Code übersetzt. |

### Schweizerische Eidgenossenschaft (sekundärer Rahmen)

| Bundesstrategie | Beitrag des Portfolios |
|---|---|
| **Strategie Einsatz von KI-Systemen in der Bundesverwaltung**, Handlungsfeld 1 «Kompetenzen aufbauen» | Praxisorientierter, öffentlicher, wiederverwendbarer Kompetenzaufbau — nutzbar als Referenzmaterial für das Kompetenznetzwerk KI (CNAI) des Bundes. |
| **Strategie Einsatz von KI-Systemen in der Bundesverwaltung**, Handlungsfeld 2 «Vertrauen verdienen» | No-Auth-First plus ausschliesslich Public Open Data ergibt eine inhärent risikoarme Angriffsfläche. Keine Personendaten, keine gespeicherten Credentials, keine intransparent trainierten Modelle. |
| **Strategie Digitale Schweiz 2026**, Wirkungsbereich Infrastruktur | Erweitert den praktischen Wert der ~13'600 Datensätze auf opendata.swiss, indem es sie über ein gemeinsames Protokoll LLM-konsumierbar macht. |
| **Strategie Digitale Schweiz 2026**, Wirkungsbereich Bildung & Kompetenzen | Zweisprachige DE/EN-Dokumentation senkt die Einstiegshürde für Lernende digitaler Kompetenzen über Sprachregionen hinweg. |

---

## Qualitätsmethodik — warum diese Server auditierbar sind, nicht nur ausgeliefert

Einen MCP-Server zu bauen, ist einfach. **27 Server** ohne Qualitätsdrift zu bauen, ist das eigentliche Problem. Ein Referenz-Katalog plus ein interner `mcp-audit`-Skill wenden auf jeden Server im Portfolio dasselbe sechsstufige Audit an — statt bei jedem Server die Best Practices neu aus dem Bauch herzuleiten.

### Der Audit-Katalog

Jeder Server ist gegen einen versionierten Katalog von rund **65 Checks in acht Kategorien** auditierbar:

| Kategorie | Abdeckung | Beispiel-Checks |
|---|---|---|
| **ARCH** | Tool-Design, Annotations, Idempotency, Repo-Struktur, Spec-Versionierung | Tool-Naming, Vollständigkeit Input-Schema, Fehler-Semantik |
| **SDK** | FastMCP / TypeScript / Zod / Lifecycle | Lifespan-Handling, Capability-Deklarationen |
| **SEC** | Security (grösste Kategorie) | Confused-Deputy / OAuth-Proxy, SSRF, Session-Hijacking, Prompt-Injection-Surface, Secret-Handling |
| **SCALE** | Transport, Load Balancing, Container, Gateway | Stateless Transport, horizontale Skalierung, Gateway-Kompatibilität |
| **OBS** | Logging, Errors, SIEM, Tracing | Strukturierte Logs, Error-Envelopes, Trace-Korrelation |
| **HITL** | Sampling, Human-in-the-Loop | Sampling-Capability, Write-Confirmation-Gates |
| **CH** | Schweiz-Compliance — DSG / EDÖB | Datenklassifikation, Datenstandort, Einwilligung, Rechtsgrundlage |
| **OPS** | Test-Strategie, Dokumentation, Phasenarchitektur | Live-Test-Isolation, phasenbasierte Roadmap, README-Vollständigkeit |

### Wie die Methodik funktioniert

Jeder Audit folgt sechs nummerierten Schritten in dieser Reihenfolge:

1. **Profil zuerst** — Sechs Pflichtfelder (Transport, Auth-Modell, Datenklasse, Schreibzugriff, Deployment, Repo-URL) bestimmen, welche Checks für diesen Server überhaupt anwendbar sind.
2. **Katalog laden** — Der gesamte Check-Katalog wird geparst und nach Kategorie und Severity indexiert.
3. **Applicability-Filter** — Eine Boolean-Klausel `applies_when` wird gegen das Profil ausgewertet. Irrelevante Checks (z. B. OAuth-Checks für einen stdio-only-Server ohne Auth) fallen vor Audit-Beginn aus dem Set heraus. Typisches Resultat: Ein `Public Open Data`- / `read-only`- / `no-auth`-Server läuft durch ~15–20 der ~65 Checks; ein `Verwaltungsdaten`- / `OAuth-Proxy`- / `Cloud`-Server durch ~45–55.
4. **Check-Ausführung** — Severity absteigend: `critical` zuerst, dann `high`, `medium`, `low`. Verifikationsmodi je Check: `automated` (grep/AST), `code_review`, `config_check`, `runtime_test`. Jedes Finding braucht Evidenz mit Datei und Zeilennummer — *«ein Finding ohne `path/to/file.py:42` ist eine Meinung, kein Befund.»*
5. **Finding-Dokumentation** — Pro fehlgeschlagenem Check ein strukturiertes Finding mit beobachtetem vs. erwartetem Verhalten, Evidenz, Risikobeschreibung, Remediation-Diff, Effort-Schätzung (S / M / L / XL).
6. **Audit-Report** — Executive Summary in drei Sätzen, Profile-Snapshot, Applicability-Übersicht, Findings-Tabelle, Detail-Findings, Remediation-Plan mit Reihenfolge-Vorschlag, Audit-Metadata.

### Severity-Disziplin

| Stufe | Bedeutung | Konsequenz |
|---|---|---|
| `critical` | Sicherheitslücke oder Compliance-Bruch | Blockiert Produktion. Muss vor Release gefixt sein. |
| `high` | Architektureller Mangel mit signifikantem Risiko | Im laufenden Sprint fixen, max. 1 Sprint Karenz. |
| `medium` | Best-Practice-Verletzung, kein akutes Risiko | Im nächsten Sprint planen. |
| `low` | Polish, Optimierung, Stilistik | Backlog. |

> *«`critical` heisst critical. Wer die Stufe inflationiert, hat irgendwann nur noch `critical`.»*

### Warum das fürs Portfolio zählt

Jeder Server im untenstehenden Index wurde oder wird gegen diesen Katalog auditiert. Die Status-Badges (✅ / ⚠️ / 🔄 / 🔐) widerspiegeln nicht bloss «läuft», sondern «hat ein Audit am angemessenen Severity-Gate bestanden». Genau das macht aus 27 Servern ein kohärentes Portfolio statt einen Friedhof von Wochenend-Projekten.

---

## Server-Portfolio

**Status-Legende:** ✅ Stabil, Audit am Gate `high`+ bestanden · ⚠️ Findings offen · 🔄 Audit oder PyPI-Publikation ausstehend · 🔐 API-Credentials erforderlich

### 🚆 Verkehr & Mobilität

| Server | Beschreibung | Anchor-Query | Status |
|---|---|---|---|
| [swiss-transport-mcp](https://github.com/malkreide/swiss-transport-mcp) | OJP 2.0 Reiseauskunft, SIRI-SX-Störungen, Auslastung, Tarife, Zugformation | *«Frühester Zug Zürich → Bern morgen um 8 Uhr?»* | ✅ |
| [swiss-road-mobility-mcp](https://github.com/malkreide/swiss-road-mobility-mcp) | GBFS Shared Mobility, EV-Ladestationen, DATEX II Verkehr, Park & Rail | *«Verfügbare E-Bikes nahe Zürich HB jetzt gerade?»* | ✅ |
| [sbb-opendata-mcp](https://github.com/malkreide/sbb-opendata-mcp) | SBB Open Data via OpenDataSoft | *«Pünktlichkeitsstatistik der IC-1-Linie im letzten Monat?»* | ✅ |

### 🌿 Umwelt & Klima

| Server | Beschreibung | Anchor-Query | Status |
|---|---|---|---|
| [swiss-environment-mcp](https://github.com/malkreide/swiss-environment-mcp) | BAFU-Umweltdaten, NABEL-Luftqualität, Hydrologie | *«PM2.5-Werte in Zürich in den letzten 7 Tagen?»* | ⚠️ |
| [wsl-envidat-mcp](https://github.com/malkreide/wsl-envidat-mcp) | WSL / EnviDat Umweltforschungs-Datensätze via CKAN | *«Datensätze zu Permafrost in den Alpen von der WSL?»* | 🔄 |
| [meteoswiss-mcp](https://github.com/malkreide/meteoswiss-mcp) | MeteoSchweiz Open Data — Wetter, Klimanormwerte, Warnungen | *«War die Bise im letzten Winter in Zürich aussergewöhnlich stark?»* | 🔄 |

### ⚖️ Recht & Regulierung

| Server | Beschreibung | Anchor-Query | Status |
|---|---|---|---|
| [fedlex-mcp](https://github.com/malkreide/fedlex-mcp) | Schweizer Bundesrecht via Fedlex-SPARQL-Endpoint | *«Was sagt Art. 62 BV zum öffentlichen Bildungswesen?»* | ✅ |
| [register-mcp](https://github.com/malkreide/register-mcp) | Zefix-Handelsregister und UID-Lookup | *«Aktive Firmen in Zürich Kreis 5 im IT-Sektor?»* | 🔄 |
| [swiss-ip-mcp](https://github.com/malkreide/swiss-ip-mcp) | IGE/IPI Swissreg — Marken, Patente, ESZ | *«Aktive Schweizer Marken mit ‹Zurich› in Klasse 41?»* | 🔐 |

### 📊 Statistik & Geodaten

| Server | Beschreibung | Anchor-Query | Status |
|---|---|---|---|
| [swiss-statistics-mcp](https://github.com/malkreide/swiss-statistics-mcp) | BFS STAT-TAB PxWeb-API — offizielle Schweizer Statistik | *«Bevölkerung der Schweizer Gemeinden nach Kanton, 2023?»* | 🔄 |
| [zurich-opendata-mcp](https://github.com/malkreide/zurich-opendata-mcp) | Stadt Zürich — Wetter, Luftqualität, Parking, Geodaten, Gemeinderat, Tourismus | *«Welche Schulhäuser in Zürich haben noch keinen Glasfaseranschluss?»* | ⚠️ |

### 🎓 Bildung & Forschung

| Server | Beschreibung | Anchor-Query | Status |
|---|---|---|---|
| [global-education-mcp](https://github.com/malkreide/global-education-mcp) | UNESCO UIS und OECD Education at a Glance | *«Abschlussquote Sekundarstufe II in der CH vs. OECD-Durchschnitt?»* | ✅ |
| [zh-education-mcp](https://github.com/malkreide/zh-education-mcp) | Bildungsdaten Kanton und Stadt Zürich — Schulen, Statistiken, Infrastruktur | *«Wie verteilen sich die Schüler*innenzahlen auf die sieben Schulkreise von Zürich?»* | 🔄 |
| [swiss-academic-libraries-mcp](https://github.com/malkreide/swiss-academic-libraries-mcp) | swisscovery, e-rara, e-periodica, e-manuscripta (SRU/OAI-PMH) | *«Digitalisierte Schweizer Karten aus dem 18. Jahrhundert in e-rara?»* | 🔄 |
| [eth-library-mcp](https://github.com/malkreide/eth-library-mcp) | ETH-Bibliothek Discovery- und Persons-APIs | *«ETH-Publikationen zu urbanen Hitzeinseln seit 2020?»* | ⚠️ |

### 💰 Wirtschaft & Finanzen

| Server | Beschreibung | Anchor-Query | Status |
|---|---|---|---|
| [swiss-snb-mcp](https://github.com/malkreide/swiss-snb-mcp) | SNB-Datenportal — Wechselkurse, Bilanz, Zinssätze, SARON, Geldaggregate | *«Wie hat sich der EUR/CHF-Kurs seit 2015 entwickelt, und wo steht der SNB-Leitzins heute?»* | ✅ |
| [seco-labor-mcp](https://github.com/malkreide/seco-labor-mcp) | SECO-Arbeitsmarkt — Arbeitslosigkeit, offene Stellen, Beschäftigungsindikatoren | *«Arbeitslosenquote Kanton Zürich vs. Schweizer Durchschnitt in den letzten 12 Monaten?»* | 🔄 |

### 🎭 Kultur & Medien

| Server | Beschreibung | Anchor-Query | Status |
|---|---|---|---|
| [swiss-culture-mcp](https://github.com/malkreide/swiss-culture-mcp) | BAK Kulturerbe, ISOS, lebendige Traditionen, RSS | *«UNESCO-gelistete lebendige Traditionen im Kanton Zürich?»* | ✅ |
| [swiss-cultural-heritage-mcp](https://github.com/malkreide/swiss-cultural-heritage-mcp) | Kulturerbe-Inventare, Denkmallisten, archäologische Register | *«Geschützte Baudenkmäler in Zürich Kreis 6?»* | 🔄 |
| [bakom-mcp](https://github.com/malkreide/bakom-mcp) | BAKOM Telekommunikations- und Medien-Open-Data | *«Welche Gemeinden haben noch kein 100-Mbit/s-Breitband?»* | 🔄 |
| [srgssr-mcp](https://github.com/malkreide/srgssr-mcp) | SRG SSR — Wetter, Video, Audio, EPG, Polis | *«Aktuellste SRF-Beiträge zur Bildungspolitik?»* | 🔐 |
| [news-monitor-mcp](https://github.com/malkreide/news-monitor-mcp) | Aggregiertes News-Monitoring über RSS-Feeds Schweizer Medien | *«Top-drei bildungspolitische Geschichten in Schweizer Medien diese Woche?»* | 🔄 |

### 🏥 Gesundheit

| Server | Beschreibung | Anchor-Query | Status |
|---|---|---|---|
| [bag-health-mcp](https://github.com/malkreide/bag-health-mcp) | BAG Public-Health-Open-Data — Indikatoren, Programme, Statistiken | *«Impfquote nach Kanton in der letzten Berichtsperiode?»* | 🔄 |
| [bag-epl-mcp](https://github.com/malkreide/bag-epl-mcp) | BAG EPL — Spezialitätenliste, Medikamente und Vergütung | *«Welche Medikamente wurden in den letzten sechs Monaten in die Spezialitätenliste aufgenommen?»* | 🔄 |

### 🍽️ Lebensmittelsicherheit

| Server | Beschreibung | Anchor-Query | Status |
|---|---|---|---|
| [swiss-food-safety-mcp](https://github.com/malkreide/swiss-food-safety-mcp) | BLV Open Data — Lebensmittelsicherheit und Veterinärinspektionen | *«Aktuelle Lebensmittel-Rückrufe in der Schweiz?»* | ✅ |

### 🗳️ Demokratie

| Server | Beschreibung | Anchor-Query | Status |
|---|---|---|---|
| [swiss-democracy-mcp](https://github.com/malkreide/swiss-democracy-mcp) | Parlament OData (Vorstösse, Geschäfte, Sessionen), Abstimmungen, Wahlen | *«Welche hängigen Vorstösse betreffen KI in der Schule?»* | 🔄 |

### 🛰️ Tech-Intelligence

| Server | Beschreibung | Anchor-Query | Status |
|---|---|---|---|
| [hn-tech-signal-mcp](https://github.com/malkreide/hn-tech-signal-mcp) | Hacker-News-Signalextraktion zur Beobachtung von Tech-Trends | *«Welche KI-Infrastruktur-Themen werden diese Woche am meisten diskutiert?»* | 🔄 |

---

## Architektur-Prinzipien

**No-Auth-First** — Phase 1 jedes Servers nutzt ausschliesslich offene, nicht-authentifizierte Endpoints. Authentifizierte APIs kommen in späteren Phasen mit Graceful Degradation hinzu, sodass der Server immer auch ohne Credentials nutzbar bleibt.

**Phasenarchitektur** — Jeder Server ist explizit in Phasen strukturiert (Phase 1: No-Auth → Phase 2: Auth → Phase 3: Advanced). Das erlaubt schnelle Auslieferung nutzbarer Tools und dokumentiert die Roadmap ehrlich.

**Portfolio-Synergie** — Server sind so gestaltet, dass sie sich kombinieren lassen. Siehe *Kombinationsszenarien* unten.

**Dual Transport** — Alle Server unterstützen `stdio` (Claude Desktop, lokale IDEs) und `Streamable HTTP` (Cloud-Deployment auf Render.com / Railway).

**Standard-Stack** — FastMCP · Pydantic v2 · httpx · hatchling · `src/`-Layout · `pyproject.toml` · pytest mit `@pytest.mark.live`-Isolation · GitHub Actions CI (Python 3.11–3.13) · `uvx`-fähiges Packaging · PyPI-Publikation via OIDC Trusted Publisher.

**Zweisprachige Dokumentation** — Jeder Server hat `README.md` (Englisch, primär) und `README.de.md` (Deutsch), gegenseitig verlinkt mit Flag-Emoji. Inklusive `CONTRIBUTING.md`, `CHANGELOG.md` (Keep-a-Changelog), Portfolio-Banner, Badges, Architektur-ASCII-Diagramm, bekannte Limitierungen.

**Audit-getriebene Qualität** — Siehe *Qualitätsmethodik* oben. Jeder Server durchläuft dasselbe sechsstufige Audit, bevor sich der Status von 🔄 auf ✅ ändert.

---

## Quickstart

Jeder Server ist unabhängig installierbar via `uvx` (empfohlen) oder `pip`. Konfigurationsdetails siehe README des einzelnen Servers.

**Beispiel — `swiss-transport-mcp` zu Claude Desktop hinzufügen:**

```json
// ~/Library/Application Support/Claude/claude_desktop_config.json
{
  "mcpServers": {
    "swiss-transport": {
      "command": "uvx",
      "args": ["swiss-transport-mcp"]
    }
  }
}
```

Für Server, die noch nicht auf PyPI sind (Status 🔄), das Repository klonen und ausführen:

```bash
git clone https://github.com/malkreide/<server-name>
cd <server-name>
uv run mcp dev src/<package>/server.py
```

---

## Kombinationsszenarien

Der eigentliche Wert liegt nicht im einzelnen Server — er liegt in den Kombinationen. Sechs konkrete Beispiele:

| Szenario | Beteiligte Server | Beispielfrage |
|---|---|---|
| **Makroökonomischer Kontext** | swiss-snb-mcp + swiss-statistics-mcp + seco-labor-mcp | *«CHF/EUR-Kursverlauf seit 2015 zusammen mit Schweizer BIP, LIK und Arbeitslosigkeit?»* |
| **Multimodaler Pendelplaner** | swiss-transport-mcp + swiss-road-mobility-mcp + sbb-opendata-mcp | *«Zug von Wädenswil nach Zürich HB, dann E-Bike zur ETH. Beste Variante um 8:15, inkl. Pünktlichkeits-Historie?»* |
| **Schulinfrastruktur-Audit** | zh-education-mcp + zurich-opendata-mcp + swiss-statistics-mcp | *«Zürcher Schulen ohne Glasfaser im Vergleich zur kantonalen Breitband-Abdeckung und Schüler*innenverteilung pro Schulkreis?»* |
| **Bildungspolitische Recherche** | global-education-mcp + fedlex-mcp + swiss-statistics-mcp + swiss-democracy-mcp | *«Wie steht die CH-Abschlussquote Sek II im OECD-Vergleich, was schreibt das Bundesrecht vor und welche Vorstösse sind im Parlament hängig?»* |
| **Umwelt-Briefing** | swiss-environment-mcp + meteoswiss-mcp + wsl-envidat-mcp | *«Aktuelle Luftqualität und Wetter in Zürich, plus aktuelle WSL-Studien zu urbanen Hitzeinseln?»* |
| **Gesundheitspolitik-Loop** | bag-health-mcp + bag-epl-mcp + fedlex-mcp + swiss-democracy-mcp | *«Aktuelle Aufnahmen in die Spezialitätenliste, Impfquoten nach Kanton und die jeweilige Rechtsgrundlage?»* |

---

## Repository-Karte

Alle Server tragen den GitHub-Topic [`swiss-public-data-mcp`](https://github.com/topics/swiss-public-data-mcp) — damit ist das vollständige Portfolio auf GitHub auffindbar.

```
malkreide/
├── swiss-public-data-mcp                 ← Dieser Index (du bist hier)
│
├── Verkehr & Mobilität
│   ├── swiss-transport-mcp
│   ├── swiss-road-mobility-mcp
│   └── sbb-opendata-mcp
│
├── Umwelt & Klima
│   ├── swiss-environment-mcp
│   ├── wsl-envidat-mcp
│   └── meteoswiss-mcp
│
├── Recht & Regulierung
│   ├── fedlex-mcp
│   ├── register-mcp
│   └── swiss-ip-mcp
│
├── Statistik & Geodaten
│   ├── swiss-statistics-mcp
│   └── zurich-opendata-mcp
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
├── Demokratie
│   └── swiss-democracy-mcp
│
└── Tech-Intelligence
    └── hn-tech-signal-mcp
```

---

## Roadmap

Konkrete nächste Schritte fürs Portfolio als Ganzes (Roadmaps einzelner Server liegen in deren jeweiligen Repos):

- **Kantonale Rechtsschicht für Zürich** — `fedlex-mcp`-Muster ausweiten auf kantonales Recht (ZH-Lex, OS, ABl).
- **Swiss Courts MCP** — Bundesgerichts- und kantonale Gerichtsentscheide, anonymisiert.
- **Tiefere swisstopo-Geodaten** — über die in `zurich-opendata-mcp` enthaltenen WMS/WFS-Basics hinaus.
- **Wikidata- / semantische Schicht** — Entity Linking über Server hinweg (eine Bundesrätin in `swiss-democracy-mcp` ist dieselbe Person wie in den Fedlex-Debatten und der SRG-Berichterstattung).
- **Historische Zeitreihen-Integration** — die jetzigen Server sind weitgehend «gegenwartsorientiert»; Langzeit-Vergleiche sind lückenhaft.

---

## Mitwirken

Bug-Reports und Feature-Wünsche bitte direkt in den jeweiligen Server-Repositories. Wenn du selbst einen MCP-Server für Schweizer Open Data baust und ihn im Index gelistet haben möchtest, eröffne ein Issue mit kurzer Beschreibung und Link.

Der interne Audit-Katalog ist derzeit nicht offen publiziert, die Methodik ist aber oben beschrieben. Wer einen ähnlichen Ansatz auf das eigene MCP-Portfolio anwenden möchte, kann mit den sechs Schritten eigenständig arbeiten.

---

## Lizenz

MIT-Lizenz — siehe [LICENSE](LICENSE)

---

## Autor

**Hayal Oezkan** · [github.com/malkreide](https://github.com/malkreide)

> *Erinnerung — dies ist ein privates Open-Source-Projekt. Affiliationen, die in anderen öffentlichen Profilen des Autors erwähnt sind, haben für dieses Repository keine Relevanz. Der Abschnitt zur strategischen Einordnung oben ist deskriptive Analyse, keine institutionelle Aussage.*
