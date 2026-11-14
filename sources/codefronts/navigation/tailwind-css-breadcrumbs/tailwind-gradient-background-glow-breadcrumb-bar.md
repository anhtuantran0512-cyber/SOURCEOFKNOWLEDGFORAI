---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-gradient-background-glow-breadcrumb-bar/"
title: "Tailwind Gradient Background Glow Breadcrumb Bar"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "A vivid gradient bar with a matching bloom beneath it: the glow is a blurred duplicate of the same gradient on a before: layer, and the current crumb's label…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Gradient Background Glow Breadcrumb Bar
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-gradient-background-glow-breadcrumb-bar/

A vivid gradient bar with a matching bloom beneath it: the glow is a blurred duplicate of the same gradient on a before: layer, and the current crumb's label is painted with a clipped white-to-lilac gradient. Bold, and the glow is one utility run rather than a second element.
## HTML
```html
<section class="tbc-31 w-full min-h-svh flex items-center justify-center isolate bg-tbc31-bg font-tbc31-sans px-8 py-11">
  <nav aria-label="Breadcrumb">
    <ol class="relative flex flex-wrap items-center list-none m-0 px-4.5 py-2.75 rounded-2xl bg-linear-[100deg,oklch(0.6_0.2_300),oklch(0.62_0.19_260)_50%,oklch(0.68_0.17_200)] before:content-[''] before:absolute before:inset-0 before:-z-1 before:rounded-2xl before:bg-[inherit] before:blur-[18px] before:opacity-70 before:translate-y-2 before:pointer-events-none">
      <li class="flex items-center"><a href="#" class="flex items-center min-h-9 px-2.5 rounded-lg text-sm font-semibold text-white no-underline transition-colors duration-200 hover:bg-white/16 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:transition-none">Home</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-2.25 before:text-white/75"><a href="#" class="flex items-center min-h-9 px-2.5 rounded-lg text-sm font-semibold text-white no-underline transition-colors duration-200 hover:bg-white/16 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:transition-none">Studio</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-2.25 before:text-white/75"><a href="#" class="flex items-center min-h-9 px-2.5 rounded-lg text-sm font-semibold text-white no-underline transition-colors duration-200 hover:bg-white/16 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:transition-none">Work</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-2.25 before:text-white/75"><a href="#" aria-current="page" class="flex items-center min-h-9 px-2.5 rounded-lg text-sm font-extrabold no-underline bg-clip-text text-transparent bg-linear-[90deg,white,oklch(0.92_0.08_300)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Spectrum</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc31-bg: #1e1a2b;
  --color-tbc31-bg: oklch(0.15 0.02 285);
  --font-tbc31-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-31 {
  width: 100%;
  min-height: 100svh;
}
```
