---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-inline-edit-field/"
title: "Tailwind Inline Edit Field"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "Click-to-edit text that swaps a display span for an input, saves on Enter or blur and cancels on Escape."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Inline Edit Field
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-inline-edit-field/

Click-to-edit text that swaps a display span for an input, saves on Enter or blur and cancels on Escape. The editing state is a data-editing attribute on the wrapper, so the border, background and pencil all read it as a variant.
## HTML
```html
<div class="tif-23 grid min-h-svh w-full place-items-center bg-tif23-bg px-6 py-14 font-tif23-sans" aria-label="Inline edit field demo">
  <div class="grid w-full max-w-70 gap-1.5">
    <span class="font-tif23-mono text-[10px] tracking-[0.12em] text-tif23-mut uppercase" id="tif23-cap">Project name</span>
    <span data-tif23 data-value="Aurora Dashboard"
      class="group flex cursor-text items-center gap-1.5 rounded-lg border border-dashed border-transparent bg-transparent px-3 py-2 transition-[background-color,border-color] duration-150 hover:border-tif23-acc/20 hover:bg-tif23-acc/6 focus-within:border-tif23-acc/40 data-editing:border-solid data-editing:border-tif23-acc data-editing:bg-tif23-field">
      <span data-tif23-display tabindex="0" role="button" aria-labelledby="tif23-cap" aria-label="Edit project name"
        class="min-w-0 flex-1 text-sm font-semibold text-tif23-ink outline-none">Aurora Dashboard</span>
      <input data-tif23-input type="text" value="Aurora Dashboard" hidden aria-label="Project name"
        class="min-w-0 flex-1 border-0 bg-transparent p-0 text-sm font-semibold text-tif23-ink outline-none">
      <span aria-hidden="true" class="text-xs text-tif23-dim opacity-0 transition-opacity duration-150 group-hover:opacity-100 group-focus-within:opacity-100 group-data-editing:hidden">✎</span>
    </span>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif23-bg: #12121a;
  --color-tif23-bg: oklch(0.19 0.015 285);
  --color-tif23-field: #1a1a22;
  --color-tif23-field: oklch(0.23 0.015 285);
  --color-tif23-ink: #f0eeff;
  --color-tif23-ink: oklch(0.95 0.02 290);
  --color-tif23-mut: #b8b6d4;
  --color-tif23-mut: oklch(0.77 0.03 290);
  --color-tif23-dim: #7a7899;
  --color-tif23-dim: oklch(0.6 0.04 292);
  --color-tif23-acc: #7c6cff;
  --color-tif23-acc: oklch(0.62 0.2 288);
  --font-tif23-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tif23-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tif-23 {
  width: 100%;
}

.tif-23 ::selection {
  background: var(--color-tif23-acc);
  color: #12121a;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tif-23').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    root.querySelectorAll('[data-tif23]').forEach(function (wrap) {
      var display = wrap.querySelector('[data-tif23-display]');
      var input = wrap.querySelector('[data-tif23-input]');
      if (!display || !input) return;

      function enter() {
        wrap.dataset.editing = '';
        display.hidden = true;
        input.hidden = false;
        input.value = wrap.dataset.value || display.textContent;
        input.focus();
        input.select();
      }
      function exit() {
        delete wrap.dataset.editing;
        input.hidden = true;
        display.hidden = false;
      }
      function commit() {
        var v = input.value.trim();
        if (v) {
          display.textContent = v;
          wrap.dataset.value = v;
          wrap.dispatchEvent(new CustomEvent('inline-edit:change', { detail: v, bubbles: true }));
        }
        exit();
      }
      function cancel() {
        input.value = wrap.dataset.value || display.textContent;
        exit();
        display.focus();
      }

      display.addEventListener('click', enter);
      display.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); enter(); }
      });
      input.addEventListener('blur', commit);
      input.addEventListener('keydown', function (e) {
        if (e.key === 'Enter') { e.preventDefault(); commit(); }
        if (e.key === 'Escape') { e.preventDefault(); cancel(); }
      });
    });
  });
})();
```
