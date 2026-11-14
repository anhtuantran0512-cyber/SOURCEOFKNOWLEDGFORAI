---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-circular-icon-numbered-step-breadcrumbs/"
title: "Tailwind Circular Icon & Numbered Step Breadcrumbs"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "Stepper meets breadcrumb: every crumb leads with a circular badge holding an icon or an auto-incremented number, joined by short connector rules."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Circular Icon & Numbered Step Breadcrumbs
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-circular-icon-numbered-step-breadcrumbs/

Stepper meets breadcrumb: every crumb leads with a circular badge holding an icon or an auto-incremented number, joined by short connector rules. The counter stays in CSS (it must), while the badge states, the connectors and the responsive icon-only mode are all utilities.
## HTML
```html
<section class="tbc-37 w-full min-h-svh grid place-items-center bg-tbc37-bg font-tbc37-sans px-8 py-8">
  <nav aria-label="Breadcrumb">
    <ol class="flex flex-wrap items-center gap-4.5 list-none m-0 p-0 [counter-reset:tbc37step]">
      <li class="group relative flex items-center before:content-[''] before:absolute before:-left-4.5 before:w-4.5 before:border-t-2 before:border-tbc37-line first:before:hidden"><a href="#" class="inline-flex items-center gap-2.25 text-[13.5px] font-semibold text-tbc37-link no-underline transition-colors duration-150 hover:text-tbc37-linkhover focus-visible:outline-2 focus-visible:outline-tbc37-acc focus-visible:outline-offset-3 focus-visible:rounded-md max-sm:gap-0 max-sm:text-[0]"><span aria-hidden="true" class="grid place-items-center flex-none w-7 h-7 rounded-full text-xs font-bold bg-tbc37-tint text-tbc37-acc group-aria-[current=page]:bg-tbc37-acc group-aria-[current=page]:text-white"><svg viewBox="0 0 24 24" class="w-3.75 h-3.75 fill-none stroke-current [stroke-width:1.9] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M3 10.5 12 3l9 7.5M5.5 9.5V21h13V9.5"/></svg></span>Home</a></li>
      <li class="group relative flex items-center before:content-[''] before:absolute before:-left-4.5 before:w-4.5 before:border-t-2 before:border-tbc37-line"><a href="#" class="inline-flex items-center gap-2.25 text-[13.5px] font-semibold text-tbc37-link no-underline transition-colors duration-150 hover:text-tbc37-linkhover focus-visible:outline-2 focus-visible:outline-tbc37-acc focus-visible:outline-offset-3 focus-visible:rounded-md max-sm:gap-0 max-sm:text-[0]"><span aria-hidden="true" class="tbc37-num grid place-items-center flex-none w-7 h-7 rounded-full text-xs font-bold bg-tbc37-tint text-tbc37-acc [counter-increment:tbc37step] group-aria-[current=page]:bg-tbc37-acc group-aria-[current=page]:text-white"></span>Account</a></li>
      <li class="group relative flex items-center before:content-[''] before:absolute before:-left-4.5 before:w-4.5 before:border-t-2 before:border-tbc37-line"><a href="#" class="inline-flex items-center gap-2.25 text-[13.5px] font-semibold text-tbc37-link no-underline transition-colors duration-150 hover:text-tbc37-linkhover focus-visible:outline-2 focus-visible:outline-tbc37-acc focus-visible:outline-offset-3 focus-visible:rounded-md max-sm:gap-0 max-sm:text-[0]"><span aria-hidden="true" class="tbc37-num grid place-items-center flex-none w-7 h-7 rounded-full text-xs font-bold bg-tbc37-tint text-tbc37-acc [counter-increment:tbc37step] group-aria-[current=page]:bg-tbc37-acc group-aria-[current=page]:text-white"></span>Profile</a></li>
      <li aria-current="page" class="group relative flex items-center before:content-[''] before:absolute before:-left-4.5 before:w-4.5 before:border-t-2 before:border-tbc37-line"><a href="#" aria-current="page" class="inline-flex items-center gap-2.25 text-[13.5px] font-bold text-tbc37-strong no-underline focus-visible:outline-2 focus-visible:outline-tbc37-acc focus-visible:outline-offset-3 focus-visible:rounded-md max-sm:gap-0 max-sm:text-[0]"><span aria-hidden="true" class="tbc37-num grid place-items-center flex-none w-7 h-7 rounded-full text-xs font-bold bg-tbc37-acc text-white [counter-increment:tbc37step]"></span>Preferences</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc37-bg: #fbfbfd;
  --color-tbc37-bg: oklch(0.98 0.004 260);
  --color-tbc37-tint: #dfe2f6;
  --color-tbc37-tint: oklch(0.91 0.03 265);
  --color-tbc37-acc: #4a5ac4;
  --color-tbc37-acc: oklch(0.5 0.16 265);
  --color-tbc37-link: #61656f;
  --color-tbc37-link: oklch(0.46 0.03 260);
  --color-tbc37-linkhover: #3a3f8c;
  --color-tbc37-linkhover: oklch(0.36 0.13 265);
  --color-tbc37-strong: #33363f;
  --color-tbc37-strong: oklch(0.28 0.02 260);
  --color-tbc37-line: #d5d8e2;
  --color-tbc37-line: oklch(0.86 0.01 260);
  --font-tbc37-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-37 {
  width: 100%;
  min-height: 100svh;
}
/* content:counter() has no utility form. One rule, and the badges number themselves. */

.tbc-37 .tbc37-num::after {
  content: counter(tbc37step);
}
/* The compact mode restates the badge's own size, because the link's text-[0] would
   otherwise cascade into it. */

@media (max-width: 40rem) {
  .tbc-37 span[aria-hidden] {
    font-size: 0.75rem;
  }
}
```
