---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-fluid-masonry-card-grid/"
title: "Tailwind Fluid Masonry Card Grid"
section: "layouts"
category: "tailwind-card-grid-layout"
category_name: "Tailwind Card Grid Layouts"
description: "A Pinterest-style wall built on multi-column flow, which is still the only masonry that works everywhere."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Fluid Masonry Card Grid
Source: https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-fluid-masonry-card-grid/

A Pinterest-style wall built on multi-column flow, which is still the only masonry that works everywhere. Tailwind has first-class utilities for the whole technique &mdash; columns-3, break-inside-avoid, gap-4 &mdash; so this is one of the few demos where the port is shorter than the CSS and nothing has to stay in the stylesheet.
## HTML
```html
<section class="tcg-04 w-full min-h-svh bg-tcg04-bg font-tcg04-sans px-6 py-12" aria-label="Fluid masonry card grid demo">
  <div class="max-w-[900px] mx-auto columns-3 max-[640px]:columns-2 gap-4">

    <figure style="--h:280px" class="group relative inline-block w-full mb-4 break-inside-avoid rounded-xl overflow-hidden bg-tcg04-card">
      <div class="w-full h-[var(--h)] bg-linear-[160deg,#fbcfe8,#a855f7] transition-transform duration-400 group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100" aria-hidden="true"></div>
      <figcaption class="absolute inset-x-0 bottom-0 px-3 py-2.5 text-[.78rem] font-semibold text-white bg-linear-[0deg,oklch(0_0_0/0.6),transparent] opacity-85 transition-opacity duration-250 group-hover:opacity-100 motion-reduce:transition-none">Portrait Study</figcaption>
    </figure>

    <figure style="--h:180px" class="group relative inline-block w-full mb-4 break-inside-avoid rounded-xl overflow-hidden bg-tcg04-card">
      <div class="w-full h-[var(--h)] bg-linear-[160deg,#bae6fd,#0284c7] transition-transform duration-400 group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100" aria-hidden="true"></div>
      <figcaption class="absolute inset-x-0 bottom-0 px-3 py-2.5 text-[.78rem] font-semibold text-white bg-linear-[0deg,oklch(0_0_0/0.6),transparent] opacity-85 transition-opacity duration-250 group-hover:opacity-100 motion-reduce:transition-none">Harbor Light</figcaption>
    </figure>

    <figure style="--h:340px" class="group relative inline-block w-full mb-4 break-inside-avoid rounded-xl overflow-hidden bg-tcg04-card">
      <div class="w-full h-[var(--h)] bg-linear-[160deg,#fde68a,#d97706] transition-transform duration-400 group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100" aria-hidden="true"></div>
      <figcaption class="absolute inset-x-0 bottom-0 px-3 py-2.5 text-[.78rem] font-semibold text-white bg-linear-[0deg,oklch(0_0_0/0.6),transparent] opacity-85 transition-opacity duration-250 group-hover:opacity-100 motion-reduce:transition-none">Desert Bloom</figcaption>
    </figure>

    <figure style="--h:220px" class="group relative inline-block w-full mb-4 break-inside-avoid rounded-xl overflow-hidden bg-tcg04-card">
      <div class="w-full h-[var(--h)] bg-linear-[160deg,#bbf7d0,#15803d] transition-transform duration-400 group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100" aria-hidden="true"></div>
      <figcaption class="absolute inset-x-0 bottom-0 px-3 py-2.5 text-[.78rem] font-semibold text-white bg-linear-[0deg,oklch(0_0_0/0.6),transparent] opacity-85 transition-opacity duration-250 group-hover:opacity-100 motion-reduce:transition-none">Quiet Forest</figcaption>
    </figure>

    <figure style="--h:300px" class="group relative inline-block w-full mb-4 break-inside-avoid rounded-xl overflow-hidden bg-tcg04-card">
      <div class="w-full h-[var(--h)] bg-linear-[160deg,#fecaca,#b91c1c] transition-transform duration-400 group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100" aria-hidden="true"></div>
      <figcaption class="absolute inset-x-0 bottom-0 px-3 py-2.5 text-[.78rem] font-semibold text-white bg-linear-[0deg,oklch(0_0_0/0.6),transparent] opacity-85 transition-opacity duration-250 group-hover:opacity-100 motion-reduce:transition-none">Red Canyon</figcaption>
    </figure>

    <figure style="--h:200px" class="group relative inline-block w-full mb-4 break-inside-avoid rounded-xl overflow-hidden bg-tcg04-card">
      <div class="w-full h-[var(--h)] bg-linear-[160deg,#ddd6fe,#6d28d9] transition-transform duration-400 group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100" aria-hidden="true"></div>
      <figcaption class="absolute inset-x-0 bottom-0 px-3 py-2.5 text-[.78rem] font-semibold text-white bg-linear-[0deg,oklch(0_0_0/0.6),transparent] opacity-85 transition-opacity duration-250 group-hover:opacity-100 motion-reduce:transition-none">Twilight Field</figcaption>
    </figure>

  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcg04-bg: #111114;
  --color-tcg04-bg: oklch(0.17 0.004 285);
  --color-tcg04-card: #1a1a1f;
  --color-tcg04-card: oklch(0.22 0.006 285);
  --font-tcg04-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract. */

.tcg-04 {
  width: 100%;
  min-height: 100svh;
}

.tcg-04 ::selection {
  background: #a855f7;
  color: #fff;
}
```
