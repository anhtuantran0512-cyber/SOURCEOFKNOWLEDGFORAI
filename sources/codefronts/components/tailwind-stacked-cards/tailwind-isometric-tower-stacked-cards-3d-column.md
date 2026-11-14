---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-isometric-tower-stacked-cards-3d-column/"
title: "Tailwind Isometric Tower Stacked Cards 3D Column"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "Five floors on a steep isometric plane, each extruded by a before: slab so the column has real thickness."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Isometric Tower Stacked Cards 3D Column
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-isometric-tower-stacked-cards-3d-column/

Five floors on a steep isometric plane, each extruded by a before: slab so the column has real thickness. The shading is the interesting port: instead of five colour tokens, each floor computes its own fill from its index inside oklch() &mdash; calc(0.78-var(--i)*0.05) in the lightness slot &mdash; so the whole tonal ramp is one expression.
## HTML
```html
<section class="stk-22 w-full min-h-svh flex items-center justify-center px-5 py-[8vh] font-stk22-sans bg-stk22-bg [background-image:radial-gradient(circle_at_50%_30%,var(--color-stk22-glow),transparent_70%)]" aria-label="Isometric tower of cards">
  <div class="[perspective:1200px] has-focus-visible:outline-3 has-focus-visible:outline-stk22-ring has-focus-visible:outline-offset-[26px] has-focus-visible:rounded-lg">
    <div class="group relative w-50 h-75 outline-none [transform-style:preserve-3d] [transform:rotateX(58deg)_rotateZ(-42deg)]" tabindex="0" aria-hidden="true">
      <div class="absolute left-0 top-0 flex size-45 items-center justify-center rounded-[10px] p-3.5 shadow-[0_20px_30px_-16px_rgba(0,0,0,0.6)] [background-image:linear-gradient(160deg,oklch(calc(0.78-var(--i)*0.05)_0.09_240),oklch(calc(0.64-var(--i)*0.05)_0.11_250))] [transform:translateZ(calc(var(--i)*34px))] before:absolute before:left-0 before:bottom-0 before:h-8.5 before:w-full before:rounded-b-[10px] before:[background:oklch(calc(0.5-var(--i)*0.04)_0.1_250)] before:[transform:translateZ(-34px)] transition-transform duration-500 ease-stk22 group-hover:[transform:translateZ(calc(var(--i)*60px+10px))] group-focus-visible:[transform:translateZ(calc(var(--i)*60px+10px))] motion-reduce:transition-none" style="--i:0">
        <b class="text-center text-[15px] font-extrabold tracking-[0.02em] text-white [text-shadow:0_1px_2px_rgba(0,0,0,0.45)]">Rooftop</b>
      </div>
      <div class="absolute left-0 top-0 flex size-45 items-center justify-center rounded-[10px] p-3.5 shadow-[0_20px_30px_-16px_rgba(0,0,0,0.6)] [background-image:linear-gradient(160deg,oklch(calc(0.78-var(--i)*0.05)_0.09_240),oklch(calc(0.64-var(--i)*0.05)_0.11_250))] [transform:translateZ(calc(var(--i)*34px))] before:absolute before:left-0 before:bottom-0 before:h-8.5 before:w-full before:rounded-b-[10px] before:[background:oklch(calc(0.5-var(--i)*0.04)_0.1_250)] before:[transform:translateZ(-34px)] transition-transform duration-500 ease-stk22 group-hover:[transform:translateZ(calc(var(--i)*60px+10px))] group-focus-visible:[transform:translateZ(calc(var(--i)*60px+10px))] motion-reduce:transition-none" style="--i:1">
        <b class="text-center text-[15px] font-extrabold tracking-[0.02em] text-white [text-shadow:0_1px_2px_rgba(0,0,0,0.45)]">Sky lounge</b>
      </div>
      <div class="absolute left-0 top-0 flex size-45 items-center justify-center rounded-[10px] p-3.5 shadow-[0_20px_30px_-16px_rgba(0,0,0,0.6)] [background-image:linear-gradient(160deg,oklch(calc(0.78-var(--i)*0.05)_0.09_240),oklch(calc(0.64-var(--i)*0.05)_0.11_250))] [transform:translateZ(calc(var(--i)*34px))] before:absolute before:left-0 before:bottom-0 before:h-8.5 before:w-full before:rounded-b-[10px] before:[background:oklch(calc(0.5-var(--i)*0.04)_0.1_250)] before:[transform:translateZ(-34px)] transition-transform duration-500 ease-stk22 group-hover:[transform:translateZ(calc(var(--i)*60px+10px))] group-focus-visible:[transform:translateZ(calc(var(--i)*60px+10px))] motion-reduce:transition-none" style="--i:2">
        <b class="text-center text-[15px] font-extrabold tracking-[0.02em] text-white [text-shadow:0_1px_2px_rgba(0,0,0,0.45)]">Offices</b>
      </div>
      <div class="absolute left-0 top-0 flex size-45 items-center justify-center rounded-[10px] p-3.5 shadow-[0_20px_30px_-16px_rgba(0,0,0,0.6)] [background-image:linear-gradient(160deg,oklch(calc(0.78-var(--i)*0.05)_0.09_240),oklch(calc(0.64-var(--i)*0.05)_0.11_250))] [transform:translateZ(calc(var(--i)*34px))] before:absolute before:left-0 before:bottom-0 before:h-8.5 before:w-full before:rounded-b-[10px] before:[background:oklch(calc(0.5-var(--i)*0.04)_0.1_250)] before:[transform:translateZ(-34px)] transition-transform duration-500 ease-stk22 group-hover:[transform:translateZ(calc(var(--i)*60px+10px))] group-focus-visible:[transform:translateZ(calc(var(--i)*60px+10px))] motion-reduce:transition-none" style="--i:3">
        <b class="text-center text-[15px] font-extrabold tracking-[0.02em] text-white [text-shadow:0_1px_2px_rgba(0,0,0,0.45)]">Atrium</b>
      </div>
      <div class="absolute left-0 top-0 flex size-45 items-center justify-center rounded-[10px] p-3.5 shadow-[0_20px_30px_-16px_rgba(0,0,0,0.6)] [background-image:linear-gradient(160deg,oklch(calc(0.78-var(--i)*0.05)_0.09_240),oklch(calc(0.64-var(--i)*0.05)_0.11_250))] [transform:translateZ(calc(var(--i)*34px))] before:absolute before:left-0 before:bottom-0 before:h-8.5 before:w-full before:rounded-b-[10px] before:[background:oklch(calc(0.5-var(--i)*0.04)_0.1_250)] before:[transform:translateZ(-34px)] transition-transform duration-500 ease-stk22 group-hover:[transform:translateZ(calc(var(--i)*60px+10px))] group-focus-visible:[transform:translateZ(calc(var(--i)*60px+10px))] motion-reduce:transition-none" style="--i:4">
        <b class="text-center text-[15px] font-extrabold tracking-[0.02em] text-white [text-shadow:0_1px_2px_rgba(0,0,0,0.45)]">Lobby</b>
      </div>
    </div>
    <p class="sr-only">Tower floors, top to bottom: Rooftop, Sky lounge, Offices, Atrium, Lobby.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk22-bg: #0a0d15;
  --color-stk22-bg: oklch(0.13 0.016 265);
  --color-stk22-glow: #1a2030;
  --color-stk22-glow: oklch(0.24 0.026 265);
  --color-stk22-ring: #7fb2e8;
  --color-stk22-ring: oklch(0.70 0.12 240);
  --font-stk22-sans: 'Archivo', system-ui, sans-serif;
  --ease-stk22: cubic-bezier(0.3, 0.9, 0.3, 1);
}
```
