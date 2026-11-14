---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-url-input-with-protocol/"
title: "Tailwind URL Input With Protocol"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "A URL field with a fixed https:// badge welded to its left edge: users type the host, you join the protocol on submit."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind URL Input With Protocol
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-url-input-with-protocol/

A URL field with a fixed https:// badge welded to its left edge: users type the host, you join the protocol on submit. The CSS original's pattern carries eight backslashes and matches nothing — fixed here.
## HTML
```html
<div class="tif-25 grid min-h-svh w-full place-items-center bg-tif25-bg px-6 py-14 font-tif25-sans" aria-label="URL input with protocol demo">
  <label class="grid w-full max-w-80 gap-1.5">
    <span class="font-tif25-mono text-[10px] tracking-[0.12em] text-tif25-mut uppercase">Website</span>
    <span class="flex items-stretch overflow-hidden rounded-[10px] border border-white/12 bg-tif25-field transition-colors duration-200 focus-within:border-tif25-acc">
      <span class="flex items-center border-r border-white/8 bg-tif25-acc/8 px-3 font-tif25-mono text-xs font-semibold text-tif25-acc select-none" aria-hidden="true">https://</span>
      <input type="text" name="tif25-host" inputmode="url" placeholder="codefronts.com" pattern="[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}.*"
        class="min-w-0 flex-1 border-0 bg-transparent px-3.5 py-3 text-sm font-medium text-tif25-ink outline-none placeholder:text-tif25-mut user-invalid:text-tif25-bad">
    </span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif25-bg: #12121a;
  --color-tif25-bg: oklch(0.19 0.015 285);
  --color-tif25-field: #1a1a22;
  --color-tif25-field: oklch(0.23 0.015 285);
  --color-tif25-ink: #f0eeff;
  --color-tif25-ink: oklch(0.95 0.02 290);
  --color-tif25-mut: #b8b6d4;
  --color-tif25-mut: oklch(0.77 0.03 290);
  --color-tif25-acc: #06b6d4;
  --color-tif25-acc: oklch(0.72 0.13 205);
  --color-tif25-bad: #ef4444;
  --color-tif25-bad: oklch(0.63 0.22 27);
  --font-tif25-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tif25-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tif-25 {
  width: 100%;
}

.tif-25 ::selection {
  background: var(--color-tif25-acc);
  color: #12121a;
}
```
