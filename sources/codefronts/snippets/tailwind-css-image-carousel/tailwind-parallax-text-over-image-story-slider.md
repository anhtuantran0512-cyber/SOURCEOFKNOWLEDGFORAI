---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-parallax-text-over-image-story-slider/"
title: "Tailwind Parallax Text-Over-Image Story Slider"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "A presentation carousel where, on each transition, the photograph and the headline travel different distances at different speeds."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Parallax Text-Over-Image Story Slider
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-parallax-text-over-image-story-slider/

A presentation carousel where, on each transition, the photograph and the headline travel different distances at different speeds. The depth illusion is entirely a mismatch in two numbers, and Tailwind puts both numbers on the elements they move.
## HTML
```html
<section class="tcar-22 w-full min-h-svh grid place-items-center bg-tcar22-bg font-tcar22-sans px-5 py-10" aria-label="Parallax story slider">
  <div class="group relative w-[min(760px,100%)]">
    <input type="radio" name="tcar-22" id="tcar-22-1" class="sr-only" checked>
    <input type="radio" name="tcar-22" id="tcar-22-2" class="sr-only">
    <input type="radio" name="tcar-22" id="tcar-22-3" class="sr-only">
    <div class="relative aspect-[12/7] rounded-[18px] overflow-hidden shadow-[0_30px_60px_-34px_oklch(0_0_0/0.9)]">
      <article class="absolute inset-0 opacity-0 pointer-events-none transition-opacity duration-700 group-has-[#tcar-22-1:checked]:opacity-100 group-has-[#tcar-22-1:checked]:pointer-events-auto">
        <img src="https://picsum.photos/seed/plx-1/1200/700" width="1200" height="700" fetchpriority="high" decoding="async" alt="Canyon at sunrise" class="absolute inset-0 size-full object-cover scale-[1.12] translate-x-[6%] transition-[scale,translate] duration-1000 ease-[cubic-bezier(0.2,0.8,0.2,1)] group-has-[#tcar-22-1:checked]:scale-[1.06] group-has-[#tcar-22-1:checked]:translate-x-0 motion-reduce:transition-none motion-reduce:scale-100 motion-reduce:translate-x-0">
        <div aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(90deg,oklch(0.14_0.01_265/0.82),transparent_65%)]"></div>
        <div class="absolute left-0 bottom-0 z-[2] p-[clamp(22px,5vw,52px)] max-w-[70%] text-white -translate-x-[14%] opacity-0 transition-[translate,opacity] duration-[800ms] delay-[120ms] ease-[cubic-bezier(0.2,0.8,0.2,1)] group-has-[#tcar-22-1:checked]:translate-x-0 group-has-[#tcar-22-1:checked]:opacity-100 motion-reduce:transition-opacity motion-reduce:translate-x-0">
          <p class="text-xs tracking-[0.2em] uppercase text-tcar22-acc mb-2.5">Chapter 01</p>
          <h3 class="text-[clamp(26px,5vw,44px)] font-extrabold leading-[1.05] tracking-[-0.01em] m-0 [text-shadow:0_2px_20px_oklch(0_0_0/0.5)]">Into the canyon</h3>
          <p class="text-[15px] leading-[1.55] text-tcar22-lead mt-3 max-w-[36ch]">Where light carves the rock a little differently every hour.</p>
        </div>
      </article>
      <article class="absolute inset-0 opacity-0 pointer-events-none transition-opacity duration-700 group-has-[#tcar-22-2:checked]:opacity-100 group-has-[#tcar-22-2:checked]:pointer-events-auto">
        <img src="https://picsum.photos/seed/plx-2/1200/700" width="1200" height="700" loading="lazy" decoding="async" alt="Open ocean" class="absolute inset-0 size-full object-cover scale-[1.12] translate-x-[6%] transition-[scale,translate] duration-1000 ease-[cubic-bezier(0.2,0.8,0.2,1)] group-has-[#tcar-22-2:checked]:scale-[1.06] group-has-[#tcar-22-2:checked]:translate-x-0 motion-reduce:transition-none motion-reduce:scale-100 motion-reduce:translate-x-0">
        <div aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(90deg,oklch(0.14_0.01_265/0.82),transparent_65%)]"></div>
        <div class="absolute left-0 bottom-0 z-[2] p-[clamp(22px,5vw,52px)] max-w-[70%] text-white -translate-x-[14%] opacity-0 transition-[translate,opacity] duration-[800ms] delay-[120ms] ease-[cubic-bezier(0.2,0.8,0.2,1)] group-has-[#tcar-22-2:checked]:translate-x-0 group-has-[#tcar-22-2:checked]:opacity-100 motion-reduce:transition-opacity motion-reduce:translate-x-0">
          <p class="text-xs tracking-[0.2em] uppercase text-tcar22-acc mb-2.5">Chapter 02</p>
          <h3 class="text-[clamp(26px,5vw,44px)] font-extrabold leading-[1.05] tracking-[-0.01em] m-0 [text-shadow:0_2px_20px_oklch(0_0_0/0.5)]">Beyond the shore</h3>
          <p class="text-[15px] leading-[1.55] text-tcar22-lead mt-3 max-w-[36ch]">Nothing but horizon, and the sound of the hull.</p>
        </div>
      </article>
      <article class="absolute inset-0 opacity-0 pointer-events-none transition-opacity duration-700 group-has-[#tcar-22-3:checked]:opacity-100 group-has-[#tcar-22-3:checked]:pointer-events-auto">
        <img src="https://picsum.photos/seed/plx-3/1200/700" width="1200" height="700" loading="lazy" decoding="async" alt="Alpine ridge" class="absolute inset-0 size-full object-cover scale-[1.12] translate-x-[6%] transition-[scale,translate] duration-1000 ease-[cubic-bezier(0.2,0.8,0.2,1)] group-has-[#tcar-22-3:checked]:scale-[1.06] group-has-[#tcar-22-3:checked]:translate-x-0 motion-reduce:transition-none motion-reduce:scale-100 motion-reduce:translate-x-0">
        <div aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(90deg,oklch(0.14_0.01_265/0.82),transparent_65%)]"></div>
        <div class="absolute left-0 bottom-0 z-[2] p-[clamp(22px,5vw,52px)] max-w-[70%] text-white -translate-x-[14%] opacity-0 transition-[translate,opacity] duration-[800ms] delay-[120ms] ease-[cubic-bezier(0.2,0.8,0.2,1)] group-has-[#tcar-22-3:checked]:translate-x-0 group-has-[#tcar-22-3:checked]:opacity-100 motion-reduce:transition-opacity motion-reduce:translate-x-0">
          <p class="text-xs tracking-[0.2em] uppercase text-tcar22-acc mb-2.5">Chapter 03</p>
          <h3 class="text-[clamp(26px,5vw,44px)] font-extrabold leading-[1.05] tracking-[-0.01em] m-0 [text-shadow:0_2px_20px_oklch(0_0_0/0.5)]">Above the clouds</h3>
          <p class="text-[15px] leading-[1.55] text-tcar22-lead mt-3 max-w-[36ch]">The last ridge before the summit, and the quiet up there.</p>
        </div>
      </article>
    </div>
    <div class="absolute right-[clamp(2px,1.5vw,24px)] bottom-[clamp(2px,1.5vw,24px)] z-[3] flex">
      <label for="tcar-22-1" aria-label="Chapter 1" class="group/pip size-11 grid place-items-center cursor-pointer"><span class="size-3 rounded-full bg-tcar22-pip shadow-[0_0_0_1px_oklch(0_0_0/0.35)] transition-[scale,background-color] duration-200 group-hover/pip:bg-tcar22-piphover group-has-[#tcar-22-1:checked]:bg-tcar22-acc group-has-[#tcar-22-1:checked]:scale-[1.3] group-has-[#tcar-22-1:focus-visible]:outline-3 group-has-[#tcar-22-1:focus-visible]:outline-tcar22-acc group-has-[#tcar-22-1:focus-visible]:outline-offset-[3px] motion-reduce:transition-none"></span></label>
      <label for="tcar-22-2" aria-label="Chapter 2" class="group/pip size-11 grid place-items-center cursor-pointer"><span class="size-3 rounded-full bg-tcar22-pip shadow-[0_0_0_1px_oklch(0_0_0/0.35)] transition-[scale,background-color] duration-200 group-hover/pip:bg-tcar22-piphover group-has-[#tcar-22-2:checked]:bg-tcar22-acc group-has-[#tcar-22-2:checked]:scale-[1.3] group-has-[#tcar-22-2:focus-visible]:outline-3 group-has-[#tcar-22-2:focus-visible]:outline-tcar22-acc group-has-[#tcar-22-2:focus-visible]:outline-offset-[3px] motion-reduce:transition-none"></span></label>
      <label for="tcar-22-3" aria-label="Chapter 3" class="group/pip size-11 grid place-items-center cursor-pointer"><span class="size-3 rounded-full bg-tcar22-pip shadow-[0_0_0_1px_oklch(0_0_0/0.35)] transition-[scale,background-color] duration-200 group-hover/pip:bg-tcar22-piphover group-has-[#tcar-22-3:checked]:bg-tcar22-acc group-has-[#tcar-22-3:checked]:scale-[1.3] group-has-[#tcar-22-3:focus-visible]:outline-3 group-has-[#tcar-22-3:focus-visible]:outline-tcar22-acc group-has-[#tcar-22-3:focus-visible]:outline-offset-[3px] motion-reduce:transition-none"></span></label>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar22-bg: #0c0d10;
  --color-tcar22-bg: oklch(0.16 0.006 265);
  --color-tcar22-lead: #dfe2e8;
  --color-tcar22-lead: oklch(0.9 0.006 265);
  --color-tcar22-pip: #ffffff;
  --color-tcar22-pip: oklch(1 0 0 / 0.4);
  --color-tcar22-piphover: #ffffff;
  --color-tcar22-piphover: oklch(1 0 0 / 0.68);
  --color-tcar22-acc: #f5c542;
  --color-tcar22-acc: oklch(0.84 0.14 88);
  --font-tcar22-sans: 'Archivo', system-ui, sans-serif;
}

.tcar-22 {
  width: 100%;
  min-height: 100svh;
}

.tcar-22 ::selection {
  background: #fff;
  color: #111;
}
```
