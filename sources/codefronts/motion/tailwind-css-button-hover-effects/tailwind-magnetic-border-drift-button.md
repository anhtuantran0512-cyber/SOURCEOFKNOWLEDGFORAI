---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-magnetic-border-drift-button/"
title: "Tailwind Magnetic Border Drift Button"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A subtle high-craft CTA where the outlined frame drifts toward the cursor as it approaches, lagging behind with an elastic settle, and the label drifts a…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Magnetic Border Drift Button
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-magnetic-border-drift-button/

A subtle high-craft CTA where the outlined frame drifts toward the cursor as it approaches, lagging behind with an elastic settle, and the label drifts a fraction less for parallax. Restrained, premium, and the clearest case in the collection for keeping JavaScript to a pair of normalised numbers.
## HTML
```html
<div class="tbh-16-group w-full min-h-svh flex flex-wrap">
<section class="tbh-16a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh16-sans bg-tbh16a-stage" aria-label="Magnetic border button">
  <div id="tbh-16a-wrap" class="p-[34px] grid place-items-center">
    <button type="button" class="relative cursor-pointer rounded-full border-2 border-tbh16a-edge px-[42px] py-[18px] text-base font-bold text-tbh16a-edge bg-transparent translate-x-[calc(var(--dx,0)*14px)] translate-y-[calc(var(--dy,0)*14px)] transition-[translate,background-color,color] duration-500 ease-[cubic-bezier(.34,1.56,.64,1)] hover:bg-tbh16a-edge hover:text-tbh16a-stage focus-visible:bg-tbh16a-edge focus-visible:text-tbh16a-stage focus-visible:outline-3 focus-visible:outline-tbh16a-edge focus-visible:outline-offset-4 motion-reduce:transition-[background-color,color] motion-reduce:duration-200">
      <span class="inline-block translate-x-[calc(var(--dx,0)*6px)] translate-y-[calc(var(--dy,0)*6px)] transition-[translate] duration-500 ease-[cubic-bezier(.34,1.56,.64,1)] motion-reduce:transition-none">Let's talk</span>
    </button>
  </div>
</section>
<section class="tbh-16b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh16-sans bg-tbh16b-stage" aria-label="Magnetic filled button">
  <div id="tbh-16b-wrap" class="p-10 grid place-items-center">
    <button type="button" class="relative cursor-pointer border-0 rounded-[14px] px-11 py-[18px] text-base font-extrabold text-white bg-tbh16b-acc shadow-[0_14px_30px_-14px_var(--color-tbh16b-acc)] translate-x-[calc(var(--dx,0)*18px)] translate-y-[calc(var(--dy,0)*18px)] transition-[translate,box-shadow] duration-[450ms] ease-[cubic-bezier(.34,1.56,.64,1)] hover:shadow-[0_22px_44px_-16px_var(--color-tbh16b-acc)] focus-visible:shadow-[0_22px_44px_-16px_var(--color-tbh16b-acc)] focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-4 motion-reduce:transition-[box-shadow] motion-reduce:duration-200">
      <span class="inline-block translate-x-[calc(var(--dx,0)*8px)] translate-y-[calc(var(--dy,0)*8px)] transition-[translate] duration-[450ms] ease-[cubic-bezier(.34,1.56,.64,1)] motion-reduce:transition-none">Hire us</span>
    </button>
  </div>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh16a-edge: #d8b45c;
  --color-tbh16a-edge: oklch(0.78 0.13 90);
  --color-tbh16a-stage: #141210;
  --color-tbh16a-stage: oklch(0.18 0.01 80);
  --color-tbh16b-acc: #7a5ce0;
  --color-tbh16b-acc: oklch(0.6 0.19 285);
  --color-tbh16b-stage: #0c0a18;
  --color-tbh16b-stage: oklch(0.13 0.02 285);
  --font-tbh16-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Nothing stays CSS: the drift is a calc() inside a translate utility, and the two
   normalised inputs are written by the controller. */

.tbh-16-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-16a,
.tbh-16b {
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const setup = (wrapId, strength) => {
    const wrap = document.querySelector(wrapId); if (!wrap) return;
    const btn = wrap.querySelector('button'); if (!btn) return;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const label = btn.querySelector('span');
    const write = (dx, dy) => {
      [btn, label].forEach(el => el && (el.style.setProperty('--dx', dx), el.style.setProperty('--dy', dy)));
    };
    wrap.addEventListener('pointermove', e => {
      const r = wrap.getBoundingClientRect();
      write(((e.clientX - r.left) / r.width - .5).toFixed(3), ((e.clientY - r.top) / r.height - .5).toFixed(3));
    });
    wrap.addEventListener('pointerleave', () => write('0', '0'));
  };
  setup('#tbh-16a-wrap');
  setup('#tbh-16b-wrap');
})();
```
