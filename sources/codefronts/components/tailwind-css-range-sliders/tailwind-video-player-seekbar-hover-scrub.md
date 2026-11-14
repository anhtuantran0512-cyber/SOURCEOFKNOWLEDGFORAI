---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-range-sliders/tailwind-video-player-seekbar-hover-scrub/"
title: "Tailwind CSS Video Player Seekbar with Hover Scrub & Chapters"
section: "components"
category: "tailwind-css-range-sliders"
category_name: "Tailwind CSS Range Sliders"
description: "The streaming seekbar: a hairline track that thickens on hover, a thumb that blooms out of nothing, a buffer layer, chapter markers and a timecode tooltip…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Video Player Seekbar with Hover Scrub & Chapters
Source: https://codefronts.com/components/tailwind-css-range-sliders/tailwind-video-player-seekbar-hover-scrub/

The streaming seekbar: a hairline track that thickens on hover, a thumb that blooms out of nothing, a buffer layer, chapter markers and a timecode tooltip that follows the pointer rather than the value. The port replaces a hover-state CSS block with group-hover:/group-focus-within: utilities and one --scrub property.
## HTML
```html
<section class="trs-06 w-full min-h-svh grid place-items-center bg-trs06-bg font-trs06-sans px-5 py-10" id="trs-06-root" style="--v:.32;--scrub:.32;--buf:.6">
  <div class="w-[min(560px,100%)] rounded-xl bg-trs06-panel overflow-hidden shadow-[0_24px_60px_-24px_oklch(0_0_0/0.9)]">
    <div class="relative aspect-video grid place-items-center bg-[radial-gradient(ellipse_at_center,oklch(0.35_0.16_25/0.25),transparent_62%),linear-gradient(135deg,#0d0d0d,#2b0406_65%,#0d0d0d)]">
      <button type="button" aria-label="Play Neon Horizon" class="grid place-items-center size-16 rounded-full bg-trs06-red/85 shadow-[0_0_40px_-6px_var(--color-trs06-red)] transition-[scale,background-color] duration-200 hover:scale-108 hover:bg-trs06-red focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white motion-reduce:hover:scale-100">
        <svg viewBox="0 0 24 24" class="size-6 fill-white ml-1"><polygon points="5,3 19,12 5,21"/></svg>
      </button>
      <div class="absolute bottom-4 left-5">
        <div class="text-xl font-bold text-white drop-shadow-[0_2px_12px_oklch(0_0_0/0.8)]">Neon Horizon</div>
        <div class="text-xs text-trs06-mut">2024 · Drama · 2h 07m</div>
      </div>
    </div>

    <div class="px-4 pt-3 pb-4">
      <div class="group/seek relative h-5 flex items-center cursor-pointer" id="trs-06-seek">
        <div class="absolute inset-x-0 h-1 rounded-full bg-white/20 transition-[height] duration-150 group-hover/seek:h-1.5 motion-reduce:transition-none"></div>
        <div class="absolute left-0 h-1 rounded-full bg-white/35 w-[calc(var(--buf)*100%)] transition-[height] duration-150 group-hover/seek:h-1.5 motion-reduce:transition-none" aria-hidden="true"></div>
        <div class="absolute left-0 h-1 rounded-full bg-white/25 w-[calc(var(--scrub)*100%)] opacity-0 transition-opacity duration-150 group-hover/seek:opacity-100 motion-reduce:transition-none" aria-hidden="true"></div>
        <div class="absolute left-0 h-1 rounded-full bg-trs06-mut w-[calc(var(--v)*100%)] transition-[background-color,height] duration-150 group-hover/seek:bg-trs06-red group-hover/seek:h-1.5 group-focus-within/seek:bg-trs06-red motion-reduce:transition-none"></div>

        <div class="absolute inset-x-0 h-5 pointer-events-none" id="trs-06-chapters" aria-hidden="true"></div>

        <input type="range" min="0" max="7620" value="2438" id="trs-06-inp" aria-label="Seek video"
               class="absolute inset-0 w-full h-5 appearance-none bg-transparent outline-none cursor-pointer z-10 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white rounded-full">

        <span aria-hidden="true" class="absolute top-1/2 left-[calc(var(--v)*100%)] size-3.5 rounded-full bg-white shadow-[0_2px_8px_oklch(0_0_0/0.6)] -translate-x-1/2 -translate-y-1/2 scale-0 opacity-0 transition-[scale,opacity] duration-200 group-hover/seek:scale-100 group-hover/seek:opacity-100 group-focus-within/seek:scale-100 group-focus-within/seek:opacity-100 motion-reduce:transition-none"></span>
        <span aria-hidden="true" class="absolute bottom-[calc(100%_+_8px)] left-[calc(var(--scrub)*100%)] -translate-x-1/2 rounded-md bg-black/80 backdrop-blur-sm px-2 py-1 font-trs06-mono text-[11px] font-medium text-white whitespace-nowrap opacity-0 transition-opacity duration-150 group-hover/seek:opacity-100 group-focus-within/seek:opacity-100 motion-reduce:transition-none" id="trs-06-tip">0:40:38</span>
      </div>

      <div class="flex items-center justify-between gap-3 mt-2.5">
        <div class="flex items-center gap-2.5">
          <button type="button" aria-label="Play" class="grid place-items-center min-h-11 min-w-11 rounded-lg text-white/80 transition-colors duration-150 hover:text-white hover:bg-white/10 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">
            <svg viewBox="0 0 24 24" class="size-5 fill-current"><polygon points="5,3 19,12 5,21"/></svg>
          </button>
          <button type="button" aria-label="Next episode" class="grid place-items-center min-h-11 min-w-11 rounded-lg text-white/80 transition-colors duration-150 hover:text-white hover:bg-white/10 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">
            <svg viewBox="0 0 24 24" class="size-5 fill-current"><polygon points="5,4 15,12 5,20"/><rect x="17" y="4" width="2" height="16"/></svg>
          </button>
          <div class="flex items-center gap-1.5">
            <span class="grid place-items-center size-6 text-white/80"><svg viewBox="0 0 24 24" class="size-5 fill-current"><polygon points="11,5 6,9 2,9 2,15 6,15 11,19"/></svg></span>
            <input type="range" min="0" max="100" value="80" aria-label="Volume" class="w-16 h-[3px] appearance-none rounded-full bg-white/30 outline-none cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white" id="trs-06-vol">
          </div>
          <p class="font-trs06-mono text-xs text-trs06-mut tabular-nums m-0"><span class="text-white" id="trs-06-cur">0:40:38</span> / 2:07:00</p>
        </div>
        <button type="button" aria-label="Full screen" class="grid place-items-center min-h-11 min-w-11 rounded-lg text-white/80 transition-colors duration-150 hover:text-white hover:bg-white/10 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">
          <svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2"><polyline points="15,3 21,3 21,9"/><polyline points="9,21 3,21 3,15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg>
        </button>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trs06-bg: #141414;
  --color-trs06-bg: oklch(0.18 0 0);
  --color-trs06-panel: #1f1f1f;
  --color-trs06-panel: oklch(0.24 0 0);
  --color-trs06-red: #e50914;
  --color-trs06-red: oklch(0.55 0.23 25);
  --color-trs06-mut: #9a9a9a;
  --color-trs06-mut: oklch(0.68 0 0);
  --font-trs06-sans: 'DM Sans', system-ui, sans-serif;
  --font-trs06-mono: 'JetBrains Mono', ui-monospace, monospace;
}

@property --v {
  syntax: "<number>";
  inherits: true;
  initial-value: 0.32;
}

@property --scrub {
  syntax: "<number>";
  inherits: true;
  initial-value: 0.32;
}

@property --buf {
  syntax: "<number>";
  inherits: true;
  initial-value: 0.6;
}

.trs-06 {
  width: 100%;
  min-height: 100svh;
}
/* The seek thumb is a utility-styled span, so the native thumb is a
   transparent hit target; the volume slider keeps a visible one. */

.trs-06 #trs-06-inp::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 18px;
  height: 18px;
  background: transparent;
}

.trs-06 #trs-06-inp::-moz-range-thumb {
  width: 18px;
  height: 18px;
  border: 0;
  background: transparent;
}

.trs-06 #trs-06-vol::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 11px;
  height: 11px;
  border-radius: 9999px;
  background: #fff;
}

.trs-06 #trs-06-vol::-moz-range-thumb {
  width: 11px;
  height: 11px;
  border: 0;
  border-radius: 9999px;
  background: #fff;
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('trs-06-root');
  var seek = document.getElementById('trs-06-seek');
  var inp = document.getElementById('trs-06-inp');
  var tip = document.getElementById('trs-06-tip');
  var cur = document.getElementById('trs-06-cur');
  var chaptersEl = document.getElementById('trs-06-chapters');
  var DUR = +inp.max;
  var CHAPTERS = [
    { at: 0, label: 'Cold open' }, { at: 900, label: 'The offer' },
    { at: 2400, label: 'Night drive' }, { at: 4200, label: 'The fall' },
    { at: 6300, label: 'Horizon' }
  ];

  CHAPTERS.forEach(function(c){
    var t = document.createElement('span');
    t.className = 'absolute top-1/2 -translate-y-1/2 w-0.5 h-2.5 rounded-full bg-black/55 left-[calc(var(--at)*100%)]';
    t.style.setProperty('--at', c.at / DUR);
    t.title = c.label;
    chaptersEl.appendChild(t);
  });

  function fmt(s){
    s = Math.floor(s);
    var h = Math.floor(s / 3600), m = Math.floor(s % 3600 / 60), sec = s % 60;
    var mm = (h && m < 10 ? '0' : '') + m;
    return (h ? h + ':' : '0:') + mm + ':' + (sec < 10 ? '0' : '') + sec;
  }
  function chapterAt(s){
    var name = CHAPTERS[0].label;
    CHAPTERS.forEach(function(c){ if (s >= c.at) name = c.label; });
    return name;
  }
  function update(){
    var v = +inp.value, f = v / DUR;
    root.style.setProperty('--v', f);
    root.style.setProperty('--scrub', f);
    cur.textContent = fmt(v);
    tip.textContent = fmt(v);
    inp.setAttribute('aria-valuetext', fmt(v) + ' of ' + fmt(DUR) + ', ' + chapterAt(v));
  }
  seek.addEventListener('pointermove', function(e){
    var r = seek.getBoundingClientRect();
    var f = Math.min(1, Math.max(0, (e.clientX - r.left) / r.width));
    root.style.setProperty('--scrub', f);
    tip.textContent = fmt(f * DUR) + ' · ' + chapterAt(f * DUR);
  });
  seek.addEventListener('pointerleave', function(){
    root.style.setProperty('--scrub', +inp.value / DUR);
    tip.textContent = fmt(+inp.value);
  });
  inp.addEventListener('input', update);
  update();
})();
```
