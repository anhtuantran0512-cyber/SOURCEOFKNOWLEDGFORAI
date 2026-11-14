---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-marketplace-filter-chip-breadcrumb-icon-chips/"
title: "Tailwind Marketplace Filter-Chip Breadcrumb with Icon Chips"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "The travel-marketplace bar: a category path on the left, a row of icon-bearing removable filter chips on the right, all inside one pill that becomes a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Marketplace Filter-Chip Breadcrumb with Icon Chips
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-marketplace-filter-chip-breadcrumb-icon-chips/

The travel-marketplace bar: a category path on the left, a row of icon-bearing removable filter chips on the right, all inside one pill that becomes a stacked card in a narrow container. Chips lift on hover and their &times; turns accent &mdash; group-hover: doing the work of three descendant rules.
## HTML
```html
<section class="tbc-20 w-full min-h-svh grid place-items-center px-5 py-8 font-tbc20-sans text-tbc20-ink dark:text-tbc20-dink bg-[radial-gradient(1200px_500px_at_12%_-10%,oklch(0.96_0.03_30/0.55),transparent_60%),radial-gradient(900px_400px_at_100%_0%,oklch(0.96_0.025_220/0.35),transparent_60%),var(--color-tbc20-bg)] dark:bg-tbc20-dbg">
  <div class="@container/bar w-[min(100%,1080px)]">
    <nav aria-label="Breadcrumb and active filters" class="flex flex-wrap items-center gap-4 pl-5 pr-3 py-2 rounded-full bg-tbc20-surface dark:bg-tbc20-dsurface border border-tbc20-edge dark:border-tbc20-dedge shadow-[inset_0_1px_0_oklch(1_0_0/0.6),0_10px_30px_-18px_oklch(0.2_0.05_60/0.25)] @max-lg/bar:flex-col @max-lg/bar:items-stretch @max-lg/bar:rounded-[22px] @max-lg/bar:px-4 @max-lg/bar:py-3.5 @max-lg/bar:gap-3">
    <ol class="flex flex-wrap items-center gap-x-1.5 gap-y-0.5 list-none m-0 p-0 min-h-11 text-[15px] font-medium">
      <li class="inline-flex items-center text-tbc20-mut dark:text-tbc20-dmut"><a href="#" class="inline-flex items-center min-h-11 px-1 rounded-lg text-tbc20-mut dark:text-tbc20-dmut no-underline transition-colors duration-200 hover:text-tbc20-ink dark:hover:text-tbc20-dink hover:underline hover:underline-offset-3 focus-visible:outline-2 focus-visible:outline-tbc20-focus focus-visible:outline-offset-3 motion-reduce:transition-none">Stays</a></li>
      <li class="inline-flex items-center text-tbc20-mut dark:text-tbc20-dmut before:content-[''] before:w-1.5 before:h-1.5 before:mr-2 before:ml-1 before:rotate-45 before:opacity-55 before:border-t-[1.5px] before:border-r-[1.5px] before:border-current"><a href="#" class="inline-flex items-center min-h-11 px-1 rounded-lg text-tbc20-mut dark:text-tbc20-dmut no-underline transition-colors duration-200 hover:text-tbc20-ink dark:hover:text-tbc20-dink hover:underline hover:underline-offset-3 focus-visible:outline-2 focus-visible:outline-tbc20-focus focus-visible:outline-offset-3 motion-reduce:transition-none">Paris</a></li>
      <li class="inline-flex items-center text-tbc20-mut dark:text-tbc20-dmut before:content-[''] before:w-1.5 before:h-1.5 before:mr-2 before:ml-1 before:rotate-45 before:opacity-55 before:border-t-[1.5px] before:border-r-[1.5px] before:border-current"><a href="#" aria-current="page" class="inline-flex items-center min-h-11 px-1 rounded-lg font-semibold text-tbc20-ink dark:text-tbc20-dink no-underline focus-visible:outline-2 focus-visible:outline-tbc20-focus focus-visible:outline-offset-3">Le Marais</a></li>
    </ol>
    <ul aria-label="Active filters" class="flex flex-wrap items-center gap-1.5 list-none m-0 ms-auto p-0 @max-lg/bar:ms-0">
      <li><button type="button" aria-label="Remove Dec 15-22 filter" class="group inline-flex items-center gap-2 min-h-11 pl-2.5 pr-3 rounded-full cursor-pointer appearance-none text-sm font-medium whitespace-nowrap text-tbc20-ink dark:text-tbc20-dink bg-tbc20-surface dark:bg-tbc20-dsurface border border-tbc20-edge dark:border-tbc20-dedge transition-[translate,border-color,box-shadow,background-color] duration-200 hover:-translate-y-px hover:border-[color-mix(in_oklch,var(--color-tbc20-acc)_40%,var(--color-tbc20-edge))] hover:bg-[color-mix(in_oklch,var(--color-tbc20-acc)_6%,var(--color-tbc20-surface))] hover:shadow-[0_6px_14px_-8px_color-mix(in_oklch,var(--color-tbc20-acc)_55%,transparent)] active:translate-y-0 focus-visible:outline-2 focus-visible:outline-tbc20-focus focus-visible:outline-offset-3 motion-reduce:transition-none motion-reduce:hover:translate-y-0"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="w-4 h-4 flex-none text-tbc20-mut dark:text-tbc20-dmut transition-colors duration-200 group-hover:text-tbc20-ink dark:group-hover:text-tbc20-dink"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg><span>Dec 15-22</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="w-3.5 h-3.5 ml-0.5 flex-none text-tbc20-xmut transition-[color,scale] duration-200 group-hover:text-tbc20-acc group-hover:scale-110 motion-reduce:group-hover:scale-100"><path d="M18 6 6 18M6 6l12 12"/></svg></button></li>
      <li><button type="button" aria-label="Remove 2 guests filter" class="group inline-flex items-center gap-2 min-h-11 pl-2.5 pr-3 rounded-full cursor-pointer appearance-none text-sm font-medium whitespace-nowrap text-tbc20-ink dark:text-tbc20-dink bg-tbc20-surface dark:bg-tbc20-dsurface border border-tbc20-edge dark:border-tbc20-dedge transition-[translate,border-color,box-shadow,background-color] duration-200 hover:-translate-y-px hover:border-[color-mix(in_oklch,var(--color-tbc20-acc)_40%,var(--color-tbc20-edge))] hover:bg-[color-mix(in_oklch,var(--color-tbc20-acc)_6%,var(--color-tbc20-surface))] hover:shadow-[0_6px_14px_-8px_color-mix(in_oklch,var(--color-tbc20-acc)_55%,transparent)] active:translate-y-0 focus-visible:outline-2 focus-visible:outline-tbc20-focus focus-visible:outline-offset-3 motion-reduce:transition-none motion-reduce:hover:translate-y-0"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="w-4 h-4 flex-none text-tbc20-mut dark:text-tbc20-dmut transition-colors duration-200 group-hover:text-tbc20-ink dark:group-hover:text-tbc20-dink"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg><span>2 guests</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="w-3.5 h-3.5 ml-0.5 flex-none text-tbc20-xmut transition-[color,scale] duration-200 group-hover:text-tbc20-acc group-hover:scale-110 motion-reduce:group-hover:scale-100"><path d="M18 6 6 18M6 6l12 12"/></svg></button></li>
      <li><button type="button" aria-label="Remove under $200 per night filter" class="group inline-flex items-center gap-2 min-h-11 pl-2.5 pr-3 rounded-full cursor-pointer appearance-none text-sm font-medium whitespace-nowrap text-tbc20-ink dark:text-tbc20-dink bg-tbc20-surface dark:bg-tbc20-dsurface border border-tbc20-edge dark:border-tbc20-dedge transition-[translate,border-color,box-shadow,background-color] duration-200 hover:-translate-y-px hover:border-[color-mix(in_oklch,var(--color-tbc20-acc)_40%,var(--color-tbc20-edge))] hover:bg-[color-mix(in_oklch,var(--color-tbc20-acc)_6%,var(--color-tbc20-surface))] hover:shadow-[0_6px_14px_-8px_color-mix(in_oklch,var(--color-tbc20-acc)_55%,transparent)] active:translate-y-0 focus-visible:outline-2 focus-visible:outline-tbc20-focus focus-visible:outline-offset-3 motion-reduce:transition-none motion-reduce:hover:translate-y-0"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="w-4 h-4 flex-none text-tbc20-mut dark:text-tbc20-dmut transition-colors duration-200 group-hover:text-tbc20-ink dark:group-hover:text-tbc20-dink"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg><span>Under $200/night</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="w-3.5 h-3.5 ml-0.5 flex-none text-tbc20-xmut transition-[color,scale] duration-200 group-hover:text-tbc20-acc group-hover:scale-110 motion-reduce:group-hover:scale-100"><path d="M18 6 6 18M6 6l12 12"/></svg></button></li>
      <li><button type="button" aria-label="Remove Pool amenity filter" class="group inline-flex items-center gap-2 min-h-11 pl-2.5 pr-3 rounded-full cursor-pointer appearance-none text-sm font-medium whitespace-nowrap text-tbc20-ink dark:text-tbc20-dink bg-tbc20-surface dark:bg-tbc20-dsurface border border-tbc20-edge dark:border-tbc20-dedge transition-[translate,border-color,box-shadow,background-color] duration-200 hover:-translate-y-px hover:border-[color-mix(in_oklch,var(--color-tbc20-acc)_40%,var(--color-tbc20-edge))] hover:bg-[color-mix(in_oklch,var(--color-tbc20-acc)_6%,var(--color-tbc20-surface))] hover:shadow-[0_6px_14px_-8px_color-mix(in_oklch,var(--color-tbc20-acc)_55%,transparent)] active:translate-y-0 focus-visible:outline-2 focus-visible:outline-tbc20-focus focus-visible:outline-offset-3 motion-reduce:transition-none motion-reduce:hover:translate-y-0"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="w-4 h-4 flex-none text-tbc20-mut dark:text-tbc20-dmut transition-colors duration-200 group-hover:text-tbc20-ink dark:group-hover:text-tbc20-dink"><path d="M2 20c1.5 0 1.5-1 3-1s1.5 1 3 1 1.5-1 3-1 1.5 1 3 1 1.5-1 3-1 1.5 1 3 1"/><path d="M2 16c1.5 0 1.5-1 3-1s1.5 1 3 1 1.5-1 3-1 1.5 1 3 1 1.5-1 3-1 1.5 1 3 1"/><path d="M7 14V5a2 2 0 0 1 2-2h1M17 14V5a2 2 0 0 0-2-2h-1"/></svg><span>Pool</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="w-3.5 h-3.5 ml-0.5 flex-none text-tbc20-xmut transition-[color,scale] duration-200 group-hover:text-tbc20-acc group-hover:scale-110 motion-reduce:group-hover:scale-100"><path d="M18 6 6 18M6 6l12 12"/></svg></button></li>
      </ul>
    </nav>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* dark: follows the OS here rather than a document class — one line, and every
   dark:* utility in the markup starts working. */

@custom-variant dark (@media (prefers-color-scheme: dark));

@theme {
  --color-tbc20-bg: #fbfaf7;
  --color-tbc20-bg: oklch(0.986 0.008 60);
  --color-tbc20-surface: #ffffff;
  --color-tbc20-ink: #3a352f;
  --color-tbc20-ink: oklch(0.24 0.02 60);
  --color-tbc20-mut: #7d766d;
  --color-tbc20-mut: oklch(0.52 0.015 60);
  --color-tbc20-xmut: #a29a90;
  --color-tbc20-xmut: oklch(0.66 0.012 60);
  --color-tbc20-edge: #e6e2dc;
  --color-tbc20-edge: oklch(0.9 0.012 60);
  --color-tbc20-acc: #d1543a;
  --color-tbc20-acc: oklch(0.63 0.19 25);
  --color-tbc20-focus: #3f63c4;
  --color-tbc20-focus: oklch(0.5 0.15 250);
  --color-tbc20-dbg: #23252e;
  --color-tbc20-dbg: oklch(0.18 0.015 260);
  --color-tbc20-dsurface: #2b2e38;
  --color-tbc20-dsurface: oklch(0.22 0.018 260);
  --color-tbc20-dink: #f4f2ee;
  --color-tbc20-dink: oklch(0.96 0.01 60);
  --color-tbc20-dmut: #b6b3ad;
  --color-tbc20-dmut: oklch(0.72 0.015 60);
  --color-tbc20-dedge: #3d404a;
  --color-tbc20-dedge: oklch(0.3 0.015 260);
  --font-tbc20-sans: 'Space Grotesk', ui-sans-serif, system-ui, sans-serif;
}

.tbc-20 {
  width: 100%;
  min-height: 100svh;
}
```
