---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-product-cards/tailwind-3d-flip-product-card-spec-back/"
title: "Pure-Tailwind 3D Flip Product Card with Spec Back"
section: "components"
category: "tailwind-css-product-cards"
category_name: "Tailwind CSS Product Cards"
description: "The apparel-and-gadget flip, and v4 finally has first-class utilities for it: transform-3d, rotate-y-180 and backface-hidden are real classes now, so the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure-Tailwind 3D Flip Product Card with Spec Back
Source: https://codefronts.com/components/tailwind-css-product-cards/tailwind-3d-flip-product-card-spec-back/

The apparel-and-gadget flip, and v4 finally has first-class utilities for it: transform-3d, rotate-y-180 and backface-hidden are real classes now, so the whole effect is four utilities and one arbitrary perspective. Hover or focus the card and it turns to a dark spec sheet with a real Add-to-Cart on the back.
## HTML
```html
<section class="tpc-02 w-full min-h-svh grid place-items-center bg-tpc02-bg font-tpc02-sans px-5 py-12" aria-label="3D flip product card demo">
  <article tabindex="0" aria-label="Trailhead GTX running shoe — hover or focus the card to read the specifications" class="group w-75 max-w-full [perspective:1100px] rounded-[18px] focus-visible:outline-3 focus-visible:outline-tpc02-acc focus-visible:outline-offset-4 focus:outline-none">
    <div class="relative h-105 transform-3d transition-transform duration-700 ease-tpc02 group-hover:rotate-y-180 group-focus-visible:rotate-y-180 motion-reduce:transition-none motion-reduce:group-hover:rotate-y-0 motion-reduce:group-focus-visible:rotate-y-0">
      <div class="absolute inset-0 flex flex-col rounded-[18px] overflow-hidden backface-hidden bg-tpc02-card shadow-[0_18px_44px_-22px_oklch(0.25_0.03_150/0.5)] motion-reduce:group-hover:opacity-0 motion-reduce:group-focus-visible:opacity-0">
        <div role="img" aria-label="Product photo: Trailhead GTX running shoe" class="flex-1 bg-linear-[135deg,var(--color-tpc02-ph),var(--color-tpc02-ph2)] bg-[url('https://images.unsplash.com/photo-1600185365926-3a2ce3cdb9eb?w=700&h=700&fit=crop&q=70')] bg-cover bg-center"></div>
        <div class="flex items-baseline justify-between px-5 pt-4 pb-1">
          <h3 class="text-[18px] font-semibold text-tpc02-ink">Trailhead GTX</h3>
          <p class="text-[18px] font-bold text-tpc02-acc tabular-nums">$189</p>
        </div>
        <p class="px-5 pb-4.5 font-tpc02-mono text-[11px] tracking-[0.16em] uppercase text-tpc02-dim">hover / focus to flip</p>
      </div>
      <div class="absolute inset-0 flex flex-col gap-4 rounded-[18px] overflow-hidden backface-hidden rotate-y-180 bg-tpc02-back text-tpc02-backink px-6 py-6.5 shadow-[0_18px_44px_-22px_oklch(0.25_0.03_150/0.5)]">
        <h3 class="text-[18px] font-semibold text-tpc02-backhi">Specifications</h3>
        <ul class="flex-1 flex flex-col gap-2.5 list-none">
          <li class="flex justify-between pb-2.5 text-sm border-b border-tpc02-backline"><span class="text-tpc02-backdim">Upper</span><b class="font-semibold text-tpc02-backhi">Recycled knit</b></li>
          <li class="flex justify-between pb-2.5 text-sm border-b border-tpc02-backline"><span class="text-tpc02-backdim">Drop</span><b class="font-semibold text-tpc02-backhi">8&nbsp;mm</b></li>
          <li class="flex justify-between pb-2.5 text-sm border-b border-tpc02-backline"><span class="text-tpc02-backdim">Weight</span><b class="font-semibold text-tpc02-backhi">272&nbsp;g</b></li>
          <li class="flex justify-between pb-2.5 text-sm border-b border-tpc02-backline"><span class="text-tpc02-backdim">Grip</span><b class="font-semibold text-tpc02-backhi">Vibram&reg; Megagrip</b></li>
        </ul>
        <button type="button" class="min-h-11 h-11.5 rounded-xl border-0 bg-tpc02-acc text-tpc02-onacc text-[15px] font-semibold cursor-pointer transition-colors duration-200 hover:bg-tpc02-acc2 focus-visible:outline-3 focus-visible:outline-tpc02-ring focus-visible:outline-offset-2 motion-reduce:transition-none">Add to Cart</button>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpc02-bg: #eef1ee;
  --color-tpc02-bg: oklch(0.95 0.008 150);
  --color-tpc02-card: #ffffff;
  --color-tpc02-card: oklch(1 0 0);
  --color-tpc02-ink: #101c14;
  --color-tpc02-ink: oklch(0.22 0.03 155);
  --color-tpc02-dim: #9aab9c;
  --color-tpc02-dim: oklch(0.71 0.02 150);
  --color-tpc02-ph: #e3ebe4;
  --color-tpc02-ph: oklch(0.93 0.012 150);
  --color-tpc02-ph2: #d5e0d6;
  --color-tpc02-ph2: oklch(0.89 0.018 150);
  --color-tpc02-back: #101c14;
  --color-tpc02-back: oklch(0.22 0.03 155);
  --color-tpc02-backink: #e7f0e9;
  --color-tpc02-backink: oklch(0.94 0.015 155);
  --color-tpc02-backhi: #ffffff;
  --color-tpc02-backhi: oklch(1 0 0);
  --color-tpc02-backdim: #9db6a6;
  --color-tpc02-backdim: oklch(0.74 0.03 155);
  --color-tpc02-backline: #2a3a30;
  --color-tpc02-backline: oklch(0.32 0.02 155);
  --color-tpc02-acc: #2f8a52;
  --color-tpc02-acc: oklch(0.55 0.15 155);
  --color-tpc02-acc2: #277a47;
  --color-tpc02-acc2: oklch(0.49 0.14 155);
  --color-tpc02-onacc: #ffffff;
  --color-tpc02-onacc: oklch(1 0 0);
  --color-tpc02-ring: #8fd0a6;
  --color-tpc02-ring: oklch(0.8 0.1 155);
  --font-tpc02-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tpc02-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-tpc02: cubic-bezier(0.2, 0.7, 0.2, 1);
}

.tpc-02 {
  width: 100%;
  min-height: 100svh;
}

.tpc-02 ::selection {
  background: var(--color-tpc02-acc);
  color: #fff;
}
```
