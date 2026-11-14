---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-polaroid-photo-stack-scattered-rotate/"
title: "Tailwind Polaroid Photo Stack Scattered Rotate"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "Snapshots tossed on a table: thick white frames, handwritten captions, deliberate mess."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Polaroid Photo Stack Scattered Rotate
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-polaroid-photo-stack-scattered-rotate/

Snapshots tossed on a table: thick white frames, handwritten captions, deliberate mess. Each snap's position is three numbers on the element (--x, --y, --r) and hovering zeroes the rotation while raising z-10, so the one you are looking at pops clean out of the pile. The captions carry a --font-* theme entry, which is how a second typeface becomes font-stk12-hand rather than a one-off rule.
## HTML
```html
<section class="stk-12 w-full min-h-svh flex items-center justify-center px-5 py-15 font-stk12-sans bg-stk12-table" aria-label="Scattered Polaroid photos">
  <div class="relative w-[min(360px,90vw)] h-85">
    <figure class="absolute left-1/2 top-1/2 -ml-22.5 -mt-27.5 w-45 cursor-pointer rounded-[3px] bg-white p-3 pb-0 shadow-[0_16px_30px_-14px_rgba(40,30,10,0.6)] [transform:translate(var(--x),var(--y))_rotate(var(--r))] transition-[transform,box-shadow] duration-350 ease-stk12 hover:z-10 hover:shadow-[0_30px_50px_-18px_rgba(40,30,10,0.75)] hover:[transform:translate(var(--x),var(--y))_rotate(0deg)_scale(1.08)] focus-visible:z-10 focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_var(--color-stk12-ring),0_30px_50px_-18px_rgba(40,30,10,0.75)] focus-visible:[transform:translate(var(--x),var(--y))_rotate(0deg)_scale(1.08)] motion-reduce:hover:[transform:translate(var(--x),var(--y))_rotate(0deg)] motion-reduce:focus-visible:[transform:translate(var(--x),var(--y))_rotate(0deg)]" tabindex="0" style="--x:-90px;--y:-30px;--r:-8deg">
      <img class="block w-full h-37.5 object-cover" src="https://picsum.photos/seed/tw-pola-1/300/300" width="300" height="300" alt="Tent pitched beside a lake at dawn">
      <figcaption class="px-1 pt-3 pb-3.5 text-center font-stk12-hand text-base text-stk12-ink">Dawn, day 3</figcaption>
    </figure>
    <figure class="absolute left-1/2 top-1/2 -ml-22.5 -mt-27.5 w-45 cursor-pointer rounded-[3px] bg-white p-3 pb-0 shadow-[0_16px_30px_-14px_rgba(40,30,10,0.6)] [transform:translate(var(--x),var(--y))_rotate(var(--r))] transition-[transform,box-shadow] duration-350 ease-stk12 hover:z-10 hover:shadow-[0_30px_50px_-18px_rgba(40,30,10,0.75)] hover:[transform:translate(var(--x),var(--y))_rotate(0deg)_scale(1.08)] focus-visible:z-10 focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_var(--color-stk12-ring),0_30px_50px_-18px_rgba(40,30,10,0.75)] focus-visible:[transform:translate(var(--x),var(--y))_rotate(0deg)_scale(1.08)] motion-reduce:hover:[transform:translate(var(--x),var(--y))_rotate(0deg)] motion-reduce:focus-visible:[transform:translate(var(--x),var(--y))_rotate(0deg)]" tabindex="0" style="--x:30px;--y:-50px;--r:6deg">
      <img class="block w-full h-37.5 object-cover" src="https://picsum.photos/seed/tw-pola-2/300/300" width="300" height="300" alt="Two enamel mugs of coffee on a camp stove">
      <figcaption class="px-1 pt-3 pb-3.5 text-center font-stk12-hand text-base text-stk12-ink">First light coffee</figcaption>
    </figure>
    <figure class="absolute left-1/2 top-1/2 -ml-22.5 -mt-27.5 w-45 cursor-pointer rounded-[3px] bg-white p-3 pb-0 shadow-[0_16px_30px_-14px_rgba(40,30,10,0.6)] [transform:translate(var(--x),var(--y))_rotate(var(--r))] transition-[transform,box-shadow] duration-350 ease-stk12 hover:z-10 hover:shadow-[0_30px_50px_-18px_rgba(40,30,10,0.75)] hover:[transform:translate(var(--x),var(--y))_rotate(0deg)_scale(1.08)] focus-visible:z-10 focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_var(--color-stk12-ring),0_30px_50px_-18px_rgba(40,30,10,0.75)] focus-visible:[transform:translate(var(--x),var(--y))_rotate(0deg)_scale(1.08)] motion-reduce:hover:[transform:translate(var(--x),var(--y))_rotate(0deg)] motion-reduce:focus-visible:[transform:translate(var(--x),var(--y))_rotate(0deg)]" tabindex="0" style="--x:-40px;--y:40px;--r:4deg">
      <img class="block w-full h-37.5 object-cover" src="https://picsum.photos/seed/tw-pola-3/300/300" width="300" height="300" alt="Painted trail marker on a mountain path">
      <figcaption class="px-1 pt-3 pb-3.5 text-center font-stk12-hand text-base text-stk12-ink">Km 14</figcaption>
    </figure>
    <figure class="absolute left-1/2 top-1/2 -ml-22.5 -mt-27.5 w-45 cursor-pointer rounded-[3px] bg-white p-3 pb-0 shadow-[0_16px_30px_-14px_rgba(40,30,10,0.6)] [transform:translate(var(--x),var(--y))_rotate(var(--r))] transition-[transform,box-shadow] duration-350 ease-stk12 hover:z-10 hover:shadow-[0_30px_50px_-18px_rgba(40,30,10,0.75)] hover:[transform:translate(var(--x),var(--y))_rotate(0deg)_scale(1.08)] focus-visible:z-10 focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_var(--color-stk12-ring),0_30px_50px_-18px_rgba(40,30,10,0.75)] focus-visible:[transform:translate(var(--x),var(--y))_rotate(0deg)_scale(1.08)] motion-reduce:hover:[transform:translate(var(--x),var(--y))_rotate(0deg)] motion-reduce:focus-visible:[transform:translate(var(--x),var(--y))_rotate(0deg)]" tabindex="0" style="--x:80px;--y:30px;--r:-5deg">
      <img class="block w-full h-37.5 object-cover" src="https://picsum.photos/seed/tw-pola-4/300/300" width="300" height="300" alt="Sun setting behind a long ridge">
      <figcaption class="px-1 pt-3 pb-3.5 text-center font-stk12-hand text-base text-stk12-ink">Golden hour</figcaption>
    </figure>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk12-table: #cdbfa8;
  --color-stk12-table: oklch(0.81 0.032 80);
  --color-stk12-ink: #4a4030;
  --color-stk12-ink: oklch(0.38 0.025 80);
  --color-stk12-ring: #5b78e8;
  --color-stk12-ring: oklch(0.60 0.17 262);
  --font-stk12-sans: 'Archivo', system-ui, sans-serif;
  --font-stk12-hand: 'Caveat', 'Segoe Script', cursive;
  --ease-stk12: cubic-bezier(0.3, 0.9, 0.3, 1);
}
```
