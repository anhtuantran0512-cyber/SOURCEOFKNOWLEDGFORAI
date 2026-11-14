---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-accessible-breadcrumb-schema-org-microdata-aria/"
title: "Tailwind Accessible Breadcrumb with Schema.org Microdata & ARIA"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "The reference-grade trail: full schema.org BreadcrumbList Microdata inline in the markup so Google can render breadcrumb rich results, ARIA done correctly,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Accessible Breadcrumb with Schema.org Microdata & ARIA
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-accessible-breadcrumb-schema-org-microdata-aria/

The reference-grade trail: full schema.org BreadcrumbList Microdata inline in the markup so Google can render breadcrumb rich results, ARIA done correctly, and separators that stay out of the accessibility tree. The port's win is aria-[current=page]: — the current-page style keys off the attribute a screen reader already reads, so style and semantics cannot drift.
## HTML
```html
<section class="tbc-01 w-full min-h-svh grid place-items-center bg-tbc01-bg font-tbc01-sans px-5 py-9">
  <nav aria-label="Breadcrumb" class="w-[min(680px,100%)] px-4 py-3 rounded-2xl bg-white border border-tbc01-edge shadow-[0_1px_2px_oklch(0.4_0.02_250/0.06)]">
    <ol itemscope itemtype="https://schema.org/BreadcrumbList" class="flex flex-wrap items-center gap-y-0.5 list-none m-0 p-0">
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem" class="flex items-center text-sm font-medium">
        <a itemprop="item" href="/" class="inline-flex items-center min-h-8 px-1.5 rounded-md text-tbc01-link no-underline transition-colors duration-150 hover:text-tbc01-linkhover hover:bg-tbc01-tint hover:underline hover:underline-offset-2 focus-visible:outline-3 focus-visible:outline-tbc01-acc focus-visible:outline-offset-2"><span itemprop="name">Home</span></a>
        <meta itemprop="position" content="1">
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem" class="flex items-center text-sm font-medium before:content-['/'] before:mx-3 before:font-normal before:text-tbc01-sep">
        <a itemprop="item" href="/guides" class="inline-flex items-center min-h-8 px-1.5 rounded-md text-tbc01-link no-underline transition-colors duration-150 hover:text-tbc01-linkhover hover:bg-tbc01-tint hover:underline hover:underline-offset-2 focus-visible:outline-3 focus-visible:outline-tbc01-acc focus-visible:outline-offset-2"><span itemprop="name">Guides</span></a>
        <meta itemprop="position" content="2">
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem" class="flex items-center text-sm font-medium before:content-['/'] before:mx-3 before:font-normal before:text-tbc01-sep">
        <a itemprop="item" href="/guides/css" class="inline-flex items-center min-h-8 px-1.5 rounded-md text-tbc01-link no-underline transition-colors duration-150 hover:text-tbc01-linkhover hover:bg-tbc01-tint hover:underline hover:underline-offset-2 focus-visible:outline-3 focus-visible:outline-tbc01-acc focus-visible:outline-offset-2"><span itemprop="name">CSS</span></a>
        <meta itemprop="position" content="3">
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem" aria-current="page" class="flex items-center text-sm font-medium before:content-['/'] before:mx-3 before:font-normal before:text-tbc01-sep aria-[current=page]:font-semibold aria-[current=page]:text-tbc01-strong">
        <span itemprop="name" class="inline-flex items-center min-h-8 px-1.5">Accessible Breadcrumbs</span>
        <meta itemprop="position" content="4">
      </li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc01-bg: #fcfcfd;
  --color-tbc01-bg: oklch(0.99 0.003 250);
  --color-tbc01-edge: #e6e7ec;
  --color-tbc01-edge: oklch(0.92 0.005 250);
  --color-tbc01-link: #4a63b5;
  --color-tbc01-link: oklch(0.5 0.13 255);
  --color-tbc01-linkhover: #3a4f9c;
  --color-tbc01-linkhover: oklch(0.42 0.16 255);
  --color-tbc01-tint: #eef1fb;
  --color-tbc01-tint: oklch(0.95 0.02 255);
  --color-tbc01-sep: #adb1bd;
  --color-tbc01-sep: oklch(0.72 0.02 250);
  --color-tbc01-strong: #4c4f57;
  --color-tbc01-strong: oklch(0.35 0.01 250);
  --color-tbc01-acc: #3d54a8;
  --color-tbc01-acc: oklch(0.45 0.18 255);
  --font-tbc01-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tbc-01 {
  width: 100%;
  min-height: 100svh;
}
```
