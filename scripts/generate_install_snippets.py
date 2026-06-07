#!/usr/bin/env python3
"""Generate copy-paste MCP client install snippets from portfolio.json.

For each active portfolio server this writes a section to ``docs/INSTALL.md`` with
a ready-to-paste client configuration. The servers are PyPI packages launched via
``uvx`` over stdio, so a single ``mcpServers`` JSON block works for Claude
Desktop, Cursor and Windsurf; VS Code uses the same block under a ``servers`` key.
Credential servers get an ``env`` block populated from their
``environment_variables`` in portfolio.json.

The intended use is to copy each server's block into that server's own README
(promotion lever: lower the install friction for registry/catalogue visitors).

``portfolio.json`` is the single source of truth.

Usage:
    python scripts/generate_install_snippets.py           # (re)write docs/INSTALL.md
    python scripts/generate_install_snippets.py --check    # exit 1 if out of date

The --check mode runs in CI so the snippets cannot drift from portfolio.json,
mirroring scripts/generate_server_json.py.
"""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PORTFOLIO = ROOT / "portfolio.json"
OUT = ROOT / "docs" / "INSTALL.md"

HEADER = """\
# Client install snippets

Copy-paste configuration for adding these servers to common MCP clients. Each
server is a PyPI package run via [`uv`](https://docs.astral.sh/uv/)'s `uvx` over
stdio — no clone or manual install needed.

> Generated from [`portfolio.json`](../portfolio.json) by
> `scripts/generate_install_snippets.py`. Do not edit by hand. The intended use
> is to copy a server's block into that server's own README.

## Where the config lives

| Client | Config file | Top-level key |
|---|---|---|
| Claude Desktop | `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) · `%APPDATA%\\Claude\\claude_desktop_config.json` (Windows) | `mcpServers` |
| Cursor | `~/.cursor/mcp.json` (global) or `.cursor/mcp.json` (project) | `mcpServers` |
| Windsurf | `~/.codeium/windsurf/mcp_config.json` | `mcpServers` |
| VS Code | `.vscode/mcp.json` (workspace) | `servers` |

The JSON blocks below use `mcpServers` (Claude Desktop / Cursor / Windsurf). For
**VS Code**, use the identical inner object under a top-level `servers` key
instead of `mcpServers`.
"""


def load() -> dict:
    return json.loads(PORTFOLIO.read_text(encoding="utf-8"))


def active_servers(data: dict) -> list[dict]:
    return [s for s in data["servers"] if s.get("scope") != "legacy"]


def server_config(server: dict) -> dict:
    entry: dict = {"command": "uvx", "args": [server["id"]]}
    env = server.get("environment_variables") or []
    if env:
        entry["env"] = {var["name"]: f"<your {var['name']}>" for var in env}
    return {"mcpServers": {server["id"]: entry}}


def build_section(server: dict) -> str:
    block = json.dumps(server_config(server), indent=2, ensure_ascii=False)
    lines = [
        f"## {server['id']}",
        "",
        server["description"] + ".",
        "",
        "```json",
        block,
        "```",
    ]
    if server.get("environment_variables"):
        names = ", ".join(f"`{v['name']}`" for v in server["environment_variables"])
        lines += ["", f"Requires credentials: replace the placeholder values for {names}."]
    return "\n".join(lines)


def render(data: dict) -> str:
    sections = [build_section(s) for s in active_servers(data)]
    return HEADER + "\n" + "\n\n---\n\n".join(sections) + "\n"


def main() -> int:
    check = "--check" in sys.argv[1:]
    content = render(load())
    current = OUT.read_text(encoding="utf-8") if OUT.exists() else None
    if current == content:
        if not check:
            print("up to date")
        return 0
    if check:
        print(
            "ERROR: docs/INSTALL.md out of sync with portfolio.json.\n"
            "Run: python scripts/generate_install_snippets.py",
            file=sys.stderr,
        )
        return 1
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(content, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
