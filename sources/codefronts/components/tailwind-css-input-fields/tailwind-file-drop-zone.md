---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-file-drop-zone/"
title: "Tailwind File Drop Zone"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "Drag-and-drop upload with a dashed boundary and zero JavaScript: a real file input stretched invisibly over the whole zone, so the browser handles the drop,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind File Drop Zone
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-file-drop-zone/

Drag-and-drop upload with a dashed boundary and zero JavaScript: a real file input stretched invisibly over the whole zone, so the browser handles the drop, the picker and keyboard focus. A 0 KB replacement for Dropzone.js in the common single-file case.
## HTML
```html
<div class="tif-15 grid min-h-svh w-full place-items-center bg-tif15-bg px-6 py-14 font-tif15-sans" aria-label="File drop zone demo">
  <label class="relative block w-full max-w-80 cursor-pointer rounded-xl border-[1.5px] border-dashed border-tif15-acc/50 bg-tif15-acc/5 px-4.5 py-5.5 text-center transition-[border-color,background-color] duration-200 hover:border-tif15-acc2 hover:bg-tif15-acc/10 focus-within:border-tif15-acc2 focus-within:bg-tif15-acc/12 focus-within:ring-3 focus-within:ring-tif15-acc2/18">
    <input type="file" name="tif15-upload" accept="image/*,.pdf" class="absolute inset-0 size-full cursor-pointer opacity-0">
    <span class="mx-auto mb-2 grid size-10 place-items-center rounded-[10px] bg-tif15-acc/18 text-tif15-acc3" aria-hidden="true">
      <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
    </span>
    <span class="block text-[13px] text-tif15-ink"><strong class="font-semibold text-tif15-acc3">Click to upload</strong> or drag &amp; drop
      <span class="mt-1 block text-[11px] text-tif15-mut">PNG, JPG, or PDF · max 10 MB</span>
    </span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif15-bg: #12121a;
  --color-tif15-bg: oklch(0.19 0.015 285);
  --color-tif15-ink: #c8c0ff;
  --color-tif15-ink: oklch(0.83 0.07 295);
  --color-tif15-mut: #b8b6d4;
  --color-tif15-mut: oklch(0.77 0.03 290);
  --color-tif15-acc: #6366f1;
  --color-tif15-acc: oklch(0.58 0.21 277);
  --color-tif15-acc2: #818cf8;
  --color-tif15-acc2: oklch(0.68 0.16 277);
  --color-tif15-acc3: #a5b4fc;
  --color-tif15-acc3: oklch(0.78 0.11 277);
  --font-tif15-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tif-15 {
  width: 100%;
}

.tif-15 ::selection {
  background: var(--color-tif15-acc2);
  color: #12121a;
}
```
