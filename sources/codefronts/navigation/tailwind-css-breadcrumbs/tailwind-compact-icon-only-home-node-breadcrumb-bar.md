---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-compact-icon-only-home-node-breadcrumb-bar/"
title: "Tailwind Compact Icon-Only Home Node Breadcrumb Bar"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "The space-saving convention: the first crumb is a house icon, with the word \"Home\" kept for screen readers by Tailwind's built-in sr-only."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Compact Icon-Only Home Node Breadcrumb Bar
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-compact-icon-only-home-node-breadcrumb-bar/

The space-saving convention: the first crumb is a house icon, with the word "Home" kept for screen readers by Tailwind's built-in sr-only. The port's whole argument is that the visually-hidden pattern &mdash; the thing developers most often get wrong by hand &mdash; is one correct utility here.
## HTML
```html
<section class="tbc-14 w-full min-h-svh grid place-items-center bg-tbc14-bg font-tbc14-sans px-8 py-8">
  <nav aria-label="Breadcrumb">
    <ol class="flex flex-wrap items-center list-none m-0 p-0">
      <li class="flex items-center"><a href="#" class="inline-flex items-center justify-center min-w-11 min-h-11 px-2.5 rounded-[9px] text-[13.5px] font-semibold text-tbc14-link no-underline transition-colors duration-200 hover:text-tbc14-acc hover:bg-[color-mix(in_oklab,var(--color-tbc14-acc)_12%,transparent)] focus-visible:outline-2 focus-visible:outline-tbc14-acc focus-visible:outline-offset-2 motion-reduce:transition-none"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.75 h-4.75 fill-none stroke-current [stroke-width:1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M3 10.5 12 3l9 7.5M5.5 9.5V21h13V9.5"/></svg><span class="sr-only">Home</span></a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-tbc14-sep"><a href="#" class="inline-flex items-center justify-center min-w-11 min-h-11 px-2.5 rounded-[9px] text-[13.5px] font-semibold text-tbc14-link no-underline transition-colors duration-200 hover:text-tbc14-acc hover:bg-[color-mix(in_oklab,var(--color-tbc14-acc)_12%,transparent)] focus-visible:outline-2 focus-visible:outline-tbc14-acc focus-visible:outline-offset-2 motion-reduce:transition-none">Help Center</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-tbc14-sep"><a href="#" class="inline-flex items-center justify-center min-w-11 min-h-11 px-2.5 rounded-[9px] text-[13.5px] font-semibold text-tbc14-link no-underline transition-colors duration-200 hover:text-tbc14-acc hover:bg-[color-mix(in_oklab,var(--color-tbc14-acc)_12%,transparent)] focus-visible:outline-2 focus-visible:outline-tbc14-acc focus-visible:outline-offset-2 motion-reduce:transition-none">Billing</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-tbc14-sep"><a href="#" aria-current="page" class="inline-flex items-center justify-center min-w-11 min-h-11 px-2.5 rounded-[9px] text-[13.5px] font-bold text-tbc14-strong no-underline focus-visible:outline-2 focus-visible:outline-tbc14-acc focus-visible:outline-offset-2">Refunds</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc14-bg: #fafbfd;
  --color-tbc14-bg: oklch(0.98 0.004 235);
  --color-tbc14-link: #5c6b7d;
  --color-tbc14-link: oklch(0.46 0.05 235);
  --color-tbc14-strong: #343a41;
  --color-tbc14-strong: oklch(0.3 0.02 235);
  --color-tbc14-sep: #a9b0ba;
  --color-tbc14-sep: oklch(0.72 0.02 235);
  --color-tbc14-acc: #2f79b5;
  --color-tbc14-acc: oklch(0.55 0.14 235);
  --font-tbc14-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-14 {
  width: 100%;
  min-height: 100svh;
}
```
