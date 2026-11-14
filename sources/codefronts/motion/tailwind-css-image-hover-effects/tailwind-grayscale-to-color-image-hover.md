---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-grayscale-to-color-image-hover/"
title: "Tailwind Grayscale to Color Image Hover"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "Three filter functions transitioned as one unit &mdash; and in utilities they are three named classes: grayscale brightness-75 saturate-0 at rest,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Grayscale to Color Image Hover
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-grayscale-to-color-image-hover/

Three filter functions transitioned as one unit &mdash; and in utilities they are three named classes: grayscale brightness-75 saturate-0 at rest, group-hover:grayscale-0 group-hover:brightness-100 group-hover:saturate-120 on hover. The 20% saturation overshoot is what makes the colour land rather than merely appear.
## HTML
```html
<section class="tih-06 w-full min-h-svh grid place-items-center bg-tih06-bg font-tih06-sans px-6 py-10" aria-label="Grayscale to colour image hover demo">
  <div class="grid w-full max-w-195 gap-3.5 grid-cols-2 sm:grid-cols-4">
    <article class="group relative overflow-hidden rounded-[10px] aspect-[3/4] ring-2 ring-transparent transition-[box-shadow] duration-550 ease-tih06 group-hover:ring-[oklch(0.79_0.13_205/0.4)] hover:ring-[oklch(0.79_0.13_205/0.4)] motion-reduce:transition-none">
      <div class="absolute inset-0 grid place-items-center bg-[image:url('https://i.pravatar.cc/400?img=47'),linear-gradient(135deg,oklch(0.3_0.05_250),oklch(0.4_0.17_265),oklch(0.62_0.19_260),oklch(0.82_0.09_250))] bg-cover bg-center bg-no-repeat grayscale brightness-75 saturate-0 transition-[filter,scale] duration-550 ease-tih06 group-hover:grayscale-0 group-hover:brightness-100 group-hover:saturate-120 group-hover:scale-104 motion-reduce:transition-none motion-reduce:grayscale-0 motion-reduce:brightness-100 motion-reduce:saturate-100 motion-reduce:group-hover:scale-100">
      </div>
      <div class="absolute inset-x-0 bottom-0 p-3 bg-linear-[to_top,oklch(0_0_0/0.8),transparent]">
        <p class="text-xs font-bold text-tih06-text">Aria Chen</p>
        <p class="mt-0.5 text-[10px] text-tih06-muted transition-colors duration-550 ease-tih06 group-hover:text-tih06-acc motion-reduce:transition-none">Lead Engineer</p>
      </div>
    </article>
    <article class="group relative overflow-hidden rounded-[10px] aspect-[3/4] ring-2 ring-transparent transition-[box-shadow] duration-550 ease-tih06 hover:ring-[oklch(0.79_0.13_205/0.4)] motion-reduce:transition-none">
      <div class="absolute inset-0 grid place-items-center bg-[image:url('https://i.pravatar.cc/400?img=12'),linear-gradient(135deg,oklch(0.25_0.08_45),oklch(0.45_0.15_45),oklch(0.63_0.22_28),oklch(0.8_0.1_25))] bg-cover bg-center bg-no-repeat grayscale brightness-75 saturate-0 transition-[filter,scale] duration-550 ease-tih06 group-hover:grayscale-0 group-hover:brightness-100 group-hover:saturate-120 group-hover:scale-104 motion-reduce:transition-none motion-reduce:grayscale-0 motion-reduce:brightness-100 motion-reduce:saturate-100 motion-reduce:group-hover:scale-100">
      </div>
      <div class="absolute inset-x-0 bottom-0 p-3 bg-linear-[to_top,oklch(0_0_0/0.8),transparent]">
        <p class="text-xs font-bold text-tih06-text">Marcus Webb</p>
        <p class="mt-0.5 text-[10px] text-tih06-muted transition-colors duration-550 ease-tih06 group-hover:text-tih06-acc motion-reduce:transition-none">Creative Director</p>
      </div>
    </article>
    <article class="group relative overflow-hidden rounded-[10px] aspect-[3/4] ring-2 ring-transparent transition-[box-shadow] duration-550 ease-tih06 hover:ring-[oklch(0.79_0.13_205/0.4)] motion-reduce:transition-none">
      <div class="absolute inset-0 grid place-items-center bg-[image:url('https://i.pravatar.cc/400?img=45'),linear-gradient(135deg,oklch(0.3_0.08_165),oklch(0.4_0.1_165),oklch(0.7_0.15_165),oklch(0.86_0.12_165))] bg-cover bg-center bg-no-repeat grayscale brightness-75 saturate-0 transition-[filter,scale] duration-550 ease-tih06 group-hover:grayscale-0 group-hover:brightness-100 group-hover:saturate-120 group-hover:scale-104 motion-reduce:transition-none motion-reduce:grayscale-0 motion-reduce:brightness-100 motion-reduce:saturate-100 motion-reduce:group-hover:scale-100">
      </div>
      <div class="absolute inset-x-0 bottom-0 p-3 bg-linear-[to_top,oklch(0_0_0/0.8),transparent]">
        <p class="text-xs font-bold text-tih06-text">Priya Nair</p>
        <p class="mt-0.5 text-[10px] text-tih06-muted transition-colors duration-550 ease-tih06 group-hover:text-tih06-acc motion-reduce:transition-none">Research Scientist</p>
      </div>
    </article>
    <article class="group relative overflow-hidden rounded-[10px] aspect-[3/4] ring-2 ring-transparent transition-[box-shadow] duration-550 ease-tih06 hover:ring-[oklch(0.79_0.13_205/0.4)] motion-reduce:transition-none">
      <div class="absolute inset-0 grid place-items-center bg-[image:url('https://i.pravatar.cc/400?img=33'),linear-gradient(135deg,oklch(0.25_0.13_305),oklch(0.45_0.22_300),oklch(0.63_0.21_300),oklch(0.89_0.06_305))] bg-cover bg-center bg-no-repeat grayscale brightness-75 saturate-0 transition-[filter,scale] duration-550 ease-tih06 group-hover:grayscale-0 group-hover:brightness-100 group-hover:saturate-120 group-hover:scale-104 motion-reduce:transition-none motion-reduce:grayscale-0 motion-reduce:brightness-100 motion-reduce:saturate-100 motion-reduce:group-hover:scale-100">
      </div>
      <div class="absolute inset-x-0 bottom-0 p-3 bg-linear-[to_top,oklch(0_0_0/0.8),transparent]">
        <p class="text-xs font-bold text-tih06-text">Leo Santos</p>
        <p class="mt-0.5 text-[10px] text-tih06-muted transition-colors duration-550 ease-tih06 group-hover:text-tih06-acc motion-reduce:transition-none">Product Strategist</p>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tih06-bg: #09090f;
  --color-tih06-bg: oklch(0.13 0.008 285);
  --color-tih06-text: #f1f5f9;
  --color-tih06-text: oklch(0.96 0.005 250);
  --color-tih06-muted: #475569;
  --color-tih06-muted: oklch(0.63 0.03 255);
  --color-tih06-acc: #22d3ee;
  --color-tih06-acc: oklch(0.79 0.13 205);
  --font-tih06-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih06: cubic-bezier(0.25, 0.46, 0.45, 0.94);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-06 {
  width: 100%;
  min-height: 100svh;
}

.tih-06 ::selection {
  background: oklch(0.79 0.13 205);
  color: #000;
}
```
