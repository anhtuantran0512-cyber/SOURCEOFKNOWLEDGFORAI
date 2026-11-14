---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-pure-css-collapsible-sidebar-drawer-no-javascript/"
title: "Tailwind Pure CSS Collapsible Sidebar Drawer without JavaScript"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The zero-JS drawer done the 2026 way: a hidden checkbox holds state, has-checked: reads it from any depth, and the panel slides on a GPU-composited transform."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pure CSS Collapsible Sidebar Drawer without JavaScript
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-pure-css-collapsible-sidebar-drawer-no-javascript/

The zero-JS drawer done the 2026 way: a hidden checkbox holds state, has-checked: reads it from any depth, and the panel slides on a GPU-composited transform. The hamburger morphs into an X from the same signal, using nth-child arbitrary variants.
## HTML
```html
<section class="tsl-08 relative w-full h-svh min-h-svh grid grid-rows-[auto_1fr] overflow-hidden font-tsl08-sans bg-tsl08-bg text-tsl08-ink">
  <input type="checkbox" id="tsl08-t" class="sr-only peer">
  <header class="flex items-center gap-3.5 h-[54px] px-4 bg-tsl08-panel border-b border-tsl08-line text-[15px] font-semibold">
    <label for="tsl08-t" aria-hidden="true" class="grid gap-[4.5px] -ml-2.5 px-2.5 py-3 rounded-[9px] cursor-pointer">
      <span class="tsl-08-b1 block w-[19px] h-0.5 rounded-sm bg-tsl08-ink transition-[rotate,translate,opacity] duration-300 motion-reduce:transition-none"></span>
      <span class="tsl-08-b2 block w-[19px] h-0.5 rounded-sm bg-tsl08-ink transition-opacity duration-200"></span>
      <span class="tsl-08-b3 block w-[19px] h-0.5 rounded-sm bg-tsl08-ink transition-[rotate,translate,opacity] duration-300 motion-reduce:transition-none"></span>
    </label>
    <strong>Fieldnotes</strong>
  </header>
  <label for="tsl08-t" aria-hidden="true" class="tsl-08-scrim absolute inset-x-0 bottom-0 top-[54px] z-10 bg-[oklch(0_0_0/0.5)] backdrop-blur-[2px] opacity-0 pointer-events-none transition-opacity duration-300 motion-reduce:transition-none"></label>
  <aside aria-label="Menu" class="tsl-08-drawer absolute left-0 top-[54px] bottom-0 z-20 w-[min(280px,85vw)] px-3 py-4 bg-tsl08-panel border-r border-tsl08-line -translate-x-full invisible transition-[translate,visibility] duration-[320ms] ease-[cubic-bezier(.4,0,.2,1)] delay-0 starting:-translate-x-full motion-reduce:transition-none [transition-behavior:allow-discrete]">
    <nav class="flex flex-col gap-0.5">
      <a href="#" aria-current="page" class="flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl08-mut no-underline transition-colors duration-200 hover:text-tsl08-ink hover:bg-tsl08-hover aria-[current=page]:text-tsl08-ink aria-[current=page]:bg-tsl08-tint focus-visible:outline-2 focus-visible:outline-tsl08-accent focus-visible:outline-offset-2">All notes</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl08-mut no-underline transition-colors duration-200 hover:text-tsl08-ink hover:bg-tsl08-hover focus-visible:outline-2 focus-visible:outline-tsl08-accent focus-visible:outline-offset-2">Notebooks</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl08-mut no-underline transition-colors duration-200 hover:text-tsl08-ink hover:bg-tsl08-hover focus-visible:outline-2 focus-visible:outline-tsl08-accent focus-visible:outline-offset-2">Tags</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl08-mut no-underline transition-colors duration-200 hover:text-tsl08-ink hover:bg-tsl08-hover focus-visible:outline-2 focus-visible:outline-tsl08-accent focus-visible:outline-offset-2">Archive</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl08-mut no-underline transition-colors duration-200 hover:text-tsl08-ink hover:bg-tsl08-hover focus-visible:outline-2 focus-visible:outline-tsl08-accent focus-visible:outline-offset-2">Trash</a>
    </nav>
  </aside>
  <main class="p-7 overflow-y-auto [scrollbar-gutter:stable]">
    <h1 class="text-[22px] font-semibold leading-tight mb-2.5">All notes</h1>
    <p class="max-w-[46ch] text-sm leading-relaxed text-tsl08-mut text-pretty">Open the drawer &mdash; the only animated property is transform, so the slide is fully GPU-composited. Zero JavaScript on this page.</p>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl08-bg: #16121b;
  --color-tsl08-bg: oklch(0.14 0.015 300);
  --color-tsl08-panel: #1d1824;
  --color-tsl08-panel: oklch(0.18 0.02 300);
  --color-tsl08-ink: #eae7ef;
  --color-tsl08-ink: oklch(0.93 0.005 300);
  --color-tsl08-mut: #9b95a4;
  --color-tsl08-mut: oklch(0.64 0.012 300);
  --color-tsl08-line: #3c3545;
  --color-tsl08-line: oklch(0.29 0.02 300);
  --color-tsl08-accent: #d07ae0;
  --color-tsl08-accent: oklch(0.72 0.16 320);
  --color-tsl08-hover: rgb(234 231 239 / 0.07);
  --color-tsl08-hover: color-mix(in oklab, oklch(0.93 0.005 300) 7%, transparent);
  --color-tsl08-tint: rgb(208 122 224 / 0.18);
  --color-tsl08-tint: color-mix(in oklab, oklch(0.72 0.16 320) 18%, transparent);
  --font-tsl08-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tsl-08 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
/* STATE — one checkbox, four consequences: drawer, scrim and the three bars. */

#tsl08-t:checked ~ .tsl-08-drawer {
  translate: 0;
  visibility: visible;
}

#tsl08-t:checked ~ .tsl-08-scrim {
  opacity: 1;
  pointer-events: auto;
}

#tsl08-t:checked ~ header .tsl-08-b1 {
  rotate: 45deg;
  translate: 0 6.5px;
}

#tsl08-t:checked ~ header .tsl-08-b2 {
  opacity: 0;
}

#tsl08-t:checked ~ header .tsl-08-b3 {
  rotate: -45deg;
  translate: 0 -6.5px;
}

#tsl08-t:focus-visible ~ header label[for="tsl08-t"] {
  outline: 2px solid var(--color-tsl08-accent);
  outline-offset: 2px;
}
/* visibility must lag the slide on close and lead it on open — one property
   with two different timings, which no single utility can express. */

.tsl-08 aside {
  transition-delay: 0s, 320ms;
}

.tsl-08:has(#tsl08-t:checked) aside {
  transition-delay: 0s, 0s;
}
```
