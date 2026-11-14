---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-product-colour-variant-picker-slider/"
title: "Tailwind Product Colour Variant Picker Slider"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "Click a swatch to swap the product photo — the apparel and furniture variant picker."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Product Colour Variant Picker Slider
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-product-colour-variant-picker-slider/

Click a swatch to swap the product photo — the apparel and furniture variant picker. Three elements change per choice (photo, swatch ring, colour caption) and in Tailwind all three carry the same group-has-[#id:checked]: condition, which is the clearest argument for the pattern.
## HTML
```html
<section class="tcar-04 w-full min-h-svh grid place-items-center bg-tcar04-bg font-tcar04-sans px-5 py-10" aria-label="Product colour variant picker">
  <div class="group w-[min(400px,100%)] bg-white rounded-[18px] overflow-hidden shadow-[0_24px_50px_-34px_oklch(0.3_0.03_265/0.6)]">
    <input type="radio" name="tcar-04" id="tcar-04-1" class="sr-only" checked>
    <input type="radio" name="tcar-04" id="tcar-04-2" class="sr-only">
    <input type="radio" name="tcar-04" id="tcar-04-3" class="sr-only">
    <div class="relative aspect-square bg-tcar04-ph">
      <img src="https://picsum.photos/seed/chair-slate/700/700" width="700" height="700" fetchpriority="high" decoding="async" alt="Lounge chair in slate" class="absolute inset-0 size-full object-cover opacity-0 transition-opacity duration-500 ease-out group-has-[#tcar-04-1:checked]:opacity-100 motion-reduce:transition-none">
      <img src="https://picsum.photos/seed/chair-ochre/700/700" width="700" height="700" loading="lazy" decoding="async" alt="Lounge chair in ochre" class="absolute inset-0 size-full object-cover opacity-0 transition-opacity duration-500 ease-out group-has-[#tcar-04-2:checked]:opacity-100 motion-reduce:transition-none">
      <img src="https://picsum.photos/seed/chair-moss/700/700" width="700" height="700" loading="lazy" decoding="async" alt="Lounge chair in moss" class="absolute inset-0 size-full object-cover opacity-0 transition-opacity duration-500 ease-out group-has-[#tcar-04-3:checked]:opacity-100 motion-reduce:transition-none">
    </div>
    <div class="flex items-center justify-between gap-3.5 px-5 pt-4 pb-5">
      <p class="text-sm text-tcar04-mute m-0"><span class="font-semibold text-tcar04-ink">Colour:</span>
        <span class="hidden font-semibold text-tcar04-ink group-has-[#tcar-04-1:checked]:inline">Slate</span><span class="hidden font-semibold text-tcar04-ink group-has-[#tcar-04-2:checked]:inline">Ochre</span><span class="hidden font-semibold text-tcar04-ink group-has-[#tcar-04-3:checked]:inline">Moss</span>
      </p>
      <div class="flex gap-4">
        <label for="tcar-04-1" aria-label="Slate" style="background:#5b6470" class="relative size-7 rounded-full cursor-pointer border-2 border-white shadow-[0_0_0_1px_oklch(0_0_0/0.14)] transition-[scale,box-shadow] duration-200 before:content-[''] before:absolute before:-inset-2 before:rounded-full hover:scale-[1.08] group-has-[#tcar-04-1:checked]:scale-[1.12] group-has-[#tcar-04-1:checked]:shadow-[0_0_0_2px_var(--color-tcar04-acc)] group-has-[#tcar-04-1:focus-visible]:outline-3 group-has-[#tcar-04-1:focus-visible]:outline-tcar04-acc group-has-[#tcar-04-1:focus-visible]:outline-offset-[3px] motion-reduce:transition-none"></label>
        <label for="tcar-04-2" aria-label="Ochre" style="background:#c98a2b" class="relative size-7 rounded-full cursor-pointer border-2 border-white shadow-[0_0_0_1px_oklch(0_0_0/0.14)] transition-[scale,box-shadow] duration-200 before:content-[''] before:absolute before:-inset-2 before:rounded-full hover:scale-[1.08] group-has-[#tcar-04-2:checked]:scale-[1.12] group-has-[#tcar-04-2:checked]:shadow-[0_0_0_2px_var(--color-tcar04-acc)] group-has-[#tcar-04-2:focus-visible]:outline-3 group-has-[#tcar-04-2:focus-visible]:outline-tcar04-acc group-has-[#tcar-04-2:focus-visible]:outline-offset-[3px] motion-reduce:transition-none"></label>
        <label for="tcar-04-3" aria-label="Moss" style="background:#6f8256" class="relative size-7 rounded-full cursor-pointer border-2 border-white shadow-[0_0_0_1px_oklch(0_0_0/0.14)] transition-[scale,box-shadow] duration-200 before:content-[''] before:absolute before:-inset-2 before:rounded-full hover:scale-[1.08] group-has-[#tcar-04-3:checked]:scale-[1.12] group-has-[#tcar-04-3:checked]:shadow-[0_0_0_2px_var(--color-tcar04-acc)] group-has-[#tcar-04-3:focus-visible]:outline-3 group-has-[#tcar-04-3:focus-visible]:outline-tcar04-acc group-has-[#tcar-04-3:focus-visible]:outline-offset-[3px] motion-reduce:transition-none"></label>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar04-bg: #f2f0ec;
  --color-tcar04-bg: oklch(0.95 0.006 85);
  --color-tcar04-ph: #e9e6e1;
  --color-tcar04-ph: oklch(0.93 0.006 85);
  --color-tcar04-ink: #20242c;
  --color-tcar04-ink: oklch(0.26 0.012 265);
  --color-tcar04-mute: #5a5f68;
  --color-tcar04-mute: oklch(0.48 0.012 265);
  --color-tcar04-acc: #1f2430;
  --color-tcar04-acc: oklch(0.27 0.02 265);
  --font-tcar04-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tcar-04 {
  width: 100%;
  min-height: 100svh;
}

.tcar-04 ::selection {
  background: var(--color-tcar04-acc);
  color: #fff;
}
```
