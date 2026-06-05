# Security Policy

This repository (`swiss-public-data-mcp`) is the **portfolio index** for a family of
Model Context Protocol (MCP) servers that connect AI agents to Swiss public and open
data. It contains documentation and the machine-readable inventory
[`portfolio.json`](portfolio.json) — it does **not** ship runtime server code itself.
Each MCP server lives in its own repository under
[`github.com/malkreide`](https://github.com/malkreide) and is the place to report
issues affecting that server.

> Reminder: this is a private open-source project by Hayal Oezkan. It is **not** an
> official project of any public institution, and these servers expose **public, open
> data** only. Still, security is treated as a first-class concern across the portfolio.

## Scope

| In scope | Out of scope |
|---|---|
| Vulnerabilities in this index repo (e.g. malicious links, supply-chain risks in any tooling added here) | The availability or correctness of upstream public-data APIs (opendata.swiss, GeoAdmin, Fedlex, BFS, SNB, …) |
| Security weaknesses in a listed MCP server (report on **that server's** repository) | Feature requests and general bugs — use normal issues on the relevant repo |
| Exposure of secrets, tokens, or credentials in any portfolio repository | Findings that require a non-default, insecure client configuration |

Because the portfolio follows a **No-Auth-First** design, most core servers use only
open, unauthenticated endpoints and hold no user data or secrets. Servers that *do*
require API credentials (marked 🔐 in the README) never store credentials in the
repository; they read them from the client environment at runtime.

## Reporting a Vulnerability

**Please do not open a public issue for security-sensitive reports.**

1. **Preferred:** Use **GitHub Private Vulnerability Reporting** on the affected
   repository — the *Security* tab → *Report a vulnerability*. For a finding in this
   index repo, use it here:
   <https://github.com/malkreide/swiss-public-data-mcp/security/advisories/new>
2. **Alternative:** Open a minimal public issue that says only *"security report —
   please enable a private channel"* (no technical detail), and a private advisory
   will be opened to continue the conversation.

Please include, where possible:

- the affected repository and (if known) the audited commit / version,
- a description of the issue and its impact,
- reproduction steps or a proof of concept,
- any relevant client, transport (`stdio` / Streamable HTTP), and configuration details.

### What to expect

| Stage | Target |
|---|---|
| Acknowledgement of your report | within **5 working days** |
| Initial assessment / triage | within **10 working days** |
| Coordinated disclosure | after a fix is available, by mutual agreement |

This is a volunteer-run open-source project, so timelines are best-effort. Good-faith
research is welcome and appreciated; please act responsibly and avoid privacy
violations, data destruction, or service disruption while testing.

## How Security Is Handled Across the Portfolio

Security is part of the portfolio's audit methodology, documented in the public
[`mcp-audit-skill`](https://github.com/malkreide/mcp-audit-skill) repository
(**68 checks across eight categories**). Two categories are directly security- and
compliance-oriented:

- **`SEC`** — OAuth proxy risks, confused-deputy risks, SSRF, session hijacking,
  prompt-injection surface, and secret handling.
- **`CH`** — Swiss DSG / EDÖB and public-sector compliance considerations.

The audit skill is **not** a vulnerability scanner and **not** a compliance
certificate — it is a reproducible review method. Architecture and risk judgement
remain human. Published audit evidence is linked per server from the
[README](README.md).

---

## Sicherheitsrichtlinie (Deutsch)

Dieses Repository ist der **Portfolio-Index** für eine Familie von MCP-Servern, die
KI-Agenten mit Schweizer öffentlichen und offenen Daten verbinden. Es enthält
Dokumentation und das maschinenlesbare Inventar [`portfolio.json`](portfolio.json),
aber **keinen** Server-Laufzeitcode. Jeder MCP-Server liegt in einem eigenen
Repository unter [`github.com/malkreide`](https://github.com/malkreide); dort werden
serverspezifische Sicherheitsmeldungen entgegengenommen.

**Sicherheitslücken bitte nicht über öffentliche Issues melden.** Nutze stattdessen das
**GitHub Private Vulnerability Reporting** im betroffenen Repository (Reiter *Security*
→ *Report a vulnerability*), für diesen Index-Repo hier:
<https://github.com/malkreide/swiss-public-data-mcp/security/advisories/new>.
Alternativ ein minimales öffentliches Issue ohne technische Details mit der Bitte um
einen privaten Kanal eröffnen.

Bitte nach Möglichkeit angeben: betroffenes Repository und (falls bekannt) Commit/Version,
Beschreibung und Auswirkung, Reproduktionsschritte sowie relevante Client-, Transport-
und Konfigurationsdetails. Eingang wird innert **5 Arbeitstagen** bestätigt, eine erste
Einschätzung erfolgt innert **10 Arbeitstagen** (Best-Effort, freiwilliges Open-Source-Projekt).

Das Portfolio folgt einem **No-Auth-First**-Ansatz: Kernserver nutzen offene,
unauthentifizierte Endpunkte und speichern weder Nutzerdaten noch Secrets. Server mit
nötigen API-Credentials (im README mit 🔐 markiert) lesen diese zur Laufzeit aus der
Client-Umgebung und legen sie nie im Repository ab. Sicherheit ist Teil der
Audit-Methodik im öffentlichen
[`mcp-audit-skill`](https://github.com/malkreide/mcp-audit-skill) — insbesondere die
Kategorien **`SEC`** (u. a. SSRF, Prompt-Injection-Flächen, Secret-Handling) und
**`CH`** (Schweizer DSG / EDÖB).
