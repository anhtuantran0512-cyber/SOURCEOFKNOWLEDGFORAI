---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-multi-line-aligned-breadcrumb-css-subgrid/"
title: "Tailwind Multi-Line Aligned Breadcrumb Layout with CSS Subgrid"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "A trail whose icon, label and separator stay in perfect vertical alignment even when it wraps over several lines &mdash; each crumb inherits the parent's…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Multi-Line Aligned Breadcrumb Layout with CSS Subgrid
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-multi-line-aligned-breadcrumb-css-subgrid/

A trail whose icon, label and separator stay in perfect vertical alignment even when it wraps over several lines &mdash; each crumb inherits the parent's column tracks with subgrid. The port keeps both track declarations arbitrary, because a track list is not a design-scale value.
## HTML
```html
<section class="tbc-24 w-full min-h-svh grid place-items-center bg-tbc24-bg font-tbc24-sans px-7 py-7">
  <nav aria-label="Breadcrumb" class="max-w-[520px]">
    <ol class="grid justify-start items-center gap-x-2.25 gap-y-2.5 list-none m-0 p-0 [grid-template-columns:repeat(3,auto)]">
      <li class="grid items-center gap-2.25 col-span-3 [grid-template-columns:subgrid]"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-current [stroke-width:1.8] [stroke-linecap:round] [stroke-linejoin:round] text-tbc24-icon"><path d="M3 10.5 12 3l9 7.5M5.5 9.5V21h13V9.5"/></svg><a href="#" class="px-1 py-0.75 rounded-md text-sm font-semibold text-tbc24-link no-underline transition-colors duration-150 hover:text-tbc24-linkhover hover:underline hover:underline-offset-3 focus-visible:outline-2 focus-visible:outline-tbc24-acc focus-visible:outline-offset-2">Home</a><span aria-hidden="true" class="justify-self-center text-[15px] text-tbc24-sep">&rsaquo;</span></li>
      <li class="grid items-center gap-2.25 col-span-3 [grid-template-columns:subgrid]"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-current [stroke-width:1.8] [stroke-linecap:round] [stroke-linejoin:round] text-tbc24-icon"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18"/></svg><a href="#" class="px-1 py-0.75 rounded-md text-sm font-semibold text-tbc24-link no-underline transition-colors duration-150 hover:text-tbc24-linkhover hover:underline hover:underline-offset-3 focus-visible:outline-2 focus-visible:outline-tbc24-acc focus-visible:outline-offset-2">Documentation</a><span aria-hidden="true" class="justify-self-center text-[15px] text-tbc24-sep">&rsaquo;</span></li>
      <li class="grid items-center gap-2.25 col-span-3 [grid-template-columns:subgrid]"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-current [stroke-width:1.8] [stroke-linecap:round] [stroke-linejoin:round] text-tbc24-icon"><path d="M4 6h16M4 12h16M4 18h10"/></svg><a href="#" class="px-1 py-0.75 rounded-md text-sm font-semibold text-tbc24-link no-underline transition-colors duration-150 hover:text-tbc24-linkhover hover:underline hover:underline-offset-3 focus-visible:outline-2 focus-visible:outline-tbc24-acc focus-visible:outline-offset-2">CSS Layout Techniques</a><span aria-hidden="true" class="justify-self-center text-[15px] text-tbc24-sep">&rsaquo;</span></li>
      <li aria-current="page" class="grid items-center gap-2.25 col-span-2 [grid-template-columns:subgrid]"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-current [stroke-width:1.8] [stroke-linecap:round] [stroke-linejoin:round] text-tbc24-icon"><rect x="4" y="4" width="7" height="7" rx="1"/><rect x="13" y="4" width="7" height="7" rx="1"/><rect x="4" y="13" width="7" height="7" rx="1"/></svg><a href="#" aria-current="page" class="px-1 py-0.75 rounded-md text-sm font-bold text-tbc24-strong no-underline focus-visible:outline-2 focus-visible:outline-tbc24-acc focus-visible:outline-offset-2">Subgrid Alignment Guide</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc24-bg: #f4f7f8;
  --color-tbc24-bg: oklch(0.97 0.006 200);
  --color-tbc24-icon: #5f8894;
  --color-tbc24-icon: oklch(0.55 0.06 200);
  --color-tbc24-link: #3d6b80;
  --color-tbc24-link: oklch(0.45 0.08 210);
  --color-tbc24-linkhover: #2b5a75;
  --color-tbc24-linkhover: oklch(0.38 0.13 215);
  --color-tbc24-strong: #2b3339;
  --color-tbc24-strong: oklch(0.3 0.02 210);
  --color-tbc24-sep: #a9bcc2;
  --color-tbc24-sep: oklch(0.72 0.03 200);
  --color-tbc24-acc: #1b6f95;
  --color-tbc24-acc: oklch(0.5 0.15 215);
  --font-tbc24-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-24 {
  width: 100%;
  min-height: 100svh;
}
```
