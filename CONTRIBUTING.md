# Contributing

Thanks for your interest in this portfolio. This repository
(`swiss-public-data-mcp`) is the **index** for a family of Model Context
Protocol (MCP) servers that connect AI agents to Swiss public and open data.
It contains documentation and the machine-readable inventory
[`portfolio.json`](portfolio.json) — it does **not** contain server runtime code.

> Reminder: this is a private open-source project by Hayal Oezkan. It is **not**
> an official project of any public institution. Contributing here does not
> imply any affiliation.

## Where does my contribution belong?

| Your contribution | Right place |
|---|---|
| Bug, feature request, or fix for a specific MCP server | The **individual server repository** under [`github.com/malkreide`](https://github.com/malkreide) |
| Security report | See [`SECURITY.md`](SECURITY.md) — please use private reporting |
| Listing a new server, fixing inventory data, docs in this repo | **This repository** (read on) |

## Reporting issues for the index repo

Open a GitHub issue with a clear title and:

- what you expected vs. what you found (a broken link, an outdated entry, a
  count that no longer matches, …),
- the affected file (`README.md`, `README.de.md`, `portfolio.json`), and
- for a new server proposal, the details below.

## Proposing a new server for the inventory

Servers in the portfolio meet a few baseline expectations:

1. **Public / open data.** Core servers wrap a Swiss public-data source or a
   coherent source family. Sources that are useful for context but not Swiss
   government data (e.g. international or technology-signal sources) are listed
   as **adjacent** (`scope: "adjacent-context"`, shown with 🧭).
2. **Audit gate.** Production-ready status requires **at least one completed
   audit** using the public
   [`mcp-audit-skill`](https://github.com/malkreide/mcp-audit-skill), with the
   audit evidence published in the server repo (`audits/`, `audit/`, or
   `docs/audit/`).
3. **Discoverability.** The server repo carries the GitHub topic
   [`swiss-public-data-mcp`](https://github.com/topics/swiss-public-data-mcp).
4. **Conventions.** Bilingual `README.md` / `README.de.md`, and ideally the
   shared stack (FastMCP, Pydantic v2, httpx, `src/` layout, pytest with
   `@pytest.mark.live`, CI for Python 3.11–3.13). See *Architecture Principles*
   in the README.

To propose a listing, open an issue with: a short description, the repository
link, data-source notes, the intended scope (`core` / `adjacent-context`), and
the audit profile (transport, auth model, data class, write access).

## Editing the inventory (`portfolio.json` is the source of truth)

The **Server Portfolio** tables and the **Repository Map** in both READMEs are
**generated** from `portfolio.json`. Do **not** hand-edit anything between the
`<!-- BEGIN GENERATED: … -->` and `<!-- END GENERATED: … -->` markers.

Instead:

1. Edit [`portfolio.json`](portfolio.json). A server entry uses:

   ```json
   {
     "id": "example-mcp",
     "display_name": "example-mcp",
     "repository": "https://github.com/malkreide/example-mcp",
     "category": "Statistics & Geodata",
     "scope": "core",
     "status": "production_ready",
     "audit": "published",
     "audit_evidence": "https://github.com/malkreide/example-mcp/tree/main/audits",
     "description": "English one-line description",
     "anchor_query": "A representative English example question?",
     "description_de": "Deutsche Einzeiler-Beschreibung",
     "anchor_query_de": "Eine repräsentative deutsche Beispielfrage?",
     "requires_credentials": false
   }
   ```

   - `category` must match a `label` in the top-level `display_categories`.
   - `requires_credentials: true` renders the 🔐 icon; `scope: "adjacent-context"`
     renders 🧭; status/audit icons are derived automatically.
   - The audit-link label (`audits/`, `audit/`, `docs/audit/`) and the `main` vs
     `master` branch are derived from `audit_evidence` — use the real URL.

2. Regenerate the READMEs:

   ```bash
   python scripts/generate_readme.py
   ```

3. Verify they are in sync (this is what CI runs):

   ```bash
   python scripts/generate_readme.py --check
   ```

The [`readme-sync`](.github/workflows/readme-sync.yml) workflow runs `--check`
on every pull request and **fails if the READMEs drift** from `portfolio.json`.

## Pull requests

- Keep PRs focused; describe the *why*, not just the *what*.
- Run `python scripts/generate_readme.py --check` before pushing.
- Update **both** `README.md` and `README.de.md` for any prose change so the
  bilingual versions stay aligned.
- By contributing, you agree your contribution is licensed under the project's
  [MIT License](LICENSE).

---

## Mitwirken (Deutsch)

Dieses Repository ist der **Index** für eine Familie von MCP-Servern, die
KI-Agenten mit Schweizer öffentlichen und offenen Daten verbinden. Es enthält
Dokumentation und das maschinenlesbare Inventar
[`portfolio.json`](portfolio.json) — **keinen** Server-Laufzeitcode.

**Wohin gehört mein Beitrag?** Bugs/Features zu einem bestimmten Server gehören
in dessen eigenes Repository unter
[`github.com/malkreide`](https://github.com/malkreide). Sicherheitsmeldungen via
[`SECURITY.md`](SECURITY.md) (privat). Inventar- und Doku-Änderungen in dieses Repo.

**Neuen Server vorschlagen:** Issue mit Beschreibung, Repo-Link, Datenquellen,
Scope (`core` / `adjacent-context`) und Auditprofil eröffnen. Voraussetzungen:
öffentliche/offene Daten, mindestens **ein abgeschlossenes Audit** mit dem
[`mcp-audit-skill`](https://github.com/malkreide/mcp-audit-skill) und
veröffentlichter Audit-Evidence, GitHub-Topic
[`swiss-public-data-mcp`](https://github.com/topics/swiss-public-data-mcp) sowie
zweisprachige READMEs.

**Inventar bearbeiten:** `portfolio.json` ist die Quelle der Wahrheit. Die
Server-Portfolio-Tabellen und die Repository-Map werden daraus generiert —
**nichts** zwischen den `<!-- BEGIN/END GENERATED -->`-Markern von Hand
bearbeiten. Stattdessen `portfolio.json` ändern, dann:

```bash
python scripts/generate_readme.py          # READMEs neu generieren
python scripts/generate_readme.py --check   # Synchronität prüfen (wie in CI)
```

Der CI-Workflow [`readme-sync`](.github/workflows/readme-sync.yml) lässt PRs
**fehlschlagen**, wenn die READMEs vom Inventar abweichen.

**Pull Requests:** fokussiert halten, das *Warum* beschreiben, vor dem Push
`--check` laufen lassen, Prosa immer in `README.md` **und** `README.de.md`
pflegen. Mit dem Beitrag stimmst du der [MIT-Lizenz](LICENSE) zu.
