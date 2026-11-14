---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-floating-label-input/"
title: "Tailwind Floating Label Input"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "The canonical floating label, and the demo that teaches the whole collection: peer on the input, peer-focus: and peer-[:not(:placeholder-shown)]: on the label."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Floating Label Input
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-floating-label-input/

The canonical floating label, and the demo that teaches the whole collection: peer on the input, peer-focus: and peer-[:not(:placeholder-shown)]: on the label. The CSS original writes two selector blocks that live nowhere near the label; here the label owns both of its lifted states.
## HTML
```html
<div class="tif-01 grid min-h-svh w-full place-items-center bg-tif01-bg px-6 py-14 font-tif01-sans" aria-label="Floating label input demo">
  <label class="relative block w-full max-w-70">
    <input type="email" name="tif01-email" autocomplete="email" placeholder=" " required
      class="peer w-full rounded-xl border border-white/12 bg-tif01-field px-3.5 pt-4.5 pb-2 text-sm text-tif01-ink outline-none transition-[border-color,background-color] duration-200 focus:border-tif01-acc2 focus:bg-tif01-field2">
    <span class="pointer-events-none absolute top-3.5 left-3.5 text-[13px] tracking-normal text-tif01-mut transition-[transform,font-size,color,letter-spacing] duration-200 peer-focus:-translate-y-2.5 peer-focus:text-[10px] peer-focus:tracking-[0.06em] peer-focus:text-tif01-acc peer-focus:uppercase peer-[:not(:placeholder-shown)]:-translate-y-2.5 peer-[:not(:placeholder-shown)]:text-[10px] peer-[:not(:placeholder-shown)]:tracking-[0.06em] peer-[:not(:placeholder-shown)]:text-tif01-acc peer-[:not(:placeholder-shown)]:uppercase motion-reduce:transition-none">Email address</span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif01-bg: #12121a;
  --color-tif01-bg: oklch(0.19 0.015 285);
  --color-tif01-field: #1a1a22;
  --color-tif01-field: oklch(0.23 0.015 285);
  --color-tif01-field2: #1f1f2a;
  --color-tif01-field2: oklch(0.26 0.018 285);
  --color-tif01-ink: #f0eeff;
  --color-tif01-ink: oklch(0.95 0.02 290);
  --color-tif01-mut: #b8b6d4;
  --color-tif01-mut: oklch(0.77 0.03 290);
  --color-tif01-acc: #a78bfa;
  --color-tif01-acc: oklch(0.74 0.15 295);
  --color-tif01-acc2: #7c6cff;
  --color-tif01-acc2: oklch(0.62 0.2 288);
  --font-tif01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Stage contract, stated in CSS as well as in the markup, so the demo is sized
   before the browser build compiles. */

.tif-01 {
  width: 100%;
}

.tif-01 ::selection {
  background: var(--color-tif01-acc);
  color: #12121a;
}
```
