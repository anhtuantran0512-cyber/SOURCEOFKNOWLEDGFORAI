---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-search-input-with-clear/"
title: "Tailwind Search Input With Clear"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "A pill search field with a leading magnifier and a trailing clear button that only exists when there is something to clear."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Search Input With Clear
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-search-input-with-clear/

A pill search field with a leading magnifier and a trailing clear button that only exists when there is something to clear. type="reset" does the clearing; has-[input:placeholder-shown]: does the hiding.
## HTML
```html
<div class="tif-08 grid min-h-svh w-full place-items-center bg-tif08-bg px-6 py-14 font-tif08-sans" aria-label="Search input with clear demo">
  <form role="search" class="group relative flex w-full max-w-80 items-center gap-1 rounded-full border border-white/10 bg-tif08-field pr-1.5 pl-10 transition-[border-color,box-shadow] duration-200 focus-within:border-tif08-acc focus-within:ring-3 focus-within:ring-tif08-acc/18">
    <span class="pointer-events-none absolute left-3.5 grid place-items-center text-tif08-mut transition-colors group-focus-within:text-tif08-acc" aria-hidden="true">
      <svg viewBox="0 0 16 16" width="14" height="14"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" d="M11 11l3 3M7 12a5 5 0 1 1 0-10 5 5 0 0 1 0 10z"/></svg>
    </span>
    <input type="search" name="q" placeholder="Search projects, people, files…" aria-label="Search"
      class="min-w-0 flex-1 border-0 bg-transparent py-2.5 text-sm text-tif08-ink outline-none placeholder:text-tif08-mut [&::-webkit-search-cancel-button]:hidden">
    <button type="reset" aria-label="Clear search"
      class="grid size-11 shrink-0 cursor-pointer place-items-center rounded-full border-0 bg-transparent text-tif08-mut transition-[opacity,background-color,color] duration-150 hover:bg-white/12 hover:text-tif08-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tif08-acc group-has-[input:placeholder-shown]:pointer-events-none group-has-[input:placeholder-shown]:opacity-0">
      <svg viewBox="0 0 12 12" width="10" height="10" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" d="M2 2l8 8M10 2l-8 8"/></svg>
    </button>
  </form>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif08-bg: #12121a;
  --color-tif08-bg: oklch(0.19 0.015 285);
  --color-tif08-field: #1a1a22;
  --color-tif08-field: oklch(0.23 0.015 285);
  --color-tif08-ink: #f0eeff;
  --color-tif08-ink: oklch(0.95 0.02 290);
  --color-tif08-mut: #b8b6d4;
  --color-tif08-mut: oklch(0.77 0.03 290);
  --color-tif08-acc: #60a5fa;
  --color-tif08-acc: oklch(0.73 0.14 255);
  --font-tif08-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tif-08 {
  width: 100%;
}

.tif-08 ::selection {
  background: var(--color-tif08-acc);
  color: #12121a;
}
```
