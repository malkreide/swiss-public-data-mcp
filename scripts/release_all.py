#!/usr/bin/env python3
"""Cut a metadata release per server repo so ``mcp-name`` lands on PyPI.

PyPI metadata is immutable per version: once ``scripts/patch_mcp_name.py`` has
added the ``[project.urls] "mcp-name"`` link, that link only reaches the registry
after a **new release** is published. This script automates that release across
all server repos: bump the version, build, verify the built metadata actually
carries ``mcp-name``, and (optionally) upload to PyPI.

It is the step between ``patch_mcp_name.py`` and ``publish_registry.py``:

    patch_mcp_name.py --write --commit --push     # mcp-name into pyproject.toml
    release_all.py    --build --commit --push --upload   # <-- this script
    publish_registry.py --clone --publish         # reads the fresh metadata

The expected registry name is read from ``registry/<id>/server.json`` and is the
exact value the build must advertise (``Project-URL: mcp-name, <name>``).

Versioning modes (auto-detected from pyproject.toml):
  * **static**  -- ``[project].version`` (or ``[tool.poetry].version``): bumped.
  * **dynamic** -- ``dynamic = ["version"]`` (setuptools-scm / hatch-vcs): the
    release is a git tag, so the bump is a new ``vX.Y.Z`` tag (needs --commit).

Safe by default: with no flags it does a **dry run** (prints the per-repo plan:
mode, current -> next version, whether mcp-name is present). Nothing is edited,
built, or uploaded. Then:
  --build   bump version, run `python -m build`, `twine check`, verify metadata
  --commit  commit the bump and create the vX.Y.Z tag (implies --build)
  --push    push the commit and tag (implies --commit)
  --upload  `twine upload dist/*` for repos that built and verified (implies --build)

Uploading needs PyPI credentials (e.g. ``~/.pypirc`` or TWINE_USERNAME/PASSWORD).
"""
from __future__ import annotations

import argparse
import glob
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tomllib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
REGISTRY_DIR = ROOT / "registry"

# `version = "1.2.3"` line inside a given [table] (header .. next top-level table).
def _section_re(table: str) -> re.Pattern[str]:
    esc = re.escape(table)
    return re.compile(
        rf"^(?P<header>[ \t]*\[{esc}\][ \t]*\r?\n)(?P<body>.*?)(?=^\[|\Z)",
        re.MULTILINE | re.DOTALL,
    )

VERSION_LINE = re.compile(r"""^(?P<pre>[ \t]*version[ \t]*=[ \t]*)['"](?P<ver>[^'"]+)['"]""", re.MULTILINE)
SEMVER_TAG = re.compile(r"^v?(\d+)\.(\d+)\.(\d+)$")

# States.
BLOCKED = "BLOCKED_NO_MCP_NAME"
NO_REPO = "NO_REPO"
NO_PYPROJECT = "NO_PYPROJECT"
NO_VERSION = "NO_VERSION_FIELD"
TAG_NEEDS_COMMIT = "TAG_MODE_NEEDS_COMMIT"
BUILD_FAILED = "BUILD_FAILED"
CHECK_FAILED = "TWINE_CHECK_FAILED"
VERIFY_FAILED = "MCP_NAME_NOT_IN_BUILD"
BUILT = "BUILT"
UPLOADED = "UPLOADED"


def load_drafts() -> list[tuple[str, str, str]]:
    """(server_id, registry name, repo url) from the committed registry drafts."""
    out = []
    for path in sorted(REGISTRY_DIR.glob("*/server.json")):
        d = json.loads(path.read_text(encoding="utf-8"))
        out.append((path.parent.name, d["name"], d["repository"]["url"]))
    return out


def bump(version: str, part: str) -> str:
    """PEP 440-ish release bump; pre/post/dev suffixes are dropped to the release."""
    release = re.match(r"\d+(?:\.\d+)*", version)
    nums = [int(x) for x in (release.group(0) if release else "0").split(".")]
    while len(nums) < 3:
        nums.append(0)
    if part == "major":
        nums = [nums[0] + 1, 0, 0]
    elif part == "minor":
        nums = [nums[0], nums[1] + 1, 0]
    else:  # patch
        nums = [nums[0], nums[1], nums[2] + 1]
    return ".".join(map(str, nums))


def has_mcp_name(data: dict, name: str) -> bool:
    return (data.get("project", {}).get("urls", {}) or {}).get("mcp-name") == name


def detect_version(data: dict) -> tuple[str | None, str | None]:
    """Return (mode, current_version). mode in {'project','poetry','dynamic'}."""
    project = data.get("project", {})
    if "version" in project:
        return "project", project["version"]
    if "version" in (project.get("dynamic") or []):
        return "dynamic", None
    poetry = data.get("tool", {}).get("poetry", {})
    if "version" in poetry:
        return "poetry", poetry["version"]
    return None, None


def set_version_in_section(text: str, table: str, new_version: str) -> str | None:
    sec = _section_re(table).search(text)
    if not sec or not VERSION_LINE.search(sec.group("body")):
        return None
    new_body = VERSION_LINE.sub(lambda m: f'{m.group("pre")}"{new_version}"', sec.group("body"), count=1)
    start, end = sec.span()
    return text[:start] + sec.group("header") + new_body + text[end:]


def latest_tag_version(repo_dir: pathlib.Path) -> str:
    res = subprocess.run(["git", "-C", str(repo_dir), "tag", "--list", "v*"],
                         capture_output=True, text=True, check=False)
    best = (0, 0, 0)
    for line in res.stdout.split():
        m = SEMVER_TAG.match(line.strip())
        if m:
            best = max(best, tuple(int(g) for g in m.groups()))
    return ".".join(map(str, best))


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


def run(cmd: list[str], cwd: pathlib.Path) -> bool:
    return subprocess.run(cmd, cwd=str(cwd), check=False).returncode == 0


def git(repo_dir: pathlib.Path, *args: str) -> bool:
    return subprocess.run(["git", "-C", str(repo_dir), *args], check=False).returncode == 0


def mcp_name_in_dist(repo_dir: pathlib.Path, name: str) -> bool:
    """True if the freshest built wheel advertises Project-URL: mcp-name, <name>."""
    wheels = sorted(glob.glob(str(repo_dir / "dist" / "*.whl")), key=lambda p: pathlib.Path(p).stat().st_mtime)
    if not wheels:
        return False
    with zipfile.ZipFile(wheels[-1]) as zf:
        meta_names = [n for n in zf.namelist() if n.endswith("METADATA")]
        if not meta_names:
            return False
        meta = zf.read(meta_names[0]).decode("utf-8", "replace")
    for line in meta.splitlines():
        if line.lower().startswith("project-url:"):
            label, _, value = line[len("project-url:"):].partition(",")
            if label.strip().lower() == "mcp-name" and value.strip() == name:
                return True
    return False


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--only", nargs="+", metavar="ID", help="restrict to these server ids")
    p.add_argument("--repos-dir", type=pathlib.Path, default=ROOT.parent,
                   help="directory containing server repos as <id>/ (default: parent of this repo)")
    p.add_argument("--clone", action="store_true", help="git clone missing repos (ff-pull existing)")
    p.add_argument("--part", choices=["patch", "minor", "major"], default="patch",
                   help="version bump size for static-version projects (default: patch)")
    p.add_argument("--build", action="store_true", help="bump, build, twine check, verify metadata")
    p.add_argument("--commit", action="store_true", help="commit the bump and create the vX.Y.Z tag (implies --build)")
    p.add_argument("--push", action="store_true", help="push commit and tag (implies --commit)")
    p.add_argument("--upload", action="store_true", help="twine upload verified builds (implies --build)")
    return p.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.push:
        args.commit = True
    if args.commit or args.upload:
        args.build = True

    drafts = load_drafts()
    if args.only:
        wanted = set(args.only)
        drafts = [r for r in drafts if r[0] in wanted]
        missing = wanted - {r[0] for r in drafts}
        if missing:
            print(f"ERROR: unknown server id(s): {', '.join(sorted(missing))}", file=sys.stderr)
            return 2

    rows: list[tuple[str, str, str]] = []
    uploaded = built = 0

    for sid, name, url in drafts:
        print(f"\n== {sid} ({name})")
        repo_dir = (args.repos_dir / sid).resolve()
        if not ensure_repo(repo_dir, url, args.clone):
            rows.append((sid, NO_REPO, f"{repo_dir} (use --clone)"))
            print(f"  repo not found (use --clone)")
            continue
        pyproject = repo_dir / "pyproject.toml"
        if not pyproject.exists():
            rows.append((sid, NO_PYPROJECT, str(pyproject)))
            print("  no pyproject.toml")
            continue

        text = pyproject.read_text(encoding="utf-8")
        try:
            data = tomllib.loads(text)
        except tomllib.TOMLDecodeError as exc:
            rows.append((sid, NO_PYPROJECT, f"unparseable: {exc}"))
            continue

        if not has_mcp_name(data, name):
            rows.append((sid, BLOCKED, "run patch_mcp_name.py first"))
            print("  blocked: mcp-name missing (run patch_mcp_name.py)")
            continue

        mode, current = detect_version(data)
        if mode is None:
            rows.append((sid, NO_VERSION, "no [project].version / dynamic / poetry version"))
            print("  no version field found")
            continue

        if mode == "dynamic":
            nxt = bump(latest_tag_version(repo_dir), args.part)
            plan = f"tag v{nxt} (dynamic)"
        else:
            nxt = bump(current, args.part)
            plan = f"{current} -> {nxt} ({mode})"
        print(f"  plan: {plan}")

        if not args.build:
            rows.append((sid, "PLAN", plan))
            continue

        # --- apply the bump ---
        if mode == "dynamic":
            if not args.commit:
                rows.append((sid, TAG_NEEDS_COMMIT, f"would tag v{nxt}; needs --commit"))
                print("  dynamic version: tagging requires --commit; skipped build")
                continue
        else:
            new_text = set_version_in_section(text, "project" if mode == "project" else "tool.poetry", nxt)
            if new_text is None or detect_version(tomllib.loads(new_text))[1] != nxt:
                rows.append((sid, NO_VERSION, "could not rewrite version line"))
                print("  ERROR: could not rewrite version; left untouched")
                continue
            pyproject.write_text(new_text, encoding="utf-8")
            if args.commit:
                git(repo_dir, "add", "pyproject.toml")
                git(repo_dir, "commit", "-m", f"Release {nxt}")

        if args.commit:
            git(repo_dir, "tag", f"v{nxt}")

        # --- build ---
        dist = repo_dir / "dist"
        if dist.exists():
            shutil.rmtree(dist)
        if not run([sys.executable, "-m", "build"], repo_dir):
            rows.append((sid, BUILD_FAILED, "python -m build failed"))
            print("  build failed")
            continue
        if not run([sys.executable, "-m", "twine", "check", *glob.glob(str(dist / "*"))], repo_dir):
            rows.append((sid, CHECK_FAILED, "twine check failed"))
            print("  twine check failed")
            continue
        if not mcp_name_in_dist(repo_dir, name):
            rows.append((sid, VERIFY_FAILED, "Project-URL mcp-name absent from wheel"))
            print("  ERROR: built wheel does not advertise mcp-name; not uploading")
            continue
        built += 1
        print(f"  built and verified mcp-name in wheel ({nxt})")

        if args.push:
            git(repo_dir, "push")
            git(repo_dir, "push", "--tags")

        if args.upload:
            if run([sys.executable, "-m", "twine", "upload", *glob.glob(str(dist / "*"))], repo_dir):
                uploaded += 1
                rows.append((sid, UPLOADED, nxt))
                print(f"  uploaded {nxt}")
            else:
                rows.append((sid, "UPLOAD_FAILED", nxt))
        else:
            rows.append((sid, BUILT, nxt))

    # Summary.
    print("\n" + "=" * 66)
    print(f"{'SERVER':<32} {'STATE':<22} DETAIL")
    print("-" * 66)
    for sid, state, detail in rows:
        print(f"{sid:<32} {state:<22} {detail}")
    print("-" * 66)
    if args.upload:
        print(f"uploaded {uploaded} release(s); built {built}")
    elif args.build:
        print(f"built {built} release(s) (not uploaded). Re-run with --upload to publish.")
    else:
        plans = sum(1 for _, s, _ in rows if s == "PLAN")
        print(f"dry run: {plans} repo(s) ready to release. Re-run with --build (and --upload).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
