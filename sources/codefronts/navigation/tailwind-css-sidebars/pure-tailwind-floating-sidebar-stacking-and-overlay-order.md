---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/pure-tailwind-floating-sidebar-stacking-and-overlay-order/"
title: "Pure Tailwind Floating Sidebar Stacking and Overlay Order"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "A detached, glassy panel floating over the content &mdash; and the reason it is a machinery demo rather than a looks demo is isolate."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind Floating Sidebar Stacking and Overlay Order
Source: https://codefronts.com/navigation/tailwind-css-sidebars/pure-tailwind-floating-sidebar-stacking-and-overlay-order/

A detached, glassy panel floating over the content &mdash; and the reason it is a machinery demo rather than a looks demo is isolate. The scene declares itself a stacking context on purpose, so the panel's z- values are resolved locally and cannot be outranked by something unrelated elsewhere on the page. The whole thing is utilities, including the blur.
## HTML
```html
<section class="tsb-18 block relative w-full min-h-svh bg-tsb18-bg text-tsb18-ink font-tsb18-sans leading-[1.55]" aria-label="Nova stage">
  <div class="absolute top-3.5 right-3.5 z-90">
    <input class="tsb-18-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-18-theme">
    <label class="grid place-items-center w-11 h-11 rounded-[0.9rem] border border-tsb18-line bg-tsb18-surf text-tsb18-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-tsb18-acc peer-focus-visible:outline-offset-2" for="tsb-18-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="relative isolate overflow-hidden min-h-svh p-5 bg-tsb18-surf r46:p-8">
    <div class="min-w-0 pr-16 r46:pr-68 max-r32:pr-0" id="tsb-18-lib">
      <p class="m-0 mb-3.5 font-tsb18-display text-[0.78rem] tracking-[0.16em] uppercase text-tsb18-mut">Continue watching</p>
      <div class="grid grid-cols-[repeat(auto-fill,minmax(8.5rem,1fr))] gap-3 [&>article]:min-w-0 [&>article]:aspect-[3/4] [&>article]:flex [&>article]:flex-col [&>article]:justify-end [&>article]:gap-0.5 [&>article]:p-2.5 [&>article]:rounded-[0.8rem] [&>article]:bg-tsb18-bg [&>article]:border [&>article]:border-tsb18-line [&_p]:m-0 [&_p]:min-w-0 [&_p]:text-[0.88rem] [&_p]:font-semibold [&_span]:text-[0.74rem] [&_span]:text-tsb18-mut">
        <article class="!border-tsb18-acc"><p>Harbour Wall</p><span>ep 4</span></article>
        <article><p>Field Recordings</p><span>ep 11</span></article>
        <article><p>Slack Water</p><span>ep 2</span></article>
        <article><p>Kestrel</p><span>ep 7</span></article>
        <article><p>Two Bells</p><span>ep 1</span></article>
        <article><p>Low Tide</p><span>ep 9</span></article>
      </div>
    </div>

    <div class="absolute inset-0 z-20 pointer-events-none max-r32:static">
      <div class="absolute inset-0 z-30 bg-[oklch(14%_0.03_260/0.28)] max-r32:hidden" aria-hidden="true"></div>
      <nav class="absolute z-40 inset-y-6 right-6 w-[min(14.5rem,62%)] pointer-events-auto flex flex-col p-3 rounded-2xl border border-tsb18-line bg-tsb18-glass backdrop-blur-[14px] backdrop-saturate-150 shadow-[0_1.2rem_2.6rem_oklch(10%_0.02_260/0.45)] max-r32:static max-r32:w-full max-r32:mt-4" aria-label="Nova library">
        <p class="m-0 mb-2.5 font-tsb18-display text-[0.7rem] tracking-[0.18em] uppercase text-tsb18-mut">Library</p>
        <ul class="list-none m-0 p-0 grid gap-0.5">
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.7rem] text-[0.88rem] text-tsb18-ink no-underline hover:bg-tsb18-accsoft focus-visible:outline-2 focus-visible:outline-tsb18-acc focus-visible:outline-offset-2 aria-[current=page]:bg-tsb18-acc aria-[current=page]:text-tsb18-onacc aria-[current=page]:font-semibold" href="#tsb-18-lib" aria-current="page">Continue watching</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.7rem] text-[0.88rem] text-tsb18-ink no-underline hover:bg-tsb18-accsoft focus-visible:outline-2 focus-visible:outline-tsb18-acc focus-visible:outline-offset-2" href="#tsb-18-lib">My list</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.7rem] text-[0.88rem] text-tsb18-ink no-underline hover:bg-tsb18-accsoft focus-visible:outline-2 focus-visible:outline-tsb18-acc focus-visible:outline-offset-2" href="#tsb-18-lib">Downloads</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.7rem] text-[0.88rem] text-tsb18-ink no-underline hover:bg-tsb18-accsoft focus-visible:outline-2 focus-visible:outline-tsb18-acc focus-visible:outline-offset-2" href="#tsb-18-lib">Channels</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.7rem] text-[0.88rem] text-tsb18-ink no-underline hover:bg-tsb18-accsoft focus-visible:outline-2 focus-visible:outline-tsb18-acc focus-visible:outline-offset-2" href="#tsb-18-lib">Settings</a></li>
        </ul>
      </nav>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb18-bg: #070c1a;
  --color-tsb18-bg: oklch(13% 0.03 265);
  --color-tsb18-surf: #0e1730;
  --color-tsb18-surf: oklch(19% 0.04 265);
  --color-tsb18-glass: rgba(20, 32, 64, 0.62);
  --color-tsb18-glass: oklch(25% 0.05 265 / 0.62);
  --color-tsb18-line: #1f2c4d;
  --color-tsb18-line: oklch(28% 0.045 265);
  --color-tsb18-ink: #e8ecfa;
  --color-tsb18-ink: oklch(93% 0.015 265);
  --color-tsb18-mut: #8e9bc0;
  --color-tsb18-mut: oklch(67% 0.035 265);
  --color-tsb18-acc: #6ff2d0;
  --color-tsb18-acc: oklch(88% 0.13 172);
  --color-tsb18-accsoft: #10332f;
  --color-tsb18-accsoft: oklch(28% 0.05 172);
  --color-tsb18-onacc: #070c1a;
  --color-tsb18-onacc: oklch(13% 0.03 265);
  --font-tsb18-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tsb18-display: 'Barlow', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  --breakpoint-r32: 32rem;
  --breakpoint-r46: 46rem;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. */

.tsb-18 {
  width: 100%;
  min-height: 100svh;
}

.tsb-18 *,
.tsb-18 *::before,
.tsb-18 *::after {
  box-sizing: border-box;
}
/* Dark-first demo: the @theme block IS the dark palette, light mirror below. The glass
   token carries its own alpha, because backdrop-blur alone is not glass. */

.tsb-18:has(.tsb-18-theme-input:checked) {
  --color-tsb18-bg: #eef1f8;
  --color-tsb18-surf: #ffffff;
  --color-tsb18-glass: oklch(100% 0 0 / 0.68);
  --color-tsb18-line: #d3d9e8;
  --color-tsb18-ink: #101527;
  --color-tsb18-mut: #565f7a;
  --color-tsb18-acc: #0a6f5c;
  --color-tsb18-acc: oklch(46% 0.1 172);
  --color-tsb18-accsoft: #d3ece6;
  --color-tsb18-onacc: #ffffff;
}

@media (prefers-color-scheme: light) {
  .tsb-18 {
    --color-tsb18-bg: #eef1f8;
    --color-tsb18-surf: #ffffff;
    --color-tsb18-glass: oklch(100% 0 0 / 0.68);
    --color-tsb18-line: #d3d9e8;
    --color-tsb18-ink: #101527;
    --color-tsb18-mut: #565f7a;
    --color-tsb18-acc: #0a6f5c;
    --color-tsb18-acc: oklch(46% 0.1 172);
    --color-tsb18-accsoft: #d3ece6;
    --color-tsb18-onacc: #ffffff;
  }

  .tsb-18:has(.tsb-18-theme-input:checked) {
    --color-tsb18-bg: #070c1a;
    --color-tsb18-surf: #0e1730;
    --color-tsb18-glass: oklch(25% 0.05 265 / 0.62);
    --color-tsb18-line: #1f2c4d;
    --color-tsb18-ink: #e8ecfa;
    --color-tsb18-mut: #8e9bc0;
    --color-tsb18-acc: #6ff2d0;
    --color-tsb18-acc: oklch(88% 0.13 172);
    --color-tsb18-accsoft: #10332f;
    --color-tsb18-onacc: #070c1a;
  }
}

@media (prefers-color-scheme: dark) {
  .tsb-18:has(.tsb-18-theme-input:checked) {
    --color-tsb18-bg: #eef1f8;
    --color-tsb18-surf: #ffffff;
    --color-tsb18-glass: oklch(100% 0 0 / 0.68);
    --color-tsb18-line: #d3d9e8;
    --color-tsb18-ink: #101527;
    --color-tsb18-mut: #565f7a;
    --color-tsb18-acc: #0a6f5c;
    --color-tsb18-acc: oklch(46% 0.1 172);
    --color-tsb18-accsoft: #d3ece6;
    --color-tsb18-onacc: #ffffff;
  }
}
```
