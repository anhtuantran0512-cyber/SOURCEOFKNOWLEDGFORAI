---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-auto-grow-textarea/"
title: "Tailwind Auto-Grow Textarea"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "A textarea that grows with its content and shrinks back — one utility, field-sizing-content, replacing the ResizeObserver-and-hidden-mirror dance every form…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Auto-Grow Textarea
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-auto-grow-textarea/

A textarea that grows with its content and shrinks back — one utility, field-sizing-content, replacing the ResizeObserver-and-hidden-mirror dance every form library used to ship.
## HTML
```html
<div class="tif-22 grid min-h-svh w-full place-items-center bg-tif22-bg px-6 py-14 font-tif22-sans" aria-label="Auto-grow textarea demo">
  <label class="grid w-full max-w-80 gap-1.5">
    <span class="font-tif22-mono text-[10px] tracking-[0.12em] text-tif22-mut uppercase">Notes</span>
    <textarea name="tif22-notes" rows="2" placeholder="Type as much as you need…"
      class="field-sizing-content max-h-60 min-h-16 w-full resize-none overflow-y-auto rounded-[10px] border border-white/12 bg-tif22-field px-3.5 py-3 text-sm font-medium leading-relaxed text-tif22-ink outline-none transition-[border-color,background-color] duration-200 placeholder:text-tif22-mut focus:border-tif22-acc focus:bg-tif22-field2"></textarea>
    <span class="text-[11px] text-tif22-mut">Field grows as you type</span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif22-bg: #12121a;
  --color-tif22-bg: oklch(0.19 0.015 285);
  --color-tif22-field: #1a1a22;
  --color-tif22-field: oklch(0.23 0.015 285);
  --color-tif22-field2: #1f1f2a;
  --color-tif22-field2: oklch(0.26 0.018 285);
  --color-tif22-ink: #f0eeff;
  --color-tif22-ink: oklch(0.95 0.02 290);
  --color-tif22-mut: #b8b6d4;
  --color-tif22-mut: oklch(0.77 0.03 290);
  --color-tif22-acc: #a78bfa;
  --color-tif22-acc: oklch(0.74 0.15 295);
  --font-tif22-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tif22-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tif-22 {
  width: 100%;
}

.tif-22 ::selection {
  background: var(--color-tif22-acc);
  color: #12121a;
}
```
