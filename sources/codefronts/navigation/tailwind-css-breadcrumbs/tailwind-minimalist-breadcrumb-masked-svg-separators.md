---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-minimalist-breadcrumb-masked-svg-separators/"
title: "Tailwind Minimalist Breadcrumb with Swappable Masked SVG Separators"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "The cleanest trail in the collection: plain text links divided by a masked SVG chevron that inherits the crumb's colour, so switching the divider &mdash;…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Minimalist Breadcrumb with Swappable Masked SVG Separators
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-minimalist-breadcrumb-masked-svg-separators/

The cleanest trail in the collection: plain text links divided by a masked SVG chevron that inherits the crumb's colour, so switching the divider &mdash; slash, dot, chevron, anything &mdash; is a one-property edit. Everything else is four utilities.
## HTML
```html
<section class="tbc-26 w-full min-h-svh grid place-items-center bg-tbc26-bg font-tbc26-sans px-8 py-8">
  <nav aria-label="Breadcrumb">
    <ol class="flex flex-wrap items-center list-none m-0 p-0 text-tbc26-mut">
      <li class="flex items-center"><a href="#" class="px-1 py-0.75 rounded-md text-sm font-medium tracking-[0.01em] text-tbc26-link no-underline transition-colors duration-150 hover:text-tbc26-acc focus-visible:outline-2 focus-visible:outline-tbc26-acc focus-visible:outline-offset-2">Home</a></li>
      <li class="flex items-center before:content-[''] before:w-3.5 before:h-3.5 before:mx-2.5 before:opacity-50 before:bg-current before:[mask-image:var(--tbc26-sep)] before:[mask-size:contain] before:[mask-position:center] before:[mask-repeat:no-repeat]"><a href="#" class="px-1 py-0.75 rounded-md text-sm font-medium tracking-[0.01em] text-tbc26-link no-underline transition-colors duration-150 hover:text-tbc26-acc focus-visible:outline-2 focus-visible:outline-tbc26-acc focus-visible:outline-offset-2">Blog</a></li>
      <li class="flex items-center before:content-[''] before:w-3.5 before:h-3.5 before:mx-2.5 before:opacity-50 before:bg-current before:[mask-image:var(--tbc26-sep)] before:[mask-size:contain] before:[mask-position:center] before:[mask-repeat:no-repeat]"><a href="#" class="px-1 py-0.75 rounded-md text-sm font-medium tracking-[0.01em] text-tbc26-link no-underline transition-colors duration-150 hover:text-tbc26-acc focus-visible:outline-2 focus-visible:outline-tbc26-acc focus-visible:outline-offset-2">CSS</a></li>
      <li class="flex items-center text-tbc26-strong before:content-[''] before:w-3.5 before:h-3.5 before:mx-2.5 before:opacity-50 before:bg-current before:[mask-image:var(--tbc26-sep)] before:[mask-size:contain] before:[mask-position:center] before:[mask-repeat:no-repeat]"><a href="#" aria-current="page" class="px-1 py-0.75 rounded-md text-sm font-semibold tracking-[0.01em] text-tbc26-strong no-underline focus-visible:outline-2 focus-visible:outline-tbc26-acc focus-visible:outline-offset-2">Minimal Separators</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc26-bg: #fdfdfe;
  --color-tbc26-bg: oklch(0.99 0.003 250);
  --color-tbc26-mut: #82858f;
  --color-tbc26-mut: oklch(0.58 0.01 250);
  --color-tbc26-link: #6a6d78;
  --color-tbc26-link: oklch(0.5 0.02 250);
  --color-tbc26-strong: #414449;
  --color-tbc26-strong: oklch(0.3 0.01 250);
  --color-tbc26-acc: #4a62cc;
  --color-tbc26-acc: oklch(0.52 0.16 265);
  --font-tbc26-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* The separator glyph: one plain custom property, deliberately not an @theme entry. */

.tbc-26 {
  width: 100%;
  min-height: 100svh;
  --tbc26-sep: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M9 6l6 6-6 6' fill='none' stroke='black' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
}
/* Safari < 15.4 mask prefix. */

.tbc-26 li::before {
  -webkit-mask: var(--tbc26-sep) center/contain no-repeat;
}
```
