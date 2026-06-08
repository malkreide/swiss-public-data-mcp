# Client install snippets

Copy-paste configuration for adding these servers to common MCP clients. Each
server is a PyPI package run via [`uv`](https://docs.astral.sh/uv/)'s `uvx` over
stdio — no clone or manual install needed.

> Generated from [`portfolio.json`](../portfolio.json) by
> `scripts/generate_install_snippets.py`. Do not edit by hand. To insert these
> blocks into the server repos automatically, use
> `scripts/patch_install_readme.py` (idempotent; dry run by default).

## Where the config lives

| Client | Config file | Top-level key |
|---|---|---|
| Claude Desktop | `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) · `%APPDATA%\Claude\claude_desktop_config.json` (Windows) | `mcpServers` |
| Cursor | `~/.cursor/mcp.json` (global) or `.cursor/mcp.json` (project) | `mcpServers` |
| Windsurf | `~/.codeium/windsurf/mcp_config.json` | `mcpServers` |
| VS Code | `.vscode/mcp.json` (workspace) | `servers` |

The JSON blocks below use `mcpServers` (Claude Desktop / Cursor / Windsurf). For
**VS Code**, use the identical inner object under a top-level `servers` key
instead of `mcpServers`.

## swiss-transport-mcp

OJP 2.0 journey planning, SIRI-SX disruptions, occupancy, fares, train formation.

```json
{
  "mcpServers": {
    "swiss-transport-mcp": {
      "command": "uvx",
      "args": [
        "swiss-transport-mcp"
      ]
    }
  }
}
```

---

## swiss-road-mobility-mcp

GBFS shared mobility, EV charging, DATEX II traffic, Park & Rail.

```json
{
  "mcpServers": {
    "swiss-road-mobility-mcp": {
      "command": "uvx",
      "args": [
        "swiss-road-mobility-mcp"
      ]
    }
  }
}
```

---

## sbb-opendata-mcp

SBB Open Data via OpenDataSoft.

```json
{
  "mcpServers": {
    "sbb-opendata-mcp": {
      "command": "uvx",
      "args": [
        "sbb-opendata-mcp"
      ]
    }
  }
}
```

---

## swiss-energy-mcp

Swiss energy data via SFOE/BFE and GeoAdmin REST APIs.

```json
{
  "mcpServers": {
    "swiss-energy-mcp": {
      "command": "uvx",
      "args": [
        "swiss-energy-mcp"
      ]
    }
  }
}
```

---

## swiss-electricity-mcp

BFE energy dashboard, ElCom tariffs, public consumption data.

```json
{
  "mcpServers": {
    "swiss-electricity-mcp": {
      "command": "uvx",
      "args": [
        "swiss-electricity-mcp"
      ]
    }
  }
}
```

---

## swiss-environment-mcp

BAFU environmental data, NABEL air quality, hydrology.

```json
{
  "mcpServers": {
    "swiss-environment-mcp": {
      "command": "uvx",
      "args": [
        "swiss-environment-mcp"
      ]
    }
  }
}
```

---

## wsl-envidat-mcp

WSL / EnviDat environmental research datasets via CKAN.

```json
{
  "mcpServers": {
    "wsl-envidat-mcp": {
      "command": "uvx",
      "args": [
        "wsl-envidat-mcp"
      ]
    }
  }
}
```

---

## meteoswiss-mcp

MeteoSwiss Open Data for weather, climate normals, warnings.

```json
{
  "mcpServers": {
    "meteoswiss-mcp": {
      "command": "uvx",
      "args": [
        "meteoswiss-mcp"
      ]
    }
  }
}
```

---

## fedlex-mcp

Swiss federal law via Fedlex SPARQL endpoint.

```json
{
  "mcpServers": {
    "fedlex-mcp": {
      "command": "uvx",
      "args": [
        "fedlex-mcp"
      ]
    }
  }
}
```

---

## openlex-mcp

Canton Zurich legislation via ZH-Lex with full-text search and article extraction.

```json
{
  "mcpServers": {
    "openlex-mcp": {
      "command": "uvx",
      "args": [
        "openlex-mcp"
      ]
    }
  }
}
```

---

## swiss-courts-mcp

Swiss court decisions via entscheidsuche.ch, including federal and cantonal courts.

```json
{
  "mcpServers": {
    "swiss-courts-mcp": {
      "command": "uvx",
      "args": [
        "swiss-courts-mcp"
      ]
    }
  }
}
```

---

## register-mcp

Zefix commercial register and UID lookup.

```json
{
  "mcpServers": {
    "register-mcp": {
      "command": "uvx",
      "args": [
        "register-mcp"
      ]
    }
  }
}
```

---

## swiss-ip-mcp

IGE/IPI Swissreg trademarks, patents, SPCs.

```json
{
  "mcpServers": {
    "swiss-ip-mcp": {
      "command": "uvx",
      "args": [
        "swiss-ip-mcp"
      ],
      "env": {
        "IGE_USERNAME": "<your IGE_USERNAME>",
        "IGE_PASSWORD": "<your IGE_PASSWORD>"
      }
    }
  }
}
```

Requires credentials: replace the placeholder values for `IGE_USERNAME`, `IGE_PASSWORD`.

---

## swiss-statistics-mcp

BFS STAT-TAB PxWeb API for official Swiss statistics.

```json
{
  "mcpServers": {
    "swiss-statistics-mcp": {
      "command": "uvx",
      "args": [
        "swiss-statistics-mcp"
      ]
    }
  }
}
```

---

## zurich-opendata-mcp

City of Zurich weather, air quality, parking, geodata, Gemeinderat, tourism.

```json
{
  "mcpServers": {
    "zurich-opendata-mcp": {
      "command": "uvx",
      "args": [
        "zurich-opendata-mcp"
      ]
    }
  }
}
```

---

## swisstopo-mcp

Swiss federal geodata: geocoding, height, STAC, WMTS, OEREB and more.

```json
{
  "mcpServers": {
    "swisstopo-mcp": {
      "command": "uvx",
      "args": [
        "swisstopo-mcp"
      ]
    }
  }
}
```

---

## global-education-mcp

UNESCO UIS and OECD Education at a Glance.

```json
{
  "mcpServers": {
    "global-education-mcp": {
      "command": "uvx",
      "args": [
        "global-education-mcp"
      ]
    }
  }
}
```

---

## zh-education-mcp

Canton and City of Zurich education data: schools, statistics, infrastructure.

```json
{
  "mcpServers": {
    "zh-education-mcp": {
      "command": "uvx",
      "args": [
        "zh-education-mcp"
      ]
    }
  }
}
```

---

## swiss-academic-libraries-mcp

swisscovery, e-rara, e-periodica, e-manuscripta via SRU/OAI-PMH.

```json
{
  "mcpServers": {
    "swiss-academic-libraries-mcp": {
      "command": "uvx",
      "args": [
        "swiss-academic-libraries-mcp"
      ]
    }
  }
}
```

---

## eth-library-mcp

ETH Library Discovery and Persons APIs.

```json
{
  "mcpServers": {
    "eth-library-mcp": {
      "command": "uvx",
      "args": [
        "eth-library-mcp"
      ]
    }
  }
}
```

---

## swiss-snb-mcp

SNB data portal: exchange rates, balance sheet, policy rates, SARON, monetary aggregates.

```json
{
  "mcpServers": {
    "swiss-snb-mcp": {
      "command": "uvx",
      "args": [
        "swiss-snb-mcp"
      ]
    }
  }
}
```

---

## seco-labor-mcp

SECO labour market: unemployment, vacancies, workforce indicators.

```json
{
  "mcpServers": {
    "seco-labor-mcp": {
      "command": "uvx",
      "args": [
        "seco-labor-mcp"
      ]
    }
  }
}
```

---

## swiss-culture-mcp

BAK cultural heritage, ISOS, living traditions, RSS.

```json
{
  "mcpServers": {
    "swiss-culture-mcp": {
      "command": "uvx",
      "args": [
        "swiss-culture-mcp"
      ]
    }
  }
}
```

---

## swiss-cultural-heritage-mcp

Heritage inventories, monument lists, archaeological registers.

```json
{
  "mcpServers": {
    "swiss-cultural-heritage-mcp": {
      "command": "uvx",
      "args": [
        "swiss-cultural-heritage-mcp"
      ]
    }
  }
}
```

---

## bakom-mcp

BAKOM telecommunications and media open data.

```json
{
  "mcpServers": {
    "bakom-mcp": {
      "command": "uvx",
      "args": [
        "bakom-mcp"
      ]
    }
  }
}
```

---

## srgssr-mcp

SRG SSR weather, video, audio, EPG, Polis.

```json
{
  "mcpServers": {
    "srgssr-mcp": {
      "command": "uvx",
      "args": [
        "srgssr-mcp"
      ]
    }
  }
}
```

---

## news-monitor-mcp

Aggregated news monitoring across Swiss public media RSS feeds.

```json
{
  "mcpServers": {
    "news-monitor-mcp": {
      "command": "uvx",
      "args": [
        "news-monitor-mcp"
      ]
    }
  }
}
```

---

## bag-health-mcp

BAG public-health open data: indicators, programmes, statistics.

```json
{
  "mcpServers": {
    "bag-health-mcp": {
      "command": "uvx",
      "args": [
        "bag-health-mcp"
      ]
    }
  }
}
```

---

## bag-epl-mcp

BAG EPL: Spezialitätenliste, medication and reimbursement data.

```json
{
  "mcpServers": {
    "bag-epl-mcp": {
      "command": "uvx",
      "args": [
        "bag-epl-mcp"
      ]
    }
  }
}
```

---

## swiss-food-safety-mcp

BLV open data for food safety and veterinary inspections.

```json
{
  "mcpServers": {
    "swiss-food-safety-mcp": {
      "command": "uvx",
      "args": [
        "swiss-food-safety-mcp"
      ]
    }
  }
}
```

---

## swiss-democracy-mcp

Parliament OData, Swissvotes, referendums, voting results.

```json
{
  "mcpServers": {
    "swiss-democracy-mcp": {
      "command": "uvx",
      "args": [
        "swiss-democracy-mcp"
      ]
    }
  }
}
```

---

## parlament-mcp

Swiss Federal Parliament Curia Vista OData API.

```json
{
  "mcpServers": {
    "parlament-mcp": {
      "command": "uvx",
      "args": [
        "parlament-mcp"
      ]
    }
  }
}
```

---

## lobbywatch-mcp

Lobbywatch.ch transparency data on parliamentarians, interests, access badges.

```json
{
  "mcpServers": {
    "lobbywatch-mcp": {
      "command": "uvx",
      "args": [
        "lobbywatch-mcp"
      ]
    }
  }
}
```

---

## hn-tech-signal-mcp

Hacker News signal extraction for technology trend monitoring.

```json
{
  "mcpServers": {
    "hn-tech-signal-mcp": {
      "command": "uvx",
      "args": [
        "hn-tech-signal-mcp"
      ]
    }
  }
}
```
