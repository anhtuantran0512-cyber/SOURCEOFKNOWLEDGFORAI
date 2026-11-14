---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-animated-collapsible-sidebar-icon-only-mode/"
title: "Tailwind Animated Collapsible Sidebar with Icon-Only Mode"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The polished shrink-to-rail: 248px of labelled navigation eases to a 68px icon rail in one motion, with labels fading before the track finishes on collapse…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Collapsible Sidebar with Icon-Only Mode
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-animated-collapsible-sidebar-icon-only-mode/

The polished shrink-to-rail: 248px of labelled navigation eases to a 68px icon rail in one motion, with labels fading before the track finishes on collapse and after it on expand. That asymmetric stagger is the whole demo, and in Tailwind it is two delay utilities.
## HTML
```html
<section class="tsl-06 w-full h-svh min-h-svh grid grid-cols-[248px_1fr] transition-[grid-template-columns] duration-300 ease-[cubic-bezier(.4,0,.2,1)] font-tsl06-sans bg-tsl06-bg text-tsl06-ink motion-reduce:transition-none">
  <input type="checkbox" id="tsl06-c" class="sr-only peer">
  <aside class="flex flex-col gap-0.5 px-2.5 py-4 bg-tsl06-panel border-r border-tsl06-line overflow-hidden">
    <div class="grid grid-cols-[28px_1fr] items-center gap-2.5 px-2.5 pt-1 pb-[18px] whitespace-nowrap">
      <span aria-hidden="true" class="w-7 h-7 rounded-[9px] bg-[conic-gradient(from_120deg,var(--color-tsl06-accent),oklch(0.65_0.14_300))]"></span>
      <span class="text-[15px] font-bold tracking-tight opacity-100 transition-opacity duration-[180ms] delay-[120ms]">Northwind</span>
    </div>
    <nav aria-label="Main" class="flex flex-col gap-0.5">
      <a href="#" aria-current="page" class="grid grid-cols-[20px_1fr] items-center gap-3 min-h-11 px-3.5 rounded-[10px] text-sm font-medium whitespace-nowrap text-tsl06-mut no-underline transition-colors duration-200 hover:text-tsl06-ink hover:bg-tsl06-hover aria-[current=page]:text-tsl06-accent aria-[current=page]:bg-tsl06-tint focus-visible:outline-2 focus-visible:outline-tsl06-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[19px] h-[19px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><rect x="3" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="3" y="13.5" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="13.5" width="7.5" height="7.5" rx="1.5"/></svg><span class="tsl-06-label opacity-100 transition-opacity duration-[180ms] delay-[120ms]">Dashboard</span></a>
      <a href="#" class="grid grid-cols-[20px_1fr] items-center gap-3 min-h-11 px-3.5 rounded-[10px] text-sm font-medium whitespace-nowrap text-tsl06-mut no-underline transition-colors duration-200 hover:text-tsl06-ink hover:bg-tsl06-hover focus-visible:outline-2 focus-visible:outline-tsl06-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[19px] h-[19px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M21 12a9 9 0 1 1-9-9"/><path d="M12 3a9 9 0 0 1 9 9h-9z"/></svg><span class="tsl-06-label opacity-100 transition-opacity duration-[180ms] delay-[120ms]">Insights</span></a>
      <a href="#" class="grid grid-cols-[20px_1fr] items-center gap-3 min-h-11 px-3.5 rounded-[10px] text-sm font-medium whitespace-nowrap text-tsl06-mut no-underline transition-colors duration-200 hover:text-tsl06-ink hover:bg-tsl06-hover focus-visible:outline-2 focus-visible:outline-tsl06-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[19px] h-[19px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M20 7 12 3 4 7m16 0v10l-8 4-8-4V7m16 0-8 4M4 7l8 4m0 0v10"/></svg><span class="tsl-06-label opacity-100 transition-opacity duration-[180ms] delay-[120ms]">Inventory</span></a>
      <a href="#" class="grid grid-cols-[20px_1fr] items-center gap-3 min-h-11 px-3.5 rounded-[10px] text-sm font-medium whitespace-nowrap text-tsl06-mut no-underline transition-colors duration-200 hover:text-tsl06-ink hover:bg-tsl06-hover focus-visible:outline-2 focus-visible:outline-tsl06-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[19px] h-[19px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><circle cx="9" cy="8" r="3.5"/><path d="M3 20c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5m1-13.5a3.5 3.5 0 0 1 0 7"/></svg><span class="tsl-06-label opacity-100 transition-opacity duration-[180ms] delay-[120ms]">Team</span></a>
      <a href="#" class="grid grid-cols-[20px_1fr] items-center gap-3 min-h-11 px-3.5 rounded-[10px] text-sm font-medium whitespace-nowrap text-tsl06-mut no-underline transition-colors duration-200 hover:text-tsl06-ink hover:bg-tsl06-hover focus-visible:outline-2 focus-visible:outline-tsl06-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[19px] h-[19px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><circle cx="12" cy="12" r="3"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3M4.9 4.9l2.1 2.1m10 10 2.1 2.1m0-14.2-2.1 2.1m-10 10-2.1 2.1"/></svg><span class="tsl-06-label opacity-100 transition-opacity duration-[180ms] delay-[120ms]">Settings</span></a>
    </nav>
    <label for="tsl06-c" class="mt-auto grid grid-cols-[20px_1fr] items-center gap-3 min-h-11 px-3.5 rounded-[10px] text-sm font-medium whitespace-nowrap text-tsl06-mut cursor-pointer transition-colors duration-200 hover:text-tsl06-ink hover:bg-tsl06-hover">
      <svg viewBox="0 0 24 24" aria-hidden="true" class="tsl-06-chev w-[19px] h-[19px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-300 ease-[cubic-bezier(.4,0,.2,1)] motion-reduce:transition-none"><path d="m14 6-6 6 6 6"/></svg>
      <span class="tsl-06-label opacity-100 transition-opacity duration-[180ms] delay-[120ms]">Collapse</span>
    </label>
  </aside>
  <main class="p-8 overflow-y-auto [scrollbar-gutter:stable]">
    <h1 class="text-[22px] font-semibold leading-tight mb-2.5">Dashboard</h1>
    <p class="max-w-[46ch] text-sm leading-relaxed text-tsl06-mut text-pretty">Watch the choreography: on collapse the labels fade first, then the rail narrows. On expand, the reverse.</p>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl06-bg: #fcfcfd;
  --color-tsl06-bg: oklch(0.99 0.002 250);
  --color-tsl06-panel: #f3f4f7;
  --color-tsl06-panel: oklch(0.965 0.006 250);
  --color-tsl06-ink: #363b44;
  --color-tsl06-ink: oklch(0.25 0.02 250);
  --color-tsl06-mut: #71767f;
  --color-tsl06-mut: oklch(0.5 0.015 250);
  --color-tsl06-line: #dfe1e6;
  --color-tsl06-line: oklch(0.89 0.008 250);
  --color-tsl06-accent: #3f63c8;
  --color-tsl06-accent: oklch(0.52 0.16 250);
  --color-tsl06-hover: rgb(54 59 68 / 0.06);
  --color-tsl06-hover: color-mix(in oklab, oklch(0.25 0.02 250) 6%, transparent);
  --color-tsl06-tint: rgb(63 99 200 / 0.12);
  --color-tsl06-tint: color-mix(in oklab, oklch(0.52 0.16 250) 12%, transparent);
  --font-tsl06-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tsl-06 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: light;
}
/* STATE — collapse, plus the asymmetric stagger: labels fade with no delay on
   the way out, and wait for the rail on the way back in. */

.tsl-06:has(#tsl06-c:checked) {
  grid-template-columns: 68px 1fr;
}

#tsl06-c:checked ~ aside .tsl-06-label {
  opacity: 0;
  transition-delay: 0ms;
}

#tsl06-c:checked ~ aside .tsl-06-chev {
  rotate: 180deg;
}

#tsl06-c:focus-visible ~ aside label[for="tsl06-c"] {
  outline: 2px solid var(--color-tsl06-accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .tsl-06 * {
    transition-duration: 1ms !important;
    transition-delay: 0ms !important;
  }
}
```
