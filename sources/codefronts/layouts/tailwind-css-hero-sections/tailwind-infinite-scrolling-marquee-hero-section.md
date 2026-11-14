---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-infinite-scrolling-marquee-hero-section/"
title: "Infinite Scrolling Marquee Hero Section in Tailwind CSS"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "A streetwear drop hero — two counter-scrolling marquee bands frame the drop details, a countdown-style date strip and a hot CTA."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Infinite Scrolling Marquee Hero Section in Tailwind CSS
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-infinite-scrolling-marquee-hero-section/

A streetwear drop hero — two counter-scrolling marquee bands frame the drop details, a countdown-style date strip and a hot CTA. Tangerine on chocolate. Seamless loops (no jump), pause on hover, and frozen under reduced motion.
## HTML
```html
<section class="ths-14 flex w-full min-h-svh flex-col justify-between overflow-hidden bg-ths14-bg py-8 font-ths14-sans text-ths14-cream" aria-label="Marquee hero">
  <div aria-hidden="true" class="group -mx-[5%] -rotate-2 border-y-4 border-ths14-bg bg-ths14-tang py-4 text-ths14-bg">
    <div class="flex w-max animate-ths14-roll font-ths14-display text-[clamp(32px,5.5vw,60px)] leading-none font-black tracking-[-0.01em] whitespace-nowrap italic group-hover:[animation-play-state:paused] motion-reduce:animate-none">
      <span class="pr-8">EVERYTHING SELLS OUT ✦ EVERYTHING SELLS OUT ✦ EVERYTHING SELLS OUT ✦ EVERYTHING SELLS OUT ✦</span>
      <span class="pr-8">EVERYTHING SELLS OUT ✦ EVERYTHING SELLS OUT ✦ EVERYTHING SELLS OUT ✦ EVERYTHING SELLS OUT ✦</span>
    </div>
  </div>
  <div class="grid flex-1 place-items-center px-5 py-14 text-center">
    <div class="max-w-2xl">
      <h1 class="font-ths14-display text-[clamp(38px,6vw,68px)] leading-[1.02] font-black tracking-[-0.025em] text-balance [font-stretch:110%]">Drop 04. <em class="text-ths14-amber">Tuesday 11am EST.</em></h1>
      <p class="mx-auto mt-4 max-w-md text-[17px] leading-relaxed text-ths14-mut">72 pieces. No restock. No back-orders. No DM begging.</p>
      <ul class="mt-7 flex flex-wrap justify-center gap-2 font-ths14-mono text-[11px] font-bold tracking-[0.14em] uppercase">
        <li class="border border-ths14-tang/60 px-3 py-1.5 text-ths14-tang">72 units</li>
        <li class="border border-ths14-tang/60 px-3 py-1.5 text-ths14-tang">Limit 1 per customer</li>
        <li class="border border-ths14-tang/60 px-3 py-1.5 text-ths14-tang">Ships 48h</li>
      </ul>
      <a href="#join" class="mt-8 inline-flex min-h-12 items-center gap-2 bg-ths14-amber px-8 text-[15px] font-extrabold tracking-[0.04em] text-ths14-bg transition hover:bg-ths14-cream focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths14-amber motion-reduce:transition-none">⏰ Set the alarm</a>
    </div>
  </div>
  <div aria-hidden="true" class="group -mx-[5%] rotate-1 border-y-4 border-ths14-tang bg-ths14-bg py-4 text-ths14-tang">
    <div class="flex w-max animate-ths14-roll font-ths14-display text-[clamp(32px,5.5vw,60px)] leading-none font-black whitespace-nowrap italic [animation-direction:reverse] group-hover:[animation-play-state:paused] motion-reduce:animate-none">
      <span class="pr-8">NO RESTOCK ✦ NO RESTOCK ✦ NO RESTOCK ✦ NO RESTOCK ✦ NO RESTOCK ✦ NO RESTOCK ✦</span>
      <span class="pr-8">NO RESTOCK ✦ NO RESTOCK ✦ NO RESTOCK ✦ NO RESTOCK ✦ NO RESTOCK ✦ NO RESTOCK ✦</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths14-bg: #2a1410;
  --color-ths14-bg: oklch(0.222 0.037 31.2);
  --color-ths14-cream: #ffe4d6;
  --color-ths14-cream: oklch(0.937 0.035 49.2);
  --color-ths14-mut: #d6b8a9;
  --color-ths14-mut: oklch(0.804 0.04 48.2);
  --color-ths14-tang: #f04e23;
  --color-ths14-tang: oklch(0.645 0.205 35.1);
  --color-ths14-amber: #f5b148;
  --color-ths14-amber: oklch(0.806 0.142 74.7);
  --font-ths14-display: 'Archivo', system-ui, sans-serif;
  --font-ths14-sans: 'Geist', system-ui, sans-serif;
  --font-ths14-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ths14-roll: ths14-roll 24s linear infinite;

  @keyframes ths14-roll {
    to {
      transform: translateX(-50%);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-14 {
  width: 100%;
  min-height: 100svh;
}
```
