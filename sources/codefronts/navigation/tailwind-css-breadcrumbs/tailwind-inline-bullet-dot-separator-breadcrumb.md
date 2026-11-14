---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-inline-bullet-dot-separator-breadcrumb/"
title: "Tailwind Inline Bullet-Dot Separator Breadcrumb"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "The classic article-header trail: serif text links divided by small centred bullets, with an italic current page."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Inline Bullet-Dot Separator Breadcrumb
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-inline-bullet-dot-separator-breadcrumb/

The classic article-header trail: serif text links divided by small centred bullets, with an italic current page. Two utilities carry the whole separator, and the port's only real change is that the bullet now belongs to the crumb that follows it.
## HTML
```html
<section class="tbc-34 w-full min-h-svh grid place-items-center bg-tbc34-bg font-tbc34-serif px-8 py-8">
  <nav aria-label="Breadcrumb">
    <ol class="flex flex-wrap items-center list-none m-0 p-0">
      <li class="flex items-center"><a href="#" class="px-0.25 py-0.5 text-[14.5px] text-tbc34-link no-underline transition-colors duration-150 hover:text-tbc34-linkhover hover:underline hover:underline-offset-3 focus-visible:outline-2 focus-visible:outline-tbc34-acc focus-visible:outline-offset-3">Home</a></li>
      <li class="flex items-center before:content-['\2022'] before:mx-3 before:text-[11px] before:text-tbc34-sep"><a href="#" class="px-0.25 py-0.5 text-[14.5px] text-tbc34-link no-underline transition-colors duration-150 hover:text-tbc34-linkhover hover:underline hover:underline-offset-3 focus-visible:outline-2 focus-visible:outline-tbc34-acc focus-visible:outline-offset-3">Blog</a></li>
      <li class="flex items-center before:content-['\2022'] before:mx-3 before:text-[11px] before:text-tbc34-sep"><a href="#" class="px-0.25 py-0.5 text-[14.5px] text-tbc34-link no-underline transition-colors duration-150 hover:text-tbc34-linkhover hover:underline hover:underline-offset-3 focus-visible:outline-2 focus-visible:outline-tbc34-acc focus-visible:outline-offset-3">Frontend</a></li>
      <li class="flex items-center before:content-['\2022'] before:mx-3 before:text-[11px] before:text-tbc34-sep"><a href="#" aria-current="page" class="px-0.25 py-0.5 text-[14.5px] italic text-tbc34-strong no-underline focus-visible:outline-2 focus-visible:outline-tbc34-acc focus-visible:outline-offset-3">Modern CSS in 2027</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc34-bg: #fdfcfa;
  --color-tbc34-bg: oklch(0.99 0.003 60);
  --color-tbc34-link: #77675c;
  --color-tbc34-link: oklch(0.45 0.05 40);
  --color-tbc34-linkhover: #5e4438;
  --color-tbc34-linkhover: oklch(0.36 0.11 35);
  --color-tbc34-strong: #3a3029;
  --color-tbc34-strong: oklch(0.25 0.02 40);
  --color-tbc34-sep: #b9b0a6;
  --color-tbc34-sep: oklch(0.75 0.02 60);
  --color-tbc34-acc: #7d4a38;
  --color-tbc34-acc: oklch(0.45 0.12 35);
  --font-tbc34-serif: 'Fraunces', Georgia, 'Times New Roman', serif;
}

.tbc-34 {
  width: 100%;
  min-height: 100svh;
}
```
