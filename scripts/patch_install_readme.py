#!/usr/bin/env python3
"""Insert the client install snippet into each server repo's README, idempotently.

This is the automation for "copy each block from docs/INSTALL.md into the
server's own README". For every active portfolio server it inserts (or updates)
a managed ``## Installation`` section in that repo's ``README.md``, delimited by
HTML comment markers so re-runs replace the block in place:

    <!-- BEGIN GENERATED: install -->
    ...
    <!-- END GENERATED: install -->

The snippet content is built from ``portfolio.json`` (the single source of truth)
using the same ``uvx``/stdio config as ``scripts/generate_install_snippets.py``;
credential servers get an ``env`` block from their ``environment_variables``.

Safe by default: with no flags it does a **dry run** (prints the per-repo plan,
writes nothing). Pass ``--write`` to edit READMEs, ``--commit`` to also commit,
and ``--push`` to push.

Examples
--------
    python scripts/patch_install_readme.py --repos-dir ../repos             # dry run
    python scripts/patch_install_readme.py --repos-dir ../repos --clone --write
    python scripts/patch_install_readme.py --repos-dir ../repos --write --commit --push
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import subprocess
import sys

from generate_install_snippets import server_config  # same source of truth

ROOT = pathlib.Path(__file__).resolve().parent.parent
PORTFOLIO = ROOT / "portfolio.json"

BEGIN = "<!-- BEGIN GENERATED: install -->"
END = "<!-- END GENERATED: install -->"
REGION = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.DOTALL)
COMMIT_MSG = "Add client install snippet to README"

# Outcome states.
ADDED = "INSTALL_ADDED"
UPDATED = "INSTALL_UPDATED"
OK = "INSTALL_OK"
NO_README = "NO_README"
NO_REPO = "NO_REPO"


def load() -> dict:
    return json.loads(PORTFOLIO.read_text(encoding="utf-8"))


def active_servers(data: dict) -> list[dict]:
    return [s for s in data["servers"] if s.get("scope") != "legacy"]


def install_block(server: dict) -> str:
    """The managed block, markers included, deterministic for idempotency."""
    cfg = json.dumps(server_config(server), indent=2, ensure_ascii=False)
    inner = [
        "## Installation",
        "",
        "Run via [`uv`](https://docs.astral.sh/uv/)'s `uvx` — no clone or manual "
        "install needed. Add to your MCP client config (`mcpServers` for Claude "
        "Desktop, Cursor and Windsurf; use a top-level `servers` key for VS Code "
        "in `.vscode/mcp.json`):",
        "",
        "```json",
        cfg,
        "```",
    ]
    if server.get("environment_variables"):
        names = ", ".join(f"`{v['name']}`" for v in server["environment_variables"])
        inner += ["", f"Requires credentials: set {names} (replace the placeholder values above)."]
    return BEGIN + "\n" + "\n".join(inner) + "\n" + END


def apply_block(text: str, block: str) -> tuple[str, str]:
    """Insert or update the managed block; return (new_text, state)."""
    if REGION.search(text):
        new = REGION.sub(lambda _m: block, text, count=1)
        return new, (OK if new == text else UPDATED)
    sep = "" if text.endswith("\n") else "\n"
    return f"{text}{sep}\n{block}\n", ADDED


def find_readme(repo_dir: pathlib.Path) -> pathlib.Path | None:
    primary = repo_dir / "README.md"
    if primary.exists():
        return primary
    for cand in sorted(repo_dir.glob("README*")):
        return cand
    return None


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

    servers = active_servers(load())
    if args.only:
        wanted = set(args.only)
        servers = [s for s in servers if s["id"] in wanted]
        missing = wanted - {s["id"] for s in servers}
        if missing:
            print(f"ERROR: unknown server id(s): {', '.join(sorted(missing))}", file=sys.stderr)
            return 2

    rows: list[tuple[str, str]] = []
    changed = 0

    for server in servers:
        sid = server["id"]
        print(f"\n== {sid}")
        repo_dir = (args.repos_dir / sid).resolve()
        if not ensure_repo(repo_dir, server["repository"], args.clone):
            rows.append((sid, NO_REPO))
            print(f"  repo not found: {repo_dir} (use --clone)")
            continue
        readme = find_readme(repo_dir)
        if readme is None:
            rows.append((sid, NO_README))
            print("  no README found")
            continue

        text = readme.read_text(encoding="utf-8")
        new_text, state = apply_block(text, install_block(server))
        print(f"  {state}")
        if state == OK:
            rows.append((sid, OK))
            continue
        if not args.write:
            rows.append((sid, state + " (dry-run)"))
            continue

        readme.write_text(new_text, encoding="utf-8")
        changed += 1
        if args.commit:
            git(repo_dir, "add", "-A")
            if git(repo_dir, "commit", "-m", COMMIT_MSG) == 0:
                print("  committed")
                if args.push and git(repo_dir, "push") == 0:
                    print("  pushed")
        rows.append((sid, state))

    # Summary.
    print("\n" + "=" * 56)
    print(f"{'SERVER':<32} STATE")
    print("-" * 56)
    for sid, state in rows:
        print(f"{sid:<32} {state}")
    print("-" * 56)
    if args.write:
        print(f"changed {changed} README(s)"
              + (" and committed" if args.commit else "")
              + (" and pushed" if args.push else ""))
    else:
        actionable = sum(1 for _, s in rows if s.endswith("(dry-run)"))
        print(f"dry run: {actionable} README(s) would change. Re-run with --write to apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
