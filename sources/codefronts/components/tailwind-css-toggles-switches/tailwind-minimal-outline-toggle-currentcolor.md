---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-minimal-outline-toggle-currentcolor/"
title: "Tailwind Minimal Outline Toggle Drawn in currentColor"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "A stroke-only switch drawn entirely in currentColor: hollow track, hollow thumb that fills solid when on."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Minimal Outline Toggle Drawn in currentColor
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-minimal-outline-toggle-currentcolor/

A stroke-only switch drawn entirely in currentColor: hollow track, hollow thumb that fills solid when on. Because it inherits colour from surrounding text, the identical markup works on a white card, a dark card and a brand banner with zero per-theme CSS.
## HTML
```html
<section class="ttg-24 w-full min-h-svh flex flex-col items-center justify-center gap-7 px-5 py-14 bg-ttg24-bg font-ttg24-sans" aria-label="Outline currentColor toggles">
  <div class="flex flex-wrap justify-center gap-4">
    <label class="flex items-center gap-5 px-6 py-4 rounded-2xl cursor-pointer text-[15px] font-semibold bg-white text-ttg24-lightink border border-ttg24-edge">
      <span>Autosave</span>
      <input type="checkbox" role="switch" checked aria-label="Autosave on light" class="appearance-none shrink-0 w-14 h-8 rounded-2xl border-2 border-current bg-transparent relative cursor-pointer before:content-[''] before:absolute before:top-[3px] before:left-[3px] before:w-5 before:h-5 before:rounded-full before:border-2 before:border-current before:bg-transparent before:transition-[transform,background-color] before:duration-300 before:ease-[cubic-bezier(0.3,1,0.35,1.05)] checked:before:translate-x-6 checked:before:bg-current focus-visible:outline-3 focus-visible:outline-current focus-visible:outline-offset-3 motion-reduce:before:transition-none">
    </label>
    <label class="flex items-center gap-5 px-6 py-4 rounded-2xl cursor-pointer text-[15px] font-semibold bg-ttg24-dark text-ttg24-darkink">
      <span>Autosave</span>
      <input type="checkbox" role="switch" checked aria-label="Autosave on dark" class="appearance-none shrink-0 w-14 h-8 rounded-2xl border-2 border-current bg-transparent relative cursor-pointer before:content-[''] before:absolute before:top-[3px] before:left-[3px] before:w-5 before:h-5 before:rounded-full before:border-2 before:border-current before:bg-transparent before:transition-[transform,background-color] before:duration-300 before:ease-[cubic-bezier(0.3,1,0.35,1.05)] checked:before:translate-x-6 checked:before:bg-current focus-visible:outline-3 focus-visible:outline-current focus-visible:outline-offset-3 motion-reduce:before:transition-none">
    </label>
    <label class="flex items-center gap-5 px-6 py-4 rounded-2xl cursor-pointer text-[15px] font-semibold bg-ttg24-brand text-white">
      <span>Autosave</span>
      <input type="checkbox" role="switch" aria-label="Autosave on brand" class="appearance-none shrink-0 w-14 h-8 rounded-2xl border-2 border-current bg-transparent relative cursor-pointer before:content-[''] before:absolute before:top-[3px] before:left-[3px] before:w-5 before:h-5 before:rounded-full before:border-2 before:border-current before:bg-transparent before:transition-[transform,background-color] before:duration-300 before:ease-[cubic-bezier(0.3,1,0.35,1.05)] checked:before:translate-x-6 checked:before:bg-current focus-visible:outline-3 focus-visible:outline-current focus-visible:outline-offset-3 motion-reduce:before:transition-none">
    </label>
  </div>
  <p class="text-[12px] tracking-[0.12em] uppercase text-ttg24-mute">One switch &middot; three themes &middot; zero theme CSS</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg24-bg: #f3f3f1;
  --color-ttg24-bg: oklch(0.96 0.004 110);
  --color-ttg24-edge: #e2e2de;
  --color-ttg24-edge: oklch(0.92 0.005 110);
  --color-ttg24-lightink: #23262c;
  --color-ttg24-lightink: oklch(0.27 0.012 265);
  --color-ttg24-dark: #1b1d22;
  --color-ttg24-dark: oklch(0.23 0.008 265);
  --color-ttg24-darkink: #eceef2;
  --color-ttg24-darkink: oklch(0.94 0.005 265);
  --color-ttg24-brand: #4b5fd6;
  --color-ttg24-brand: oklch(0.52 0.17 270);
  --color-ttg24-mute: #8e8e86;
  --color-ttg24-mute: oklch(0.63 0.01 110);
  --font-ttg24-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-24 {
  width: 100%;
  min-height: 100svh;
}

.ttg-24 input[type="checkbox"] {
  -webkit-appearance: none;
}
```
