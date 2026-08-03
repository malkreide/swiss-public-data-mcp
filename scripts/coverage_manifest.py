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

``start_event`` is the marker a tool can watch for to know this server reached
serving. For a structured log line it must be the **exact** value of the
``event``/``msg`` field — a prefix does not match, which cost one entry a round
of verification (``openlex-mcp`` was declared as ``Lifespan gestartet`` while
the field reads ``Lifespan gestartet — geteilter HTTP-Client bereit``). For a
plain-text line any stable substring works, but it must not contain a
timestamp: such a marker matches on the first run and never again.

``null`` means **not measured**, not "has none" — a consumer must be able to
tell those apart, or it counts its own ignorance as a finding.

A single ``null`` cannot carry that distinction, so ``start_event_status``
does, with one of four values:

    declared          a marker was measured and stands in ``start_event``
    silent            measured: no output at all within the smoke window
    sdk_banner_only   measured: only the SDK's own banner, which belongs to the
                      SDK rather than to the server and would vanish with an
                      SDK upgrade — pinning on it would measure the wrong thing
    unmeasured        not measured (no package on the index, or archived)

The two fields are two views of one measurement, and ``--check`` refuses any
entry where they disagree: ``declared`` exactly when ``start_event`` is set.
Without the status field a derived statement could only say "fifteen carry no
marker", which merges "says nothing" with "nobody looked" — the very
conflation this manifest exists to prevent.

``repositories`` (JSON output only) lists every repository the portfolio owns —
servers, tooling, and this index — and is deliberately *unfiltered*. The
selector answers "which servers should this probe measure"; a sweep over
repositories (open pull requests, workflow health, branch protection) asks a
different question, and handing it a scope-filtered list would narrow it
without saying so. Each entry carries ``archived`` so a consumer can name what
it skipped instead of silently not seeing it.

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


def repositories(d: dict) -> list[dict]:
    """Every repository this portfolio owns — servers, tooling, and the index.

    Deliberately **not** filtered by the selector. The selector answers "which
    servers should this probe measure"; this answers "which repositories exist",
    and they are different questions. A tool that sweeps repositories — open
    pull requests, branch protection, workflow health — needs the second one,
    and handing it a scope-filtered list would narrow its sweep without saying
    so. That is the failure this module exists to prevent, one layer out.

    ``archived`` travels with each entry rather than being dropped: an archived
    repository is read-only, so a finding about it is usually noise — but the
    consumer must be able to *say* it skipped one, not silently not see it.
    """
    out: list[dict] = [
        {
            "id": "swiss-public-data-mcp",
            "repository": d["portfolio_repository"],
            "kind": "index",
            "archived": False,
        }
    ]
    out += [
        {
            "id": t["id"],
            "repository": t["repository"],
            "kind": "tooling",
            "archived": bool(t.get("archived")),
        }
        for t in d.get("tooling", [])
    ]
    out += [
        {
            "id": s["id"],
            "repository": s["repository"],
            "kind": "server",
            "archived": bool(s.get("archived")),
        }
        for s in d["servers"]
    ]
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

        # `start_event`: die Zeichenkette, an der ein Werkzeug erkennt, dass
        # dieser Server das Bedienen erreicht hat. `null` heisst ausdruecklich
        # "noch nicht erhoben" — nicht "hat keins". Ein Werkzeug muss die
        # beiden unterscheiden koennen, sonst zaehlt es Nichtwissen als Befund.
        if "start_event" not in s:
            problems.append(f"{sid}: Feld 'start_event' fehlt (String oder null)")
        elif s["start_event"] is not None and not (
            isinstance(s["start_event"], str) and s["start_event"].strip()
        ):
            problems.append(f"{sid}: 'start_event' ist weder null noch ein Marker")

        problems.extend(check_start_event_status(s))

    return problems


# `start_event` und `start_event_status` sind zwei Sichten auf eine Messung.
# Ohne den Status heisst `null` zugleich "sagt nichts" und "nicht gemessen" —
# und ein daraus abgeleiteter Satz zaehlt das eigene Nichtwissen mit.
START_EVENT_STATES = ("declared", "silent", "sdk_banner_only", "unmeasured")


def check_start_event_status(s: dict) -> list[str]:
    """Der Status muss bekannt sein und zum Marker passen.

    Getrennte Funktion, weil `generate_readme.py` dieselbe Pruefung braucht:
    dort haengt ein veroeffentlichter Zahlensatz daran, und ein Widerspruch
    zwischen den beiden Feldern wuerde dort zu einer Aussage, die niemand
    gemessen hat.
    """
    sid = s.get("id", "<ohne id>")
    if "start_event_status" not in s:
        return [f"{sid}: Feld 'start_event_status' fehlt ({'/'.join(START_EVENT_STATES)})"]
    state = s["start_event_status"]
    if state not in START_EVENT_STATES:
        return [f"{sid}: 'start_event_status' {state!r} ist kein bekannter Wert"]
    declared = s.get("start_event") is not None
    if (state == "declared") != declared:
        return [
            f"{sid}: 'start_event_status' ist {state!r}, "
            f"'start_event' ist {'gesetzt' if declared else 'null'} — das widerspricht sich"
        ]
    return []


def validate_repositories(d: dict) -> list[str]:
    """Every declared repository is a GitHub URL, and no URL appears twice.

    A duplicate would make a repository-wide sweep report it twice and its own
    coverage count wrong — the same denominator problem as everywhere else here.
    """
    problems: list[str] = []
    seen: dict[str, str] = {}
    for r in repositories(d):
        url = (r.get("repository") or "").rstrip("/")
        parts = url.removeprefix("https://github.com/").split("/")
        if not url.startswith("https://github.com/") or len(parts) != 2 or not all(parts):
            problems.append(f"{r['id']}: 'repository' ist keine github.com/<owner>/<name>-URL")
            continue
        if url in seen:
            problems.append(f"{r['id']}: 'repository' {url} schon bei {seen[url]}")
        seen[url] = r["id"]
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
        problems = validate(servers) + validate_repositories(d)
        if problems:
            print("portfolio.json: Manifest-Verstoesse", file=sys.stderr)
            for msg in problems:
                print(f"  {msg}", file=sys.stderr)
            return 1
        counts = collections.Counter(
            "ohne Paket" if s["pypi_dist"] is None else "mit Paket" for s in servers
        )
        starts = collections.Counter(s["start_event_status"] for s in servers)
        repos = collections.Counter(r["kind"] for r in repositories(d))
        print(f"pypi_dist OK ({len(servers)} Eintraege; {dict(counts)})")
        print(f"start_event OK ({dict(starts)})")
        print(f"repositories OK ({sum(repos.values())}; {dict(repos)})")
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
                "repositories": repositories(d),
                "servers": [
                    {
                        "id": s["id"],
                        "repository": s["repository"],
                        "pypi_dist": s["pypi_dist"],
                        "start_event": s.get("start_event"),
                        "start_event_status": s.get("start_event_status"),
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
