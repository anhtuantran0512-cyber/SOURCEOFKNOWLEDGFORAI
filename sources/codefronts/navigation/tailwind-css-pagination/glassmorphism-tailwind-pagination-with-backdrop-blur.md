---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/glassmorphism-tailwind-pagination-with-backdrop-blur/"
title: "Glassmorphism Tailwind Pagination with Backdrop Blur"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "A frosted pagination pill floating over a photo gallery: backdrop-blur-xl backdrop-saturate-150 on a low-alpha fill, a lit hairline ring and an inset top…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Tailwind Pagination with Backdrop Blur
Source: https://codefronts.com/navigation/tailwind-css-pagination/glassmorphism-tailwind-pagination-with-backdrop-blur/

A frosted pagination pill floating over a photo gallery: backdrop-blur-xl backdrop-saturate-150 on a low-alpha fill, a lit hairline ring and an inset top highlight. The glass is applied only inside supports-[backdrop-filter:blur(1px)]:, so engines without the filter get an opaque, fully legible bar, and a short scrim under the pill &mdash; not over the whole photo &mdash; guarantees contrast in both themes.
## HTML
```html
<section class="tpg-19 w-full min-h-svh grid place-items-center bg-tpg19-bg bg-[radial-gradient(55%_45%_at_10%_10%,var(--color-tpg19-glowc),transparent_70%),radial-gradient(55%_45%_at_90%_90%,var(--color-tpg19-glowp),transparent_70%)] px-4 py-14 font-tpg19-sans text-tpg19-ink antialiased sm:px-5" aria-label="Glassmorphism pagination demo">
  <div class="grid w-full justify-items-center gap-7">
    <div class="w-full max-w-[56rem]">
      <header class="mb-4 flex flex-wrap items-end justify-between gap-x-6 gap-y-1 px-1">
        <div>
          <p class="font-tpg19-mono text-[11px] tracking-[0.12em] text-tpg19-hl uppercase">Collection</p>
          <h2 class="text-[1.75rem] leading-tight font-semibold tracking-[-0.03em]">Coastline, <span class="bg-linear-to-r from-tpg19-tx1 via-tpg19-tx2 to-tpg19-tx3 bg-clip-text text-transparent">Winter 2026</span></h2>
        </div>
        <p class="font-tpg19-mono text-xs text-tpg19-mut tabular-nums">Page 2 of 9 &middot; 216 photographs</p>
      </header>
      <div class="relative overflow-hidden rounded-[1.5rem] shadow-tpg19-frame ring-1 ring-tpg19-line">
        <ul class="grid grid-cols-3 gap-1 sm:gap-1.5">
          <li class="aspect-[4/5] sm:aspect-[4/3] bg-[oklch(0.62_0.07_220)]"><img class="size-full object-cover text-transparent" src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=480&amp;q=70&amp;auto=format&amp;fit=crop&amp;h=360" alt="Turquoise water breaking on an empty white-sand beach" width="480" height="360" loading="lazy" decoding="async"></li>
          <li class="aspect-[4/5] sm:aspect-[4/3] bg-[oklch(0.48_0.06_240)]"><img class="size-full object-cover text-transparent" src="https://images.unsplash.com/photo-1505142468610-359e7d316be0?w=480&amp;q=70&amp;auto=format&amp;fit=crop&amp;h=360" alt="A deep blue wave curling over in close-up" width="480" height="360" loading="lazy" decoding="async"></li>
          <li class="aspect-[4/5] sm:aspect-[4/3] bg-[oklch(0.74_0.06_70)]"><img class="size-full object-cover text-transparent" src="https://images.unsplash.com/photo-1519046904884-53103b34b206?w=480&amp;q=70&amp;auto=format&amp;fit=crop&amp;h=360" alt="Footprints across pale sand toward the shoreline" width="480" height="360" loading="lazy" decoding="async"></li>
          <li class="aspect-[4/5] sm:aspect-[4/3] bg-[oklch(0.56_0.08_200)]"><img class="size-full object-cover text-transparent" src="https://images.unsplash.com/photo-1500375592092-40eb2168fd21?w=480&amp;q=70&amp;auto=format&amp;fit=crop&amp;h=360" alt="Green-blue wave lit from behind by low sun" width="480" height="360" loading="lazy" decoding="async"></li>
          <li class="aspect-[4/5] sm:aspect-[4/3] bg-[oklch(0.68_0.05_50)]"><img class="size-full object-cover text-transparent" src="https://images.unsplash.com/photo-1473116763249-2faaef81ccda?w=480&amp;q=70&amp;auto=format&amp;fit=crop&amp;h=360" alt="Golden-hour beach with a soft haze over the sea" width="480" height="360" loading="lazy" decoding="async"></li>
          <li class="aspect-[4/5] sm:aspect-[4/3] bg-[oklch(0.42_0.05_250)]"><img class="size-full object-cover text-transparent" src="https://images.unsplash.com/photo-1471922694854-ff1b63b20054?w=480&amp;q=70&amp;auto=format&amp;fit=crop&amp;h=360" alt="Aerial view of surf lines rolling onto a long coast" width="480" height="360" loading="lazy" decoding="async"></li>
        </ul>
        <span aria-hidden="true" class="pointer-events-none absolute inset-x-0 bottom-0 h-2/5 bg-linear-to-t from-tpg19-scrim to-transparent"></span>
        <nav aria-label="Pagination" class="absolute inset-x-0 bottom-4 mx-auto flex w-fit max-w-[calc(100%-1.5rem)] items-center gap-1 rounded-[1.25rem] bg-tpg19-solid p-1.5 text-tpg19-glink shadow-tpg19-glass before:pointer-events-none before:absolute before:inset-0 before:rounded-[inherit] before:bg-linear-to-r before:from-tpg19-cy before:via-tpg19-vi before:to-tpg19-pk before:p-px before:[-webkit-mask-composite:xor] before:[-webkit-mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] before:[mask:linear-gradient(#000_0_0)_content-box_exclude,linear-gradient(#000_0_0)] supports-[backdrop-filter:blur(1px)]:bg-tpg19-glass supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl supports-[backdrop-filter:blur(1px)]:backdrop-saturate-150 sm:bottom-6">
          <a href="#tpg-19-p1" rel="prev" aria-label="Previous page" class="grid size-11 place-items-center rounded-xl transition duration-200 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-px hover:bg-tpg19-hover hover:text-tpg19-hl motion-reduce:hover:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg19-ring"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
          <span aria-hidden="true" class="h-6 w-px bg-linear-to-b from-transparent via-tpg19-edge to-transparent"></span>
          <ol class="flex items-center gap-0.5">
            <li><a href="#tpg-19-p1" aria-label="Page 1" class="grid h-11 min-w-11 place-items-center rounded-xl px-2 text-[15px] font-medium tabular-nums transition duration-200 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-px hover:bg-tpg19-hover hover:text-tpg19-hl motion-reduce:hover:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg19-ring">1</a></li>
            <li><a href="#tpg-19-p2" aria-label="Page 2" aria-current="page" class="grid h-11 min-w-11 place-items-center rounded-xl bg-linear-to-br from-tpg19-on1 via-tpg19-on2 to-tpg19-on3 px-2 text-[15px] font-bold text-tpg19-onink tabular-nums shadow-tpg19-on focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg19-ring">2</a></li>
            <li class="max-sm:hidden"><a href="#tpg-19-p3" aria-label="Page 3" class="grid h-11 min-w-11 place-items-center rounded-xl px-2 text-[15px] font-medium tabular-nums transition duration-200 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-px hover:bg-tpg19-hover hover:text-tpg19-hl motion-reduce:hover:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg19-ring">3</a></li>
            <li class="max-sm:hidden"><a href="#tpg-19-p4" aria-label="Page 4" class="grid h-11 min-w-11 place-items-center rounded-xl px-2 text-[15px] font-medium tabular-nums transition duration-200 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-px hover:bg-tpg19-hover hover:text-tpg19-hl motion-reduce:hover:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg19-ring">4</a></li>
            <li aria-hidden="true" class="grid h-11 w-6 place-items-center font-bold text-tpg19-gmut">&hellip;</li>
            <li><a href="#tpg-19-p9" aria-label="Page 9" class="grid h-11 min-w-11 place-items-center rounded-xl px-2 text-[15px] font-medium tabular-nums transition duration-200 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-px hover:bg-tpg19-hover hover:text-tpg19-hl motion-reduce:hover:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg19-ring">9</a></li>
          </ol>
          <span aria-hidden="true" class="h-6 w-px bg-linear-to-b from-transparent via-tpg19-edge to-transparent"></span>
          <a href="#tpg-19-p3" rel="next" aria-label="Next page" class="grid size-11 place-items-center rounded-xl transition duration-200 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-px hover:bg-tpg19-hover hover:text-tpg19-hl motion-reduce:hover:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg19-ring"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        </nav>
      </div>
    </div>
    <p aria-hidden="true" class="max-w-full rounded-2xl px-3.5 py-2 text-center font-tpg19-mono text-[11.5px] text-tpg19-mut ring-1 ring-tpg19-line">supports-[backdrop-filter:blur(1px)]: &middot; backdrop-blur-xl &middot; inset highlight</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg19-bg: #f2effb;
  --color-tpg19-bg: oklch(0.957 0.018 295);
  --color-tpg19-glowc: #a5f3fc80;
  --color-tpg19-glowc: oklch(0.91 0.08 205 / 0.5);
  --color-tpg19-glowp: #fbcfe880;
  --color-tpg19-glowp: oklch(0.89 0.07 345 / 0.5);
  --color-tpg19-ink: #1b1530;
  --color-tpg19-ink: oklch(0.22 0.05 295);
  --color-tpg19-mut: #5c5378;
  --color-tpg19-mut: oklch(0.47 0.06 295);
  --color-tpg19-hl: #6d28d9;
  --color-tpg19-hl: oklch(0.491 0.241 292.6);
  --color-tpg19-line: #e1dbf3;
  --color-tpg19-line: oklch(0.9 0.03 295);
  --color-tpg19-glass: #fbf8ffad;
  --color-tpg19-glass: oklch(0.985 0.012 300 / 0.68);
  --color-tpg19-solid: #f6f2fd;
  --color-tpg19-solid: oklch(0.97 0.014 300);
  --color-tpg19-edge: #8b5cf666;
  --color-tpg19-edge: oklch(0.606 0.25 292.7 / 0.4);
  --color-tpg19-hover: #efe5ffcc;
  --color-tpg19-hover: oklch(0.95 0.035 300 / 0.8);
  --color-tpg19-glink: #1b1530;
  --color-tpg19-glink: oklch(0.22 0.05 295);
  --color-tpg19-gmut: #7c3aed;
  --color-tpg19-gmut: oklch(0.541 0.247 293);
  --color-tpg19-cy: #22d3ee;
  --color-tpg19-cy: oklch(0.797 0.134 211.5);
  --color-tpg19-vi: #8b5cf6;
  --color-tpg19-vi: oklch(0.606 0.25 292.7);
  --color-tpg19-pk: #ec4899;
  --color-tpg19-pk: oklch(0.656 0.241 354.3);
  --color-tpg19-on1: #6d28d9;
  --color-tpg19-on1: oklch(0.491 0.241 292.6);
  --color-tpg19-on2: #a21caf;
  --color-tpg19-on2: oklch(0.518 0.222 323.9);
  --color-tpg19-on3: #be185d;
  --color-tpg19-on3: oklch(0.525 0.199 3.9);
  --color-tpg19-tx1: #6d28d9;
  --color-tpg19-tx1: oklch(0.491 0.241 292.6);
  --color-tpg19-tx2: #a21caf;
  --color-tpg19-tx2: oklch(0.518 0.222 323.9);
  --color-tpg19-tx3: #be185d;
  --color-tpg19-tx3: oklch(0.525 0.199 3.9);
  --color-tpg19-onink: #ffffff;
  --color-tpg19-onink: oklch(1 0 0);
  --color-tpg19-ring: #6d28d9;
  --color-tpg19-ring: oklch(0.491 0.241 292.6);
  --color-tpg19-scrim: #2a124566;
  --color-tpg19-scrim: oklch(0.25 0.08 300 / 0.4);
  --font-tpg19-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tpg19-mono: 'Space Mono', ui-monospace, monospace;
  --shadow-tpg19-frame: 0 1px 2px oklch(0.3 0.1 295 / 0.08), 0 28px 64px -26px oklch(0.45 0.2 300 / 0.45);
  --shadow-tpg19-glass: 0 14px 40px -8px oklch(0.25 0.12 300 / 0.5), inset 0 1px 0 oklch(1 0 0 / 0.5);
  --shadow-tpg19-on: 0 8px 22px -6px oklch(0.55 0.25 330 / 0.75), 0 0 0 1px oklch(1 0 0 / 0.18), inset 0 1px 0 oklch(1 0 0 / 0.35);
}

@media (prefers-color-scheme: dark) {
  .tpg-19:not([data-theme="light"]) {
    --color-tpg19-bg: #0d0a1c;
    --color-tpg19-bg: oklch(0.155 0.04 290);
    --color-tpg19-glowc: #0e749059;
    --color-tpg19-glowc: oklch(0.45 0.09 215 / 0.35);
    --color-tpg19-glowp: #83184359;
    --color-tpg19-glowp: oklch(0.4 0.14 350 / 0.35);
    --color-tpg19-ink: #f3f0ff;
    --color-tpg19-ink: oklch(0.96 0.02 295);
    --color-tpg19-mut: #b2a9d3;
    --color-tpg19-mut: oklch(0.76 0.06 295);
    --color-tpg19-hl: #c4b5fd;
    --color-tpg19-hl: oklch(0.811 0.111 293.6);
    --color-tpg19-line: #2a2346;
    --color-tpg19-line: oklch(0.28 0.06 295);
    --color-tpg19-glass: #1a143073;
    --color-tpg19-glass: oklch(0.21 0.05 292 / 0.45);
    --color-tpg19-solid: #211a38;
    --color-tpg19-solid: oklch(0.25 0.06 292);
    --color-tpg19-edge: #c4b5fd59;
    --color-tpg19-edge: oklch(0.811 0.111 293.6 / 0.35);
    --color-tpg19-hover: #a78bfa33;
    --color-tpg19-hover: oklch(0.709 0.159 293.5 / 0.22);
    --color-tpg19-glink: #ffffff;
    --color-tpg19-glink: oklch(1 0 0);
    --color-tpg19-tx1: #c4b5fd;
    --color-tpg19-tx1: oklch(0.811 0.111 293.6);
    --color-tpg19-tx2: #f0abfc;
    --color-tpg19-tx2: oklch(0.833 0.145 321.4);
    --color-tpg19-tx3: #fda4af;
    --color-tpg19-tx3: oklch(0.81 0.117 11.6);
    --color-tpg19-gmut: #f0abfc;
    --color-tpg19-gmut: oklch(0.833 0.145 321.4);
    --color-tpg19-ring: #f0abfc;
    --color-tpg19-ring: oklch(0.833 0.145 321.4);
    --color-tpg19-scrim: #0b0618b3;
    --color-tpg19-scrim: oklch(0.12 0.05 290 / 0.7);
  }
}

.tpg-19[data-theme="dark"] {
  --color-tpg19-bg: #0d0a1c;
  --color-tpg19-bg: oklch(0.155 0.04 290);
  --color-tpg19-glowc: #0e749059;
  --color-tpg19-glowc: oklch(0.45 0.09 215 / 0.35);
  --color-tpg19-glowp: #83184359;
  --color-tpg19-glowp: oklch(0.4 0.14 350 / 0.35);
  --color-tpg19-ink: #f3f0ff;
  --color-tpg19-ink: oklch(0.96 0.02 295);
  --color-tpg19-mut: #b2a9d3;
  --color-tpg19-mut: oklch(0.76 0.06 295);
  --color-tpg19-hl: #c4b5fd;
  --color-tpg19-hl: oklch(0.811 0.111 293.6);
  --color-tpg19-line: #2a2346;
  --color-tpg19-line: oklch(0.28 0.06 295);
  --color-tpg19-glass: #1a143073;
  --color-tpg19-glass: oklch(0.21 0.05 292 / 0.45);
  --color-tpg19-solid: #211a38;
  --color-tpg19-solid: oklch(0.25 0.06 292);
  --color-tpg19-edge: #c4b5fd59;
  --color-tpg19-edge: oklch(0.811 0.111 293.6 / 0.35);
  --color-tpg19-hover: #a78bfa33;
  --color-tpg19-hover: oklch(0.709 0.159 293.5 / 0.22);
  --color-tpg19-glink: #ffffff;
  --color-tpg19-glink: oklch(1 0 0);
  --color-tpg19-tx1: #c4b5fd;
  --color-tpg19-tx1: oklch(0.811 0.111 293.6);
  --color-tpg19-tx2: #f0abfc;
  --color-tpg19-tx2: oklch(0.833 0.145 321.4);
  --color-tpg19-tx3: #fda4af;
  --color-tpg19-tx3: oklch(0.81 0.117 11.6);
  --color-tpg19-gmut: #f0abfc;
  --color-tpg19-gmut: oklch(0.833 0.145 321.4);
  --color-tpg19-ring: #f0abfc;
  --color-tpg19-ring: oklch(0.833 0.145 321.4);
  --color-tpg19-scrim: #0b0618b3;
  --color-tpg19-scrim: oklch(0.12 0.05 290 / 0.7);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-19 {
  width: 100%;
  min-height: 100svh;
}
```
