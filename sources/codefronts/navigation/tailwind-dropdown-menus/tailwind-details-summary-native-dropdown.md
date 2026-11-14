---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-details-summary-native-dropdown/"
title: "Tailwind Details Summary Native Dropdown"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "The dropdown the browser already ships."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Details Summary Native Dropdown
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-details-summary-native-dropdown/

The dropdown the browser already ships. <details> toggles itself, is keyboard operable for free, and v4 reads its state with the open: variant — so a click-to-open menu with zero JavaScript is four utilities and a marker reset.
## HTML
```html
<section class="tdd-09 w-full min-h-svh grid place-items-center bg-linear-[160deg,var(--color-tdd09-bg1),var(--color-tdd09-bg2)] font-tdd09-sans text-tdd09-ink px-5 py-10" aria-label="Details summary native dropdown demo">
  <div class="flex w-[min(640px,100%)] flex-col items-center gap-4">
    <nav class="flex w-full justify-center gap-3 rounded-xl border border-tdd09-edge bg-white p-2.5 shadow-[0_4px_16px_oklch(0_0_0/0.06)]" aria-label="Primary">
      <details class="group/d relative max-w-45 flex-1">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-2 rounded-lg px-3.5 py-2.5 text-sm font-semibold text-tdd09-ink select-none transition-colors duration-150 hover:bg-tdd09-tint hover:text-tdd09-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd09-acc open:bg-tdd09-tint open:text-tdd09-acc [&::-webkit-details-marker]:hidden">
          <span class="font-tdd09-serif text-[15px]">Discover</span>
          <span class="relative block size-4 shrink-0 overflow-hidden before:absolute before:top-1/2 before:left-[3px] before:h-[1.5px] before:w-[7px] before:-translate-y-1/2 before:rotate-45 before:bg-current before:transition-transform before:duration-200 before:content-[''] after:absolute after:top-1/2 after:right-[3px] after:h-[1.5px] after:w-[7px] after:-translate-y-1/2 after:-rotate-45 after:bg-current after:transition-transform after:duration-200 after:content-[''] group-open/d:before:-rotate-45 group-open/d:after:rotate-45" aria-hidden="true"></span>
        </summary>
        <div class="absolute top-[calc(100%+8px)] left-0 z-10 flex max-h-0 w-full min-w-40 flex-col gap-0.5 overflow-hidden rounded-[10px] border border-tdd09-edge bg-white p-1.5 opacity-0 shadow-[0_8px_24px_oklch(0_0_0/0.1)] transition-[max-height,opacity] duration-340 [[open]>&]:max-h-100 [[open]>&]:opacity-100 motion-reduce:transition-none">
          <a href="#destinations" class="block rounded-[7px] px-3 py-2.5 font-tdd09-serif text-[13.5px] font-medium text-tdd09-ink no-underline transition-colors duration-150 hover:bg-tdd09-tint hover:text-tdd09-acc focus-visible:bg-tdd09-tint focus-visible:outline-none">Destinations</a>
          <a href="#experiences" class="block rounded-[7px] px-3 py-2.5 font-tdd09-serif text-[13.5px] font-medium text-tdd09-ink no-underline transition-colors duration-150 hover:bg-tdd09-tint hover:text-tdd09-acc focus-visible:bg-tdd09-tint focus-visible:outline-none">Experiences</a>
          <a href="#collections" class="block rounded-[7px] px-3 py-2.5 font-tdd09-serif text-[13.5px] font-medium text-tdd09-ink no-underline transition-colors duration-150 hover:bg-tdd09-tint hover:text-tdd09-acc focus-visible:bg-tdd09-tint focus-visible:outline-none">Collections</a>
          <a href="#guides" class="block rounded-[7px] px-3 py-2.5 font-tdd09-serif text-[13.5px] font-medium text-tdd09-ink no-underline transition-colors duration-150 hover:bg-tdd09-tint hover:text-tdd09-acc focus-visible:bg-tdd09-tint focus-visible:outline-none">Guides</a>
        </div>
      </details>
      <details class="group/d relative max-w-45 flex-1">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-2 rounded-lg px-3.5 py-2.5 text-sm font-semibold text-tdd09-ink select-none transition-colors duration-150 hover:bg-tdd09-tint hover:text-tdd09-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd09-acc open:bg-tdd09-tint open:text-tdd09-acc [&::-webkit-details-marker]:hidden">
          <span class="font-tdd09-serif text-[15px]">Plan</span>
          <span class="relative block size-4 shrink-0 overflow-hidden before:absolute before:top-1/2 before:left-[3px] before:h-[1.5px] before:w-[7px] before:-translate-y-1/2 before:rotate-45 before:bg-current before:transition-transform before:duration-200 before:content-[''] after:absolute after:top-1/2 after:right-[3px] after:h-[1.5px] after:w-[7px] after:-translate-y-1/2 after:-rotate-45 after:bg-current after:transition-transform after:duration-200 after:content-[''] group-open/d:before:-rotate-45 group-open/d:after:rotate-45" aria-hidden="true"></span>
        </summary>
        <div class="absolute top-[calc(100%+8px)] left-0 z-10 flex max-h-0 w-full min-w-40 flex-col gap-0.5 overflow-hidden rounded-[10px] border border-tdd09-edge bg-white p-1.5 opacity-0 shadow-[0_8px_24px_oklch(0_0_0/0.1)] transition-[max-height,opacity] duration-340 [[open]>&]:max-h-100 [[open]>&]:opacity-100 motion-reduce:transition-none">
          <a href="#trip-builder" class="block rounded-[7px] px-3 py-2.5 font-tdd09-serif text-[13.5px] font-medium text-tdd09-ink no-underline transition-colors duration-150 hover:bg-tdd09-tint hover:text-tdd09-acc focus-visible:bg-tdd09-tint focus-visible:outline-none">Trip Builder</a>
          <a href="#booking" class="block rounded-[7px] px-3 py-2.5 font-tdd09-serif text-[13.5px] font-medium text-tdd09-ink no-underline transition-colors duration-150 hover:bg-tdd09-tint hover:text-tdd09-acc focus-visible:bg-tdd09-tint focus-visible:outline-none">Booking</a>
          <a href="#itineraries" class="block rounded-[7px] px-3 py-2.5 font-tdd09-serif text-[13.5px] font-medium text-tdd09-ink no-underline transition-colors duration-150 hover:bg-tdd09-tint hover:text-tdd09-acc focus-visible:bg-tdd09-tint focus-visible:outline-none">Itineraries</a>
        </div>
      </details>
      <details class="group/d relative max-w-45 flex-1">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-2 rounded-lg px-3.5 py-2.5 text-sm font-semibold text-tdd09-ink select-none transition-colors duration-150 hover:bg-tdd09-tint hover:text-tdd09-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd09-acc open:bg-tdd09-tint open:text-tdd09-acc [&::-webkit-details-marker]:hidden">
          <span class="font-tdd09-serif text-[15px]">Journal</span>
          <span class="relative block size-4 shrink-0 overflow-hidden before:absolute before:top-1/2 before:left-[3px] before:h-[1.5px] before:w-[7px] before:-translate-y-1/2 before:rotate-45 before:bg-current before:transition-transform before:duration-200 before:content-[''] after:absolute after:top-1/2 after:right-[3px] after:h-[1.5px] after:w-[7px] after:-translate-y-1/2 after:-rotate-45 after:bg-current after:transition-transform after:duration-200 after:content-[''] group-open/d:before:-rotate-45 group-open/d:after:rotate-45" aria-hidden="true"></span>
        </summary>
        <div class="absolute top-[calc(100%+8px)] left-0 z-10 flex max-h-0 w-full min-w-40 flex-col gap-0.5 overflow-hidden rounded-[10px] border border-tdd09-edge bg-white p-1.5 opacity-0 shadow-[0_8px_24px_oklch(0_0_0/0.1)] transition-[max-height,opacity] duration-340 [[open]>&]:max-h-100 [[open]>&]:opacity-100 motion-reduce:transition-none">
          <a href="#stories" class="block rounded-[7px] px-3 py-2.5 font-tdd09-serif text-[13.5px] font-medium text-tdd09-ink no-underline transition-colors duration-150 hover:bg-tdd09-tint hover:text-tdd09-acc focus-visible:bg-tdd09-tint focus-visible:outline-none">Stories</a>
          <a href="#photography" class="block rounded-[7px] px-3 py-2.5 font-tdd09-serif text-[13.5px] font-medium text-tdd09-ink no-underline transition-colors duration-150 hover:bg-tdd09-tint hover:text-tdd09-acc focus-visible:bg-tdd09-tint focus-visible:outline-none">Photography</a>
          <a href="#reviews" class="block rounded-[7px] px-3 py-2.5 font-tdd09-serif text-[13.5px] font-medium text-tdd09-ink no-underline transition-colors duration-150 hover:bg-tdd09-tint hover:text-tdd09-acc focus-visible:bg-tdd09-tint focus-visible:outline-none">Reviews</a>
        </div>
      </details>
    </nav>
    <p class="text-xs italic text-tdd09-mut">Click any nav item to toggle &mdash; no JavaScript on this one</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdd09-bg1: #fffbeb;
  --color-tdd09-bg1: oklch(0.98 0.02 95);
  --color-tdd09-bg2: #fef3c7;
  --color-tdd09-bg2: oklch(0.95 0.06 92);
  --color-tdd09-ink: #1c1917;
  --color-tdd09-ink: oklch(0.22 0.01 60);
  --color-tdd09-mut: #78716c;
  --color-tdd09-mut: oklch(0.56 0.01 60);
  --color-tdd09-edge: #e7e5e4;
  --color-tdd09-edge: oklch(0.91 0.005 60);
  --color-tdd09-tint: #fef3c7;
  --color-tdd09-tint: oklch(0.95 0.06 92);
  --color-tdd09-acc: #b45309;
  --color-tdd09-acc: oklch(0.53 0.14 55);
  --font-tdd09-sans: 'Source Sans 3', system-ui, sans-serif;
  --font-tdd09-serif: 'Lora', Georgia, serif;
}

.tdd-09 {
  width: 100%;
  min-height: 100svh;
}

.tdd-09 ::selection {
  background: var(--color-tdd09-acc);
  color: #fffbeb;
}
```
