#!/usr/bin/env python3
"""Insert the MCP Registry ``mcp-name`` link into each server's pyproject.toml.

The official registry validates package ownership by requiring the PyPI package
to advertise its registry name. The convention is a project URL labelled
``mcp-name``:

    [project.urls]
    "mcp-name" = "io.github.malkreide/<server-id>"

``scripts/publish_registry.py`` reports every server as ``MISSING_MCP_NAME``
until this line exists *and* a fresh release is published. This script applies
that one edit across all server repos idempotently, so the only remaining manual
step is cutting the releases.

The registry name is taken from each committed draft in
``registry/<id>/server.json`` (the ``name`` field), keeping the namespace in
sync with the rest of the portfolio tooling.

Idempotent by design:
  * correct value already present -> skipped,
  * ``mcp-name`` present with a different value -> updated in place,
  * ``[project.urls]`` table exists but no ``mcp-name`` -> line inserted,
  * no ``[project.urls]`` table -> table appended.

Safe by default: with no flags it does a **dry run** (prints the per-repo plan,
writes nothing). Pass ``--write`` to edit files, ``--commit`` to also commit, and
``--push`` to push. Each edited file is re-parsed with tomllib before writing, so
a malformed result is never saved.

Examples
--------
    python scripts/patch_mcp_name.py --repos-dir ../repos             # dry run
    python scripts/patch_mcp_name.py --repos-dir ../repos --clone --write
    python scripts/patch_mcp_name.py --repos-dir ../repos --write --commit --push
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import subprocess
import sys
import tomllib

ROOT = pathlib.Path(__file__).resolve().parent.parent
REGISTRY_DIR = ROOT / "registry"

COMMIT_MSG = "Add mcp-name to pyproject.toml for MCP Registry ownership"
# A line like:  "mcp-name" = "..."  /  mcp-name = '...'  (any quoting, any indent).
MCP_NAME_LINE = re.compile(r"""^[ \t]*['"]?mcp-name['"]?[ \t]*=.*$""", re.MULTILINE)
# The [project.urls] header and the span up to the next top-level table / EOF.
URLS_SECTION = re.compile(
    r"^(?P<header>[ \t]*\[project\.urls\][ \t]*\r?\n)(?P<body>.*?)(?=^\[|\Z)",
    re.MULTILINE | re.DOTALL,
)

# Per-repo outcome states.
SKIP_OK = "ALREADY_SET"
UPDATED = "UPDATED"
INSERTED = "INSERTED"
APPENDED = "APPENDED_TABLE"
NO_PYPROJECT = "NO_PYPROJECT"
NO_REPO = "NO_REPO"
PARSE_ERROR = "PARSE_ERROR"


def load_drafts() -> list[tuple[str, str, str]]:
    """(server_id, registry name, repo url) for every committed registry draft."""
    out = []
    for path in sorted(REGISTRY_DIR.glob("*/server.json")):
        draft = json.loads(path.read_text(encoding="utf-8"))
        out.append((path.parent.name, draft["name"], draft["repository"]["url"]))
    return out


def current_mcp_name(text: str) -> str | None:
    """Existing project.urls.mcp-name value, or None if absent/unparseable."""
    try:
        data = tomllib.loads(text)
    except tomllib.TOMLDecodeError:
        return None
    return (data.get("project", {}).get("urls", {}) or {}).get("mcp-name")


def patch_text(text: str, name: str) -> tuple[str, str]:
    """Return (new_text, state) ensuring project.urls.mcp-name == name."""
    if current_mcp_name(text) == name:
        return text, SKIP_OK

    new_line = f'"mcp-name" = "{name}"'
    section = URLS_SECTION.search(text)

    if section:
        body = section.group("body")
        if MCP_NAME_LINE.search(body):
            new_body = MCP_NAME_LINE.sub(new_line, body, count=1)
            state = UPDATED
        else:
            # Insert right after the header, before the rest of the table.
            new_body = new_line + "\n" + body
            state = INSERTED
        start, end = section.span()
        new_text = text[:start] + section.group("header") + new_body + text[end:]
        return new_text, state

    # No [project.urls] table at all: append one (table order is irrelevant in TOML).
    sep = "" if text.endswith("\n") else "\n"
    new_text = f"{text}{sep}\n[project.urls]\n{new_line}\n"
    return new_text, APPENDED


def ensure_repo(repo_dir: pathlib.Path, url: str, clone: bool) -> bool:
    if repo_dir.exists():
        if clone:
            subprocess.run(["git", "-C", str(repo_dir), "pull", "--ff-only"], check=False)
        return True
    if not clone:
        return False
    repo_dir.parent.mkdir(parents=True, exist_ok=True)
    print(f"  cloning {url} -> {repo_dir}")
    return subprocess.run(["git", "clone", "--depth", "1", url, str(repo_dir)], check=False).returncode == 0


def git(repo_dir: pathlib.Path, *args: str) -> int:
    return subprocess.run(["git", "-C", str(repo_dir), *args], check=False).returncode


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--only", nargs="+", metavar="ID", help="restrict to these server ids")
    p.add_argument("--repos-dir", type=pathlib.Path, default=ROOT.parent,
                   help="directory containing server repos as <id>/ (default: parent of this repo)")
    p.add_argument("--clone", action="store_true", help="git clone missing repos (ff-pull existing)")
    p.add_argument("--write", action="store_true", help="write edits (default: dry run)")
    p.add_argument("--commit", action="store_true", help="git commit the edit in each repo (implies --write)")
    p.add_argument("--push", action="store_true", help="git push after committing (implies --commit)")
    return p.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.push:
        args.commit = True
    if args.commit:
        args.write = True

    drafts = load_drafts()
    if args.only:
        wanted = set(args.only)
        drafts = [row for row in drafts if row[0] in wanted]
        missing = wanted - {row[0] for row in drafts}
        if missing:
            print(f"ERROR: unknown server id(s): {', '.join(sorted(missing))}", file=sys.stderr)
            return 2

    rows: list[tuple[str, str, str]] = []  # (id, state, detail)
    changed = 0

    for sid, name, url in drafts:
        print(f"\n== {sid} ({name})")
        repo_dir = (args.repos_dir / sid).resolve()
        if not ensure_repo(repo_dir, url, args.clone):
            rows.append((sid, NO_REPO, f"{repo_dir} missing (use --clone)"))
            print(f"  repo not found: {repo_dir} (use --clone)")
            continue

        pyproject = repo_dir / "pyproject.toml"
        if not pyproject.exists():
            rows.append((sid, NO_PYPROJECT, str(pyproject)))
            print("  no pyproject.toml")
            continue

        text = pyproject.read_text(encoding="utf-8")
        new_text, state = patch_text(text, name)

        if state == SKIP_OK:
            rows.append((sid, SKIP_OK, name))
            print("  already set")
            continue

        # Guard: the edited file must still parse and carry the expected value.
        if current_mcp_name(new_text) != name:
            rows.append((sid, PARSE_ERROR, "edited file would not parse / value mismatch"))
            print("  ERROR: edit did not validate; left untouched")
            continue

        print(f"  {state}: \"mcp-name\" = \"{name}\"")
        if not args.write:
            rows.append((sid, state + " (dry-run)", name))
            continue

        pyproject.write_text(new_text, encoding="utf-8")
        changed += 1
        if args.commit:
            if git(repo_dir, "add", "pyproject.toml") == 0 and git(repo_dir, "commit", "-m", COMMIT_MSG) == 0:
                print("  committed")
                if args.push and git(repo_dir, "push") == 0:
                    print("  pushed")
        rows.append((sid, state, name))

    # Summary.
    print("\n" + "=" * 64)
    print(f"{'SERVER':<32} {'STATE':<22} DETAIL")
    print("-" * 64)
    for sid, state, detail in rows:
        print(f"{sid:<32} {state:<22} {detail}")
    print("-" * 64)
    if args.write:
        print(f"edited {changed} pyproject.toml file(s)"
              + (" and committed" if args.commit else "")
              + (" and pushed" if args.push else ""))
    else:
        actionable = sum(1 for _, s, _ in rows if s.endswith("(dry-run)"))
        print(f"dry run: {actionable} file(s) would change. Re-run with --write to apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
