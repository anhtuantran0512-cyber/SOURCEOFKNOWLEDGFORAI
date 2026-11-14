---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-dithering-patterns-with-gradients/"
title: "Tailwind Dithering Patterns with Gradients"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "Ordered dithering is how a limited palette fakes colours it does not have: alternate two available colours in a fixed pattern and the eye averages them."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dithering Patterns with Gradients
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-dithering-patterns-with-gradients/

Ordered dithering is how a limited palette fakes colours it does not have: alternate two available colours in a fixed pattern and the eye averages them. Built from layered repeating-conic-gradient checkerboards over flat palette fills &mdash; and because every pattern is an arbitrary background utility, each band's coverage is legible in the markup instead of hidden behind a modifier class.
## HTML
```html
<section class="twr-03 relative block w-full min-h-svh box-border bg-twr03-bg text-twr03-ink font-twr03-cond" aria-labelledby="twr-03-title">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-03-title">Ordered dithering ramps built from gradients</h2>

  <div class="absolute top-4 right-4 z-6">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-03-theme">
    <label class="grid place-items-center size-11 rounded-full border border-twr03-line bg-twr03-surface text-twr03-ink2 cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-twr03-acc peer-focus-visible:outline-offset-2" for="twr-03-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle dark surround</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] gap-[clamp(1.5rem,1rem+2vw,2.25rem)] max-w-[68rem] mx-auto px-[clamp(0.85rem,0.5rem+2vw,2rem)] pt-[clamp(3.5rem,3rem+3vw,5rem)] pb-16">
    <header class="grid gap-1.5 min-w-0">
      <p class="m-0 font-twr03-mono text-[0.68rem] tracking-[0.14em] uppercase text-twr03-ink2">Palette &middot; Game Boy DMG-01 &middot; 4 tones, exact sRGB</p>
      <h3 class="m-0 min-w-0 text-[clamp(1.35rem,1rem+2vw,2.2rem)] font-bold leading-[1.08] tracking-[-0.03em] text-balance">Four colours, twelve apparent tones</h3>
      <p class="m-0 min-w-0 max-w-[52ch] text-[0.95rem] leading-relaxed text-pretty text-twr03-ink2">Every band below contains only palette colours. The intermediate tones are patterns, not blends.</p>
    </header>

    <div class="flex flex-wrap gap-2">
      <span class="flex-none min-w-0 font-twr03-mono text-[0.7rem] tracking-[0.03em] px-2.5 py-2 border border-twr03-line bg-twr03-p0 text-twr03-p3">#0f380f</span>
      <span class="flex-none min-w-0 font-twr03-mono text-[0.7rem] tracking-[0.03em] px-2.5 py-2 border border-twr03-line bg-twr03-p1 text-[#dff0a8]">#306230</span>
      <span class="flex-none min-w-0 font-twr03-mono text-[0.7rem] tracking-[0.03em] px-2.5 py-2 border border-twr03-line bg-twr03-p2 text-[#10290a]">#8bac0f</span>
      <span class="flex-none min-w-0 font-twr03-mono text-[0.7rem] tracking-[0.03em] px-2.5 py-2 border border-twr03-line bg-twr03-p3 text-[#10290a]">#9bbc0f</span>
    </div>

    <div class="grid grid-cols-[minmax(0,1fr)] gap-4 lg:grid-cols-2">
      <article class="min-w-0 grid content-start gap-2.5 border border-twr03-line bg-twr03-surface p-[clamp(0.8rem,0.6rem+0.8vw,1.1rem)]" aria-labelledby="twr-03-r0">
        <h4 class="m-0 min-w-0 font-twr03-mono text-[0.7rem] tracking-[0.1em] uppercase text-twr03-ink2" id="twr-03-r0">Reference &middot; unlimited colour</h4>
        <div class="flex min-w-0 h-[clamp(64px,8vw,92px)] overflow-hidden border-2 border-[#0f380f] [background:linear-gradient(90deg,#0f380f,#306230,#8bac0f,#9bbc0f)]" aria-hidden="true"></div>
        <p class="m-0 min-w-0 text-[0.82rem] leading-normal text-pretty text-twr03-ink2">A plain linear gradient. Contains thousands of colours the hardware never had.</p>
      </article>

      <article class="min-w-0 grid content-start gap-2.5 border border-twr03-line bg-twr03-surface p-[clamp(0.8rem,0.6rem+0.8vw,1.1rem)]" aria-labelledby="twr-03-r1">
        <h4 class="m-0 min-w-0 font-twr03-mono text-[0.7rem] tracking-[0.1em] uppercase text-twr03-ink2" id="twr-03-r1">2 colours &middot; 2&times;2 Bayer</h4>
        <div class="flex min-w-0 h-[clamp(64px,8vw,92px)] overflow-hidden border-2 border-[#0f380f]" aria-hidden="true">
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] bg-twr03-p0"></span>
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] twr-03__dith bg-twr03-p0 [background-image:repeating-conic-gradient(var(--color-twr03-p3)_0%_25%,rgba(0,0,0,0)_0%_100%)]"></span>
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] twr-03__dith bg-twr03-p0 [background-image:repeating-conic-gradient(var(--color-twr03-p3)_0%_25%,rgba(0,0,0,0)_0%_50%,var(--color-twr03-p3)_0%_75%,rgba(0,0,0,0)_0%_100%)]"></span>
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] twr-03__dith bg-twr03-p3 [background-image:repeating-conic-gradient(var(--color-twr03-p0)_0%_25%,rgba(0,0,0,0)_0%_100%)]"></span>
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] bg-twr03-p3"></span>
        </div>
        <p class="m-0 min-w-0 text-[0.82rem] leading-normal text-pretty text-twr03-ink2">Darkest and lightest tone only. Five apparent steps from two real ones.</p>
      </article>

      <article class="min-w-0 grid content-start gap-2.5 border border-twr03-line bg-twr03-surface p-[clamp(0.8rem,0.6rem+0.8vw,1.1rem)]" aria-labelledby="twr-03-r2">
        <h4 class="m-0 min-w-0 font-twr03-mono text-[0.7rem] tracking-[0.1em] uppercase text-twr03-ink2" id="twr-03-r2">4 colours &middot; adjacent-pair dither</h4>
        <div class="flex min-w-0 h-[clamp(64px,8vw,92px)] overflow-hidden border-2 border-[#0f380f]" aria-hidden="true">
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] bg-twr03-p0"></span>
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] twr-03__dith bg-twr03-p0 [background-image:repeating-conic-gradient(var(--color-twr03-p1)_0%_25%,rgba(0,0,0,0)_0%_50%,var(--color-twr03-p1)_0%_75%,rgba(0,0,0,0)_0%_100%)]"></span>
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] bg-twr03-p1"></span>
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] twr-03__dith bg-twr03-p1 [background-image:repeating-conic-gradient(var(--color-twr03-p2)_0%_25%,rgba(0,0,0,0)_0%_50%,var(--color-twr03-p2)_0%_75%,rgba(0,0,0,0)_0%_100%)]"></span>
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] bg-twr03-p2"></span>
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] twr-03__dith bg-twr03-p2 [background-image:repeating-conic-gradient(var(--color-twr03-p3)_0%_25%,rgba(0,0,0,0)_0%_50%,var(--color-twr03-p3)_0%_75%,rgba(0,0,0,0)_0%_100%)]"></span>
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] bg-twr03-p3"></span>
        </div>
        <p class="m-0 min-w-0 text-[0.82rem] leading-normal text-pretty text-twr03-ink2">Each pattern mixes only its two neighbouring palette entries.</p>
      </article>

      <article class="min-w-0 grid content-start gap-2.5 border border-twr03-line bg-twr03-surface p-[clamp(0.8rem,0.6rem+0.8vw,1.1rem)]" aria-labelledby="twr-03-r3">
        <h4 class="m-0 min-w-0 font-twr03-mono text-[0.7rem] tracking-[0.1em] uppercase text-twr03-ink2" id="twr-03-r3">8 steps &middot; 2px cell, fine mask</h4>
        <div class="flex min-w-0 h-[clamp(64px,8vw,92px)] overflow-hidden border-2 border-[#0f380f] [--twr-03-cell:2px]" aria-hidden="true">
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] bg-twr03-p0"></span>
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] twr-03__dith bg-twr03-p0 [background-image:repeating-conic-gradient(var(--color-twr03-p1)_0%_25%,rgba(0,0,0,0)_0%_50%,var(--color-twr03-p1)_0%_75%,rgba(0,0,0,0)_0%_100%)]"></span>
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] bg-twr03-p1"></span>
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] twr-03__dith bg-twr03-p1 [background-image:repeating-conic-gradient(var(--color-twr03-p2)_0%_25%,rgba(0,0,0,0)_0%_50%,var(--color-twr03-p2)_0%_75%,rgba(0,0,0,0)_0%_100%)]"></span>
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] bg-twr03-p2"></span>
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] twr-03__dith bg-twr03-p2 [background-image:repeating-conic-gradient(var(--color-twr03-p3)_0%_25%,rgba(0,0,0,0)_0%_50%,var(--color-twr03-p3)_0%_75%,rgba(0,0,0,0)_0%_100%)]"></span>
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] bg-twr03-p3"></span>
            <span class="flex-1 min-w-0 [background-size:var(--twr-03-cell)_var(--twr-03-cell)] bg-twr03-p3"></span>
        </div>
        <p class="m-0 min-w-0 text-[0.82rem] leading-normal text-pretty text-twr03-ink2">Same construction at a 2px cell. Closer to a blend, further from a period-correct look.</p>
      </article>
    </div>

    <aside class="min-w-0 grid gap-2.5 border border-twr03-line border-l-4 border-l-twr03-acc bg-twr03-surface p-[clamp(0.85rem,0.6rem+1vw,1.2rem)]">
      <h4 class="m-0 font-twr03-mono text-[0.7rem] tracking-[0.12em] uppercase text-twr03-ink2">Coverage table</h4>
      <dl class="m-0 grid gap-1 text-[0.85rem]">
        <div class="flex items-baseline gap-3 min-w-0"><dt class="m-0 flex-none w-14 font-twr03-mono tabular-nums text-twr03-acc">0%</dt><dd class="m-0 min-w-0 text-twr03-ink2">flat base colour, no overlay</dd></div>
        <div class="flex items-baseline gap-3 min-w-0"><dt class="m-0 flex-none w-14 font-twr03-mono tabular-nums text-twr03-acc">25%</dt><dd class="m-0 min-w-0 text-twr03-ink2">one quadrant of the 2&times;2 cell</dd></div>
        <div class="flex items-baseline gap-3 min-w-0"><dt class="m-0 flex-none w-14 font-twr03-mono tabular-nums text-twr03-acc">50%</dt><dd class="m-0 min-w-0 text-twr03-ink2">two opposite quadrants &mdash; checkerboard</dd></div>
        <div class="flex items-baseline gap-3 min-w-0"><dt class="m-0 flex-none w-14 font-twr03-mono tabular-nums text-twr03-acc">75%</dt><dd class="m-0 min-w-0 text-twr03-ink2">three quadrants, inverse of 25%</dd></div>
        <div class="flex items-baseline gap-3 min-w-0"><dt class="m-0 flex-none w-14 font-twr03-mono tabular-nums text-twr03-acc">100%</dt><dd class="m-0 min-w-0 text-twr03-ink2">flat next palette colour</dd></div>
      </dl>
    </aside>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr03-p0: #0f380f;
  --color-twr03-p1: #306230;
  --color-twr03-p2: #8bac0f;
  --color-twr03-p3: #9bbc0f;
  --color-twr03-bg: #f2efe6;
  --color-twr03-bg: oklch(0.95 0.012 100);
  --color-twr03-surface: #ffffff;
  --color-twr03-surface: oklch(1 0 0);
  --color-twr03-ink: #15170f;
  --color-twr03-ink: oklch(0.19 0.012 120);
  --color-twr03-ink2: #4e5344;
  --color-twr03-ink2: oklch(0.45 0.017 120);
  --color-twr03-line: #b6b9a6;
  --color-twr03-line: oklch(0.77 0.02 118);
  --color-twr03-acc: #2f6b12;
  --color-twr03-acc: oklch(0.46 0.14 133);
  --font-twr03-cond: 'Archivo', ui-sans-serif, 'Arial Narrow', Helvetica, sans-serif;
  --font-twr03-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}

.twr-03 {
  --twr-03-cell: 4px;
}
/* A feature query has no variant form, and the fallback has to reach every
   patterned band at once — hence one shared hook class on the bands. */

@supports not (background: repeating-conic-gradient(#000 0% 25%, #fff 0% 50%)) {
  .twr-03__dith {
    background-image: repeating-linear-gradient(45deg, currentColor 0 2px, rgba(0, 0, 0, 0) 2px 4px);
    color: var(--color-twr03-p3);
  }
}

.twr-03:has(#twr-03-theme:checked) {
  --color-twr03-bg: #14160f;
  --color-twr03-bg: oklch(0.19 0.009 120);
  --color-twr03-surface: #1e2117;
  --color-twr03-surface: oklch(0.24 0.012 120);
  --color-twr03-ink: #f0f2e7;
  --color-twr03-ink: oklch(0.96 0.008 120);
  --color-twr03-ink2: #a8ad99;
  --color-twr03-ink2: oklch(0.74 0.016 120);
  --color-twr03-line: #414635;
  --color-twr03-line: oklch(0.37 0.018 120);
  --color-twr03-acc: #a4d96a;
  --color-twr03-acc: oklch(0.83 0.15 133);
}
```
