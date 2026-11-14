---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-breadcrumb-links-animated-underline-glow/"
title: "Tailwind Breadcrumb Links with Animated Underline Glow"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "A dark minimal trail where each link grows a glowing underline that wipes in from the left and retracts to the right &mdash; one pseudo-element, a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Breadcrumb Links with Animated Underline Glow
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-breadcrumb-links-animated-underline-glow/

A dark minimal trail where each link grows a glowing underline that wipes in from the left and retracts to the right &mdash; one pseudo-element, a transform-origin flip, and a drop-shadow for the glow. Entirely compositor-driven, and the current crumb keeps its underline lit.
## HTML
```html
<section class="tbc-25 w-full min-h-svh grid place-items-center bg-tbc25-bg font-tbc25-sans px-8 py-8">
  <nav aria-label="Breadcrumb">
    <ol class="flex flex-wrap items-center list-none m-0 p-0">
      <li class="flex items-center"><a href="#" class="relative px-0.25 py-0.75 text-[15px] font-semibold text-tbc25-link no-underline transition-colors duration-200 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-tbc25-acc focus-visible:outline-offset-4 after:content-[''] after:absolute after:inset-x-0 after:-bottom-1 after:h-[2.5px] after:rounded-[2px] after:bg-tbc25-acc after:scale-x-0 after:origin-right after:transition-transform after:duration-350 after:ease-[cubic-bezier(0.25,1,0.5,1)] after:[filter:drop-shadow(0_0_5px_var(--color-tbc25-acc))] hover:after:scale-x-100 hover:after:origin-left focus-visible:after:scale-x-100 focus-visible:after:origin-left motion-reduce:after:transition-none">Home</a></li>
      <li class="flex items-center before:content-['/'] before:mx-3.5 before:text-tbc25-sep"><a href="#" class="relative px-0.25 py-0.75 text-[15px] font-semibold text-tbc25-link no-underline transition-colors duration-200 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-tbc25-acc focus-visible:outline-offset-4 after:content-[''] after:absolute after:inset-x-0 after:-bottom-1 after:h-[2.5px] after:rounded-[2px] after:bg-tbc25-acc after:scale-x-0 after:origin-right after:transition-transform after:duration-350 after:ease-[cubic-bezier(0.25,1,0.5,1)] after:[filter:drop-shadow(0_0_5px_var(--color-tbc25-acc))] hover:after:scale-x-100 hover:after:origin-left focus-visible:after:scale-x-100 focus-visible:after:origin-left motion-reduce:after:transition-none">Journal</a></li>
      <li class="flex items-center before:content-['/'] before:mx-3.5 before:text-tbc25-sep"><a href="#" class="relative px-0.25 py-0.75 text-[15px] font-semibold text-tbc25-link no-underline transition-colors duration-200 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-tbc25-acc focus-visible:outline-offset-4 after:content-[''] after:absolute after:inset-x-0 after:-bottom-1 after:h-[2.5px] after:rounded-[2px] after:bg-tbc25-acc after:scale-x-0 after:origin-right after:transition-transform after:duration-350 after:ease-[cubic-bezier(0.25,1,0.5,1)] after:[filter:drop-shadow(0_0_5px_var(--color-tbc25-acc))] hover:after:scale-x-100 hover:after:origin-left focus-visible:after:scale-x-100 focus-visible:after:origin-left motion-reduce:after:transition-none">Typography</a></li>
      <li class="flex items-center before:content-['/'] before:mx-3.5 before:text-tbc25-sep"><a href="#" aria-current="page" class="relative px-0.25 py-0.75 text-[15px] font-semibold text-white no-underline cursor-default focus-visible:outline-2 focus-visible:outline-tbc25-acc focus-visible:outline-offset-4 after:content-[''] after:absolute after:inset-x-0 after:-bottom-1 after:h-[2.5px] after:rounded-[2px] after:bg-tbc25-acc after:scale-x-100 after:origin-left after:[filter:drop-shadow(0_0_5px_var(--color-tbc25-acc))]">Variable Fonts</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc25-bg: #1c1a26;
  --color-tbc25-bg: oklch(0.16 0.02 300);
  --color-tbc25-link: #cbc4d6;
  --color-tbc25-link: oklch(0.82 0.02 300);
  --color-tbc25-sep: #6d6580;
  --color-tbc25-sep: oklch(0.5 0.02 300);
  --color-tbc25-acc: #c78ef0;
  --color-tbc25-acc: oklch(0.72 0.17 300);
  --font-tbc25-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-25 {
  width: 100%;
  min-height: 100svh;
}
```
