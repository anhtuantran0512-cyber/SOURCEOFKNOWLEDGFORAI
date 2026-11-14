---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-micro-interaction-animated-hover-breadcrumbs/"
title: "Tailwind Micro-Interaction Animated Hover Breadcrumbs"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "Three tiny motions stacked on one hover: the crumb lifts 2px, a soft shadow fades in beneath it, and &mdash; the detail that sells it &mdash; the following…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Micro-Interaction Animated Hover Breadcrumbs
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-micro-interaction-animated-hover-breadcrumbs/

Three tiny motions stacked on one hover: the crumb lifts 2px, a soft shadow fades in beneath it, and &mdash; the detail that sells it &mdash; the following separator nudges forward. has-hover: turns the CSS version's relational selector into a variant on the crumb that owns the chevron.
## HTML
```html
<section class="tbc-39 w-full min-h-svh grid place-items-center bg-tbc39-bg font-tbc39-sans px-7 py-9">
  <nav aria-label="Breadcrumb">
    <ol class="flex flex-wrap items-center list-none m-0 p-0">
      <li class="flex items-center"><a href="#" class="inline-flex items-center min-h-9 px-3 rounded-[9px] text-[13.5px] font-semibold text-tbc39-ink no-underline bg-transparent transition-[translate,box-shadow,color,background-color] duration-200 ease-[cubic-bezier(0.34,1.56,0.64,1)] hover:-translate-y-0.5 hover:text-tbc39-acc hover:bg-white hover:shadow-[0_6px_16px_oklch(0.2_0.06_285/0.14)] focus-visible:outline-none focus-visible:-translate-y-0.5 focus-visible:text-tbc39-acc focus-visible:bg-white focus-visible:shadow-[0_6px_16px_oklch(0.2_0.06_285/0.14),0_0_0_2px_var(--color-tbc39-acc)] motion-reduce:transition-[color,background-color] motion-reduce:hover:translate-y-0 motion-reduce:focus-visible:translate-y-0">Home</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-tbc39-sep before:transition-[translate,color] before:duration-200 before:ease-[cubic-bezier(0.34,1.56,0.64,1)] has-hover:before:translate-x-[3px] has-hover:before:text-tbc39-acc motion-reduce:before:transition-colors motion-reduce:has-hover:before:translate-x-0"><a href="#" class="inline-flex items-center min-h-9 px-3 rounded-[9px] text-[13.5px] font-semibold text-tbc39-ink no-underline bg-transparent transition-[translate,box-shadow,color,background-color] duration-200 ease-[cubic-bezier(0.34,1.56,0.64,1)] hover:-translate-y-0.5 hover:text-tbc39-acc hover:bg-white hover:shadow-[0_6px_16px_oklch(0.2_0.06_285/0.14)] focus-visible:outline-none focus-visible:-translate-y-0.5 focus-visible:text-tbc39-acc focus-visible:bg-white focus-visible:shadow-[0_6px_16px_oklch(0.2_0.06_285/0.14),0_0_0_2px_var(--color-tbc39-acc)] motion-reduce:transition-[color,background-color] motion-reduce:hover:translate-y-0 motion-reduce:focus-visible:translate-y-0">Products</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-tbc39-sep before:transition-[translate,color] before:duration-200 before:ease-[cubic-bezier(0.34,1.56,0.64,1)] has-hover:before:translate-x-[3px] has-hover:before:text-tbc39-acc motion-reduce:before:transition-colors motion-reduce:has-hover:before:translate-x-0"><a href="#" class="inline-flex items-center min-h-9 px-3 rounded-[9px] text-[13.5px] font-semibold text-tbc39-ink no-underline bg-transparent transition-[translate,box-shadow,color,background-color] duration-200 ease-[cubic-bezier(0.34,1.56,0.64,1)] hover:-translate-y-0.5 hover:text-tbc39-acc hover:bg-white hover:shadow-[0_6px_16px_oklch(0.2_0.06_285/0.14)] focus-visible:outline-none focus-visible:-translate-y-0.5 focus-visible:text-tbc39-acc focus-visible:bg-white focus-visible:shadow-[0_6px_16px_oklch(0.2_0.06_285/0.14),0_0_0_2px_var(--color-tbc39-acc)] motion-reduce:transition-[color,background-color] motion-reduce:hover:translate-y-0 motion-reduce:focus-visible:translate-y-0">Hardware</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-tbc39-sep before:transition-[translate,color] before:duration-200 before:ease-[cubic-bezier(0.34,1.56,0.64,1)] has-hover:before:translate-x-[3px] has-hover:before:text-tbc39-acc motion-reduce:before:transition-colors motion-reduce:has-hover:before:translate-x-0"><a href="#" aria-current="page" class="inline-flex items-center min-h-9 px-3 rounded-[9px] text-[13.5px] font-bold text-tbc39-strong no-underline cursor-default focus-visible:outline-2 focus-visible:outline-tbc39-acc focus-visible:outline-offset-2">Keyboards</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc39-bg: #fbfafd;
  --color-tbc39-bg: oklch(0.98 0.004 285);
  --color-tbc39-ink: #6a6577;
  --color-tbc39-ink: oklch(0.45 0.04 285);
  --color-tbc39-strong: #3b3745;
  --color-tbc39-strong: oklch(0.3 0.02 285);
  --color-tbc39-sep: #aaa5b8;
  --color-tbc39-sep: oklch(0.7 0.02 285);
  --color-tbc39-acc: #6c5ac9;
  --color-tbc39-acc: oklch(0.52 0.15 285);
  --font-tbc39-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-39 {
  width: 100%;
  min-height: 100svh;
}
```
