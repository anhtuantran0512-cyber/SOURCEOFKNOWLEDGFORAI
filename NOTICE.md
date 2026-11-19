# NOTICE — sources, licenses and attribution

This repository is a **learning archive**. It indexes public front-end patterns and keeps the
original attribution next to every file. Nothing here is sold, relicensed or presented as original work.

| Source | Upstream repository | License on record |
|---|---|---|
| CodeFronts | <https://github.com/codefronts/toolkit> (tools only, not the catalogue) | MIT |
| lucianLabs | <https://github.com/Seokwoooo/lucian-uxui-prompt> | MIT (c) 2026 Seokwoooo |
| lucianLabs skill | <https://github.com/Seokwoooo/lucian-uxui> | MIT |
| MotionSites AI | none | free prompts, property of MotionSites AI |
| Pin UI | <https://github.com/shadcn-labs/Pin-UI> (no `LICENSE` file; terms in README) | MIT components |
| ThreeUI | none | catalogue metadata; source sold via Pro MCP |

## 1. CodeFronts — `sources/codefronts/`

- Source: <https://codefronts.com/>
- Collected: public component pages (live demo + code + built-in "AI prompt" block).
- License: each archived prompt keeps the site's own line: **"MIT licensed."** The generated prompt is
  published by CodeFronts for copy/paste into AI tools.
- Preserved per file: source URL, title, section, category, description, full prompt.
- Do not remove the `Source:` line inside the prompt.

## 2. lucianLabs UX/UI Prompt — `sources/lucianlabs/`

- Source: <https://lucianlabs.dev/en/uxui-prompt/>
- Collected: 400 elements (200 interfaces + 200 animations), English titles/summaries, localized code,
  theme tokens and the site's own ready-to-use prompt wrapper.
- License: **MIT License (c) 2026 Seokwoooo**, stated by the site and kept as a comment at the top of
  every element's code. Full text: [`LICENSES/lucianlabs-MIT.txt`](LICENSES/lucianlabs-MIT.txt).
- Preserved per file: element id, canonical URL, license comment, tags, category.

## 3. MotionSites AI — `sources/motionsites/`

- Source: <https://motionsites.ai/sections>
- Collected: **only the prompts the site publishes as free** (`is_free = true`, 321 of 772 at the time
  of collection). Paid/unlimited prompts are **not** collected, not bypassed and not mirrored.
- Rights: prompts remain the property of MotionSites AI and their authors. They are included here for
  personal study and reference, with a link back to the source. This repository does not relicense them.
- The full catalogue of titles/categories (`sources/motionsites/catalog.json`) is public listing metadata
  and is included as an index only; `is_free` marks what is accessible without a subscription.
- If you are the rights holder and want an entry removed, open an issue in this repository.

## 4. Pin UI — `sources/pinui/`

- Site: <https://www.pinui.xyz/> · Source repo: <https://github.com/shadcn-labs/Pin-UI>
- Collected: the site's own public shadcn registry (`/r/registry.json`, 30 components) and its public
  block registry (`/r/blocx/<slug>.json`, 11 sections), plus the 50 public pages as briefs.
- License: **MIT (c) Rachit Thakur / Shadcn Labs**, kept as the header comment inside every component
  file. The registry is published by the site specifically for `npx shadcn@latest add`.
- `robots.txt` disallows `/api/`; this archive never calls it. No paid or gated content exists on the site.
- If you are the rights holder and want an entry removed, open an issue.

## 5. ThreeUI — `sources/threeui/`

- Site: <https://threeui.com/> · Browse: <https://threeui.com/browse?sort=recent>
- Collected: **public catalogue metadata only** — every item page listed in `sitemap.xml` (961 items,
  1,485 tag pages), with title, category, description, runtime, live URL and preview image.
- **Not collected:** source files, premium templates and prompts. ThreeUI distributes those through an
  authenticated Pro MCP (<https://threeui.com/mcp>). This archive does not bypass, guess or reconstruct
  that content; the item briefs link to the live page instead.
- Rights: ThreeUI and the individual authors. Metadata is reproduced for indexing and reference with a
  link back to every item.
- If you are the rights holder and want an entry removed, open an issue.

## 6. Generated / original material

Files under `docs/`, the repository structure, the index files and `scripts/` are original work for this
archive and may be reused under MIT. They do not relicense any third-party content listed above.

## 7. External assets referenced inside prompts

Some prompts reference third-party images, fonts, videos or CDN URLs (for example `images.higgs.ai`,
`cloudfront.net`, Google Fonts). Those URLs belong to their owners, may expire, and are **not** bundled
here. Replace them with your own assets before shipping anything.

## 8. No affiliation

This repository is not affiliated with CodeFronts, lucianLabs, MotionSites AI, Pin UI / Shadcn Labs or
ThreeUI. Names and links are used for attribution only.
