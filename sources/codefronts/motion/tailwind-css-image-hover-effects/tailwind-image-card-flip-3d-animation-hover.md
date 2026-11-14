---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-image-card-flip-3d-animation-hover/"
title: "Tailwind Image Card Flip 3D Animation Hover"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "The three-layer flip &mdash; scene, flipper, two faces &mdash; with every one of its four critical properties now a named utility: [perspective:800px],…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Image Card Flip 3D Animation Hover
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-image-card-flip-3d-animation-hover/

The three-layer flip &mdash; scene, flipper, two faces &mdash; with every one of its four critical properties now a named utility: [perspective:800px], transform-3d, backface-hidden and group-hover:rotate-y-180. The pattern's failure modes are all &ldquo;you forgot one of these&rdquo;, and a class list makes a missing one visible.
## HTML
```html
<section class="tih-20 w-full min-h-svh grid place-items-center bg-tih20-bg font-tih20-sans px-6 py-10" aria-label="3D card flip hover demo">
  <div class="grid w-full max-w-195 gap-5 grid-cols-1 sm:grid-cols-3">
    <div class="group [perspective:800px] aspect-[3/4]">
      <div class="relative w-full h-full transform-3d transition-transform duration-650 ease-tih20 group-hover:rotate-y-180 focus-within:rotate-y-180 motion-reduce:transition-none motion-reduce:group-hover:rotate-y-0 motion-reduce:focus-within:rotate-y-0">
        <div class="absolute inset-0 flex flex-col justify-end overflow-hidden rounded-2xl backface-hidden bg-[image:url('https://picsum.photos/seed/tih20-cosmos/600/800'),linear-gradient(145deg,oklch(0.25_0.1_285),oklch(0.35_0.15_280),oklch(0.5_0.2_275),oklch(0.72_0.14_275))] bg-cover bg-center bg-no-repeat motion-reduce:opacity-100 motion-reduce:transition-opacity motion-reduce:duration-300 motion-reduce:group-hover:opacity-0">
          <div class="relative z-1 p-4 bg-linear-[to_top,oklch(0_0_0/0.8),transparent]">
            <p class="text-sm font-bold text-tih20-text">Cosmos Explorer</p>
            <p class="mt-0.5 text-[10px] text-tih20-muted">Astrophotography</p>
          </div>
          <span class="absolute top-2.5 right-2.5 z-2 px-2 py-0.75 rounded-full text-[9px] font-bold text-tih20-muted bg-[oklch(1_0_0/0.07)] border border-[oklch(1_0_0/0.1)] transition-opacity duration-300 group-hover:opacity-0">Hover to flip</span>
        </div>
        <div class="absolute inset-0 flex flex-col items-center justify-center p-5 overflow-hidden rounded-2xl backface-hidden rotate-y-180 bg-linear-[135deg,oklch(0.18_0.07_285),oklch(0.25_0.1_285)] motion-reduce:opacity-0 motion-reduce:rotate-y-0 motion-reduce:transition-opacity motion-reduce:duration-300 motion-reduce:group-hover:opacity-100">
          <span class="mb-3 text-4xl" aria-hidden="true">&#127756;</span>
          <p class="mb-2 text-[15px] font-extrabold text-center text-tih20-text">20-Week Course</p>
          <p class="mb-3.5 text-[11px] leading-[1.5] text-center text-tih20-muted">Master astrophotography from light-pollution basics to deep-sky stacking.</p>
          <a href="#cosmos-enroll" class="px-4.5 py-2 rounded-full text-[11px] font-bold tracking-[0.05em] text-black no-underline bg-tih20-acc transition-[scale,box-shadow] duration-200 hover:scale-104 hover:shadow-[0_0_16px_oklch(0.8_0.14_163/0.4)] focus-visible:outline-2 focus-visible:outline-tih20-text focus-visible:outline-offset-2 motion-reduce:transition-none">Enroll Now</a>
        </div>
      </div>
    </div>
    <div class="group [perspective:800px] aspect-[3/4]">
      <div class="relative w-full h-full transform-3d transition-transform duration-650 ease-tih20 group-hover:rotate-y-180 focus-within:rotate-y-180 motion-reduce:transition-none motion-reduce:group-hover:rotate-y-0 motion-reduce:focus-within:rotate-y-0">
        <div class="absolute inset-0 flex flex-col justify-end overflow-hidden rounded-2xl backface-hidden bg-[image:url('https://picsum.photos/seed/tih20-bio/600/800'),linear-gradient(145deg,oklch(0.22_0.06_150),oklch(0.35_0.09_150),oklch(0.55_0.13_155),oklch(0.8_0.14_163))] bg-cover bg-center bg-no-repeat motion-reduce:opacity-100 motion-reduce:transition-opacity motion-reduce:duration-300 motion-reduce:group-hover:opacity-0">
          <div class="relative z-1 p-4 bg-linear-[to_top,oklch(0_0_0/0.8),transparent]">
            <p class="text-sm font-bold text-tih20-text">Bio Systems</p>
            <p class="mt-0.5 text-[10px] text-tih20-muted">Botany Research</p>
          </div>
          <span class="absolute top-2.5 right-2.5 z-2 px-2 py-0.75 rounded-full text-[9px] font-bold text-tih20-muted bg-[oklch(1_0_0/0.07)] border border-[oklch(1_0_0/0.1)] transition-opacity duration-300 group-hover:opacity-0">Hover to flip</span>
        </div>
        <div class="absolute inset-0 flex flex-col items-center justify-center p-5 overflow-hidden rounded-2xl backface-hidden rotate-y-180 bg-linear-[135deg,oklch(0.15_0.05_150),oklch(0.22_0.06_150)] motion-reduce:opacity-0 motion-reduce:rotate-y-0 motion-reduce:transition-opacity motion-reduce:duration-300 motion-reduce:group-hover:opacity-100">
          <span class="mb-3 text-4xl" aria-hidden="true">&#129516;</span>
          <p class="mb-2 text-[15px] font-extrabold text-center text-tih20-text">Lab Access</p>
          <p class="mb-3.5 text-[11px] leading-[1.5] text-center text-tih20-muted">12 months of virtual lab sessions with live microscopy and specimen archives.</p>
          <a href="#bio-join" class="px-4.5 py-2 rounded-full text-[11px] font-bold tracking-[0.05em] text-black no-underline bg-tih20-acc transition-[scale,box-shadow] duration-200 hover:scale-104 hover:shadow-[0_0_16px_oklch(0.8_0.14_163/0.4)] focus-visible:outline-2 focus-visible:outline-tih20-text focus-visible:outline-offset-2 motion-reduce:transition-none">Join Lab</a>
        </div>
      </div>
    </div>
    <div class="group [perspective:800px] aspect-[3/4]">
      <div class="relative w-full h-full transform-3d transition-transform duration-650 ease-tih20 group-hover:rotate-y-180 focus-within:rotate-y-180 motion-reduce:transition-none motion-reduce:group-hover:rotate-y-0 motion-reduce:focus-within:rotate-y-0">
        <div class="absolute inset-0 flex flex-col justify-end overflow-hidden rounded-2xl backface-hidden bg-[image:url('https://picsum.photos/seed/tih20-arts/600/800'),linear-gradient(145deg,oklch(0.25_0.13_305),oklch(0.4_0.19_302),oklch(0.55_0.22_300),oklch(0.78_0.19_320))] bg-cover bg-center bg-no-repeat motion-reduce:opacity-100 motion-reduce:transition-opacity motion-reduce:duration-300 motion-reduce:group-hover:opacity-0">
          <div class="relative z-1 p-4 bg-linear-[to_top,oklch(0_0_0/0.8),transparent]">
            <p class="text-sm font-bold text-tih20-text">Digital Arts</p>
            <p class="mt-0.5 text-[10px] text-tih20-muted">Creative Studio</p>
          </div>
          <span class="absolute top-2.5 right-2.5 z-2 px-2 py-0.75 rounded-full text-[9px] font-bold text-tih20-muted bg-[oklch(1_0_0/0.07)] border border-[oklch(1_0_0/0.1)] transition-opacity duration-300 group-hover:opacity-0">Hover to flip</span>
        </div>
        <div class="absolute inset-0 flex flex-col items-center justify-center p-5 overflow-hidden rounded-2xl backface-hidden rotate-y-180 bg-linear-[135deg,oklch(0.17_0.09_310),oklch(0.25_0.13_305)] motion-reduce:opacity-0 motion-reduce:rotate-y-0 motion-reduce:transition-opacity motion-reduce:duration-300 motion-reduce:group-hover:opacity-100">
          <span class="mb-3 text-4xl" aria-hidden="true">&#127912;</span>
          <p class="mb-2 text-[15px] font-extrabold text-center text-tih20-text">Creator Pack</p>
          <p class="mb-3.5 text-[11px] leading-[1.5] text-center text-tih20-muted">Unlimited generative art tools, 500+ premium assets and weekly critique sessions.</p>
          <a href="#arts-access" class="px-4.5 py-2 rounded-full text-[11px] font-bold tracking-[0.05em] text-black no-underline bg-tih20-acc2 transition-[scale,box-shadow] duration-200 hover:scale-104 hover:shadow-[0_0_16px_oklch(0.78_0.19_320/0.4)] focus-visible:outline-2 focus-visible:outline-tih20-text focus-visible:outline-offset-2 motion-reduce:transition-none">Get Access</a>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tih20-bg: #07070f;
  --color-tih20-bg: oklch(0.11 0.012 285);
  --color-tih20-text: #f1f5f9;
  --color-tih20-text: oklch(0.96 0.005 250);
  --color-tih20-muted: #64748b;
  --color-tih20-muted: oklch(0.68 0.03 255);
  --color-tih20-acc: #34d399;
  --color-tih20-acc: oklch(0.8 0.14 163);
  --color-tih20-acc2: #e879f9;
  --color-tih20-acc2: oklch(0.78 0.19 320);
  --font-tih20-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih20: cubic-bezier(0.45, 0, 0.55, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-20 {
  width: 100%;
  min-height: 100svh;
}

.tih-20 ::selection {
  background: oklch(0.8 0.14 163);
  color: #000;
}
/* Firefox subpixel artefacts on face edges inside a 3D context. A bug workaround,
   which is exactly the category that should stay out of the markup. */

.tih-20 .backface-hidden {
  border: 1px solid transparent;
}
```
