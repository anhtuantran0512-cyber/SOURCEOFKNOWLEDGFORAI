---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-material-design-flat-breadcrumb-ink-ripple/"
title: "Tailwind Material Design Flat Breadcrumb Bar with Ink Ripple"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "Material's flat surface, type scale and state layers in utilities: an elevation-1 card, a masked chevron separator, a color-mix() hover layer, and an ink…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material Design Flat Breadcrumb Bar with Ink Ripple
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-material-design-flat-breadcrumb-ink-ripple/

Material's flat surface, type scale and state layers in utilities: an elevation-1 card, a masked chevron separator, a color-mix() hover layer, and an ink ripple that fires on :active from a radial-gradient pseudo-element &mdash; no ripple library, no JS.
## HTML
```html
<section class="tbc-08 w-full min-h-svh grid place-items-center bg-tbc08-bg font-tbc08-sans px-8 py-8">
  <nav aria-label="Breadcrumb">
    <ol class="inline-flex flex-wrap items-center list-none m-0 px-2 py-1.5 rounded-lg bg-white shadow-[0_1px_2px_oklch(0_0_0/0.12),0_1px_3px_oklch(0_0_0/0.08)]">
      <li class="flex items-center"><a href="#" class="relative overflow-hidden inline-flex items-center min-h-11 px-3.5 rounded-lg text-sm font-medium text-tbc08-primary no-underline transition-colors duration-200 hover:bg-[color-mix(in_oklab,var(--color-tbc08-primary)_8%,transparent)] focus-visible:outline-2 focus-visible:outline-tbc08-primary focus-visible:outline-offset-2 after:content-[''] after:absolute after:left-1/2 after:top-1/2 after:w-[160%] after:aspect-square after:-translate-x-1/2 after:-translate-y-1/2 after:rounded-full after:pointer-events-none after:scale-0 after:opacity-0 after:bg-[radial-gradient(circle,color-mix(in_oklab,var(--color-tbc08-primary)_40%,transparent),transparent_60%)] after:transition-[scale,opacity] after:duration-400 active:after:scale-100 active:after:opacity-100 active:after:duration-0 motion-reduce:after:hidden">Home</a></li>
      <li class="flex items-center before:content-[''] before:w-4.5 before:h-4.5 before:mx-0.5 before:bg-tbc08-mut before:[mask-image:var(--tbc08-chev)] before:[mask-size:contain] before:[mask-position:center] before:[mask-repeat:no-repeat]"><a href="#" class="relative overflow-hidden inline-flex items-center min-h-11 px-3.5 rounded-lg text-sm font-medium text-tbc08-primary no-underline transition-colors duration-200 hover:bg-[color-mix(in_oklab,var(--color-tbc08-primary)_8%,transparent)] focus-visible:outline-2 focus-visible:outline-tbc08-primary focus-visible:outline-offset-2 after:content-[''] after:absolute after:left-1/2 after:top-1/2 after:w-[160%] after:aspect-square after:-translate-x-1/2 after:-translate-y-1/2 after:rounded-full after:pointer-events-none after:scale-0 after:opacity-0 after:bg-[radial-gradient(circle,color-mix(in_oklab,var(--color-tbc08-primary)_40%,transparent),transparent_60%)] after:transition-[scale,opacity] after:duration-400 active:after:scale-100 active:after:opacity-100 active:after:duration-0 motion-reduce:after:hidden">Materials</a></li>
      <li class="flex items-center before:content-[''] before:w-4.5 before:h-4.5 before:mx-0.5 before:bg-tbc08-mut before:[mask-image:var(--tbc08-chev)] before:[mask-size:contain] before:[mask-position:center] before:[mask-repeat:no-repeat]"><a href="#" class="relative overflow-hidden inline-flex items-center min-h-11 px-3.5 rounded-lg text-sm font-medium text-tbc08-primary no-underline transition-colors duration-200 hover:bg-[color-mix(in_oklab,var(--color-tbc08-primary)_8%,transparent)] focus-visible:outline-2 focus-visible:outline-tbc08-primary focus-visible:outline-offset-2 after:content-[''] after:absolute after:left-1/2 after:top-1/2 after:w-[160%] after:aspect-square after:-translate-x-1/2 after:-translate-y-1/2 after:rounded-full after:pointer-events-none after:scale-0 after:opacity-0 after:bg-[radial-gradient(circle,color-mix(in_oklab,var(--color-tbc08-primary)_40%,transparent),transparent_60%)] after:transition-[scale,opacity] after:duration-400 active:after:scale-100 active:after:opacity-100 active:after:duration-0 motion-reduce:after:hidden">Components</a></li>
      <li class="flex items-center before:content-[''] before:w-4.5 before:h-4.5 before:mx-0.5 before:bg-tbc08-mut before:[mask-image:var(--tbc08-chev)] before:[mask-size:contain] before:[mask-position:center] before:[mask-repeat:no-repeat]"><a href="#" aria-current="page" class="inline-flex items-center min-h-11 px-3.5 rounded-lg text-sm font-medium text-tbc08-on no-underline cursor-default focus-visible:outline-2 focus-visible:outline-tbc08-primary focus-visible:outline-offset-2">Navigation</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc08-bg: #f6f6f9;
  --color-tbc08-bg: oklch(0.97 0.004 265);
  --color-tbc08-primary: #4d5fc0;
  --color-tbc08-primary: oklch(0.5 0.15 265);
  --color-tbc08-on: #52555c;
  --color-tbc08-on: oklch(0.35 0.01 265);
  --color-tbc08-mut: #8f9199;
  --color-tbc08-mut: oklch(0.6 0.01 265);
  --font-tbc08-sans: 'Roboto', system-ui, sans-serif;
}
/* Mask data-URI as a plain custom property: not a design-scale value, so it should
   not mint utilities. */

.tbc-08 {
  width: 100%;
  min-height: 100svh;
  --tbc08-chev: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M9 6l6 6-6 6' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
}
/* Safari < 15.4 mask prefix. */

.tbc-08 li::before {
  -webkit-mask: var(--tbc08-chev) center/contain no-repeat;
}
```
