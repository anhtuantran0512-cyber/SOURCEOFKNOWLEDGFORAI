---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-notched-outline-input/"
title: "Tailwind Notched Outline Input"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "The Material notched outline — rebuilt on a real <fieldset> and <legend>, so the browser cuts the gap for you."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Notched Outline Input
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-notched-outline-input/

The Material notched outline — rebuilt on a real <fieldset> and <legend>, so the browser cuts the gap for you. The CSS original fakes it with three bordered spans and an opaque label background that must exactly match the page; this version works on any surface, gradient included.
## HTML
```html
<div class="tif-05 grid min-h-svh w-full place-items-center bg-tif05-bg px-6 py-14 font-tif05-sans" aria-label="Notched outline input demo">
  <label class="group relative block w-full max-w-70">
    <input type="text" name="tif05-name" autocomplete="name" placeholder=" " required
      class="relative z-1 w-full bg-transparent px-3.5 py-3.5 text-sm text-tif05-ink outline-none placeholder:text-transparent">
    <span class="pointer-events-none absolute top-3.5 left-3.5 text-[13px] text-tif05-mut transition-opacity duration-150 group-focus-within:opacity-0 group-has-[input:not(:placeholder-shown)]:opacity-0">Full name</span>
    <fieldset aria-hidden="true" class="pointer-events-none absolute inset-x-0 -top-2 bottom-0 rounded-lg border border-tif05-acc/35 px-2 transition-colors duration-200 group-focus-within:border-tif05-acc">
      <legend class="ml-1 max-w-0 overflow-hidden p-0 text-[10px] font-semibold tracking-[0.06em] whitespace-nowrap text-tif05-acc uppercase opacity-0 transition-[max-width,padding,opacity] duration-200 group-focus-within:max-w-40 group-focus-within:px-1 group-focus-within:opacity-100 group-has-[input:not(:placeholder-shown)]:max-w-40 group-has-[input:not(:placeholder-shown)]:px-1 group-has-[input:not(:placeholder-shown)]:opacity-100 motion-reduce:transition-none">Full name</legend>
    </fieldset>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif05-bg: #07070f;
  --color-tif05-bg: oklch(0.13 0.012 280);
  --color-tif05-ink: #f0eeff;
  --color-tif05-ink: oklch(0.95 0.02 290);
  --color-tif05-mut: #b8b6d4;
  --color-tif05-mut: oklch(0.77 0.03 290);
  --color-tif05-acc: #2eb88a;
  --color-tif05-acc: oklch(0.7 0.13 165);
  --font-tif05-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tif-05 {
  width: 100%;
}

.tif-05 ::selection {
  background: var(--color-tif05-acc);
  color: #07070f;
}
```
