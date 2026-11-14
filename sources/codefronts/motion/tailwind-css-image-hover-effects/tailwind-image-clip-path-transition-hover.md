---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-image-clip-path-transition-hover/"
title: "Tailwind Image Clip-Path Transition Hover"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "Shape morphing where both shapes sit on the same element as two arbitrary clip-path utilities &mdash; resting and hovered, one line apart."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Image Clip-Path Transition Hover
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-image-clip-path-transition-hover/

Shape morphing where both shapes sit on the same element as two arbitrary clip-path utilities &mdash; resting and hovered, one line apart. Since interpolation requires matching vertex counts, having both values visible together is not cosmetic: it is what stops the pair from silently degrading into a hard cut.
## HTML
```html
<section class="tih-11 w-full min-h-svh grid place-items-center bg-tih11-bg font-tih11-sans px-6 py-10" aria-label="Clip-path shape morph hover demo">
  <div class="grid w-full max-w-195 gap-5 grid-cols-1 sm:grid-cols-3">
    <article class="group flex flex-col items-center gap-3">
      <div class="relative w-full aspect-square overflow-visible">
        <div class="grid place-items-center w-full h-full bg-[image:url('https://picsum.photos/seed/tih11-moon/600/600'),radial-gradient(circle,oklch(0.28_0.11_290),oklch(0.35_0.18_295),oklch(0.55_0.24_295))] bg-cover bg-center bg-no-repeat [clip-path:circle(42%_at_50%_50%)] transition-[clip-path,scale] duration-500 ease-tih11 group-hover:[clip-path:polygon(10%_0%,90%_0%,100%_10%,100%_90%,90%_100%,10%_100%,0%_90%,0%_10%)] group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:[clip-path:circle(42%_at_50%_50%)] motion-reduce:group-hover:scale-100">
        </div>
      </div>
      <div class="text-center">
        <p class="text-[10px] tracking-[0.08em] text-tih11-muted">Circle<span class="mx-1 text-tih11-acc">&rarr;</span><span class="font-bold text-tih11-acc">Rounded Rect</span></p>
        <p class="mt-0.75 text-[13px] font-bold text-tih11-text">Orbital Shift</p>
      </div>
    </article>
    <article class="group flex flex-col items-center gap-3">
      <div class="relative w-full aspect-square overflow-visible">
        <div class="grid place-items-center w-full h-full bg-[image:url('https://picsum.photos/seed/tih11-gem/600/600'),radial-gradient(circle,oklch(0.25_0.05_180),oklch(0.42_0.09_165),oklch(0.8_0.14_163))] bg-cover bg-center bg-no-repeat [clip-path:polygon(50%_0%,100%_50%,50%_100%,0%_50%)] transition-[clip-path,scale] duration-500 ease-tih11 group-hover:[clip-path:circle(48%_at_50%_50%)] group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:[clip-path:polygon(50%_0%,100%_50%,50%_100%,0%_50%)] motion-reduce:group-hover:scale-100">
        </div>
      </div>
      <div class="text-center">
        <p class="text-[10px] tracking-[0.08em] text-tih11-muted">Diamond<span class="mx-1 text-tih11-acc">&rarr;</span><span class="font-bold text-tih11-acc">Circle</span></p>
        <p class="mt-0.75 text-[13px] font-bold text-tih11-text">Gem Reveal</p>
      </div>
    </article>
    <article class="group flex flex-col items-center gap-3">
      <div class="relative w-full aspect-square overflow-visible">
        <div class="grid place-items-center w-full h-full bg-[image:url('https://picsum.photos/seed/tih11-lattice/600/600'),radial-gradient(circle,oklch(0.2_0.02_60),oklch(0.45_0.11_60),oklch(0.78_0.16_72))] bg-cover bg-center bg-no-repeat [clip-path:polygon(50%_0%,100%_25%,100%_75%,50%_100%,0%_75%,0%_25%)] transition-[clip-path,scale,rotate] duration-500 ease-tih11 group-hover:[clip-path:polygon(25%_0%,75%_0%,100%_50%,75%_100%,25%_100%,0%_50%)] group-hover:scale-105 group-hover:rotate-30 motion-reduce:transition-none motion-reduce:group-hover:[clip-path:polygon(50%_0%,100%_25%,100%_75%,50%_100%,0%_75%,0%_25%)] motion-reduce:group-hover:scale-100 motion-reduce:group-hover:rotate-0">
        </div>
      </div>
      <div class="text-center">
        <p class="text-[10px] tracking-[0.08em] text-tih11-muted">Hex<span class="mx-1 text-tih11-acc">&rarr;</span><span class="font-bold text-tih11-acc">Wide Hex + Spin</span></p>
        <p class="mt-0.75 text-[13px] font-bold text-tih11-text">Lattice Morph</p>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tih11-bg: #08080d;
  --color-tih11-bg: oklch(0.12 0.008 285);
  --color-tih11-text: #f1f5f9;
  --color-tih11-text: oklch(0.96 0.005 250);
  --color-tih11-muted: #64748b;
  --color-tih11-muted: oklch(0.58 0.035 255);
  --color-tih11-acc: #e879f9;
  --color-tih11-acc: oklch(0.78 0.19 320);
  --font-tih11-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih11: cubic-bezier(0.34, 1.56, 0.64, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-11 {
  width: 100%;
  min-height: 100svh;
}

.tih-11 ::selection {
  background: oklch(0.78 0.19 320);
  color: #000;
}
```
