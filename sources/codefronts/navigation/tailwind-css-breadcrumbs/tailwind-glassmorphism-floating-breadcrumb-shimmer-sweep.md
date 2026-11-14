---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-glassmorphism-floating-breadcrumb-shimmer-sweep/"
title: "Tailwind Glassmorphism Floating Breadcrumb Pill with Shimmer Sweep"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "A frosted-glass breadcrumb pill floating over a colour field: heavy backdrop-blur and saturation, a light-catching gradient hairline, and a shimmer that…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism Floating Breadcrumb Pill with Shimmer Sweep
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-glassmorphism-floating-breadcrumb-shimmer-sweep/

A frosted-glass breadcrumb pill floating over a colour field: heavy backdrop-blur and saturation, a light-catching gradient hairline, and a shimmer that sweeps across the bar on hover or keyboard focus. The premium floating-UI treatment, kept readable at AA and reachable from the keyboard.
## HTML
```html
<section class="tbc-05 w-full min-h-svh grid place-items-center px-8 py-12 font-tbc05-sans bg-linear-[120deg,oklch(0.55_0.2_300),oklch(0.6_0.18_220)_45%,oklch(0.68_0.16_180)]">
  <nav aria-label="Breadcrumb" class="group relative overflow-hidden rounded-2xl border border-transparent bg-[linear-gradient(oklch(1_0_0/0.12),oklch(1_0_0/0.08))_padding-box,linear-gradient(155deg,oklch(1_0_0/0.7),oklch(1_0_0/0.15)_40%,oklch(1_0_0/0.04))_border-box] [backdrop-filter:blur(12px)_saturate(180%)] shadow-[0_8px_32px_oklch(0_0_0/0.12),inset_0_1px_0_oklch(1_0_0/0.25)] after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:-translate-x-[120%] after:bg-linear-[115deg,transparent_40%,oklch(1_0_0/0.35)_50%,transparent_60%] after:transition-transform after:duration-700 group-hover:after:translate-x-[220%] group-focus-within:after:translate-x-[220%] motion-reduce:after:hidden">
    <ol class="relative z-1 flex flex-wrap items-center list-none m-0 px-4 py-2.5">
      <li class="flex items-center"><a href="#" class="flex items-center min-h-9 px-2.5 rounded-lg text-sm font-semibold text-white/85 no-underline transition-colors duration-200 hover:text-white hover:bg-white/15 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Home</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-white/60"><a href="#" class="flex items-center min-h-9 px-2.5 rounded-lg text-sm font-semibold text-white/85 no-underline transition-colors duration-200 hover:text-white hover:bg-white/15 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Gallery</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-white/60"><a href="#" class="flex items-center min-h-9 px-2.5 rounded-lg text-sm font-semibold text-white/85 no-underline transition-colors duration-200 hover:text-white hover:bg-white/15 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Collections</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-white/60"><a href="#" aria-current="page" class="flex items-center min-h-9 px-2.5 rounded-lg text-sm font-bold text-white no-underline bg-white/22 shadow-[inset_0_1px_0_oklch(1_0_0/0.3)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Aurora Series</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-tbc05-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-05 {
  width: 100%;
  min-height: 100svh;
}
/* Safari < 16.4 backdrop-filter prefix; Tailwind's arbitrary property emits the
   unprefixed form only. */

.tbc-05 nav {
  -webkit-backdrop-filter: blur(12px) saturate(180%);
}
```
