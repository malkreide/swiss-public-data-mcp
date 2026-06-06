#!/usr/bin/env python3
"""Generate official MCP Registry ``server.json`` drafts from portfolio.json.

``portfolio.json`` is the single source of truth for the server inventory. This
script derives one ``server.json`` per active portfolio server, ready to publish
to the official MCP Registry (https://registry.modelcontextprotocol.io). The
files are written under:

    registry/<server-id>/server.json

Each file follows the MCP Registry schema and uses:

  * the reverse-DNS namespace ``io.github.malkreide/<server-id>`` (validated for
    free via GitHub OAuth when publishing -- no custom-domain DNS record needed),
  * a ``pypi`` package launched with the ``uvx`` runtime hint, and
  * the English ``description`` and ``repository`` from portfolio.json.

These are *drafts*: two per-server values cannot be derived from portfolio.json
and MUST be reconciled against each server's own repository before publishing:

  * ``packages[0].version`` -- must match the actually published PyPI version,
  * the PyPI ``identifier`` -- assumed equal to the server id; fix if it differs.

Credential servers declare their real environment variables under
``environment_variables`` in portfolio.json; those are emitted verbatim.

See ``registry/README.md`` for the full publishing workflow (mcp-publisher CLI,
namespace auth, and the ``mcp-name`` ownership-validation file each repo needs).

Usage:
    python scripts/generate_server_json.py           # (re)write registry/*/server.json
    python scripts/generate_server_json.py --check    # exit 1 if anything is out of date

The --check mode is run in CI so a stale draft (e.g. after a repo rename) fails
the build instead of silently drifting, mirroring scripts/generate_readme.py.
"""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PORTFOLIO = ROOT / "portfolio.json"
REGISTRY_DIR = ROOT / "registry"

# Registry schema and publishing conventions (see registry/README.md).
SCHEMA_URL = "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json"
NAMESPACE = "io.github.malkreide"
# Placeholder version. The MCP Registry requires this to match a published PyPI
# release; the per-repo publish step (and the mcp-name validation) is the gate
# that enforces it. Update before `mcp-publisher publish`.
DEFAULT_VERSION = "0.1.0"
PUBLISHER_META_KEY = "io.modelcontextprotocol.registry/publisher-provided"


def load() -> dict:
    return json.loads(PORTFOLIO.read_text(encoding="utf-8"))


def active_servers(data: dict) -> list[dict]:
    """Portfolio servers eligible for the registry (legacy servers excluded)."""
    return [s for s in data["servers"] if s.get("scope") != "legacy"]


def build_package(server: dict) -> dict:
    """A pypi + uvx package entry; declares the server's real credential vars."""
    package: dict = {
        "registryType": "pypi",
        # PyPI distribution name is assumed equal to the server id. Fix here (or
        # in portfolio.json) if a server publishes under a different name.
        "identifier": server["id"],
        "version": DEFAULT_VERSION,
        "transport": {"type": "stdio"},
        "runtimeHint": "uvx",
    }
    # Credential servers declare their actual variables in portfolio.json; the
    # registry entry reflects them verbatim (no guessed placeholders).
    env = server.get("environment_variables") or []
    if server.get("requires_credentials") and not env:
        raise SystemExit(
            f"ERROR: {server['id']} has requires_credentials but no "
            "environment_variables in portfolio.json"
        )
    if env:
        package["environmentVariables"] = [
            {
                "name": var["name"],
                "description": var["description"],
                "isRequired": var.get("isRequired", True),
                "isSecret": var.get("isSecret", True),
            }
            for var in env
        ]
    return package


def build_server_json(server: dict) -> dict:
    return {
        "$schema": SCHEMA_URL,
        "name": f"{NAMESPACE}/{server['id']}",
        "description": server["description"],
        "version": DEFAULT_VERSION,
        "repository": {
            "url": server["repository"],
            "source": "github",
        },
        "websiteUrl": server["repository"],
        "packages": [build_package(server)],
        "_meta": {
            PUBLISHER_META_KEY: {
                "category": server["category"],
                "scope": server["scope"],
            }
        },
    }


def serialize(obj: dict) -> str:
    """Stable 2-space JSON with a trailing newline (diff- and CI-friendly)."""
    return json.dumps(obj, indent=2, ensure_ascii=False) + "\n"


def target_path(server: dict) -> pathlib.Path:
    return REGISTRY_DIR / server["id"] / "server.json"


def expected_files(data: dict) -> dict[pathlib.Path, str]:
    return {target_path(s): serialize(build_server_json(s)) for s in active_servers(data)}


def existing_files() -> set[pathlib.Path]:
    return set(REGISTRY_DIR.glob("*/server.json"))


def main() -> int:
    check = "--check" in sys.argv[1:]
    data = load()
    expected = expected_files(data)

    stale: list[str] = []
    # Orphans: server.json files with no matching active server (e.g. a rename).
    orphans = sorted(existing_files() - set(expected))
    for path in orphans:
        rel = path.relative_to(ROOT)
        if check:
            stale.append(f"orphaned: {rel}")
        else:
            path.unlink()
            try:
                path.parent.rmdir()
            except OSError:
                pass
            print(f"removed {rel}")

    for path, content in sorted(expected.items()):
        rel = path.relative_to(ROOT)
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == content:
            continue
        if check:
            stale.append(f"stale: {rel}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            print(f"wrote {rel}")

    if check and stale:
        print(
            "ERROR: registry/*/server.json out of sync with portfolio.json:\n  "
            + "\n  ".join(stale)
            + "\nRun: python scripts/generate_server_json.py",
            file=sys.stderr,
        )
        return 1
    if not check:
        print(f"done ({len(expected)} servers)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
