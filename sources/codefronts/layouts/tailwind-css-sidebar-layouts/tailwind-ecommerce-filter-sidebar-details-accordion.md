---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-ecommerce-filter-sidebar-details-accordion/"
title: "Tailwind E-Commerce Filter Sidebar with Native Details Accordion"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "A storefront filter rail built entirely on native <details>/<summary> &mdash; keyboard-operable, screen-reader-announced and crawlable with zero script."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind E-Commerce Filter Sidebar with Native Details Accordion
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-ecommerce-filter-sidebar-details-accordion/

A storefront filter rail built entirely on native <details>/<summary> &mdash; keyboard-operable, screen-reader-announced and crawlable with zero script. v4's open: variant styles the expanded state, and accent-color brands every checkbox in one utility.
## HTML
```html
<section class="tsl-15 w-full h-svh min-h-svh overflow-y-auto grid grid-cols-[250px_1fr] gap-7 p-7 font-tsl15-sans bg-tsl15-bg text-tsl15-ink">
  <aside aria-label="Product filters" class="sticky top-0 self-start max-h-[calc(100svh-3.5rem)] overflow-y-auto flex flex-col gap-1">
    <h2 class="flex justify-between items-baseline px-0.5 pt-1 pb-3.5 text-[15px] font-bold">Filters <button type="button" class="min-h-11 px-1 border-0 bg-transparent text-tsl15-accent text-[12.5px] font-medium underline underline-offset-[3px] cursor-pointer rounded focus-visible:outline-2 focus-visible:outline-tsl15-accent focus-visible:outline-offset-2">Clear all</button></h2>
    <details name="tsl15-filters" open class="group border-t border-tsl15-line">
      <summary class="flex items-center gap-2 min-h-11 px-0.5 text-[13.5px] font-semibold cursor-pointer list-none rounded-md [&amp;::-webkit-details-marker]:hidden focus-visible:outline-2 focus-visible:outline-tsl15-accent focus-visible:outline-offset-2">Category <span class="ml-auto text-[11.5px] font-medium text-tsl15-mut">128</span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-tsl15-mut stroke-2 [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-[250ms] group-open:rotate-180 motion-reduce:transition-none"><path d="m6 9 6 6 6-6"/></svg></summary>
      <div class="flex flex-col gap-2.5 px-0.5 pt-0.5 pb-4">
        <label class="flex items-center gap-2.5 min-h-11 text-[13.5px] cursor-pointer"><input type="checkbox" checked class="w-4 h-4 accent-tsl15-accent focus-visible:outline-2 focus-visible:outline-tsl15-accent focus-visible:outline-offset-2">Sneakers <span class="ml-auto text-[11.5px] text-tsl15-mut">64</span></label>
        <label class="flex items-center gap-2.5 min-h-11 text-[13.5px] cursor-pointer"><input type="checkbox" class="w-4 h-4 accent-tsl15-accent focus-visible:outline-2 focus-visible:outline-tsl15-accent focus-visible:outline-offset-2">Running <span class="ml-auto text-[11.5px] text-tsl15-mut">38</span></label>
        <label class="flex items-center gap-2.5 min-h-11 text-[13.5px] cursor-pointer"><input type="checkbox" class="w-4 h-4 accent-tsl15-accent focus-visible:outline-2 focus-visible:outline-tsl15-accent focus-visible:outline-offset-2">Trail <span class="ml-auto text-[11.5px] text-tsl15-mut">26</span></label>
      </div>
    </details>
    <details name="tsl15-filters" class="group border-t border-tsl15-line">
      <summary class="flex items-center gap-2 min-h-11 px-0.5 text-[13.5px] font-semibold cursor-pointer list-none rounded-md [&amp;::-webkit-details-marker]:hidden focus-visible:outline-2 focus-visible:outline-tsl15-accent focus-visible:outline-offset-2">Price <span class="ml-auto text-[11.5px] font-medium text-tsl15-mut">$40&ndash;220</span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-tsl15-mut stroke-2 [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-[250ms] group-open:rotate-180 motion-reduce:transition-none"><path d="m6 9 6 6 6-6"/></svg></summary>
      <div class="flex flex-col gap-2.5 px-0.5 pt-0.5 pb-4">
        <input type="range" min="40" max="220" value="120" aria-label="Maximum price" class="w-full accent-tsl15-accent focus-visible:outline-2 focus-visible:outline-tsl15-accent focus-visible:outline-offset-2">
        <label class="flex items-center gap-2.5 min-h-11 text-[13.5px] cursor-pointer"><input type="checkbox" class="w-4 h-4 accent-tsl15-accent focus-visible:outline-2 focus-visible:outline-tsl15-accent focus-visible:outline-offset-2">Under $80 <span class="ml-auto text-[11.5px] text-tsl15-mut">31</span></label>
        <label class="flex items-center gap-2.5 min-h-11 text-[13.5px] cursor-pointer"><input type="checkbox" class="w-4 h-4 accent-tsl15-accent focus-visible:outline-2 focus-visible:outline-tsl15-accent focus-visible:outline-offset-2">$80&ndash;$150 <span class="ml-auto text-[11.5px] text-tsl15-mut">57</span></label>
      </div>
    </details>
    <details name="tsl15-filters" class="group border-t border-tsl15-line">
      <summary class="flex items-center gap-2 min-h-11 px-0.5 text-[13.5px] font-semibold cursor-pointer list-none rounded-md [&amp;::-webkit-details-marker]:hidden focus-visible:outline-2 focus-visible:outline-tsl15-accent focus-visible:outline-offset-2">Brand <span class="ml-auto text-[11.5px] font-medium text-tsl15-mut">12</span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-tsl15-mut stroke-2 [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-[250ms] group-open:rotate-180 motion-reduce:transition-none"><path d="m6 9 6 6 6-6"/></svg></summary>
      <div class="flex flex-col gap-2.5 px-0.5 pt-0.5 pb-4">
        <label class="flex items-center gap-2.5 min-h-11 text-[13.5px] cursor-pointer"><input type="checkbox" class="w-4 h-4 accent-tsl15-accent focus-visible:outline-2 focus-visible:outline-tsl15-accent focus-visible:outline-offset-2">Veloce <span class="ml-auto text-[11.5px] text-tsl15-mut">44</span></label>
        <label class="flex items-center gap-2.5 min-h-11 text-[13.5px] cursor-pointer"><input type="checkbox" class="w-4 h-4 accent-tsl15-accent focus-visible:outline-2 focus-visible:outline-tsl15-accent focus-visible:outline-offset-2">Northpeak <span class="ml-auto text-[11.5px] text-tsl15-mut">29</span></label>
        <label class="flex items-center gap-2.5 min-h-11 text-[13.5px] cursor-pointer"><input type="checkbox" class="w-4 h-4 accent-tsl15-accent focus-visible:outline-2 focus-visible:outline-tsl15-accent focus-visible:outline-offset-2">Atlasform <span class="ml-auto text-[11.5px] text-tsl15-mut">18</span></label>
      </div>
    </details>
  </aside>
  <main aria-label="Products" class="grid grid-cols-[repeat(auto-fill,minmax(160px,1fr))] gap-[18px] content-start">
    <article><div class="aspect-square rounded-xl bg-[linear-gradient(135deg,oklch(0.93_0.01_265),oklch(0.88_0.015_265))]"></div><h3 class="mt-2.5 text-[13.5px] font-semibold leading-snug">Veloce Cloudrunner</h3><p class="mt-1 text-[13px] font-medium text-tsl15-mut">$128</p></article>
    <article><div class="aspect-square rounded-xl bg-[linear-gradient(135deg,oklch(0.93_0.01_265),oklch(0.88_0.015_265))]"></div><h3 class="mt-2.5 text-[13.5px] font-semibold leading-snug">Northpeak Trail 2</h3><p class="mt-1 text-[13px] font-medium text-tsl15-mut">$156</p></article>
    <article><div class="aspect-square rounded-xl bg-[linear-gradient(135deg,oklch(0.93_0.01_265),oklch(0.88_0.015_265))]"></div><h3 class="mt-2.5 text-[13.5px] font-semibold leading-snug">Atlasform Daily</h3><p class="mt-1 text-[13px] font-medium text-tsl15-mut">$92</p></article>
    <article><div class="aspect-square rounded-xl bg-[linear-gradient(135deg,oklch(0.93_0.01_265),oklch(0.88_0.015_265))]"></div><h3 class="mt-2.5 text-[13.5px] font-semibold leading-snug">Veloce Street LX</h3><p class="mt-1 text-[13px] font-medium text-tsl15-mut">$110</p></article>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl15-bg: #fbfbf9;
  --color-tsl15-bg: oklch(0.98 0.003 100);
  --color-tsl15-ink: #393d45;
  --color-tsl15-ink: oklch(0.26 0.015 265);
  --color-tsl15-mut: #7c8089;
  --color-tsl15-mut: oklch(0.55 0.012 265);
  --color-tsl15-line: #e6e7eb;
  --color-tsl15-line: oklch(0.91 0.006 265);
  --color-tsl15-accent: #c23d2e;
  --color-tsl15-accent: oklch(0.55 0.19 25);
  --font-tsl15-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tsl-15 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: light;
  interpolate-size: allow-keywords;
}
/* ::details-content has no variant, and interpolate-size is an inherited
   property set once — both are stylesheet concerns, not class-list ones. */

.tsl-15 details::details-content {
  height: 0;
  overflow: clip;
  transition: height .3s ease, content-visibility .3s allow-discrete;
}

.tsl-15 details[open]::details-content {
  height: auto;
}

@media (prefers-reduced-motion: reduce) {
  .tsl-15 details::details-content {
    transition: none;
  }
}
```
