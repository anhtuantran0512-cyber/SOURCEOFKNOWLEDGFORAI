---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-floating-card-shadow-breadcrumb-navigation/"
title: "Tailwind Floating Card Shadow Breadcrumb Navigation"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "Each crumb is an elevated white card linked by faint dotted connectors, lifting on hover and resting at top elevation when current."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Floating Card Shadow Breadcrumb Navigation
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-floating-card-shadow-breadcrumb-navigation/

Each crumb is an elevated white card linked by faint dotted connectors, lifting on hover and resting at top elevation when current. Three elevation levels as three arbitrary shadow pairs, and the connector is a dotted border on a pseudo-element.
## HTML
```html
<section class="tbc-32 w-full min-h-svh grid place-items-center bg-tbc32-bg font-tbc32-sans px-7 py-9">
  <nav aria-label="Breadcrumb">
    <ol class="flex flex-wrap items-center gap-5 list-none m-0 p-0">
      <li class="relative flex items-center"><a href="#" class="relative z-1 inline-flex items-center min-h-10 px-4 rounded-xl text-[13.5px] font-semibold text-tbc32-ink no-underline bg-white shadow-[0_1px_2px_oklch(0.25_0.05_265/0.1),0_3px_8px_oklch(0.25_0.05_265/0.08)] transition-[translate,box-shadow,color] duration-200 hover:-translate-y-0.5 hover:text-tbc32-acc hover:shadow-[0_3px_6px_oklch(0.25_0.05_265/0.12),0_10px_22px_oklch(0.25_0.05_265/0.14)] focus-visible:outline-2 focus-visible:outline-tbc32-acc focus-visible:outline-offset-2 motion-reduce:transition-[box-shadow,color] motion-reduce:hover:translate-y-0">Home</a></li>
      <li class="relative flex items-center before:content-[''] before:absolute before:-left-5 before:z-0 before:w-5 before:border-t-2 before:border-dotted before:border-tbc32-dots"><a href="#" class="relative z-1 inline-flex items-center min-h-10 px-4 rounded-xl text-[13.5px] font-semibold text-tbc32-ink no-underline bg-white shadow-[0_1px_2px_oklch(0.25_0.05_265/0.1),0_3px_8px_oklch(0.25_0.05_265/0.08)] transition-[translate,box-shadow,color] duration-200 hover:-translate-y-0.5 hover:text-tbc32-acc hover:shadow-[0_3px_6px_oklch(0.25_0.05_265/0.12),0_10px_22px_oklch(0.25_0.05_265/0.14)] focus-visible:outline-2 focus-visible:outline-tbc32-acc focus-visible:outline-offset-2 motion-reduce:transition-[box-shadow,color] motion-reduce:hover:translate-y-0">Library</a></li>
      <li class="relative flex items-center before:content-[''] before:absolute before:-left-5 before:z-0 before:w-5 before:border-t-2 before:border-dotted before:border-tbc32-dots"><a href="#" class="relative z-1 inline-flex items-center min-h-10 px-4 rounded-xl text-[13.5px] font-semibold text-tbc32-ink no-underline bg-white shadow-[0_1px_2px_oklch(0.25_0.05_265/0.1),0_3px_8px_oklch(0.25_0.05_265/0.08)] transition-[translate,box-shadow,color] duration-200 hover:-translate-y-0.5 hover:text-tbc32-acc hover:shadow-[0_3px_6px_oklch(0.25_0.05_265/0.12),0_10px_22px_oklch(0.25_0.05_265/0.14)] focus-visible:outline-2 focus-visible:outline-tbc32-acc focus-visible:outline-offset-2 motion-reduce:transition-[box-shadow,color] motion-reduce:hover:translate-y-0">Courses</a></li>
      <li class="relative flex items-center before:content-[''] before:absolute before:-left-5 before:z-0 before:w-5 before:border-t-2 before:border-dotted before:border-tbc32-dots"><a href="#" aria-current="page" class="relative z-1 inline-flex items-center min-h-10 px-4 rounded-xl text-[13.5px] font-bold text-tbc32-acc no-underline cursor-default bg-white shadow-[0_4px_8px_oklch(0.25_0.05_265/0.14),0_14px_30px_oklch(0.25_0.05_265/0.16),inset_0_0_0_1.5px_color-mix(in_oklab,var(--color-tbc32-acc)_40%,transparent)] focus-visible:outline-2 focus-visible:outline-tbc32-acc focus-visible:outline-offset-2">CSS Mastery</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc32-bg: #eef0f4;
  --color-tbc32-bg: oklch(0.95 0.006 250);
  --color-tbc32-ink: #575c69;
  --color-tbc32-ink: oklch(0.42 0.02 250);
  --color-tbc32-acc: #3f5cc4;
  --color-tbc32-acc: oklch(0.52 0.16 260);
  --color-tbc32-dots: #bfc3cc;
  --color-tbc32-dots: oklch(0.78 0.01 250);
  --font-tbc32-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-32 {
  width: 100%;
  min-height: 100svh;
}
```
