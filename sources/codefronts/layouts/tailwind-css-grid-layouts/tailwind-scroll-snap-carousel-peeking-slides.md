---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-scroll-snap-carousel-peeking-slides/"
title: "Tailwind Scroll Snap Carousel with Peeking Slides"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A destination carousel with native physics and no library: 78% slides centred by snap-center, neighbours peeking at both edges, real photography and a price…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Scroll Snap Carousel with Peeking Slides
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-scroll-snap-carousel-peeking-slides/

A destination carousel with native physics and no library: 78% slides centred by snap-center, neighbours peeking at both edges, real photography and a price line per card. Momentum, rubber-banding and keyboard scrolling come from the browser.
## HTML
```html
<section class="tgx-27 w-full min-h-svh bg-tgx27-bg font-tgx27-sans py-9 grid content-center gap-4">
  <header class="px-[11%] flex items-end justify-between gap-4 flex-wrap">
    <div class="flex flex-col gap-1">
      <p class="text-[0.66rem] tracking-[0.18em] uppercase text-tgx27-accent">Meridian Travel</p>
      <h2 class="text-[1.35rem] font-semibold text-white tracking-[-0.01em]">Trips leaving in October</h2>
    </div>
    <p class="text-[0.74rem] text-tgx27-dim">Swipe, drag or Tab through</p>
  </header>
  <div role="group" aria-label="Featured trips" class="grid grid-flow-col auto-cols-[78%] gap-4 overflow-x-auto overscroll-x-contain snap-x snap-mandatory scroll-smooth px-[11%] pb-3">
    <article tabindex="0" class="snap-center relative aspect-[16/9] rounded-2xl overflow-hidden border border-white/15 focus-visible:outline-[3px] focus-visible:outline-tgx27-ring focus-visible:outline-offset-[3px]">
      <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=900&h=506&q=80&auto=format&fit=crop" alt="Still lake below a wooded ridge at dusk" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
      <div class="absolute inset-0 bg-[linear-gradient(180deg,transparent_35%,oklch(0.12_0.02_300/0.88))]"></div>
      <div class="relative h-full flex flex-col justify-end gap-1 p-5">
        <p class="text-[0.66rem] tracking-[0.16em] uppercase text-tgx27-ring">6 nights · guided</p>
        <h3 class="text-[1.15rem] font-semibold text-white">Kuusamo lakes</h3>
        <p class="text-[0.8rem] text-tgx27-slidedim">Cabins, canoes and the first frost. From <span class="tabular-nums font-medium text-white">£1,240</span></p>
      </div>
    </article>
    <article tabindex="0" class="snap-center relative aspect-[16/9] rounded-2xl overflow-hidden border border-white/15 focus-visible:outline-[3px] focus-visible:outline-tgx27-ring focus-visible:outline-offset-[3px]">
      <img src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=900&h=506&q=80&auto=format&fit=crop" alt="Rock face rising into mist above a valley" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
      <div class="absolute inset-0 bg-[linear-gradient(180deg,transparent_35%,oklch(0.12_0.02_300/0.88))]"></div>
      <div class="relative h-full flex flex-col justify-end gap-1 p-5">
        <p class="text-[0.66rem] tracking-[0.16em] uppercase text-tgx27-ring">8 nights · self-guided</p>
        <h3 class="text-[1.15rem] font-semibold text-white">Lofoten crossing</h3>
        <p class="text-[0.8rem] text-tgx27-slidedim">Ferry hops and fishing villages. From <span class="tabular-nums font-medium text-white">£1,880</span></p>
      </div>
    </article>
    <article tabindex="0" class="snap-center relative aspect-[16/9] rounded-2xl overflow-hidden border border-white/15 focus-visible:outline-[3px] focus-visible:outline-tgx27-ring focus-visible:outline-offset-[3px]">
      <img src="https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=900&h=506&q=80&auto=format&fit=crop" alt="City street at night with lights reflected on wet pavement" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
      <div class="absolute inset-0 bg-[linear-gradient(180deg,transparent_35%,oklch(0.12_0.02_300/0.88))]"></div>
      <div class="relative h-full flex flex-col justify-end gap-1 p-5">
        <p class="text-[0.66rem] tracking-[0.16em] uppercase text-tgx27-ring">3 nights · city</p>
        <h3 class="text-[1.15rem] font-semibold text-white">London, off-season</h3>
        <p class="text-[0.8rem] text-tgx27-slidedim">Galleries before the crowds. From <span class="tabular-nums font-medium text-white">£420</span></p>
      </div>
    </article>
    <article tabindex="0" class="snap-center relative aspect-[16/9] rounded-2xl overflow-hidden border border-white/15 focus-visible:outline-[3px] focus-visible:outline-tgx27-ring focus-visible:outline-offset-[3px]">
      <img src="https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=900&h=506&q=80&auto=format&fit=crop" alt="Mountain range with cloud sitting in the valley" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
      <div class="absolute inset-0 bg-[linear-gradient(180deg,transparent_35%,oklch(0.12_0.02_300/0.88))]"></div>
      <div class="relative h-full flex flex-col justify-end gap-1 p-5">
        <p class="text-[0.66rem] tracking-[0.16em] uppercase text-tgx27-ring">5 nights · walking</p>
        <h3 class="text-[1.15rem] font-semibold text-white">Hardanger ridges</h3>
        <p class="text-[0.8rem] text-tgx27-slidedim">Hut to hut, bags moved for you. From <span class="tabular-nums font-medium text-white">£980</span></p>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx27-bg: #191225;
  --color-tgx27-bg: oklch(0.18 0.02 310);
  --color-tgx27-dim: #b2a4c4;
  --color-tgx27-dim: oklch(0.75 0.04 310);
  --color-tgx27-slidedim: #e6dcf0;
  --color-tgx27-slidedim: oklch(0.92 0.02 310);
  --color-tgx27-accent: #d79ae0;
  --color-tgx27-accent: oklch(0.79 0.12 320);
  --color-tgx27-ring: #e39ad0;
  --color-tgx27-ring: oklch(0.8 0.14 330);
  --font-tgx27-sans: 'Inter Tight', system-ui, sans-serif;
}

.tgx-27 {
  width: 100%;
  min-height: 100svh;
  /* Thin coloured scrollbar: no utility, and worth keeping as the visible
       affordance this pattern's discoverability depends on. */
  scrollbar-width: thin;
  scrollbar-color: oklch(0.5 0.1 310) transparent;
}
```
