---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-magazine-spread-layout-overlapping-headline/"
title: "Tailwind Magazine Spread Layout with Overlapping Headline"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A print-grade travel opener: the display headline crosses the photograph, a vertical byline runs up the gutter, the standfirst sits under a hairline rule and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Magazine Spread Layout with Overlapping Headline
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-magazine-spread-layout-overlapping-headline/

A print-grade travel opener: the display headline crosses the photograph, a vertical byline runs up the gutter, the standfirst sits under a hairline rule and the body copy breaks into columns with a drop cap.
## HTML
```html
<section class="tgx-10 w-full min-h-svh bg-tgx10-paper text-tgx10-ink font-tgx10-serif px-6 py-10">
  <article class="grid grid-cols-12 grid-rows-[auto_auto_auto_1fr] gap-4 w-[min(700px,100%)] mx-auto">
    <figure class="col-start-5 col-end-13 row-start-1 row-end-4 max-sm:col-start-1 max-sm:row-end-2 z-10 overflow-hidden bg-tgx10-shade">
      <img src="https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=900&h=675&q=80&auto=format&fit=crop" alt="Parisian boulevard at dusk seen from a rooftop, lights coming on" loading="lazy" class="w-full h-full object-cover aspect-[4/3]">
    </figure>
    <h2 class="col-start-1 col-end-9 row-start-2 row-end-3 max-sm:col-end-13 z-20 text-[clamp(2rem,6vw,3.3rem)] leading-[1.02] font-bold tracking-[-0.015em] text-balance [text-shadow:0_0_18px_var(--color-tgx10-paper),0_0_6px_var(--color-tgx10-paper),2px_2px_0_var(--color-tgx10-paper)]">Forty hours in the tenth</h2>
    <p class="col-start-12 col-end-13 row-start-1 row-end-2 max-sm:hidden z-30 justify-self-end [writing-mode:vertical-rl] font-tgx10-sans text-[0.62rem] tracking-[0.22em] uppercase text-white px-1 py-3 [text-shadow:0_1px_6px_oklch(0.2_0.02_60/0.8)]">Words · Amara Chen</p>
    <div class="col-start-1 col-end-5 row-start-3 row-end-4 max-sm:col-end-13 border-t-[3px] border-tgx10-ink pt-3">
      <p class="font-tgx10-sans text-[0.86rem] leading-[1.6] text-tgx10-mut">A weekend spent entirely between Canal Saint-Martin and Gare de l'Est, on the theory that the best way to see a city is to refuse to cross it.</p>
    </div>
    <p class="col-start-1 col-end-9 row-start-4 row-end-5 max-sm:col-end-13 text-[0.98rem] leading-[1.72] [column-width:17rem] [column-gap:2rem] [column-rule:1px_solid_var(--color-tgx10-rule)] first-letter:float-left first-letter:text-[3.2em] first-letter:leading-[0.82] first-letter:pr-[0.12em] first-letter:font-bold first-letter:text-tgx10-rust">Arrondissements are an administrative fiction that tourists treat as a map, and for one weekend I decided to take the fiction seriously. Everything within a twenty-minute walk of the canal, nothing outside it: the same four cafés, the same bakery queue, the same bench by the lock. By Saturday evening the waiter had stopped asking. By Sunday I had opinions about which side of the water gets the better light, which is the point at which a neighbourhood stops being a destination and starts being somewhere you have been.</p>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx10-paper: #f8f5ee;
  --color-tgx10-paper: oklch(0.97 0.008 85);
  --color-tgx10-shade: #e6e0d4;
  --color-tgx10-shade: oklch(0.9 0.012 85);
  --color-tgx10-ink: #2b2620;
  --color-tgx10-ink: oklch(0.24 0.01 60);
  --color-tgx10-mut: #574f45;
  --color-tgx10-mut: oklch(0.42 0.015 60);
  --color-tgx10-rule: #c4bcae;
  --color-tgx10-rule: oklch(0.79 0.015 80);
  --color-tgx10-rust: #a3512a;
  --color-tgx10-rust: oklch(0.53 0.15 40);
  --font-tgx10-serif: 'Fraunces', Georgia, serif;
  --font-tgx10-sans: 'Inter Tight', system-ui, sans-serif;
}

.tgx-10 {
  width: 100%;
  min-height: 100svh;
}
```
