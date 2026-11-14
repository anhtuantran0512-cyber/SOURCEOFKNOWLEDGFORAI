---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-full-screen-hero-scroll-down-indicator/"
title: "Full-Screen Tailwind Hero with Animated Scroll Down Indicator"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "A full-screen cabin-retreat hero with an animated mouse-wheel scroll cue — forest green on birch, a soft-yellow neo-brutalist CTA and a booking detail strip."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full-Screen Tailwind Hero with Animated Scroll Down Indicator
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-full-screen-hero-scroll-down-indicator/

A full-screen cabin-retreat hero with an animated mouse-wheel scroll cue — forest green on birch, a soft-yellow neo-brutalist CTA and a booking detail strip. The cue is a real link to the next section, so it works for keyboards too.
## HTML
```html
<section class="ths-10 relative grid w-full min-h-svh place-items-center bg-ths10-bg bg-[radial-gradient(80%_60%_at_50%_0%,var(--color-ths10-glow),transparent_70%)] px-5 pt-16 pb-32 font-ths10-sans text-ths10-ink sm:px-14" aria-label="Full-screen hero with scroll cue">
  <div class="max-w-[46rem] text-center">
    <span class="font-ths10-serif text-lg text-ths10-sage italic">— A small place upstate</span>
    <h1 class="mt-4 font-ths10-serif text-[clamp(38px,6vw,68px)] leading-[1.02] font-semibold tracking-[-0.015em] text-balance">Slow Sundays, <em class="text-ths10-honey">warm wood,</em> not a single notification.</h1>
    <p class="mx-auto mt-5 max-w-[30rem] text-[17px] leading-relaxed text-ths10-body">Three cabins, two acres, no Wi-Fi, one shared kitchen. Book yourself a real weekend.</p>
    <a href="#book" class="mt-8 inline-flex min-h-12 items-center border-2 border-ths10-ink bg-ths10-sun px-7 text-sm font-bold tracking-[0.04em] text-ths10-ink shadow-[4px_4px_0_var(--color-ths10-ink)] transition hover:translate-x-0.5 hover:translate-y-0.5 hover:shadow-[2px_2px_0_var(--color-ths10-ink)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths10-ink motion-reduce:transition-none">Check availability</a>
    <dl class="mx-auto mt-10 flex max-w-md flex-wrap justify-center divide-x divide-ths10-ink/15 font-ths10-mono text-xs text-ths10-body">
      <div class="px-5"><dt class="sr-only">Drive</dt><dd>2h from NYC</dd></div>
      <div class="px-5"><dt class="sr-only">From</dt><dd>from $180 / night</dd></div>
      <div class="px-5"><dt class="sr-only">Capacity</dt><dd>sleeps 2–6</dd></div>
    </dl>
  </div>
  <a href="#ths10-next" aria-label="Scroll to details" class="group absolute bottom-6 left-1/2 flex min-h-11 -translate-x-1/2 flex-col items-center gap-2 rounded-lg px-3 py-1 font-ths10-mono text-[10px] tracking-[0.2em] text-ths10-sage uppercase focus-visible:outline-2 focus-visible:outline-ths10-ink">
    <span>scroll</span>
    <span class="relative h-9 w-[22px] rounded-xl border-2 border-ths10-ink transition group-hover:border-ths10-honey"><span class="absolute top-1.5 left-1/2 h-[7px] w-[3px] -translate-x-1/2 animate-ths10-wheel rounded-sm bg-ths10-ink motion-reduce:animate-none"></span></span>
  </a>
</section>
<div id="ths10-next" class="grid h-40 place-items-center bg-ths10-ink font-ths10-mono text-xs tracking-[0.2em] text-ths10-bg uppercase">Next section</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths10-bg: #f3eadb;
  --color-ths10-bg: oklch(0.94 0.022 80.7);
  --color-ths10-glow: #d3dccb;
  --color-ths10-glow: oklch(0.883 0.025 129.9);
  --color-ths10-ink: #1e3a26;
  --color-ths10-ink: oklch(0.32 0.05 151.9);
  --color-ths10-body: #4a5b48;
  --color-ths10-body: oklch(0.451 0.037 142.1);
  --color-ths10-sage: #4f6d53;
  --color-ths10-sage: oklch(0.503 0.054 148.3);
  --color-ths10-honey: #9a6d22;
  --color-ths10-honey: oklch(0.568 0.105 75.8);
  --color-ths10-sun: #f4d35e;
  --color-ths10-sun: oklch(0.873 0.14 93.5);
  --font-ths10-serif: 'Cormorant Garamond', Georgia, serif;
  --font-ths10-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ths10-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ths10-wheel: ths10-wheel 1.4s ease-in-out infinite;

  @keyframes ths10-wheel {
    0%,
        100% {
      translate: 0 0;
      opacity: 1;
    }

    50% {
      translate: 0 10px;
      opacity: 0.35;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-10 {
  width: 100%;
  min-height: 100svh;
}
```
