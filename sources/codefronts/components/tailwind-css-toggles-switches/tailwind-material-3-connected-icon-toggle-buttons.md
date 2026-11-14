---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-material-3-connected-icon-toggle-buttons/"
title: "Tailwind Material 3 Connected Icon Toggle Buttons"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "M3's other switch: a connected group of icon toggle buttons where each segment is independently on or off, the ends are fully rounded, and a selected segment…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material 3 Connected Icon Toggle Buttons
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-material-3-connected-icon-toggle-buttons/

M3's other switch: a connected group of icon toggle buttons where each segment is independently on or off, the ends are fully rounded, and a selected segment fills with the secondary container tone and grows a check. Multi-select, not a radio group.
## HTML
```html
<section class="ttg-35 w-full min-h-svh flex flex-col items-center justify-center gap-6 px-5 py-14 bg-ttg35-bg font-ttg35-sans" aria-label="Material 3 icon toggle buttons">
  <div class="flex flex-col items-center gap-4 px-7 py-6 rounded-[24px] bg-ttg35-surface border border-ttg35-edge">
    <p class="text-[12px] tracking-[0.08em] uppercase text-ttg35-mute">Text style</p>
    <div class="flex" role="group" aria-label="Text style">
      <span class="relative">
        <input type="checkbox" id="ttg-35-b" checked aria-label="Bold" class="peer sr-only">
        <label for="ttg-35-b" class="flex items-center gap-1 min-h-11 px-5 rounded-l-full border border-ttg35-outline cursor-pointer text-[14px] font-medium text-ttg35-ink transition-[background-color,color] duration-200 hover:bg-ttg35-layer/10 peer-checked:bg-ttg35-fill peer-checked:text-ttg35-onfill peer-focus-visible:outline-3 peer-focus-visible:outline-ttg35-primary peer-focus-visible:outline-offset-2 peer-checked:[&_.ttg35-check]:w-4.5 peer-checked:[&_.ttg35-check]:opacity-100">
          <svg viewBox="0 0 18 18" class="ttg35-check w-0 h-4.5 opacity-0 overflow-hidden transition-[width,opacity] duration-200" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 9.5l4 4L15 5"/></svg>
          <b class="font-bold">B</b>
        </label>
      </span>
      <span class="relative -ml-px">
        <input type="checkbox" id="ttg-35-i" aria-label="Italic" class="peer sr-only">
        <label for="ttg-35-i" class="flex items-center gap-1 min-h-11 px-5 border border-ttg35-outline cursor-pointer text-[14px] font-medium text-ttg35-ink transition-[background-color,color] duration-200 hover:bg-ttg35-layer/10 peer-checked:bg-ttg35-fill peer-checked:text-ttg35-onfill peer-focus-visible:outline-3 peer-focus-visible:outline-ttg35-primary peer-focus-visible:outline-offset-2 peer-checked:[&_.ttg35-check]:w-4.5 peer-checked:[&_.ttg35-check]:opacity-100">
          <svg viewBox="0 0 18 18" class="ttg35-check w-0 h-4.5 opacity-0 overflow-hidden transition-[width,opacity] duration-200" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 9.5l4 4L15 5"/></svg>
          <i class="font-serif">I</i>
        </label>
      </span>
      <span class="relative -ml-px">
        <input type="checkbox" id="ttg-35-u" checked aria-label="Underline" class="peer sr-only">
        <label for="ttg-35-u" class="flex items-center gap-1 min-h-11 px-5 rounded-r-full border border-ttg35-outline cursor-pointer text-[14px] font-medium text-ttg35-ink transition-[background-color,color] duration-200 hover:bg-ttg35-layer/10 peer-checked:bg-ttg35-fill peer-checked:text-ttg35-onfill peer-focus-visible:outline-3 peer-focus-visible:outline-ttg35-primary peer-focus-visible:outline-offset-2 peer-checked:[&_.ttg35-check]:w-4.5 peer-checked:[&_.ttg35-check]:opacity-100">
          <svg viewBox="0 0 18 18" class="ttg35-check w-0 h-4.5 opacity-0 overflow-hidden transition-[width,opacity] duration-200" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 9.5l4 4L15 5"/></svg>
          <span class="underline underline-offset-4">U</span>
        </label>
      </span>
    </div>
    <p class="text-[12.5px] text-ttg35-mute">Each segment toggles on its own &mdash; checkboxes, not radios</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg35-bg: #fdf7ff;
  --color-ttg35-bg: oklch(0.98 0.012 310);
  --color-ttg35-surface: #ffffff;
  --color-ttg35-surface: oklch(1 0 0);
  --color-ttg35-edge: #e7e0ec;
  --color-ttg35-edge: oklch(0.91 0.012 310);
  --color-ttg35-outline: #78727f;
  --color-ttg35-outline: oklch(0.55 0.02 300);
  --color-ttg35-primary: #6750a4;
  --color-ttg35-primary: oklch(0.47 0.13 296);
  --color-ttg35-fill: #e5ddf8;
  --color-ttg35-fill: oklch(0.9 0.05 296);
  --color-ttg35-onfill: #251a47;
  --color-ttg35-onfill: oklch(0.28 0.08 296);
  --color-ttg35-layer: #6750a4;
  --color-ttg35-layer: oklch(0.47 0.13 296);
  --color-ttg35-ink: #1d1b20;
  --color-ttg35-ink: oklch(0.23 0.008 300);
  --color-ttg35-mute: #6b6572;
  --color-ttg35-mute: oklch(0.51 0.018 300);
  --font-ttg35-sans: Roboto, 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-35 {
  width: 100%;
  min-height: 100svh;
}
```
