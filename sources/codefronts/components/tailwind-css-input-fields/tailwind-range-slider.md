---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-range-slider/"
title: "Tailwind Range Slider"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "A native type=\"range\" with a painted fill and a live value chip."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Range Slider
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-range-slider/

A native type="range" with a painted fill and a live value chip. The script writes one custom property; the gradient and the chip both read it — so dragging touches a single number, not a stylesheet.
## HTML
```html
<div class="tif-24 grid min-h-svh w-full place-items-center bg-tif24-bg px-6 py-14 font-tif24-mono" aria-label="Range slider demo">
  <div class="grid w-full max-w-70 gap-2">
    <label for="tif24-input" class="flex items-center justify-between text-[10px] tracking-[0.12em] text-tif24-mut uppercase">
      Volume
      <output for="tif24-input" data-tif24-out class="rounded-full bg-tif24-acc px-1.75 py-0.75 text-[11px] font-bold tracking-normal text-tif24-ink">50</output>
    </label>
    <input id="tif24-input" type="range" name="tif24-volume" min="0" max="100" value="50" data-tif24
      class="h-1.5 w-full cursor-pointer appearance-none rounded-full bg-[linear-gradient(90deg,var(--color-tif24-acc)_0%,var(--color-tif24-acc)_var(--tif24-fill,50%),oklch(1_0_0/0.08)_var(--tif24-fill,50%),oklch(1_0_0/0.08)_100%)] outline-none focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tif24-acc [&::-moz-range-thumb]:size-4.5 [&::-moz-range-thumb]:cursor-pointer [&::-moz-range-thumb]:rounded-full [&::-moz-range-thumb]:border-0 [&::-moz-range-thumb]:bg-white [&::-webkit-slider-thumb]:size-4.5 [&::-webkit-slider-thumb]:cursor-pointer [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:border-0 [&::-webkit-slider-thumb]:bg-white [&::-webkit-slider-thumb]:shadow-[0_2px_6px_oklch(0.62_0.2_288/0.5)] [&::-webkit-slider-thumb]:transition-transform [&::-webkit-slider-thumb]:duration-150 [&::-webkit-slider-thumb:hover]:scale-112">
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif24-bg: #12121a;
  --color-tif24-bg: oklch(0.19 0.015 285);
  --color-tif24-ink: #f0eeff;
  --color-tif24-ink: oklch(0.95 0.02 290);
  --color-tif24-mut: #b8b6d4;
  --color-tif24-mut: oklch(0.77 0.03 290);
  --color-tif24-acc: #7c6cff;
  --color-tif24-acc: oklch(0.62 0.2 288);
  --font-tif24-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tif-24 {
  width: 100%;
}

.tif-24 ::selection {
  background: var(--color-tif24-acc);
  color: #12121a;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tif-24').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    root.querySelectorAll('[data-tif24]').forEach(function (input) {
      var out = root.querySelector('[data-tif24-out]');
      function update() {
        var min = Number(input.min) || 0;
        var max = Number(input.max) || 100;
        var pct = ((Number(input.value) - min) / (max - min)) * 100;
        input.style.setProperty('--tif24-fill', pct + '%');
        if (out) out.value = input.value;
      }
      input.addEventListener('input', update);
      update();
    });
  });
})();
```
