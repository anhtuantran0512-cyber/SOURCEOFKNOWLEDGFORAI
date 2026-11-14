---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/pastel-gradient-text-in-tailwind-css/"
title: "Pastel Gradient Text in Tailwind CSS"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "A slow-living blog layout in soft rose, sky and mint."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pastel Gradient Text in Tailwind CSS
Source: https://codefronts.com/motion/tailwind-css-text-gradient/pastel-gradient-text-in-tailwind-css/

A slow-living blog layout in soft rose, sky and mint. Pastels on white are a contrast trap &mdash; the original's 60–90% lightness stops measured under 2:1 &mdash; so this port keeps the soft feel in the card washes (bg-ttg12-rose/12) and uses deeper, still-gentle oklch stops for the text itself.
## HTML
```html
<section class="ttg-12 w-full min-h-svh bg-ttg12-bg font-ttg12-sans text-ttg12-ink" aria-labelledby="ttg12-title">
  <div class="mx-auto max-w-3xl px-6 py-16">
    <p class="flex items-center gap-2 text-xs font-semibold tracking-[0.1em] text-ttg12-mut uppercase"><span class="rounded-full bg-ttg12-rose/15 px-2.5 py-1 text-ttg12-rose2">Lifestyle</span>4 min read</p>
    <h1 id="ttg12-title" class="mt-6 font-ttg12-serif text-[clamp(2.75rem,7vw,4.75rem)] leading-[1.02] tracking-[-0.02em] text-balance">The art of <span class="bg-linear-110/oklch from-ttg12-rose via-ttg12-sky to-ttg12-mint bg-clip-text pr-[0.05em] text-transparent italic">slow mornings</span></h1>
    <p class="mt-6 max-w-xl text-[17px]/[1.75] text-ttg12-mut text-pretty">Gentle routines and intentional starts that reshape how you work, rest and create throughout the day.</p>
    <div class="mt-12 grid gap-4 sm:grid-cols-3">
      <article class="rounded-3xl border border-ttg12-rose/20 bg-ttg12-rose/12 p-6"><span aria-hidden="true" class="font-ttg12-serif text-3xl text-ttg12-rose2/60">01</span><h3 class="mt-3 w-fit bg-linear-to-r from-ttg12-rose to-ttg12-rose2 bg-clip-text text-lg font-bold text-transparent">Mindful journaling</h3><p class="mt-2 text-sm/[1.65] text-ttg12-mut">Five minutes of unstructured writing before checking any screen.</p></article>
      <article class="rounded-3xl border border-ttg12-sky/20 bg-ttg12-sky/12 p-6"><span aria-hidden="true" class="font-ttg12-serif text-3xl text-ttg12-sky2/60">02</span><h3 class="mt-3 w-fit bg-linear-to-r from-ttg12-sky to-ttg12-sky2 bg-clip-text text-lg font-bold text-transparent">Herbal rituals</h3><p class="mt-2 text-sm/[1.65] text-ttg12-mut">Brewing tea as a meditative practice — warmth, aroma, presence.</p></article>
      <article class="rounded-3xl border border-ttg12-mint/20 bg-ttg12-mint/12 p-6"><span aria-hidden="true" class="font-ttg12-serif text-3xl text-ttg12-mint2/60">03</span><h3 class="mt-3 w-fit bg-linear-to-r from-ttg12-mint to-ttg12-mint2 bg-clip-text text-lg font-bold text-transparent">Gentle movement</h3><p class="mt-2 text-sm/[1.65] text-ttg12-mut">Ten minutes of stretching outdoors to anchor the body in the day.</p></article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg12-bg: #fdf8f5;
  --color-ttg12-bg: oklch(0.982 0.008 50);
  --color-ttg12-ink: #2a211d;
  --color-ttg12-ink: oklch(0.26 0.015 45);
  --color-ttg12-mut: #6c5f58;
  --color-ttg12-mut: oklch(0.5 0.02 45);
  --color-ttg12-rose: #d9567a;
  --color-ttg12-rose: oklch(0.62 0.16 5);
  --color-ttg12-rose2: #c0508f;
  --color-ttg12-rose2: oklch(0.57 0.16 350);
  --color-ttg12-sky: #3a8fc9;
  --color-ttg12-sky: oklch(0.6 0.12 240);
  --color-ttg12-sky2: #6a6fd0;
  --color-ttg12-sky2: oklch(0.56 0.14 275);
  --color-ttg12-mint: #23977a;
  --color-ttg12-mint: oklch(0.6 0.11 170);
  --color-ttg12-mint2: #3b8f55;
  --color-ttg12-mint2: oklch(0.57 0.11 150);
  --font-ttg12-serif: 'Instrument Serif', Georgia, serif;
  --font-ttg12-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-12 {
  width: 100%;
  min-height: 100svh;
}
```
