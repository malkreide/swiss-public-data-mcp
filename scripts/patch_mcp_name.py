#!/usr/bin/env python3
"""Declare each server's MCP Registry name for PyPI ownership validation.

The registry verifies PyPI package ownership by reading the package's README
(its long description on PyPI) and looking for a line:

    mcp-name: io.github.malkreide/<server-id>

PyPI does **not** accept this as a `[project.urls]` entry — values there must be
valid URLs, so an `mcp-name` URL makes `twine upload` fail with
``'io.github...' is not a valid url``. The marker therefore belongs in the
README, written here as an HTML comment so it does not clutter the rendered page:

    <!-- mcp-name: io.github.malkreide/<server-id> -->

This script does two things per server repo, idempotently:
  1. ensures that marker exists in ``README.md`` (adds/updates as needed), and
  2. removes any obsolete ``mcp-name`` entry from ``pyproject.toml`` ``[project.urls]``
     (cleaning up the earlier, rejected approach), dropping the table if it ends
     up empty.

``scripts/publish_registry.py`` reports a server as ``MISSING_MCP_NAME`` until
the marker is present in the *published* PyPI description, so after running this
you still need to cut a release (``scripts/release_all.py``).

The registry name is taken from each committed draft in
``registry/<id>/server.json`` (the ``name`` field).

Safe by default: with no flags it does a **dry run** (prints the per-repo plan,
writes nothing). Pass ``--write`` to edit files, ``--commit`` to also commit, and
``--push`` to push. Each edited pyproject is re-parsed with tomllib before
writing, so a malformed result is never saved.

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

COMMIT_MSG = "Declare mcp-name in README for MCP Registry (PyPI ownership)"

# An existing marker anywhere in the README, plain or inside an HTML comment.
README_MARKER = re.compile(r"""^.*mcp-name:\s*(?P<val>[^\s>]+).*$""", re.MULTILINE)
# A `"mcp-name" = "..."` line inside pyproject (any quoting / indent).
PYPROJECT_URL_LINE = re.compile(r"""^[ \t]*['"]?mcp-name['"]?[ \t]*=.*\r?\n""", re.MULTILINE)
# The [project.urls] header plus its body, up to the next top-level table / EOF.
URLS_SECTION = re.compile(
    r"^(?P<header>[ \t]*\[project\.urls\][ \t]*\r?\n)(?P<body>.*?)(?=^\[|\Z)",
    re.MULTILINE | re.DOTALL,
)

# README outcome states.
README_OK = "README_OK"
README_ADDED = "README_ADDED"
README_UPDATED = "README_UPDATED"
NO_README = "NO_README"
NO_REPO = "NO_REPO"


def load_drafts() -> list[tuple[str, str, str]]:
    """(server_id, registry name, repo url) for every committed registry draft."""
    out = []
    for path in sorted(REGISTRY_DIR.glob("*/server.json")):
        draft = json.loads(path.read_text(encoding="utf-8"))
        out.append((path.parent.name, draft["name"], draft["repository"]["url"]))
    return out


def marker_for(name: str) -> str:
    return f"<!-- mcp-name: {name} -->"


def patch_readme(text: str, name: str) -> tuple[str, str]:
    """Ensure the README carries `mcp-name: <name>`; return (new_text, state)."""
    marker = marker_for(name)
    m = README_MARKER.search(text)
    if m:
        if m.group("val") == name:
            return text, README_OK
        new_text = README_MARKER.sub(marker, text, count=1)
        return new_text, README_UPDATED
    sep = "" if text.endswith("\n") else "\n"
    return f"{text}{sep}\n{marker}\n", README_ADDED


def clean_pyproject(text: str) -> tuple[str, bool]:
    """Remove an obsolete mcp-name from [project.urls]; drop the table if empty."""
    sec = URLS_SECTION.search(text)
    if not sec or not PYPROJECT_URL_LINE.search(sec.group("body")):
        return text, False
    new_body = PYPROJECT_URL_LINE.sub("", sec.group("body"), count=1)
    start, end = sec.span()
    if new_body.strip() == "":
        # Table is now empty: remove header + body, then tidy blank lines.
        new_text = text[:start] + text[end:]
        new_text = re.sub(r"\n{3,}", "\n\n", new_text)
    else:
        new_text = text[:start] + sec.group("header") + new_body + text[end:]
    return new_text, True


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
    p.add_argument("--commit", action="store_true", help="git commit the edits in each repo (implies --write)")
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
            rows.append((sid, NO_REPO, f"{repo_dir} (use --clone)"))
            print(f"  repo not found (use --clone)")
            continue

        readme = find_readme(repo_dir)
        if readme is None:
            rows.append((sid, NO_README, "no README* file"))
            print("  no README found")
            continue

        # 1. README marker (the part PyPI actually validates).
        rtext = readme.read_text(encoding="utf-8")
        new_rtext, rstate = patch_readme(rtext, name)

        # 2. Clean up the obsolete pyproject [project.urls] mcp-name, if any.
        pyproject = repo_dir / "pyproject.toml"
        url_removed = False
        new_ptext = None
        if pyproject.exists():
            ptext = pyproject.read_text(encoding="utf-8")
            new_ptext, url_removed = clean_pyproject(ptext)
            if url_removed:
                try:
                    tomllib.loads(new_ptext)  # guard: must still parse
                except tomllib.TOMLDecodeError:
                    rows.append((sid, "PARSE_ERROR", "pyproject cleanup would not parse; left untouched"))
                    print("  ERROR: pyproject cleanup did not validate; skipping repo")
                    continue

        detail = name + ("  (+removed pyproject url)" if url_removed else "")
        will_change = rstate != README_OK or url_removed
        print(f"  README: {rstate}" + ("; pyproject mcp-name url removed" if url_removed else ""))

        if not args.write:
            rows.append((sid, rstate + (" (dry-run)" if will_change else ""), detail))
            continue

        if rstate != README_OK:
            readme.write_text(new_rtext, encoding="utf-8")
        if url_removed and new_ptext is not None:
            pyproject.write_text(new_ptext, encoding="utf-8")

        if will_change:
            changed += 1
            if args.commit:
                git(repo_dir, "add", "-A")
                if git(repo_dir, "commit", "-m", COMMIT_MSG) == 0:
                    print("  committed")
                    if args.push and git(repo_dir, "push") == 0:
                        print("  pushed")
        rows.append((sid, rstate, detail))

    # Summary.
    print("\n" + "=" * 70)
    print(f"{'SERVER':<32} {'STATE':<22} DETAIL")
    print("-" * 70)
    for sid, state, detail in rows:
        print(f"{sid:<32} {state:<22} {detail}")
    print("-" * 70)
    if args.write:
        print(f"changed {changed} repo(s)"
              + (" and committed" if args.commit else "")
              + (" and pushed" if args.push else ""))
    else:
        actionable = sum(1 for _, s, _ in rows if s.endswith("(dry-run)"))
        print(f"dry run: {actionable} repo(s) would change. Re-run with --write to apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
