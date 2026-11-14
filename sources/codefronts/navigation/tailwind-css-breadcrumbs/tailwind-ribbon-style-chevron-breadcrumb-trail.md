---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-ribbon-style-chevron-breadcrumb-trail/"
title: "Tailwind Ribbon-Style Chevron Breadcrumb Trail"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "The paper-ribbon banner: warm overlapping chevrons with a shadowed crease where each segment folds behind the next."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Ribbon-Style Chevron Breadcrumb Trail
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-ribbon-style-chevron-breadcrumb-trail/

The paper-ribbon banner: warm overlapping chevrons with a shadowed crease where each segment folds behind the next. The fold is one directional inset shadow, and the stacking order is four z- utilities &mdash; the part the CSS version needed four nth-child rules for.
## HTML
```html
<section class="tbc-28 w-full min-h-svh flex items-center justify-center bg-tbc28-bg font-tbc28-sans px-7 py-7 [--tbc28-depth:18px]">
  <nav aria-label="Breadcrumb">
    <ol class="flex list-none m-0 p-0">
      <li class="relative z-4 flex"><a href="#" class="flex items-center h-10.5 pl-5.5 pr-5 text-[13.5px] font-bold text-white no-underline bg-tbc28-step1 [clip-path:polygon(0_0,calc(100%-var(--tbc28-depth))_0,100%_50%,calc(100%-var(--tbc28-depth))_100%,0_100%)] transition-[filter] duration-200 hover:brightness-108 focus-visible:outline-none focus-visible:shadow-[inset_0_0_0_2.5px_white] motion-reduce:transition-none">Home</a></li>
      <li class="relative z-3 flex"><a href="#" class="flex items-center h-10.5 pl-7.5 pr-5 -ms-[var(--tbc28-depth)] text-[13.5px] font-bold text-white no-underline bg-tbc28-step2 shadow-[inset_14px_0_14px_-12px_oklch(0_0_0/0.35)] [clip-path:polygon(0_0,calc(100%-var(--tbc28-depth))_0,100%_50%,calc(100%-var(--tbc28-depth))_100%,0_100%,var(--tbc28-depth)_50%)] transition-[filter] duration-200 hover:brightness-108 focus-visible:outline-none focus-visible:shadow-[inset_0_0_0_2.5px_white] motion-reduce:transition-none">Shop</a></li>
      <li class="relative z-2 flex"><a href="#" class="flex items-center h-10.5 pl-7.5 pr-5 -ms-[var(--tbc28-depth)] text-[13.5px] font-bold text-white no-underline bg-tbc28-step3 shadow-[inset_14px_0_14px_-12px_oklch(0_0_0/0.35)] [clip-path:polygon(0_0,calc(100%-var(--tbc28-depth))_0,100%_50%,calc(100%-var(--tbc28-depth))_100%,0_100%,var(--tbc28-depth)_50%)] transition-[filter] duration-200 hover:brightness-108 focus-visible:outline-none focus-visible:shadow-[inset_0_0_0_2.5px_white] motion-reduce:transition-none">Toys</a></li>
      <li class="relative z-1 flex"><a href="#" aria-current="page" class="flex items-center h-10.5 pl-7.5 pr-6 -ms-[var(--tbc28-depth)] text-[13.5px] font-bold text-white no-underline cursor-default bg-tbc28-current shadow-[inset_14px_0_14px_-12px_oklch(0_0_0/0.35)] [clip-path:polygon(0_0,100%_0,100%_100%,0_100%,var(--tbc28-depth)_50%)] focus-visible:outline-none focus-visible:shadow-[inset_0_0_0_2.5px_white]">Building Blocks</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc28-bg: #f7f0e4;
  --color-tbc28-bg: oklch(0.96 0.02 60);
  --color-tbc28-step1: #b85a2a;
  --color-tbc28-step1: oklch(0.55 0.15 40);
  --color-tbc28-step2: #bf5433;
  --color-tbc28-step2: oklch(0.56 0.16 30);
  --color-tbc28-step3: #c24e38;
  --color-tbc28-step3: oklch(0.57 0.17 22);
  --color-tbc28-current: #b03a63;
  --color-tbc28-current: oklch(0.52 0.18 350);
  --font-tbc28-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-28 {
  width: 100%;
  min-height: 100svh;
}
```
