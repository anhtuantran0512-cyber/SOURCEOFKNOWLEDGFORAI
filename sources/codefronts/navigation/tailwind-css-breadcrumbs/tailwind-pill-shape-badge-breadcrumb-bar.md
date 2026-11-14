---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-pill-shape-badge-breadcrumb-bar/"
title: "Tailwind Pill-Shape Badge Breadcrumb Bar"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "The friendly dashboard trail: every crumb is a softly tinted capsule, hover deepens the tint, and the current crumb is a solid accent pill."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pill-Shape Badge Breadcrumb Bar
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-pill-shape-badge-breadcrumb-bar/

The friendly dashboard trail: every crumb is a softly tinted capsule, hover deepens the tint, and the current crumb is a solid accent pill. Two color-mix() values do all the work, both derived from one accent token, so the whole bar retints from a single edit.
## HTML
```html
<section class="tbc-29 w-full min-h-svh grid place-items-center bg-tbc29-surface font-tbc29-sans px-8 py-8">
  <nav aria-label="Breadcrumb">
    <ol class="flex flex-wrap items-center gap-2 list-none m-0 p-0">
      <li class="flex items-center gap-2"><a href="#" class="inline-flex items-center min-h-10 px-4 rounded-full text-[13px] font-semibold text-tbc29-ink no-underline bg-[color-mix(in_oklab,var(--color-tbc29-acc)_10%,var(--color-tbc29-surface))] transition-colors duration-200 hover:text-tbc29-inkhover hover:bg-[color-mix(in_oklab,var(--color-tbc29-acc)_20%,var(--color-tbc29-surface))] focus-visible:outline-2 focus-visible:outline-tbc29-acc focus-visible:outline-offset-2 motion-reduce:transition-none">Home</a></li>
      <li class="flex items-center gap-2 before:content-['\203A'] before:text-sm before:text-tbc29-sep"><a href="#" class="inline-flex items-center min-h-10 px-4 rounded-full text-[13px] font-semibold text-tbc29-ink no-underline bg-[color-mix(in_oklab,var(--color-tbc29-acc)_10%,var(--color-tbc29-surface))] transition-colors duration-200 hover:text-tbc29-inkhover hover:bg-[color-mix(in_oklab,var(--color-tbc29-acc)_20%,var(--color-tbc29-surface))] focus-visible:outline-2 focus-visible:outline-tbc29-acc focus-visible:outline-offset-2 motion-reduce:transition-none">Team</a></li>
      <li class="flex items-center gap-2 before:content-['\203A'] before:text-sm before:text-tbc29-sep"><a href="#" class="inline-flex items-center min-h-10 px-4 rounded-full text-[13px] font-semibold text-tbc29-ink no-underline bg-[color-mix(in_oklab,var(--color-tbc29-acc)_10%,var(--color-tbc29-surface))] transition-colors duration-200 hover:text-tbc29-inkhover hover:bg-[color-mix(in_oklab,var(--color-tbc29-acc)_20%,var(--color-tbc29-surface))] focus-visible:outline-2 focus-visible:outline-tbc29-acc focus-visible:outline-offset-2 motion-reduce:transition-none">Design</a></li>
      <li class="flex items-center gap-2 before:content-['\203A'] before:text-sm before:text-tbc29-sep"><a href="#" aria-current="page" class="inline-flex items-center min-h-10 px-4 rounded-full text-[13px] font-bold text-white no-underline cursor-default bg-tbc29-acc focus-visible:outline-2 focus-visible:outline-tbc29-ring focus-visible:outline-offset-2">Tokens</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc29-surface: #fbfafe;
  --color-tbc29-surface: oklch(0.98 0.004 285);
  --color-tbc29-ink: #4e4870;
  --color-tbc29-ink: oklch(0.42 0.08 285);
  --color-tbc29-inkhover: #382f60;
  --color-tbc29-inkhover: oklch(0.32 0.12 285);
  --color-tbc29-sep: #a9a4bc;
  --color-tbc29-sep: oklch(0.7 0.02 285);
  --color-tbc29-acc: #6a5ad4;
  --color-tbc29-acc: oklch(0.52 0.16 285);
  --color-tbc29-ring: #2e2856;
  --color-tbc29-ring: oklch(0.28 0.1 285);
  --font-tbc29-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-29 {
  width: 100%;
  min-height: 100svh;
}
```
