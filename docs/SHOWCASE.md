# opendata.swiss showcase submission

Prepared copy for submitting this portfolio to the
[opendata.swiss showcase](https://opendata.swiss/en/showcase) via the official
form at <https://opendata.swiss/en/submit-showcase>.

The form has five blocks: showcase information, datasets used, tags, categories,
and contact details. Fields marked `*` are mandatory. The text below is ready to
paste; nothing here is submitted automatically.

---

## 1. Showcase information

| Form field | Value to paste |
|---|---|
| **Title\*** | `swiss-public-data-mcp — Swiss open data for AI assistants` |
| **Showcase URL\*** | `https://github.com/malkreide/swiss-public-data-mcp` |
| **Image URL** | `https://raw.githubusercontent.com/malkreide/swiss-public-data-mcp/main/docs/showcase-card.png` |
| **Type of content\*** | `Application` (DE: *Applikation*) |

### Short description\* (max. 400 characters)

**English (352 characters):**

```
42 open-source Model Context Protocol servers that let AI assistants query
Swiss open data directly — transport, law, statistics, geodata, energy,
environment, health, education and democracy. Each server is a thin, read-only
client for an official API; no data is copied or re-hosted. Every server is
audited, MIT-licensed and installable in one line.
```

**German (398 characters):**

```
42 quelloffene Model-Context-Protocol-Server, mit denen KI-Assistenten Schweizer
Open Data direkt abfragen — Verkehr, Recht, Statistik, Geodaten, Energie, Umwelt,
Gesundheit, Bildung und Demokratie. Jeder Server ist ein schlanker, nur lesender
Client für eine offizielle API; Daten werden nicht kopiert oder neu gehostet.
Alle Server sind auditiert, MIT-lizenziert und in einer Zeile installierbar.
```

> Both variants are under the 400-character limit. Check the character count
> again if the server count changes — see "Keeping this file honest" below.

### On the image field

The form accepts an image URL, and showcase cards look noticeably weaker without
one. [`docs/showcase-card.png`](showcase-card.png) is a purpose-built 1200×630
card served straight from this repository over `raw.githubusercontent.com`, so
there is no separate asset hosting to maintain.

It is **generated, not hand-drawn**: the counts it states and the number of
converging lines come from `portfolio.json` via
[`scripts/generate_showcase_card.py`](../scripts/generate_showcase_card.py), and
CI fails if the HTML drifts from the inventory. Edit
`docs/showcase-card.tmpl.html` for design changes, then regenerate and
re-render — the PNG is a committed bitmap, so `--check` cannot catch a stale
image on its own.

The same file works as the repository's social preview (**Settings → Social
preview**), which is worth setting so links to the repo render the same card.

---

## 2. Datasets used

The form autocompletes against existing `opendata.swiss` datasets. Not every
source in this portfolio is catalogued there (Fedlex, entscheidsuche.ch, ZH-Lex,
Zefix and the SRG SSR APIs are direct APIs rather than catalogued datasets), so
select the ones that do resolve. Search these publishers and pick the datasets
that come up:

| Search term | Covered by |
|---|---|
| `Bundesamt für Statistik` / STAT-TAB | `swiss-statistics-mcp` |
| `Stadt Zürich` | `zurich-opendata-mcp`, `zh-education-mcp` |
| `MeteoSchweiz` | `meteoswiss-mcp` |
| `Bundesamt für Umwelt` / NABEL | `swiss-environment-mcp` |
| `Bundesamt für Energie` / Energiedashboard | `swiss-energy-mcp`, `swiss-electricity-mcp` |
| `SBB` / Fahrgastfrequenzen | `sbb-opendata-mcp`, `swiss-transport-mcp` |
| `Bundesamt für Gesundheit` | `bag-health-mcp`, `bag-epl-mcp` |
| `swisstopo` / geo.admin.ch | `swisstopo-mcp` |
| `Gebäude- und Wohnungsregister` | `swiss-housing-mcp` |
| `Lebensmittelsicherheit` / BLV | `swiss-food-safety-mcp` |
| `BAKOM` | `bakom-mcp` |
| `EnviDat` / WSL | `wsl-envidat-mcp` |

Selecting eight to twelve representative datasets is enough; the full,
authoritative source list is the `Data source` column of the
[server portfolio](../README.md#server-portfolio), which links every server to
the exact portal or API it reads.

---

## 3. Tags

```
mcp, model-context-protocol, ai, llm, open-data, api, python, open-source
```

---

## 4. Categories

The portfolio spans most of the opendata.swiss category tree. Tick the
categories that match servers actually in the inventory:

| opendata.swiss category | Portfolio coverage |
|---|---|
| Population and society | `swiss-statistics-mcp`, `swiss-housing-mcp` |
| Education, culture and sport | `zh-education-mcp`, `swiss-culture-mcp`, `swiss-cultural-heritage-mcp`, `swiss-academic-libraries-mcp`, `eth-library-mcp`, `swiss-holidays-mcp` |
| Energy | `swiss-energy-mcp`, `swiss-electricity-mcp` |
| Health | `bag-health-mcp`, `bag-epl-mcp` |
| Justice, legal system and public safety | `fedlex-mcp`, `openlex-mcp`, `swiss-courts-mcp`, `amtsblatt-mcp` |
| Agriculture, fisheries, forestry and food | `swiss-food-safety-mcp` |
| Government and public sector | `swiss-democracy-mcp`, `parlament-mcp`, `swiss-procurement-mcp`, `i14y-mcp`, `termdat-mcp`, `lindas-mcp` |
| Regions and cities | `zurich-opendata-mcp`, `swisstopo-mcp` |
| Environment | `swiss-environment-mcp`, `meteoswiss-mcp`, `wsl-envidat-mcp` |
| Transport | `swiss-transport-mcp`, `swiss-road-mobility-mcp`, `sbb-opendata-mcp` |
| Economy and finance | `swiss-snb-mcp`, `swiss-efv-mcp`, `seco-labor-mcp`, `register-mcp` |
| Science and technology | `swiss-ip-mcp`, `bakom-mcp` |

Leave *International topics* and *Provisional data* unticked.

---

## 5. Contact details

| Form field | Value |
|---|---|
| **Name of contact person, unit or team\*** | `Hayal Oezkan` |
| **Email address\*** (not published) | *your private address* |
| **Twitter account** (published) | *leave empty unless you want it public* |
| **GitHub account** (published) | `https://github.com/malkreide` |

The submission is a **private open-source project**. Do not enter an
institutional affiliation — the README carries an explicit independence
disclaimer and the showcase entry must not contradict it.

---

## Before submitting — checklist

- [ ] `docs/showcase-card.png` re-rendered if any count changed (`python scripts/generate_showcase_card.py`, then the Chromium command in its docstring).
- [ ] Repository social preview set to the same card.
- [ ] `README.md` counts match `portfolio.json` (`python scripts/generate_readme.py --check`).
- [ ] No active server row points at an archived repository (the same check enforces this).
- [ ] Every active server repository carries the `swiss-public-data-mcp` topic.
- [ ] Short description still under 400 characters after any count change.
- [ ] The independence disclaimer is visible near the top of the README.

## Keeping this file honest

The server count appears three times here (title block, EN description, DE
description). It is **not** generated, because the descriptions are hand-tuned to
the 400-character limit. When the inventory changes, update the three numbers and
re-count the descriptions:

```bash
python - <<'EOF'
import json, pathlib, re
n = len([s for s in json.load(open('portfolio.json'))['servers'] if s['scope'] != 'legacy'])
text = pathlib.Path('docs/SHOWCASE.md').read_text()
print('active servers in portfolio.json:', n)
print('counts mentioned in SHOWCASE.md :', sorted(set(re.findall(r'\b(\d{2})\b', text))))
for block in re.findall(r'```\n([^`]+)\n```', text)[:2]:
    print(len(block.replace('\n', ' ')), 'chars —', block.split('\n')[0][:50], '...')
EOF
```
