---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-truncated-ellipsis-compact-mobile-breadcrumb/"
title: "Tailwind Truncated Ellipsis Compact Mobile Breadcrumb"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "A single-line trail engineered for tight widths: ancestors cap at 12ch and truncate with an ellipsis, the current page never shrinks, and the bar never wraps…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Truncated Ellipsis Compact Mobile Breadcrumb
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-truncated-ellipsis-compact-mobile-breadcrumb/

A single-line trail engineered for tight widths: ancestors cap at 12ch and truncate with an ellipsis, the current page never shrinks, and the bar never wraps or overflows. Priority is expressed as shrink / shrink-0 rather than as media queries.
## HTML
```html
<section class="tbc-33 w-full min-h-svh grid place-items-center bg-tbc33-bg font-tbc33-sans px-6 py-7">
  <nav aria-label="Breadcrumb">
    <ol class="flex flex-nowrap items-center list-none mx-auto my-0 px-3 py-2.5 max-w-[340px] overflow-hidden rounded-[10px] bg-white border border-tbc33-edge">
      <li class="flex items-center min-w-0"><a href="#" title="Home" class="shrink-0 px-0.75 py-0.5 rounded-[5px] text-[13px] font-medium text-tbc33-link no-underline whitespace-nowrap hover:text-tbc33-linkhover hover:underline hover:underline-offset-2 focus-visible:outline-2 focus-visible:outline-tbc33-acc focus-visible:outline-offset-1">Home</a></li>
      <li class="flex items-center min-w-0 before:content-['\203A'] before:flex-none before:mx-1.5 before:text-tbc33-sep"><a href="#" title="Electronics &amp; Accessories" class="shrink min-w-0 max-w-[12ch] truncate px-0.75 py-0.5 rounded-[5px] text-[13px] font-medium text-tbc33-link no-underline hover:text-tbc33-linkhover hover:underline hover:underline-offset-2 focus-visible:outline-2 focus-visible:outline-tbc33-acc focus-visible:outline-offset-1">Electronics &amp; Accessories</a></li>
      <li class="flex items-center min-w-0 before:content-['\203A'] before:flex-none before:mx-1.5 before:text-tbc33-sep"><a href="#" title="Headphones and Earbuds" class="shrink min-w-0 max-w-[12ch] truncate px-0.75 py-0.5 rounded-[5px] text-[13px] font-medium text-tbc33-link no-underline hover:text-tbc33-linkhover hover:underline hover:underline-offset-2 focus-visible:outline-2 focus-visible:outline-tbc33-acc focus-visible:outline-offset-1">Headphones and Earbuds</a></li>
      <li class="flex items-center min-w-0 before:content-['\203A'] before:flex-none before:mx-1.5 before:text-tbc33-sep"><a href="#" aria-current="page" title="Wireless Over-Ear Noise-Cancelling" class="shrink-0 max-w-none px-0.75 py-0.5 rounded-[5px] text-[13px] font-semibold text-tbc33-strong no-underline whitespace-nowrap focus-visible:outline-2 focus-visible:outline-tbc33-acc focus-visible:outline-offset-1">Wireless Over-Ear Noise-Cancelling</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc33-bg: #fafbfd;
  --color-tbc33-bg: oklch(0.98 0.004 240);
  --color-tbc33-edge: #e1e4ea;
  --color-tbc33-edge: oklch(0.9 0.008 240);
  --color-tbc33-link: #5b6a8c;
  --color-tbc33-link: oklch(0.48 0.07 250);
  --color-tbc33-linkhover: #3f5182;
  --color-tbc33-linkhover: oklch(0.4 0.13 250);
  --color-tbc33-strong: #353a41;
  --color-tbc33-strong: oklch(0.3 0.02 240);
  --color-tbc33-sep: #a7acb6;
  --color-tbc33-sep: oklch(0.7 0.02 240);
  --color-tbc33-acc: #3f59b8;
  --color-tbc33-acc: oklch(0.48 0.14 250);
  --font-tbc33-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-33 {
  width: 100%;
  min-height: 100svh;
}
```
