---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-responsive-sidebar-bottom-navigation-switch/"
title: "Tailwind Responsive Sidebar to Bottom Navigation Switch Layout"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "One <nav>, two personalities: under 768px an iOS-style bottom tab bar with safe-area padding, at and above it the same markup stands up into a left sidebar."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Responsive Sidebar to Bottom Navigation Switch Layout
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-responsive-sidebar-bottom-navigation-switch/

One <nav>, two personalities: under 768px an iOS-style bottom tab bar with safe-area padding, at and above it the same markup stands up into a left sidebar. No duplicate nav trees, no resize listeners &mdash; the breakpoint prefix does all of it.
## HTML
```html
<section class="tsl-04 w-full h-svh min-h-svh grid grid-rows-[1fr_auto] md:grid-cols-[248px_1fr] md:grid-rows-1 font-tsl04-sans bg-tsl04-bg text-tsl04-ink">
  <nav aria-label="Primary" class="order-2 md:order-1 flex flex-row md:flex-col md:gap-0.5 md:justify-start bg-tsl04-panel border-t md:border-t-0 md:border-r border-tsl04-line px-2 pt-1.5 pb-[calc(0.375rem+env(safe-area-inset-bottom,0px))] md:px-3 md:py-[18px]">
    <a href="#" aria-current="page" class="flex-1 md:flex-none flex flex-col md:flex-row items-center justify-center md:justify-start gap-[3px] md:gap-3 min-h-12 md:min-h-11 md:px-3.5 rounded-xl text-[10.5px] md:text-sm font-medium text-tsl04-mut no-underline transition-colors duration-200 hover:text-tsl04-ink aria-[current=page]:text-tsl04-accent aria-[current=page]:bg-tsl04-tint focus-visible:outline-2 focus-visible:outline-tsl04-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[21px] h-[21px] shrink-0 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M3 10.5 12 3l9 7.5M5.5 9.5V21h13V9.5"/></svg><span>Home</span></a>
    <a href="#" class="flex-1 md:flex-none flex flex-col md:flex-row items-center justify-center md:justify-start gap-[3px] md:gap-3 min-h-12 md:min-h-11 md:px-3.5 rounded-xl text-[10.5px] md:text-sm font-medium text-tsl04-mut no-underline transition-colors duration-200 hover:text-tsl04-ink focus-visible:outline-2 focus-visible:outline-tsl04-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[21px] h-[21px] shrink-0 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><span>Search</span></a>
    <a href="#" class="flex-1 md:flex-none flex flex-col md:flex-row items-center justify-center md:justify-start gap-[3px] md:gap-3 min-h-12 md:min-h-11 md:px-3.5 rounded-xl text-[10.5px] md:text-sm font-medium text-tsl04-mut no-underline transition-colors duration-200 hover:text-tsl04-ink focus-visible:outline-2 focus-visible:outline-tsl04-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[21px] h-[21px] shrink-0 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><rect x="3" y="4" width="18" height="16" rx="3"/><path d="M3 9h18M8 2v4m8-4v4"/></svg><span>Bookings</span></a>
    <a href="#" class="flex-1 md:flex-none flex flex-col md:flex-row items-center justify-center md:justify-start gap-[3px] md:gap-3 min-h-12 md:min-h-11 md:px-3.5 rounded-xl text-[10.5px] md:text-sm font-medium text-tsl04-mut no-underline transition-colors duration-200 hover:text-tsl04-ink focus-visible:outline-2 focus-visible:outline-tsl04-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[21px] h-[21px] shrink-0 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M18 8a6 6 0 1 0-12 0c0 7-3 8-3 8h18s-3-1-3-8m-4.3 11a2 2 0 0 1-3.4 0"/></svg><span>Alerts</span></a>
    <a href="#" class="flex-1 md:flex-none flex flex-col md:flex-row items-center justify-center md:justify-start gap-[3px] md:gap-3 min-h-12 md:min-h-11 md:px-3.5 rounded-xl text-[10.5px] md:text-sm font-medium text-tsl04-mut no-underline transition-colors duration-200 hover:text-tsl04-ink focus-visible:outline-2 focus-visible:outline-tsl04-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[21px] h-[21px] shrink-0 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-3.9 3.6-6.5 8-6.5s8 2.6 8 6.5"/></svg><span>Profile</span></a>
  </nav>
  <main class="order-1 md:order-2 overflow-y-auto p-7 [scrollbar-gutter:stable]">
    <h1 class="text-[22px] font-semibold leading-tight mb-2.5">Today</h1>
    <p class="max-w-[46ch] text-sm leading-relaxed text-tsl04-mut text-pretty">Resize the viewport &mdash; under 768px this same nav element becomes a bottom tab bar with safe-area padding.</p>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl04-bg: #121519;
  --color-tsl04-bg: oklch(0.13 0.015 250);
  --color-tsl04-panel: #191d23;
  --color-tsl04-panel: oklch(0.17 0.02 250);
  --color-tsl04-ink: #e9ebef;
  --color-tsl04-ink: oklch(0.93 0.005 250);
  --color-tsl04-mut: #8f939c;
  --color-tsl04-mut: oklch(0.62 0.012 250);
  --color-tsl04-line: #383d45;
  --color-tsl04-line: oklch(0.28 0.02 250);
  --color-tsl04-accent: #57c9df;
  --color-tsl04-accent: oklch(0.75 0.14 200);
  --color-tsl04-tint: rgb(87 201 223 / 0.14);
  --color-tsl04-tint: color-mix(in oklab, oklch(0.75 0.14 200) 14%, transparent);
  --font-tsl04-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tsl-04 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
```
