#!/usr/bin/env python3
"""Generate the data-driven README sections from portfolio.json.

`portfolio.json` is the single source of truth for the server inventory. This
script regenerates the two drift-prone, data-driven regions in both READMEs:

  * the **Server Portfolio** tables, and
  * the **Repository Map** tree.

Each region in the README is delimited by HTML comment markers:

    <!-- BEGIN GENERATED: <name> -->
    ...generated content...
    <!-- END GENERATED: <name> -->

Usage:
    python scripts/generate_readme.py           # rewrite README.md / README.de.md
    python scripts/generate_readme.py --check    # exit 1 if anything is out of date

The --check mode is run in CI so a stale README (e.g. after a repo rename) fails
the build instead of silently drifting.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PORTFOLIO = ROOT / "portfolio.json"

LANGS = {
    "en": {
        "readme": ROOT / "README.md",
        "label_key": "label",
        "desc_key": "description",
        "query_key": "anchor_query",
        "legend": (
            "**Status legend:** ✅ Production ready and audited at least once · "
            "🔐 Requires API credentials · 🧭 Adjacent/context source · "
            "🗄️ Legacy or superseded"
        ),
        "table_header": "| Server | Description | Anchor query | Status | Audit |",
        "legacy_header": "| Server | Current treatment | Reason |",
        "legacy_treatment_key": "legacy_treatment",
        "legacy_reason_key": "legacy_reason",
        "map_index": "← this index",
        "map_audit": "← audit methodology, not a server",
    },
    "de": {
        "readme": ROOT / "README.de.md",
        "label_key": "label_de",
        "desc_key": "description_de",
        "query_key": "anchor_query_de",
        "legend": (
            "**Status-Legende:** ✅ Production ready und mindestens einmal auditiert · "
            "🔐 API-Credentials nötig · 🧭 angrenzende Kontextquelle · "
            "🗄️ Legacy oder abgelöst"
        ),
        "table_header": "| Server | Beschreibung | Anchor Query | Status | Audit |",
        "legacy_header": "| Server | Behandlung | Grund |",
        "legacy_treatment_key": "legacy_treatment_de",
        "legacy_reason_key": "legacy_reason_de",
        "map_index": "← dieser Index",
        "map_audit": "← Auditmethodik, kein Server",
    },
}

TABLE_SEP = "|---|---|---|---|---|"
LEGACY_SEP = "|---|---|---|"
LEGACY_LABEL = "Legacy / Superseded"  # canonical category id used in server records


def load() -> dict:
    return json.loads(PORTFOLIO.read_text(encoding="utf-8"))


def repo_basename(url: str) -> str:
    return url.rstrip("/").rsplit("/", 1)[-1]


def audit_label(url: str) -> str:
    """Trailing path after /tree/<branch>/ , e.g. 'audits/' or 'docs/audit/'."""
    after = url.split("/tree/", 1)[1]
    path = after.split("/", 1)[1]
    return path + "/"


def status_icons(server: dict) -> str:
    icons = "✅"
    if server.get("requires_credentials"):
        icons += " 🔐"
    if server.get("scope") == "adjacent-context":
        icons += " 🧭"
    return icons


def servers_in(data: dict, category_label: str) -> list[dict]:
    return [s for s in data["servers"] if s["category"] == category_label]


def build_server_portfolio(data: dict, lang: dict) -> str:
    out: list[str] = [lang["legend"], ""]
    for cat in data["display_categories"]:
        label = cat[lang["label_key"]]
        out.append(f"### {cat['emoji']} {label}")
        out.append("")
        if cat["label"] == LEGACY_LABEL:
            out.append(lang["legacy_header"])
            out.append(LEGACY_SEP)
            for s in servers_in(data, cat["label"]):
                out.append(
                    f"| [{s['display_name']}]({s['repository']}) "
                    f"| {s[lang['legacy_treatment_key']]} "
                    f"| {s[lang['legacy_reason_key']]} |"
                )
        else:
            out.append(lang["table_header"])
            out.append(TABLE_SEP)
            for s in servers_in(data, cat["label"]):
                out.append(
                    f"| [{s['display_name']}]({s['repository']}) "
                    f"| {s[lang['desc_key']]} "
                    f"| *\"{s[lang['query_key']]}\"* "
                    f"| {status_icons(s)} "
                    f"| [{audit_label(s['audit_evidence'])}]({s['audit_evidence']}) |"
                )
        out.append("")
    return "\n".join(out).rstrip("\n")


def build_repository_map(data: dict, lang: dict) -> str:
    lines = ["```text", "malkreide/"]
    lines.append(f"├── swiss-public-data-mcp                 {lang['map_index']}")
    lines.append(f"├── mcp-audit-skill                       {lang['map_audit']}")
    cats = data["display_categories"]
    for i, cat in enumerate(cats):
        last_cat = i == len(cats) - 1
        branch = "└──" if last_cat else "├──"
        child_prefix = "    " if last_cat else "│   "
        lines.append("│")
        lines.append(f"{branch} {cat[lang['label_key']]}")
        repos = [repo_basename(s["repository"]) for s in servers_in(data, cat["label"])]
        for j, repo in enumerate(repos):
            connector = "└──" if j == len(repos) - 1 else "├──"
            lines.append(f"{child_prefix}{connector} {repo}")
    lines.append("```")
    return "\n".join(lines)


def replace_region(text: str, name: str, new_inner: str) -> str:
    begin = f"<!-- BEGIN GENERATED: {name} -->"
    end = f"<!-- END GENERATED: {name} -->"
    pattern = re.compile(re.escape(begin) + r"\n.*?\n" + re.escape(end), re.DOTALL)
    if not pattern.search(text):
        raise SystemExit(f"ERROR: markers for '{name}' not found in README")
    return pattern.sub(lambda _m: f"{begin}\n{new_inner}\n{end}", text, count=1)


def validate_counts(data: dict) -> None:
    active = [s for s in data["servers"] if s["scope"] != "legacy"]
    legacy = [s for s in data["servers"] if s["scope"] == "legacy"]
    c = data["counts"]
    problems = []
    if c["active_servers"] != len(active):
        problems.append(f"active_servers {c['active_servers']} != {len(active)}")
    if c["legacy_servers"] != len(legacy):
        problems.append(f"legacy_servers {c['legacy_servers']} != {len(legacy)}")
    if c["production_ready_active_servers"] != len(active):
        problems.append(
            f"production_ready_active_servers {c['production_ready_active_servers']} != {len(active)}"
        )
    if c["audited_mcp_server_repos"] != len(active) + len(legacy):
        problems.append(
            f"audited_mcp_server_repos {c['audited_mcp_server_repos']} != {len(active) + len(legacy)}"
        )
    for s in active:
        if s["status"] != "production_ready" or s["audit"] != "published":
            problems.append(f"{s['id']} is not production_ready/published")
    if problems:
        raise SystemExit("ERROR: portfolio.json count validation failed:\n  " + "\n  ".join(problems))


def render(data: dict, lang: dict) -> str:
    text = lang["readme"].read_text(encoding="utf-8")
    text = replace_region(text, "server-portfolio", build_server_portfolio(data, lang))
    text = replace_region(text, "repository-map", build_repository_map(data, lang))
    return text


def main() -> int:
    check = "--check" in sys.argv[1:]
    data = load()
    validate_counts(data)
    stale = []
    for code, lang in LANGS.items():
        current = lang["readme"].read_text(encoding="utf-8")
        rendered = render(data, lang)
        if current != rendered:
            if check:
                stale.append(lang["readme"].name)
            else:
                lang["readme"].write_text(rendered, encoding="utf-8")
                print(f"updated {lang['readme'].name}")
    if check and stale:
        print(
            "ERROR: README is out of sync with portfolio.json: "
            + ", ".join(stale)
            + "\nRun: python scripts/generate_readme.py",
            file=sys.stderr,
        )
        return 1
    if not check:
        print("done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
