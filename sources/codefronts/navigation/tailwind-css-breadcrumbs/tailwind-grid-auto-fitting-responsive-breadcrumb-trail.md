---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-grid-auto-fitting-responsive-breadcrumb-trail/"
title: "Tailwind CSS Grid Auto-Fitting Responsive Breadcrumb Trail"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "A trail laid out on a grid instead of a flex row: crumbs flow into as many max-content columns as fit, then stack into full-width rows below the breakpoint…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Grid Auto-Fitting Responsive Breadcrumb Trail
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-grid-auto-fitting-responsive-breadcrumb-trail/

A trail laid out on a grid instead of a flex row: crumbs flow into as many max-content columns as fit, then stack into full-width rows below the breakpoint &mdash; each crumb a small card that lifts 1px on hover. The port turns one media query into a max-sm: run on four elements.
## HTML
```html
<section class="tbc-17 w-full min-h-svh grid place-items-center px-7 py-7 font-tbc17-sans bg-linear-[180deg,oklch(0.99_0.003_200),oklch(0.96_0.008_205)]">
  <nav aria-label="Breadcrumb" class="w-full max-w-[720px]">
    <ol class="grid justify-center items-center gap-x-1.5 gap-y-2 list-none m-0 p-0 max-w-full [grid-auto-flow:column] [grid-template-columns:repeat(auto-fit,minmax(max-content,auto))] max-sm:[grid-auto-flow:row] max-sm:grid-cols-1 max-sm:gap-1.5">
      <li class="inline-flex items-center gap-1.5 min-w-0 max-sm:w-full max-sm:justify-center"><a href="#" class="inline-flex items-center justify-center h-10 px-3 rounded-lg text-[13px] font-semibold text-tbc17-ink no-underline bg-white border border-tbc17-edge transition-[background-color,border-color,color,translate] duration-200 hover:text-tbc17-acc hover:border-[color-mix(in_oklab,var(--color-tbc17-acc)_40%,var(--color-tbc17-edge))] hover:bg-[color-mix(in_oklab,var(--color-tbc17-acc)_6%,white)] hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tbc17-acc focus-visible:outline-offset-3 max-sm:w-full motion-reduce:transition-none motion-reduce:hover:translate-y-0">Home</a></li>
      <li class="inline-flex items-center gap-1.5 min-w-0 before:content-['\203A'] before:text-sm before:font-semibold before:text-tbc17-mut before:shrink-0 max-sm:w-full max-sm:justify-center max-sm:before:hidden"><a href="#" class="inline-flex items-center justify-center h-10 px-3 rounded-lg text-[13px] font-semibold text-tbc17-ink no-underline bg-white border border-tbc17-edge transition-[background-color,border-color,color,translate] duration-200 hover:text-tbc17-acc hover:border-[color-mix(in_oklab,var(--color-tbc17-acc)_40%,var(--color-tbc17-edge))] hover:bg-[color-mix(in_oklab,var(--color-tbc17-acc)_6%,white)] hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tbc17-acc focus-visible:outline-offset-3 max-sm:w-full motion-reduce:transition-none motion-reduce:hover:translate-y-0">Continents</a></li>
      <li class="inline-flex items-center gap-1.5 min-w-0 before:content-['\203A'] before:text-sm before:font-semibold before:text-tbc17-mut before:shrink-0 max-sm:w-full max-sm:justify-center max-sm:before:hidden"><a href="#" class="inline-flex items-center justify-center h-10 px-3 rounded-lg text-[13px] font-semibold text-tbc17-ink no-underline bg-white border border-tbc17-edge transition-[background-color,border-color,color,translate] duration-200 hover:text-tbc17-acc hover:border-[color-mix(in_oklab,var(--color-tbc17-acc)_40%,var(--color-tbc17-edge))] hover:bg-[color-mix(in_oklab,var(--color-tbc17-acc)_6%,white)] hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tbc17-acc focus-visible:outline-offset-3 max-sm:w-full motion-reduce:transition-none motion-reduce:hover:translate-y-0">Europe</a></li>
      <li class="inline-flex items-center gap-1.5 min-w-0 before:content-['\203A'] before:text-sm before:font-semibold before:text-tbc17-mut before:shrink-0 max-sm:w-full max-sm:justify-center max-sm:before:hidden"><a href="#" class="inline-flex items-center justify-center h-10 px-3 rounded-lg text-[13px] font-semibold text-tbc17-ink no-underline bg-white border border-tbc17-edge transition-[background-color,border-color,color,translate] duration-200 hover:text-tbc17-acc hover:border-[color-mix(in_oklab,var(--color-tbc17-acc)_40%,var(--color-tbc17-edge))] hover:bg-[color-mix(in_oklab,var(--color-tbc17-acc)_6%,white)] hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tbc17-acc focus-visible:outline-offset-3 max-sm:w-full motion-reduce:transition-none motion-reduce:hover:translate-y-0">Countries</a></li>
      <li class="inline-flex items-center gap-1.5 min-w-0 before:content-['\203A'] before:text-sm before:font-semibold before:text-tbc17-mut before:shrink-0 max-sm:w-full max-sm:justify-center max-sm:before:hidden"><a href="#" class="inline-flex items-center justify-center h-10 px-3 rounded-lg text-[13px] font-semibold text-tbc17-ink no-underline bg-white border border-tbc17-edge transition-[background-color,border-color,color,translate] duration-200 hover:text-tbc17-acc hover:border-[color-mix(in_oklab,var(--color-tbc17-acc)_40%,var(--color-tbc17-edge))] hover:bg-[color-mix(in_oklab,var(--color-tbc17-acc)_6%,white)] hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tbc17-acc focus-visible:outline-offset-3 max-sm:w-full motion-reduce:transition-none motion-reduce:hover:translate-y-0">Portugal</a></li>
      <li class="inline-flex items-center gap-1.5 min-w-0 before:content-['\203A'] before:text-sm before:font-semibold before:text-tbc17-mut before:shrink-0 max-sm:w-full max-sm:justify-center max-sm:before:hidden"><a href="#" aria-current="page" class="inline-flex items-center justify-center h-10 px-3 rounded-lg text-[13px] font-bold text-white no-underline bg-tbc17-acc border border-tbc17-acc focus-visible:outline-2 focus-visible:outline-tbc17-ink focus-visible:outline-offset-3 max-sm:w-full">Lisbon</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc17-edge: #e3e8ea;
  --color-tbc17-edge: oklch(0.92 0.008 205);
  --color-tbc17-ink: #2e3b40;
  --color-tbc17-ink: oklch(0.28 0.03 210);
  --color-tbc17-mut: #93a5aa;
  --color-tbc17-mut: oklch(0.68 0.04 205);
  --color-tbc17-acc: #10708f;
  --color-tbc17-acc: oklch(0.5 0.13 210);
  --font-tbc17-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-17 {
  width: 100%;
  min-height: 100svh;
}
```
