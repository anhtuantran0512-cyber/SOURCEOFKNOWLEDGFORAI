---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-neumorphic-soft-inset-shadow-breadcrumb-channel/"
title: "Tailwind Neumorphic Soft Inset-Shadow Breadcrumb Channel"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "The inverse of the extruded soft-UI trail: the whole path sits in a channel carved into the surface, each crumb gets its own shallow well on hover, and the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neumorphic Soft Inset-Shadow Breadcrumb Channel
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-neumorphic-soft-inset-shadow-breadcrumb-channel/

The inverse of the extruded soft-UI trail: the whole path sits in a channel carved into the surface, each crumb gets its own shallow well on hover, and the current crumb is the single raised node in the groove. One surface colour, three shadow recipes.
## HTML
```html
<section class="tbc-16 w-full min-h-svh grid place-items-center bg-tbc16-surface font-tbc16-sans px-8 py-10">
  <nav aria-label="Breadcrumb">
    <ol class="flex flex-wrap items-center gap-1.5 list-none m-0 px-3.5 py-2.5 rounded-2xl bg-tbc16-surface shadow-[inset_5px_5px_10px_var(--color-tbc16-dark),inset_-5px_-5px_10px_var(--color-tbc16-light)]">
      <li class="flex items-center"><a href="#" class="inline-flex items-center min-h-10 px-3.5 rounded-xl text-[13px] font-semibold text-tbc16-link no-underline transition-shadow duration-200 hover:shadow-[inset_2px_2px_5px_var(--color-tbc16-dark),inset_-2px_-2px_5px_var(--color-tbc16-light)] focus-visible:outline-2 focus-visible:outline-tbc16-acc focus-visible:outline-offset-2 motion-reduce:transition-none">Home</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-1.5 before:text-tbc16-sep"><a href="#" class="inline-flex items-center min-h-10 px-3.5 rounded-xl text-[13px] font-semibold text-tbc16-link no-underline transition-shadow duration-200 hover:shadow-[inset_2px_2px_5px_var(--color-tbc16-dark),inset_-2px_-2px_5px_var(--color-tbc16-light)] focus-visible:outline-2 focus-visible:outline-tbc16-acc focus-visible:outline-offset-2 motion-reduce:transition-none">Devices</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-1.5 before:text-tbc16-sep"><a href="#" class="inline-flex items-center min-h-10 px-3.5 rounded-xl text-[13px] font-semibold text-tbc16-link no-underline transition-shadow duration-200 hover:shadow-[inset_2px_2px_5px_var(--color-tbc16-dark),inset_-2px_-2px_5px_var(--color-tbc16-light)] focus-visible:outline-2 focus-visible:outline-tbc16-acc focus-visible:outline-offset-2 motion-reduce:transition-none">Thermostat</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-1.5 before:text-tbc16-sep"><a href="#" aria-current="page" class="inline-flex items-center min-h-10 px-3.5 rounded-xl text-[13px] font-bold text-tbc16-pressink no-underline shadow-[5px_5px_10px_var(--color-tbc16-dark),-5px_-5px_10px_var(--color-tbc16-light)] focus-visible:outline-2 focus-visible:outline-tbc16-acc focus-visible:outline-offset-2">Schedule</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc16-surface: #dfe2e8;
  --color-tbc16-surface: oklch(0.9 0.008 250);
  --color-tbc16-dark: #b8bcc5;
  --color-tbc16-dark: oklch(0.78 0.015 250);
  --color-tbc16-light: #fbfcfe;
  --color-tbc16-light: oklch(0.99 0.004 250);
  --color-tbc16-link: #4450b4;
  --color-tbc16-link: oklch(0.45 0.15 260);
  --color-tbc16-pressink: #474b54;
  --color-tbc16-pressink: oklch(0.34 0.02 250);
  --color-tbc16-sep: #8b8f98;
  --color-tbc16-sep: oklch(0.6 0.01 250);
  --color-tbc16-acc: #3f4bb2;
  --color-tbc16-acc: oklch(0.44 0.16 260);
  --font-tbc16-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-16 {
  width: 100%;
  min-height: 100svh;
}
```
