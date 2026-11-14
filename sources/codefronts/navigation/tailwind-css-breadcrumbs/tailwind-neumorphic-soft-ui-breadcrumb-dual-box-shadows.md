---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-neumorphic-soft-ui-breadcrumb-dual-box-shadows/"
title: "Tailwind Neumorphic Soft UI Breadcrumb with Dual Box Shadows"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "The soft-UI treatment: crumbs extruded from a single-colour surface by two opposing shadows &mdash; one light source, one dark &mdash; and the current crumb…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neumorphic Soft UI Breadcrumb with Dual Box Shadows
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-neumorphic-soft-ui-breadcrumb-dual-box-shadows/

The soft-UI treatment: crumbs extruded from a single-colour surface by two opposing shadows &mdash; one light source, one dark &mdash; and the current crumb pressed inward with the same pair inverted. Tailwind's shadow-[...] with token references makes the light/dark pair a single editable value instead of four scattered numbers.
## HTML
```html
<section class="tbc-06 w-full min-h-svh grid place-items-center bg-tbc06-surface font-tbc06-sans px-8 py-10">
  <nav aria-label="Breadcrumb">
    <ol class="flex flex-wrap items-center gap-4 list-none m-0 p-0">
      <li class="flex items-center"><a href="#" class="inline-flex items-center min-h-11 px-4 rounded-2xl text-[13.5px] font-semibold text-tbc06-link no-underline bg-tbc06-surface shadow-[5px_5px_10px_var(--color-tbc06-dark),-5px_-5px_10px_var(--color-tbc06-light)] transition-shadow duration-200 hover:shadow-[7px_7px_14px_var(--color-tbc06-dark),-7px_-7px_14px_var(--color-tbc06-light)] focus-visible:outline-2 focus-visible:outline-tbc06-acc focus-visible:outline-offset-3 motion-reduce:transition-none">Home</a></li>
      <li class="flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:mr-4 before:rounded-full before:bg-tbc06-surface before:shadow-[inset_1px_1px_2px_var(--color-tbc06-dark),inset_-1px_-1px_2px_var(--color-tbc06-light)]"><a href="#" class="inline-flex items-center min-h-11 px-4 rounded-2xl text-[13.5px] font-semibold text-tbc06-link no-underline bg-tbc06-surface shadow-[5px_5px_10px_var(--color-tbc06-dark),-5px_-5px_10px_var(--color-tbc06-light)] transition-shadow duration-200 hover:shadow-[7px_7px_14px_var(--color-tbc06-dark),-7px_-7px_14px_var(--color-tbc06-light)] focus-visible:outline-2 focus-visible:outline-tbc06-acc focus-visible:outline-offset-3 motion-reduce:transition-none">Apps</a></li>
      <li class="flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:mr-4 before:rounded-full before:bg-tbc06-surface before:shadow-[inset_1px_1px_2px_var(--color-tbc06-dark),inset_-1px_-1px_2px_var(--color-tbc06-light)]"><a href="#" class="inline-flex items-center min-h-11 px-4 rounded-2xl text-[13.5px] font-semibold text-tbc06-link no-underline bg-tbc06-surface shadow-[5px_5px_10px_var(--color-tbc06-dark),-5px_-5px_10px_var(--color-tbc06-light)] transition-shadow duration-200 hover:shadow-[7px_7px_14px_var(--color-tbc06-dark),-7px_-7px_14px_var(--color-tbc06-light)] focus-visible:outline-2 focus-visible:outline-tbc06-acc focus-visible:outline-offset-3 motion-reduce:transition-none">Finance</a></li>
      <li class="flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:mr-4 before:rounded-full before:bg-tbc06-surface before:shadow-[inset_1px_1px_2px_var(--color-tbc06-dark),inset_-1px_-1px_2px_var(--color-tbc06-light)]"><a href="#" aria-current="page" class="inline-flex items-center min-h-11 px-4 rounded-2xl text-[13.5px] font-bold no-underline bg-tbc06-surface text-tbc06-pressink shadow-[inset_3px_3px_6px_var(--color-tbc06-dark),inset_-3px_-3px_6px_var(--color-tbc06-light)] focus-visible:outline-2 focus-visible:outline-tbc06-acc focus-visible:outline-offset-3">Wallet</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc06-surface: #dfe3e9;
  --color-tbc06-surface: oklch(0.9 0.01 255);
  --color-tbc06-dark: #b9bfc9;
  --color-tbc06-dark: oklch(0.78 0.02 255);
  --color-tbc06-light: #fbfcfe;
  --color-tbc06-light: oklch(0.99 0.005 255);
  --color-tbc06-link: #4453b8;
  --color-tbc06-link: oklch(0.45 0.16 265);
  --color-tbc06-pressink: #43474f;
  --color-tbc06-pressink: oklch(0.32 0.02 255);
  --color-tbc06-acc: #3f4fb0;
  --color-tbc06-acc: oklch(0.45 0.17 265);
  --font-tbc06-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-06 {
  width: 100%;
  min-height: 100svh;
}
```
