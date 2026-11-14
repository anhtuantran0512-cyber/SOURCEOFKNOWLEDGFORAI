---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-segmented-rounded-outline-pill-breadcrumb/"
title: "Tailwind Segmented Rounded-Outline Pill Breadcrumb"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "Outline-only capsules: each crumb is a hairline rounded border with no fill, hover washes in a faint tint and shifts the border toward the accent, and the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Segmented Rounded-Outline Pill Breadcrumb
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-segmented-rounded-outline-pill-breadcrumb/

Outline-only capsules: each crumb is a hairline rounded border with no fill, hover washes in a faint tint and shifts the border toward the accent, and the current crumb becomes a solid accent pill. The understated treatment, and the port's cleanest one-to-one mapping &mdash; almost every declaration has a utility.
## HTML
```html
<section class="tbc-15 w-full min-h-svh grid place-items-center bg-tbc15-bg font-tbc15-sans px-8 py-8">
  <nav aria-label="Breadcrumb">
    <ol class="flex flex-wrap items-center gap-2.25 list-none m-0 p-0">
      <li class="flex items-center gap-2.25"><a href="#" class="inline-flex items-center min-h-10 px-4 rounded-full border-[1.5px] border-tbc15-edge bg-transparent text-[13px] font-semibold text-tbc15-link no-underline transition-[background-color,border-color,color] duration-200 hover:text-tbc15-acc hover:border-[color-mix(in_oklab,var(--color-tbc15-acc)_50%,var(--color-tbc15-edge))] hover:bg-[color-mix(in_oklab,var(--color-tbc15-acc)_8%,transparent)] focus-visible:outline-2 focus-visible:outline-tbc15-acc focus-visible:outline-offset-2 motion-reduce:transition-none">Home</a></li>
      <li class="flex items-center gap-2.25 before:content-['\203A'] before:text-[13px] before:text-tbc15-sep"><a href="#" class="inline-flex items-center min-h-10 px-4 rounded-full border-[1.5px] border-tbc15-edge bg-transparent text-[13px] font-semibold text-tbc15-link no-underline transition-[background-color,border-color,color] duration-200 hover:text-tbc15-acc hover:border-[color-mix(in_oklab,var(--color-tbc15-acc)_50%,var(--color-tbc15-edge))] hover:bg-[color-mix(in_oklab,var(--color-tbc15-acc)_8%,transparent)] focus-visible:outline-2 focus-visible:outline-tbc15-acc focus-visible:outline-offset-2 motion-reduce:transition-none">Workspace</a></li>
      <li class="flex items-center gap-2.25 before:content-['\203A'] before:text-[13px] before:text-tbc15-sep"><a href="#" class="inline-flex items-center min-h-10 px-4 rounded-full border-[1.5px] border-tbc15-edge bg-transparent text-[13px] font-semibold text-tbc15-link no-underline transition-[background-color,border-color,color] duration-200 hover:text-tbc15-acc hover:border-[color-mix(in_oklab,var(--color-tbc15-acc)_50%,var(--color-tbc15-edge))] hover:bg-[color-mix(in_oklab,var(--color-tbc15-acc)_8%,transparent)] focus-visible:outline-2 focus-visible:outline-tbc15-acc focus-visible:outline-offset-2 motion-reduce:transition-none">Boards</a></li>
      <li class="flex items-center gap-2.25 before:content-['\203A'] before:text-[13px] before:text-tbc15-sep"><a href="#" aria-current="page" class="inline-flex items-center min-h-10 px-4 rounded-full border-[1.5px] text-[13px] font-semibold no-underline text-white bg-tbc15-acc border-tbc15-acc focus-visible:outline-2 focus-visible:outline-tbc15-ink focus-visible:outline-offset-2">Roadmap</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc15-bg: #fdfdfe;
  --color-tbc15-bg: oklch(0.99 0.003 250);
  --color-tbc15-edge: #d6d8e0;
  --color-tbc15-edge: oklch(0.86 0.01 250);
  --color-tbc15-link: #666a77;
  --color-tbc15-link: oklch(0.48 0.03 250);
  --color-tbc15-sep: #b4b7c0;
  --color-tbc15-sep: oklch(0.75 0.02 250);
  --color-tbc15-acc: #4f63c8;
  --color-tbc15-acc: oklch(0.52 0.15 265);
  --color-tbc15-ink: #2f323a;
  --color-tbc15-ink: oklch(0.26 0.02 265);
  --font-tbc15-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-15 {
  width: 100%;
  min-height: 100svh;
}
```
