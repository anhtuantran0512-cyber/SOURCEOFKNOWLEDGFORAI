---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-peel-back-corner-card-reveal/"
title: "Tailwind Peel Back Corner Card Reveal"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "A sticker-card that curls off its stack from the top-right corner, revealing the vivid layers beneath."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Peel Back Corner Card Reveal
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-peel-back-corner-card-reveal/

A sticker-card that curls off its stack from the top-right corner, revealing the vivid layers beneath. The port swaps animated clip-path for a rotate-scale-and-radius peel, which is the better engineering call: clip-path only interpolates between polygons with matching vertex counts, while a transform plus one asymmetric border-radius gets the same read and stays on the compositor.
## HTML
```html
<section class="stk-34 grid w-full min-h-svh place-items-center px-5 py-15 font-stk34-sans bg-stk34-bg" aria-label="Peel-back card stack">
  <div class="group relative h-85 w-65">
    <div class="absolute inset-0 z-1 flex flex-col justify-end overflow-hidden rounded-[22px] bg-linear-[150deg,var(--color-stk34-c3a),var(--color-stk34-c3b)] p-7.5 text-stk34-deep shadow-[0_12px_26px_rgba(0,0,0,0.18)]">
      <h3 class="m-0 font-stk34-display text-3xl font-extrabold leading-none">Layer C</h3>
      <p class="m-0 mt-1.5 opacity-85">Bottom of the stack</p>
    </div>
    <div class="absolute inset-0 z-2 flex flex-col justify-end overflow-hidden rounded-[22px] bg-linear-[150deg,var(--color-stk34-c2a),var(--color-stk34-c2b)] p-7.5 text-white shadow-[0_12px_26px_rgba(0,0,0,0.18)] transition-transform duration-700 ease-stk34 group-hover:-translate-y-2.5 motion-reduce:transition-none motion-reduce:translate-none!">
      <h3 class="m-0 font-stk34-display text-3xl font-extrabold leading-none">Layer B</h3>
      <p class="m-0 mt-1.5 opacity-85">The middle ground</p>
    </div>
    <div class="absolute inset-0 z-3 flex cursor-pointer flex-col justify-end overflow-hidden rounded-[22px] bg-linear-[150deg,var(--color-stk34-c1a),var(--color-stk34-c1b)] p-7.5 text-white shadow-[0_12px_26px_rgba(0,0,0,0.18)] [transform-origin:top_right] transition-[transform,border-radius,box-shadow,opacity] duration-700 ease-stk34 group-hover:rounded-bl-[90px] group-hover:shadow-[-20px_20px_40px_rgba(0,0,0,0.3)] group-hover:[transform:rotate(-14deg)_translate(-30px,-30px)_scale(0.78)] motion-reduce:transition-opacity motion-reduce:rotate-none! motion-reduce:translate-none! motion-reduce:scale-100! motion-reduce:group-hover:opacity-0">
      <h3 class="m-0 font-stk34-display text-3xl font-extrabold leading-none">Peel me</h3>
      <p class="m-0 mt-1.5 opacity-85">Hover to lift the top</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk34-bg: #ececec;
  --color-stk34-bg: oklch(0.94 0.001 0);
  --color-stk34-deep: #044d33;
  --color-stk34-deep: oklch(0.35 0.080 165);
  --color-stk34-c1a: #ff6a3d;
  --color-stk34-c1b: #f9484a;
  --color-stk34-c2a: #1fa2ff;
  --color-stk34-c2b: #12d8fa;
  --color-stk34-c3a: #43e97b;
  --color-stk34-c3b: #38f9d7;
  --font-stk34-sans: 'Outfit', system-ui, sans-serif;
  --font-stk34-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --ease-stk34: cubic-bezier(0.2, 0.8, 0.2, 1);
}
```
