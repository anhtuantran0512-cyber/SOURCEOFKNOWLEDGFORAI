---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-ecommerce-filter-facet-breadcrumb-removable-chips/"
title: "Tailwind E-Commerce Filter & Facet Breadcrumb with Removable Chips"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "The Shopify/Magento faceted trail: Home &rsaquo; Women &rsaquo; Shoes plus removable filter chips, each with its own remove button."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind E-Commerce Filter & Facet Breadcrumb with Removable Chips
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-ecommerce-filter-facet-breadcrumb-removable-chips/

The Shopify/Magento faceted trail: Home &rsaquo; Women &rsaquo; Shoes plus removable filter chips, each with its own remove button. The port's interesting move is has-hover: &mdash; the chip tints when its remove button is hovered, which the CSS version needed :has(button:hover) for and Tailwind expresses as a variant on the chip itself.
## HTML
```html
<section class="tbc-04 w-full min-h-svh grid place-items-center bg-tbc04-bg font-tbc04-sans px-5 py-9">
  <div class="w-[min(720px,100%)] flex flex-wrap items-center justify-center gap-x-5 gap-y-3">
    <nav aria-label="Breadcrumb">
      <ol class="flex flex-wrap items-center list-none m-0 p-0">
        <li class="flex items-center"><a href="#" class="flex items-center min-h-9 px-1.5 rounded-md text-[13.5px] font-semibold text-tbc04-link no-underline transition-colors duration-150 hover:text-tbc04-acc focus-visible:outline-2 focus-visible:outline-tbc04-acc focus-visible:outline-offset-2">Home</a></li>
        <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-tbc04-sep"><a href="#" class="flex items-center min-h-9 px-1.5 rounded-md text-[13.5px] font-semibold text-tbc04-link no-underline transition-colors duration-150 hover:text-tbc04-acc focus-visible:outline-2 focus-visible:outline-tbc04-acc focus-visible:outline-offset-2">Women</a></li>
        <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-tbc04-sep"><a href="#" aria-current="page" class="flex items-center min-h-9 px-1.5 rounded-md text-[13.5px] font-bold text-tbc04-strong no-underline focus-visible:outline-2 focus-visible:outline-tbc04-acc focus-visible:outline-offset-2">Shoes</a></li>
      </ol>
    </nav>
    <ul aria-label="Active filters" class="flex flex-wrap items-center gap-2 list-none m-0 p-0">
      <li class="inline-flex items-center gap-1 pl-3.5 pr-1 rounded-full text-[12.5px] font-semibold text-tbc04-chipink bg-tbc04-chip border border-tbc04-chipedge transition-colors duration-200 has-hover:bg-[color-mix(in_oklab,var(--color-tbc04-danger)_15%,var(--color-tbc04-chip))] has-hover:text-tbc04-danger has-focus-visible:bg-[color-mix(in_oklab,var(--color-tbc04-danger)_15%,var(--color-tbc04-chip))] has-focus-visible:text-tbc04-danger motion-reduce:transition-none">Size 8<button type="button" aria-label="Remove filter: Size 8" class="grid place-items-center min-w-11 min-h-11 border-0 bg-transparent cursor-pointer before:content-[''] before:w-5 before:h-5 before:rounded-full before:bg-tbc04-xdot before:[mask-image:var(--tbc04-x)] before:[mask-size:13px] before:[mask-position:center] before:[mask-repeat:no-repeat] before:transition-[scale,background-color] before:duration-150 hover:before:scale-115 hover:before:bg-tbc04-danger focus-visible:outline-2 focus-visible:outline-tbc04-danger focus-visible:outline-offset-1 focus-visible:rounded-full motion-reduce:before:transition-none"></button></li>
      <li class="inline-flex items-center gap-1 pl-3.5 pr-1 rounded-full text-[12.5px] font-semibold text-tbc04-chipink bg-tbc04-chip border border-tbc04-chipedge transition-colors duration-200 has-hover:bg-[color-mix(in_oklab,var(--color-tbc04-danger)_15%,var(--color-tbc04-chip))] has-hover:text-tbc04-danger has-focus-visible:bg-[color-mix(in_oklab,var(--color-tbc04-danger)_15%,var(--color-tbc04-chip))] has-focus-visible:text-tbc04-danger motion-reduce:transition-none">Under $120<button type="button" aria-label="Remove filter: Under $120" class="grid place-items-center min-w-11 min-h-11 border-0 bg-transparent cursor-pointer before:content-[''] before:w-5 before:h-5 before:rounded-full before:bg-tbc04-xdot before:[mask-image:var(--tbc04-x)] before:[mask-size:13px] before:[mask-position:center] before:[mask-repeat:no-repeat] before:transition-[scale,background-color] before:duration-150 hover:before:scale-115 hover:before:bg-tbc04-danger focus-visible:outline-2 focus-visible:outline-tbc04-danger focus-visible:outline-offset-1 focus-visible:rounded-full motion-reduce:before:transition-none"></button></li>
      <li class="inline-flex items-center gap-1 pl-3.5 pr-1 rounded-full text-[12.5px] font-semibold text-tbc04-chipink bg-tbc04-chip border border-tbc04-chipedge transition-colors duration-200 has-hover:bg-[color-mix(in_oklab,var(--color-tbc04-danger)_15%,var(--color-tbc04-chip))] has-hover:text-tbc04-danger has-focus-visible:bg-[color-mix(in_oklab,var(--color-tbc04-danger)_15%,var(--color-tbc04-chip))] has-focus-visible:text-tbc04-danger motion-reduce:transition-none">In stock<button type="button" aria-label="Remove filter: In stock" class="grid place-items-center min-w-11 min-h-11 border-0 bg-transparent cursor-pointer before:content-[''] before:w-5 before:h-5 before:rounded-full before:bg-tbc04-xdot before:[mask-image:var(--tbc04-x)] before:[mask-size:13px] before:[mask-position:center] before:[mask-repeat:no-repeat] before:transition-[scale,background-color] before:duration-150 hover:before:scale-115 hover:before:bg-tbc04-danger focus-visible:outline-2 focus-visible:outline-tbc04-danger focus-visible:outline-offset-1 focus-visible:rounded-full motion-reduce:before:transition-none"></button></li>
      <li class="inline-flex items-center gap-1 pl-3.5 pr-1 rounded-full text-[12.5px] font-semibold text-tbc04-chipink bg-tbc04-chip border border-tbc04-chipedge transition-colors duration-200 has-hover:bg-[color-mix(in_oklab,var(--color-tbc04-danger)_15%,var(--color-tbc04-chip))] has-hover:text-tbc04-danger has-focus-visible:bg-[color-mix(in_oklab,var(--color-tbc04-danger)_15%,var(--color-tbc04-chip))] has-focus-visible:text-tbc04-danger motion-reduce:transition-none">Colour: Tan<button type="button" aria-label="Remove filter: Colour Tan" class="grid place-items-center min-w-11 min-h-11 border-0 bg-transparent cursor-pointer before:content-[''] before:w-5 before:h-5 before:rounded-full before:bg-tbc04-xdot before:[mask-image:var(--tbc04-x)] before:[mask-size:13px] before:[mask-position:center] before:[mask-repeat:no-repeat] before:transition-[scale,background-color] before:duration-150 hover:before:scale-115 hover:before:bg-tbc04-danger focus-visible:outline-2 focus-visible:outline-tbc04-danger focus-visible:outline-offset-1 focus-visible:rounded-full motion-reduce:before:transition-none"></button></li>
    </ul>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc04-bg: #fcfcfa;
  --color-tbc04-bg: oklch(0.98 0.004 90);
  --color-tbc04-link: #7c6a52;
  --color-tbc04-link: oklch(0.52 0.04 70);
  --color-tbc04-strong: #3d3428;
  --color-tbc04-strong: oklch(0.32 0.02 70);
  --color-tbc04-sep: #b3ada0;
  --color-tbc04-sep: oklch(0.74 0.02 90);
  --color-tbc04-acc: #b4653a;
  --color-tbc04-acc: oklch(0.55 0.14 45);
  --color-tbc04-chip: #eee2cf;
  --color-tbc04-chip: oklch(0.92 0.03 70);
  --color-tbc04-chipedge: #ded0b8;
  --color-tbc04-chipedge: oklch(0.86 0.04 65);
  --color-tbc04-chipink: #6b5a44;
  --color-tbc04-chipink: oklch(0.46 0.05 55);
  --color-tbc04-xdot: #8b7256;
  --color-tbc04-xdot: oklch(0.55 0.05 55);
  --color-tbc04-danger: #b83a2b;
  --color-tbc04-danger: oklch(0.55 0.19 25);
  --font-tbc04-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Not an @theme entry on purpose: a mask data-URI is not a design-scale value and has no
   business minting utilities. It lives as a plain custom property the mask utilities read. */

.tbc-04 {
  width: 100%;
  min-height: 100svh;
  --tbc04-x: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M6 6l12 12M18 6L6 18' stroke='black' stroke-width='2.5' stroke-linecap='round'/%3E%3C/svg%3E");
}
/* Safari < 15.4 mask prefix, which Tailwind's arbitrary mask utilities do not emit. */

.tbc-04 button::before {
  -webkit-mask: var(--tbc04-x) center/13px no-repeat;
}
```
