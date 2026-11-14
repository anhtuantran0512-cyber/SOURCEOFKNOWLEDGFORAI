---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-sliding-active-indicator-sidebar-target/"
title: "Tailwind Sliding Active Indicator Sidebar with CSS :target"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The sliding active bar &mdash; the effect teams install a motion library for &mdash; with zero JavaScript."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sliding Active Indicator Sidebar with CSS :target
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-sliding-active-indicator-sidebar-target/

The sliding active bar &mdash; the effect teams install a motion library for &mdash; with zero JavaScript. Links target anchors, :target identifies the section, and one indicator element transitions between stops computed from a single row-height variable.
## HTML
```html
<section class="tsl-23 w-full h-svh min-h-svh grid grid-cols-[224px_1fr] [--row:46px] font-tsl23-sans bg-tsl23-bg text-tsl23-ink">
  <aside aria-label="Sections" class="relative bg-tsl23-panel border-r border-tsl23-line px-3 py-[18px]">
    <span aria-hidden="true" class="tsl-23-ind absolute left-1 top-[18px] mt-2 w-[3px] h-7 rounded bg-tsl23-accent shadow-[0_0_12px_var(--color-tsl23-glow)] translate-y-0 transition-transform duration-[320ms] ease-[cubic-bezier(.5,0,.2,1.15)] motion-reduce:transition-none"></span>
    <nav class="flex flex-col gap-0.5">
      <a href="#tsl23-inbox" class="flex items-center h-11 px-4 rounded-[10px] text-sm font-medium text-tsl23-mut no-underline transition-colors duration-200 hover:text-tsl23-ink hover:bg-tsl23-hover focus-visible:outline-2 focus-visible:outline-tsl23-accent focus-visible:outline-offset-2">Inbox</a>
      <a href="#tsl23-today" class="flex items-center h-11 px-4 rounded-[10px] text-sm font-medium text-tsl23-mut no-underline transition-colors duration-200 hover:text-tsl23-ink hover:bg-tsl23-hover focus-visible:outline-2 focus-visible:outline-tsl23-accent focus-visible:outline-offset-2">Today</a>
      <a href="#tsl23-upcoming" class="flex items-center h-11 px-4 rounded-[10px] text-sm font-medium text-tsl23-mut no-underline transition-colors duration-200 hover:text-tsl23-ink hover:bg-tsl23-hover focus-visible:outline-2 focus-visible:outline-tsl23-accent focus-visible:outline-offset-2">Upcoming</a>
      <a href="#tsl23-someday" class="flex items-center h-11 px-4 rounded-[10px] text-sm font-medium text-tsl23-mut no-underline transition-colors duration-200 hover:text-tsl23-ink hover:bg-tsl23-hover focus-visible:outline-2 focus-visible:outline-tsl23-accent focus-visible:outline-offset-2">Someday</a>
      <a href="#tsl23-logbook" class="flex items-center h-11 px-4 rounded-[10px] text-sm font-medium text-tsl23-mut no-underline transition-colors duration-200 hover:text-tsl23-ink hover:bg-tsl23-hover focus-visible:outline-2 focus-visible:outline-tsl23-accent focus-visible:outline-offset-2">Logbook</a>
    </nav>
  </aside>
  <div class="overflow-y-auto p-8 grid gap-10 content-start [scrollbar-gutter:stable]">
    <section id="tsl23-inbox" class="scroll-mt-6"><h1 class="mb-2 text-[21px] font-semibold leading-tight">Inbox</h1><p class="max-w-[48ch] text-sm leading-relaxed text-tsl23-mut text-pretty">Click the menu &mdash; the accent bar glides between items. URL fragments plus <code class="font-tsl23-mono text-[12.5px]">:target</code> and <code class="font-tsl23-mono text-[12.5px]">:has()</code>, no script.</p></section>
    <section id="tsl23-today" class="scroll-mt-6"><h1 class="mb-2 text-[21px] font-semibold leading-tight">Today</h1><p class="max-w-[48ch] text-sm leading-relaxed text-tsl23-mut text-pretty">Three tasks scheduled.</p></section>
    <section id="tsl23-upcoming" class="scroll-mt-6"><h1 class="mb-2 text-[21px] font-semibold leading-tight">Upcoming</h1><p class="max-w-[48ch] text-sm leading-relaxed text-tsl23-mut text-pretty">Planning horizon: two weeks.</p></section>
    <section id="tsl23-someday" class="scroll-mt-6"><h1 class="mb-2 text-[21px] font-semibold leading-tight">Someday</h1><p class="max-w-[48ch] text-sm leading-relaxed text-tsl23-mut text-pretty">Ideas parked without guilt.</p></section>
    <section id="tsl23-logbook" class="scroll-mt-6"><h1 class="mb-2 text-[21px] font-semibold leading-tight">Logbook</h1><p class="max-w-[48ch] text-sm leading-relaxed text-tsl23-mut text-pretty">Completed items, newest first.</p></section>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl23-bg: #101613;
  --color-tsl23-bg: oklch(0.13 0.012 145);
  --color-tsl23-panel: #161f1a;
  --color-tsl23-panel: oklch(0.17 0.015 145);
  --color-tsl23-ink: #e8f0ea;
  --color-tsl23-ink: oklch(0.94 0.005 145);
  --color-tsl23-mut: #929d95;
  --color-tsl23-mut: oklch(0.64 0.012 145);
  --color-tsl23-line: #333e37;
  --color-tsl23-line: oklch(0.28 0.016 145);
  --color-tsl23-accent: #67e29a;
  --color-tsl23-accent: oklch(0.8 0.16 150);
  --color-tsl23-glow: rgb(103 226 154 / 0.55);
  --color-tsl23-glow: color-mix(in oklab, oklch(0.8 0.16 150) 55%, transparent);
  --color-tsl23-hover: rgb(232 240 234 / 0.06);
  --color-tsl23-hover: color-mix(in oklab, oklch(0.94 0.005 145) 6%, transparent);
  --color-tsl23-tint: rgb(103 226 154 / 0.12);
  --color-tsl23-tint: color-mix(in oklab, oklch(0.8 0.16 150) 12%, transparent);
  --font-tsl23-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tsl23-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tsl-23 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
/* Nothing is :target on first paint — park the resting highlight on item one
   so the default state looks intentional rather than empty. */

.tsl-23:not(:has(:target)) nav a:first-child {
  color: var(--color-tsl23-ink);
  background: var(--color-tsl23-tint);
}
/* STATE — indicator stops and the matching highlight, both derived from --row. */

.tsl-23:has(#tsl23-today:target) .tsl-23-ind {
  translate: 0 var(--row);
}

.tsl-23:has(#tsl23-upcoming:target) .tsl-23-ind {
  translate: 0 calc(var(--row) * 2);
}

.tsl-23:has(#tsl23-someday:target) .tsl-23-ind {
  translate: 0 calc(var(--row) * 3);
}

.tsl-23:has(#tsl23-logbook:target) .tsl-23-ind {
  translate: 0 calc(var(--row) * 4);
}

.tsl-23:has(#tsl23-inbox:target) a[href="#tsl23-inbox"],
.tsl-23:has(#tsl23-today:target) a[href="#tsl23-today"],
.tsl-23:has(#tsl23-upcoming:target) a[href="#tsl23-upcoming"],
.tsl-23:has(#tsl23-someday:target) a[href="#tsl23-someday"],
.tsl-23:has(#tsl23-logbook:target) a[href="#tsl23-logbook"] {
  color: var(--color-tsl23-ink);
  background: var(--color-tsl23-tint);
}
```
