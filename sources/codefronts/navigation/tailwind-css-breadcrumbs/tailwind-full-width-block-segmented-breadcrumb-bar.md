---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-full-width-block-segmented-breadcrumb-bar/"
title: "Tailwind Full-Width Block-Style Segmented Breadcrumb Bar"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "An edge-to-edge banner where each hierarchy step is a full-height coloured block, segments meeting flush with a bevel hairline and a tonal ramp encoding depth."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Full-Width Block-Style Segmented Breadcrumb Bar
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-full-width-block-segmented-breadcrumb-bar/

An edge-to-edge banner where each hierarchy step is a full-height coloured block, segments meeting flush with a bevel hairline and a tonal ramp encoding depth. The current step right-fills and takes the accent. On narrow screens the row becomes a stack &mdash; one max-sm: run instead of a media query.
## HTML
```html
<section class="tbc-11 w-full min-h-svh grid place-items-center bg-tbc11-bg font-tbc11-sans">
  <nav aria-label="Breadcrumb" class="w-full">
    <ol class="flex w-full list-none m-0 p-0 max-sm:flex-col">
      <li class="flex"><a href="#" class="flex items-center w-full h-13 px-5.5 text-[13px] font-bold tracking-[0.02em] uppercase text-white no-underline bg-tbc11-step1 shadow-[inset_-1px_0_0_oklch(1_0_0/0.18),inset_1px_0_0_oklch(0_0_0/0.12)] transition-[filter] duration-200 hover:brightness-110 focus-visible:outline-none focus-visible:shadow-[inset_0_0_0_3px_white] max-sm:shadow-[inset_0_-1px_0_oklch(0_0_0/0.15)] motion-reduce:transition-none">Home</a></li>
      <li class="flex"><a href="#" class="flex items-center w-full h-13 px-5.5 text-[13px] font-bold tracking-[0.02em] uppercase text-white no-underline bg-tbc11-step2 shadow-[inset_-1px_0_0_oklch(1_0_0/0.18),inset_1px_0_0_oklch(0_0_0/0.12)] transition-[filter] duration-200 hover:brightness-110 focus-visible:outline-none focus-visible:shadow-[inset_0_0_0_3px_white] max-sm:shadow-[inset_0_-1px_0_oklch(0_0_0/0.15)] motion-reduce:transition-none">Region</a></li>
      <li class="flex"><a href="#" class="flex items-center w-full h-13 px-5.5 text-[13px] font-bold tracking-[0.02em] uppercase text-white no-underline bg-tbc11-step3 shadow-[inset_-1px_0_0_oklch(1_0_0/0.18),inset_1px_0_0_oklch(0_0_0/0.12)] transition-[filter] duration-200 hover:brightness-110 focus-visible:outline-none focus-visible:shadow-[inset_0_0_0_3px_white] max-sm:shadow-[inset_0_-1px_0_oklch(0_0_0/0.15)] motion-reduce:transition-none">Country</a></li>
      <li class="flex flex-1 max-sm:flex-none"><a href="#" aria-current="page" class="flex items-center w-full h-13 px-5.5 text-[13px] font-bold tracking-[0.02em] uppercase text-white no-underline bg-tbc11-current shadow-[inset_1px_0_0_oklch(0_0_0/0.12)] focus-visible:outline-none focus-visible:shadow-[inset_0_0_0_3px_white] max-sm:shadow-none">City Guide</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc11-bg: #f2f3f6;
  --color-tbc11-bg: oklch(0.96 0.005 250);
  --color-tbc11-step1: #414a63;
  --color-tbc11-step1: oklch(0.42 0.05 250);
  --color-tbc11-step2: #4a5677;
  --color-tbc11-step2: oklch(0.47 0.07 250);
  --color-tbc11-step3: #52628c;
  --color-tbc11-step3: oklch(0.52 0.09 250);
  --color-tbc11-current: #4f6bd6;
  --color-tbc11-current: oklch(0.55 0.17 255);
  --font-tbc11-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-11 {
  width: 100%;
  min-height: 100svh;
}
```
