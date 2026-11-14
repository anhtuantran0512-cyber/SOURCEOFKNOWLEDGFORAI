---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-image-color-overlay-tint-on-hover/"
title: "Tailwind Image Color Overlay Tint on Hover"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "A brand colour washed over a photograph with mix-blend-color, which replaces hue and saturation while keeping luminosity &mdash; a lighting gel, not a paint…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Image Color Overlay Tint on Hover
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-image-color-overlay-tint-on-hover/

A brand colour washed over a photograph with mix-blend-color, which replaces hue and saturation while keeping luminosity &mdash; a lighting gel, not a paint bucket. The tint is a per-card inline custom property, so the overlay is one class list serving any colour, and the text sits in an isolate wrapper so the blend cannot touch it.
## HTML
```html
<section class="tih-07 w-full min-h-svh grid place-items-center bg-tih07-bg font-tih07-sans px-6 py-10" aria-label="Colour overlay tint on hover demo">
  <div class="grid w-full max-w-195 gap-4 grid-cols-1 sm:grid-cols-3">
    <article style="--tint:oklch(0.7 0.19 45)" class="group relative overflow-hidden rounded-[14px] aspect-square">
      <div class="absolute inset-0 grid place-items-center bg-[image:url('https://picsum.photos/seed/landscape-orange/600/600'),linear-gradient(135deg,oklch(0.27_0.03_265),oklch(0.35_0.02_265),oklch(0.45_0.015_265))] bg-cover bg-center bg-no-repeat transition-transform duration-380 ease-tih07 group-hover:scale-106 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
      </div>
      <div class="absolute inset-0 bg-[var(--tint)] mix-blend-color opacity-0 transition-opacity duration-380 ease-tih07 group-hover:opacity-70 motion-reduce:transition-none motion-reduce:opacity-50"></div>
      <span class="absolute top-2.5 left-2.5 z-2 isolate px-2 py-0.75 rounded-md text-[10px] font-semibold text-tih07-muted bg-[oklch(1_0_0/0.08)] border border-[oklch(1_0_0/0.1)]">Brand A</span>
      <div class="absolute inset-0 z-2 isolate grid place-items-center">
        <p class="text-sm font-bold text-tih07-text opacity-0 scale-90 transition-[opacity,scale] duration-380 ease-tih07 group-hover:opacity-100 group-hover:scale-100 motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:scale-100">Ember Orange Tint</p>
      </div>
    </article>
    <article style="--tint:oklch(0.62 0.19 255)" class="group relative overflow-hidden rounded-[14px] aspect-square">
      <div class="absolute inset-0 grid place-items-center bg-[image:url('https://picsum.photos/seed/landscape-blue/600/600'),linear-gradient(135deg,oklch(0.14_0_0),oklch(0.22_0_0),oklch(0.3_0_0))] bg-cover bg-center bg-no-repeat transition-transform duration-380 ease-tih07 group-hover:scale-106 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
      </div>
      <div class="absolute inset-0 bg-[var(--tint)] mix-blend-color opacity-0 transition-opacity duration-380 ease-tih07 group-hover:opacity-70 motion-reduce:transition-none motion-reduce:opacity-50"></div>
      <span class="absolute top-2.5 left-2.5 z-2 isolate px-2 py-0.75 rounded-md text-[10px] font-semibold text-tih07-muted bg-[oklch(1_0_0/0.08)] border border-[oklch(1_0_0/0.1)]">Brand B</span>
      <div class="absolute inset-0 z-2 isolate grid place-items-center">
        <p class="text-sm font-bold text-tih07-text opacity-0 scale-90 transition-[opacity,scale] duration-380 ease-tih07 group-hover:opacity-100 group-hover:scale-100 motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:scale-100">Pacific Blue Tint</p>
      </div>
    </article>
    <article style="--tint:oklch(0.62 0.21 295)" class="group relative overflow-hidden rounded-[14px] aspect-square">
      <div class="absolute inset-0 grid place-items-center bg-[image:url('https://picsum.photos/seed/landscape-violet/600/600'),linear-gradient(135deg,oklch(0.16_0.01_285),oklch(0.21_0.015_285),oklch(0.29_0.02_285))] bg-cover bg-center bg-no-repeat transition-transform duration-380 ease-tih07 group-hover:scale-106 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
      </div>
      <div class="absolute inset-0 bg-[var(--tint)] mix-blend-color opacity-0 transition-opacity duration-380 ease-tih07 group-hover:opacity-70 motion-reduce:transition-none motion-reduce:opacity-50"></div>
      <span class="absolute top-2.5 left-2.5 z-2 isolate px-2 py-0.75 rounded-md text-[10px] font-semibold text-tih07-muted bg-[oklch(1_0_0/0.08)] border border-[oklch(1_0_0/0.1)]">Brand C</span>
      <div class="absolute inset-0 z-2 isolate grid place-items-center">
        <p class="text-sm font-bold text-tih07-text opacity-0 scale-90 transition-[opacity,scale] duration-380 ease-tih07 group-hover:opacity-100 group-hover:scale-100 motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:scale-100">Deep Violet Tint</p>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tih07-bg: #0d0d0f;
  --color-tih07-bg: oklch(0.15 0.004 285);
  --color-tih07-text: #f1f5f9;
  --color-tih07-text: oklch(0.96 0.005 250);
  --color-tih07-muted: #94a3b8;
  --color-tih07-muted: oklch(0.7 0.03 250);
  --color-tih07-acc: #f97316;
  --color-tih07-acc: oklch(0.7 0.19 45);
  --font-tih07-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih07: cubic-bezier(0.25, 0.46, 0.45, 0.94);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-07 {
  width: 100%;
  min-height: 100svh;
}

.tih-07 ::selection {
  background: oklch(0.7 0.19 45);
  color: #000;
}
```
