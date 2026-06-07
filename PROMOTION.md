# Promotion & distribution

How to broaden adoption of the portfolio's MCP servers beyond the official
registry. Generated context: **34 active servers**, source of truth
[`portfolio.json`](portfolio.json).

## Status of the levers

| Lever | Status |
|---|---|
| Official **MCP Registry** (`registry.modelcontextprotocol.io`) | **Done** — all 34 servers published under `io.github.malkreide/*`. |
| `modelcontextprotocol/servers` community list | **Retired** — that list was removed in favour of the MCP Registry, so there is nothing to submit there. |
| `punkpeye/awesome-mcp-servers` (community awesome list) | **Open** — accepts PRs; see below. |
| Third-party catalogues (Smithery, Glama, PulseMCP, MCP.so, …) | **Mostly automatic** — they ingest from the registry; a few accept manual submissions. |

---

## 1. awesome-mcp-servers (`punkpeye/awesome-mcp-servers`)

The most-referenced community list. Entry format (emoji legend: language ·
scope · OS):

```
- [owner/repo](https://github.com/owner/repo) 🐍 🏠 🍎 🪟 🐧 - One-line description.
```

`🐍` Python · `🏠` local (stdio) service · `🍎 🪟 🐧` cross-platform — which is
what every server in this portfolio is.

### Recommended: one collection entry (least spammy, high signal)

Rather than adding 34 lines from a single author, lead with one entry
for the portfolio and slot it under the most fitting current category (e.g. a
government / open-data section). Check the live README for the exact category
names before submitting.

```
- [malkreide/swiss-public-data-mcp](https://github.com/malkreide/swiss-public-data-mcp) 🐍 🏠 🍎 🪟 🐧 - Curated portfolio of 34 MCP servers for Swiss public & open data — transport, law, statistics, energy, environment, health, geodata, democracy and more.
```

### Optional: all 34 individual entries

If you prefer per-server visibility, distribute these into the matching topical
categories (transport, finance, law, location, etc.). Paste only the ones you
want — avoid dumping all 34 into a single category.

```
- [malkreide/swiss-transport-mcp](https://github.com/malkreide/swiss-transport-mcp) 🐍 🏠 🍎 🪟 🐧 - OJP 2.0 journey planning, SIRI-SX disruptions, occupancy, fares, train formation
- [malkreide/swiss-road-mobility-mcp](https://github.com/malkreide/swiss-road-mobility-mcp) 🐍 🏠 🍎 🪟 🐧 - GBFS shared mobility, EV charging, DATEX II traffic, Park & Rail
- [malkreide/sbb-opendata-mcp](https://github.com/malkreide/sbb-opendata-mcp) 🐍 🏠 🍎 🪟 🐧 - SBB Open Data via OpenDataSoft
- [malkreide/swiss-energy-mcp](https://github.com/malkreide/swiss-energy-mcp) 🐍 🏠 🍎 🪟 🐧 - Swiss energy data via SFOE/BFE and GeoAdmin REST APIs
- [malkreide/swiss-electricity-mcp](https://github.com/malkreide/swiss-electricity-mcp) 🐍 🏠 🍎 🪟 🐧 - BFE energy dashboard, ElCom tariffs, public consumption data
- [malkreide/swiss-environment-mcp](https://github.com/malkreide/swiss-environment-mcp) 🐍 🏠 🍎 🪟 🐧 - BAFU environmental data, NABEL air quality, hydrology
- [malkreide/wsl-envidat-mcp](https://github.com/malkreide/wsl-envidat-mcp) 🐍 🏠 🍎 🪟 🐧 - WSL / EnviDat environmental research datasets via CKAN
- [malkreide/meteoswiss-mcp](https://github.com/malkreide/meteoswiss-mcp) 🐍 🏠 🍎 🪟 🐧 - MeteoSwiss Open Data for weather, climate normals, warnings
- [malkreide/fedlex-mcp](https://github.com/malkreide/fedlex-mcp) 🐍 🏠 🍎 🪟 🐧 - Swiss federal law via Fedlex SPARQL endpoint
- [malkreide/openlex-mcp](https://github.com/malkreide/openlex-mcp) 🐍 🏠 🍎 🪟 🐧 - Canton Zurich legislation via ZH-Lex with full-text search and article extraction
- [malkreide/swiss-courts-mcp](https://github.com/malkreide/swiss-courts-mcp) 🐍 🏠 🍎 🪟 🐧 - Swiss court decisions via entscheidsuche.ch, including federal and cantonal courts
- [malkreide/register-mcp](https://github.com/malkreide/register-mcp) 🐍 🏠 🍎 🪟 🐧 - Zefix commercial register and UID lookup
- [malkreide/swiss-ip-mcp](https://github.com/malkreide/swiss-ip-mcp) 🐍 🏠 🍎 🪟 🐧 - IGE/IPI Swissreg trademarks, patents, SPCs
- [malkreide/swiss-statistics-mcp](https://github.com/malkreide/swiss-statistics-mcp) 🐍 🏠 🍎 🪟 🐧 - BFS STAT-TAB PxWeb API for official Swiss statistics
- [malkreide/zurich-opendata-mcp](https://github.com/malkreide/zurich-opendata-mcp) 🐍 🏠 🍎 🪟 🐧 - City of Zurich weather, air quality, parking, geodata, Gemeinderat, tourism
- [malkreide/swisstopo-mcp](https://github.com/malkreide/swisstopo-mcp) 🐍 🏠 🍎 🪟 🐧 - Swiss federal geodata: geocoding, height, STAC, WMTS, OEREB and more
- [malkreide/global-education-mcp](https://github.com/malkreide/global-education-mcp) 🐍 🏠 🍎 🪟 🐧 - UNESCO UIS and OECD Education at a Glance
- [malkreide/zh-education-mcp](https://github.com/malkreide/zh-education-mcp) 🐍 🏠 🍎 🪟 🐧 - Canton and City of Zurich education data: schools, statistics, infrastructure
- [malkreide/swiss-academic-libraries-mcp](https://github.com/malkreide/swiss-academic-libraries-mcp) 🐍 🏠 🍎 🪟 🐧 - swisscovery, e-rara, e-periodica, e-manuscripta via SRU/OAI-PMH
- [malkreide/eth-library-mcp](https://github.com/malkreide/eth-library-mcp) 🐍 🏠 🍎 🪟 🐧 - ETH Library Discovery and Persons APIs
- [malkreide/swiss-snb-mcp](https://github.com/malkreide/swiss-snb-mcp) 🐍 🏠 🍎 🪟 🐧 - SNB data portal: exchange rates, balance sheet, policy rates, SARON, monetary aggregates
- [malkreide/seco-labor-mcp](https://github.com/malkreide/seco-labor-mcp) 🐍 🏠 🍎 🪟 🐧 - SECO labour market: unemployment, vacancies, workforce indicators
- [malkreide/swiss-culture-mcp](https://github.com/malkreide/swiss-culture-mcp) 🐍 🏠 🍎 🪟 🐧 - BAK cultural heritage, ISOS, living traditions, RSS
- [malkreide/swiss-cultural-heritage-mcp](https://github.com/malkreide/swiss-cultural-heritage-mcp) 🐍 🏠 🍎 🪟 🐧 - Heritage inventories, monument lists, archaeological registers
- [malkreide/bakom-mcp](https://github.com/malkreide/bakom-mcp) 🐍 🏠 🍎 🪟 🐧 - BAKOM telecommunications and media open data
- [malkreide/srgssr-mcp](https://github.com/malkreide/srgssr-mcp) 🐍 🏠 🍎 🪟 🐧 - SRG SSR weather, video, audio, EPG, Polis
- [malkreide/news-monitor-mcp](https://github.com/malkreide/news-monitor-mcp) 🐍 🏠 🍎 🪟 🐧 - Aggregated news monitoring across Swiss public media RSS feeds
- [malkreide/bag-health-mcp](https://github.com/malkreide/bag-health-mcp) 🐍 🏠 🍎 🪟 🐧 - BAG public-health open data: indicators, programmes, statistics
- [malkreide/bag-epl-mcp](https://github.com/malkreide/bag-epl-mcp) 🐍 🏠 🍎 🪟 🐧 - BAG EPL: Spezialitätenliste, medication and reimbursement data
- [malkreide/swiss-food-safety-mcp](https://github.com/malkreide/swiss-food-safety-mcp) 🐍 🏠 🍎 🪟 🐧 - BLV open data for food safety and veterinary inspections
- [malkreide/swiss-democracy-mcp](https://github.com/malkreide/swiss-democracy-mcp) 🐍 🏠 🍎 🪟 🐧 - Parliament OData, Swissvotes, referendums, voting results
- [malkreide/parlament-mcp](https://github.com/malkreide/parlament-mcp) 🐍 🏠 🍎 🪟 🐧 - Swiss Federal Parliament Curia Vista OData API
- [malkreide/lobbywatch-mcp](https://github.com/malkreide/lobbywatch-mcp) 🐍 🏠 🍎 🪟 🐧 - Lobbywatch.ch transparency data on parliamentarians, interests, access badges
- [malkreide/hn-tech-signal-mcp](https://github.com/malkreide/hn-tech-signal-mcp) 🐍 🏠 🍎 🪟 🐧 - Hacker News signal extraction for technology trend monitoring
```

### PR text for the submission

**Title:**

```
Add swiss-public-data-mcp: curated portfolio of 34 Swiss open-data MCP servers
```

**Body:**

```
Adds a curated, audited portfolio of 34 MCP servers connecting AI agents to
Swiss public and open data (opendata.swiss, GeoAdmin, Fedlex, BFS, SNB, SBB,
MeteoSwiss, BAG, parliament, and more).

- All servers are production-ready, audited, and published in the official MCP
  Registry under the `io.github.malkreide/*` namespace.
- Python / stdio / cross-platform; installable via uvx.
- Single source of truth: https://github.com/malkreide/swiss-public-data-mcp/blob/main/portfolio.json

I've added one collection entry to keep the list tidy; happy to split into
per-category entries if you prefer.
```

---

## 2. Third-party catalogues

Most of these **ingest from the official MCP Registry automatically**, so being
in the registry (done) already propagates here over time. A few support manual
submission or claiming to speed it up:

- **Glama** (`glama.ai/mcp/servers`) — indexes from GitHub + registry; you can
  claim/verify the servers.
- **Smithery** (`smithery.ai`) — connect the GitHub repos / submit.
- **PulseMCP** (`pulsemcp.com`) — ingests from the registry; has a submit form.
- **MCP.so** — manual submit form.
- **mcpservers.org** — PR-based list.

### Cheap multipliers (in your own repos)

- Add the discovery topics `mcp` and `model-context-protocol` to each server
  repo (you already require `swiss-public-data-mcp`).
- Keep copy-paste client install snippets (Claude Desktop / Cursor / VS Code)
  in each server's README so a catalogue visitor can run it in one step.

