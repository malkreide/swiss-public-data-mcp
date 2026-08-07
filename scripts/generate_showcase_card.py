#!/usr/bin/env python3
"""Generate the opendata.swiss showcase card from portfolio.json.

The card image submitted to the showcase form states counts — servers, distinct
official data sources, domains — and draws one converging line per domain. Baking
those numbers into an image by hand is exactly the drift the other generators
exist to prevent, so the card's HTML is generated from `portfolio.json` and CI
checks it, mirroring `scripts/generate_readme.py`.

    docs/showcase-card.tmpl.html   template with {{PLACEHOLDER}} slots (edit this)
    docs/showcase-card.html        generated (do not edit)
    docs/showcase-card.png         1200x630, submitted to the showcase form
    docs/social-preview.png        1280x640, GitHub social preview

The bitmaps are rendered from that HTML by ``scripts/render_showcase_images.mjs``
in two sizes -- 1200x630 for the showcase form, 1280x640 for GitHub's social
preview. They are committed, so ``--check`` verifies the HTML but *not* the
images; re-render whenever the counts change:

    python scripts/generate_showcase_card.py
    node scripts/render_showcase_images.mjs

Usage:
    python scripts/generate_showcase_card.py           # rewrite the HTML
    python scripts/generate_showcase_card.py --check    # exit 1 if out of date
"""

from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PORTFOLIO = ROOT / "portfolio.json"
TEMPLATE = ROOT / "docs" / "showcase-card.tmpl.html"
OUT = ROOT / "docs" / "showcase-card.html"

LEGACY_LABEL = "Legacy / Superseded"

# Short labels for the card's domain strip. Keyed by the portfolio category
# label so a renamed category fails loudly instead of silently disappearing
# from the image.
DOMAIN_LABELS = {
    "Transport & Mobility": "Transport",
    "Energy & Infrastructure": "Energy",
    "Environment & Climate": "Environment",
    "Legal, Courts & Regulatory": "Law",
    "Semantics, Metadata & Interoperability": "Interoperability",
    "Statistics & Geodata": "Statistics & geodata",
    "Education & Research": "Education",
    "Economics & Finance": "Finance",
    "Culture & Media": "Culture",
    "Health": "Health",
    "Food Safety": "Food safety",
    "Democracy & Transparency": "Democracy",
    "Tech Intelligence": "Tech signals",
}

# Diagram geometry in SVG user units; sources fan in to the hub at (HUB_X, HUB_Y).
FAN_TOP, FAN_BOTTOM = 12, 388
HUB_X, HUB_Y = 208, 200


def load() -> dict:
    return json.loads(PORTFOLIO.read_text(encoding="utf-8"))


def facts(data: dict) -> dict:
    active = [s for s in data["servers"] if s.get("scope") != "legacy"]
    cats = [c for c in data["display_categories"] if c["label"] != LEGACY_LABEL]
    missing = [c["label"] for c in cats if c["label"] not in DOMAIN_LABELS]
    if missing:
        raise SystemExit(
            "ERROR: no short card label for: "
            + ", ".join(missing)
            + "\nAdd them to DOMAIN_LABELS in scripts/generate_showcase_card.py"
        )
    return {
        "servers": len(active),
        # Servers that read the same portal (e.g. both mobility servers) count once.
        "sources": len({s["data_source_url"] for s in active}),
        "domains": len(cats),
        "labels": [DOMAIN_LABELS[c["label"]] for c in cats],
    }


def build_fan(n: int) -> str:
    """One dot and one converging bezier per domain."""
    step = (FAN_BOTTOM - FAN_TOP) / (n - 1) if n > 1 else 0
    ys = [round(FAN_TOP + i * step) for i in range(n)]
    paths = "\n".join(
        f'          <path d="M26 {y} C150 {y} 158 {HUB_Y} {HUB_X} {HUB_Y}"/>' for y in ys
    )
    dots = "\n".join(f'          <circle cx="20" cy="{y}" r="5.2"/>' for y in ys)
    return (
        '        <g fill="none" stroke="url(#ln)" stroke-width="1.9">\n'
        f"{paths}\n        </g>\n\n"
        f'        <g fill="#3878FF">\n{dots}\n        </g>'
    )


def render(data: dict) -> str:
    f = facts(data)
    out = TEMPLATE.read_text(encoding="utf-8")
    for token, value in (
        ("{{SERVERS}}", str(f["servers"])),
        ("{{SOURCES}}", str(f["sources"])),
        ("{{DOMAINS}}", str(f["domains"])),
        ("{{DOMAIN_LIST}}", " · ".join(f["labels"])),
        ("{{FAN}}", build_fan(f["domains"])),
    ):
        out = out.replace(token, value)
    if "{{" in out:
        raise SystemExit(f"ERROR: unresolved placeholder in {TEMPLATE.name}")
    return out


def main() -> int:
    check = "--check" in sys.argv[1:]
    rendered = render(load())
    current = OUT.read_text(encoding="utf-8") if OUT.exists() else None
    if current == rendered:
        if not check:
            print("docs/showcase-card.html already up to date")
        return 0
    if check:
        print(
            "ERROR: docs/showcase-card.html is out of sync with portfolio.json\n"
            "Run: python scripts/generate_showcase_card.py\n"
            "Then: node scripts/render_showcase_images.mjs",
            file=sys.stderr,
        )
        return 1
    OUT.write_text(rendered, encoding="utf-8")
    print("updated docs/showcase-card.html — now run: node scripts/render_showcase_images.mjs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
