---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-tag-chip-input/"
title: "Tailwind Tag Chip Input"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "Type a tag, press Enter or comma, get a chip."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Tag Chip Input
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-tag-chip-input/

Type a tag, press Enter or comma, get a chip. Backspace on an empty input removes the last one. The chip's whole appearance is a single class string in the script — the one place a port has to put utilities in JavaScript, and worth seeing.
## HTML
```html
<div class="tif-12 grid min-h-svh w-full place-items-center bg-tif12-bg px-6 py-14 font-tif12-sans" aria-label="Tag chip input demo">
  <label class="grid w-full max-w-70 gap-1.5 text-[11px] text-tif12-mut">
    <span class="font-semibold">Tags</span>
    <span class="flex flex-wrap items-center gap-1.5 rounded-lg border border-white/10 bg-tif12-field px-2.5 py-2 transition-[border-color,box-shadow] duration-200 focus-within:border-tif12-acc focus-within:ring-3 focus-within:ring-tif12-acc/15" data-tif-tags>
      <span class="contents" data-tif-list></span>
      <input type="text" placeholder="Add a tag…" aria-label="Tags"
        class="min-w-20 flex-1 border-0 bg-transparent py-0.5 text-sm text-tif12-ink outline-none placeholder:text-tif12-mut">
      <input type="hidden" name="tif12-tags" data-tif-value>
    </span>
    <span class="text-[10.5px] text-tif12-mut">Press <kbd class="inline-block rounded border border-white/8 bg-tif12-key px-1 font-tif12-mono text-[10px]">Enter</kbd> or <kbd class="inline-block rounded border border-white/8 bg-tif12-key px-1 font-tif12-mono text-[10px]">,</kbd> to add</span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif12-bg: #12121a;
  --color-tif12-bg: oklch(0.19 0.015 285);
  --color-tif12-field: #1a1a22;
  --color-tif12-field: oklch(0.23 0.015 285);
  --color-tif12-key: #2a2a36;
  --color-tif12-key: oklch(0.31 0.017 285);
  --color-tif12-ink: #f0eeff;
  --color-tif12-ink: oklch(0.95 0.02 290);
  --color-tif12-mut: #b8b6d4;
  --color-tif12-mut: oklch(0.77 0.03 290);
  --color-tif12-acc: #fb923c;
  --color-tif12-acc: oklch(0.75 0.16 55);
  --color-tif12-acc2: #fdba74;
  --color-tif12-acc2: oklch(0.82 0.11 60);
  --font-tif12-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tif12-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tif-12 {
  width: 100%;
}

.tif-12 ::selection {
  background: var(--color-tif12-acc);
  color: #12121a;
}
```

## JavaScript
```js
(function () {
  var CHIP = 'inline-flex items-center gap-1.5 rounded-full border border-tif12-acc/35 ' +
    'bg-tif12-acc/12 px-2 py-0.5 text-xs font-medium text-tif12-acc2';
  var X = 'grid size-5 cursor-pointer place-items-center rounded-full border-0 bg-transparent ' +
    'p-0 text-xs leading-none text-inherit opacity-70 hover:opacity-100 ' +
    'focus-visible:outline-2 focus-visible:outline-offset-1 focus-visible:outline-tif12-acc';

  document.querySelectorAll('.tif-12').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var wrap = root.querySelector('[data-tif-tags]');
    var list = root.querySelector('[data-tif-list]');
    var store = root.querySelector('[data-tif-value]');
    var input = wrap && wrap.querySelector('input[type="text"]');
    if (!wrap || !list || !input) return;

    function sync() {
      var values = Array.prototype.map.call(list.children, function (c) { return c.dataset.value; });
      if (store) store.value = values.join(',');
      wrap.dispatchEvent(new CustomEvent('tags:change', { detail: values, bubbles: true }));
    }
    function addChip(value) {
      value = (value || '').trim();
      if (!value) return;
      var chip = document.createElement('span');
      chip.className = CHIP;
      chip.dataset.value = value;
      var text = document.createElement('span');
      text.textContent = value;
      var x = document.createElement('button');
      x.type = 'button';
      x.className = X;
      x.setAttribute('aria-label', 'Remove tag ' + value);
      x.textContent = '\u00d7';
      x.addEventListener('click', function () { chip.remove(); sync(); });
      chip.append(text, x);
      list.appendChild(chip);
      sync();
    }
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ',') {
        e.preventDefault();
        addChip(input.value);
        input.value = '';
      } else if (e.key === 'Backspace' && !input.value && list.lastElementChild) {
        list.lastElementChild.remove();
        sync();
      }
    });
    ['design', 'css'].forEach(addChip);
  });
})();
```
