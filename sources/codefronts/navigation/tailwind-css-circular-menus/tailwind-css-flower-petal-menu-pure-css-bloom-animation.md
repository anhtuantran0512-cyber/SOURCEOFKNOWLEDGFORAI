---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-flower-petal-menu-pure-css-bloom-animation/"
title: "Tailwind CSS Flower Petal Menu (Pure CSS Bloom Animation)"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "A navigation that blooms for a florist: five petal-shaped links unfold from a leaf-green bud, each petal cut by one asymmetric radius &mdash;…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Flower Petal Menu (Pure CSS Bloom Animation)
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-flower-petal-menu-pure-css-bloom-animation/

A navigation that blooms for a florist: five petal-shaped links unfold from a leaf-green bud, each petal cut by one asymmetric radius &mdash; rounded-[50%_50%_50%_10%] &mdash; and turned with rotate-45 so the sharp corner points at the stem. A checkbox and group-has-checked/flower: drive the whole bloom; no JavaScript.
## HTML
```html
<section class="tcm-10 w-full min-h-svh grid place-items-center bg-tcm10-bg bg-[radial-gradient(55%_50%_at_50%_55%,var(--color-tcm10-glow),transparent_72%)] px-5 py-14 font-tcm10-sans text-tcm10-ink antialiased" aria-label="Flower petal menu demo">
  <div class="grid w-full justify-items-center gap-8">
    <header class="grid justify-items-center gap-2 text-center">
      <p class="font-tcm10-mono text-[11px] tracking-[0.2em] text-tcm10-leaf-ink uppercase">Petal &amp; Stem · Florist</p>
      <h2 class="font-tcm10-serif text-[clamp(2rem,5.5vw,2.9rem)] leading-[1.02] font-medium tracking-[-0.02em]">Let the menu <em class="text-tcm10-p2-ink">bloom</em></h2>
    </header>
    <nav class="group/flower relative grid size-[20rem] place-items-center" aria-label="Florist menu">
      <span aria-hidden="true" class="absolute size-56 rounded-full bg-tcm10-p1/20 blur-3xl scale-50 transition-[scale] duration-700 group-has-checked/flower:scale-100"></span>
      <input type="checkbox" id="tcm-10-toggle" class="sr-only" aria-label="Open florist menu">
      <ul class="absolute inset-0">
        <li class="pointer-events-none absolute inset-0 rotate-[calc(var(--i)*72deg)] [--i:0]">
          <a href="#tcm-10-shop" class="pointer-events-auto absolute top-1/2 left-1/2 -m-12 block size-24 rounded-[50%_50%_50%_10%] bg-linear-to-br from-tcm10-p1 to-tcm10-p2 shadow-tcm10-petal rotate-45 translate-y-0 scale-0 opacity-0 invisible transition-[translate,scale,opacity,visibility,filter] duration-600 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*50ms)] group-has-checked/flower:-translate-y-[5.9rem] group-has-checked/flower:scale-100 group-has-checked/flower:opacity-100 group-has-checked/flower:visible hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tcm10-ring motion-reduce:transition-none">
            <span class="absolute inset-0 grid place-content-center justify-items-center gap-1 rotate-[calc(-45deg-var(--i)*72deg)] text-[12.5px] font-semibold tracking-[0.02em] text-white [text-shadow:0_1px_2px_oklch(0.4_0.15_350/0.5)]"><svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M6 8h12l-1 12H7zM9 8a3 3 0 0 1 6 0"/></svg>Shop</span>
          </a>
        </li>
        <li class="pointer-events-none absolute inset-0 rotate-[calc(var(--i)*72deg)] [--i:1]">
          <a href="#tcm-10-care" class="pointer-events-auto absolute top-1/2 left-1/2 -m-12 block size-24 rounded-[50%_50%_50%_10%] bg-linear-to-br from-tcm10-p1 to-tcm10-p2 shadow-tcm10-petal rotate-45 translate-y-0 scale-0 opacity-0 invisible transition-[translate,scale,opacity,visibility,filter] duration-600 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*50ms)] group-has-checked/flower:-translate-y-[5.9rem] group-has-checked/flower:scale-100 group-has-checked/flower:opacity-100 group-has-checked/flower:visible hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tcm10-ring motion-reduce:transition-none">
            <span class="absolute inset-0 grid place-content-center justify-items-center gap-1 rotate-[calc(-45deg-var(--i)*72deg)] text-[12.5px] font-semibold tracking-[0.02em] text-white [text-shadow:0_1px_2px_oklch(0.4_0.15_350/0.5)]"><svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 20s-7-4.4-9.3-8.8A5.2 5.2 0 0 1 12 6.4a5.2 5.2 0 0 1 9.3 4.8C19 15.6 12 20 12 20z"/></svg>Care</span>
          </a>
        </li>
        <li class="pointer-events-none absolute inset-0 rotate-[calc(var(--i)*72deg)] [--i:2]">
          <a href="#tcm-10-gifts" class="pointer-events-auto absolute top-1/2 left-1/2 -m-12 block size-24 rounded-[50%_50%_50%_10%] bg-linear-to-br from-tcm10-p1 to-tcm10-p2 shadow-tcm10-petal rotate-45 translate-y-0 scale-0 opacity-0 invisible transition-[translate,scale,opacity,visibility,filter] duration-600 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*50ms)] group-has-checked/flower:-translate-y-[5.9rem] group-has-checked/flower:scale-100 group-has-checked/flower:opacity-100 group-has-checked/flower:visible hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tcm10-ring motion-reduce:transition-none">
            <span class="absolute inset-0 grid place-content-center justify-items-center gap-1 rotate-[calc(-45deg-var(--i)*72deg)] text-[12.5px] font-semibold tracking-[0.02em] text-white [text-shadow:0_1px_2px_oklch(0.4_0.15_350/0.5)]"><svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 9h16v4H4zM6 13h12v8H6zM12 9v12M12 9C9 9 7.5 7.5 7.5 6A2.5 2.5 0 0 1 12 4.5 2.5 2.5 0 0 1 16.5 6C16.5 7.5 15 9 12 9z"/></svg>Gifts</span>
          </a>
        </li>
        <li class="pointer-events-none absolute inset-0 rotate-[calc(var(--i)*72deg)] [--i:3]">
          <a href="#tcm-10-events" class="pointer-events-auto absolute top-1/2 left-1/2 -m-12 block size-24 rounded-[50%_50%_50%_10%] bg-linear-to-br from-tcm10-p1 to-tcm10-p2 shadow-tcm10-petal rotate-45 translate-y-0 scale-0 opacity-0 invisible transition-[translate,scale,opacity,visibility,filter] duration-600 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*50ms)] group-has-checked/flower:-translate-y-[5.9rem] group-has-checked/flower:scale-100 group-has-checked/flower:opacity-100 group-has-checked/flower:visible hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tcm10-ring motion-reduce:transition-none">
            <span class="absolute inset-0 grid place-content-center justify-items-center gap-1 rotate-[calc(-45deg-var(--i)*72deg)] text-[12.5px] font-semibold tracking-[0.02em] text-white [text-shadow:0_1px_2px_oklch(0.4_0.15_350/0.5)]"><svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 5h14v15H5zM5 9h14M9 3v4M15 3v4"/></svg>Events</span>
          </a>
        </li>
        <li class="pointer-events-none absolute inset-0 rotate-[calc(var(--i)*72deg)] [--i:4]">
          <a href="#tcm-10-visit" class="pointer-events-auto absolute top-1/2 left-1/2 -m-12 block size-24 rounded-[50%_50%_50%_10%] bg-linear-to-br from-tcm10-p1 to-tcm10-p2 shadow-tcm10-petal rotate-45 translate-y-0 scale-0 opacity-0 invisible transition-[translate,scale,opacity,visibility,filter] duration-600 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*50ms)] group-has-checked/flower:-translate-y-[5.9rem] group-has-checked/flower:scale-100 group-has-checked/flower:opacity-100 group-has-checked/flower:visible hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tcm10-ring motion-reduce:transition-none">
            <span class="absolute inset-0 grid place-content-center justify-items-center gap-1 rotate-[calc(-45deg-var(--i)*72deg)] text-[12.5px] font-semibold tracking-[0.02em] text-white [text-shadow:0_1px_2px_oklch(0.4_0.15_350/0.5)]"><svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 21c4-4.5 7-7.8 7-11.5a7 7 0 1 0-14 0C5 13.2 8 16.5 12 21zM12 7a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5z"/></svg>Visit</span>
          </a>
        </li>
      </ul>
      <label for="tcm-10-toggle" aria-hidden="true" class="relative z-10 grid size-20 cursor-pointer place-items-center rounded-full bg-[radial-gradient(circle_at_35%_30%,var(--color-tcm10-leaf-hi),var(--color-tcm10-leaf))] text-white shadow-tcm10-bud transition-[rotate,scale] duration-700 ease-[cubic-bezier(.34,1.45,.5,1)] hover:scale-105 group-has-checked/flower:rotate-180 group-has-focus-visible/flower:outline-2 group-has-focus-visible/flower:outline-offset-4 group-has-focus-visible/flower:outline-tcm10-ring motion-reduce:transition-none">
        <svg viewBox="0 0 24 24" class="size-9" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" aria-hidden="true"><path d="M12 8.8C10 7 10 4.5 12 3c2 1.5 2 4 0 5.8zM15.2 12c1.8-2 4.3-2 5.8 0-1.5 2-4 2-5.8 0zM12 15.2c2 1.8 2 4.3 0 5.8-2-1.5-2-4 0-5.8zM8.8 12c-1.8 2-4.3 2-5.8 0 1.5-2 4-2 5.8 0zM12 9.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5z"/></svg>
      </label>
    </nav>
    <p class="text-[13px] text-tcm10-mut">Tap the bud &mdash; five petals, no JavaScript</p>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm10-card px-3.5 py-2 text-center font-tcm10-mono text-[11.5px] text-tcm10-mut ring-1 ring-tcm10-line ">rounded-[50%_50%_50%_10%] · rotate-45 · group-has-checked/flower:-translate-y-[5.9rem]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm10-bg: #f8f6ef;
  --color-tcm10-bg: oklch(0.973 0.01 93.6);
  --color-tcm10-glow: #fbcfe8a6;
  --color-tcm10-glow: oklch(0.899 0.059 343.2 / 0.65);
  --color-tcm10-ink: #24201a;
  --color-tcm10-ink: oklch(0.246 0.013 78);
  --color-tcm10-mut: #6a6255;
  --color-tcm10-mut: oklch(0.5 0.022 80);
  --color-tcm10-p1: #f472b6;
  --color-tcm10-p1: oklch(0.725 0.175 349.8);
  --color-tcm10-p2: #be185d;
  --color-tcm10-p2: oklch(0.525 0.199 4);
  --color-tcm10-p2-ink: #be185d;
  --color-tcm10-p2-ink: oklch(0.525 0.199 4);
  --color-tcm10-leaf: #3f7d3a;
  --color-tcm10-leaf: oklch(0.532 0.119 142.3);
  --color-tcm10-leaf-hi: #7cb26a;
  --color-tcm10-leaf-hi: oklch(0.708 0.116 138.2);
  --color-tcm10-leaf-ink: #3f6b2f;
  --color-tcm10-leaf-ink: oklch(0.481 0.102 138);
  --color-tcm10-ring: #be185d;
  --color-tcm10-ring: oklch(0.525 0.199 4);
  --color-tcm10-card: #fffdf8;
  --color-tcm10-card: oklch(0.994 0.007 88.6);
  --color-tcm10-line: #ebe5d6;
  --color-tcm10-line: oklch(0.923 0.021 88.7);
  --font-tcm10-sans: 'DM Sans', system-ui, sans-serif;
  --font-tcm10-serif: 'Fraunces', Georgia, serif;
  --font-tcm10-mono: 'DM Mono', ui-monospace, monospace;
  --shadow-tcm10-petal: 0 12px 26px -12px oklch(0.55 0.2 350 / 0.6), inset 0 1px 0 oklch(1 0 0 / 0.35);
  --shadow-tcm10-bud: 0 14px 30px -10px oklch(0.45 0.1 140 / 0.7), inset 0 1px 0 oklch(1 0 0 / 0.3);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-10 {
  width: 100%;
  min-height: 100svh;
}
/* Dark theme: night garden: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-10:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm10-bg: #14120d;
    --color-tcm10-bg: oklch(0.183 0.01 88.8);
    --color-tcm10-glow: #9d174d4d;
    --color-tcm10-glow: oklch(0.459 0.17 3.8 / 0.3);
    --color-tcm10-ink: #f6f1e6;
    --color-tcm10-ink: oklch(0.959 0.016 86.4);
    --color-tcm10-mut: #b8ad99;
    --color-tcm10-mut: oklch(0.751 0.031 82.6);
    --color-tcm10-p1: #f472b6;
    --color-tcm10-p1: oklch(0.725 0.175 349.8);
    --color-tcm10-p2: #be185d;
    --color-tcm10-p2: oklch(0.525 0.199 4);
    --color-tcm10-p2-ink: #f9a8d4;
    --color-tcm10-p2-ink: oklch(0.823 0.11 346);
    --color-tcm10-leaf: #3f7d3a;
    --color-tcm10-leaf: oklch(0.532 0.119 142.3);
    --color-tcm10-leaf-hi: #86c16f;
    --color-tcm10-leaf-hi: oklch(0.751 0.128 137.4);
    --color-tcm10-leaf-ink: #a3d58f;
    --color-tcm10-leaf-ink: oklch(0.821 0.108 137);
    --color-tcm10-ring: #f9a8d4;
    --color-tcm10-ring: oklch(0.823 0.11 346);
    --color-tcm10-card: #1f1c15;
    --color-tcm10-card: oklch(0.227 0.014 87.6);
    --color-tcm10-line: #352f24;
    --color-tcm10-line: oklch(0.308 0.021 82.6);
  }
}

.tcm-10[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm10-bg: #14120d;
  --color-tcm10-bg: oklch(0.183 0.01 88.8);
  --color-tcm10-glow: #9d174d4d;
  --color-tcm10-glow: oklch(0.459 0.17 3.8 / 0.3);
  --color-tcm10-ink: #f6f1e6;
  --color-tcm10-ink: oklch(0.959 0.016 86.4);
  --color-tcm10-mut: #b8ad99;
  --color-tcm10-mut: oklch(0.751 0.031 82.6);
  --color-tcm10-p1: #f472b6;
  --color-tcm10-p1: oklch(0.725 0.175 349.8);
  --color-tcm10-p2: #be185d;
  --color-tcm10-p2: oklch(0.525 0.199 4);
  --color-tcm10-p2-ink: #f9a8d4;
  --color-tcm10-p2-ink: oklch(0.823 0.11 346);
  --color-tcm10-leaf: #3f7d3a;
  --color-tcm10-leaf: oklch(0.532 0.119 142.3);
  --color-tcm10-leaf-hi: #86c16f;
  --color-tcm10-leaf-hi: oklch(0.751 0.128 137.4);
  --color-tcm10-leaf-ink: #a3d58f;
  --color-tcm10-leaf-ink: oklch(0.821 0.108 137);
  --color-tcm10-ring: #f9a8d4;
  --color-tcm10-ring: oklch(0.823 0.11 346);
  --color-tcm10-card: #1f1c15;
  --color-tcm10-card: oklch(0.227 0.014 87.6);
  --color-tcm10-line: #352f24;
  --color-tcm10-line: oklch(0.308 0.021 82.6);
}
```
