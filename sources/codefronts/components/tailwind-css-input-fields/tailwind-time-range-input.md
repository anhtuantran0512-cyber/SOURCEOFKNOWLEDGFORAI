---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-time-range-input/"
title: "Tailwind Time Range Input"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "Two type=\"time\" fields grouped in a <fieldset> with an arrow between them: one visual unit, two independently submittable values."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Time Range Input
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-time-range-input/

Two type="time" fields grouped in a <fieldset> with an arrow between them: one visual unit, two independently submittable values. Quiet hours, shift windows, appointment ranges.
## HTML
```html
<div class="tif-18 grid min-h-svh w-full place-items-center bg-tif18-bg px-6 py-14 font-tif18-sans" aria-label="Time range input demo">
  <fieldset class="w-full max-w-80 rounded-xl border border-white/10 bg-tif18-field px-3.5 pb-3.5">
    <legend class="px-1.5 font-tif18-mono text-[10px] tracking-[0.12em] text-tif18-mut uppercase">Quiet hours</legend>
    <div class="flex items-end gap-3">
      <label class="grid flex-1 gap-1">
        <span class="text-[10px] tracking-[0.08em] text-tif18-mut uppercase">From</span>
        <input type="time" name="tif18-from" value="22:00" step="900"
          class="w-full scheme-dark rounded-lg border border-white/10 bg-tif18-deep px-2.5 py-2 font-tif18-mono text-[13px] font-semibold text-tif18-ink outline-none transition-colors duration-200 focus:border-tif18-acc">
      </label>
      <span class="pb-2 text-sm text-tif18-acc" aria-hidden="true">→</span>
      <label class="grid flex-1 gap-1">
        <span class="text-[10px] tracking-[0.08em] text-tif18-mut uppercase">To</span>
        <input type="time" name="tif18-to" value="07:00" step="900"
          class="w-full scheme-dark rounded-lg border border-white/10 bg-tif18-deep px-2.5 py-2 font-tif18-mono text-[13px] font-semibold text-tif18-ink outline-none transition-colors duration-200 focus:border-tif18-acc">
      </label>
    </div>
  </fieldset>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif18-bg: #12121a;
  --color-tif18-bg: oklch(0.19 0.015 285);
  --color-tif18-field: #1a1a22;
  --color-tif18-field: oklch(0.23 0.015 285);
  --color-tif18-deep: #0c0c12;
  --color-tif18-deep: oklch(0.16 0.012 285);
  --color-tif18-ink: #f0eeff;
  --color-tif18-ink: oklch(0.95 0.02 290);
  --color-tif18-mut: #b8b6d4;
  --color-tif18-mut: oklch(0.77 0.03 290);
  --color-tif18-acc: #a78bfa;
  --color-tif18-acc: oklch(0.74 0.15 295);
  --font-tif18-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tif18-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tif-18 {
  width: 100%;
}

.tif-18 ::selection {
  background: var(--color-tif18-acc);
  color: #12121a;
}
```
