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

A second render, [`docs/social-preview.png`](social-preview.png), exists at
1280×640 for **Settings → Social preview**. GitHub renders social previews at a
strict 2:1 and letterboxes anything else, so upload that file there rather than
the 1200×630 one. Setting it means links to the repository — in chat, on
socials, in the showcase listing — render the same card.

Uploading a social preview is a web-UI action; GitHub exposes no API for it.

---

## 2. Datasets used

The form autocompletes against real `opendata.swiss` datasets. The mapping below
was **verified against the CKAN API** (`package_search` filtered by
`organization:`), not guessed from server descriptions.

An important distinction: opendata.swiss is a *metadata catalogue*. These servers
call the publishers' APIs directly rather than going through opendata.swiss, so
the entries below are the catalogue records **for the sources each server reads**
— that is what the form is asking for. Where a publisher runs several hundred
datasets, one representative record is named.

### Publishers present on opendata.swiss (26 servers)

| Server | Publisher (datasets) | Representative dataset |
|---|---|---|
| `swiss-statistics-mcp` | Bundesamt für Statistik BFS (3292) | [Nationalratswahlen 2023: Panaschierstatistik](https://opendata.swiss/de/dataset/nationalratswahlen-2023-panaschierstatistik-parteien-nach-gemeinden) |
| `swiss-housing-mcp` | BFS | [Wohnungen und Gebäude nach Bauperiode](https://opendata.swiss/de/dataset/wohnungen-und-gebaude-nach-bauperiode2) |
| `swiss-democracy-mcp` | BFS | [Eidgenössische Abstimmungsresultate](https://opendata.swiss/de/dataset/eidgenossische-abstimmungsresultate) |
| `zurich-opendata-mcp` | Stadt Zürich (687) | [Täglich aktualisierte Luftqualitätsmessungen, seit 1983](https://opendata.swiss/de/dataset/taglich-aktualisierte-luftqualitatsmessungen-seit-1983) |
| `zh-education-mcp` | Bildungsstatistik Kanton Zürich (11) | [Übersicht über alle Lernenden im Kanton Zürich ab 2000](https://opendata.swiss/de/dataset/ubersicht-uber-alle-lernenden-im-kanton-zurich) |
| `swiss-environment-mcp` | Bundesamt für Umwelt BAFU (361) | [NABEL: Stationen](https://opendata.swiss/de/dataset/nationales-beobachtungsnetz-fur-luftfremdstoffe-nabel-stationen) |
| `wsl-envidat-mcp` | EnviDat / WSL (585) | [Mountain Permafrost Hydrology](https://opendata.swiss/de/dataset/mountain-permafrost-hydrology) |
| `meteoswiss-mcp` | MeteoSchweiz (53) | [Totalisator-Niederschlagsstationen – Messwerte](https://opendata.swiss/de/dataset/totalisator-niederschlagsstationen-messwerte) |
| `swiss-energy-mcp` | Bundesamt für Energie BFE (147) | [Statistik der Wasserkraftanlagen (WASTA)](https://opendata.swiss/de/dataset/statistik-der-wasserkraftanlagen-wasta) |
| `swiss-electricity-mcp` | BFE | [Elektrizitätsproduktionsanlagen](https://opendata.swiss/de/dataset/elektrizitatsproduktionsanlagen) |
| `bakom-mcp` | BAKOM (120) | [Abdeckungsgrad der Gebäude mit Breitbanddiensten](https://opendata.swiss/de/dataset/abdeckungsgrad-der-gebaude-mit-breitbanddiensten-nach-gemeinde) |
| `bag-health-mcp` | Bundesamt für Gesundheit BAG (49) | [COVID-19 Schweiz](https://opendata.swiss/de/dataset/covid-19-schweiz) |
| `swiss-food-safety-mcp` | BLV (29) | [Lebensmittelkontrolle](https://opendata.swiss/de/dataset/lebensmittelkontrolle) |
| `swisstopo-mcp` | swisstopo (187) | [swissALTI3D](https://opendata.swiss/de/dataset/swissalti3d) |
| `lindas-mcp` | swisstopo | [Linked Data Dienst BGDI](https://opendata.swiss/de/dataset/sparql-endpoint-bgdi) |
| `sbb-opendata-mcp` | SBB (74) | [Ein- und Aussteigende an Bahnhöfen](https://opendata.swiss/de/dataset/passagierfrequenz1) |
| `swiss-transport-mcp` | Open Data ÖV Schweiz (65) · BAV (25) | [Fahrplan 2026 (NeTEx)](https://opendata.swiss/de/dataset/timetablenetex_2026) · [Haltestellen des öffentlichen Verkehrs](https://opendata.swiss/de/dataset/haltestellen-des-offentlichen-verkehrs) |
| `swiss-road-mobility-mcp` | ASTRA (26) | [Strassenverkehrszählung – übergeordnetes Netz](https://opendata.swiss/de/dataset/strassenverkehrszahlung-ubergeordnetes-netz) |
| `swiss-culture-mcp` | Bundesamt für Kultur BAK (5) | [ISOS – Bundesinventar der schützenswerten Ortsbilder](https://opendata.swiss/de/dataset/isos-bundesinventar-der-schutzenswerten-ortsbilder-der-schweiz-von-nationaler-bedeutung) |
| `swiss-cultural-heritage-mcp` | Schweizerisches Nationalmuseum (10) | [Sammlung «Keramik & Glas»](https://opendata.swiss/de/dataset/reprasentative-auswahl-aus-der-sammlung-keramik-glas-des-schweizerischen-nationalmuseums) |
| `swiss-academic-libraries-mcp` | Schweizerische Nationalbibliothek (13) | [Bildersammlung Annemarie Schwarzenbach](https://opendata.swiss/de/dataset/bildersammlung-annemarie-schwarzenbach1) |
| `eth-library-mcp` | ETH-Bibliothek (14) | [Fotos der Documenta Natura (1987–2010)](https://opendata.swiss/de/dataset/fotos-der-documenta-natura-1987-2010) |
| `swiss-procurement-mcp` | Beschaffungskonferenz des Bundes BKB (4) | [Beschaffungen ab 50 000 Franken der zentralen Bundesverwaltung 2024](https://opendata.swiss/de/dataset/beschaffungen-ab-50-000-franken-der-zentralen-bundesverwaltung-20241) |
| `swiss-efv-mcp` | Eidg. Finanzverwaltung EFV (7) | [Bundesfinanzen – Institutionen](https://opendata.swiss/de/dataset/bundesfinanzen-institutionen) |
| `parlament-mcp` | Parlamentsdienste (1) | [Webservices ws-old.parlament.ch](https://opendata.swiss/de/dataset/webservices-httpws-old-parlament-ch) |
| `srgssr-mcp` | SRG SSR (1) | [Polis API](https://opendata.swiss/de/dataset/polis-api) |

### Sources not catalogued on opendata.swiss (16 servers)

These read APIs that have no publisher entry in the catalogue. Do not invent
dataset links for them — say so in the description instead, since "42 servers,
26 catalogued publishers" is a more credible claim than a padded dataset list.

| Server | Source | Why it is absent |
|---|---|---|
| `fedlex-mcp` | Fedlex SPARQL | No Federal Office of Justice / Fedlex publisher on opendata.swiss |
| `openlex-mcp` | ZH-Lex | Cantonal law collection, not catalogued |
| `swiss-courts-mcp` | entscheidsuche.ch | No court publisher on opendata.swiss |
| `register-mcp` | Zefix (federal) | Only cantonal Zefix extracts are catalogued, not the federal API |
| `amtsblatt-mcp` | amtsblattportal.ch | SHAB itself is not catalogued |
| `swiss-ip-mcp` | IGE/IPI Swissreg | No IGE/IPI publisher |
| `termdat-mcp` | TERMDAT | No Federal Chancellery publisher |
| `i14y-mcp` | I14Y | The interoperability platform is a peer catalogue, not a dataset |
| `swiss-snb-mcp` | SNB data portal | No SNB publisher |
| `seco-labor-mcp` | SECO / AMSTAT | No SECO publisher (unemployment datasets found are cantonal) |
| `bag-epl-mcp` | Spezialitätenliste | Not published as open data |
| `swiss-holidays-mcp` | openholidaysapi.org | International, community-run |
| `global-education-mcp` | UNESCO UIS / OECD | International |
| `lobbywatch-mcp` | Lobbywatch.ch | NGO, not a public body |
| `hn-tech-signal-mcp` | Hacker News | Not Swiss public data (adjacent context server) |
| `news-monitor-mcp` | Public-media RSS | Feeds, not catalogued datasets |

### Recommended selection for the form

Twelve entries that cover the breadth and match the anchor queries in the README:

```
swissALTI3D
Statistik der Wasserkraftanlagen (WASTA)
Abdeckungsgrad der Gebäude mit Breitbanddiensten nach Gemeinde
Täglich aktualisierte Luftqualitätsmessungen, seit 1983
Übersicht über alle Lernenden im Kanton Zürich ab 2000
Eidgenössische Abstimmungsresultate
Ein- und Aussteigende an Bahnhöfen
Fahrplan 2026 (NeTEx)
Nationales Beobachtungsnetz für Luftfremdstoffe NABEL: Stationen
ISOS - Bundesinventar der schützenswerten Ortsbilder
Lebensmittelkontrolle
Polis API
```

> Verified against the opendata.swiss CKAN API. Dataset slugs can change when a
> publisher re-harvests; re-check any link that 404s before submitting.

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

- [ ] Card bitmaps re-rendered if any count changed (`python scripts/generate_showcase_card.py && node scripts/render_showcase_images.mjs`).
- [ ] Repository social preview set from `docs/social-preview.png` (Settings → Social preview).
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
