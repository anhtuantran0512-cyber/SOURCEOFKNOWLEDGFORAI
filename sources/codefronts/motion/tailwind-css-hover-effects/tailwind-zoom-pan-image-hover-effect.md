---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-zoom-pan-image-hover-effect/"
title: "Tailwind Zoom Pan Image Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Six cinematic image moves — centre zoom, corner pan, slow drift, zoom with a colour grade, a clip-path un-crop and zoom-with-rotation."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Zoom Pan Image Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-zoom-pan-image-hover-effect/

Six cinematic image moves — centre zoom, corner pan, slow drift, zoom with a colour grade, a clip-path un-crop and zoom-with-rotation. The container clips, the inner layer scales, and every variant is one group-hover: transform.
## HTML
```html
<section class="thv-19 w-full min-h-svh grid place-items-center bg-thv19-bg font-thv19-sans px-6 py-14">
  <div class="w-[min(880px,100%)] grid grid-cols-[repeat(auto-fit,minmax(230px,1fr))] gap-6">
    <figure class="group flex flex-col items-center gap-3 m-0">
      <div class="w-full aspect-[4/3] overflow-hidden rounded-xl cursor-pointer">
        <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=900&q=80" alt="Sunlit modern living room with a pale sectional sofa" decoding="async" class="w-full h-full transition-transform duration-600 ease-[cubic-bezier(.4,0,.2,1)] group-hover:scale-[1.12] motion-reduce:transition-none object-cover">
      </div>
      <figcaption class="text-[11px] tracking-[0.12em] uppercase text-thv19-dim">center zoom</figcaption>
    </figure>
    <figure class="group flex flex-col items-center gap-3 m-0">
      <div class="w-full aspect-[4/3] overflow-hidden rounded-xl cursor-pointer">
        <img src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=900&q=80" alt="Open-plan kitchen and dining room in warm daylight" decoding="async" class="w-full h-full transition-transform duration-600 ease-[cubic-bezier(.4,0,.2,1)] group-hover:scale-[1.18] group-hover:-translate-x-[5%] group-hover:-translate-y-[5%] motion-reduce:transition-none object-cover">
      </div>
      <figcaption class="text-[11px] tracking-[0.12em] uppercase text-thv19-dim">corner-pan zoom</figcaption>
    </figure>
    <figure class="group flex flex-col items-center gap-3 m-0">
      <div class="w-full aspect-[4/3] overflow-hidden rounded-xl cursor-pointer">
        <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=900&q=80" alt="Contemporary white villa behind a manicured lawn" decoding="async" class="w-full h-full transition-transform duration-[1200ms] ease-[cubic-bezier(.4,0,.2,1)] group-hover:scale-[1.1] group-hover:translate-x-[3%] group-hover:translate-y-[2%] motion-reduce:transition-none object-cover">
      </div>
      <figcaption class="text-[11px] tracking-[0.12em] uppercase text-thv19-dim">slow ken-burns drift</figcaption>
    </figure>
    <figure class="group flex flex-col items-center gap-3 m-0">
      <div class="w-full aspect-[4/3] overflow-hidden rounded-xl cursor-pointer">
        <img src="https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?auto=format&fit=crop&w=900&q=80" alt="Upholstered armchair against a plaster wall" decoding="async" class="w-full h-full transition-[transform,filter] duration-600 ease-[cubic-bezier(.4,0,.2,1)] group-hover:scale-[1.1] group-hover:[filter:brightness(1.25)_saturate(1.2)] motion-reduce:transition-[filter] object-cover">
      </div>
      <figcaption class="text-[11px] tracking-[0.12em] uppercase text-thv19-dim">zoom + brightness</figcaption>
    </figure>
    <figure class="group flex flex-col items-center gap-3 m-0">
      <div class="w-full aspect-[4/3] overflow-visible rounded-xl cursor-pointer">
        <img src="https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=900&q=80" alt="Minimal lounge with floor-to-ceiling glazing" decoding="async" class="w-full h-full [clip-path:inset(8%_round_12px)] transition-[transform,clip-path] duration-600 ease-[cubic-bezier(.4,0,.2,1)] group-hover:scale-[1.08] group-hover:[clip-path:inset(0%_round_12px)] motion-reduce:transition-none object-cover">
      </div>
      <figcaption class="text-[11px] tracking-[0.12em] uppercase text-thv19-dim">clip-path crop zoom</figcaption>
    </figure>
    <figure class="group flex flex-col items-center gap-3 m-0">
      <div class="w-full aspect-[4/3] overflow-hidden rounded-xl cursor-pointer">
        <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=900&q=80" alt="Suburban house exterior at golden hour" decoding="async" class="w-full h-full transition-transform duration-600 ease-[cubic-bezier(.4,0,.2,1)] group-hover:scale-[1.15] group-hover:rotate-3 motion-reduce:transition-none object-cover">
      </div>
      <figcaption class="text-[11px] tracking-[0.12em] uppercase text-thv19-dim">zoom + rotation</figcaption>
    </figure>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv19-bg: #08080f;
  --color-thv19-bg: oklch(0.12 0.01 285);
  --color-thv19-dim: #8b91a0;
  --color-thv19-dim: oklch(0.66 0.02 265);
  --font-thv19-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-19 {
  width: 100%;
  min-height: 100svh;
}

.thv-19 ::selection {
  background: #1d4ed8;
  color: #fff;
}
```
