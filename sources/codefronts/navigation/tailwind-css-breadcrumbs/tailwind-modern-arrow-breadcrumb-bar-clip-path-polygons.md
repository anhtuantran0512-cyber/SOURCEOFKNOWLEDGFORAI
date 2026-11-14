---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-modern-arrow-breadcrumb-bar-clip-path-polygons/"
title: "Tailwind Modern Arrow Breadcrumb Bar using clip-path Polygons"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "The interlocking-arrow bar with a tunable point: one --tbc23-depth property drives every polygon and every overlap, so the chevron angle is a one-line edit…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Modern Arrow Breadcrumb Bar using clip-path Polygons
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-modern-arrow-breadcrumb-bar-clip-path-polygons/

The interlocking-arrow bar with a tunable point: one --tbc23-depth property drives every polygon and every overlap, so the chevron angle is a one-line edit across a five-step trail. The list carries a drop-shadow filter, which is the only way to shadow a clipped shape.
## HTML
```html
<section class="tbc-23 w-full min-h-svh flex items-center justify-center bg-tbc23-bg font-tbc23-sans px-7 py-7 [--tbc23-depth:16px]">
  <nav aria-label="Breadcrumb">
    <ol class="flex list-none m-0 p-0 [filter:drop-shadow(0_2px_4px_oklch(0_0_0/0.12))]">
      <li class="flex"><a href="#" class="flex items-center h-10 pl-5 pr-4.5 text-[13.5px] font-semibold text-white no-underline bg-tbc23-step1 [clip-path:polygon(0_0,calc(100%-var(--tbc23-depth))_0,100%_50%,calc(100%-var(--tbc23-depth))_100%,0_100%)] transition-[filter] duration-200 hover:brightness-112 focus-visible:outline-none focus-visible:shadow-[inset_0_0_0_2.5px_white,inset_0_0_0_4px_var(--color-tbc23-acc)] motion-reduce:transition-none">Home</a></li>
      <li class="flex"><a href="#" class="flex items-center h-10 pl-6.5 pr-4.5 -ms-[var(--tbc23-depth)] text-[13.5px] font-semibold text-white no-underline bg-tbc23-step2 [clip-path:polygon(0_0,calc(100%-var(--tbc23-depth))_0,100%_50%,calc(100%-var(--tbc23-depth))_100%,0_100%,var(--tbc23-depth)_50%)] transition-[filter] duration-200 hover:brightness-112 focus-visible:outline-none focus-visible:shadow-[inset_0_0_0_2.5px_white,inset_0_0_0_4px_var(--color-tbc23-acc)] motion-reduce:transition-none">Electronics</a></li>
      <li class="flex"><a href="#" class="flex items-center h-10 pl-6.5 pr-4.5 -ms-[var(--tbc23-depth)] text-[13.5px] font-semibold text-white no-underline bg-tbc23-step3 [clip-path:polygon(0_0,calc(100%-var(--tbc23-depth))_0,100%_50%,calc(100%-var(--tbc23-depth))_100%,0_100%,var(--tbc23-depth)_50%)] transition-[filter] duration-200 hover:brightness-112 focus-visible:outline-none focus-visible:shadow-[inset_0_0_0_2.5px_white,inset_0_0_0_4px_var(--color-tbc23-acc)] motion-reduce:transition-none">Audio</a></li>
      <li class="flex"><a href="#" class="flex items-center h-10 pl-6.5 pr-4.5 -ms-[var(--tbc23-depth)] text-[13.5px] font-semibold text-white no-underline bg-tbc23-step4 [clip-path:polygon(0_0,calc(100%-var(--tbc23-depth))_0,100%_50%,calc(100%-var(--tbc23-depth))_100%,0_100%,var(--tbc23-depth)_50%)] transition-[filter] duration-200 hover:brightness-112 focus-visible:outline-none focus-visible:shadow-[inset_0_0_0_2.5px_white,inset_0_0_0_4px_var(--color-tbc23-acc)] motion-reduce:transition-none">Headphones</a></li>
      <li class="flex"><a href="#" aria-current="page" class="flex items-center h-10 pl-6.5 pr-5.5 -ms-[var(--tbc23-depth)] text-[13.5px] font-bold text-white no-underline cursor-default bg-tbc23-acc [clip-path:polygon(0_0,100%_0,100%_100%,0_100%,var(--tbc23-depth)_50%)] focus-visible:outline-none focus-visible:shadow-[inset_0_0_0_2.5px_white,inset_0_0_0_4px_var(--color-tbc23-ring)]">Wireless Over-Ear</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc23-bg: #f2f3f6;
  --color-tbc23-bg: oklch(0.96 0.005 260);
  --color-tbc23-step1: #8f929d;
  --color-tbc23-step1: oklch(0.6 0.02 260);
  --color-tbc23-step2: #82868f;
  --color-tbc23-step2: oklch(0.56 0.03 260);
  --color-tbc23-step3: #757985;
  --color-tbc23-step3: oklch(0.52 0.04 260);
  --color-tbc23-step4: #686d7d;
  --color-tbc23-step4: oklch(0.48 0.05 260);
  --color-tbc23-acc: #5a63cf;
  --color-tbc23-acc: oklch(0.55 0.17 265);
  --color-tbc23-ring: #2b2f66;
  --color-tbc23-ring: oklch(0.3 0.1 265);
  --font-tbc23-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-23 {
  width: 100%;
  min-height: 100svh;
}
```
