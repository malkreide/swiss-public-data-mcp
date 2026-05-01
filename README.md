# swiss-public-data-mcp

![Servers](https://img.shields.io/badge/servers-27-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.11--3.13-blue)
![Protocol](https://img.shields.io/badge/protocol-MCP-orange)
![Data](https://img.shields.io/badge/data-Swiss%20Open%20Data-red)
![Audit](https://img.shields.io/badge/quality-audited%20against%20internal%20catalogue-purple)

> A curated portfolio of Model Context Protocol (MCP) servers connecting AI agents to Swiss public and open data — built on a reproducible quality methodology, not as one-off experiments.

[🇩🇪 Deutsche Version](README.de.md)

> ⚠️ **Disclaimer — independence of this project**
>
> This is a **personal open-source project** by Hayal Oezkan. It is developed in private capacity, on private time, with private infrastructure. It is **not** an official project of the City of Zürich, the Schulamt, the KI-Fachgruppe der Stadtverwaltung Zürich, or any other public institution. References to municipal or federal strategies in this README are descriptive — they explain how the portfolio happens to align with public-sector digital agendas. They do not imply institutional endorsement, mandate, or affiliation. All views expressed in this repository are personal.

---

## Why this exists

`opendata.swiss` lists roughly 13'600 public datasets. Geo.admin.ch, Fedlex, the SNB data portal, BAFU, BFS PxWeb, swisstopo, the parliament's OData feed, the Zürich Open Data portal — each exposes its own API, its own auth model, its own quirks. For an AI agent, this landscape is effectively **unreachable**: every dataset is one custom integration away.

This portfolio closes that last mile. Each server in the index translates one Swiss public-data source into a small set of well-designed, AI-consumable tools that any MCP-compatible client (Claude Desktop, VS Code + Continue, Cursor, Windsurf, custom agents) can call directly.

The portfolio is deliberately **synergistic, not just additive**: transport plus road mobility becomes a multimodal routing agent; statistics plus geodata enables spatial analysis; education plus law plus statistics supports policy research.

---

## How this aligns with public-sector digital strategies

The portfolio was built bottom-up from a practitioner's frustration with broken integrations — not top-down from a strategy paper. But the engineering choices map cleanly onto several public-sector digital agendas. Useful for context; never the justification for the work itself.

### City of Zürich (primary frame)

The portfolio operationalises three goals from **Strategien Zürich 2040**, Handlungsfeld IV «Leistungsfähige Stadt», Dimension Digitalisierung:

| City strategy goal | What this portfolio actually does |
|---|---|
| SZ 4 — «Open Government Data standardmässig öffentlich zur freien Verfügung» | Closes the gap between *available* and *AI-usable*. Data already published by the City and Confederation only delivers full value when agents can consume it without custom integration work. |
| SZ 1 — «Stadtinterne Prozesse durchgehend digital gedacht» | Servers like `zurich-opendata-mcp`, `zh-education-mcp`, `swiss-statistics-mcp` make agentic workflows possible on top of existing data infrastructure — without rebuilding it. |
| SZ 5 — «Digitalisierungskompetenzen der städtischen Angestellten» | Open-source, bilingual (EN/DE), publicly readable code serves as a concrete learning artefact. Not a course, but something to read and run. |

The **Digitalisierungsstrategie der Stadt Zürich (2024)** maps onto the portfolio's design choices in three places:

| City strategy focus | Portfolio response |
|---|---|
| Schwerpunkt 1 «Bleibender Mehrwert» / Stossrichtung B «Nutzer*innen im Fokus» | Each server has a single concrete anchor query it must answer. No anchor query, no server. |
| Schwerpunkt 3 «Vernetzte Zusammenarbeit» / Stossrichtung E «Informationen teilen» | Open source from day one. Bilingual docs. GitHub topic for portfolio-level discoverability. |
| Schwerpunkt 4 «Verantwortungsvoller Technologieeinsatz» / Stossrichtung I «Datenbestände nutzen» | No-Auth-First architecture is «Open by Default» translated into code. |

### Swiss Confederation (secondary frame)

| Federal strategy | Portfolio contribution |
|---|---|
| **Strategie Einsatz von KI-Systemen in der Bundesverwaltung**, Handlungsfeld 1 «Kompetenzen aufbauen» | Practitioner-driven, public, reusable competence build-up — useful as reference material for the federal CNAI competence network. |
| **Strategie Einsatz von KI-Systemen in der Bundesverwaltung**, Handlungsfeld 2 «Vertrauen verdienen» | No-Auth-First + Public-Open-Data-only = inherently lower-risk surface. No PII handled, no credentials stored, no opaque models trained. |
| **Strategie Digitale Schweiz 2026**, Wirkungsbereich Infrastruktur | Extends the practical value of the ~13'600 datasets on opendata.swiss by making them LLM-consumable through a common protocol. |
| **Strategie Digitale Schweiz 2026**, Wirkungsbereich Bildung & Kompetenzen | Bilingual EN/DE documentation lowers the entry barrier for digital-competence learners across language regions. |

---

## Quality methodology — why these servers are auditable, not just shipped

Building one MCP server is easy. Building **27** without quality drift is the actual problem. A reference catalogue plus an internal `mcp-audit` skill applies the same six-step audit to every server in the portfolio — instead of re-deriving best practices from first principles each time.

### The audit catalogue

Every server is auditable against a versioned catalogue of approximately **65 checks across eight categories**:

| Category | Coverage | Example checks |
|---|---|---|
| **ARCH** | Tool design, annotations, idempotency, repo structure, spec-version alignment | Tool naming, input-schema completeness, error semantics |
| **SDK** | FastMCP / TypeScript / Zod / lifecycle | Lifespan handling, capability declarations |
| **SEC** | Security (largest category) | Confused-deputy / OAuth proxy, SSRF, session hijacking, prompt-injection surface, secret handling |
| **SCALE** | Transport, load balancing, container, gateway | Stateless transport, horizontal scaling, gateway compatibility |
| **OBS** | Logging, errors, SIEM, tracing | Structured logs, error envelopes, trace correlation |
| **HITL** | Sampling, human-in-the-loop | Sampling capability, write-confirmation gates |
| **CH** | Swiss compliance — DSG / EDÖB | Data classification, residency, consent, lawful basis |
| **OPS** | Test strategy, documentation, phase architecture | Live-test isolation, phased roadmap, README completeness |

### How the methodology works

Each audit follows six numbered steps, in order:

1. **Profile first** — Six mandatory profile fields (transport, auth model, data class, write access, deployment, repo URL) determine which checks even apply to this server.
2. **Catalogue load** — The full check set is parsed and indexed by category and severity.
3. **Applicability filter** — A boolean `applies_when` clause is evaluated against the profile. Irrelevant checks (e.g. OAuth checks for a stdio-only no-auth server) drop out before the audit starts. Typical result: a `Public Open Data` / `read-only` / `no-auth` server runs ~15–20 of the ~65 checks; a `Verwaltungsdaten` / `OAuth-Proxy` / `Cloud` server runs ~45–55.
4. **Check execution** — Severity descending: `critical` first, then `high`, `medium`, `low`. Verification modes per check: `automated` (grep/AST), `code_review`, `config_check`, `runtime_test`. Every finding requires evidence with file path and line number — *«ein Finding ohne `path/to/file.py:42` ist eine Meinung, kein Befund.»*
5. **Finding documentation** — Per failed check: a structured finding with observed vs. expected behaviour, evidence, risk description, remediation diff, effort estimate (S / M / L / XL).
6. **Audit report** — Executive summary in three sentences, profile snapshot, applicability overview, findings table, detailed findings, remediation plan with proposed sequencing, audit metadata.

### Severity discipline

| Stufe | Bedeutung | Konsequenz |
|---|---|---|
| `critical` | Security gap or compliance breach | Blocks production. Must be fixed before release. |
| `high` | Architectural defect with significant risk | Fix in current sprint, max. one sprint of grace. |
| `medium` | Best-practice deviation, no acute risk | Plan for next sprint. |
| `low` | Polish, optimisation, stylistic | Backlog. |

> *«`critical` heisst critical. Wer die Stufe inflationiert, hat irgendwann nur noch `critical`.»*

### Why this matters for the portfolio

Every server in the index below has been or will be audited against this catalogue. The status badges (✅ / ⚠️ / 🔄 / 🔐) reflect not just "does it run" but "did it pass an audit at the appropriate severity gates". This is what makes a 27-server portfolio coherent rather than a graveyard of weekend projects.

---

## Server portfolio

**Status legend:** ✅ Stable, audit passed at `high`+ gate · ⚠️ Known finding(s) open · 🔄 Audit pending or PyPI publication pending · 🔐 Requires API credentials

### 🚆 Transport & Mobility

| Server | Description | Anchor query | Status |
|---|---|---|---|
| [swiss-transport-mcp](https://github.com/malkreide/swiss-transport-mcp) | OJP 2.0 journey planning, SIRI-SX disruptions, occupancy, fares, train formation | *«Earliest train Zürich → Bern tomorrow at 8 am?»* | ✅ |
| [swiss-road-mobility-mcp](https://github.com/malkreide/swiss-road-mobility-mcp) | GBFS shared mobility, EV charging, DATEX II traffic, Park & Rail | *«Available e-bikes near Zürich HB right now?»* | ✅ |
| [sbb-opendata-mcp](https://github.com/malkreide/sbb-opendata-mcp) | SBB Open Data via OpenDataSoft | *«Punctuality statistics for IC 1 line last month?»* | ✅ |

### 🌿 Environment & Climate

| Server | Description | Anchor query | Status |
|---|---|---|---|
| [swiss-environment-mcp](https://github.com/malkreide/swiss-environment-mcp) | BAFU environmental data, NABEL air quality, hydrology | *«PM2.5 levels in Zürich over the last 7 days?»* | ⚠️ |
| [wsl-envidat-mcp](https://github.com/malkreide/wsl-envidat-mcp) | WSL / EnviDat environmental research datasets via CKAN | *«Datasets on Alpine permafrost from WSL?»* | 🔄 |
| [meteoswiss-mcp](https://github.com/malkreide/meteoswiss-mcp) | MeteoSwiss Open Data — weather, climate normals, warnings | *«Was the Bise unusually strong in Zürich last winter?»* | 🔄 |

### ⚖️ Legal & Regulatory

| Server | Description | Anchor query | Status |
|---|---|---|---|
| [fedlex-mcp](https://github.com/malkreide/fedlex-mcp) | Swiss federal law via Fedlex SPARQL endpoint | *«What does Art. 62 BV say about public education?»* | ✅ |
| [register-mcp](https://github.com/malkreide/register-mcp) | Zefix commercial register and UID lookup | *«Active companies in Zürich Kreis 5 in the IT sector?»* | 🔄 |
| [swiss-ip-mcp](https://github.com/malkreide/swiss-ip-mcp) | IGE/IPI Swissreg — trademarks, patents, SPCs | *«Active Swiss trademarks containing 'Zurich' in class 41?»* | 🔐 |

### 📊 Statistics & Geodata

| Server | Description | Anchor query | Status |
|---|---|---|---|
| [swiss-statistics-mcp](https://github.com/malkreide/swiss-statistics-mcp) | BFS STAT-TAB PxWeb API — official Swiss statistics | *«Population of Swiss municipalities by canton, 2023?»* | 🔄 |
| [zurich-opendata-mcp](https://github.com/malkreide/zurich-opendata-mcp) | City of Zürich — weather, air quality, parking, geodata, Gemeinderat, tourism | *«Which school buildings in Zürich don't yet have fibre?»* | ⚠️ |

### 🎓 Education & Research

| Server | Description | Anchor query | Status |
|---|---|---|---|
| [global-education-mcp](https://github.com/malkreide/global-education-mcp) | UNESCO UIS and OECD Education at a Glance | *«Upper secondary attainment rates in CH vs. OECD average?»* | ✅ |
| [zh-education-mcp](https://github.com/malkreide/zh-education-mcp) | Canton and City of Zürich education data — schools, statistics, infrastructure | *«How are pupil numbers distributed across Zürich's seven Schulkreise?»* | 🔄 |
| [swiss-academic-libraries-mcp](https://github.com/malkreide/swiss-academic-libraries-mcp) | swisscovery, e-rara, e-periodica, e-manuscripta (SRU/OAI-PMH) | *«Digitised 18th-century Swiss maps in e-rara?»* | 🔄 |
| [eth-library-mcp](https://github.com/malkreide/eth-library-mcp) | ETH Library Discovery and Persons APIs | *«ETH publications on urban heat islands since 2020?»* | ⚠️ |

### 💰 Economics & Finance

| Server | Description | Anchor query | Status |
|---|---|---|---|
| [swiss-snb-mcp](https://github.com/malkreide/swiss-snb-mcp) | SNB data portal — exchange rates, balance sheet, interest rates, SARON, monetary aggregates | *«How has the EUR/CHF rate developed since 2015, and where is the SNB policy rate today?»* | ✅ |
| [seco-labor-mcp](https://github.com/malkreide/seco-labor-mcp) | SECO labour market — unemployment, vacancies, workforce indicators | *«Unemployment rate in Canton Zürich vs. Swiss average over the last 12 months?»* | 🔄 |

### 🎭 Culture & Media

| Server | Description | Anchor query | Status |
|---|---|---|---|
| [swiss-culture-mcp](https://github.com/malkreide/swiss-culture-mcp) | BAK cultural heritage, ISOS, living traditions, RSS | *«UNESCO-listed living traditions in Canton Zürich?»* | ✅ |
| [swiss-cultural-heritage-mcp](https://github.com/malkreide/swiss-cultural-heritage-mcp) | Heritage inventories, monument lists, archaeological registers | *«Listed Baudenkmäler in Zürich Kreis 6?»* | 🔄 |
| [bakom-mcp](https://github.com/malkreide/bakom-mcp) | BAKOM telecommunications and media open data | *«Which municipalities still lack 100 Mbit/s broadband?»* | 🔄 |
| [srgssr-mcp](https://github.com/malkreide/srgssr-mcp) | SRG SSR — weather, video, audio, EPG, Polis | *«Latest SRF news segments on education policy?»* | ✅ |
| [news-monitor-mcp](https://github.com/malkreide/news-monitor-mcp) | Aggregated news monitoring across Swiss public media RSS feeds | *«Top three education-policy stories in Swiss media this week?»* | 🔄 |

### 🏥 Health

| Server | Description | Anchor query | Status |
|---|---|---|---|
| [bag-health-mcp](https://github.com/malkreide/bag-health-mcp) | BAG public-health open data — indicators, programmes, statistics | *«Vaccination coverage by canton for the last reporting period?»* | 🔄 |
| [bag-epl-mcp](https://github.com/malkreide/bag-epl-mcp) | BAG EPL — Spezialitätenliste, medication and reimbursement data | *«Which medications were added to the Spezialitätenliste in the last six months?»* | 🔄 |

### 🍽️ Food Safety

| Server | Description | Anchor query | Status |
|---|---|---|---|
| [swiss-food-safety-mcp](https://github.com/malkreide/swiss-food-safety-mcp) | BLV open data — food safety and veterinary inspections | *«Recent food recall notices in Switzerland?»* | ✅ |

### 🗳️ Democracy

| Server | Description | Anchor query | Status |
|---|---|---|---|
| [swiss-democracy-mcp](https://github.com/malkreide/swiss-democracy-mcp) | Parliament OData (Vorstösse, Geschäfte, Sessionen), referendums, voting results | *«Which pending parliamentary motions concern AI in education?»* | 🔄 |

### 🛰️ Tech Intelligence

| Server | Description | Anchor query | Status |
|---|---|---|---|
| [hn-tech-signal-mcp](https://github.com/malkreide/hn-tech-signal-mcp) | Hacker News signal extraction for technology trend monitoring | *«What are this week's most-discussed AI-infrastructure topics?»* | 🔄 |

---

## Architecture principles

**No-Auth-First** — Phase 1 of every server uses only open, unauthenticated endpoints. Authenticated APIs are added in later phases with graceful degradation, so the server always remains usable without credentials.

**Phase architecture** — Every server is structured in explicit phases (Phase 1: No-Auth → Phase 2: Auth → Phase 3: advanced features). This enables rapid delivery of usable tools while documenting the roadmap honestly.

**Portfolio synergy** — Servers are designed to combine. See *Combination scenarios* below.

**Dual transport** — All servers support `stdio` (Claude Desktop, local IDEs) and `Streamable HTTP` (cloud deployment on Render.com / Railway).

**Standard stack** — FastMCP · Pydantic v2 · httpx · hatchling · `src/` layout · `pyproject.toml` · pytest with `@pytest.mark.live` isolation · GitHub Actions CI (Python 3.11–3.13) · `uvx`-ready packaging · PyPI publication via OIDC Trusted Publisher.

**Bilingual documentation** — Every server has `README.md` (English, primary) and `README.de.md` (German), cross-linked with flag emoji. Includes `CONTRIBUTING.md`, `CHANGELOG.md` (Keep-a-Changelog), portfolio banner, badges, architecture ASCII diagram, known limitations.

**Audit-driven quality** — See *Quality methodology* above. Every server passes through the same six-step audit before status changes from 🔄 to ✅.

---

## Quickstart

Each server is independently installable via `uvx` (recommended) or `pip`. See the individual server README for configuration details.

**Example — add `swiss-transport-mcp` to Claude Desktop:**

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

For servers not yet on PyPI (status 🔄), clone the repository and use:

```bash
git clone https://github.com/malkreide/<server-name>
cd <server-name>
uv run mcp dev src/<package>/server.py
```

---

## Combination scenarios

The real value isn't a single server — it's combinations. Six concrete examples:

| Scenario | Servers needed | Example query |
|---|---|---|
| **Macroeconomic context** | swiss-snb-mcp + swiss-statistics-mcp + seco-labor-mcp | *«CHF/EUR rate trend since 2015 alongside Swiss GDP, CPI, and unemployment?»* |
| **Multimodal commute planner** | swiss-transport-mcp + swiss-road-mobility-mcp + sbb-opendata-mcp | *«Train from Wädenswil to Zürich HB, then e-bike to ETH. Best option at 8:15, including punctuality history?»* |
| **School-infrastructure audit** | zh-education-mcp + zurich-opendata-mcp + swiss-statistics-mcp | *«Zürich schools without fibre vs. canton average broadband coverage and pupil distribution per Schulkreis?»* |
| **Education-policy research** | global-education-mcp + fedlex-mcp + swiss-statistics-mcp + swiss-democracy-mcp | *«How does CH upper secondary attainment compare to OECD, what does federal law mandate, and which motions are pending in parliament?»* |
| **Environmental briefing** | swiss-environment-mcp + meteoswiss-mcp + wsl-envidat-mcp | *«Current air quality and weather in Zürich, plus recent WSL studies on urban heat islands?»* |
| **Health-policy loop** | bag-health-mcp + bag-epl-mcp + fedlex-mcp + swiss-democracy-mcp | *«Recent additions to the Spezialitätenliste, vaccination coverage by canton, and the legal basis for both?»* |

---

## Repository map

All servers share the GitHub topic [`swiss-public-data-mcp`](https://github.com/topics/swiss-public-data-mcp) — use it to discover the full portfolio on GitHub.

```
malkreide/
├── swiss-public-data-mcp                 ← This index (you are here)
│
├── Transport & Mobility
│   ├── swiss-transport-mcp
│   ├── swiss-road-mobility-mcp
│   └── sbb-opendata-mcp
│
├── Environment & Climate
│   ├── swiss-environment-mcp
│   ├── wsl-envidat-mcp
│   └── meteoswiss-mcp
│
├── Legal & Regulatory
│   ├── fedlex-mcp
│   ├── register-mcp
│   └── swiss-ip-mcp
│
├── Statistics & Geodata
│   ├── swiss-statistics-mcp
│   └── zurich-opendata-mcp
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
├── Democracy
│   └── swiss-democracy-mcp
│
└── Tech Intelligence
    └── hn-tech-signal-mcp
```

---

## Roadmap

Concrete next steps for the portfolio as a whole (individual server roadmaps live in each server repo):

- **Cantonal legal layer for Zürich** — extend `fedlex-mcp` pattern to cantonal law (ZH-Lex, OS, ABl).
- **Swiss courts MCP** — federal and cantonal court decisions, anonymised.
- **Deeper swisstopo geodata** — beyond the WMS/WFS basics already in `zurich-opendata-mcp`.
- **Wikidata/semantic layer** — entity linking across servers (a Bundesrätin in `swiss-democracy-mcp` is the same person as in `fedlex-mcp` debates and `srgssr-mcp` coverage).
- **Historical time-series integration** — current servers are largely "now-oriented"; long-horizon comparison is patchy.

---

## Contributing

Bug reports and feature requests are welcome on the individual server repositories. If you build a new MCP server for Swiss open data and would like it listed here, open an issue with a short description and a link.

The internal audit catalogue is not currently open-sourced, but the methodology is described above. If you would like to apply a similar approach to your own MCP portfolio, the six steps work standalone.

---

## License

MIT License — see [LICENSE](LICENSE)

---

## Author

**Hayal Oezkan** · [github.com/malkreide](https://github.com/malkreide)

> *Reminder — this is a private open-source project. Affiliations mentioned in the author's other public profiles are not relevant to this repository. The strategic-alignment section above is descriptive analysis, not an institutional statement.*
