# swiss-public-data-mcp

![Servers](https://img.shields.io/badge/servers-17-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.11--3.13-blue)
![Protocol](https://img.shields.io/badge/protocol-MCP-orange)
![Data](https://img.shields.io/badge/data-Swiss%20Open%20Data-red)

> A curated portfolio of MCP servers connecting AI models to Swiss public and open data sources.

[🇩🇪 Deutsche Version](README.de.md)

---

## Overview

This repository is the central index for a portfolio of open-source [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) servers built around Swiss public data. Each server exposes a specific domain — transport, environment, law, statistics, education, culture — as a set of AI-ready tools that any MCP-compatible client (Claude Desktop, VS Code + Continue, Cursor, Windsurf) can use directly.

The portfolio follows a **No-Auth-First** architecture: every server works out of the box with publicly available, unauthenticated endpoints. Authenticated APIs are introduced in later phases with graceful degradation. All servers are built on the same Python stack (FastMCP, Pydantic v2, httpx) and support both local stdio and cloud-based Streamable HTTP transport.

The goal is a coherent, synergistic infrastructure — not a collection of isolated tools. Servers are designed to combine: transport + road mobility becomes a multimodal routing agent; statistics + geodata enables spatial analysis; education + law supports policy research.

---

## Server Portfolio

### 🚆 Transport & Mobility

| Server | Description | Tools | Anchor Demo | Status |
|---|---|---|---|---|
| [swiss-transport-mcp](https://github.com/malkreide/swiss-transport-mcp) | OJP 2.0 journey planning, SIRI-SX disruptions, occupancy, fares, train formation | 11 | *"Earliest train Zürich → Bern tomorrow at 8 am?"* | ✅ |
| [swiss-road-mobility-mcp](https://github.com/malkreide/swiss-road-mobility-mcp) | GBFS shared mobility, EV charging, DATEX II traffic, Park & Rail | 15 | *"Available e-bikes near Zürich HB right now?"* | ✅ |
| [sbb-opendata-mcp](https://github.com/malkreide/sbb-opendata-mcp) | SBB Open Data via OpenDataSoft | 10 | *"Punctuality statistics for IC 1 line last month?"* | ✅ |

### 🌿 Environment & Climate

| Server | Description | Tools | Anchor Demo | Status |
|---|---|---|---|---|
| [swiss-environment-mcp](https://github.com/malkreide/swiss-environment-mcp) | BAFU environmental data, NABEL air quality, hydrology | 12 | *"PM2.5 levels in Zürich over the last 7 days?"* | ⚠️ |
| [wsl-envidat-mcp](https://github.com/malkreide/wsl-envidat-mcp) | WSL / EnviDat environmental research datasets via CKAN | 12 | *"Datasets on Alpine permafrost from WSL?"* | 🔄 |

### ⚖️ Legal & Regulatory

| Server | Description | Tools | Anchor Demo | Status |
|---|---|---|---|---|
| [fedlex-mcp](https://github.com/malkreide/fedlex-mcp) | Swiss federal law via Fedlex SPARQL endpoint | 7 | *"What does Art. 62 BV say about public education?"* | ✅ |
| [bakom-mcp](https://github.com/malkreide/bakom-mcp) | BAKOM telecommunications and media open data | 12 | *"Which municipalities still lack 100 Mbit/s broadband?"* | 🔄 |
| [swiss-ip-mcp](https://github.com/malkreide/swiss-ip-mcp) | IGE/IPI Swissreg — trademarks, patents, SPCs | 11 | *"Active Swiss trademarks containing 'Zurich' in class 41?"* | 🔐 |

### 📊 Statistics & Geodata

| Server | Description | Tools | Anchor Demo | Status |
|---|---|---|---|---|
| [swiss-statistics-mcp](https://github.com/malkreide/swiss-statistics-mcp) | BFS STAT-TAB PxWeb API — official Swiss statistics | 9 | *"Population of Swiss municipalities by canton, 2023?"* | 🔄 |
| [zurich-opendata-mcp](https://github.com/malkreide/zurich-opendata-mcp) | City of Zürich — weather, air quality, parking, geodata, Gemeinderat, tourism | 23 | *"Which school buildings in Zürich don't yet have fibre?"* | ⚠️ |

### 🎓 Education & Research

| Server | Description | Tools | Anchor Demo | Status |
|---|---|---|---|---|
| [global-education-mcp](https://github.com/malkreide/global-education-mcp) | UNESCO UIS and OECD Education at a Glance | 10 | *"Upper secondary attainment rates in CH vs. OECD average?"* | ✅ |
| [eth-library-mcp](https://github.com/malkreide/eth-library-mcp) | ETH Library Discovery and Persons APIs | — | *"ETH publications on urban heat islands since 2020?"* | ⚠️ |
| [swiss-academic-libraries-mcp](https://github.com/malkreide/swiss-academic-libraries-mcp) | swisscovery, e-rara, e-periodica, e-manuscripta (SRU/OAI-PMH) | 11 | *"Digitised 18th-century Swiss maps in e-rara?"* | 🔄 |

### 🎭 Culture & Media

| Server | Description | Tools | Anchor Demo | Status |
|---|---|---|---|---|
| [swiss-culture-mcp](https://github.com/malkreide/swiss-culture-mcp) | BAK cultural heritage, ISOS, living traditions, RSS | 10 | *"UNESCO-listed living traditions in Canton Zürich?"* | ✅ |
| [srgssr-mcp](https://github.com/malkreide/srgssr-mcp) | SRG SSR — weather, video, audio, EPG, Polis | — | *"Latest SRF news segments on education policy?"* | 🔐 |

### 💰 Economics & Finance

| Server | Description | Tools | Anchor Demo | Status |
|---|---|---|---|---|
| [swiss-snb-mcp](https://github.com/malkreide/swiss-snb-mcp) | SNB data portal — exchange rates, balance sheet, interest rates, SARON, monetary aggregates | 9 | *"How has the EUR/CHF rate developed since 2015, and where is the SNB policy rate today?"* | ✅ |

### 🍽️ Food Safety

| Server | Description | Tools | Anchor Demo | Status |
|---|---|---|---|---|
| [swiss-food-safety-mcp](https://github.com/malkreide/swiss-food-safety-mcp) | BLV open data — food safety and veterinary inspections | 11 | *"Recent food recall notices in Switzerland?"* | ✅ |

**Status legend:** ✅ Stable &nbsp;|&nbsp; ⚠️ Known bug(s) open &nbsp;|&nbsp; 🔄 PyPI publication pending &nbsp;|&nbsp; 🔐 Requires API credentials

---

## Architecture Principles

**No-Auth-First** — Phase 1 of every server uses only open, unauthenticated endpoints. Authenticated APIs are added in later phases with graceful degradation, so the server always remains usable without credentials.

**Portfolio synergy** — Servers are designed to combine. Examples:
- `swiss-transport-mcp` + `swiss-road-mobility-mcp` → multimodal routing agent
- `swiss-statistics-mcp` + `zurich-opendata-mcp` → city benchmarking
- `global-education-mcp` + `fedlex-mcp` → education policy analysis
- `swiss-environment-mcp` + `wsl-envidat-mcp` → environmental research assistant

**Dual transport** — All servers support `stdio` (Claude Desktop, local IDEs) and `Streamable HTTP` (cloud deployment on Render.com).

**Standard stack** — FastMCP · Pydantic v2 · httpx · hatchling · `src/` layout · `pyproject.toml` · pytest with `@pytest.mark.live` isolation · GitHub Actions CI (Python 3.11–3.13)

**Bilingual documentation** — Every server has `README.md` (English, primary) and `README.de.md` (German), cross-linked with flag emoji.

---

## Quickstart

Each server is independently installable via `uvx` (recommended) or `pip`. See the individual server README for configuration details.

**Example — add `swiss-transport-mcp` to Claude Desktop:**

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

For servers not yet on PyPI (status 🔄), clone the repository and use:

```bash
git clone https://github.com/malkreide/<server-name>
cd <server-name>
uv run mcp dev src/<package>/server.py
```

---

## Combination Scenarios

| Scenario | Servers needed | Example query |
|---|---|---|
| **Macroeconomic context** | swiss-snb-mcp + swiss-statistics | *"CHF/EUR rate trend since 2015 alongside Swiss GDP and CPI from BFS?"* |
| **Multimodal commute planner** | swiss-transport + swiss-road-mobility | *"Train from Wädenswil to Zürich HB, then e-bike to ETH. Best option at 8:15?"* |
| **School infrastructure audit** | zurich-opendata + swiss-statistics | *"Zürich schools without fibre vs. canton average broadband coverage?"* |
| **Education policy research** | global-education + fedlex + swiss-statistics | *"How does CH upper secondary attainment compare to OECD, and what does the law mandate?"* |
| **Environmental briefing** | swiss-environment + wsl-envidat | *"Current air quality in Zürich + recent WSL studies on urban heat?"* |
| **Cultural heritage explorer** | swiss-culture + swiss-academic-libraries | *"Living traditions in Appenzell + related digitised manuscripts in e-rara?"* |

---

## Repository Map

All servers share the GitHub topic [`swiss-public-data-mcp`](https://github.com/topics/swiss-public-data-mcp) — use it to discover the full portfolio on GitHub.

```
malkreide/
├── swiss-public-data-mcp          ← This index (you are here)
│
├── Transport & Mobility
│   ├── swiss-transport-mcp
│   ├── swiss-road-mobility-mcp
│   └── sbb-opendata-mcp
│
├── Environment & Climate
│   ├── swiss-environment-mcp
│   └── wsl-envidat-mcp
│
├── Legal & Regulatory
│   ├── fedlex-mcp
│   ├── bakom-mcp
│   └── swiss-ip-mcp
│
├── Statistics & Geodata
│   ├── swiss-statistics-mcp
│   └── zurich-opendata-mcp
│
├── Education & Research
│   ├── global-education-mcp
│   ├── eth-library-mcp
│   └── swiss-academic-libraries-mcp
│
├── Economics & Finance
│   └── swiss-snb-mcp
│
├── Culture & Media
│   ├── swiss-culture-mcp
│   └── srgssr-mcp
│
└── Food Safety
    └── swiss-food-safety-mcp
```

---

## Contributing

Bug reports and feature requests are welcome on the individual server repositories. If you build a new MCP server for Swiss open data and would like it listed here, open an issue with a short description and a link.

Please note that all servers in this portfolio are personal open-source projects, independent of any employer or public institution.

---

## License

MIT License — see [LICENSE](LICENSE)

## Author

Hayal Oezkan · [github.com/malkreide](https://github.com/malkreide)
