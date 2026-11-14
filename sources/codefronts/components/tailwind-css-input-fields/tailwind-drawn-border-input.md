---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-drawn-border-input/"
title: "Tailwind Drawn Border Input"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "Four background layers, one per edge, animating from zero to full length on a staggered delay chain — the stroke draws around the field on focus."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Drawn Border Input
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-drawn-border-input/

Four background layers, one per edge, animating from zero to full length on a staggered delay chain — the stroke draws around the field on focus. No keyframes, no SVG, no @property: only background-size moves.
## HTML
```html
<div class="tif-06 grid min-h-svh w-full place-items-center bg-tif06-bg px-6 py-14 font-tif06-sans" aria-label="Drawn border input demo">
  <label class="grid w-full max-w-70 gap-1.5">
    <span class="text-[11px] tracking-[0.08em] text-tif06-mut uppercase">Project name</span>
    <input type="text" name="tif06-project" placeholder="My next big idea…" required
      class="w-full rounded-lg border border-tif06-edge bg-tif06-field bg-[linear-gradient(90deg,var(--color-tif06-acc),var(--color-tif06-acc)),linear-gradient(0deg,var(--color-tif06-acc),var(--color-tif06-acc)),linear-gradient(90deg,var(--color-tif06-acc),var(--color-tif06-acc)),linear-gradient(0deg,var(--color-tif06-acc),var(--color-tif06-acc))] bg-no-repeat px-3.5 py-2.5 text-sm text-tif06-ink outline-none transition-[background-size,border-color] duration-350 ease-linear [background-position:0_0,100%_0,100%_100%,0_100%] [background-size:0_2px,2px_0,0_2px,2px_0] placeholder:text-tif06-mut focus:border-transparent focus:[background-size:100%_2px,2px_100%,100%_2px,2px_100%] focus:[transition-delay:0s,0.35s,0.7s,1.05s] motion-reduce:focus:[transition-delay:0s]">
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif06-bg: #12121a;
  --color-tif06-bg: oklch(0.19 0.015 285);
  --color-tif06-field: #1a1a22;
  --color-tif06-field: oklch(0.23 0.015 285);
  --color-tif06-edge: #2a2a36;
  --color-tif06-edge: oklch(0.31 0.017 285);
  --color-tif06-ink: #f0eeff;
  --color-tif06-ink: oklch(0.95 0.02 290);
  --color-tif06-mut: #b8b6d4;
  --color-tif06-mut: oklch(0.77 0.03 290);
  --color-tif06-acc: #fbbf24;
  --color-tif06-acc: oklch(0.84 0.16 85);
  --font-tif06-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tif-06 {
  width: 100%;
}

.tif-06 ::selection {
  background: var(--color-tif06-acc);
  color: #12121a;
}
```
