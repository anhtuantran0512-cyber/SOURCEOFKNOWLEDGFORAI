---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-outline-border-only-geometric-breadcrumbs/"
title: "Tailwind Outline Border-Only Geometric Breadcrumbs"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "Line-art chevrons with no fills: each crumb is an outline drawn as an inset ring inside a clipped shape, hover washes in a faint tint, and the current crumb…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Outline Border-Only Geometric Breadcrumbs
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-outline-border-only-geometric-breadcrumbs/

Line-art chevrons with no fills: each crumb is an outline drawn as an inset ring inside a clipped shape, hover washes in a faint tint, and the current crumb inverts to solid. The blueprint aesthetic for developer tools and design-system docs.
## HTML
```html
<section class="tbc-36 w-full min-h-svh flex items-center justify-center bg-tbc36-bg font-tbc36-mono px-8 py-8 [--tbc36-depth:15px]">
  <nav aria-label="Breadcrumb">
    <ol class="flex list-none m-0 p-0">
      <li class="flex"><a href="#" class="flex items-center h-9.5 pl-4.5 pr-4 text-xs font-semibold tracking-[0.02em] text-tbc36-acc no-underline bg-transparent shadow-[inset_0_0_0_1.5px_var(--color-tbc36-acc)] [clip-path:polygon(0_0,calc(100%-var(--tbc36-depth))_0,100%_50%,calc(100%-var(--tbc36-depth))_100%,0_100%)] transition-[background-color,color] duration-200 hover:text-tbc36-accdark hover:bg-[color-mix(in_oklab,var(--color-tbc36-acc)_12%,transparent)] focus-visible:outline-none focus-visible:shadow-[inset_0_0_0_1.5px_var(--color-tbc36-acc),inset_0_0_0_4px_color-mix(in_oklab,var(--color-tbc36-acc)_30%,transparent)] motion-reduce:transition-none">Home</a></li>
      <li class="flex"><a href="#" class="flex items-center h-9.5 pl-6 pr-4 -ms-[var(--tbc36-depth)] text-xs font-semibold tracking-[0.02em] text-tbc36-acc no-underline bg-transparent shadow-[inset_0_0_0_1.5px_var(--color-tbc36-acc)] [clip-path:polygon(0_0,calc(100%-var(--tbc36-depth))_0,100%_50%,calc(100%-var(--tbc36-depth))_100%,0_100%,var(--tbc36-depth)_50%)] transition-[background-color,color] duration-200 hover:text-tbc36-accdark hover:bg-[color-mix(in_oklab,var(--color-tbc36-acc)_12%,transparent)] focus-visible:outline-none focus-visible:shadow-[inset_0_0_0_1.5px_var(--color-tbc36-acc),inset_0_0_0_4px_color-mix(in_oklab,var(--color-tbc36-acc)_30%,transparent)] motion-reduce:transition-none">System</a></li>
      <li class="flex"><a href="#" class="flex items-center h-9.5 pl-6 pr-4 -ms-[var(--tbc36-depth)] text-xs font-semibold tracking-[0.02em] text-tbc36-acc no-underline bg-transparent shadow-[inset_0_0_0_1.5px_var(--color-tbc36-acc)] [clip-path:polygon(0_0,calc(100%-var(--tbc36-depth))_0,100%_50%,calc(100%-var(--tbc36-depth))_100%,0_100%,var(--tbc36-depth)_50%)] transition-[background-color,color] duration-200 hover:text-tbc36-accdark hover:bg-[color-mix(in_oklab,var(--color-tbc36-acc)_12%,transparent)] focus-visible:outline-none focus-visible:shadow-[inset_0_0_0_1.5px_var(--color-tbc36-acc),inset_0_0_0_4px_color-mix(in_oklab,var(--color-tbc36-acc)_30%,transparent)] motion-reduce:transition-none">Modules</a></li>
      <li class="flex"><a href="#" aria-current="page" class="flex items-center h-9.5 pl-6 pr-5 -ms-[var(--tbc36-depth)] text-xs font-semibold tracking-[0.02em] text-white no-underline cursor-default bg-tbc36-acc shadow-none [clip-path:polygon(0_0,100%_0,100%_100%,0_100%,var(--tbc36-depth)_50%)] focus-visible:outline-none focus-visible:shadow-[inset_0_0_0_2.5px_white]">Renderer</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc36-bg: #fafcfc;
  --color-tbc36-bg: oklch(0.98 0.005 200);
  --color-tbc36-acc: #14748f;
  --color-tbc36-acc: oklch(0.52 0.14 205);
  --color-tbc36-accdark: #0f5c73;
  --color-tbc36-accdark: oklch(0.42 0.15 205);
  --font-tbc36-mono: 'JetBrains Mono', ui-monospace, 'SF Mono', monospace;
}

.tbc-36 {
  width: 100%;
  min-height: 100svh;
}
```
