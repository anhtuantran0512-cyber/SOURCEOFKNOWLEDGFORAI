---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-stacked-layer-reveal-card/"
title: "Tailwind Stacked Layer Reveal Card (Fanned Risograph Deck)"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "Three coloured plates that fan out and rotate on hover like spreading a deck of risograph prints."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stacked Layer Reveal Card (Fanned Risograph Deck)
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-stacked-layer-reveal-card/

Three coloured plates that fan out and rotate on hover like spreading a deck of risograph prints. The port trades CSS's pseudo-element layers for real <div>s &mdash; more markup, but each plate's rest state, fanned state and stagger delay are now readable in one place.
## HTML
```html
<section class="tch-09 w-full min-h-svh grid place-items-center bg-tch09-bg bg-[repeating-linear-gradient(45deg,rgb(0_0_0/0.02)_0_12px,transparent_12px_24px)] font-tch09-sans p-8">
  <article tabindex="0" class="group relative w-[320px] h-[410px] cursor-pointer outline-none">
    <div class="absolute inset-0 z-1 rounded-2xl bg-tch09-a transition-transform duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] delay-150 group-hover:-translate-x-7 group-hover:translate-y-5 group-hover:-rotate-6 group-focus-visible:-translate-x-7 group-focus-visible:translate-y-5 group-focus-visible:-rotate-6 motion-reduce:transition-none motion-reduce:group-hover:translate-x-0 motion-reduce:group-hover:translate-y-0 motion-reduce:group-hover:rotate-0"></div>
    <div class="absolute inset-0 z-2 rounded-2xl bg-tch09-b transition-transform duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] delay-75 group-hover:translate-x-6 group-hover:-translate-y-2 group-hover:rotate-5 group-focus-visible:translate-x-6 group-focus-visible:-translate-y-2 group-focus-visible:rotate-5 motion-reduce:transition-none motion-reduce:group-hover:translate-x-0 motion-reduce:group-hover:translate-y-0 motion-reduce:group-hover:rotate-0"></div>
    <div class="absolute inset-0 z-3 rounded-2xl bg-tch09-c shadow-[0_18px_40px_rgb(0_0_0/0.25)] transition-[translate,box-shadow] duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] group-hover:-translate-y-1.5 group-hover:shadow-[0_30px_60px_rgb(0_0_0/0.35)] group-focus-visible:-translate-y-1.5 motion-reduce:transition-none"></div>
    <div class="relative z-4 h-full p-[2.2rem] flex flex-col justify-between text-tch09-ink pointer-events-none">
      <span class="text-[0.7rem] tracking-[0.28em] uppercase text-tch09-b">Vinyl Press · 2025</span>
      <h2 class="font-tch09-display text-[2.6rem] leading-[0.95] uppercase">Paper<br>Cities</h2>
      <p class="text-[0.85rem] leading-[1.6] text-tch09-body">Limited run pressing. Three layers of risograph artwork fan out across the gatefold sleeve.</p>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch09-bg: #ebe4d8;
  --color-tch09-bg: oklch(0.92 0.017 85);
  --color-tch09-a: #d94f30;
  --color-tch09-a: oklch(0.58 0.18 33);
  --color-tch09-b: #f2b138;
  --color-tch09-b: oklch(0.8 0.15 78);
  --color-tch09-c: #1a1a1a;
  --color-tch09-c: oklch(0.2 0 0);
  --color-tch09-ink: #f4efe6;
  --color-tch09-ink: oklch(0.95 0.01 85);
  --color-tch09-body: #c9c2b6;
  --color-tch09-body: oklch(0.81 0.015 85);
  --font-tch09-sans: 'Archivo', system-ui, sans-serif;
  --font-tch09-display: 'Archivo Black', system-ui, sans-serif;
}

.tch-09 {
  width: 100%;
  min-height: 100svh;
}
```
