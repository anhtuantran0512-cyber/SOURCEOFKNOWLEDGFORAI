---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-neumorphic-image-card-hover-effect/"
title: "Tailwind Neumorphic Image Card Hover Effect"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "Soft UI is two shadows going in opposite directions, and the port's win is that they become tokens: --shadow-tih08-out and --shadow-tih08-in in @theme mint…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neumorphic Image Card Hover Effect
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-neumorphic-image-card-hover-effect/

Soft UI is two shadows going in opposite directions, and the port's win is that they become tokens: --shadow-tih08-out and --shadow-tih08-in in @theme mint shadow-tih08-out and shadow-tih08-in, so the raised and pressed states are named rather than re-typed as eight-value strings on every card and button.
## HTML
```html
<section class="tih-08 w-full min-h-svh grid place-items-center bg-tih08-nm font-tih08-sans px-6 py-10" aria-label="Neumorphic image card hover demo">
  <div class="grid w-full max-w-195 gap-6 grid-cols-1 sm:grid-cols-3">
    <article class="group p-3 rounded-[20px] bg-tih08-nm shadow-tih08-out transition-[box-shadow,scale] duration-400 ease-tih08 hover:shadow-tih08-in hover:scale-98 motion-reduce:transition-none">
      <div class="relative aspect-square overflow-hidden rounded-xl shadow-tih08-well">
        <div class="absolute inset-0 grid place-items-center bg-[image:url('https://picsum.photos/seed/tih08-controller/600/600'),linear-gradient(135deg,oklch(0.22_0.09_285),oklch(0.31_0.14_280),oklch(0.45_0.19_275))] bg-cover bg-center bg-no-repeat transition-transform duration-400 ease-tih08 group-hover:scale-104 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
        </div>
      </div>
      <div class="pt-3 px-1">
        <h3 class="mb-0.75 text-[13px] font-bold text-tih08-text">Phantom Controller</h3>
        <p class="text-[11px] text-tih08-muted">Haptic &middot; Wireless &middot; 40h</p>
        <div class="flex items-center justify-between mt-2.5">
          <span class="text-[15px] font-bold text-tih08-acc tabular-nums">$89</span>
          <button type="button" class="px-3 py-1.25 rounded-full text-[10px] font-bold tracking-[0.06em] text-tih08-text bg-tih08-nm shadow-tih08-btn cursor-pointer transition-shadow duration-200 hover:shadow-tih08-in focus-visible:outline-2 focus-visible:outline-tih08-acc focus-visible:outline-offset-2 motion-reduce:transition-none">Add to Cart</button>
        </div>
      </div>
    </article>
    <article class="group p-3 rounded-[20px] bg-tih08-nm shadow-tih08-out transition-[box-shadow,scale] duration-400 ease-tih08 hover:shadow-tih08-in hover:scale-98 motion-reduce:transition-none">
      <div class="relative aspect-square overflow-hidden rounded-xl shadow-tih08-well">
        <div class="absolute inset-0 grid place-items-center bg-[image:url('https://picsum.photos/seed/tih08-headphones/600/600'),linear-gradient(135deg,oklch(0.29_0.07_240),oklch(0.38_0.1_238),oklch(0.75_0.12_230))] bg-cover bg-center bg-no-repeat transition-transform duration-400 ease-tih08 group-hover:scale-104 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
        </div>
      </div>
      <div class="pt-3 px-1">
        <h3 class="mb-0.75 text-[13px] font-bold text-tih08-text">AquaTone Studio</h3>
        <p class="text-[11px] text-tih08-muted">ANC &middot; Hi-Res &middot; 60h</p>
        <div class="flex items-center justify-between mt-2.5">
          <span class="text-[15px] font-bold text-tih08-acc tabular-nums">$229</span>
          <button type="button" class="px-3 py-1.25 rounded-full text-[10px] font-bold tracking-[0.06em] text-tih08-text bg-tih08-nm shadow-tih08-btn cursor-pointer transition-shadow duration-200 hover:shadow-tih08-in focus-visible:outline-2 focus-visible:outline-tih08-acc focus-visible:outline-offset-2 motion-reduce:transition-none">Add to Cart</button>
        </div>
      </div>
    </article>
    <article class="group p-3 rounded-[20px] bg-tih08-nm shadow-tih08-out transition-[box-shadow,scale] duration-400 ease-tih08 hover:shadow-tih08-in hover:scale-98 motion-reduce:transition-none">
      <div class="relative aspect-square overflow-hidden rounded-xl shadow-tih08-well">
        <div class="absolute inset-0 grid place-items-center bg-[image:url('https://picsum.photos/seed/tih08-laptop/600/600'),linear-gradient(135deg,oklch(0.25_0.13_305),oklch(0.4_0.2_300),oklch(0.63_0.21_300))] bg-cover bg-center bg-no-repeat transition-transform duration-400 ease-tih08 group-hover:scale-104 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
        </div>
      </div>
      <div class="pt-3 px-1">
        <h3 class="mb-0.75 text-[13px] font-bold text-tih08-text">NovaPad Ultra</h3>
        <p class="text-[11px] text-tih08-muted">OLED &middot; 12-core &middot; 18h</p>
        <div class="flex items-center justify-between mt-2.5">
          <span class="text-[15px] font-bold text-tih08-acc tabular-nums">$1,299</span>
          <button type="button" class="px-3 py-1.25 rounded-full text-[10px] font-bold tracking-[0.06em] text-tih08-text bg-tih08-nm shadow-tih08-btn cursor-pointer transition-shadow duration-200 hover:shadow-tih08-in focus-visible:outline-2 focus-visible:outline-tih08-acc focus-visible:outline-offset-2 motion-reduce:transition-none">Add to Cart</button>
        </div>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tih08-nm: #1e1e2a;
  --color-tih08-nm: oklch(0.22 0.02 285);
  --color-tih08-text: #e2e8f0;
  --color-tih08-text: oklch(0.92 0.01 250);
  --color-tih08-muted: #64748b;
  --color-tih08-muted: oklch(0.6 0.035 255);
  --color-tih08-acc: #6366f1;
  --color-tih08-acc: oklch(0.62 0.2 275);
  --font-tih08-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih08: cubic-bezier(0.25, 0.46, 0.45, 0.94);
  --shadow-tih08-out: 6px 6px 16px oklch(0 0 0 / 0.45), -4px -4px 12px oklch(1 0 0 / 0.05);
  --shadow-tih08-in: inset 4px 4px 10px oklch(0 0 0 / 0.45), inset -3px -3px 8px oklch(1 0 0 / 0.05);
  --shadow-tih08-well: inset 2px 2px 6px oklch(0 0 0 / 0.45), inset -1px -1px 4px oklch(1 0 0 / 0.05);
  --shadow-tih08-btn: 3px 3px 8px oklch(0 0 0 / 0.45), -2px -2px 6px oklch(1 0 0 / 0.05);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-08 {
  width: 100%;
  min-height: 100svh;
}

.tih-08 ::selection {
  background: oklch(0.62 0.2 275);
  color: #fff;
}
/* Safari inset-shadow-against-radius stability fix: a zero-alpha hairline border.
   No utility expresses "border that exists only to stabilise a repaint". */

.tih-08 [class*="rounded-"] {
  border: 1px solid transparent;
}
```
