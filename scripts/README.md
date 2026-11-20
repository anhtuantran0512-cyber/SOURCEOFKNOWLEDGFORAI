# Scripts

Python 3.10+, standard library plus `httpx`. No API keys required: the collectors use the same public
endpoints the websites use in a browser.

| Script | Purpose |
|---|---|
| `crawl_codefronts.py` | Reads `sitemap-0.xml`, extracts the AI prompt and metadata from each component page, writes one markdown file per item and rebuilds `manifest.json`. |
| `fetch_lucian.py` | Reads the catalog + preview JSON bundles, localises Korean copy to English, writes 400 prompts, 400 standalone demos and `tokens.css`. |
| `fetch_motionsites.py` | Reads the public catalogue, fetches **only** `is_free = true` prompts, writes markdown files. Paid prompts are never requested. |
| `fetch_getlayers.py` | Reads the five catalogue pages (templates, 3D scenes, sections, backgrounds, gradients) for all 892 items, each template's `/layer/<id>` page for its JSON-LD, downloads poster and Figma stills, and calls the public copy-prompt actions for **free-tier items only**. Premium answers `forbidden` and is never retried. `--media video|all` also fetches mp4s and Lighthouse HTML. |
| `fetch_getlayers_free.py` | Streams every media file of the 47 free GetLayers items into `sources/getlayers/media/<id>/` and records them in `media-free.json`. Resumable, skips anything premium. |
| `build_index.py` | Regenerates `INDEX.md`, per-source `README.md` files and `catalog.json`. |
| `verify.py` | Validates counts, files, frontmatter, demos and the free/paid boundary. |

## Usage

```bash
# CodeFronts — resumable
python3 scripts/crawl_codefronts.py --resume --concurrency 12

# lucianLabs — fast, ~5s
python3 scripts/fetch_lucian.py

# MotionSites — concurrency, optional limit for a test run
python3 scripts/fetch_motionsites.py 4
python3 scripts/fetch_motionsites.py 4 5   # only 5 free prompts

# GetLayers — stills + free prompts; --media all adds the mp4 mockups and Lighthouse HTML
python3 scripts/fetch_getlayers.py
python3 scripts/fetch_getlayers.py --category gradient      # one library only
python3 scripts/fetch_getlayers.py --media all
python3 scripts/fetch_getlayers.py --cookie-file ~/gl-cookies.txt   # signed-in run, all 18 free prompts

# GetLayers free-tier media — 232 files, 595 MB, resumable
python3 scripts/fetch_getlayers_free.py

# Rebuild + verify
python3 scripts/build_index.py
python3 scripts/verify.py
```

## Notes

- `crawl_codefronts.py` appends to `_manifest.jsonl` as a checkpoint. Do not delete it mid-run; it is the
  resume log and is git-ignored.
- The collectors are polite: bounded concurrency, retries with backoff, a descriptive User-Agent.
- Re-running a collector overwrites files for the same item. Counts in `manifest.json` always reflect the
  last completed run.
- If a site changes its markup, `verify.py` will flag missing or short files before you commit.
- `fetch_getlayers.py` copies free prompts through the site's public copy action, which allows **one
  prompt per anonymous visitor per day**. Re-run on a later day, or pass your own signed-in cookie,
  to finish the set. It never creates an account and never retries after a refusal.
