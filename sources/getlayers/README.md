# GetLayers — template archive

Production-grade page and hero templates published on <https://www.getlayers.ai/templates>.

- Templates archived: **62 of 62** in the public catalogue
- Free prompts captured: **11 free-tier templates** (1 captured so far — see below)
- Tier split: **11 Free · 51 Premium**
- Format: one folder per template (`ITEM.md` + `metadata.json`), plus `prompts/` and `assets/`
- Upstream repository: none for the prompts. The site publishes an agent starter kit at
  <https://github.com/textura-agency/ai-design-vault>; it does not contain the prompts.
- Rights: previews and prompts remain the property of GetLayers / Textura Agency; not relicensed here.
  See [`NOTICE.md`](../../NOTICE.md).

## What each template folder holds

| File | Contents |
|---|---|
| `items/<id>/ITEM.md` | brief: description, stack, tags, tone, mood, measured frame timings, Lighthouse scores, asset URLs, prompt status |
| `items/<id>/metadata.json` | the full public record as the site ships it, plus the page's JSON-LD |
| `prompts/<id>.md` | the free prompt, verbatim (free tier only) |
| `assets/<id>.webp` | poster still |
| `assets/<id>-figma.webp` | Figma preview, where the site publishes one (40 of 62) |

## What is complete, and what is gated

**Complete:** every template in the public catalogue (62), with every public metadata field — tier,
stack, tags, tone, mood, keywords, type tags, publish date, likes, per-viewport frame timings, Lighthouse
scores and audits, and all six public asset URLs. All 62 poster stills and all 40 Figma previews are
bundled.

**Gated, not bypassed:**

- **Premium prompts (51).** The copy endpoint answers
  `{"_apiError":{"code":"forbidden","message":"Upgrade to access this prompt."}}`. The briefs link to the
  live page instead. Nothing is guessed or reconstructed.
- **Free prompts (11).** Free, but the copy endpoint grants **one prompt per anonymous visitor per day**
  and then answers `rate_limited` — *"You've used today's free copy — sign in for unlimited free
  prompts."* One prompt (`soda`) was captured on the run that built this archive; the other ten are
  listed with the exact state in their brief. Re-run the collector on a later day, or pass your own
  signed-in session cookie, to capture them all:

  ```bash
  python3 scripts/fetch_getlayers.py --cookie-file ~/gl-cookies.txt
  ```

- **Video mockups and Lighthouse HTML (not committed).** Four mp4s per template plus two report pages
  run to roughly 1.1 GB. The URLs are recorded in every `ITEM.md`; fetch them locally with
  `python3 scripts/fetch_getlayers.py --media all`.

## Categories

Layout: 40 full-page · 22 hero.

| Industry | Templates |
|---|---:|
| Agency / Studio | 20 |
| AI / Tech | 14 |
| Portfolio | 11 |
| E-commerce | 10 |
| SaaS | 7 |
| Fintech | 6 |
| Sports / Education | 4 |
| Hospitality / Travel | 4 |
| Health / Science | 4 |
| Logistics | 1 |
| Energy | 1 |

Tone: 36 dark · 26 light. Stack: 55 Next.js · 38 Three.js · 38 landing page · 24 hero · 3 React.

## How it was collected

`scripts/fetch_getlayers.py` reads the same two public surfaces a browser reads:

1. `https://www.getlayers.ai/templates` — the React Server Component payload carries the whole
   catalogue as one `items` array. No private API, no scraping of rendered markup.
2. `https://www.getlayers.ai/layer/<id>` — the item page, for its JSON-LD and to confirm the live URL.
3. The **"Copy prompt" server action** the page itself calls, for free-tier prompts only.

No account was created, no paywall touched, no rate limit worked around. The collector is polite:
bounded concurrency, retries with backoff, a descriptive User-Agent, and it stops asking for a prompt
the moment the site says no.

## Refresh

```bash
python3 scripts/fetch_getlayers.py                    # metadata + stills + free prompts
python3 scripts/fetch_getlayers.py --media all        # + videos and Lighthouse reports
python3 scripts/build_source_indexes.py               # regenerate INDEX.md
python3 scripts/verify.py                             # counts, frontmatter, free/paid boundary
```
