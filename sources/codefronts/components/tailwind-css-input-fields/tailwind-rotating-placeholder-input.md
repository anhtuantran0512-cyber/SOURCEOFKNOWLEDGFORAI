---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-rotating-placeholder-input/"
title: "Tailwind Rotating Placeholder Input"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "The native placeholder attribute itself cycles through four sample queries every 2.5 seconds, fading between them. The script swaps one attribute and flips…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Rotating Placeholder Input
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-rotating-placeholder-input/

The native placeholder attribute itself cycles through four sample queries every 2.5 seconds, fading between them. The script swaps one attribute and flips one data attribute; every visual is a utility, and rotation pauses the instant the user focuses.
## HTML
```html
<div class="tif-11 grid min-h-svh w-full place-items-center bg-tif11-bg px-6 py-14 font-tif11-sans" aria-label="Rotating placeholder input demo">
  <label class="grid w-full max-w-70 gap-1.5">
    <span class="font-tif11-mono text-[10px] tracking-[0.12em] text-tif11-mut uppercase">Search</span>
    <input type="search" name="tif11-q" inputmode="search" placeholder="Search products…" aria-label="Search"
      data-tif-rotate='["Search products…","Search docs…","Search people…","Search settings…"]'
      class="w-full rounded-[10px] border border-white/12 bg-tif11-field px-3.5 py-3 text-sm font-medium text-tif11-ink outline-none transition-[border-color,background-color] duration-250 placeholder:text-tif11-mut placeholder:transition-opacity placeholder:duration-250 focus:border-tif11-acc focus:bg-tif11-field2 data-fading:placeholder:opacity-0 motion-reduce:placeholder:transition-none">
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif11-bg: #12121a;
  --color-tif11-bg: oklch(0.19 0.015 285);
  --color-tif11-field: #1a1a22;
  --color-tif11-field: oklch(0.23 0.015 285);
  --color-tif11-field2: #1f1f2a;
  --color-tif11-field2: oklch(0.26 0.018 285);
  --color-tif11-ink: #f0eeff;
  --color-tif11-ink: oklch(0.95 0.02 290);
  --color-tif11-mut: #b8b6d4;
  --color-tif11-mut: oklch(0.77 0.03 290);
  --color-tif11-acc: #c084fc;
  --color-tif11-acc: oklch(0.75 0.17 305);
  --font-tif11-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tif11-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tif-11 {
  width: 100%;
}

.tif-11 ::selection {
  background: var(--color-tif11-acc);
  color: #12121a;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tif-11').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    root.querySelectorAll('[data-tif-rotate]').forEach(function (input) {
      var phrases = [];
      try { phrases = JSON.parse(input.getAttribute('data-tif-rotate') || '[]'); } catch (e) {}
      if (!phrases.length) return;
      var i = 0, paused = false;
      var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
      setInterval(function () {
        if (paused || document.activeElement === input || input.value) return;
        input.dataset.fading = '';
        setTimeout(function () {
          i = (i + 1) % phrases.length;
          input.setAttribute('placeholder', phrases[i]);
          delete input.dataset.fading;
        }, reduce.matches ? 0 : 250);
      }, 2500);
      input.addEventListener('focus', function () { paused = true; });
      input.addEventListener('blur', function () { paused = !!input.value; });
    });
  });
})();
```
