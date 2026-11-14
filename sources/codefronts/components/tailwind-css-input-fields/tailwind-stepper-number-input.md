---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-stepper-number-input/"
title: "Tailwind Stepper Number Input"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "A quantity control with custom −/+ buttons over a real type=\"number\", so keyboard arrows, validation and form serialisation survive."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stepper Number Input
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-stepper-number-input/

A quantity control with custom −/+ buttons over a real type="number", so keyboard arrows, validation and form serialisation survive. The CSS original's script reads the wrong dataset key and never steps at all — fixed here.
## HTML
```html
<div class="tif-14 grid min-h-svh w-full place-items-center bg-tif14-bg px-6 py-14 font-tif14-sans" aria-label="Stepper number input demo">
  <label class="grid w-full max-w-55 gap-1.5 text-[11px] text-tif14-mut">
    <span class="font-semibold">Quantity</span>
    <span class="grid grid-cols-[44px_1fr_44px] overflow-hidden rounded-lg border border-white/10 bg-tif14-field transition-colors duration-200 focus-within:border-tif14-acc">
      <button type="button" data-tif14-step="-1" aria-label="Decrease quantity"
        class="cursor-pointer border-0 bg-tif14-acc/6 text-lg font-bold text-tif14-acc2 transition-colors duration-150 hover:bg-tif14-acc/18 hover:text-white active:bg-tif14-acc/28 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tif14-acc">−</button>
      <input type="number" name="tif14-qty" min="0" max="99" value="1" aria-label="Quantity" data-tif14-input
        class="border-0 bg-transparent py-2.5 text-center text-base font-semibold text-tif14-ink outline-none [appearance:textfield] [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:appearance-none">
      <button type="button" data-tif14-step="1" aria-label="Increase quantity"
        class="cursor-pointer border-0 bg-tif14-acc/6 text-lg font-bold text-tif14-acc2 transition-colors duration-150 hover:bg-tif14-acc/18 hover:text-white active:bg-tif14-acc/28 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tif14-acc">+</button>
    </span>
    <span class="sr-only" aria-live="polite" data-tif14-live>Quantity 1</span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif14-bg: #12121a;
  --color-tif14-bg: oklch(0.19 0.015 285);
  --color-tif14-field: #1a1a22;
  --color-tif14-field: oklch(0.23 0.015 285);
  --color-tif14-ink: #f0eeff;
  --color-tif14-ink: oklch(0.95 0.02 290);
  --color-tif14-mut: #b8b6d4;
  --color-tif14-mut: oklch(0.77 0.03 290);
  --color-tif14-acc: #14b8a6;
  --color-tif14-acc: oklch(0.7 0.13 180);
  --color-tif14-acc2: #5eead4;
  --color-tif14-acc2: oklch(0.85 0.12 178);
  --font-tif14-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tif-14 {
  width: 100%;
}

.tif-14 ::selection {
  background: var(--color-tif14-acc);
  color: #12121a;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tif-14').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var input = root.querySelector('[data-tif14-input]');
    var live = root.querySelector('[data-tif14-live]');
    if (!input) return;
    root.querySelectorAll('[data-tif14-step]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var dir = Number(btn.dataset.tif14Step) || 0;
        var min = input.min !== '' ? Number(input.min) : -Infinity;
        var max = input.max !== '' ? Number(input.max) : Infinity;
        var val = (Number(input.value) || 0) + dir;
        input.value = String(Math.min(max, Math.max(min, val)));
        if (live) live.textContent = 'Quantity ' + input.value;
        input.dispatchEvent(new Event('change', { bubbles: true }));
      });
    });
  });
})();
```
