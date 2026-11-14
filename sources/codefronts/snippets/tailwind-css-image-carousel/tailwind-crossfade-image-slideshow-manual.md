---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-crossfade-image-slideshow-manual/"
title: "Tailwind Cross-Fade Image Slideshow with Manual Controls"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "A manual slideshow that dissolves between photographs with pure opacity — no sliding, no reflow, no autoplay."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Cross-Fade Image Slideshow with Manual Controls
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-crossfade-image-slideshow-manual/

A manual slideshow that dissolves between photographs with pure opacity — no sliding, no reflow, no autoplay. The calm alternative to an auto-advancing hero, and the simplest possible demonstration of the group-has- state pattern.
## HTML
```html
<section class="tcar-14 w-full min-h-svh grid place-items-center bg-tcar14-bg font-tcar14-sans px-5 py-10" aria-label="Photo slideshow">
  <div class="group w-[min(620px,100%)]">
    <input type="radio" name="tcar-14" id="tcar-14-1" class="sr-only" checked>
    <input type="radio" name="tcar-14" id="tcar-14-2" class="sr-only">
    <input type="radio" name="tcar-14" id="tcar-14-3" class="sr-only">
    <input type="radio" name="tcar-14" id="tcar-14-4" class="sr-only">
    <div class="relative aspect-[3/2] rounded-2xl overflow-hidden bg-tcar14-ph shadow-[0_26px_50px_-32px_oklch(0_0_0/0.9)]">
      <img src="https://picsum.photos/seed/fade-1/900/600" width="900" height="600" fetchpriority="high" decoding="async" alt="Foggy harbour at dawn" class="absolute inset-0 size-full object-cover opacity-0 transition-opacity duration-[800ms] ease-out group-has-[#tcar-14-1:checked]:opacity-100 motion-reduce:transition-none">
      <img src="https://picsum.photos/seed/fade-2/900/600" width="900" height="600" loading="lazy" decoding="async" alt="Neon-lit alley at night" class="absolute inset-0 size-full object-cover opacity-0 transition-opacity duration-[800ms] ease-out group-has-[#tcar-14-2:checked]:opacity-100 motion-reduce:transition-none">
      <img src="https://picsum.photos/seed/fade-3/900/600" width="900" height="600" loading="lazy" decoding="async" alt="Snowy mountain village" class="absolute inset-0 size-full object-cover opacity-0 transition-opacity duration-[800ms] ease-out group-has-[#tcar-14-3:checked]:opacity-100 motion-reduce:transition-none">
      <img src="https://picsum.photos/seed/fade-4/900/600" width="900" height="600" loading="lazy" decoding="async" alt="Field of lavender" class="absolute inset-0 size-full object-cover opacity-0 transition-opacity duration-[800ms] ease-out group-has-[#tcar-14-4:checked]:opacity-100 motion-reduce:transition-none">
    </div>
    <div class="flex gap-2.5 justify-center mt-4">
      <label for="tcar-14-1" aria-label="Slide 1" class="relative w-[34px] h-[5px] rounded-full bg-tcar14-dot cursor-pointer transition-colors duration-250 before:content-[''] before:absolute before:-inset-x-1 before:-inset-y-[19px] hover:bg-tcar14-dothover group-has-[#tcar-14-1:checked]:bg-tcar14-acc group-has-[#tcar-14-1:focus-visible]:outline-3 group-has-[#tcar-14-1:focus-visible]:outline-tcar14-acc group-has-[#tcar-14-1:focus-visible]:outline-offset-[6px]"></label>
      <label for="tcar-14-2" aria-label="Slide 2" class="relative w-[34px] h-[5px] rounded-full bg-tcar14-dot cursor-pointer transition-colors duration-250 before:content-[''] before:absolute before:-inset-x-1 before:-inset-y-[19px] hover:bg-tcar14-dothover group-has-[#tcar-14-2:checked]:bg-tcar14-acc group-has-[#tcar-14-2:focus-visible]:outline-3 group-has-[#tcar-14-2:focus-visible]:outline-tcar14-acc group-has-[#tcar-14-2:focus-visible]:outline-offset-[6px]"></label>
      <label for="tcar-14-3" aria-label="Slide 3" class="relative w-[34px] h-[5px] rounded-full bg-tcar14-dot cursor-pointer transition-colors duration-250 before:content-[''] before:absolute before:-inset-x-1 before:-inset-y-[19px] hover:bg-tcar14-dothover group-has-[#tcar-14-3:checked]:bg-tcar14-acc group-has-[#tcar-14-3:focus-visible]:outline-3 group-has-[#tcar-14-3:focus-visible]:outline-tcar14-acc group-has-[#tcar-14-3:focus-visible]:outline-offset-[6px]"></label>
      <label for="tcar-14-4" aria-label="Slide 4" class="relative w-[34px] h-[5px] rounded-full bg-tcar14-dot cursor-pointer transition-colors duration-250 before:content-[''] before:absolute before:-inset-x-1 before:-inset-y-[19px] hover:bg-tcar14-dothover group-has-[#tcar-14-4:checked]:bg-tcar14-acc group-has-[#tcar-14-4:focus-visible]:outline-3 group-has-[#tcar-14-4:focus-visible]:outline-tcar14-acc group-has-[#tcar-14-4:focus-visible]:outline-offset-[6px]"></label>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar14-bg: #0f1720;
  --color-tcar14-bg: oklch(0.2 0.02 250);
  --color-tcar14-ph: #1b2733;
  --color-tcar14-ph: oklch(0.26 0.02 250);
  --color-tcar14-dot: #31404f;
  --color-tcar14-dot: oklch(0.36 0.022 250);
  --color-tcar14-dothover: #56697c;
  --color-tcar14-dothover: oklch(0.52 0.03 250);
  --color-tcar14-acc: #38b6f0;
  --color-tcar14-acc: oklch(0.73 0.14 230);
  --font-tcar14-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tcar-14 {
  width: 100%;
  min-height: 100svh;
}

.tcar-14 ::selection {
  background: var(--color-tcar14-acc);
  color: #062030;
}
```
