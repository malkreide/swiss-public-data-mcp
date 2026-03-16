# swiss-public-data-mcp

![Server](https://img.shields.io/badge/server-17-blue)
![Lizenz](https://img.shields.io/badge/lizenz-MIT-green)
![Python](https://img.shields.io/badge/python-3.11--3.13-blue)
![Protokoll](https://img.shields.io/badge/protokoll-MCP-orange)
![Daten](https://img.shields.io/badge/daten-Swiss%20Open%20Data-red)

> Eine kuratierte Sammlung von MCP-Servern, die KI-Modelle mit Schweizer Open-Data-Quellen verbinden.

[🇬🇧 English Version](README.md)

---

## Übersicht

Dieses Repository ist der zentrale Index für ein Portfolio von Open-Source-[Model Context Protocol (MCP)](https://modelcontextprotocol.io/)-Servern rund um Schweizer Behörden- und Forschungsdaten. Jeder Server macht eine spezifische Domäne — Verkehr, Umwelt, Recht, Statistik, Bildung, Kultur — als AI-fähige Werkzeuge verfügbar, die jeder MCP-kompatible Client (Claude Desktop, VS Code + Continue, Cursor, Windsurf) direkt nutzen kann.

Das Portfolio folgt einer **No-Auth-First**-Architektur: Jeder Server funktioniert ohne Konfiguration mit öffentlichen, authentifizierungsfreien Endpunkten. Authentifizierte APIs werden in späteren Phasen mit Graceful Degradation eingeführt. Alle Server basieren auf demselben Python-Stack (FastMCP, Pydantic v2, httpx) und unterstützen sowohl lokales Stdio- als auch Cloud-basiertes Streamable-HTTP-Transport.

Das Ziel ist eine kohärente, synergetische Infrastruktur — keine Sammlung isolierter Werkzeuge. Die Server sind so konzipiert, dass sie sich kombinieren lassen: Verkehr + Strassenverkehr ergibt einen multimodalen Routing-Agenten; Statistik + Geodaten ermöglicht räumliche Analysen; Bildung + Recht unterstützt Politikforschung.

---

## Server-Portfolio

### 🚆 Verkehr & Mobilität

| Server | Beschreibung | Tools | Anchor-Demo | Status |
|---|---|---|---|---|
| [swiss-transport-mcp](https://github.com/malkreide/swiss-transport-mcp) | OJP 2.0 Verbindungssuche, SIRI-SX Störungen, Auslastung, Tarife, Zugkomposition | 11 | *«Früheste Verbindung Zürich → Bern morgen um 8 Uhr?»* | ✅ |
| [swiss-road-mobility-mcp](https://github.com/malkreide/swiss-road-mobility-mcp) | GBFS Shared Mobility, E-Ladestationen, DATEX II Verkehr, Park & Rail | 15 | *«Verfügbare E-Bikes beim Zürich HB gerade jetzt?»* | ✅ |
| [sbb-opendata-mcp](https://github.com/malkreide/sbb-opendata-mcp) | SBB Open Data via OpenDataSoft | 10 | *«Pünktlichkeitsstatistiken der IC-1-Linie letzten Monat?»* | ✅ |

### 🌿 Umwelt & Klima

| Server | Beschreibung | Tools | Anchor-Demo | Status |
|---|---|---|---|---|
| [swiss-environment-mcp](https://github.com/malkreide/swiss-environment-mcp) | BAFU-Umweltdaten, NABEL-Luftqualität, Hydrologie | 12 | *«PM2.5-Werte in Zürich der letzten 7 Tage?»* | ⚠️ |
| [wsl-envidat-mcp](https://github.com/malkreide/wsl-envidat-mcp) | WSL / EnviDat Umweltforschungsdatensätze via CKAN | 12 | *«WSL-Datensätze zum alpinen Permafrost?»* | 🔄 |

### ⚖️ Recht & Regulierung

| Server | Beschreibung | Tools | Anchor-Demo | Status |
|---|---|---|---|---|
| [fedlex-mcp](https://github.com/malkreide/fedlex-mcp) | Schweizer Bundesrecht via Fedlex SPARQL-Endpunkt | 7 | *«Was sagt Art. 62 BV zur Volksschule?»* | ✅ |
| [bakom-mcp](https://github.com/malkreide/bakom-mcp) | BAKOM Telekommunikations- und Medien-Open-Data | 12 | *«Welche Gemeinden haben noch keinen 100-Mbit/s-Anschluss?»* | 🔄 |
| [swiss-ip-mcp](https://github.com/malkreide/swiss-ip-mcp) | IGE/IPI Swissreg — Marken, Patente, ergänzende Schutzzertifikate | 11 | *«Aktive Schweizer Marken mit ‹Zürich› in Klasse 41?»* | 🔐 |

### 📊 Statistik & Geodaten

| Server | Beschreibung | Tools | Anchor-Demo | Status |
|---|---|---|---|---|
| [swiss-statistics-mcp](https://github.com/malkreide/swiss-statistics-mcp) | BFS STAT-TAB PxWeb-API — offizielle Schweizer Statistiken | 9 | *«Bevölkerung der Schweizer Gemeinden nach Kanton, 2023?»* | 🔄 |
| [zurich-opendata-mcp](https://github.com/malkreide/zurich-opendata-mcp) | Stadt Zürich — Wetter, Luftqualität, Parkplätze, Geodaten, Gemeinderat, Tourismus | 23 | *«Welche Schulgebäude in Zürich haben noch keinen Glasfaseranschluss?»* | ⚠️ |

### 🎓 Bildung & Forschung

| Server | Beschreibung | Tools | Anchor-Demo | Status |
|---|---|---|---|---|
| [global-education-mcp](https://github.com/malkreide/global-education-mcp) | UNESCO UIS und OECD Education at a Glance | 10 | *«Abschlussquoten Sekundarstufe II: CH vs. OECD-Durchschnitt?»* | ✅ |
| [eth-library-mcp](https://github.com/malkreide/eth-library-mcp) | ETH-Bibliothek Discovery und Persons-API | — | *«ETH-Publikationen zu urbanen Wärmeinseln seit 2020?»* | ⚠️ |
| [swiss-academic-libraries-mcp](https://github.com/malkreide/swiss-academic-libraries-mcp) | swisscovery, e-rara, e-periodica, e-manuscripta (SRU/OAI-PMH) | 11 | *«Digitalisierte Schweizer Karten des 18. Jahrhunderts in e-rara?»* | 🔄 |

### 🎭 Kultur & Medien

| Server | Beschreibung | Tools | Anchor-Demo | Status |
|---|---|---|---|---|
| [swiss-culture-mcp](https://github.com/malkreide/swiss-culture-mcp) | BAK Kulturerbe, ISOS, lebendige Traditionen, RSS | 10 | *«UNESCO-gelistete lebendige Traditionen im Kanton Zürich?»* | ✅ |
| [srgssr-mcp](https://github.com/malkreide/srgssr-mcp) | SRG SSR — Wetter, Video, Audio, EPG, Polis | — | *«Aktuellste SRF-Beiträge zur Bildungspolitik?»* | 🔐 |

### 💰 Wirtschaft & Finanzen

| Server | Beschreibung | Tools | Anchor-Demo | Status |
|---|---|---|---|---|
| [swiss-snb-mcp](https://github.com/malkreide/swiss-snb-mcp) | SNB-Datenportal — Wechselkurse, Bilanz, Leitzins, SARON, Geldmengenaggregate | 9 | *«Wie hat sich EUR/CHF seit 2015 entwickelt, und wo steht der SNB-Leitzins heute?»* | ✅ |

### 🍽️ Lebensmittelsicherheit

| Server | Beschreibung | Tools | Anchor-Demo | Status |
|---|---|---|---|---|
| [swiss-food-safety-mcp](https://github.com/malkreide/swiss-food-safety-mcp) | BLV Open Data — Lebensmittelsicherheit und Veterinärkontrollen | 11 | *«Aktuelle Lebensmittelrückrufe in der Schweiz?»* | ✅ |

**Status-Legende:** ✅ Stabil &nbsp;|&nbsp; ⚠️ Bekannte offene Bugs &nbsp;|&nbsp; 🔄 PyPI-Publikation ausstehend &nbsp;|&nbsp; 🔐 API-Zugangsdaten erforderlich

---

## Architekturprinzipien

**No-Auth-First** — Phase 1 jedes Servers verwendet ausschliesslich offene, nicht authentifizierungspflichtige Endpunkte. Authentifizierte APIs werden in späteren Phasen mit Graceful Degradation hinzugefügt, sodass der Server immer ohne Zugangsdaten nutzbar bleibt.

**Portfolio-Synergie** — Die Server sind so konzipiert, dass sie sich kombinieren lassen. Beispiele:
- `swiss-transport-mcp` + `swiss-road-mobility-mcp` → multimodaler Routing-Agent
- `swiss-statistics-mcp` + `zurich-opendata-mcp` → städtisches Benchmarking
- `global-education-mcp` + `fedlex-mcp` → Bildungspolitik-Analyse
- `swiss-environment-mcp` + `wsl-envidat-mcp` → Umweltforschungsassistent

**Dualer Transport** — Alle Server unterstützen `stdio` (Claude Desktop, lokale IDEs) und `Streamable HTTP` (Cloud-Deployment auf Render.com).

**Einheitlicher Stack** — FastMCP · Pydantic v2 · httpx · hatchling · `src/`-Layout · `pyproject.toml` · pytest mit `@pytest.mark.live`-Isolation · GitHub Actions CI (Python 3.11–3.13)

**Zweisprachige Dokumentation** — Jeder Server hat `README.md` (Englisch, primär) und `README.de.md` (Deutsch), gegenseitig verlinkt mit Flaggen-Emoji.

---

## Schnellstart

Jeder Server ist unabhängig via `uvx` (empfohlen) oder `pip` installierbar. Die Konfigurationsdetails finden sich im jeweiligen Server-README.

**Beispiel — `swiss-transport-mcp` zu Claude Desktop hinzufügen:**

```jsonc
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

Für Server, die noch nicht auf PyPI verfügbar sind (Status 🔄), Repository klonen und starten:

```bash
git clone https://github.com/malkreide/<server-name>
cd <server-name>
uv run mcp dev src/<package>/server.py
```

---

## Kombinationsszenarien

| Szenario | Benötigte Server | Beispielabfrage |
|---|---|---|
| **Makroökonomischer Kontext** | swiss-snb-mcp + swiss-statistics | *«CHF/EUR-Entwicklung seit 2015 zusammen mit Schweizer BIP und CPI aus dem BFS?»* |
| **Multimodaler Pendelplan** | swiss-transport + swiss-road-mobility | *«Zug von Wädenswil nach Zürich HB, dann E-Bike zur ETH. Beste Option um 8:15 Uhr?»* |
| **Schulinfrastruktur-Audit** | zurich-opendata + swiss-statistics | *«Zürcher Schulen ohne Glasfaser im Vergleich zur kantonalen Breitbandversorgung?»* |
| **Bildungspolitische Recherche** | global-education + fedlex + swiss-statistics | *«Wie schneidet die CH beim Sekundarabschluss im OECD-Vergleich ab, und was schreibt das Gesetz vor?»* |
| **Umwelt-Briefing** | swiss-environment + wsl-envidat | *«Aktuelle Luftqualität in Zürich + aktuelle WSL-Studien zur städtischen Wärme?»* |
| **Kulturerbe-Explorer** | swiss-culture + swiss-academic-libraries | *«Lebendige Traditionen in Appenzell + verwandte digitalisierte Handschriften in e-rara?»* |

---

## Repository-Übersicht

Alle Server teilen den GitHub-Topic [`swiss-public-data-mcp`](https://github.com/topics/swiss-public-data-mcp) — damit lässt sich das gesamte Portfolio auf GitHub entdecken.

```
malkreide/
├── swiss-public-data-mcp          ← Dieser Index (Sie sind hier)
│
├── Verkehr & Mobilität
│   ├── swiss-transport-mcp
│   ├── swiss-road-mobility-mcp
│   └── sbb-opendata-mcp
│
├── Umwelt & Klima
│   ├── swiss-environment-mcp
│   └── wsl-envidat-mcp
│
├── Recht & Regulierung
│   ├── fedlex-mcp
│   ├── bakom-mcp
│   └── swiss-ip-mcp
│
├── Statistik & Geodaten
│   ├── swiss-statistics-mcp
│   └── zurich-opendata-mcp
│
├── Bildung & Forschung
│   ├── global-education-mcp
│   ├── eth-library-mcp
│   └── swiss-academic-libraries-mcp
│
├── Wirtschaft & Finanzen
│   └── swiss-snb-mcp
│
├── Kultur & Medien
│   ├── swiss-culture-mcp
│   └── srgssr-mcp
│
└── Lebensmittelsicherheit
    └── swiss-food-safety-mcp
```

---

## Mitwirken

Fehlerberichte und Feature-Anfragen sind in den jeweiligen Server-Repositories willkommen. Wer einen neuen MCP-Server für Schweizer Open Data gebaut hat und ihn hier gelistet haben möchte, kann ein Issue mit einer kurzen Beschreibung und einem Link eröffnen.

Die Server in diesem Portfolio sind persönliche Open-Source-Projekte und stehen in keiner Verbindung zu einem Arbeitgeber oder einer öffentlichen Institution.

---

## Lizenz

MIT-Lizenz — siehe [LICENSE](LICENSE)

## Autor

malkreide · [github.com/malkreide](https://github.com/malkreide)
