---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-isometric-overlapping-stacked-cards/"
title: "Tailwind Isometric Overlapping Stacked Cards"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "Three pricing planes floated on a true isometric grid, sliding apart on hover so every price stays readable."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Isometric Overlapping Stacked Cards
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-isometric-overlapping-stacked-cards/

Three pricing planes floated on a true isometric grid, sliding apart on hover so every price stays readable. The port keeps the geometry in arbitrary properties where it belongs, and the accessibility work is the substantive part: prices are legible at rest, and under reduced motion the whole plane flattens to rotate-none rather than merely animating slower.
## HTML
```html
<section class="stk-31 grid w-full min-h-svh place-items-center px-5 py-15 font-stk31-mono bg-stk31-bg [background-image:radial-gradient(circle_at_50%_30%,var(--color-stk31-glow),transparent_70%)]" aria-label="Pricing plans, isometric view">
  <div class="group relative h-105 w-85 [perspective:1400px]">
    <div class="relative size-full [transform-style:preserve-3d] [transform:rotateX(52deg)_rotateZ(-34deg)] transition-transform duration-700 ease-stk31 group-hover:[transform:rotateX(46deg)_rotateZ(-28deg)] motion-reduce:transition-none motion-reduce:rotate-none!">
      <div class="absolute left-12.5 top-30 flex h-37.5 w-60 flex-col justify-between rounded-[18px] p-5.5 text-stk31-dark [transform-style:preserve-3d] bg-linear-[135deg,var(--color-stk31-t3a),var(--color-stk31-t3b)] shadow-[0_36px_60px_rgba(0,0,0,0.55)] [transform:translateZ(12px)] transition-transform duration-650 ease-stk31 group-hover:[transform:translateZ(12px)_translate(150px,150px)] motion-reduce:transition-none motion-reduce:rotate-none!">
        <span class="font-stk31-display text-[1.15rem] font-bold tracking-[0.04em]">SCALE</span>
        <span class="text-[0.72rem] leading-relaxed opacity-90">Unlimited seats &middot; SSO &middot; SLA</span>
        <span class="font-stk31-display text-[2.1rem] font-bold leading-none">$79<small class="text-[0.85rem] opacity-75">/mo</small></span>
      </div>
      <div class="absolute left-12.5 top-30 flex h-37.5 w-60 flex-col justify-between rounded-[18px] p-5.5 text-white [transform-style:preserve-3d] bg-linear-[135deg,var(--color-stk31-t2a),var(--color-stk31-t2b)] shadow-[0_36px_60px_rgba(0,0,0,0.55)] [transform:translateZ(24px)] transition-transform duration-650 ease-stk31 motion-reduce:transition-none motion-reduce:rotate-none!">
        <span class="font-stk31-display text-[1.15rem] font-bold tracking-[0.04em]">GROWTH</span>
        <span class="text-[0.72rem] leading-relaxed opacity-90">10 seats &middot; analytics &middot; API</span>
        <span class="font-stk31-display text-[2.1rem] font-bold leading-none">$29<small class="text-[0.85rem] opacity-75">/mo</small></span>
      </div>
      <div class="absolute left-12.5 top-30 flex h-37.5 w-60 flex-col justify-between rounded-[18px] p-5.5 text-white [transform-style:preserve-3d] bg-linear-[135deg,var(--color-stk31-t1a),var(--color-stk31-t1b)] shadow-[0_36px_60px_rgba(0,0,0,0.55)] [transform:translateZ(36px)] transition-transform duration-650 ease-stk31 group-hover:[transform:translateZ(36px)_translate(-150px,-150px)] motion-reduce:transition-none motion-reduce:rotate-none!">
        <span class="font-stk31-display text-[1.15rem] font-bold tracking-[0.04em]">STARTER</span>
        <span class="text-[0.72rem] leading-relaxed opacity-90">1 seat &middot; core features</span>
        <span class="font-stk31-display text-[2.1rem] font-bold leading-none">$9<small class="text-[0.85rem] opacity-75">/mo</small></span>
      </div>
    </div>
    <span class="absolute bottom-2.5 left-1/2 -translate-x-1/2 text-[0.72rem] tracking-[0.18em] text-stk31-hint transition-opacity duration-400 group-hover:opacity-0">HOVER TO COMPARE PLANS</span>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk31-bg: #0a0c14;
  --color-stk31-bg: oklch(0.13 0.016 275);
  --color-stk31-glow: #191d2e;
  --color-stk31-glow: oklch(0.23 0.028 275);
  --color-stk31-hint: #5b6480;
  --color-stk31-hint: oklch(0.52 0.030 275);
  --color-stk31-dark: #03241c;
  --color-stk31-dark: oklch(0.24 0.050 165);
  --color-stk31-t1a: #3a4cf0;
  --color-stk31-t1b: #6d7cff;
  --color-stk31-t2a: #f0466b;
  --color-stk31-t2b: #ff7aa0;
  --color-stk31-t3a: #11b894;
  --color-stk31-t3b: #46f0c4;
  --font-stk31-mono: 'DM Mono', ui-monospace, monospace;
  --font-stk31-display: 'Space Grotesk', system-ui, sans-serif;
  --ease-stk31: cubic-bezier(0.3, 0.9, 0.3, 1);
}
```
