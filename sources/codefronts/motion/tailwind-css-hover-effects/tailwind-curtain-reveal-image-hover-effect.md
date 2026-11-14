---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-curtain-reveal-image-hover-effect/"
title: "Tailwind Curtain Reveal Image Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Four theatrical reveals — split curtain, curtain drop, an iris that opens from the centre and a venetian blind of five staggered slats."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Curtain Reveal Image Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-curtain-reveal-image-hover-effect/

Four theatrical reveals — split curtain, curtain drop, an iris that opens from the centre and a venetian blind of five staggered slats. The iris is rebuilt on clip-path: circle(), replacing the source's tangled box-shadow workaround.
## HTML
```html
<section class="thv-22 w-full min-h-svh grid place-items-center bg-thv22-bg font-thv22-sans px-6 py-14">
  <div class="w-[min(760px,100%)] grid grid-cols-[repeat(auto-fit,minmax(280px,1fr))] gap-8">
    <figure class="group flex flex-col gap-3 m-0">
      <div tabindex="0" class="relative w-full aspect-video overflow-hidden rounded-xl cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv22-blue before:content-[''] before:absolute before:top-0 before:left-0 before:z-20 before:w-1/2 before:h-full before:bg-thv22-drape before:transition-transform before:duration-500 before:ease-[cubic-bezier(.4,0,.2,1)] after:content-[''] after:absolute after:top-0 after:right-0 after:z-20 after:w-1/2 after:h-full after:bg-thv22-drape after:transition-transform after:duration-500 after:ease-[cubic-bezier(.4,0,.2,1)] group-hover:before:-translate-x-full group-hover:after:translate-x-full group-focus-visible:before:-translate-x-full group-focus-visible:after:translate-x-full motion-reduce:before:transition-none motion-reduce:after:transition-none">
        <div class="relative grid place-items-center w-full h-full bg-thv22-drape"><img src="https://images.unsplash.com/photo-1505691938895-1758d7feb511?auto=format&fit=crop&w=900&q=80" alt="Hotel bedroom with drawn linen curtains" decoding="async" class="absolute inset-0 w-full h-full object-cover"><span class="relative z-10 text-2xl font-black tracking-[0.15em] text-white [text-shadow:0_2px_14px_rgba(0,0,0,.75)]">OPEN</span></div>
      </div>
      <figcaption class="text-[11px] tracking-[0.12em] uppercase text-thv22-dim">split curtain</figcaption>
    </figure>
    <figure class="group flex flex-col gap-3 m-0">
      <div tabindex="0" class="relative w-full aspect-video overflow-hidden rounded-xl cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv22-violet">
        <div class="relative grid place-items-center w-full h-full bg-thv22-drape"><img src="https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=900&q=80" alt="Living room with a pale sofa and tall windows" decoding="async" class="absolute inset-0 w-full h-full object-cover"><span class="relative z-10 text-2xl font-black tracking-[0.15em] text-white [text-shadow:0_2px_14px_rgba(0,0,0,.75)]">DROP</span></div>
        <span aria-hidden="true" class="absolute inset-0 z-20 bg-thv22-drape origin-top scale-y-100 transition-transform duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-hover:scale-y-0 group-focus-visible:scale-y-0 motion-reduce:transition-none"></span>
      </div>
      <figcaption class="text-[11px] tracking-[0.12em] uppercase text-thv22-dim">curtain drop</figcaption>
    </figure>
    <figure class="group flex flex-col gap-3 m-0">
      <div tabindex="0" class="relative w-full aspect-video overflow-hidden rounded-xl cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv22-teal">
        <div class="relative grid place-items-center w-full h-full bg-thv22-drape"><img src="https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=900&q=80" alt="Dimly lit cocktail bar interior" decoding="async" class="absolute inset-0 w-full h-full object-cover"><span class="relative z-10 text-2xl font-black tracking-[0.15em] text-white [text-shadow:0_2px_14px_rgba(0,0,0,.75)]">IRIS</span></div>
        <span aria-hidden="true" class="absolute inset-0 z-20 bg-thv22-drape [clip-path:circle(140%_at_50%_50%)] transition-[clip-path] duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-hover:[clip-path:circle(0%_at_50%_50%)] group-focus-visible:[clip-path:circle(0%_at_50%_50%)] motion-reduce:transition-none"></span>
      </div>
      <figcaption class="text-[11px] tracking-[0.12em] uppercase text-thv22-dim">iris expand</figcaption>
    </figure>
    <figure class="group flex flex-col gap-3 m-0">
      <div tabindex="0" class="relative w-full aspect-video overflow-hidden rounded-xl cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv22-pink">
        <div class="relative grid place-items-center w-full h-full bg-thv22-drape"><img src="https://images.unsplash.com/photo-1449824913935-59a10b8d2000?auto=format&fit=crop&w=900&q=80" alt="City avenue photographed at dusk" decoding="async" class="absolute inset-0 w-full h-full object-cover"><span class="relative z-10 text-2xl font-black tracking-[0.15em] text-white [text-shadow:0_2px_14px_rgba(0,0,0,.75)]">BLIND</span></div>
        <span aria-hidden="true" class="absolute top-0 left-0 z-20 w-full h-[20%] bg-thv22-drape origin-top transition-transform duration-300 ease-[cubic-bezier(.4,0,.2,1)] group-hover:scale-y-0 group-focus-visible:scale-y-0 motion-reduce:transition-none"></span>
        <span aria-hidden="true" class="absolute top-[20%] left-0 z-20 w-full h-[20%] bg-thv22-drape origin-top transition-transform duration-300 delay-[50ms] ease-[cubic-bezier(.4,0,.2,1)] group-hover:scale-y-0 group-focus-visible:scale-y-0 motion-reduce:transition-none"></span>
        <span aria-hidden="true" class="absolute top-[40%] left-0 z-20 w-full h-[20%] bg-thv22-drape origin-top transition-transform duration-300 delay-[100ms] ease-[cubic-bezier(.4,0,.2,1)] group-hover:scale-y-0 group-focus-visible:scale-y-0 motion-reduce:transition-none"></span>
        <span aria-hidden="true" class="absolute top-[60%] left-0 z-20 w-full h-[20%] bg-thv22-drape origin-top transition-transform duration-300 delay-[150ms] ease-[cubic-bezier(.4,0,.2,1)] group-hover:scale-y-0 group-focus-visible:scale-y-0 motion-reduce:transition-none"></span>
        <span aria-hidden="true" class="absolute top-[80%] left-0 z-20 w-full h-[20%] bg-thv22-drape origin-top transition-transform duration-300 delay-[200ms] ease-[cubic-bezier(.4,0,.2,1)] group-hover:scale-y-0 group-focus-visible:scale-y-0 motion-reduce:transition-none"></span>
      </div>
      <figcaption class="text-[11px] tracking-[0.12em] uppercase text-thv22-dim">venetian blind</figcaption>
    </figure>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv22-bg: #08040c;
  --color-thv22-bg: oklch(0.11 0.02 310);
  --color-thv22-drape: #1a0a2e;
  --color-thv22-drape: oklch(0.19 0.06 300);
  --color-thv22-dim: #8d8894;
  --color-thv22-dim: oklch(0.65 0.02 300);
  --color-thv22-blue: #3b82f6;
  --color-thv22-blue: oklch(0.64 0.19 258);
  --color-thv22-violet: #a855f7;
  --color-thv22-violet: oklch(0.65 0.25 303);
  --color-thv22-teal: #2dd4bf;
  --color-thv22-teal: oklch(0.8 0.13 178);
  --color-thv22-pink: #f472b6;
  --color-thv22-pink: oklch(0.72 0.19 350);
  --font-thv22-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-22 {
  width: 100%;
  min-height: 100svh;
}

.thv-22 ::selection {
  background: var(--color-thv22-pink);
  color: #fff;
}
```
