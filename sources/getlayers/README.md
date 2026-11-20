# GetLayers — five libraries

Immersive web work published on <https://www.getlayers.ai>: whole-page templates, 3D scenes, sections,
animated backgrounds and pure-WebGL gradients.

- Items archived: **892 of 892** across the five public catalogues
- Libraries: **62 templates · 222 3D scenes · 54 sections · 530 backgrounds · 24 gradients**
- Tier split: **47 Free · 845 Premium**
- Stills: **892** poster stills · **53** Figma previews
- Free media: **232 files · 595 MB** committed in `media/` — every asset the site publishes for the 47 free items
- Free prompts captured: **1** (`soda`) — the copy endpoint allows one per visitor per day, see below
- Format: one folder per item (`ITEM.md` + `metadata.json`), plus `prompts/`, `assets/` and `catalog/`
- Rights: previews and prompts remain the property of GetLayers / Textura Agency; not relicensed here.
  See [`NOTICE.md`](../../NOTICE.md).

## What each folder holds

| File | Contents |
|---|---|
| `items/<id>/ITEM.md` | brief: description, stack, tags, tone, mood, variants, measured frame timings, Lighthouse scores, asset URLs, prompt status |
| `items/<id>/metadata.json` | the full public record as the site ships it, plus the page's JSON-LD for templates |
| `prompts/<id>.md` | the free prompt, verbatim (free tier only) |
| `assets/<id>.webp` | poster still |
| `assets/<id>-figma.webp` | Figma preview, where the site publishes one (53 items) |
| `catalog/<category>.json` | the catalogue payload the site ships, untouched |
| `media/<id>/` | free items only: poster video, preview clip, device mockups, stills, Lighthouse reports |
| `MEDIA.md` · `media-sizes.json` · `media-free.json` | full inventory (10.0 GB, 5,854 files) and the record of what is downloaded |

## The five libraries

| Library | Items | Free | What it is |
|---|---:|---:|---|
| [`template`](catalog/template.json) | 62 | 11 | Full pages and heroes: stack, tone, frame timings, Lighthouse |
| [`3d_scene`](catalog/3d_scene.json) | 222 | 7 | WebGL scenes: particles, terrain, product objects, tunnels |
| [`section`](catalog/section.json) | 54 | 0 | One block, ready to place: mockups, Figma previews |
| [`background`](catalog/background.json) | 530 | 29 | Animated and still backdrops, downloadable as 4K video |
| [`gradient`](catalog/gradient.json) | 24 | 0 | Pure-WebGL looks with hue ramps and shader hashes |

Tone: templates 36 dark / 26 light · 3D 156 / 66 · sections 27 / 27 · backgrounds 224 / 306.

## What is complete, and what is gated

**Complete:** every item in all five public catalogues (892), with every public metadata field — tier,
stack, tags, tone, mood, keywords, type tags, publish date, likes, variants and their colour ramps,
per-viewport frame timings, Lighthouse scores and audits, and every public asset URL. All 892 poster
stills and all 53 Figma previews are bundled.

**Gated, not bypassed:**

- **Premium prompts (845 items).** The copy endpoint answers
  `{"_apiError":{"code":"forbidden","message":"Upgrade to access this prompt."}}` — and for backgrounds,
  *"Background prompts come with Unlimited Plus and Full Stack — free backgrounds stay free to
  download."* Briefs link to the live page instead. Nothing is guessed or reconstructed.
- **Free prompts (18: 11 templates + 7 3D scenes).** Free, but the copy endpoint grants **one prompt per
  anonymous visitor per day** and then answers `rate_limited` — *"You've used today's free copy — sign in
  for unlimited free prompts."* One prompt (`soda`) was captured on the run that built this archive; the
  other seventeen are listed with the exact state in their brief. Re-run the collector on a later day, or
  pass your own signed-in session cookie, to capture them all:

  ```bash
  python3 scripts/fetch_getlayers.py --cookie-file ~/gl-cookies.txt
  ```

- **Free backgrounds (29) are free to *download*, not to prompt.** Their 4K mp4 is public; the prompt is
  not. The still and the video URL are archived, the prompt is not.

- **Premium media (not fetched).** Nothing behind the paywall is downloaded, so the archive never holds
  what a subscription buys.

- **All media, 10.0 GB in 5,854 files.** Across the five libraries the published media measures 10.0 GB —
  4K hero videos, preview clips, device mockups, Lighthouse reports. That is far past GitHub's per-file
  (100 MB) and repository (5 GB) limits, so it is not all committed. The **free tier is** (595 MB, 232
  files, largest file 13 MB); for the rest, `MEDIA.md` lists every URL and size, and each `ITEM.md` carries
  its own:

  ```bash
  python3 scripts/fetch_getlayers_free.py           # free tier → media/ (already committed)
  python3 scripts/fetch_getlayers.py --media video  # + mockups and preview clips
  python3 scripts/fetch_getlayers.py --media all    # + hero video and Lighthouse HTML
  ```

## How it was collected

`scripts/fetch_getlayers.py` reads the same public surfaces a browser reads:

1. The five catalogue pages — the React Server Component payload carries each whole catalogue as one
   `items` array. No private API, no scraping of rendered markup.
2. `https://www.getlayers.ai/layer/<id>` — the item page, for its JSON-LD (templates only; the other four
   libraries carry everything in the catalogue payload).
3. The **"Copy prompt" server actions** the pages themselves call, for free-tier items only.

No account was created, no paywall touched, no rate limit worked around. The collector is polite: a
descriptive User-Agent, retries with backoff, and it stops asking for a prompt the moment the site says no.

## Refresh

```bash
python3 scripts/fetch_getlayers.py                    # metadata + stills + free prompts
python3 scripts/fetch_getlayers.py --category gradient # one library only
python3 scripts/fetch_getlayers.py --media all        # + videos and Lighthouse reports
python3 scripts/fetch_getlayers_free.py               # free-tier media into media/
python3 scripts/build_source_indexes.py               # regenerate INDEX.md and MEDIA.md
python3 scripts/verify.py                             # counts, frontmatter, free/paid boundary
```
