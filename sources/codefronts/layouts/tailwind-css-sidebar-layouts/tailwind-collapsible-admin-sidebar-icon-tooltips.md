---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-collapsible-admin-sidebar-icon-tooltips/"
title: "Tailwind Collapsible Admin Sidebar with Icon Tooltips"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "An enterprise rail that folds from 240px of labelled navigation down to a 64px icon strip, where every icon grows a tooltip on hover and keyboard focus."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Collapsible Admin Sidebar with Icon Tooltips
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-collapsible-admin-sidebar-icon-tooltips/

An enterprise rail that folds from 240px of labelled navigation down to a 64px icon strip, where every icon grows a tooltip on hover and keyboard focus. The port's move is has-checked: &mdash; the collapsed state is declared on each element that changes, instead of in a distant block of descendant selectors.
## HTML
```html
<section class="tsl-02 w-full h-svh min-h-svh grid grid-cols-[240px_1fr] transition-[grid-template-columns] duration-300 ease-out font-tsl02-sans bg-tsl02-bg text-tsl02-ink motion-reduce:transition-none">
  <input type="checkbox" id="tsl02-fold" class="sr-only peer">
  <aside class="flex flex-col gap-0.5 px-2.5 py-3.5 bg-tsl02-panel border-r border-tsl02-line overflow-visible">
    <label for="tsl02-fold" data-tooltip="Expand" class="group relative grid grid-cols-[auto_1fr] items-center gap-x-3 min-h-11 px-3 mb-2.5 rounded-[10px] text-sm font-medium text-tsl02-ink cursor-pointer transition-colors duration-200 hover:bg-tsl02-hover after:content-[attr(data-tooltip)] after:absolute after:left-[calc(100%+14px)] after:top-1/2 after:-translate-y-1/2 after:-translate-x-1 after:px-2.5 after:py-[7px] after:rounded-lg after:bg-tsl02-tip after:border after:border-tsl02-line after:text-tsl02-ink after:text-[12.5px] after:font-medium after:whitespace-nowrap after:shadow-[0_6px_18px_oklch(0_0_0/0.4)] after:opacity-0 after:pointer-events-none after:transition-[opacity,translate] after:duration-200 after:delay-150 after:z-10 motion-reduce:after:transition-opacity">
      <svg viewBox="0 0 24 24" aria-hidden="true" class="tsl-02-chev w-[18px] h-[18px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-300 motion-reduce:transition-none"><path d="m14 6-6 6 6 6"/></svg>
      <span class="tsl-02-label grid grid-cols-[1fr] overflow-hidden whitespace-nowrap opacity-100 transition-[grid-template-columns,opacity] duration-300"><span class="min-w-0 overflow-hidden">Collapse</span></span>
    </label>
    <nav aria-label="Admin" class="flex flex-col gap-0.5">
      <a href="#" aria-current="page" data-tooltip="Dashboard" class="relative grid grid-cols-[auto_1fr] items-center gap-x-3 min-h-11 px-3 rounded-[10px] text-sm font-medium text-tsl02-mut no-underline transition-colors duration-200 hover:text-tsl02-ink hover:bg-tsl02-hover aria-[current=page]:text-tsl02-ink aria-[current=page]:bg-tsl02-active focus-visible:outline-2 focus-visible:outline-tsl02-accent focus-visible:outline-offset-2 after:content-[attr(data-tooltip)] after:absolute after:left-[calc(100%+14px)] after:top-1/2 after:-translate-y-1/2 after:-translate-x-1 after:px-2.5 after:py-[7px] after:rounded-lg after:bg-tsl02-tip after:border after:border-tsl02-line after:text-tsl02-ink after:text-[12.5px] after:font-medium after:whitespace-nowrap after:shadow-[0_6px_18px_oklch(0_0_0/0.4)] after:opacity-0 after:pointer-events-none after:transition-[opacity,translate] after:duration-200 after:delay-150 after:z-10 motion-reduce:after:transition-opacity"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[18px] h-[18px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><rect x="3" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="3" y="13.5" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="13.5" width="7.5" height="7.5" rx="1.5"/></svg><span class="tsl-02-label grid grid-cols-[1fr] overflow-hidden whitespace-nowrap opacity-100 transition-[grid-template-columns,opacity] duration-300"><span class="min-w-0 overflow-hidden">Dashboard</span></span></a>
      <a href="#" data-tooltip="Users" class="relative grid grid-cols-[auto_1fr] items-center gap-x-3 min-h-11 px-3 rounded-[10px] text-sm font-medium text-tsl02-mut no-underline transition-colors duration-200 hover:text-tsl02-ink hover:bg-tsl02-hover focus-visible:outline-2 focus-visible:outline-tsl02-accent focus-visible:outline-offset-2 after:content-[attr(data-tooltip)] after:absolute after:left-[calc(100%+14px)] after:top-1/2 after:-translate-y-1/2 after:-translate-x-1 after:px-2.5 after:py-[7px] after:rounded-lg after:bg-tsl02-tip after:border after:border-tsl02-line after:text-tsl02-ink after:text-[12.5px] after:font-medium after:whitespace-nowrap after:shadow-[0_6px_18px_oklch(0_0_0/0.4)] after:opacity-0 after:pointer-events-none after:transition-[opacity,translate] after:duration-200 after:delay-150 after:z-10 motion-reduce:after:transition-opacity"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[18px] h-[18px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><circle cx="9" cy="8" r="3.5"/><path d="M3 20c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5m1-13.5a3.5 3.5 0 0 1 0 7"/></svg><span class="tsl-02-label grid grid-cols-[1fr] overflow-hidden whitespace-nowrap opacity-100 transition-[grid-template-columns,opacity] duration-300"><span class="min-w-0 overflow-hidden">Users</span></span></a>
      <a href="#" data-tooltip="Reports" class="relative grid grid-cols-[auto_1fr] items-center gap-x-3 min-h-11 px-3 rounded-[10px] text-sm font-medium text-tsl02-mut no-underline transition-colors duration-200 hover:text-tsl02-ink hover:bg-tsl02-hover focus-visible:outline-2 focus-visible:outline-tsl02-accent focus-visible:outline-offset-2 after:content-[attr(data-tooltip)] after:absolute after:left-[calc(100%+14px)] after:top-1/2 after:-translate-y-1/2 after:-translate-x-1 after:px-2.5 after:py-[7px] after:rounded-lg after:bg-tsl02-tip after:border after:border-tsl02-line after:text-tsl02-ink after:text-[12.5px] after:font-medium after:whitespace-nowrap after:shadow-[0_6px_18px_oklch(0_0_0/0.4)] after:opacity-0 after:pointer-events-none after:transition-[opacity,translate] after:duration-200 after:delay-150 after:z-10 motion-reduce:after:transition-opacity"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[18px] h-[18px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M4 20V10m6 10V4m6 16v-7"/></svg><span class="tsl-02-label grid grid-cols-[1fr] overflow-hidden whitespace-nowrap opacity-100 transition-[grid-template-columns,opacity] duration-300"><span class="min-w-0 overflow-hidden">Reports</span></span></a>
      <a href="#" data-tooltip="Audit log" class="relative grid grid-cols-[auto_1fr] items-center gap-x-3 min-h-11 px-3 rounded-[10px] text-sm font-medium text-tsl02-mut no-underline transition-colors duration-200 hover:text-tsl02-ink hover:bg-tsl02-hover focus-visible:outline-2 focus-visible:outline-tsl02-accent focus-visible:outline-offset-2 after:content-[attr(data-tooltip)] after:absolute after:left-[calc(100%+14px)] after:top-1/2 after:-translate-y-1/2 after:-translate-x-1 after:px-2.5 after:py-[7px] after:rounded-lg after:bg-tsl02-tip after:border after:border-tsl02-line after:text-tsl02-ink after:text-[12.5px] after:font-medium after:whitespace-nowrap after:shadow-[0_6px_18px_oklch(0_0_0/0.4)] after:opacity-0 after:pointer-events-none after:transition-[opacity,translate] after:duration-200 after:delay-150 after:z-10 motion-reduce:after:transition-opacity"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[18px] h-[18px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M8 6h13M8 12h13M8 18h13M3.5 6h.01M3.5 12h.01M3.5 18h.01"/></svg><span class="tsl-02-label grid grid-cols-[1fr] overflow-hidden whitespace-nowrap opacity-100 transition-[grid-template-columns,opacity] duration-300"><span class="min-w-0 overflow-hidden">Audit log</span></span></a>
      <a href="#" data-tooltip="Settings" class="relative grid grid-cols-[auto_1fr] items-center gap-x-3 min-h-11 px-3 rounded-[10px] text-sm font-medium text-tsl02-mut no-underline transition-colors duration-200 hover:text-tsl02-ink hover:bg-tsl02-hover focus-visible:outline-2 focus-visible:outline-tsl02-accent focus-visible:outline-offset-2 after:content-[attr(data-tooltip)] after:absolute after:left-[calc(100%+14px)] after:top-1/2 after:-translate-y-1/2 after:-translate-x-1 after:px-2.5 after:py-[7px] after:rounded-lg after:bg-tsl02-tip after:border after:border-tsl02-line after:text-tsl02-ink after:text-[12.5px] after:font-medium after:whitespace-nowrap after:shadow-[0_6px_18px_oklch(0_0_0/0.4)] after:opacity-0 after:pointer-events-none after:transition-[opacity,translate] after:duration-200 after:delay-150 after:z-10 motion-reduce:after:transition-opacity"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[18px] h-[18px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><circle cx="12" cy="12" r="3"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3M4.9 4.9l2.1 2.1m10 10 2.1 2.1m0-14.2-2.1 2.1m-10 10-2.1 2.1"/></svg><span class="tsl-02-label grid grid-cols-[1fr] overflow-hidden whitespace-nowrap opacity-100 transition-[grid-template-columns,opacity] duration-300"><span class="min-w-0 overflow-hidden">Settings</span></span></a>
    </nav>
  </aside>
  <main class="p-8 overflow-y-auto [scrollbar-gutter:stable]">
    <h1 class="text-[22px] font-semibold leading-tight mb-2.5">User management</h1>
    <p class="max-w-[44ch] text-sm leading-relaxed text-tsl02-mut text-pretty">Toggle the chevron &mdash; labels fold into a 0fr grid track and tooltips take over.</p>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl02-bg: #121319;
  --color-tsl02-bg: oklch(0.13 0.015 275);
  --color-tsl02-panel: #181a21;
  --color-tsl02-panel: oklch(0.16 0.02 275);
  --color-tsl02-tip: #24262f;
  --color-tsl02-tip: oklch(0.24 0.02 275);
  --color-tsl02-ink: #e8e9ee;
  --color-tsl02-ink: oklch(0.92 0.005 275);
  --color-tsl02-mut: #94969f;
  --color-tsl02-mut: oklch(0.64 0.012 275);
  --color-tsl02-line: #383a44;
  --color-tsl02-line: oklch(0.27 0.02 275);
  --color-tsl02-accent: #8a7cf0;
  --color-tsl02-accent: oklch(0.68 0.17 275);
  --color-tsl02-hover: rgb(232 233 238 / 0.07);
  --color-tsl02-hover: color-mix(in oklab, oklch(0.92 0.005 275) 7%, transparent);
  --color-tsl02-active: rgb(138 124 240 / 0.2);
  --color-tsl02-active: color-mix(in oklab, oklch(0.68 0.17 275) 20%, transparent);
  --font-tsl02-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tsl-02 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
/* STATE — one checkbox at the shell root, read by the shell, the label cells,
   the chevron and the tooltips. */

.tsl-02:has(#tsl02-fold:checked) {
  grid-template-columns: 64px 1fr;
}

#tsl02-fold:checked ~ aside .tsl-02-label {
  grid-template-columns: 0fr;
  opacity: 0;
}

#tsl02-fold:checked ~ aside .tsl-02-chev {
  rotate: 180deg;
}

#tsl02-fold:checked ~ aside [data-tooltip]:hover::after,
#tsl02-fold:checked ~ aside [data-tooltip]:focus-visible::after {
  opacity: 1;
  translate: 0;
}

#tsl02-fold:focus-visible ~ aside label[for="tsl02-fold"] {
  outline: 2px solid var(--color-tsl02-accent);
  outline-offset: 2px;
}
/* The tooltip pill must escape the rail; the rail therefore never clips. */

.tsl-02 aside {
  overflow: visible;
}
```
