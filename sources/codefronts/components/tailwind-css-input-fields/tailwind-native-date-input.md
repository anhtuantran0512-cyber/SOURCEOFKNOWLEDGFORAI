---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-native-date-input/"
title: "Tailwind Native Date Input"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "A styled type=\"date\" that keeps every native affordance — keyboard entry, locale, min/max, the OS calendar — while the closed field matches your form."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Native Date Input
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-native-date-input/

A styled type="date" that keeps every native affordance — keyboard entry, locale, min/max, the OS calendar — while the closed field matches your form. scheme-dark and accent-* are both real v4 utilities, which is most of the work.
## HTML
```html
<div class="tif-17 grid min-h-svh w-full place-items-center bg-tif17-bg px-6 py-14 font-tif17-sans" aria-label="Native date input demo">
  <label class="grid w-full max-w-70 gap-1.5">
    <span class="font-tif17-mono text-[10px] tracking-[0.12em] text-tif17-mut uppercase">Start date</span>
    <input type="date" name="tif17-start"
      class="w-full scheme-dark rounded-[10px] border border-white/12 bg-tif17-field px-3.5 py-3 text-sm font-medium text-tif17-ink accent-tif17-acc outline-none transition-[border-color,background-color] duration-200 focus:border-tif17-acc focus:bg-tif17-field2 [&::-webkit-calendar-picker-indicator]:cursor-pointer [&::-webkit-calendar-picker-indicator]:opacity-80 [&::-webkit-calendar-picker-indicator]:[filter:invert(0.7)_sepia(1)_saturate(5)_hue-rotate(150deg)] [&::-webkit-calendar-picker-indicator:hover]:opacity-100">
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif17-bg: #12121a;
  --color-tif17-bg: oklch(0.19 0.015 285);
  --color-tif17-field: #1a1a22;
  --color-tif17-field: oklch(0.23 0.015 285);
  --color-tif17-field2: #1f1f2a;
  --color-tif17-field2: oklch(0.26 0.018 285);
  --color-tif17-ink: #f0eeff;
  --color-tif17-ink: oklch(0.95 0.02 290);
  --color-tif17-mut: #b8b6d4;
  --color-tif17-mut: oklch(0.77 0.03 290);
  --color-tif17-acc: #06b6d4;
  --color-tif17-acc: oklch(0.72 0.13 205);
  --font-tif17-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tif17-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tif-17 {
  width: 100%;
}

.tif-17 ::selection {
  background: var(--color-tif17-acc);
  color: #12121a;
}
```
