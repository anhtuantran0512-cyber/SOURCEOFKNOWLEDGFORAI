#!/usr/bin/env python3
"""Build `sources/getlayers/gallery.html` — one offline page for the 47 free items.

The page embeds the inventory inline, so it opens straight from disk with no server
and no network: every poster, mockup and clip it plays is a file in
`sources/getlayers/media/`, and every item links to its brief and its live page.

Videos load lazily and only play while a card is hovered or focused; with
`prefers-reduced-motion` they stay on their poster.

Usage:
    python3 scripts/build_getlayers_gallery.py
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sources" / "getlayers"

CATEGORY_LABEL = {
    "template": "Template",
    "3d_scene": "3D scene",
    "background": "Background",
    "section": "Section",
    "gradient": "Gradient",
}

# Which file backs a card: the still for the poster, the smallest clip for the motion.
POSTER_FIELDS = ("image", "figmaPreview")
VIDEO_FIELDS = ("posterVideoPreview", "posterVideo", "previewVideo", "mockupDesktop")


def rel(path: str) -> str:
    """Inventory paths are repo-relative; the page sits in sources/getlayers/."""
    return path.split("sources/getlayers/", 1)[-1]


def pick(files: list[dict], fields: tuple[str, ...]) -> str | None:
    for field in fields:
        for entry in files:
            if entry["field"] == field and entry["status"] in ("ok", "cached"):
                return rel(entry["path"])
    return None


def build_data() -> dict:
    media = json.loads((OUT / "media-free.json").read_text(encoding="utf-8"))
    manifest = {row["id"]: row for row in json.loads((OUT / "manifest.json").read_text(encoding="utf-8"))}

    items = []
    for entry in media["entries"]:
        row = manifest.get(entry["id"], {})
        poster = pick(entry["files"], POSTER_FIELDS)
        video = pick(entry["files"], VIDEO_FIELDS)
        items.append(
            {
                "id": entry["id"],
                "title": entry["title"],
                "category": entry["category"],
                "tone": row.get("tone") or "",
                "stack": row.get("stack") or [],
                "tags": (row.get("tags") or [])[:4],
                "likes": row.get("likes") or 0,
                "description": row.get("description") or "",
                "poster": poster,
                "video": video,
                "bytes": entry["bytes"],
                "files": len(entry["files"]),
                "prompt": bool(row.get("prompt_path")),
            }
        )
    items.sort(key=lambda item: (item["category"] != "template", item["category"], item["title"]))
    return {
        "items": items,
        "totals": {
            "items": len(items),
            "files": media["files"],
            "bytes": media["bytes"],
            "prompts": sum(1 for item in items if item["prompt"]),
            "byCategory": {
                key: sum(1 for item in items if item["category"] == key) for key in CATEGORY_LABEL
            },
        },
    }


def build_html(data: dict) -> str:
    totals = data["totals"]
    chips = "".join(
        f'<button class="chip" data-filter="{key}" type="button">'
        f"{label}<span>{totals['byCategory'].get(key, 0)}</span></button>"
        for key, label in CATEGORY_LABEL.items()
        if totals["byCategory"].get(key)
    )
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>GetLayers — the 47 free items</title>
<style>
  :root {{
    --ink: #0b0c0d; --panel: #141618; --line: #26292c;
    --text: #eceeef; --muted: #9aa0a6; --accent: #d6f36b;
    --mono: ui-monospace, "SF Mono", "JetBrains Mono", Menlo, Consolas, monospace;
    --sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, Helvetica, Arial, sans-serif;
  }}
  * {{ box-sizing: border-box; }}
  html, body {{ margin: 0; background: var(--ink); color: var(--text); }}
  body {{ font-family: var(--sans); -webkit-font-smoothing: antialiased; }}
  a {{ color: inherit; }}
  .wrap {{ max-width: 1240px; margin: 0 auto; padding: 0 24px; }}

  header {{ border-bottom: 1px solid var(--line); }}
  .top {{ display: flex; flex-wrap: wrap; gap: 32px; align-items: flex-end; justify-content: space-between; padding: 56px 0 28px; }}
  .eyebrow {{ font-family: var(--mono); font-size: 11px; letter-spacing: .18em; text-transform: uppercase; color: var(--accent); }}
  h1 {{ font-size: clamp(30px, 5vw, 52px); line-height: 1.02; letter-spacing: -.03em; margin: 12px 0 0; font-weight: 500; }}
  h1 em {{ font-style: normal; color: var(--muted); }}
  .lede {{ max-width: 46ch; color: var(--muted); font-size: 14px; line-height: 1.6; margin: 14px 0 0; }}
  .stats {{ display: flex; gap: 26px; font-family: var(--mono); }}
  .stats div span {{ display: block; font-size: 11px; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); }}
  .stats div strong {{ font-size: 24px; font-weight: 500; letter-spacing: -.02em; }}

  .bar {{ position: sticky; top: 0; z-index: 5; background: color-mix(in srgb, var(--ink) 92%, transparent);
          backdrop-filter: blur(10px); border-bottom: 1px solid var(--line); }}
  .bar .wrap {{ display: flex; flex-wrap: wrap; gap: 10px; align-items: center; padding: 12px 24px; }}
  .chip {{ font-family: var(--mono); font-size: 12px; letter-spacing: .04em; color: var(--muted);
           background: transparent; border: 1px solid var(--line); border-radius: 999px;
           padding: 7px 13px; cursor: pointer; display: inline-flex; gap: 8px; align-items: center; }}
  .chip span {{ color: #6b7075; font-size: 10px; }}
  .chip:hover {{ color: var(--text); border-color: #3a3f44; }}
  .chip[aria-pressed="true"] {{ color: var(--ink); background: var(--accent); border-color: var(--accent); }}
  .chip[aria-pressed="true"] span {{ color: #4d5a12; }}
  .search {{ margin-left: auto; flex: 1 1 180px; max-width: 260px; }}
  .search input {{ width: 100%; background: var(--panel); border: 1px solid var(--line); border-radius: 8px;
                   color: var(--text); font-family: var(--mono); font-size: 12px; padding: 8px 11px; }}
  .search input:focus {{ outline: none; border-color: #4a5055; }}

  main {{ padding: 32px 0 72px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 18px; }}
  .card {{ background: var(--panel); border: 1px solid var(--line); border-radius: 14px; overflow: hidden;
           display: flex; flex-direction: column; }}
  .card:hover, .card:focus-within {{ border-color: #3a3f44; }}
  .card[hidden] {{ display: none; }}
  .frame {{ position: relative; aspect-ratio: 16 / 10; background: #0e1012; overflow: hidden; }}
  .frame img, .frame video {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }}
  .frame video {{ opacity: 0; transition: opacity .35s ease; }}
  .card:hover .frame video, .card:focus-within .frame video {{ opacity: 1; }}
  .badge {{ position: absolute; top: 10px; left: 10px; font-family: var(--mono); font-size: 10px;
            letter-spacing: .1em; text-transform: uppercase; padding: 4px 7px; border-radius: 4px;
            background: rgba(11,12,13,.72); color: #cfd3d6; border: 1px solid rgba(255,255,255,.08); }}
  .badge.free {{ background: var(--accent); color: #10120a; border-color: transparent; }}
  .body {{ padding: 14px 16px 16px; display: flex; flex-direction: column; gap: 8px; flex: 1; }}
  .name {{ font-size: 16px; font-weight: 500; letter-spacing: -.01em; margin: 0; display: flex;
           justify-content: space-between; gap: 10px; align-items: baseline; }}
  .name a {{ text-decoration: none; }}
  .name a:hover {{ text-decoration: underline; text-underline-offset: 3px; }}
  .likes {{ font-family: var(--mono); font-size: 11px; color: #6b7075; white-space: nowrap; }}
  .desc {{ color: var(--muted); font-size: 13px; line-height: 1.55; margin: 0;
           display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }}
  .meta {{ font-family: var(--mono); font-size: 10.5px; letter-spacing: .05em; color: #6b7075;
           margin-top: auto; padding-top: 6px; display: flex; flex-wrap: wrap; gap: 6px 10px; }}
  .meta i {{ font-style: normal; color: #8b9196; }}
  .links {{ display: flex; gap: 14px; font-family: var(--mono); font-size: 11px; padding-top: 4px; }}
  .links a {{ color: var(--muted); text-decoration: none; border-bottom: 1px solid transparent; }}
  .links a:hover {{ color: var(--accent); border-color: var(--accent); }}

  footer {{ border-top: 1px solid var(--line); padding: 26px 0 60px; color: #6b7075; font-size: 12px; line-height: 1.7; }}
  footer a {{ color: var(--muted); }}
  .empty {{ color: var(--muted); font-family: var(--mono); font-size: 13px; padding: 40px 0; }}
  @media (prefers-reduced-motion: reduce) {{
    .frame video {{ display: none; }}
    * {{ transition: none !important; }}
  }}
</style>
</head>
<body>
<header>
  <div class="wrap top">
    <div>
      <p class="eyebrow">GetLayers · free tier</p>
      <h1>Forty-seven items,<br><em>every file kept.</em></h1>
      <p class="lede">The free half of five GetLayers libraries — templates, 3D scenes and animated
        backgrounds — with the motion, mockups and Lighthouse reports the site publishes for them.</p>
    </div>
    <div class="stats">
      <div><span>items</span><strong>{totals['items']}</strong></div>
      <div><span>files</span><strong>{totals['files']}</strong></div>
      <div><span>prompts</span><strong>{totals['prompts']}</strong></div>
      <div><span>size</span><strong>{totals['bytes'] / 1e9:.2f} GB</strong></div>
    </div>
  </div>
</header>

<div class="bar">
  <div class="wrap">
    <button class="chip" data-filter="all" type="button" aria-pressed="true">All<span>{totals['items']}</span></button>
    {chips}
    <label class="search"><input id="q" type="search" placeholder="search title, tag, stack…" aria-label="Search items"></label>
  </div>
</div>

<main class="wrap">
  <div class="grid" id="grid"></div>
  <p class="empty" id="empty" hidden>Nothing matches that filter.</p>
</main>

<footer class="wrap">
  Every file here is published free on <a href="https://www.getlayers.ai">getlayers.ai</a> and belongs to
  GetLayers / Textura — see <a href="../../NOTICE.md">NOTICE.md</a>. The 845 premium items and their
  prompts are not included. Briefs live in <a href="INDEX.md">INDEX.md</a>; every URL and size, free or
  not, is in <a href="MEDIA.md">MEDIA.md</a>.
</footer>

<script type="application/json" id="data">{payload}</script>
<script>
const DATA = JSON.parse(document.getElementById("data").textContent);
const LABEL = {{template:"Template","3d_scene":"3D scene",background:"Background",section:"Section",gradient:"Gradient"}};
const kb = n => n > 1e6 ? (n / 1e6).toFixed(1) + " MB" : Math.round(n / 1e3) + " KB";
const esc = s => String(s).replace(/[&<>"]/g, c => ({{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}})[c]);

const grid = document.getElementById("grid");
const empty = document.getElementById("empty");
const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;

const cards = DATA.items.map(item => {{
  const el = document.createElement("article");
  el.className = "card";
  el.dataset.category = item.category;
  el.dataset.search = [item.title, item.id, item.category, item.tone, item.description,
                       ...(item.stack || []), ...(item.tags || [])].join(" ").toLowerCase();
  el.innerHTML = `
    <div class="frame">
      ${{item.poster ? `<img src="${{esc(item.poster)}}" alt="" loading="lazy" decoding="async">` : ""}}
      ${{item.video && !reduced ? `<video src="${{esc(item.video)}}" muted loop playsinline preload="none"></video>` : ""}}
      <span class="badge">${{LABEL[item.category] || item.category}}</span>
      ${{item.prompt ? `<span class="badge free" style="left:auto;right:10px">prompt</span>` : ""}}
    </div>
    <div class="body">
      <h2 class="name"><a href="items/${{esc(item.id)}}/ITEM.md">${{esc(item.title)}}</a>
        <span class="likes">♥ ${{item.likes}}</span></h2>
      <p class="desc">${{esc(item.description)}}</p>
      <div class="meta">
        <span><i>${{item.files}}</i> files</span><span><i>${{kb(item.bytes)}}</i></span>
        ${{item.tone ? `<span><i>${{esc(item.tone)}}</i></span>` : ""}}
        ${{(item.stack || []).slice(0, 3).map(s => `<span>${{esc(s)}}</span>`).join("")}}
      </div>
      <div class="links">
        <a href="items/${{esc(item.id)}}/ITEM.md">brief</a>
        ${{item.prompt ? `<a href="prompts/${{esc(item.id)}}.md">prompt</a>` : ""}}
        <a href="https://www.getlayers.ai/layer/${{esc(item.id)}}" rel="noopener">live ↗</a>
      </div>
    </div>`;
  const video = el.querySelector("video");
  if (video) {{
    const play = () => {{ video.play().catch(() => {{}}); }};
    const stop = () => {{ video.pause(); video.currentTime = 0; }};
    el.addEventListener("mouseenter", play);
    el.addEventListener("mouseleave", stop);
    el.addEventListener("focusin", play);
    el.addEventListener("focusout", stop);
  }}
  return el;
}});
cards.forEach(card => grid.appendChild(card));

let filter = "all";
const apply = () => {{
  const term = document.getElementById("q").value.trim().toLowerCase();
  let shown = 0;
  cards.forEach(card => {{
    const ok = (filter === "all" || card.dataset.category === filter) &&
               (!term || card.dataset.search.includes(term));
    card.hidden = !ok;
    if (ok) shown++;
  }});
  empty.hidden = shown > 0;
}};
document.querySelectorAll(".chip").forEach(chip => {{
  chip.addEventListener("click", () => {{
    filter = chip.dataset.filter;
    document.querySelectorAll(".chip").forEach(other => other.setAttribute("aria-pressed", String(other === chip)));
    apply();
  }});
}});
document.getElementById("q").addEventListener("input", apply);
</script>
</body>
</html>
"""


def main() -> int:
    data = build_data()
    path = OUT / "gallery.html"
    path.write_text(build_html(data), encoding="utf-8")
    print(
        f"{path.relative_to(ROOT)} · items={data['totals']['items']} "
        f"files={data['totals']['files']} prompts={data['totals']['prompts']} "
        f"size={path.stat().st_size / 1e3:.1f} kB",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
