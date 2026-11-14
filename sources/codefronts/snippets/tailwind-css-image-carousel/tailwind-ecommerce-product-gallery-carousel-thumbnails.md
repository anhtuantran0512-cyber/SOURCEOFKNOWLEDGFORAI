---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-ecommerce-product-gallery-carousel-thumbnails/"
title: "Tailwind E-commerce Product Gallery Carousel with Thumbnails"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "The product-page workhorse: one large image with a strip of clickable thumbnails underneath."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind E-commerce Product Gallery Carousel with Thumbnails
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-ecommerce-product-gallery-carousel-thumbnails/

The product-page workhorse: one large image with a strip of clickable thumbnails underneath. The port's win is group-has-[#id:checked]: — twelve :nth-of-type sibling rules collapse into one utility per element, written on the element that actually changes.
## HTML
```html
<section class="tcar-01 w-full min-h-svh grid place-items-center bg-tcar01-bg font-tcar01-sans px-5 py-10" aria-label="Product image gallery">
  <div class="group w-[min(440px,100%)]">
    <input type="radio" name="tcar-01" id="tcar-01-1" class="sr-only" checked>
    <input type="radio" name="tcar-01" id="tcar-01-2" class="sr-only">
    <input type="radio" name="tcar-01" id="tcar-01-3" class="sr-only">
    <input type="radio" name="tcar-01" id="tcar-01-4" class="sr-only">
    <div class="relative aspect-square rounded-2xl overflow-hidden bg-tcar01-ph shadow-[0_20px_45px_-30px_oklch(0.3_0.03_265/0.6)]">
      <img src="https://picsum.photos/seed/sneaker-a/800/800" width="800" height="800" fetchpriority="high" decoding="async" alt="Trail runner, three-quarter view" class="absolute inset-0 size-full object-cover opacity-0 transition-opacity duration-[450ms] ease-out group-has-[#tcar-01-1:checked]:opacity-100 motion-reduce:transition-none">
      <img src="https://picsum.photos/seed/sneaker-b/800/800" width="800" height="800" loading="lazy" decoding="async" alt="Trail runner, sole detail" class="absolute inset-0 size-full object-cover opacity-0 transition-opacity duration-[450ms] ease-out group-has-[#tcar-01-2:checked]:opacity-100 motion-reduce:transition-none">
      <img src="https://picsum.photos/seed/sneaker-c/800/800" width="800" height="800" loading="lazy" decoding="async" alt="Trail runner, heel and laces" class="absolute inset-0 size-full object-cover opacity-0 transition-opacity duration-[450ms] ease-out group-has-[#tcar-01-3:checked]:opacity-100 motion-reduce:transition-none">
      <img src="https://picsum.photos/seed/sneaker-d/800/800" width="800" height="800" loading="lazy" decoding="async" alt="Trail runner, top-down view" class="absolute inset-0 size-full object-cover opacity-0 transition-opacity duration-[450ms] ease-out group-has-[#tcar-01-4:checked]:opacity-100 motion-reduce:transition-none">
    </div>
    <div class="grid grid-cols-4 gap-2.5 mt-3.5">
      <label for="tcar-01-1" class="block aspect-square rounded-xl overflow-hidden cursor-pointer bg-tcar01-ph border-2 border-transparent transition-[border-color,translate] duration-200 hover:-translate-y-0.5 group-has-[#tcar-01-1:checked]:border-tcar01-acc group-has-[#tcar-01-1:focus-visible]:outline-3 group-has-[#tcar-01-1:focus-visible]:outline-tcar01-acc group-has-[#tcar-01-1:focus-visible]:outline-offset-2 motion-reduce:transition-colors motion-reduce:hover:translate-y-0"><img src="https://picsum.photos/seed/sneaker-a/160/160" width="160" height="160" loading="lazy" decoding="async" alt="" aria-hidden="true" class="size-full object-cover block"></label>
      <label for="tcar-01-2" class="block aspect-square rounded-xl overflow-hidden cursor-pointer bg-tcar01-ph border-2 border-transparent transition-[border-color,translate] duration-200 hover:-translate-y-0.5 group-has-[#tcar-01-2:checked]:border-tcar01-acc group-has-[#tcar-01-2:focus-visible]:outline-3 group-has-[#tcar-01-2:focus-visible]:outline-tcar01-acc group-has-[#tcar-01-2:focus-visible]:outline-offset-2 motion-reduce:transition-colors motion-reduce:hover:translate-y-0"><img src="https://picsum.photos/seed/sneaker-b/160/160" width="160" height="160" loading="lazy" decoding="async" alt="" aria-hidden="true" class="size-full object-cover block"></label>
      <label for="tcar-01-3" class="block aspect-square rounded-xl overflow-hidden cursor-pointer bg-tcar01-ph border-2 border-transparent transition-[border-color,translate] duration-200 hover:-translate-y-0.5 group-has-[#tcar-01-3:checked]:border-tcar01-acc group-has-[#tcar-01-3:focus-visible]:outline-3 group-has-[#tcar-01-3:focus-visible]:outline-tcar01-acc group-has-[#tcar-01-3:focus-visible]:outline-offset-2 motion-reduce:transition-colors motion-reduce:hover:translate-y-0"><img src="https://picsum.photos/seed/sneaker-c/160/160" width="160" height="160" loading="lazy" decoding="async" alt="" aria-hidden="true" class="size-full object-cover block"></label>
      <label for="tcar-01-4" class="block aspect-square rounded-xl overflow-hidden cursor-pointer bg-tcar01-ph border-2 border-transparent transition-[border-color,translate] duration-200 hover:-translate-y-0.5 group-has-[#tcar-01-4:checked]:border-tcar01-acc group-has-[#tcar-01-4:focus-visible]:outline-3 group-has-[#tcar-01-4:focus-visible]:outline-tcar01-acc group-has-[#tcar-01-4:focus-visible]:outline-offset-2 motion-reduce:transition-colors motion-reduce:hover:translate-y-0"><img src="https://picsum.photos/seed/sneaker-d/160/160" width="160" height="160" loading="lazy" decoding="async" alt="" aria-hidden="true" class="size-full object-cover block"></label>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar01-bg: #f4f5f7;
  --color-tcar01-bg: oklch(0.96 0.003 265);
  --color-tcar01-ph: #e6e8ec;
  --color-tcar01-ph: oklch(0.92 0.005 265);
  --color-tcar01-acc: #3f7ad1;
  --color-tcar01-acc: oklch(0.62 0.16 250);
  --font-tcar01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   utilities, so the stage is sized before the browser build has compiled. */

.tcar-01 {
  width: 100%;
  min-height: 100svh;
}
/* ::selection takes no variant form. */

.tcar-01 ::selection {
  background: var(--color-tcar01-acc);
  color: #fff;
}
```
