---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-range-slider/"
title: "Tailwind Liquid Glass Range Slider"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "A heavy glass lens sliding across a numeric scale, magnifying the value beneath it."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Range Slider
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-range-slider/

A heavy glass lens sliding across a numeric scale, magnifying the value beneath it. The native range input stays on top and fully transparent so keyboard, pointer and screen-reader behaviour are untouched; every glass layer under it is decoration positioned from a single --v custom property.
## HTML
```html
<section id="lgt-13-root" class="lgt-13 grid w-full min-h-svh place-items-center px-6 py-15 font-lgt13-sans [background:radial-gradient(circle_at_30%_30%,#1c3050,#0d1424)]" aria-label="Tailwind liquid glass range slider">
  <div id="lgt-13-wrap" style="--v:40" class="group relative h-30 w-[min(440px,90vw)]">
    <div aria-hidden="true" class="pointer-events-none absolute inset-x-0 top-8.5 flex justify-between text-[26px] font-extrabold text-white/14">
      <span>0</span><span>25</span><span>50</span><span>75</span><span>100</span>
    </div>

    <div aria-hidden="true" class="pointer-events-none absolute inset-x-0 top-13.5 h-2.5 overflow-hidden rounded-full border border-white/20 bg-white/10 backdrop-blur-[6px] shadow-[inset_0_2px_6px_rgba(0,0,0,.5)]">
      <div class="absolute inset-y-0 left-0 [width:calc(var(--v)*1%)] bg-linear-to-r from-lgt13-accent/60 to-lgt13-accent shadow-[0_0_16px_var(--color-lgt13-accent)]"></div>
    </div>

    <div aria-hidden="true" class="pointer-events-none absolute top-[59px] grid size-14 -translate-x-1/2 -translate-y-1/2 place-items-center rounded-full border border-white/60 bg-white/14 backdrop-blur-[3px] backdrop-saturate-160 backdrop-brightness-110 shadow-[inset_0_2px_6px_rgba(255,255,255,.5),inset_0_-6px_12px_rgba(0,0,0,.35),0_10px_24px_-8px_rgba(0,0,0,.6)] [left:calc(var(--v)*1%)] transition-shadow duration-200 group-has-[:focus-visible]:shadow-[0_0_0_3px_#fff,inset_0_2px_6px_rgba(255,255,255,.5)] motion-reduce:transition-none">
      <span id="lgt-13-mag" class="scale-115 text-2xl font-black text-white [text-shadow:0_1px_4px_rgba(0,0,0,.5)]">40</span>
    </div>

    <input id="lgt-13-input" type="range" min="0" max="100" value="40" aria-label="Quality" class="absolute -left-2 top-11 h-10 w-[calc(100%+16px)] cursor-grab appearance-none bg-transparent opacity-0 active:cursor-grabbing">
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-lgt13-accent: #4fd1e0;
  --color-lgt13-accent: oklch(0.7 0.17 200);
  --font-lgt13-sans: 'Manrope', system-ui, sans-serif;
}
/* The invisible input still needs a large hit area on both engines. */

.lgt-13 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 56px;
  height: 56px;
}

.lgt-13 input[type="range"]::-moz-range-thumb {
  width: 56px;
  height: 56px;
  border: none;
  background: transparent;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('#lgt-13-root');
  const input = root.querySelector('#lgt-13-input');
  const wrap = root.querySelector('#lgt-13-wrap');
  const mag = root.querySelector('#lgt-13-mag');
  const sync = () => { wrap.style.setProperty('--v', input.value); mag.textContent = input.value; };
  input.addEventListener('input', sync);
  sync();
})();
```
