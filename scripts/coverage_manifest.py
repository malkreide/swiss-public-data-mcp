#!/usr/bin/env python3
"""Emit the list of servers a portfolio-wide tool is supposed to cover.

Every sweep across the portfolio needs a target list, and until now each tool
carried its own. That is the failure this script exists to prevent.

THE INCIDENT
------------
A portfolio-wide identity sweep on 2026-07-31 reported "33 of 33 ok". The
sentence was true and the set was wrong: ``portfolio.json`` lists 43 active
servers, and ten of them — seven of those ``core`` — had never been in the
sweep at all. Among them ``meteoswiss-mcp``, whose broken release is the
motivating incident documented in ``release_gap.py``. Nothing contradicted the
number, because nothing ever compared it against the source of truth.

A hand-maintained target list drifts exactly the way a hand-maintained version
number drifts, and for the same reason: nothing downstream disagrees with it.

WHAT A CONSUMER IS EXPECTED TO DO
---------------------------------
Read the manifest, run against every entry, and then *say what it covered*:

    33/43 covered — 10 skipped: fedlex-mcp, i14y-mcp, …

A tool that skips entries silently reports on an unknown subset while looking
like it reported on the portfolio. Incomplete coverage should be a non-zero
exit unless the skip was named and justified — "I did not look" and "there was
nothing there" must not share an exit code.

``pypi_dist`` is the distribution name on the index, or ``null`` for a server
that publishes no package (one legacy repo). Tools that measure a *published
artefact* must skip the ``null`` entries — that is a justified skip, and it is
justified precisely because the manifest says so rather than because a list
somewhere happened to omit it.

Usage:
    python scripts/coverage_manifest.py                      # active servers, text
    python scripts/coverage_manifest.py --format json        # for tooling
    python scripts/coverage_manifest.py --scope core         # core only
    python scripts/coverage_manifest.py --published-only     # entries with a dist
    python scripts/coverage_manifest.py --check              # validate the field
    python scripts/coverage_manifest.py --verify-index       # ask the index (network)
"""
from __future__ import annotations

import argparse
import collections
import concurrent.futures
import json
import pathlib
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
PORTFOLIO = ROOT / "portfolio.json"

# A server counts as active unless it has been archived. ``production_ready``
# and ``production_ready_legacy`` are both live for coverage purposes: a legacy
# server users can still install is a server whose artefact can still be wrong.
ACTIVE_PREFIX = "production_ready"


def load() -> dict:
    return json.loads(PORTFOLIO.read_text(encoding="utf-8"))


def select(
    servers: list[dict],
    *,
    scope: str | None = None,
    include_archived: bool = False,
    published_only: bool = False,
) -> list[dict]:
    out = []
    for s in servers:
        if not include_archived and not s["status"].startswith(ACTIVE_PREFIX):
            continue
        if scope and s["scope"] != scope:
            continue
        if published_only and not s.get("pypi_dist"):
            continue
        out.append(s)
    return out


def validate(servers: list[dict]) -> list[str]:
    """Structural checks only — no network. CI runs this on every pull request.

    Whether the distribution actually exists on the index is a different
    question with a different failure mode (the index is reachable or it is
    not), and it belongs in a scheduled job rather than in the path of every
    pull request. Deliberately not "excluded from CI": excluded checks rot.
    """
    problems: list[str] = []
    seen: dict[str, str] = {}

    for s in servers:
        sid = s["id"]
        if "pypi_dist" not in s:
            problems.append(f"{sid}: Feld 'pypi_dist' fehlt (String oder null)")
            continue
        dist = s["pypi_dist"]
        if dist is None:
            continue
        if not isinstance(dist, str) or not dist.strip():
            problems.append(f"{sid}: 'pypi_dist' ist weder null noch ein Name")
            continue
        if dist in seen:
            problems.append(f"{sid}: 'pypi_dist' {dist!r} schon bei {seen[dist]}")
        seen[dist] = sid

    return problems


def verify_index(servers: list[dict], index_url: str, timeout: float) -> list[str]:
    """Ask the index whether every declared distribution is actually there.

    Separate from ``--check`` on purpose. This one needs the network, so its
    failures have two causes that look alike — a wrong name in portfolio.json,
    and an index that is briefly unreachable. Running it on every pull request
    would make the second cause block the first from being fixed. It runs on a
    schedule instead, where a red run is news rather than noise.

    Reads the Simple API (PEP 503), because that is the one ``pip`` and ``uv``
    read; the JSON API has been observed lagging behind it by minutes after a
    publish.
    """
    base = index_url.rstrip("/")
    targets = [s for s in servers if s.get("pypi_dist")]

    def probe(s: dict) -> str | None:
        url = f"{base}/{s['pypi_dist'].lower()}/"
        try:
            with urllib.request.urlopen(url, timeout=timeout) as r:
                if r.status == 200:
                    return None
                return f"{s['id']}: {s['pypi_dist']} -> HTTP {r.status}"
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return f"{s['id']}: {s['pypi_dist']} liegt nicht auf {base}"
            return f"{s['id']}: {s['pypi_dist']} -> HTTP {e.code}"
        except Exception as e:  # Netzfehler, Timeout, TLS
            return f"{s['id']}: {s['pypi_dist']} nicht erreichbar ({type(e).__name__})"

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        return [m for m in ex.map(probe, targets) if m]


def main() -> int:
    p = argparse.ArgumentParser(prog="coverage_manifest")
    p.add_argument("--scope", help="nur dieser Scope (core, adjacent-context, legacy)")
    p.add_argument(
        "--include-archived",
        action="store_true",
        help="archivierte Server mitnehmen (Standard: nur aktive)",
    )
    p.add_argument(
        "--published-only",
        action="store_true",
        help="nur Einträge mit einem Paket auf dem Index",
    )
    p.add_argument("--format", choices=["text", "json"], default="text")
    p.add_argument(
        "--check",
        action="store_true",
        help="portfolio.json gegen die pypi_dist-Regeln prüfen, Exit 1 bei Verstoss",
    )
    p.add_argument(
        "--verify-index",
        action="store_true",
        help="jeden pypi_dist gegen den Index prüfen (braucht Netz; für den Nightly)",
    )
    p.add_argument("--index-url", default="https://pypi.org/simple")
    p.add_argument("--timeout", type=float, default=30.0)
    args = p.parse_args()

    d = load()
    servers = d["servers"]

    if args.verify_index:
        problems = verify_index(servers, args.index_url, args.timeout)
        declared = sum(1 for s in servers if s.get("pypi_dist"))
        if problems:
            print(f"Index-Abgleich: {len(problems)} von {declared} fehlerhaft", file=sys.stderr)
            for msg in problems:
                print(f"  {msg}", file=sys.stderr)
            return 1
        print(f"Index-Abgleich OK ({declared} Distributionen auf {args.index_url})")
        return 0

    if args.check:
        problems = validate(servers)
        if problems:
            print("portfolio.json: pypi_dist-Verstoesse", file=sys.stderr)
            for msg in problems:
                print(f"  {msg}", file=sys.stderr)
            return 1
        counts = collections.Counter(
            "ohne Paket" if s["pypi_dist"] is None else "mit Paket" for s in servers
        )
        print(f"pypi_dist OK ({len(servers)} Eintraege; {dict(counts)})")
        return 0

    sel = select(
        servers,
        scope=args.scope,
        include_archived=args.include_archived,
        published_only=args.published_only,
    )

    if args.format == "json":
        json.dump(
            {
                "source": "portfolio.json",
                "schema_version": d["schema_version"],
                "selector": {
                    "scope": args.scope,
                    "include_archived": args.include_archived,
                    "published_only": args.published_only,
                },
                "expected": len(sel),
                "servers": [
                    {
                        "id": s["id"],
                        "repository": s["repository"],
                        "pypi_dist": s["pypi_dist"],
                        "scope": s["scope"],
                        "status": s["status"],
                    }
                    for s in sel
                ],
            },
            sys.stdout,
            indent=2,
            ensure_ascii=False,
        )
        sys.stdout.write("\n")
        return 0

    for s in sel:
        print(s["pypi_dist"] or f"# {s['id']} (kein Paket auf dem Index)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        # `… | head` schliesst die Pipe; das ist kein Fehler dieses Skripts.
        sys.stderr.close()
        raise SystemExit(0)
