---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-multi-column-form-grid-floating-labels/"
title: "Tailwind Multi-Column Form Grid with Floating Labels"
section: "components"
category: "tailwind-css-floating-label-inputs"
category_name: "Tailwind CSS Floating Label Inputs"
description: "A checkout address form laying floating-label fields onto a six-track grid: col-span-3 pairs, a full-width street, and a col-span-2 City/State/ZIP row."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Multi-Column Form Grid with Floating Labels
Source: https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-multi-column-form-grid-floating-labels/

A checkout address form laying floating-label fields onto a six-track grid: col-span-3 pairs, a full-width street, and a col-span-2 City/State/ZIP row. Named container queries (@container/form + @max-[26rem]/form:) re-flow it by the form's own width, and floated labels snap to uppercase micro-legends that unify the grid.
## HTML
```html
<section class="tfl-16 w-full min-h-svh grid place-items-center bg-tfl16-bg px-5 py-12 font-tfl16-sans" aria-label="Multi-column form grid floating labels demo">
  <form class="@container/form flex w-full max-w-[560px] flex-col gap-[22px] rounded-3xl bg-white p-8 shadow-[0_24px_60px_-32px_oklch(0.3_0.06_265/0.4)] ring-1 ring-tfl16-ink/5" novalidate>
    <div class="flex flex-wrap items-baseline justify-between gap-2">
      <h3 class="text-2xl font-bold tracking-[-0.02em] text-tfl16-ink">Shipping address</h3>
      <span class="text-xs font-semibold tracking-[.12em] text-tfl16-mut uppercase">Step 1 of 2</span>
    </div>
    <div class="grid grid-cols-6 gap-4">
      <div class="relative col-span-3 @max-[26rem]/form:col-span-6">
        <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl16-line bg-white px-4 pt-[22px] pb-1.5 text-base text-tfl16-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl16-line-hover focus:border-tfl16-acc focus:ring-4 focus:ring-tfl16-acc/15" type="text" id="tfl-16-first" name="given-name" placeholder=" " autocomplete="given-name">
        <label class="pointer-events-none absolute left-4 top-1/2 max-w-[calc(100%_-_28px)] origin-left -translate-y-1/2 truncate text-[15px] text-tfl16-mut transition-[translate,scale,color] duration-[180ms] peer-focus:translate-y-[calc(-50%_-_14px)] peer-focus:scale-70 peer-focus:font-bold peer-focus:tracking-[.12em] peer-focus:text-tfl16-acc peer-focus:uppercase peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_14px)] peer-[:not(:placeholder-shown)]:scale-70 peer-[:not(:placeholder-shown)]:font-bold peer-[:not(:placeholder-shown)]:tracking-[.12em] peer-[:not(:placeholder-shown)]:uppercase motion-reduce:transition-none" for="tfl-16-first">First name</label>
      </div>
      <div class="relative col-span-3 @max-[26rem]/form:col-span-6">
        <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl16-line bg-white px-4 pt-[22px] pb-1.5 text-base text-tfl16-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl16-line-hover focus:border-tfl16-acc focus:ring-4 focus:ring-tfl16-acc/15" type="text" id="tfl-16-last" name="family-name" placeholder=" " autocomplete="family-name">
        <label class="pointer-events-none absolute left-4 top-1/2 max-w-[calc(100%_-_28px)] origin-left -translate-y-1/2 truncate text-[15px] text-tfl16-mut transition-[translate,scale,color] duration-[180ms] peer-focus:translate-y-[calc(-50%_-_14px)] peer-focus:scale-70 peer-focus:font-bold peer-focus:tracking-[.12em] peer-focus:text-tfl16-acc peer-focus:uppercase peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_14px)] peer-[:not(:placeholder-shown)]:scale-70 peer-[:not(:placeholder-shown)]:font-bold peer-[:not(:placeholder-shown)]:tracking-[.12em] peer-[:not(:placeholder-shown)]:uppercase motion-reduce:transition-none" for="tfl-16-last">Last name</label>
      </div>
      <div class="relative col-span-6">
        <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl16-line bg-white px-4 pt-[22px] pb-1.5 text-base text-tfl16-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl16-line-hover focus:border-tfl16-acc focus:ring-4 focus:ring-tfl16-acc/15" type="text" id="tfl-16-street" name="street-address" placeholder=" " autocomplete="street-address">
        <label class="pointer-events-none absolute left-4 top-1/2 max-w-[calc(100%_-_28px)] origin-left -translate-y-1/2 truncate text-[15px] text-tfl16-mut transition-[translate,scale,color] duration-[180ms] peer-focus:translate-y-[calc(-50%_-_14px)] peer-focus:scale-70 peer-focus:font-bold peer-focus:tracking-[.12em] peer-focus:text-tfl16-acc peer-focus:uppercase peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_14px)] peer-[:not(:placeholder-shown)]:scale-70 peer-[:not(:placeholder-shown)]:font-bold peer-[:not(:placeholder-shown)]:tracking-[.12em] peer-[:not(:placeholder-shown)]:uppercase motion-reduce:transition-none" for="tfl-16-street">Street address</label>
      </div>
      <div class="relative col-span-2 @max-[32rem]/form:col-span-6">
        <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl16-line bg-white px-4 pt-[22px] pb-1.5 text-base text-tfl16-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl16-line-hover focus:border-tfl16-acc focus:ring-4 focus:ring-tfl16-acc/15" type="text" id="tfl-16-city" name="address-level2" placeholder=" " autocomplete="address-level2">
        <label class="pointer-events-none absolute left-4 top-1/2 max-w-[calc(100%_-_28px)] origin-left -translate-y-1/2 truncate text-[15px] text-tfl16-mut transition-[translate,scale,color] duration-[180ms] peer-focus:translate-y-[calc(-50%_-_14px)] peer-focus:scale-70 peer-focus:font-bold peer-focus:tracking-[.12em] peer-focus:text-tfl16-acc peer-focus:uppercase peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_14px)] peer-[:not(:placeholder-shown)]:scale-70 peer-[:not(:placeholder-shown)]:font-bold peer-[:not(:placeholder-shown)]:tracking-[.12em] peer-[:not(:placeholder-shown)]:uppercase motion-reduce:transition-none" for="tfl-16-city">City</label>
      </div>
      <div class="relative col-span-2 @max-[32rem]/form:col-span-3 @max-[26rem]/form:col-span-6">
        <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl16-line bg-white px-4 pt-[22px] pb-1.5 text-base text-tfl16-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl16-line-hover focus:border-tfl16-acc focus:ring-4 focus:ring-tfl16-acc/15" type="text" id="tfl-16-state" name="address-level1" placeholder=" " autocomplete="address-level1">
        <label class="pointer-events-none absolute left-4 top-1/2 max-w-[calc(100%_-_28px)] origin-left -translate-y-1/2 truncate text-[15px] text-tfl16-mut transition-[translate,scale,color] duration-[180ms] peer-focus:translate-y-[calc(-50%_-_14px)] peer-focus:scale-70 peer-focus:font-bold peer-focus:tracking-[.12em] peer-focus:text-tfl16-acc peer-focus:uppercase peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_14px)] peer-[:not(:placeholder-shown)]:scale-70 peer-[:not(:placeholder-shown)]:font-bold peer-[:not(:placeholder-shown)]:tracking-[.12em] peer-[:not(:placeholder-shown)]:uppercase motion-reduce:transition-none" for="tfl-16-state">State</label>
      </div>
      <div class="relative col-span-2 @max-[32rem]/form:col-span-3 @max-[26rem]/form:col-span-6">
        <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl16-line bg-white px-4 pt-[22px] pb-1.5 text-base text-tfl16-ink tabular-nums outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl16-line-hover focus:border-tfl16-acc focus:ring-4 focus:ring-tfl16-acc/15" type="text" id="tfl-16-zip" name="postal-code" placeholder=" " inputmode="numeric" autocomplete="postal-code">
        <label class="pointer-events-none absolute left-4 top-1/2 max-w-[calc(100%_-_28px)] origin-left -translate-y-1/2 truncate text-[15px] text-tfl16-mut transition-[translate,scale,color] duration-[180ms] peer-focus:translate-y-[calc(-50%_-_14px)] peer-focus:scale-70 peer-focus:font-bold peer-focus:tracking-[.12em] peer-focus:text-tfl16-acc peer-focus:uppercase peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_14px)] peer-[:not(:placeholder-shown)]:scale-70 peer-[:not(:placeholder-shown)]:font-bold peer-[:not(:placeholder-shown)]:tracking-[.12em] peer-[:not(:placeholder-shown)]:uppercase motion-reduce:transition-none" for="tfl-16-zip">ZIP</label>
      </div>
    </div>
    <button class="min-h-[52px] cursor-pointer rounded-xl bg-tfl16-acc text-[15px] font-semibold text-white shadow-[0_10px_24px_-12px_var(--color-tfl16-acc)] transition-[filter,scale] duration-150 hover:brightness-115 active:scale-98 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tfl16-acc/50" type="button">Continue to payment</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfl16-bg: #f0f1f5;
  --color-tfl16-bg: oklch(0.96 0.006 270);
  --color-tfl16-ink: #191c2b;
  --color-tfl16-ink: oklch(0.22 0.03 270);
  --color-tfl16-mut: #62677c;
  --color-tfl16-mut: oklch(0.5 0.03 270);
  --color-tfl16-line: #d6d9e4;
  --color-tfl16-line: oklch(0.88 0.015 270);
  --color-tfl16-line-hover: #b4b9cc;
  --color-tfl16-line-hover: oklch(0.78 0.025 270);
  --color-tfl16-acc: #3d4fc4;
  --color-tfl16-acc: oklch(0.49 0.18 268);
  --font-tfl16-sans: 'IBM Plex Sans', system-ui, sans-serif;
}

.tfl-16 {
  width: 100%;
  min-height: 100svh;
}
```
