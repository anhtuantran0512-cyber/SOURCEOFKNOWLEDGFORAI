---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-duotone-image-hover-effect/"
title: "Tailwind Duotone Image Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Four colour-grade transitions — grayscale to full colour, duotone to natural, a hue-rotate grade and a desaturate fade-in."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Duotone Image Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-duotone-image-hover-effect/

Four colour-grade transitions — grayscale to full colour, duotone to natural, a hue-rotate grade and a desaturate fade-in. grayscale, saturate-* and isolate are all core utilities, so only the filter chains stay arbitrary.
## HTML
```html
<section class="thv-21 w-full min-h-svh grid place-items-center bg-thv21-bg font-thv21-sans px-6 py-14">
  <div class="w-[min(760px,100%)] grid grid-cols-[repeat(auto-fit,minmax(280px,1fr))] gap-8">
    <figure class="group flex flex-col gap-3 m-0">
      <div class="relative isolate w-full aspect-video overflow-hidden rounded-xl cursor-pointer">
        <img src="https://images.unsplash.com/photo-1493809842364-78817add7ffb?auto=format&fit=crop&w=900&q=80" alt="Blue velvet armchair in a bare studio" decoding="async" class="w-full h-full [filter:grayscale(1)_contrast(1.1)] transition-[filter] duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-hover:filter-none object-cover">
      </div>
      <figcaption class="text-[11px] tracking-[0.12em] uppercase text-thv21-dim">grayscale → colour restore</figcaption>
    </figure>
    <figure class="group flex flex-col gap-3 m-0">
      <div class="relative isolate w-full aspect-video overflow-hidden rounded-xl cursor-pointer">
        <img src="https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=900&q=80" alt="Minimal bedroom with linen bedding and morning light" decoding="async" class="w-full h-full [filter:contrast(1.1)] object-cover">
        <div aria-hidden="true" class="absolute inset-0 mix-blend-color opacity-100 transition-opacity duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-hover:opacity-0 bg-[linear-gradient(135deg,#1e003c,#ff6b00)]"></div>
      </div>
      <figcaption class="text-[11px] tracking-[0.12em] uppercase text-thv21-dim">duotone → natural</figcaption>
    </figure>
    <figure class="group flex flex-col gap-3 m-0">
      <div class="relative isolate w-full aspect-video overflow-hidden rounded-xl cursor-pointer">
        <img src="https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?auto=format&fit=crop&w=900&q=80" alt="Concrete and timber staircase in a modern house" decoding="async" class="w-full h-full [filter:hue-rotate(0deg)_saturate(1)] transition-[filter] duration-600 ease-[cubic-bezier(.4,0,.2,1)] group-hover:[filter:hue-rotate(160deg)_saturate(1.5)] object-cover">
      </div>
      <figcaption class="text-[11px] tracking-[0.12em] uppercase text-thv21-dim">hue-rotate grade</figcaption>
    </figure>
    <figure class="group flex flex-col gap-3 m-0">
      <div class="relative isolate w-full aspect-video overflow-hidden rounded-xl cursor-pointer">
        <img src="https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?auto=format&fit=crop&w=900&q=80" alt="Reading corner with a low lounge chair and side table" decoding="async" class="w-full h-full grayscale transition-[filter] duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-hover:grayscale-0 group-hover:saturate-125 object-cover">
      </div>
      <figcaption class="text-[11px] tracking-[0.12em] uppercase text-thv21-dim">desaturate fade-in</figcaption>
    </figure>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv21-bg: #080608;
  --color-thv21-bg: oklch(0.11 0.01 320);
  --color-thv21-dim: #8e8b90;
  --color-thv21-dim: oklch(0.65 0.01 320);
  --font-thv21-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-21 {
  width: 100%;
  min-height: 100svh;
}

.thv-21 ::selection {
  background: #9333ea;
  color: #fff;
}
```
