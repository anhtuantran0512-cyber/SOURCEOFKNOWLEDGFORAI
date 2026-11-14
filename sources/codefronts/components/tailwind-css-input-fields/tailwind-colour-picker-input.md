---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-colour-picker-input/"
title: "Tailwind Colour Picker Input"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "A native colour swatch welded to a hex field — and, unlike the CSS original, the two actually talk to each other."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Colour Picker Input
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-colour-picker-input/

A native colour swatch welded to a hex field — and, unlike the CSS original, the two actually talk to each other. Twelve lines of JavaScript keep swatch and text in sync both ways, which is the entire point of showing them together.
## HTML
```html
<div class="tif-19 grid min-h-svh w-full place-items-center bg-tif19-bg px-6 py-14 font-tif19-mono" aria-label="Colour picker input demo">
  <label class="grid w-full max-w-70 gap-1.5">
    <span class="text-[10px] tracking-[0.12em] text-tif19-mut uppercase">Brand colour</span>
    <span class="flex items-stretch overflow-hidden rounded-[10px] border border-white/12 bg-tif19-field transition-colors duration-200 focus-within:border-tif19-acc">
      <input type="color" value="#7C6CFF" aria-label="Pick colour" data-tif19-swatch
        class="size-11 shrink-0 cursor-pointer border-0 border-r border-white/10 bg-transparent p-1.5 outline-none [&::-webkit-color-swatch]:rounded-md [&::-webkit-color-swatch]:border-0 [&::-webkit-color-swatch-wrapper]:p-0">
      <input type="text" value="#7C6CFF" aria-label="Hex value" name="tif19-hex" pattern="^#[0-9A-Fa-f]{6}$" spellcheck="false" data-tif19-text
        class="min-w-0 flex-1 border-0 bg-transparent px-3.5 text-[13px] font-semibold tracking-[0.04em] text-tif19-ink uppercase outline-none user-invalid:text-tif19-bad">
    </span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif19-bg: #12121a;
  --color-tif19-bg: oklch(0.19 0.015 285);
  --color-tif19-field: #1a1a22;
  --color-tif19-field: oklch(0.23 0.015 285);
  --color-tif19-ink: #f0eeff;
  --color-tif19-ink: oklch(0.95 0.02 290);
  --color-tif19-mut: #b8b6d4;
  --color-tif19-mut: oklch(0.77 0.03 290);
  --color-tif19-acc: #7c6cff;
  --color-tif19-acc: oklch(0.62 0.2 288);
  --color-tif19-bad: #ef4444;
  --color-tif19-bad: oklch(0.63 0.22 27);
  --font-tif19-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tif-19 {
  width: 100%;
}

.tif-19 ::selection {
  background: var(--color-tif19-acc);
  color: #12121a;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tif-19').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var swatch = root.querySelector('[data-tif19-swatch]');
    var text = root.querySelector('[data-tif19-text]');
    if (!swatch || !text) return;
    swatch.addEventListener('input', function () {
      text.value = swatch.value.toUpperCase();
    });
    text.addEventListener('input', function () {
      if (/^#[0-9a-f]{6}$/i.test(text.value.trim())) swatch.value = text.value.trim();
    });
  });
})();
```
