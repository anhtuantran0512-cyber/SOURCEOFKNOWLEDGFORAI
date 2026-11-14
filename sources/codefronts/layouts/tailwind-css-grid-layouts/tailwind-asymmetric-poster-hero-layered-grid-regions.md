---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-asymmetric-poster-hero-layered-grid-regions/"
title: "Tailwind Asymmetric Poster Hero with Layered Grid Regions"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A conference hero built like a printed poster: a crimson slab, an offset cream panel, an outlined year bleeding off the top edge and the headline straddling…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Asymmetric Poster Hero with Layered Grid Regions
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-asymmetric-poster-hero-layered-grid-regions/

A conference hero built like a printed poster: a crimson slab, an offset cream panel, an outlined year bleeding off the top edge and the headline straddling both — four layers, one grid, zero absolute positioning.
## HTML
```html
<section class="tgx-22 w-full min-h-svh bg-tgx22-ink font-tgx22-sans p-6 grid place-items-center">
  <div class="grid grid-cols-10 grid-rows-[repeat(7,minmax(34px,auto))] w-[min(660px,100%)] overflow-hidden">
    <div aria-hidden="true" class="col-start-1 col-end-6 row-start-1 row-end-5 z-10 bg-tgx22-crimson"></div>
    <div aria-hidden="true" class="col-start-4 col-end-11 row-start-2 row-end-8 z-20 bg-tgx22-cream"></div>
    <span aria-hidden="true" class="col-start-7 col-end-11 row-start-1 row-end-4 max-sm:col-start-6 z-30 justify-self-end translate-x-[6%] -translate-y-[12%] text-[clamp(4.5rem,15vw,8.5rem)] font-black leading-[0.75] text-transparent [-webkit-text-stroke:2px_var(--color-tgx22-crimson)]">26</span>
    <div class="col-start-2 col-end-9 row-start-3 row-end-5 max-sm:col-end-10 z-40 self-center flex flex-col gap-2">
      <p class="font-tgx22-mono text-[0.68rem] tracking-[0.18em] uppercase text-tgx22-crimson">Layout Conf · Rotterdam</p>
      <h2 class="text-[clamp(1.7rem,5vw,2.8rem)] leading-[1.02] font-extrabold tracking-[-0.02em] text-tgx22-ink">Balance is<br>overrated</h2>
    </div>
    <div class="col-start-4 col-end-11 row-start-6 row-end-8 z-40 self-end flex items-end justify-between gap-4 flex-wrap p-4">
      <dl class="flex gap-6">
        <div><dt class="text-[0.6rem] uppercase tracking-[0.12em] text-tgx22-caption">Dates</dt><dd class="text-[0.86rem] font-semibold text-tgx22-ink tabular-nums">14–16 Nov</dd></div>
        <div><dt class="text-[0.6rem] uppercase tracking-[0.12em] text-tgx22-caption">Talks</dt><dd class="text-[0.86rem] font-semibold text-tgx22-ink tabular-nums">24</dd></div>
        <div class="max-sm:hidden"><dt class="text-[0.6rem] uppercase tracking-[0.12em] text-tgx22-caption">Tickets</dt><dd class="text-[0.86rem] font-semibold text-tgx22-ink">€240</dd></div>
      </dl>
      <a href="#0" class="inline-flex items-center min-h-11 px-5 rounded-full bg-tgx22-crimson text-white text-[0.84rem] font-semibold no-underline transition-colors hover:bg-tgx22-crimsondark focus-visible:outline-2 focus-visible:outline-tgx22-crimson focus-visible:outline-offset-2">Get a ticket</a>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx22-crimson: #b53821;
  --color-tgx22-crimson: oklch(0.52 0.19 30);
  --color-tgx22-crimsondark: #97291a;
  --color-tgx22-crimsondark: oklch(0.44 0.17 30);
  --color-tgx22-cream: #f3ece0;
  --color-tgx22-cream: oklch(0.95 0.02 85);
  --color-tgx22-ink: #241a17;
  --color-tgx22-ink: oklch(0.22 0.02 30);
  --color-tgx22-caption: #5c4b44;
  --color-tgx22-caption: oklch(0.43 0.02 40);
  --font-tgx22-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tgx22-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tgx-22 {
  width: 100%;
  min-height: 100svh;
}
```
