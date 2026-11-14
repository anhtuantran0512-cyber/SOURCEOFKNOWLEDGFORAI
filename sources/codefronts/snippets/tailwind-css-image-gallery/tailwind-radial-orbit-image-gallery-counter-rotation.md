---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-radial-orbit-image-gallery-counter-rotation/"
title: "Tailwind Radial Orbit Image Gallery with Counter-Rotating Thumbnails"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "Circular thumbnails spaced evenly around a central hero, revolving slowly like planets and pausing the moment you reach for one."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Radial Orbit Image Gallery with Counter-Rotating Thumbnails
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-radial-orbit-image-gallery-counter-rotation/

Circular thumbnails spaced evenly around a central hero, revolving slowly like planets and pausing the moment you reach for one. The port's interesting move is that the ring animation becomes a real animate-* utility through @theme, while the per-satellite angle stays inline data.
## HTML
```html
<section class="tgl-05 w-full min-h-svh grid place-items-center px-5 py-10 font-tgl05-sans bg-[radial-gradient(120%_120%_at_50%_40%,oklch(0.26_0.06_290),oklch(0.09_0.02_280))] [--r:170px] max-[560px]:[--r:120px]" aria-label="Radial orbit gallery">
  <div class="group relative grid place-items-center w-[calc(var(--r)*2+90px)] h-[calc(var(--r)*2+90px)]">
    <div class="w-[120px] h-[120px] rounded-full overflow-hidden z-[2] shadow-[0_0_40px_-6px_var(--color-tgl05-acc),0_0_0_4px_rgba(255,255,255,0.1)]">
      <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=300&h=300&auto=format&fit=crop" alt="Spiral galaxy, featured image" loading="lazy" decoding="async" class="w-full h-full object-cover">
    </div>
    <div class="absolute inset-0 animate-tgl05-spin group-hover:[animation-play-state:paused] group-focus-within:[animation-play-state:paused] motion-reduce:animate-none">
      <a href="#" style="--a:0deg" class="group/sat absolute top-1/2 left-1/2 w-[66px] h-[66px] -m-[33px] rounded-full overflow-hidden no-underline animate-tgl05-spin [animation-direction:reverse] [transform:rotate(var(--a))_translate(var(--r))_rotate(calc(-1*var(--a)))] shadow-[0_0_0_3px_rgba(255,255,255,0.12),0_8px_20px_-8px_rgba(0,0,0,0.6)] transition-shadow duration-300 hover:shadow-[0_0_0_3px_var(--color-tgl05-acc)] focus-visible:shadow-[0_0_0_3px_var(--color-tgl05-acc)] focus-visible:outline-3 focus-visible:outline-tgl05-acc focus-visible:outline-offset-[3px] motion-reduce:animate-none max-[560px]:w-[54px] max-[560px]:h-[54px] max-[560px]:-m-[27px]">
        <img src="https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?q=80&w=200&h=200&auto=format&fit=crop" alt="Planet surface" loading="lazy" decoding="async" class="w-full h-full object-cover transition-transform duration-300 group-hover/sat:scale-[1.12] motion-reduce:transition-none">
      </a>
      <a href="#" style="--a:45deg" class="group/sat absolute top-1/2 left-1/2 w-[66px] h-[66px] -m-[33px] rounded-full overflow-hidden no-underline animate-tgl05-spin [animation-direction:reverse] [transform:rotate(var(--a))_translate(var(--r))_rotate(calc(-1*var(--a)))] shadow-[0_0_0_3px_rgba(255,255,255,0.12),0_8px_20px_-8px_rgba(0,0,0,0.6)] transition-shadow duration-300 hover:shadow-[0_0_0_3px_var(--color-tgl05-acc)] focus-visible:shadow-[0_0_0_3px_var(--color-tgl05-acc)] focus-visible:outline-3 focus-visible:outline-tgl05-acc focus-visible:outline-offset-[3px] motion-reduce:animate-none max-[560px]:w-[54px] max-[560px]:h-[54px] max-[560px]:-m-[27px]">
        <img src="https://images.unsplash.com/photo-1620121692029-d088224ddc74?q=80&w=200&h=200&auto=format&fit=crop" alt="Full moon" loading="lazy" decoding="async" class="w-full h-full object-cover transition-transform duration-300 group-hover/sat:scale-[1.12] motion-reduce:transition-none">
      </a>
      <a href="#" style="--a:90deg" class="group/sat absolute top-1/2 left-1/2 w-[66px] h-[66px] -m-[33px] rounded-full overflow-hidden no-underline animate-tgl05-spin [animation-direction:reverse] [transform:rotate(var(--a))_translate(var(--r))_rotate(calc(-1*var(--a)))] shadow-[0_0_0_3px_rgba(255,255,255,0.12),0_8px_20px_-8px_rgba(0,0,0,0.6)] transition-shadow duration-300 hover:shadow-[0_0_0_3px_var(--color-tgl05-acc)] focus-visible:shadow-[0_0_0_3px_var(--color-tgl05-acc)] focus-visible:outline-3 focus-visible:outline-tgl05-acc focus-visible:outline-offset-[3px] motion-reduce:animate-none max-[560px]:w-[54px] max-[560px]:h-[54px] max-[560px]:-m-[27px]">
        <img src="https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?q=80&w=200&h=200&auto=format&fit=crop" alt="Bright star field" loading="lazy" decoding="async" class="w-full h-full object-cover transition-transform duration-300 group-hover/sat:scale-[1.12] motion-reduce:transition-none">
      </a>
      <a href="#" style="--a:135deg" class="group/sat absolute top-1/2 left-1/2 w-[66px] h-[66px] -m-[33px] rounded-full overflow-hidden no-underline animate-tgl05-spin [animation-direction:reverse] [transform:rotate(var(--a))_translate(var(--r))_rotate(calc(-1*var(--a)))] shadow-[0_0_0_3px_rgba(255,255,255,0.12),0_8px_20px_-8px_rgba(0,0,0,0.6)] transition-shadow duration-300 hover:shadow-[0_0_0_3px_var(--color-tgl05-acc)] focus-visible:shadow-[0_0_0_3px_var(--color-tgl05-acc)] focus-visible:outline-3 focus-visible:outline-tgl05-acc focus-visible:outline-offset-[3px] motion-reduce:animate-none max-[560px]:w-[54px] max-[560px]:h-[54px] max-[560px]:-m-[27px]">
        <img src="https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?q=80&w=200&h=200&auto=format&fit=crop" alt="Coloured nebula" loading="lazy" decoding="async" class="w-full h-full object-cover transition-transform duration-300 group-hover/sat:scale-[1.12] motion-reduce:transition-none">
      </a>
      <a href="#" style="--a:180deg" class="group/sat absolute top-1/2 left-1/2 w-[66px] h-[66px] -m-[33px] rounded-full overflow-hidden no-underline animate-tgl05-spin [animation-direction:reverse] [transform:rotate(var(--a))_translate(var(--r))_rotate(calc(-1*var(--a)))] shadow-[0_0_0_3px_rgba(255,255,255,0.12),0_8px_20px_-8px_rgba(0,0,0,0.6)] transition-shadow duration-300 hover:shadow-[0_0_0_3px_var(--color-tgl05-acc)] focus-visible:shadow-[0_0_0_3px_var(--color-tgl05-acc)] focus-visible:outline-3 focus-visible:outline-tgl05-acc focus-visible:outline-offset-[3px] motion-reduce:animate-none max-[560px]:w-[54px] max-[560px]:h-[54px] max-[560px]:-m-[27px]">
        <img src="https://images.unsplash.com/photo-1517180102446-f3ece451e9d8?q=80&w=200&h=200&auto=format&fit=crop" alt="Comet trail" loading="lazy" decoding="async" class="w-full h-full object-cover transition-transform duration-300 group-hover/sat:scale-[1.12] motion-reduce:transition-none">
      </a>
      <a href="#" style="--a:225deg" class="group/sat absolute top-1/2 left-1/2 w-[66px] h-[66px] -m-[33px] rounded-full overflow-hidden no-underline animate-tgl05-spin [animation-direction:reverse] [transform:rotate(var(--a))_translate(var(--r))_rotate(calc(-1*var(--a)))] shadow-[0_0_0_3px_rgba(255,255,255,0.12),0_8px_20px_-8px_rgba(0,0,0,0.6)] transition-shadow duration-300 hover:shadow-[0_0_0_3px_var(--color-tgl05-acc)] focus-visible:shadow-[0_0_0_3px_var(--color-tgl05-acc)] focus-visible:outline-3 focus-visible:outline-tgl05-acc focus-visible:outline-offset-[3px] motion-reduce:animate-none max-[560px]:w-[54px] max-[560px]:h-[54px] max-[560px]:-m-[27px]">
        <img src="https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?q=80&w=200&h=200&auto=format&fit=crop" alt="Night sky" loading="lazy" decoding="async" class="w-full h-full object-cover transition-transform duration-300 group-hover/sat:scale-[1.12] motion-reduce:transition-none">
      </a>
      <a href="#" style="--a:270deg" class="group/sat absolute top-1/2 left-1/2 w-[66px] h-[66px] -m-[33px] rounded-full overflow-hidden no-underline animate-tgl05-spin [animation-direction:reverse] [transform:rotate(var(--a))_translate(var(--r))_rotate(calc(-1*var(--a)))] shadow-[0_0_0_3px_rgba(255,255,255,0.12),0_8px_20px_-8px_rgba(0,0,0,0.6)] transition-shadow duration-300 hover:shadow-[0_0_0_3px_var(--color-tgl05-acc)] focus-visible:shadow-[0_0_0_3px_var(--color-tgl05-acc)] focus-visible:outline-3 focus-visible:outline-tgl05-acc focus-visible:outline-offset-[3px] motion-reduce:animate-none max-[560px]:w-[54px] max-[560px]:h-[54px] max-[560px]:-m-[27px]">
        <img src="https://images.unsplash.com/photo-1590490360182-c33d57733427?q=80&w=200&h=200&auto=format&fit=crop" alt="Observatory telescope" loading="lazy" decoding="async" class="w-full h-full object-cover transition-transform duration-300 group-hover/sat:scale-[1.12] motion-reduce:transition-none">
      </a>
      <a href="#" style="--a:315deg" class="group/sat absolute top-1/2 left-1/2 w-[66px] h-[66px] -m-[33px] rounded-full overflow-hidden no-underline animate-tgl05-spin [animation-direction:reverse] [transform:rotate(var(--a))_translate(var(--r))_rotate(calc(-1*var(--a)))] shadow-[0_0_0_3px_rgba(255,255,255,0.12),0_8px_20px_-8px_rgba(0,0,0,0.6)] transition-shadow duration-300 hover:shadow-[0_0_0_3px_var(--color-tgl05-acc)] focus-visible:shadow-[0_0_0_3px_var(--color-tgl05-acc)] focus-visible:outline-3 focus-visible:outline-tgl05-acc focus-visible:outline-offset-[3px] motion-reduce:animate-none max-[560px]:w-[54px] max-[560px]:h-[54px] max-[560px]:-m-[27px]">
        <img src="https://images.unsplash.com/photo-1444723121867-7a241cacace9?q=80&w=200&h=200&auto=format&fit=crop" alt="Star chart detail" loading="lazy" decoding="async" class="w-full h-full object-cover transition-transform duration-300 group-hover/sat:scale-[1.12] motion-reduce:transition-none">
      </a>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl05-acc: #9b8cf0;
  --color-tgl05-acc: oklch(0.72 0.16 285);
  --font-tgl05-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tgl05-spin: tgl05-spin 26s linear infinite;
}
/* @keyframes has no utility form — it is the one thing that must stay CSS. */

@keyframes tgl05-spin {
  to {
    transform: rotate(360deg);
  }
}

.tgl-05 {
  width: 100%;
  min-height: 100svh;
}

.tgl-05 ::selection {
  background: var(--color-tgl05-acc);
  color: #fff;
}
```
