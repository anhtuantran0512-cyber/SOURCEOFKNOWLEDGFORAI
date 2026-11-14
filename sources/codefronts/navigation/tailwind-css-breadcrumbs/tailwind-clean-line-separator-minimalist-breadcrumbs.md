---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-clean-line-separator-minimalist-breadcrumbs/"
title: "Tailwind Clean Line-Separator Minimalist Breadcrumbs"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "The quietest trail in the set: crumbs divided by thin vertical hairlines with generous whitespace, muted low-profile type, and an underline that only appears…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Clean Line-Separator Minimalist Breadcrumbs
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-clean-line-separator-minimalist-breadcrumbs/

The quietest trail in the set: crumbs divided by thin vertical hairlines with generous whitespace, muted low-profile type, and an underline that only appears on hover. Nine declarations become nine utilities &mdash; the port that proves not every pattern needs an arbitrary value.
## HTML
```html
<section class="tbc-30 w-full min-h-svh grid place-items-center bg-tbc30-bg font-tbc30-sans px-8 py-8">
  <nav aria-label="Breadcrumb">
    <ol class="flex flex-wrap items-center list-none m-0 p-0">
      <li class="flex items-center after:content-[''] after:h-3.5 after:mx-4 after:border-e after:border-tbc30-rule last:after:hidden"><a href="#" class="px-0.25 py-0.5 text-[13.5px] font-normal tracking-[0.015em] text-tbc30-link no-underline transition-colors duration-150 hover:text-tbc30-strong hover:underline hover:underline-offset-3 hover:decoration-1 focus-visible:outline-2 focus-visible:outline-tbc30-ring focus-visible:outline-offset-3">Home</a></li>
      <li class="flex items-center after:content-[''] after:h-3.5 after:mx-4 after:border-e after:border-tbc30-rule last:after:hidden"><a href="#" class="px-0.25 py-0.5 text-[13.5px] font-normal tracking-[0.015em] text-tbc30-link no-underline transition-colors duration-150 hover:text-tbc30-strong hover:underline hover:underline-offset-3 hover:decoration-1 focus-visible:outline-2 focus-visible:outline-tbc30-ring focus-visible:outline-offset-3">Magazine</a></li>
      <li class="flex items-center after:content-[''] after:h-3.5 after:mx-4 after:border-e after:border-tbc30-rule last:after:hidden"><a href="#" class="px-0.25 py-0.5 text-[13.5px] font-normal tracking-[0.015em] text-tbc30-link no-underline transition-colors duration-150 hover:text-tbc30-strong hover:underline hover:underline-offset-3 hover:decoration-1 focus-visible:outline-2 focus-visible:outline-tbc30-ring focus-visible:outline-offset-3">Essays</a></li>
      <li class="flex items-center after:content-[''] after:h-3.5 after:mx-4 after:border-e after:border-tbc30-rule last:after:hidden"><a href="#" aria-current="page" class="px-0.25 py-0.5 text-[13.5px] font-medium tracking-[0.015em] text-tbc30-strong no-underline focus-visible:outline-2 focus-visible:outline-tbc30-ring focus-visible:outline-offset-3">On Slow Design</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc30-bg: #fdfdfc;
  --color-tbc30-bg: oklch(0.99 0.002 90);
  --color-tbc30-rule: #d2d1cd;
  --color-tbc30-rule: oklch(0.84 0.005 90);
  --color-tbc30-link: #7d7b76;
  --color-tbc30-link: oklch(0.52 0.006 90);
  --color-tbc30-strong: #302f2c;
  --color-tbc30-strong: oklch(0.26 0.008 90);
  --color-tbc30-ring: #6b6558;
  --color-tbc30-ring: oklch(0.45 0.03 90);
  --font-tbc30-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-30 {
  width: 100%;
  min-height: 100svh;
}
```
