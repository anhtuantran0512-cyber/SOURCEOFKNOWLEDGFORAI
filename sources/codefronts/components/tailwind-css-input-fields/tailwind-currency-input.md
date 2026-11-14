---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-currency-input/"
title: "Tailwind Currency Input"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "Right-aligned money with an inline $ that lights up on focus."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Currency Input
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-currency-input/

Right-aligned money with an inline $ that lights up on focus. tabular-nums keeps digit widths locked as the user types — the detail that makes a column of amounts stop shimmering.
## HTML
```html
<div class="tif-16 grid min-h-svh w-full place-items-center bg-tif16-bg px-6 py-14 font-tif16-sans" aria-label="Currency input demo">
  <label class="grid w-full max-w-70 gap-1.5">
    <span class="font-tif16-mono text-[10px] tracking-[0.12em] text-tif16-mut uppercase">Amount</span>
    <span class="group flex items-center gap-1.5 rounded-[10px] border border-white/12 bg-tif16-field px-3.5 transition-[border-color,background-color] duration-200 focus-within:border-tif16-acc focus-within:bg-tif16-field2">
      <span class="text-sm font-semibold text-tif16-mut transition-colors duration-200 group-focus-within:text-tif16-acc" aria-hidden="true">$</span>
      <input type="text" name="tif16-amount" inputmode="decimal" pattern="[0-9.,]*" placeholder="0.00"
        class="min-w-0 flex-1 border-0 bg-transparent py-3 text-right text-sm font-semibold tabular-nums text-tif16-ink outline-none placeholder:text-tif16-mut">
      <span class="font-tif16-mono text-[10px] tracking-[0.06em] text-tif16-mut">USD</span>
    </span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif16-bg: #12121a;
  --color-tif16-bg: oklch(0.19 0.015 285);
  --color-tif16-field: #1a1a22;
  --color-tif16-field: oklch(0.23 0.015 285);
  --color-tif16-field2: #1f1f2a;
  --color-tif16-field2: oklch(0.26 0.018 285);
  --color-tif16-ink: #f0eeff;
  --color-tif16-ink: oklch(0.95 0.02 290);
  --color-tif16-mut: #b8b6d4;
  --color-tif16-mut: oklch(0.77 0.03 290);
  --color-tif16-acc: #f5a84a;
  --color-tif16-acc: oklch(0.79 0.13 70);
  --font-tif16-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tif16-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tif-16 {
  width: 100%;
}

.tif-16 ::selection {
  background: var(--color-tif16-acc);
  color: #12121a;
}
```
