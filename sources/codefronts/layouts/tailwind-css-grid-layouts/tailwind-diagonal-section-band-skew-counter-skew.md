---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-diagonal-section-band-skew-counter-skew/"
title: "Tailwind Diagonal Section Band with skewY Counter-Skew"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "The angled results band every agency site ships: the section skews, its children counter-skew, and the stats grid inside never knows it is tilted."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Diagonal Section Band with skewY Counter-Skew
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-diagonal-section-band-skew-counter-skew/

The angled results band every agency site ships: the section skews, its children counter-skew, and the stats grid inside never knows it is tilted. No SVG dividers, no clip-path seams that misalign at odd widths.
## HTML
```html
<section class="tgx-21 w-full min-h-svh bg-tgx21-paper font-tgx21-sans overflow-hidden">
  <div class="px-6 py-10 w-[min(680px,100%)] mx-auto flex flex-col gap-2">
    <p class="text-[0.66rem] tracking-[0.18em] uppercase text-tgx21-accent">Northbeam · Studio</p>
    <h2 class="text-[clamp(1.4rem,3.4vw,2rem)] leading-[1.15] font-semibold text-tgx21-ink tracking-[-0.015em] text-balance">We rebuild interfaces that outgrew their first draft</h2>
    <p class="text-[0.88rem] leading-[1.65] text-tgx21-mut max-w-[52ch]">Design systems, front-end architecture and the unglamorous work of deleting CSS.</p>
  </div>
  <div class="-skew-y-[4deg] *:skew-y-[4deg] my-5 py-[calc(tan(4deg)*50vw*0.25+3rem)] bg-[linear-gradient(110deg,oklch(0.2_0.03_250),oklch(0.26_0.06_215))]">
    <div class="px-6 w-[min(680px,100%)] mx-auto">
      <div class="flex items-baseline justify-between gap-3 flex-wrap mb-5">
        <h3 class="text-tgx21-electric text-[clamp(1.15rem,3vw,1.5rem)] font-semibold">Last twelve months</h3>
        <span class="font-tgx21-mono text-[0.7rem] text-tgx21-banddim">9 engagements · 4 industries</span>
      </div>
      <div class="grid grid-cols-[repeat(auto-fit,minmax(min(160px,100%),1fr))] gap-3">
        <article class="flex flex-col gap-1 rounded-xl border border-tgx21-electric/40 bg-white/10 p-4"><strong class="font-tgx21-mono text-[1.6rem] leading-none text-tgx21-electric tabular-nums">−62%</strong><span class="text-[0.76rem] text-tgx21-banddim">CSS shipped after the rebuild</span></article>
        <article class="flex flex-col gap-1 rounded-xl border border-tgx21-electric/40 bg-white/10 p-4"><strong class="font-tgx21-mono text-[1.6rem] leading-none text-tgx21-electric tabular-nums">0.00</strong><span class="text-[0.76rem] text-tgx21-banddim">Cumulative layout shift, median page</span></article>
        <article class="flex flex-col gap-1 rounded-xl border border-tgx21-electric/40 bg-white/10 p-4"><strong class="font-tgx21-mono text-[1.6rem] leading-none text-tgx21-electric tabular-nums">9 wks</strong><span class="text-[0.76rem] text-tgx21-banddim">Median time from audit to launch</span></article>
      </div>
    </div>
  </div>
  <div class="px-6 py-10 w-[min(680px,100%)] mx-auto flex items-center justify-between gap-4 flex-wrap">
    <p class="text-[0.86rem] leading-[1.6] text-tgx21-mut max-w-[38ch]">The band's edges are transforms, not SVG dividers — they stay sharp at every viewport width.</p>
    <a href="#0" class="inline-flex items-center min-h-11 px-5 rounded-full bg-tgx21-ink text-white text-[0.84rem] font-semibold no-underline transition-colors hover:bg-tgx21-inkhover focus-visible:outline-2 focus-visible:outline-tgx21-ink focus-visible:outline-offset-2">Start a project</a>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx21-paper: #f3f6f8;
  --color-tgx21-paper: oklch(0.96 0.008 220);
  --color-tgx21-ink: #1b2730;
  --color-tgx21-ink: oklch(0.25 0.02 230);
  --color-tgx21-inkhover: #24333e;
  --color-tgx21-inkhover: oklch(0.31 0.025 230);
  --color-tgx21-mut: #4d5b63;
  --color-tgx21-mut: oklch(0.45 0.02 230);
  --color-tgx21-accent: #0d6f86;
  --color-tgx21-accent: oklch(0.47 0.09 215);
  --color-tgx21-electric: #7ce0ea;
  --color-tgx21-electric: oklch(0.86 0.13 195);
  --color-tgx21-banddim: #c2d2d8;
  --color-tgx21-banddim: oklch(0.84 0.02 220);
  --font-tgx21-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tgx21-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tgx-21 {
  width: 100%;
  min-height: 100svh;
  --tgx21-angle: 4deg;
}
```
