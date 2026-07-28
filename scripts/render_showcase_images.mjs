// Render the showcase card bitmaps from docs/showcase-card.html.
//
// Run `python scripts/generate_showcase_card.py` first — that regenerates the
// HTML from portfolio.json. This script only turns the HTML into PNGs:
//
//   docs/showcase-card.png    1200x630  submitted to the opendata.swiss form
//   docs/social-preview.png   1280x640  uploaded under Settings > Social preview
//
// Two sizes because the targets differ: opendata.swiss shows the card in a
// responsive tile, GitHub renders social previews at a strict 2:1. Feeding
// GitHub the 1200x630 file letterboxes it.
//
// Usage:  node scripts/render_showcase_images.mjs
//
// Requires Playwright + Chromium. These are committed bitmaps, so nothing in CI
// can tell that they are stale — re-run this whenever the counts change.

import { createRequire } from 'node:module'
import { existsSync } from 'node:fs'
import path from 'node:path'

const require = createRequire(import.meta.url)
const { chromium } = require('playwright')

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..')
const SOURCE = path.join(ROOT, 'docs', 'showcase-card.html')

const TARGETS = [
  { out: 'docs/showcase-card.png', width: 1200, height: 630 },
  { out: 'docs/social-preview.png', width: 1280, height: 640 },
]

if (!existsSync(SOURCE)) {
  console.error(`missing ${SOURCE}\nRun: python scripts/generate_showcase_card.py`)
  process.exit(1)
}

const browser = await chromium.launch()
try {
  for (const { out, width, height } of TARGETS) {
    const page = await browser.newPage({ viewport: { width, height } })
    await page.goto('file://' + SOURCE, { waitUntil: 'networkidle' })
    // The template pins 1200x630; override so the flex layout fills each target.
    await page.addStyleTag({
      content: `html,body{width:${width}px !important;height:${height}px !important}`,
    })
    await page.screenshot({ path: path.join(ROOT, out) })
    await page.close()
    console.log(`wrote ${out} (${width}x${height})`)
  }
} finally {
  await browser.close()
}
