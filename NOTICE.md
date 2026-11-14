# NOTICE — sources, licenses and attribution

This repository is a **learning archive**. It indexes public front-end patterns and keeps the
original attribution next to every file. Nothing here is sold, relicensed or presented as original work.

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

## 4. Generated / original material

Files under `docs/`, the repository structure, the index files and `scripts/` are original work for this
archive and may be reused under MIT. They do not relicense any third-party content listed above.

## 5. External assets referenced inside prompts

Some prompts reference third-party images, fonts, videos or CDN URLs (for example `images.higgs.ai`,
`cloudfront.net`, Google Fonts). Those URLs belong to their owners, may expire, and are **not** bundled
here. Replace them with your own assets before shipping anything.

## 6. No affiliation

This repository is not affiliated with CodeFronts, lucianLabs or MotionSites AI. Names and links are
used for attribution only.
