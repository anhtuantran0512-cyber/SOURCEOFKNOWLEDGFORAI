---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-breadcrumb-bar-dropdown-sibling-menus/"
title: "Tailwind Breadcrumb Bar with Built-In Dropdown Sibling Menus"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "Power navigation: intermediate crumbs open a dropdown of sibling pages, built on native <details>/<summary> so it is keyboard-ready and script-free."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Breadcrumb Bar with Built-In Dropdown Sibling Menus
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-breadcrumb-bar-dropdown-sibling-menus/

Power navigation: intermediate crumbs open a dropdown of sibling pages, built on native <details>/<summary> so it is keyboard-ready and script-free. The port reads the disclosure state with open: on the <details> and a direct-child arbitrary variant for the caret &mdash; never group-open:, which would match through nested disclosures.
## HTML
```html
<section class="tbc-10 w-full min-h-svh grid place-items-center bg-tbc10-bg font-tbc10-sans px-8 py-8">
  <nav aria-label="Breadcrumb" class="w-[min(620px,100%)]">
    <ol class="flex flex-wrap items-center list-none m-0 p-0">
      <li class="relative flex items-center"><a href="#" class="flex items-center min-h-9 px-2 rounded-[7px] text-[13.5px] font-semibold text-tbc10-link no-underline transition-colors duration-150 hover:text-tbc10-linkhover hover:bg-tbc10-tint focus-visible:outline-2 focus-visible:outline-tbc10-acc focus-visible:outline-offset-2">Home</a></li>
      <li class="relative flex items-center before:content-['\203A'] before:mx-1.5 before:text-tbc10-sep">
        <details open class="[&[open]>summary>svg]:rotate-180">
          <summary class="inline-flex items-center gap-1 min-h-9 px-2 rounded-[7px] list-none cursor-pointer text-[13.5px] font-semibold text-tbc10-link transition-colors duration-150 hover:text-tbc10-linkhover hover:bg-tbc10-tint focus-visible:outline-2 focus-visible:outline-tbc10-acc focus-visible:outline-offset-2 [&::-webkit-details-marker]:hidden [&::marker]:content-['']">Guides<svg viewBox="0 0 24 24" aria-hidden="true" class="w-3.25 h-3.25 fill-none stroke-current [stroke-width:2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 motion-reduce:transition-none"><path d="M6 9l6 6 6-6"/></svg></summary>
          <div role="group" aria-label="Sibling sections" class="absolute top-[calc(100%+6px)] left-0 z-20 flex flex-col min-w-[170px] p-1.5 rounded-xl bg-white border border-tbc10-edge shadow-[0_10px_30px_oklch(0.25_0.05_265/0.14)]">
            <a href="#" class="flex items-center min-h-9 px-2.5 rounded-[7px] text-[13.5px] font-medium text-tbc10-menuink no-underline transition-colors duration-150 hover:bg-[color-mix(in_oklab,var(--color-tbc10-acc)_12%,transparent)] hover:text-tbc10-acc focus-visible:outline-2 focus-visible:outline-tbc10-acc focus-visible:-outline-offset-2">Tutorials</a>
            <a href="#" class="flex items-center min-h-9 px-2.5 rounded-[7px] text-[13.5px] font-medium text-tbc10-menuink no-underline transition-colors duration-150 hover:bg-[color-mix(in_oklab,var(--color-tbc10-acc)_12%,transparent)] hover:text-tbc10-acc focus-visible:outline-2 focus-visible:outline-tbc10-acc focus-visible:-outline-offset-2">References</a>
            <a href="#" class="flex items-center min-h-9 px-2.5 rounded-[7px] text-[13.5px] font-medium text-tbc10-menuink no-underline transition-colors duration-150 hover:bg-[color-mix(in_oklab,var(--color-tbc10-acc)_12%,transparent)] hover:text-tbc10-acc focus-visible:outline-2 focus-visible:outline-tbc10-acc focus-visible:-outline-offset-2">Recipes</a>
            <a href="#" class="flex items-center min-h-9 px-2.5 rounded-[7px] text-[13.5px] font-medium text-tbc10-menuink no-underline transition-colors duration-150 hover:bg-[color-mix(in_oklab,var(--color-tbc10-acc)_12%,transparent)] hover:text-tbc10-acc focus-visible:outline-2 focus-visible:outline-tbc10-acc focus-visible:-outline-offset-2">Changelog</a>
          </div>
        </details>
      </li>
      <li class="relative flex items-center before:content-['\203A'] before:mx-1.5 before:text-tbc10-sep">
        <details class="[&[open]>summary>svg]:rotate-180">
          <summary class="inline-flex items-center gap-1 min-h-9 px-2 rounded-[7px] list-none cursor-pointer text-[13.5px] font-semibold text-tbc10-link transition-colors duration-150 hover:text-tbc10-linkhover hover:bg-tbc10-tint focus-visible:outline-2 focus-visible:outline-tbc10-acc focus-visible:outline-offset-2 [&::-webkit-details-marker]:hidden [&::marker]:content-['']">CSS<svg viewBox="0 0 24 24" aria-hidden="true" class="w-3.25 h-3.25 fill-none stroke-current [stroke-width:2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 motion-reduce:transition-none"><path d="M6 9l6 6 6-6"/></svg></summary>
          <div role="group" aria-label="Sibling sections" class="absolute top-[calc(100%+6px)] left-0 z-20 flex flex-col min-w-[170px] p-1.5 rounded-xl bg-white border border-tbc10-edge shadow-[0_10px_30px_oklch(0.25_0.05_265/0.14)]">
            <a href="#" class="flex items-center min-h-9 px-2.5 rounded-[7px] text-[13.5px] font-medium text-tbc10-menuink no-underline transition-colors duration-150 hover:bg-[color-mix(in_oklab,var(--color-tbc10-acc)_12%,transparent)] hover:text-tbc10-acc focus-visible:outline-2 focus-visible:outline-tbc10-acc focus-visible:-outline-offset-2">HTML</a>
            <a href="#" class="flex items-center min-h-9 px-2.5 rounded-[7px] text-[13.5px] font-medium text-tbc10-menuink no-underline transition-colors duration-150 hover:bg-[color-mix(in_oklab,var(--color-tbc10-acc)_12%,transparent)] hover:text-tbc10-acc focus-visible:outline-2 focus-visible:outline-tbc10-acc focus-visible:-outline-offset-2">JavaScript</a>
            <a href="#" class="flex items-center min-h-9 px-2.5 rounded-[7px] text-[13.5px] font-medium text-tbc10-menuink no-underline transition-colors duration-150 hover:bg-[color-mix(in_oklab,var(--color-tbc10-acc)_12%,transparent)] hover:text-tbc10-acc focus-visible:outline-2 focus-visible:outline-tbc10-acc focus-visible:-outline-offset-2">Accessibility</a>
          </div>
        </details>
      </li>
      <li class="relative flex items-center before:content-['\203A'] before:mx-1.5 before:text-tbc10-sep"><a href="#" aria-current="page" class="flex items-center min-h-9 px-2 rounded-[7px] text-[13.5px] font-bold text-tbc10-strong no-underline focus-visible:outline-2 focus-visible:outline-tbc10-acc focus-visible:outline-offset-2">Dropdown Breadcrumbs</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc10-bg: #fbfbfd;
  --color-tbc10-bg: oklch(0.98 0.004 265);
  --color-tbc10-edge: #e4e5ec;
  --color-tbc10-edge: oklch(0.9 0.008 265);
  --color-tbc10-tint: #eceef8;
  --color-tbc10-tint: oklch(0.94 0.02 265);
  --color-tbc10-link: #5b64ab;
  --color-tbc10-link: oklch(0.48 0.08 265);
  --color-tbc10-linkhover: #3b4396;
  --color-tbc10-linkhover: oklch(0.36 0.13 265);
  --color-tbc10-menuink: #5a5d68;
  --color-tbc10-menuink: oklch(0.4 0.02 265);
  --color-tbc10-strong: #35383f;
  --color-tbc10-strong: oklch(0.28 0.02 265);
  --color-tbc10-sep: #adb0ba;
  --color-tbc10-sep: oklch(0.72 0.02 265);
  --color-tbc10-acc: #5a68cc;
  --color-tbc10-acc: oklch(0.55 0.15 265);
  --font-tbc10-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-10 {
  width: 100%;
  min-height: 100svh;
}
/* ::details-content has no variant form, and interpolate-size is a property, not a
   utility. The progressive height tween therefore stays CSS. */

.tbc-10 details::details-content {
  height: 0;
  overflow: hidden;
  transition: height .2s ease, content-visibility .2s ease allow-discrete;
  interpolate-size: allow-keywords;
}

.tbc-10 details[open]::details-content {
  height: auto;
}

@media (prefers-reduced-motion: reduce) {
  .tbc-10 details::details-content {
    transition: none;
  }
}
```
