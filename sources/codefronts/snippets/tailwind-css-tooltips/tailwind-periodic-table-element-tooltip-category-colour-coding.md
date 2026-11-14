---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-periodic-table-element-tooltip-category-colour-coding/"
title: "Tailwind Periodic Table Element Tooltip with Category Colour Coding"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "Ten element tiles colour-coded by category, each opening a card with symbol, category badge, atomic data, electron configuration and a discovery line."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Periodic Table Element Tooltip with Category Colour Coding
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-periodic-table-element-tooltip-category-colour-coding/

Ten element tiles colour-coded by category, each opening a card with symbol, category badge, atomic data, electron configuration and a discovery line. Six categories &times; three colour roles is exactly the case for a per-tile variable: [--el:#3ca03c] paints tile, border and badge from one place.
## HTML
```html
<section class="ttp-16 w-full min-h-svh bg-ttp16-bg px-7 pt-[260px] pb-10 font-ttp16-mono">
  <div class="mx-auto flex max-w-[660px] flex-col items-center gap-1.25">

    <div class="flex gap-1.25">
      <div class="group relative shrink-0">
        <button type="button" aria-describedby="ttp16-e1" class="ttp16-tile [--el:#3ca03c]"><span class="ttp16-num">1</span><span class="ttp16-sym">H</span><span class="ttp16-ename">Hydrogen</span><span class="ttp16-mass">1.008</span></button>
        <div id="ttp16-e1" role="tooltip" class="ttp16-card">
          <div class="ttp16-ctop"><div class="ttp16-csym">H</div><div class="ttp16-cname">Hydrogen</div><span class="ttp16-cat [--el:#3ca03c]">Reactive Nonmetal</span></div>
          <div class="px-3.25 py-2.25"><div class="ttp16-row"><span class="ttp16-key">Atomic No.</span><span class="ttp16-val">1</span></div><div class="ttp16-row"><span class="ttp16-key">Atomic Mass</span><span class="ttp16-val">1.008 u</span></div><div class="ttp16-row"><span class="ttp16-key">Config</span><span class="ttp16-cfg">1s¹</span></div><div class="ttp16-row"><span class="ttp16-key">State (25°C)</span><span class="ttp16-val">Gas</span></div><div class="ttp16-row"><span class="ttp16-key">Boiling pt.</span><span class="ttp16-val">−252.9 °C</span></div></div>
          <div class="ttp16-disc">Discovered 1766 · Henry Cavendish</div>
        </div>
      </div>
      <div class="h-14 w-[380px] shrink-0" aria-hidden="true"></div>
      <div class="group relative shrink-0">
        <button type="button" aria-describedby="ttp16-e2" class="ttp16-tile [--el:#a03cc8]"><span class="ttp16-num">2</span><span class="ttp16-sym">He</span><span class="ttp16-ename">Helium</span><span class="ttp16-mass">4.003</span></button>
        <div id="ttp16-e2" role="tooltip" class="ttp16-card">
          <div class="ttp16-ctop"><div class="ttp16-csym">He</div><div class="ttp16-cname">Helium</div><span class="ttp16-cat [--el:#a03cc8]">Noble Gas</span></div>
          <div class="px-3.25 py-2.25"><div class="ttp16-row"><span class="ttp16-key">Atomic No.</span><span class="ttp16-val">2</span></div><div class="ttp16-row"><span class="ttp16-key">Atomic Mass</span><span class="ttp16-val">4.003 u</span></div><div class="ttp16-row"><span class="ttp16-key">Config</span><span class="ttp16-cfg">1s²</span></div><div class="ttp16-row"><span class="ttp16-key">Boiling pt.</span><span class="ttp16-val">−268.9 °C</span></div></div>
          <div class="ttp16-disc">Discovered 1895 · Ramsay, Clève, Langlet</div>
        </div>
      </div>
    </div>

    <div class="flex gap-1.25">
      <div class="group relative shrink-0">
        <button type="button" aria-describedby="ttp16-e3" class="ttp16-tile [--el:#e06050]"><span class="ttp16-num">3</span><span class="ttp16-sym">Li</span><span class="ttp16-ename">Lithium</span><span class="ttp16-mass">6.941</span></button>
        <div id="ttp16-e3" role="tooltip" class="ttp16-card">
          <div class="ttp16-ctop"><div class="ttp16-csym">Li</div><div class="ttp16-cname">Lithium</div><span class="ttp16-cat [--el:#e06050]">Alkali Metal</span></div>
          <div class="px-3.25 py-2.25"><div class="ttp16-row"><span class="ttp16-key">Atomic No.</span><span class="ttp16-val">3</span></div><div class="ttp16-row"><span class="ttp16-key">Config</span><span class="ttp16-cfg">[He] 2s¹</span></div><div class="ttp16-row"><span class="ttp16-key">Melting pt.</span><span class="ttp16-val">180.5 °C</span></div><div class="ttp16-row"><span class="ttp16-key">Use</span><span class="ttp16-val">Batteries, ceramics</span></div></div>
          <div class="ttp16-disc">Discovered 1817 · J. A. Arfwedson</div>
        </div>
      </div>
      <div class="group relative shrink-0">
        <button type="button" aria-describedby="ttp16-e4" class="ttp16-tile [--el:#d0a030]"><span class="ttp16-num">4</span><span class="ttp16-sym">Be</span><span class="ttp16-ename">Beryllium</span><span class="ttp16-mass">9.012</span></button>
        <div id="ttp16-e4" role="tooltip" class="ttp16-card">
          <div class="ttp16-ctop"><div class="ttp16-csym">Be</div><div class="ttp16-cname">Beryllium</div><span class="ttp16-cat [--el:#d0a030]">Alkaline Earth</span></div>
          <div class="px-3.25 py-2.25"><div class="ttp16-row"><span class="ttp16-key">Atomic No.</span><span class="ttp16-val">4</span></div><div class="ttp16-row"><span class="ttp16-key">Config</span><span class="ttp16-cfg">[He] 2s²</span></div><div class="ttp16-row"><span class="ttp16-key">Melting pt.</span><span class="ttp16-val">1,287 °C</span></div><div class="ttp16-row"><span class="ttp16-key">Note</span><span class="ttp16-val">Highly toxic dust</span></div></div>
          <div class="ttp16-disc">Discovered 1798 · L.-N. Vauquelin</div>
        </div>
      </div>
      <div class="h-14 w-[300px] shrink-0" aria-hidden="true"></div>
      <div class="group relative shrink-0">
        <button type="button" aria-describedby="ttp16-e5" class="ttp16-tile [--el:#40c0e0]"><span class="ttp16-num">5</span><span class="ttp16-sym">B</span><span class="ttp16-ename">Boron</span><span class="ttp16-mass">10.81</span></button>
        <div id="ttp16-e5" role="tooltip" class="ttp16-card">
          <div class="ttp16-ctop"><div class="ttp16-csym">B</div><div class="ttp16-cname">Boron</div><span class="ttp16-cat [--el:#40c0e0]">Metalloid</span></div>
          <div class="px-3.25 py-2.25"><div class="ttp16-row"><span class="ttp16-key">Config</span><span class="ttp16-cfg">[He] 2s² 2p¹</span></div><div class="ttp16-row"><span class="ttp16-key">Melting pt.</span><span class="ttp16-val">2,076 °C</span></div></div>
          <div class="ttp16-disc">Discovered 1808 · Gay-Lussac, Davy</div>
        </div>
      </div>
      <div class="group relative shrink-0">
        <button type="button" aria-describedby="ttp16-e6" class="ttp16-tile [--el:#3ca03c]"><span class="ttp16-num">6</span><span class="ttp16-sym">C</span><span class="ttp16-ename">Carbon</span><span class="ttp16-mass">12.01</span></button>
        <div id="ttp16-e6" role="tooltip" class="ttp16-card">
          <div class="ttp16-ctop"><div class="ttp16-csym">C</div><div class="ttp16-cname">Carbon</div><span class="ttp16-cat [--el:#3ca03c]">Reactive Nonmetal</span></div>
          <div class="px-3.25 py-2.25"><div class="ttp16-row"><span class="ttp16-key">Config</span><span class="ttp16-cfg">[He] 2s² 2p²</span></div><div class="ttp16-row"><span class="ttp16-key">Allotropes</span><span class="ttp16-val">Diamond, graphite</span></div><div class="ttp16-row"><span class="ttp16-key">Sublimation</span><span class="ttp16-val">3,642 °C</span></div></div>
          <div class="ttp16-disc">Known since antiquity</div>
        </div>
      </div>
      <div class="group relative shrink-0">
        <button type="button" aria-describedby="ttp16-e7" class="ttp16-tile [--el:#3ca03c]"><span class="ttp16-num">7</span><span class="ttp16-sym">N</span><span class="ttp16-ename">Nitrogen</span><span class="ttp16-mass">14.01</span></button>
        <div id="ttp16-e7" role="tooltip" class="ttp16-card">
          <div class="ttp16-ctop"><div class="ttp16-csym">N</div><div class="ttp16-cname">Nitrogen</div><span class="ttp16-cat [--el:#3ca03c]">Reactive Nonmetal</span></div>
          <div class="px-3.25 py-2.25"><div class="ttp16-row"><span class="ttp16-key">Config</span><span class="ttp16-cfg">[He] 2s² 2p³</span></div><div class="ttp16-row"><span class="ttp16-key">Boiling pt.</span><span class="ttp16-val">−195.8 °C</span></div><div class="ttp16-row"><span class="ttp16-key">Atmosphere</span><span class="ttp16-val">78% of air</span></div></div>
          <div class="ttp16-disc">Discovered 1772 · Daniel Rutherford</div>
        </div>
      </div>
      <div class="group relative shrink-0">
        <button type="button" aria-describedby="ttp16-e8" class="ttp16-tile [--el:#3ca03c]"><span class="ttp16-num">8</span><span class="ttp16-sym">O</span><span class="ttp16-ename">Oxygen</span><span class="ttp16-mass">16.00</span></button>
        <div id="ttp16-e8" role="tooltip" class="ttp16-card">
          <div class="ttp16-ctop"><div class="ttp16-csym">O</div><div class="ttp16-cname">Oxygen</div><span class="ttp16-cat [--el:#3ca03c]">Reactive Nonmetal</span></div>
          <div class="px-3.25 py-2.25"><div class="ttp16-row"><span class="ttp16-key">Config</span><span class="ttp16-cfg">[He] 2s² 2p⁴</span></div><div class="ttp16-row"><span class="ttp16-key">Boiling pt.</span><span class="ttp16-val">−183 °C</span></div></div>
          <div class="ttp16-disc">Discovered 1771 · C. W. Scheele</div>
        </div>
      </div>
      <div class="group relative shrink-0">
        <button type="button" aria-describedby="ttp16-e9" class="ttp16-tile [--el:#c8c830]"><span class="ttp16-num">9</span><span class="ttp16-sym">F</span><span class="ttp16-ename">Fluorine</span><span class="ttp16-mass">19.00</span></button>
        <div id="ttp16-e9" role="tooltip" class="ttp16-card">
          <div class="ttp16-ctop"><div class="ttp16-csym">F</div><div class="ttp16-cname">Fluorine</div><span class="ttp16-cat [--el:#c8c830]">Halogen</span></div>
          <div class="px-3.25 py-2.25"><div class="ttp16-row"><span class="ttp16-key">Config</span><span class="ttp16-cfg">[He] 2s² 2p⁵</span></div><div class="ttp16-row"><span class="ttp16-key">Electronegativity</span><span class="ttp16-val">3.98 (highest)</span></div><div class="ttp16-row"><span class="ttp16-key">Boiling pt.</span><span class="ttp16-val">−188 °C</span></div></div>
          <div class="ttp16-disc">Isolated 1886 · Henri Moissan</div>
        </div>
      </div>
      <div class="group relative shrink-0">
        <button type="button" aria-describedby="ttp16-e10" class="ttp16-tile [--el:#a03cc8]"><span class="ttp16-num">10</span><span class="ttp16-sym">Ne</span><span class="ttp16-ename">Neon</span><span class="ttp16-mass">20.18</span></button>
        <div id="ttp16-e10" role="tooltip" class="ttp16-card">
          <div class="ttp16-ctop"><div class="ttp16-csym">Ne</div><div class="ttp16-cname">Neon</div><span class="ttp16-cat [--el:#a03cc8]">Noble Gas</span></div>
          <div class="px-3.25 py-2.25"><div class="ttp16-row"><span class="ttp16-key">Config</span><span class="ttp16-cfg">[He] 2s² 2p⁶</span></div><div class="ttp16-row"><span class="ttp16-key">Boiling pt.</span><span class="ttp16-val">−246.1 °C</span></div><div class="ttp16-row"><span class="ttp16-key">Emission</span><span class="ttp16-val">Red-orange glow</span></div></div>
          <div class="ttp16-disc">Discovered 1898 · Ramsay &amp; Travers</div>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttp16-bg: #0d0d10;
  --color-ttp16-bg: oklch(0.16 0.005 285);
  --color-ttp16-card: #141418;
  --color-ttp16-card: oklch(0.19 0.005 285);
  --color-ttp16-bright: #f2f2f5;
  --color-ttp16-bright: oklch(0.96 0.002 285);
  --color-ttp16-ink: #c0c0c8;
  --color-ttp16-ink: oklch(0.81 0.005 285);
  --color-ttp16-dim: #9a9aa4;
  --color-ttp16-dim: oklch(0.68 0.006 285);
  --font-ttp16-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.ttp-16 {
  width: 100%;
  min-height: 100svh;
}
/* Six categories, one variable. The tile tint, its border and the
   card's badge all read var(--el), so a category is one utility. */

.ttp-16 .ttp16-tile {
  @apply relative flex h-14 w-14 shrink-0 cursor-help flex-col items-start rounded px-1.5 py-1.25 border border-[var(--el)]/40 bg-[var(--el)]/18 text-left transition-transform duration-150 group-hover:scale-[1.08] group-hover:-translate-y-0.5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--el)];
}

.ttp-16 .ttp16-num {
  @apply text-[8.5px] text-ttp16-dim;
}

.ttp-16 .ttp16-sym {
  @apply my-px text-[19px] font-semibold leading-none text-ttp16-bright;
}

.ttp-16 .ttp16-ename {
  @apply w-full truncate text-[7.5px] text-ttp16-dim;
}

.ttp-16 .ttp16-mass {
  @apply text-[7.5px] text-ttp16-dim;
}

.ttp-16 .ttp16-card {
  @apply pointer-events-none invisible absolute bottom-[calc(100%+10px)] left-1/2 z-300 w-55 max-w-[calc(100vw-48px)] -translate-x-1/2 -translate-y-1.5 overflow-hidden rounded-lg border border-white/10 bg-ttp16-card text-left opacity-0 shadow-[0_16px_44px_rgba(0,0,0,0.95)] transition-[opacity,translate,visibility] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:visible group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:visible group-focus-within:translate-y-0 group-focus-within:opacity-100;
}

.ttp-16 .ttp16-ctop {
  @apply border-b border-white/8 px-3.25 pt-2.75 pb-2.25;
}

.ttp-16 .ttp16-csym {
  @apply text-2xl font-semibold leading-none text-ttp16-bright;
}

.ttp-16 .ttp16-cname {
  @apply mt-0.5 text-[13px] text-ttp16-ink;
}

.ttp-16 .ttp16-cat {
  @apply mt-1.5 inline-block rounded-[3px] border border-[var(--el)]/40 bg-[var(--el)]/15 px-1.5 py-0.5 text-[8.5px] uppercase tracking-[0.07em] text-[var(--el)];
}

.ttp-16 .ttp16-row {
  @apply mb-1.25 flex justify-between gap-3;
}

.ttp-16 .ttp16-key {
  @apply text-[8.5px] tracking-[0.08em] text-ttp16-dim;
}

.ttp-16 .ttp16-val {
  @apply text-[9.5px] italic text-ttp16-ink;
}

.ttp-16 .ttp16-cfg {
  @apply text-[9px] tracking-[0.04em] text-ttp16-ink;
}

.ttp-16 .ttp16-disc {
  @apply border-t border-white/6 px-3.25 py-2 text-[9px] tracking-[0.04em] text-ttp16-dim;
}
```
