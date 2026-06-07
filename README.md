# swiss-public-data-mcp

![Active servers](https://img.shields.io/badge/active%20servers-34-blue)
![Production ready](https://img.shields.io/badge/production--ready-34-brightgreen)
![Audited MCP repos](https://img.shields.io/badge/audited%20MCP%20repos-35-purple)
![Legacy servers](https://img.shields.io/badge/legacy-1-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.11--3.13-blue)
![Protocol](https://img.shields.io/badge/protocol-MCP-orange)
![Data](https://img.shields.io/badge/data-Swiss%20Open%20Data-red)
![Audit](https://img.shields.io/badge/quality-mcp--audit--skill-purple)

> A curated portfolio of Model Context Protocol (MCP) servers connecting AI agents to Swiss public and open data. The portfolio is maintained as an auditable inventory, not a loose list of experiments.

[🇩🇪 Deutsche Version](README.de.md)

> ⚠️ **Disclaimer - independence of this project**
>
> This is a **personal open-source project** by Hayal Oezkan. It is developed in private capacity, on private time, with private infrastructure. It is **not** an official project of the City of Zurich, the Schulamt, the KI-Fachgruppe der Stadtverwaltung Zurich, or any other public institution. References to municipal or federal strategies are descriptive context only. They do not imply endorsement, mandate, affiliation, or production use by any institution.

---

## Current Snapshot

Last checked: **2026-06-04**

| Metric | Current value |
|---|---:|
| Active portfolio servers | 34 |
| Production-ready active servers | 34 |
| MCP server repos with at least one audit | 35 |
| Legacy / superseded MCP server repos | 1 |
| Audit tooling repos | 1 |
| `opendata.swiss` datasets | 14'551 via `package_search?rows=0` |
| Machine-readable source of truth | [`portfolio.json`](portfolio.json) |
| MCP Registry entries (generated) | [`registry/`](registry/) |
| Publishing runbook | [`RUNBOOK.md`](RUNBOOK.md) |
| Promotion & distribution | [`PROMOTION.md`](PROMOTION.md) |
| Client install snippets | [`docs/INSTALL.md`](docs/INSTALL.md) |
| Required discovery topic | [`swiss-public-data-mcp`](https://github.com/topics/swiss-public-data-mcp) |
| Current MCP spec baseline for new audits | [`2025-11-25`](https://modelcontextprotocol.io/specification/versioning) |

All developed MCP server repositories in this inventory have completed at least one audit. All active portfolio servers are production ready; the legacy server remains listed as a production-ready migration candidate. The portfolio intentionally distinguishes **core Swiss public-data servers** from **adjacent context servers**. Adjacent servers, such as global education or technology-signal monitoring, are useful in combined workflows but are not presented as Swiss government data sources.

---

## Why This Exists

`opendata.swiss` lists roughly 14'500 public datasets, and the broader Swiss data landscape includes GeoAdmin, Fedlex, the SNB data portal, BAFU, BFS PxWeb, swisstopo, parliamentary OData, cantonal law collections, city open-data portals, and sector-specific APIs. For an AI agent, this landscape is still effectively unreachable until every source is translated into a small, typed, documented interface.

This portfolio closes that last mile. Each server turns one public-data source or coherent source family into MCP tools that clients such as Claude Desktop, VS Code + Continue, Cursor, Windsurf, or custom agents can call directly.

The portfolio is deliberately synergistic: transport plus road mobility enables multimodal routing; statistics plus geodata enables spatial analysis; education plus law plus parliamentary data supports policy research.

---

## Public-Sector Strategy Context

The portfolio was built bottom-up from integration needs, not top-down from a strategy document. Still, its design maps cleanly to public-sector digital agendas:

| Strategy | Portfolio contribution |
|---|---|
| [Strategien Zurich 2040](https://www.stadt-zuerich.ch/de/politik-und-verwaltung/politik-und-recht/strategie-politikfelder/zuerich-2040.html) | Turns "published open data" into "agent-usable open data" through reusable MCP interfaces. |
| [Digitalisierungsstrategie Stadt Zurich 2024](https://www.stadt-zuerich.ch/content/dam/web/de/politik-verwaltung/stadtverwaltung/fd/digitalisierungsstrategie.pdf) | Supports user-focused digital services, information sharing, and responsible data use without rebuilding existing APIs. |
| [SB021 - Strategy for AI systems in the Federal Administration](https://www.bk.admin.ch/bk/de/home/digitale-transformation-ikt-lenkung/vorgaben/sb021-strategie-einsatz-von-ki-systemen-in-der-bundesverwaltung.html) | Provides a public, readable competence-building artefact with explicit audit and risk methodology. |
| [Digital Switzerland Strategy 2026](https://www.admin.ch/en/newnsb/d6evGIoTYTmY4VMGk0-v0) | Extends the practical value of public digital infrastructure by making data sources LLM-consumable through a common protocol. |

These links are context, not authority. The repository remains a private open-source project.

---

## Quality & Audit Tooling

The audit methodology is now linked to the public [`mcp-audit-skill`](https://github.com/malkreide/mcp-audit-skill) repository instead of being described as an internal-only catalogue. The skill currently documents **68 checks across eight categories**:

| Category | Coverage |
|---|---|
| `ARCH` | Tool design, annotations, idempotency, repo structure, spec-version alignment |
| `SDK` | FastMCP / TypeScript / Zod / lifecycle |
| `SEC` | OAuth proxy risks, confused-deputy risks, SSRF, session hijacking, prompt-injection surface, secret handling |
| `SCALE` | Transport, statelessness, containerisation, load balancing, gateway compatibility |
| `OBS` | Logging, errors, SIEM, tracing, trace correlation |
| `HITL` | Sampling and human-in-the-loop behaviour |
| `CH` | Swiss DSG / EDOB / public-sector compliance considerations |
| `OPS` | Test strategy, documentation, phase architecture, release hygiene |

The audit skill is **not** a vulnerability scanner and **not** a compliance certificate. It is a reproducible review method. Architecture judgement remains human.

### Audit Gate

The portfolio now separates server maturity from audit evidence:

| Field | Meaning |
|---|---|
| Status | Runtime/documentation maturity of the server. |
| Audit | Published evidence for the audit gate. |

Every active server row now links to the corresponding GitHub audit directory in the `Audit` column. Most repositories use `audits/`; `swiss-culture-mcp` uses `audit/`, and `bag-epl-mcp` plus `swiss-food-safety-mcp` use `docs/audit/`. The archived legacy patent repository remains listed separately as a migration candidate.

Every published audit should include metadata like this:

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

## Server Portfolio

<!-- BEGIN GENERATED: server-portfolio -->
**Status legend:** ✅ Production ready and audited at least once · 🔐 Requires API credentials · 🧭 Adjacent/context source · 🗄️ Legacy or superseded

### 🚆 Transport & Mobility

| Server | Description | Anchor query | Status | Audit |
|---|---|---|---|---|
| [swiss-transport-mcp](https://github.com/malkreide/swiss-transport-mcp) | OJP 2.0 journey planning, SIRI-SX disruptions, occupancy, fares, train formation | *"Earliest train Zurich -> Bern tomorrow at 8 am?"* | ✅ | [audits/](https://github.com/malkreide/swiss-transport-mcp/tree/main/audits) |
| [swiss-road-mobility-mcp](https://github.com/malkreide/swiss-road-mobility-mcp) | GBFS shared mobility, EV charging, DATEX II traffic, Park & Rail | *"Available e-bikes near Zurich HB right now?"* | ✅ | [audits/](https://github.com/malkreide/swiss-road-mobility-mcp/tree/main/audits) |
| [sbb-opendata-mcp](https://github.com/malkreide/sbb-opendata-mcp) | SBB Open Data via OpenDataSoft | *"Punctuality statistics for IC 1 line last month?"* | ✅ | [audits/](https://github.com/malkreide/sbb-opendata-mcp/tree/main/audits) |

### ⚡ Energy & Infrastructure

| Server | Description | Anchor query | Status | Audit |
|---|---|---|---|---|
| [swiss-energy-mcp](https://github.com/malkreide/swiss-energy-mcp) | Swiss energy data via SFOE/BFE and GeoAdmin REST APIs | *"Which hydroelectric power plants are near Wädenswil?"* | ✅ | [audits/](https://github.com/malkreide/swiss-energy-mcp/tree/main/audits) |
| [swiss-electricity-mcp](https://github.com/malkreide/swiss-electricity-mcp) | BFE energy dashboard, ElCom tariffs, public consumption data | *"How did ewz electricity tariffs for category C3 develop since 2019?"* | ✅ | [audits/](https://github.com/malkreide/swiss-electricity-mcp/tree/main/audits) |

### 🌿 Environment & Climate

| Server | Description | Anchor query | Status | Audit |
|---|---|---|---|---|
| [swiss-environment-mcp](https://github.com/malkreide/swiss-environment-mcp) | BAFU environmental data, NABEL air quality, hydrology | *"PM2.5 levels in Zurich over the last 7 days?"* | ✅ | [audits/](https://github.com/malkreide/swiss-environment-mcp/tree/main/audits) |
| [wsl-envidat-mcp](https://github.com/malkreide/wsl-envidat-mcp) | WSL / EnviDat environmental research datasets via CKAN | *"Datasets on Alpine permafrost from WSL?"* | ✅ | [audits/](https://github.com/malkreide/wsl-envidat-mcp/tree/main/audits) |
| [meteoswiss-mcp](https://github.com/malkreide/meteoswiss-mcp) | MeteoSwiss Open Data for weather, climate normals, warnings | *"Was the Bise unusually strong in Zurich last winter?"* | ✅ | [audits/](https://github.com/malkreide/meteoswiss-mcp/tree/main/audits) |

### ⚖️ Legal, Courts & Regulatory

| Server | Description | Anchor query | Status | Audit |
|---|---|---|---|---|
| [fedlex-mcp](https://github.com/malkreide/fedlex-mcp) | Swiss federal law via Fedlex SPARQL endpoint | *"What does Art. 62 BV say about public education?"* | ✅ | [audits/](https://github.com/malkreide/fedlex-mcp/tree/main/audits) |
| [openlex-mcp](https://github.com/malkreide/openlex-mcp) | Canton Zurich legislation via ZH-Lex with full-text search and article extraction | *"Which Zurich laws regulate school responsibilities?"* | ✅ | [audits/](https://github.com/malkreide/openlex-mcp/tree/master/audits) |
| [swiss-courts-mcp](https://github.com/malkreide/swiss-courts-mcp) | Swiss court decisions via entscheidsuche.ch, including federal and cantonal courts | *"Recent Federal Supreme Court cases on school transport?"* | ✅ | [audits/](https://github.com/malkreide/swiss-courts-mcp/tree/master/audits) |
| [register-mcp](https://github.com/malkreide/register-mcp) | Zefix commercial register and UID lookup | *"Active companies in Zurich Kreis 5 in the IT sector?"* | ✅ | [audits/](https://github.com/malkreide/register-mcp/tree/main/audits) |
| [swiss-ip-mcp](https://github.com/malkreide/swiss-ip-mcp) | IGE/IPI Swissreg trademarks, patents, SPCs | *"Active Swiss trademarks containing 'Zurich' in class 41?"* | ✅ 🔐 | [audits/](https://github.com/malkreide/swiss-ip-mcp/tree/main/audits) |

### 📊 Statistics & Geodata

| Server | Description | Anchor query | Status | Audit |
|---|---|---|---|---|
| [swiss-statistics-mcp](https://github.com/malkreide/swiss-statistics-mcp) | BFS STAT-TAB PxWeb API for official Swiss statistics | *"Population of Swiss municipalities by canton, 2023?"* | ✅ | [audits/](https://github.com/malkreide/swiss-statistics-mcp/tree/main/audits) |
| [zurich-opendata-mcp](https://github.com/malkreide/zurich-opendata-mcp) | City of Zurich weather, air quality, parking, geodata, Gemeinderat, tourism | *"Which school buildings in Zurich do not yet have fibre?"* | ✅ | [audits/](https://github.com/malkreide/zurich-opendata-mcp/tree/main/audits) |
| [swisstopo-mcp](https://github.com/malkreide/swisstopo-mcp) | Swiss federal geodata: geocoding, height, STAC, WMTS, OEREB and more | *"What is the elevation profile between Zurich HB and Uetliberg?"* | ✅ | [audits/](https://github.com/malkreide/swisstopo-mcp/tree/master/audits) |

### 🎓 Education & Research

| Server | Description | Anchor query | Status | Audit |
|---|---|---|---|---|
| [global-education-mcp](https://github.com/malkreide/global-education-mcp) | UNESCO UIS and OECD Education at a Glance | *"Upper secondary attainment rates in CH vs. OECD average?"* | ✅ 🧭 | [audits/](https://github.com/malkreide/global-education-mcp/tree/main/audits) |
| [zh-education-mcp](https://github.com/malkreide/zh-education-mcp) | Canton and City of Zurich education data: schools, statistics, infrastructure | *"How are pupil numbers distributed across Zurich's seven Schulkreise?"* | ✅ | [audits/](https://github.com/malkreide/zh-education-mcp/tree/main/audits) |
| [swiss-academic-libraries-mcp](https://github.com/malkreide/swiss-academic-libraries-mcp) | swisscovery, e-rara, e-periodica, e-manuscripta via SRU/OAI-PMH | *"Digitised 18th-century Swiss maps in e-rara?"* | ✅ | [audits/](https://github.com/malkreide/swiss-academic-libraries-mcp/tree/main/audits) |
| [eth-library-mcp](https://github.com/malkreide/eth-library-mcp) | ETH Library Discovery and Persons APIs | *"ETH publications on urban heat islands since 2020?"* | ✅ | [audits/](https://github.com/malkreide/eth-library-mcp/tree/main/audits) |

### 💰 Economics & Finance

| Server | Description | Anchor query | Status | Audit |
|---|---|---|---|---|
| [swiss-snb-mcp](https://github.com/malkreide/swiss-snb-mcp) | SNB data portal: exchange rates, balance sheet, policy rates, SARON, monetary aggregates | *"EUR/CHF trend since 2015 and current SNB policy rate?"* | ✅ | [audits/](https://github.com/malkreide/swiss-snb-mcp/tree/main/audits) |
| [seco-labor-mcp](https://github.com/malkreide/seco-labor-mcp) | SECO labour market: unemployment, vacancies, workforce indicators | *"Unemployment rate in Canton Zurich vs. Swiss average over the last 12 months?"* | ✅ | [audits/](https://github.com/malkreide/seco-labor-mcp/tree/main/audits) |

### 🎭 Culture & Media

| Server | Description | Anchor query | Status | Audit |
|---|---|---|---|---|
| [swiss-culture-mcp](https://github.com/malkreide/swiss-culture-mcp) | BAK cultural heritage, ISOS, living traditions, RSS | *"UNESCO-listed living traditions in Canton Zurich?"* | ✅ | [audit/](https://github.com/malkreide/swiss-culture-mcp/tree/main/audit) |
| [swiss-cultural-heritage-mcp](https://github.com/malkreide/swiss-cultural-heritage-mcp) | Heritage inventories, monument lists, archaeological registers | *"Listed Baudenkmäler in Zurich Kreis 6?"* | ✅ | [audits/](https://github.com/malkreide/swiss-cultural-heritage-mcp/tree/main/audits) |
| [bakom-mcp](https://github.com/malkreide/bakom-mcp) | BAKOM telecommunications and media open data | *"Which municipalities still lack 100 Mbit/s broadband?"* | ✅ | [audits/](https://github.com/malkreide/bakom-mcp/tree/main/audits) |
| [srgssr-mcp](https://github.com/malkreide/srgssr-mcp) | SRG SSR weather, video, audio, EPG, Polis | *"Latest SRF news segments on education policy?"* | ✅ | [audits/](https://github.com/malkreide/srgssr-mcp/tree/main/audits) |
| [news-monitor-mcp](https://github.com/malkreide/news-monitor-mcp) | Aggregated news monitoring across Swiss public media RSS feeds | *"Top three education-policy stories in Swiss media this week?"* | ✅ 🧭 | [audits/](https://github.com/malkreide/news-monitor-mcp/tree/main/audits) |

### 🏥 Health

| Server | Description | Anchor query | Status | Audit |
|---|---|---|---|---|
| [bag-health-mcp](https://github.com/malkreide/bag-health-mcp) | BAG public-health open data: indicators, programmes, statistics | *"Vaccination coverage by canton for the last reporting period?"* | ✅ | [audits/](https://github.com/malkreide/bag-health-mcp/tree/main/audits) |
| [bag-epl-mcp](https://github.com/malkreide/bag-epl-mcp) | BAG EPL: Spezialitätenliste, medication and reimbursement data | *"Which medications were added to the Spezialitätenliste in the last six months?"* | ✅ | [docs/audit/](https://github.com/malkreide/bag-epl-mcp/tree/main/docs/audit) |

### 🍽️ Food Safety

| Server | Description | Anchor query | Status | Audit |
|---|---|---|---|---|
| [swiss-food-safety-mcp](https://github.com/malkreide/swiss-food-safety-mcp) | BLV open data for food safety and veterinary inspections | *"Recent food recall notices in Switzerland?"* | ✅ | [docs/audit/](https://github.com/malkreide/swiss-food-safety-mcp/tree/main/docs/audit) |

### 🗳️ Democracy & Transparency

| Server | Description | Anchor query | Status | Audit |
|---|---|---|---|---|
| [swiss-democracy-mcp](https://github.com/malkreide/swiss-democracy-mcp) | Parliament OData, Swissvotes, referendums, voting results | *"Which pending parliamentary motions concern AI in education?"* | ✅ | [audits/](https://github.com/malkreide/swiss-democracy-mcp/tree/main/audits) |
| [parlament-mcp](https://github.com/malkreide/parlament-mcp) | Swiss Federal Parliament Curia Vista OData API | *"Welche Vorstösse zu KI in der Schule sind hängig?"* | ✅ | [audits/](https://github.com/malkreide/parlament-mcp/tree/main/audits) |
| [lobbywatch-mcp](https://github.com/malkreide/lobbywatch-mcp) | Lobbywatch.ch transparency data on parliamentarians, interests, access badges | *"Which education-commission members have ties to private education providers?"* | ✅ 🧭 | [audits/](https://github.com/malkreide/lobbywatch-mcp/tree/main/audits) |

### 🛰️ Tech Intelligence

| Server | Description | Anchor query | Status | Audit |
|---|---|---|---|---|
| [hn-tech-signal-mcp](https://github.com/malkreide/hn-tech-signal-mcp) | Hacker News signal extraction for technology trend monitoring | *"What are this week's most-discussed AI-infrastructure topics?"* | ✅ 🧭 | [audits/](https://github.com/malkreide/hn-tech-signal-mcp/tree/main/audits) |

### 🗄️ Legacy / Superseded

| Server | Current treatment | Reason |
|---|---|---|
| [MCP-Server-for-patent-research-](https://github.com/malkreide/MCP-Server-for-patent-research-) | Production-ready legacy / migration candidate | Older audited patent research server with broad EPO/Swissreg scope and naming inconsistencies. Keep discoverable, but prefer `swiss-ip-mcp` for the current portfolio unless the old repo is renamed and aligned with the current portfolio conventions. |
<!-- END GENERATED: server-portfolio -->

---

## Architecture Principles

**No-Auth-First** - Phase 1 of every core server should use only open, unauthenticated endpoints. Authenticated APIs can be added later with graceful degradation.

**Phase architecture** - Server READMEs should distinguish Phase 1 no-auth, Phase 2 authenticated/advanced, and Phase 3 production hardening.

**Dual transport** - Servers should support `stdio` for local clients and Streamable HTTP for cloud or gateway deployment when appropriate.

**Standard stack** - Python servers use FastMCP, Pydantic v2, httpx, hatchling, `src/` layout, pytest with `@pytest.mark.live` isolation, GitHub Actions CI for Python 3.11-3.13, and `uvx`-ready packaging where possible.

**Bilingual documentation** - Core servers should keep `README.md` and `README.de.md` cross-linked.

**Audit-driven quality** - Production-ready status requires at least one completed audit. Active server rows link directly to their audit evidence directory.

---

## Quickstart

Each server is independently installable via `uvx` or `pip` if published. See the individual server README for exact package names and configuration.

Example: add `swiss-transport-mcp` to Claude Desktop:

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

For servers not yet on PyPI:

```bash
git clone https://github.com/malkreide/<server-name>
cd <server-name>
uv run mcp dev src/<package>/server.py
```

---

## Combination Scenarios

| Scenario | Servers needed | Example query |
|---|---|---|
| Macroeconomic context | swiss-snb-mcp + swiss-statistics-mcp + seco-labor-mcp | *"CHF/EUR trend since 2015 alongside Swiss GDP, CPI, and unemployment?"* |
| Multimodal commute planner | swiss-transport-mcp + swiss-road-mobility-mcp + sbb-opendata-mcp | *"Train from Wädenswil to Zurich HB, then e-bike to ETH. Best option at 8:15, including punctuality history?"* |
| School-infrastructure audit | zh-education-mcp + zurich-opendata-mcp + swiss-statistics-mcp + swiss-electricity-mcp | *"Zurich schools without fibre, pupil load per Schulkreis, and electricity tariff exposure?"* |
| Education-policy research | global-education-mcp + fedlex-mcp + openlex-mcp + parlament-mcp + lobbywatch-mcp | *"How does Swiss upper secondary attainment compare to OECD, what does law require, and which parliamentary actors are involved?"* |
| Environmental briefing | swiss-environment-mcp + meteoswiss-mcp + wsl-envidat-mcp + swisstopo-mcp | *"Current air quality and weather in Zurich, plus geodata and WSL studies on urban heat islands?"* |
| Health-policy loop | bag-health-mcp + bag-epl-mcp + fedlex-mcp + swiss-democracy-mcp | *"Recent additions to the Spezialitätenliste, vaccination coverage by canton, and the legal basis for both?"* |
| Energy siting context | swiss-energy-mcp + swiss-electricity-mcp + swisstopo-mcp + swiss-statistics-mcp | *"Which municipalities combine high solar potential, grid tariff pressure, and population growth?"* |

---

## Repository Map

All active servers should carry the GitHub topic [`swiss-public-data-mcp`](https://github.com/topics/swiss-public-data-mcp). The machine-readable inventory in [`portfolio.json`](portfolio.json) is the canonical list.

<!-- BEGIN GENERATED: repository-map -->
```text
malkreide/
├── swiss-public-data-mcp                 ← this index
├── mcp-audit-skill                       ← audit methodology, not a server
│
├── Transport & Mobility
│   ├── swiss-transport-mcp
│   ├── swiss-road-mobility-mcp
│   └── sbb-opendata-mcp
│
├── Energy & Infrastructure
│   ├── swiss-energy-mcp
│   └── swiss-electricity-mcp
│
├── Environment & Climate
│   ├── swiss-environment-mcp
│   ├── wsl-envidat-mcp
│   └── meteoswiss-mcp
│
├── Legal, Courts & Regulatory
│   ├── fedlex-mcp
│   ├── openlex-mcp
│   ├── swiss-courts-mcp
│   ├── register-mcp
│   └── swiss-ip-mcp
│
├── Statistics & Geodata
│   ├── swiss-statistics-mcp
│   ├── zurich-opendata-mcp
│   └── swisstopo-mcp
│
├── Education & Research
│   ├── global-education-mcp
│   ├── zh-education-mcp
│   ├── swiss-academic-libraries-mcp
│   └── eth-library-mcp
│
├── Economics & Finance
│   ├── swiss-snb-mcp
│   └── seco-labor-mcp
│
├── Culture & Media
│   ├── swiss-culture-mcp
│   ├── swiss-cultural-heritage-mcp
│   ├── bakom-mcp
│   ├── srgssr-mcp
│   └── news-monitor-mcp
│
├── Health
│   ├── bag-health-mcp
│   └── bag-epl-mcp
│
├── Food Safety
│   └── swiss-food-safety-mcp
│
├── Democracy & Transparency
│   ├── swiss-democracy-mcp
│   ├── parlament-mcp
│   └── lobbywatch-mcp
│
├── Tech Intelligence
│   └── hn-tech-signal-mcp
│
└── Legacy / Superseded
    └── MCP-Server-for-patent-research-
```
<!-- END GENERATED: repository-map -->

---

## Maintenance Roadmap

The previous roadmap items for Zurich cantonal law, Swiss courts, and deeper swisstopo geodata have moved from roadmap to inventory because `openlex-mcp`, `swiss-courts-mcp`, and `swisstopo-mcp` now exist.

Current portfolio maintenance priorities:

- Keep all linked audit directories current with report metadata, findings, and remediation notes.
- If the archived legacy patent repository is unarchived, add an `audits/` directory there or migrate its audit evidence into `swiss-ip-mcp`.
- Align `mcp-audit-skill` and all future reports with MCP spec `2025-11-25`, while retaining older spec versions in report metadata where applicable.
- Decide whether `parlament-mcp` remains a specialised server or is folded into `swiss-democracy-mcp`.
- Decide whether `MCP-Server-for-patent-research-` is renamed, archived, or migrated into `swiss-ip-mcp`.
- The Server Portfolio tables and Repository Map are generated from `portfolio.json` by [`scripts/generate_readme.py`](scripts/generate_readme.py); a CI check (`--check`) blocks drift such as the electricity rename above.

---

## Contributing

Bug reports and feature requests are welcome on the individual server repositories. If you build a new MCP server for Swiss open data and would like it listed here, open an issue with a short description, a repository link, data-source notes, and the intended audit profile.

When changing the inventory, edit [`portfolio.json`](portfolio.json) and run `python scripts/generate_readme.py` to refresh the generated README sections. CI verifies the READMEs stay in sync via `python scripts/generate_readme.py --check`.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the full contribution guide and [`SECURITY.md`](SECURITY.md) for how to report vulnerabilities.

---

## License

MIT License - see [LICENSE](LICENSE)

---

## Author

**Hayal Oezkan** · [github.com/malkreide](https://github.com/malkreide)

> Reminder: this is a private open-source project. Affiliations mentioned in the author's other public profiles are not relevant to this repository.
