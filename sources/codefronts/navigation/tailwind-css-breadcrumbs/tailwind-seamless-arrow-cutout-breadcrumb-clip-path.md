---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-seamless-arrow-cutout-breadcrumb-clip-path/"
title: "Tailwind Seamless Arrow-Cutout Breadcrumb Trail with clip-path"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "The interlocking-chevron trail: every crumb is a clip-path polygon with a notch cut from its leading edge and a point on its trailing edge, overlapped by a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Seamless Arrow-Cutout Breadcrumb Trail with clip-path
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-seamless-arrow-cutout-breadcrumb-clip-path/

The interlocking-chevron trail: every crumb is a clip-path polygon with a notch cut from its leading edge and a point on its trailing edge, overlapped by a negative margin so the shapes mesh. First and last crumbs carry their own flat-edged polygons &mdash; three shapes, stated on the three elements that use them.
## HTML
```html
<section class="tbc-13 w-full min-h-svh grid place-items-center bg-tbc13-page font-tbc13-sans px-8 py-8">
  <nav aria-label="Breadcrumb">
    <ol class="flex list-none m-0 p-0">
      <li class="flex"><a href="#" class="relative flex items-center h-11 pl-4 pr-6.5 text-[13px] font-semibold text-white no-underline bg-tbc13-step1 [clip-path:polygon(0_0,calc(100%-14px)_0,100%_50%,calc(100%-14px)_100%,0_100%)] transition-[filter] duration-200 hover:brightness-112 focus-visible:outline-3 focus-visible:outline-tbc13-ring focus-visible:outline-offset-4 motion-reduce:transition-none">Home</a></li>
      <li class="flex -ms-[14px]"><a href="#" class="relative flex items-center h-11 px-6.5 text-[13px] font-semibold text-white no-underline bg-tbc13-step2 [clip-path:polygon(0_0,calc(100%-14px)_0,100%_50%,calc(100%-14px)_100%,0_100%,14px_50%)] transition-[filter] duration-200 hover:brightness-112 focus-visible:outline-3 focus-visible:outline-tbc13-ring focus-visible:outline-offset-4 motion-reduce:transition-none">Catalog</a></li>
      <li class="flex -ms-[14px]"><a href="#" class="relative flex items-center h-11 px-6.5 text-[13px] font-semibold text-white no-underline bg-tbc13-step3 [clip-path:polygon(0_0,calc(100%-14px)_0,100%_50%,calc(100%-14px)_100%,0_100%,14px_50%)] transition-[filter] duration-200 hover:brightness-112 focus-visible:outline-3 focus-visible:outline-tbc13-ring focus-visible:outline-offset-4 motion-reduce:transition-none">Tools</a></li>
      <li class="flex -ms-[14px]"><a href="#" aria-current="page" class="relative flex items-center h-11 pl-6.5 pr-4 text-[13px] font-bold text-white no-underline bg-tbc13-current [clip-path:polygon(0_0,100%_0,100%_100%,0_100%,14px_50%)] focus-visible:outline-3 focus-visible:outline-tbc13-ring focus-visible:outline-offset-4">Power Drills</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc13-page: #f4f2ec;
  --color-tbc13-page: oklch(0.96 0.01 90);
  --color-tbc13-step1: #8b8778;
  --color-tbc13-step1: oklch(0.58 0.03 90);
  --color-tbc13-step2: #7d7460;
  --color-tbc13-step2: oklch(0.52 0.05 60);
  --color-tbc13-step3: #7a6a55;
  --color-tbc13-step3: oklch(0.5 0.07 40);
  --color-tbc13-current: #c4553c;
  --color-tbc13-current: oklch(0.58 0.18 25);
  --color-tbc13-ring: #4a3a2e;
  --color-tbc13-ring: oklch(0.3 0.05 40);
  --font-tbc13-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-13 {
  width: 100%;
  min-height: 100svh;
}
```
