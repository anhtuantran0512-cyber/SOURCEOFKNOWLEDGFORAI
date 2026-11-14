---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-ecommerce-product-image-swap-on-hover/"
title: "Tailwind E-Commerce Product Image Swap on Hover"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "The shopping-grid cross-dissolve: two stacked layers, one fading out as the other fades in, with a half-percent scale difference that keeps it from reading…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind E-Commerce Product Image Swap on Hover
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-ecommerce-product-image-swap-on-hover/

The shopping-grid cross-dissolve: two stacked layers, one fading out as the other fades in, with a half-percent scale difference that keeps it from reading as a flat dip. Both layers state their resting and hovered geometry on themselves, so the pair can never drift out of sync &mdash; which is the entire failure mode of this pattern.
## HTML
```html
<section class="tih-03 w-full min-h-svh grid place-items-center bg-tih03-bg font-tih03-sans px-6 py-10" aria-label="Product image swap on hover demo">
  <div class="grid w-full max-w-195 gap-4 grid-cols-1 sm:grid-cols-3">
    <article class="group overflow-hidden rounded-[14px] bg-tih03-card border border-[oklch(1_0_0/0.07)] transition-shadow duration-300 hover:shadow-[0_16px_48px_oklch(0_0_0/0.4)] motion-reduce:transition-none">
      <div class="relative aspect-square overflow-hidden">
        <div class="absolute inset-0 z-1 grid place-items-center opacity-100 scale-100 bg-[image:url('https://picsum.photos/seed/tih03-runner-a/600/600'),linear-gradient(135deg,oklch(0.22_0.09_285),oklch(0.31_0.14_280),oklch(0.45_0.19_275))] bg-cover bg-center bg-no-repeat transition-[opacity,scale] duration-500 ease-tih03 group-hover:opacity-0 group-hover:scale-96 motion-reduce:duration-0"></div>
        <div class="absolute inset-0 z-2 grid place-items-center opacity-0 scale-104 bg-[image:url('https://picsum.photos/seed/tih03-runner-b/600/600'),linear-gradient(135deg,oklch(0.29_0.07_240),oklch(0.45_0.11_235),oklch(0.75_0.12_230))] bg-cover bg-center bg-no-repeat transition-[opacity,scale] duration-500 ease-tih03 group-hover:opacity-100 group-hover:scale-100 motion-reduce:duration-0"></div>
        <span class="absolute top-2.5 right-2.5 z-10 px-2 py-0.5 rounded-full text-[9px] font-bold tracking-[0.08em] uppercase text-tih03-acc bg-[oklch(0_0_0/0.6)] backdrop-blur-sm border border-[oklch(1_0_0/0.1)] transition-opacity duration-250 group-hover:opacity-0 motion-reduce:transition-none">Hover</span>
      </div>
      <div class="px-4 py-3.5">
        <h3 class="mb-1 text-[13px] font-semibold text-tih03-text"><a href="#aerostep" class="no-underline text-inherit rounded focus-visible:outline-2 focus-visible:outline-tih03-acc focus-visible:outline-offset-3">AeroStep Pro Runner</a></h3>
        <div class="flex items-center gap-2">
          <span class="text-[15px] font-bold text-tih03-acc tabular-nums">$129</span>
          <span class="text-[11px] text-tih03-muted line-through tabular-nums">$189</span>
        </div>
        <div class="flex gap-1.25 mt-2.5" aria-hidden="true">
          <span class="w-3.5 h-3.5 rounded-full border-2 border-[oklch(1_0_0/0.15)] bg-[oklch(0.42_0.2_275)]"></span>
          <span class="w-3.5 h-3.5 rounded-full border-2 border-[oklch(1_0_0/0.15)] bg-[oklch(0.75_0.13_230)]"></span>
          <span class="w-3.5 h-3.5 rounded-full border-2 border-[oklch(1_0_0/0.15)] bg-[oklch(0.76_0.16_70)]"></span>
        </div>
      </div>
    </article>
    <article class="group overflow-hidden rounded-[14px] bg-tih03-card border border-[oklch(1_0_0/0.07)] transition-shadow duration-300 hover:shadow-[0_16px_48px_oklch(0_0_0/0.4)] motion-reduce:transition-none">
      <div class="relative aspect-square overflow-hidden">
        <div class="absolute inset-0 z-1 grid place-items-center opacity-100 scale-100 bg-[image:url('https://picsum.photos/seed/tih03-tote-a/600/600'),linear-gradient(135deg,oklch(0.17_0.03_60),oklch(0.29_0.07_55),oklch(0.48_0.11_60))] bg-cover bg-center bg-no-repeat transition-[opacity,scale] duration-500 ease-tih03 group-hover:opacity-0 group-hover:scale-96 motion-reduce:duration-0"></div>
        <div class="absolute inset-0 z-2 grid place-items-center opacity-0 scale-104 bg-[image:url('https://picsum.photos/seed/tih03-tote-b/600/600'),linear-gradient(135deg,oklch(0.22_0.06_150),oklch(0.42_0.11_150),oklch(0.8_0.16_145))] bg-cover bg-center bg-no-repeat transition-[opacity,scale] duration-500 ease-tih03 group-hover:opacity-100 group-hover:scale-100 motion-reduce:duration-0"></div>
        <span class="absolute top-2.5 right-2.5 z-10 px-2 py-0.5 rounded-full text-[9px] font-bold tracking-[0.08em] uppercase text-tih03-acc bg-[oklch(0_0_0/0.6)] backdrop-blur-sm border border-[oklch(1_0_0/0.1)] transition-opacity duration-250 group-hover:opacity-0 motion-reduce:transition-none">Hover</span>
      </div>
      <div class="px-4 py-3.5">
        <h3 class="mb-1 text-[13px] font-semibold text-tih03-text"><a href="#nomad" class="no-underline text-inherit rounded focus-visible:outline-2 focus-visible:outline-tih03-acc focus-visible:outline-offset-3">Nomad Leather Tote</a></h3>
        <div class="flex items-center gap-2">
          <span class="text-[15px] font-bold text-tih03-acc tabular-nums">$249</span>
          <span class="text-[11px] text-tih03-muted line-through tabular-nums">$320</span>
        </div>
        <div class="flex gap-1.25 mt-2.5" aria-hidden="true">
          <span class="w-3.5 h-3.5 rounded-full border-2 border-[oklch(1_0_0/0.15)] bg-[oklch(0.45_0.11_60)]"></span>
          <span class="w-3.5 h-3.5 rounded-full border-2 border-[oklch(1_0_0/0.15)] bg-[oklch(0.8_0.16_145)]"></span>
          <span class="w-3.5 h-3.5 rounded-full border-2 border-[oklch(1_0_0/0.15)] bg-[oklch(0.92_0.004_250)]"></span>
        </div>
      </div>
    </article>
    <article class="group overflow-hidden rounded-[14px] bg-tih03-card border border-[oklch(1_0_0/0.07)] transition-shadow duration-300 hover:shadow-[0_16px_48px_oklch(0_0_0/0.4)] motion-reduce:transition-none">
      <div class="relative aspect-square overflow-hidden">
        <div class="absolute inset-0 z-1 grid place-items-center opacity-100 scale-100 bg-[image:url('https://picsum.photos/seed/tih03-watch-a/600/600'),linear-gradient(135deg,oklch(0.24_0.01_285),oklch(0.38_0.02_265),oklch(0.7_0.02_260))] bg-cover bg-center bg-no-repeat transition-[opacity,scale] duration-500 ease-tih03 group-hover:opacity-0 group-hover:scale-96 motion-reduce:duration-0"></div>
        <div class="absolute inset-0 z-2 grid place-items-center opacity-0 scale-104 bg-[image:url('https://picsum.photos/seed/tih03-watch-b/600/600'),linear-gradient(135deg,oklch(0.2_0.07_25),oklch(0.36_0.14_27),oklch(0.68_0.16_25))] bg-cover bg-center bg-no-repeat transition-[opacity,scale] duration-500 ease-tih03 group-hover:opacity-100 group-hover:scale-100 motion-reduce:duration-0"></div>
        <span class="absolute top-2.5 right-2.5 z-10 px-2 py-0.5 rounded-full text-[9px] font-bold tracking-[0.08em] uppercase text-tih03-acc bg-[oklch(0_0_0/0.6)] backdrop-blur-sm border border-[oklch(1_0_0/0.1)] transition-opacity duration-250 group-hover:opacity-0 motion-reduce:transition-none">Hover</span>
      </div>
      <div class="px-4 py-3.5">
        <h3 class="mb-1 text-[13px] font-semibold text-tih03-text"><a href="#vertex" class="no-underline text-inherit rounded focus-visible:outline-2 focus-visible:outline-tih03-acc focus-visible:outline-offset-3">Vertex Titanium Watch</a></h3>
        <div class="flex items-center gap-2">
          <span class="text-[15px] font-bold text-tih03-acc tabular-nums">$589</span>
          <span class="text-[11px] text-tih03-muted line-through tabular-nums">$750</span>
        </div>
        <div class="flex gap-1.25 mt-2.5" aria-hidden="true">
          <span class="w-3.5 h-3.5 rounded-full border-2 border-[oklch(1_0_0/0.15)] bg-[oklch(0.7_0.02_260)]"></span>
          <span class="w-3.5 h-3.5 rounded-full border-2 border-[oklch(1_0_0/0.15)] bg-[oklch(0.7_0.16_25)]"></span>
          <span class="w-3.5 h-3.5 rounded-full border-2 border-[oklch(1_0_0/0.15)] bg-[oklch(0.82_0.16_80)]"></span>
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
  --color-tih03-bg: #0d0d11;
  --color-tih03-bg: oklch(0.15 0.006 285);
  --color-tih03-card: #16161f;
  --color-tih03-card: oklch(0.19 0.012 285);
  --color-tih03-text: #f1f5f9;
  --color-tih03-text: oklch(0.96 0.005 250);
  --color-tih03-muted: #64748b;
  --color-tih03-muted: oklch(0.55 0.035 255);
  --color-tih03-acc: #f59e0b;
  --color-tih03-acc: oklch(0.78 0.16 72);
  --font-tih03-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih03: cubic-bezier(0.4, 0, 0.2, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-03 {
  width: 100%;
  min-height: 100svh;
}

.tih-03 ::selection {
  background: oklch(0.78 0.16 72);
  color: #000;
}
```
