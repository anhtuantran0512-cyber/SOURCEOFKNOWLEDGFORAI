---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-responsive-collapsing-breadcrumb-container-queries/"
title: "Tailwind Responsive Collapsing Breadcrumb Bar with Container Queries"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "A trail that truncates itself in a narrow column with zero JavaScript: intermediate crumbs collapse behind an ellipsis, and the ellipsis expands them back."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Responsive Collapsing Breadcrumb Bar with Container Queries
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-responsive-collapsing-breadcrumb-container-queries/

A trail that truncates itself in a narrow column with zero JavaScript: intermediate crumbs collapse behind an ellipsis, and the ellipsis expands them back. The port upgrades the interaction — the CSS original expanded on hover, which touch users cannot do; here a real checkbox holds the expanded state and has-checked: reads it, so tap, click and keyboard all work.
## HTML
```html
<section class="tbc-02 w-full min-h-svh grid place-items-center bg-tbc02-bg font-tbc02-sans text-tbc02-ink px-5 py-9">
  <div class="@container/bar w-[min(560px,100%)] px-4 py-3 rounded-2xl bg-tbc02-panel border border-tbc02-edge">
    <nav aria-label="Breadcrumb">
      <ol class="group flex items-center list-none m-0 p-0">
        <li class="flex items-center"><a href="#" class="flex items-center min-h-9 px-1.5 rounded-md text-sm text-tbc02-mut no-underline transition-colors duration-150 hover:text-white focus-visible:outline-2 focus-visible:outline-tbc02-acc focus-visible:outline-offset-2">Home</a></li>
        <li class="hidden @max-lg/bar:flex items-center before:content-['\203A'] before:mx-2 before:text-tbc02-sep">
          <input type="checkbox" id="tbc02-expand" class="peer sr-only">
          <label for="tbc02-expand" class="grid place-items-center min-w-11 min-h-9 px-2 rounded-lg bg-tbc02-chip text-tbc02-mut font-bold text-[15px] cursor-pointer transition-[opacity,background] duration-200 hover:bg-tbc02-chiphover hover:text-white peer-focus-visible:outline-2 peer-focus-visible:outline-tbc02-acc peer-focus-visible:outline-offset-2 peer-checked:opacity-0 peer-checked:pointer-events-none">&hellip;<span class="sr-only">Show collapsed breadcrumbs</span></label>
        </li>
        <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-tbc02-sep @max-lg/bar:before:hidden group-has-checked:before:inline!"><a href="#" class="flex items-center min-h-9 px-1.5 rounded-md text-sm text-tbc02-mut no-underline whitespace-nowrap overflow-hidden max-w-[14ch] transition-[max-width,opacity,padding] duration-300 hover:text-white focus-visible:outline-2 focus-visible:outline-tbc02-acc focus-visible:outline-offset-2 @max-lg/bar:[max-width:0] @max-lg/bar:opacity-0 @max-lg/bar:px-0 group-has-checked:max-w-[14ch]! group-has-checked:opacity-100! group-has-checked:px-1.5! motion-reduce:transition-none">Store</a></li>
        <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-tbc02-sep @max-lg/bar:before:hidden group-has-checked:before:inline!"><a href="#" class="flex items-center min-h-9 px-1.5 rounded-md text-sm text-tbc02-mut no-underline whitespace-nowrap overflow-hidden max-w-[14ch] transition-[max-width,opacity,padding] duration-300 hover:text-white focus-visible:outline-2 focus-visible:outline-tbc02-acc focus-visible:outline-offset-2 @max-lg/bar:[max-width:0] @max-lg/bar:opacity-0 @max-lg/bar:px-0 group-has-checked:max-w-[14ch]! group-has-checked:opacity-100! group-has-checked:px-1.5! motion-reduce:transition-none">Women</a></li>
        <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-tbc02-sep @max-lg/bar:before:hidden group-has-checked:before:inline!"><a href="#" class="flex items-center min-h-9 px-1.5 rounded-md text-sm text-tbc02-mut no-underline whitespace-nowrap overflow-hidden max-w-[14ch] transition-[max-width,opacity,padding] duration-300 hover:text-white focus-visible:outline-2 focus-visible:outline-tbc02-acc focus-visible:outline-offset-2 @max-lg/bar:[max-width:0] @max-lg/bar:opacity-0 @max-lg/bar:px-0 group-has-checked:max-w-[14ch]! group-has-checked:opacity-100! group-has-checked:px-1.5! motion-reduce:transition-none">Outerwear</a></li>
        <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-tbc02-sep"><a href="#" aria-current="page" class="flex items-center min-h-9 px-1.5 rounded-md text-sm font-semibold text-white no-underline whitespace-nowrap focus-visible:outline-2 focus-visible:outline-tbc02-acc focus-visible:outline-offset-2">Wool Coat</a></li>
      </ol>
    </nav>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc02-bg: #15161f;
  --color-tbc02-bg: oklch(0.14 0.02 265);
  --color-tbc02-panel: #1d1f2b;
  --color-tbc02-panel: oklch(0.19 0.02 265);
  --color-tbc02-edge: #2d2f3d;
  --color-tbc02-edge: oklch(0.26 0.02 265);
  --color-tbc02-chip: #2a2c3a;
  --color-tbc02-chip: oklch(0.24 0.02 265);
  --color-tbc02-chiphover: #3a3d4f;
  --color-tbc02-chiphover: oklch(0.32 0.03 265);
  --color-tbc02-ink: #e3e3ea;
  --color-tbc02-ink: oklch(0.9 0.01 265);
  --color-tbc02-mut: #b7b9c9;
  --color-tbc02-mut: oklch(0.78 0.03 265);
  --color-tbc02-sep: #7c7f93;
  --color-tbc02-sep: oklch(0.55 0.02 265);
  --color-tbc02-acc: #8f8ae8;
  --color-tbc02-acc: oklch(0.72 0.15 285);
  --font-tbc02-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-02 {
  width: 100%;
  min-height: 100svh;
}
```
