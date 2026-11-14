---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-editorial-breadcrumb-animated-svg-wave-underline/"
title: "Tailwind Editorial Breadcrumb with Animated SVG Wave Underline"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "Warm paper, italic serif crumbs, and a signature flourish: an inline SVG wave draws itself under each crumb on hover or focus by tweening stroke-dashoffset."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Editorial Breadcrumb with Animated SVG Wave Underline
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-editorial-breadcrumb-animated-svg-wave-underline/

Warm paper, italic serif crumbs, and a signature flourish: an inline SVG wave draws itself under each crumb on hover or focus by tweening stroke-dashoffset. Tailwind has no dash utilities, so the port keeps two arbitrary properties on the path and everything else moves inline.
## HTML
```html
<section class="tbc-21 w-full min-h-svh grid place-items-center px-6 py-12 font-tbc21-serif bg-tbc21-paper dark:bg-tbc21-dpaper text-tbc21-ink dark:text-tbc21-dink">
  <article class="w-full max-w-[62ch] flex flex-col gap-5">
    <nav aria-label="Breadcrumb" class="text-[15px]/[1.4]">
      <ol class="flex flex-wrap items-center gap-x-1.5 gap-y-0.5 list-none m-0 p-0">
        <li class="inline-flex items-center min-h-11"><a href="#" class="group relative inline-flex items-center min-h-11 px-0.5 py-2.5 rounded-sm italic tracking-[0.005em] text-tbc21-ink dark:text-tbc21-dink no-underline transition-colors duration-200 hover:text-tbc21-strong dark:hover:text-tbc21-dstrong focus-visible:text-tbc21-strong focus-visible:outline-2 focus-visible:outline-tbc21-acc focus-visible:outline-offset-3"><span class="relative inline-block">Home<svg aria-hidden="true" viewBox="0 0 60 6" preserveAspectRatio="none" class="absolute inset-x-0 bottom-1.5 w-full h-1.5 overflow-visible pointer-events-none text-tbc21-acc dark:text-tbc21-dacc"><path d="M0 3 Q 15 0, 30 3 T 60 3" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" pathLength="100" vector-effect="non-scaling-stroke" class="opacity-0 [stroke-dasharray:100] [stroke-dashoffset:100] transition-[stroke-dashoffset,opacity] duration-450 group-hover:opacity-100 group-hover:[stroke-dashoffset:0] group-focus-visible:opacity-100 group-focus-visible:[stroke-dashoffset:0] motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:duration-150"/></svg></span></a></li>
        <li class="inline-flex items-center min-h-11 before:content-['\00B7'] before:mr-2 before:ml-1 before:text-[1.05em] before:text-tbc21-sep"><a href="#" class="group relative inline-flex items-center min-h-11 px-0.5 py-2.5 rounded-sm italic tracking-[0.005em] text-tbc21-ink dark:text-tbc21-dink no-underline transition-colors duration-200 hover:text-tbc21-strong dark:hover:text-tbc21-dstrong focus-visible:text-tbc21-strong focus-visible:outline-2 focus-visible:outline-tbc21-acc focus-visible:outline-offset-3"><span class="relative inline-block">Style<svg aria-hidden="true" viewBox="0 0 60 6" preserveAspectRatio="none" class="absolute inset-x-0 bottom-1.5 w-full h-1.5 overflow-visible pointer-events-none text-tbc21-acc dark:text-tbc21-dacc"><path d="M0 3 Q 15 0, 30 3 T 60 3" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" pathLength="100" vector-effect="non-scaling-stroke" class="opacity-0 [stroke-dasharray:100] [stroke-dashoffset:100] transition-[stroke-dashoffset,opacity] duration-450 group-hover:opacity-100 group-hover:[stroke-dashoffset:0] group-focus-visible:opacity-100 group-focus-visible:[stroke-dashoffset:0] motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:duration-150"/></svg></span></a></li>
        <li class="inline-flex items-center min-h-11 before:content-['\00B7'] before:mr-2 before:ml-1 before:text-[1.05em] before:text-tbc21-sep"><a href="#" class="group relative inline-flex items-center min-h-11 px-0.5 py-2.5 rounded-sm italic tracking-[0.005em] text-tbc21-ink dark:text-tbc21-dink no-underline transition-colors duration-200 hover:text-tbc21-strong dark:hover:text-tbc21-dstrong focus-visible:text-tbc21-strong focus-visible:outline-2 focus-visible:outline-tbc21-acc focus-visible:outline-offset-3"><span class="relative inline-block">Fashion<svg aria-hidden="true" viewBox="0 0 60 6" preserveAspectRatio="none" class="absolute inset-x-0 bottom-1.5 w-full h-1.5 overflow-visible pointer-events-none text-tbc21-acc dark:text-tbc21-dacc"><path d="M0 3 Q 15 0, 30 3 T 60 3" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" pathLength="100" vector-effect="non-scaling-stroke" class="opacity-0 [stroke-dasharray:100] [stroke-dashoffset:100] transition-[stroke-dashoffset,opacity] duration-450 group-hover:opacity-100 group-hover:[stroke-dashoffset:0] group-focus-visible:opacity-100 group-focus-visible:[stroke-dashoffset:0] motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:duration-150"/></svg></span></a></li>
        <li aria-current="page" class="inline-flex items-center min-h-11 before:content-['\00B7'] before:mr-2 before:ml-1 before:text-[1.05em] before:text-tbc21-sep"><span class="inline-flex items-center min-h-11 px-0.5 py-2.5 not-italic font-semibold cursor-default text-tbc21-strong dark:text-tbc21-dstrong">The Return of Tailored Denim</span></li>
      </ol>
    </nav>
    <h1 class="m-0 mt-2 text-[clamp(1.75rem,4vw,2.4rem)]/[1.15] font-semibold tracking-[-0.01em] text-tbc21-strong dark:text-tbc21-dstrong">The Return of Tailored Denim</h1>
    <p class="m-0 max-w-[48ch] text-base/[1.55] italic text-tbc21-ink dark:text-tbc21-dink">A quiet revival of pressed seams and structured silhouettes, filed under Style / Fashion.</p>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@custom-variant dark (@media (prefers-color-scheme: dark));

@theme {
  --color-tbc21-paper: #f7f3ea;
  --color-tbc21-paper: oklch(0.97 0.01 85);
  --color-tbc21-ink: #6b6459;
  --color-tbc21-ink: oklch(0.42 0.02 60);
  --color-tbc21-strong: #37322c;
  --color-tbc21-strong: oklch(0.22 0.02 60);
  --color-tbc21-sep: #9b948a;
  --color-tbc21-sep: oklch(0.62 0.02 60);
  --color-tbc21-acc: #a85a34;
  --color-tbc21-acc: oklch(0.55 0.14 30);
  --color-tbc21-dpaper: #2b2620;
  --color-tbc21-dpaper: oklch(0.19 0.01 70);
  --color-tbc21-dink: #c4bdaf;
  --color-tbc21-dink: oklch(0.74 0.02 80);
  --color-tbc21-dstrong: #f1ece0;
  --color-tbc21-dstrong: oklch(0.93 0.02 85);
  --color-tbc21-dacc: #e0a866;
  --color-tbc21-dacc: oklch(0.78 0.14 60);
  --font-tbc21-serif: 'Fraunces', Charter, 'Iowan Old Style', Georgia, serif;
}

.tbc-21 {
  width: 100%;
  min-height: 100svh;
}
```
