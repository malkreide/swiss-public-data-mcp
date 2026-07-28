#!/usr/bin/env python3
"""Generate the data-driven regions of PROMOTION.md from portfolio.json.

PROMOTION.md used to hard-code the server count and the full awesome-list entry
block by hand, which silently drifted once the inventory grew (it still claimed
34 servers while portfolio.json listed 43). The counts, the collection entry, the
per-server entries and the PR text are now generated, so the same CI drift check
that guards the READMEs guards this file too.

Region markers mirror scripts/generate_readme.py:

    <!-- BEGIN GENERATED: <name> -->
    ...generated content...
    <!-- END GENERATED: <name> -->

Usage:
    python scripts/generate_promotion.py           # rewrite PROMOTION.md
    python scripts/generate_promotion.py --check    # exit 1 if out of date
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PORTFOLIO = ROOT / "portfolio.json"
PROMOTION = ROOT / "PROMOTION.md"

# awesome-mcp-servers emoji legend: Python · local stdio service · cross-platform.
BADGES = "🐍 🏠 🍎 🪟 🐧"


def load() -> dict:
    return json.loads(PORTFOLIO.read_text(encoding="utf-8"))


def active_servers(data: dict) -> list[dict]:
    """Archived/legacy repositories are never promoted."""
    return [s for s in data["servers"] if s.get("scope") != "legacy"]


def build_intro(data: dict) -> str:
    n = len(active_servers(data))
    return (
        "How to broaden adoption of the portfolio's MCP servers beyond the official\n"
        f"registry. Generated context: **{n} active servers**, source of truth\n"
        "[`portfolio.json`](portfolio.json).\n"
        "\n"
        "## Status of the levers\n"
        "\n"
        "| Lever | Status |\n"
        "|---|---|\n"
        f"| Official **MCP Registry** (`registry.modelcontextprotocol.io`) | **Done** — all {n} servers published under `io.github.malkreide/*`. |\n"
        "| `modelcontextprotocol/servers` community list | **Retired** — that list was removed in favour of the MCP Registry, so there is nothing to submit there. |\n"
        "| `punkpeye/awesome-mcp-servers` (community awesome list) | **Open** — accepts PRs; see below. |\n"
        "| [`opendata.swiss` showcase](https://opendata.swiss/en/submit-showcase) | **Open** — submission text is prepared in [`docs/SHOWCASE.md`](docs/SHOWCASE.md). |\n"
        "| Third-party catalogues (Smithery, Glama, PulseMCP, MCP.so, …) | **Mostly automatic** — they ingest from the registry; a few accept manual submissions. |"
    )


def build_entries(data: dict) -> str:
    servers = active_servers(data)
    n = len(servers)
    lines = [
        "### Recommended: one collection entry (least spammy, high signal)",
        "",
        f"Rather than adding {n} lines from a single author, lead with one entry",
        "for the portfolio and slot it under the most fitting current category (e.g. a",
        "government / open-data section). Check the live README for the exact category",
        "names before submitting.",
        "",
        "```",
        f"- [malkreide/swiss-public-data-mcp](https://github.com/malkreide/swiss-public-data-mcp) {BADGES} - "
        f"Curated portfolio of {n} MCP servers for Swiss public & open data — transport, law, "
        "statistics, energy, environment, health, geodata, democracy and more.",
        "```",
        "",
        f"### Optional: all {n} individual entries",
        "",
        "If you prefer per-server visibility, distribute these into the matching topical",
        "categories (transport, finance, law, location, etc.). Paste only the ones you",
        f"want — avoid dumping all {n} into a single category.",
        "",
        "```",
    ]
    for s in servers:
        lines.append(
            f"- [malkreide/{s['id']}]({s['repository']}) {BADGES} - {s['description']}"
        )
    lines += [
        "```",
        "",
        "### PR text for the submission",
        "",
        "**Title:**",
        "",
        "```",
        f"Add swiss-public-data-mcp: curated portfolio of {n} Swiss open-data MCP servers",
        "```",
        "",
        "**Body:**",
        "",
        "```",
        f"Adds a curated, audited portfolio of {n} MCP servers connecting AI agents to",
        "Swiss public and open data (opendata.swiss, GeoAdmin, Fedlex, BFS, SNB, SBB,",
        "MeteoSwiss, BAG, parliament, and more).",
        "",
        "- All servers are production-ready, audited, and published in the official MCP",
        "  Registry under the `io.github.malkreide/*` namespace.",
        "- Every server is a thin read-only client for an official public endpoint; no",
        "  data is mirrored or re-published.",
        "- Python / stdio / cross-platform; installable via uvx.",
        "- Single source of truth: https://github.com/malkreide/swiss-public-data-mcp/blob/main/portfolio.json",
        "",
        "I've added one collection entry to keep the list tidy; happy to split into",
        "per-category entries if you prefer.",
        "```",
    ]
    return "\n".join(lines)


def replace_region(text: str, name: str, new_inner: str) -> str:
    begin = f"<!-- BEGIN GENERATED: {name} -->"
    end = f"<!-- END GENERATED: {name} -->"
    pattern = re.compile(re.escape(begin) + r"\n.*?\n" + re.escape(end), re.DOTALL)
    if not pattern.search(text):
        raise SystemExit(f"ERROR: markers for '{name}' not found in PROMOTION.md")
    return pattern.sub(lambda _m: f"{begin}\n{new_inner}\n{end}", text, count=1)


def render(data: dict) -> str:
    text = PROMOTION.read_text(encoding="utf-8")
    text = replace_region(text, "promotion-intro", build_intro(data))
    text = replace_region(text, "awesome-entries", build_entries(data))
    return text


def main() -> int:
    check = "--check" in sys.argv[1:]
    data = load()
    current = PROMOTION.read_text(encoding="utf-8")
    rendered = render(data)
    if current == rendered:
        if not check:
            print("PROMOTION.md already up to date")
        return 0
    if check:
        print(
            "ERROR: PROMOTION.md is out of sync with portfolio.json\n"
            "Run: python scripts/generate_promotion.py",
            file=sys.stderr,
        )
        return 1
    PROMOTION.write_text(rendered, encoding="utf-8")
    print("updated PROMOTION.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
