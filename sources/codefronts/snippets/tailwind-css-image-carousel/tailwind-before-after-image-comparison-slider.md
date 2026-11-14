---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-before-after-image-comparison-slider/"
title: "Tailwind Before / After Image Comparison Slider"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "A draggable divider that wipes between 'before' and 'after' versions of one photograph."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Before / After Image Comparison Slider
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-before-after-image-comparison-slider/

A draggable divider that wipes between 'before' and 'after' versions of one photograph. A native range input is the control — so keyboard, screen reader and touch support arrive for free — and three lines of JS write its value into one custom property that CSS reads.
## HTML
```html
<section class="tcar-18 w-full min-h-svh grid place-items-center bg-tcar18-bg font-tcar18-sans px-5 py-10" aria-label="Before and after comparison">
  <figure style="--pos:50" class="group tcar18-cmp relative w-[min(620px,100%)] aspect-[3/2] m-0 rounded-2xl overflow-hidden select-none shadow-[0_26px_50px_-32px_oklch(0_0_0/0.9)]">
    <img src="https://picsum.photos/seed/edit-shot/900/600" width="900" height="600" decoding="async" alt="After: colour-graded edit" class="absolute inset-0 size-full object-cover block">
    <img src="https://picsum.photos/seed/edit-shot/900/600?grayscale" width="900" height="600" decoding="async" alt="Before: original photo" class="absolute inset-0 size-full object-cover block [clip-path:inset(0_0_0_calc(var(--pos)*1%))]">
    <input type="range" min="0" max="100" value="50" aria-label="Reveal amount: drag to compare before and after" class="peer absolute inset-0 size-full m-0 opacity-0 cursor-ew-resize z-[3]">
    <span aria-hidden="true" class="absolute inset-y-0 left-[calc(var(--pos)*1%)] w-0.5 -translate-x-px bg-white pointer-events-none shadow-[0_0_0_1px_oklch(0_0_0/0.25)] peer-focus-visible:shadow-[0_0_0_3px_var(--color-tcar18-acc)]">
      <span class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 size-11 rounded-full bg-white text-tcar18-acc flex items-center justify-center text-base font-bold shadow-[0_4px_12px_oklch(0_0_0/0.4)] group-has-[input:focus-visible]:shadow-[0_0_0_3px_var(--color-tcar18-acc),0_4px_12px_oklch(0_0_0/0.4)]">&#8660;</span>
    </span>
    <span aria-hidden="true" class="absolute bottom-3.5 left-3.5 px-3 py-1.5 rounded-full text-[11px] font-bold tracking-[0.08em] uppercase text-white bg-tcar18-badge backdrop-blur-[4px]">Before</span>
    <span aria-hidden="true" class="absolute bottom-3.5 right-3.5 px-3 py-1.5 rounded-full text-[11px] font-bold tracking-[0.08em] uppercase text-white bg-tcar18-badge backdrop-blur-[4px]">After</span>
  </figure>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar18-bg: #0d1412;
  --color-tcar18-bg: oklch(0.18 0.018 165);
  --color-tcar18-acc: #10b981;
  --color-tcar18-acc: oklch(0.7 0.15 165);
  --color-tcar18-badge: #0a0e0d;
  --color-tcar18-badge: oklch(0.16 0.01 165 / 0.66);
  --font-tcar18-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tcar-18 {
  width: 100%;
  min-height: 100svh;
}

.tcar-18 ::selection {
  background: var(--color-tcar18-acc);
  color: #04201a;
}
```

## JavaScript
```js
// Three lines: the range's value becomes --pos, and CSS does the rest.
document.querySelectorAll('.tcar18-cmp').forEach((cmp) => {
  const range = cmp.querySelector('input[type="range"]');
  const sync = () => cmp.style.setProperty('--pos', range.value);
  range.addEventListener('input', sync);
  sync();
});
```
