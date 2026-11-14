# Scripts

Python 3.10+, standard library plus `httpx`. No API keys required: the collectors use the same public
endpoints the websites use in a browser.

| Script | Purpose |
|---|---|
| `crawl_codefronts.py` | Reads `sitemap-0.xml`, extracts the AI prompt and metadata from each component page, writes one markdown file per item and rebuilds `manifest.json`. |
| `fetch_lucian.py` | Reads the catalog + preview JSON bundles, localises Korean copy to English, writes 400 prompts, 400 standalone demos and `tokens.css`. |
| `fetch_motionsites.py` | Reads the public catalogue, fetches **only** `is_free = true` prompts, writes markdown files. Paid prompts are never requested. |
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
