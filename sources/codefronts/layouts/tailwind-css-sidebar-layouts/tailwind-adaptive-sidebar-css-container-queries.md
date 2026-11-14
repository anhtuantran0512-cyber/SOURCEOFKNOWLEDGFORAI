---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-adaptive-sidebar-css-container-queries/"
title: "Tailwind Adaptive Sidebar Layout Using CSS Container Queries"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "A sidebar that responds to its own width, not the viewport."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Adaptive Sidebar Layout Using CSS Container Queries
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-adaptive-sidebar-css-container-queries/

A sidebar that responds to its own width, not the viewport. Drag the handle and the nav morphs through three densities &mdash; full, labels-only, icon rail &mdash; entirely from container queries, which v4 exposes as ordinary variants.
## HTML
```html
<section class="tsl-29 w-full h-svh min-h-svh flex font-tsl29-sans bg-tsl29-bg text-tsl29-ink">
  <div class="@container/rail relative flex-none w-[264px] min-w-[76px] max-w-[340px] resize-x overflow-auto bg-tsl29-panel border-r border-tsl29-line">
    <aside aria-label="Library" class="min-h-full px-2.5 py-4">
      <div class="flex items-center gap-2.5 px-2.5 pt-1 pb-4 overflow-hidden @max-[120px]/rail:justify-center @max-[120px]/rail:px-0">
        <span aria-hidden="true" class="flex-none w-7 h-7 rounded-[9px] bg-[conic-gradient(from_250deg,var(--color-tsl29-accent),oklch(0.6_0.14_220))]"></span>
        <span class="whitespace-nowrap font-bold text-[clamp(13px,6cqi,16px)] @max-[120px]/rail:hidden">Shelfspace</span>
      </div>
      <nav class="flex flex-col gap-[3px]">
        <a href="#" aria-current="page" class="flex items-center gap-[11px] min-h-11 px-3 rounded-[11px] text-sm font-medium whitespace-nowrap text-tsl29-mut no-underline transition-colors duration-[180ms] hover:text-tsl29-ink hover:bg-tsl29-hover aria-[current=page]:text-tsl29-accent aria-[current=page]:bg-tsl29-tint focus-visible:outline-2 focus-visible:outline-tsl29-accent focus-visible:outline-offset-2 @max-[120px]/rail:justify-center @max-[120px]/rail:px-0 @max-[120px]/rail:w-11 @max-[120px]/rail:mx-auto"><svg viewBox="0 0 24 24" aria-hidden="true" class="flex-none w-[19px] h-[19px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V2H6.5A2.5 2.5 0 0 0 4 4.5zM4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/></svg><span class="@max-[120px]/rail:hidden">Reading now</span><small class="ms-auto rounded-full px-2 py-[3px] text-[11px] font-semibold text-tsl29-mut bg-tsl29-chip @max-[220px]/rail:hidden">3</small></a>
        <a href="#" class="flex items-center gap-[11px] min-h-11 px-3 rounded-[11px] text-sm font-medium whitespace-nowrap text-tsl29-mut no-underline transition-colors duration-[180ms] hover:text-tsl29-ink hover:bg-tsl29-hover focus-visible:outline-2 focus-visible:outline-tsl29-accent focus-visible:outline-offset-2 @max-[120px]/rail:justify-center @max-[120px]/rail:px-0 @max-[120px]/rail:w-11 @max-[120px]/rail:mx-auto"><svg viewBox="0 0 24 24" aria-hidden="true" class="flex-none w-[19px] h-[19px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M6 2h12a2 2 0 0 1 2 2v18l-8-4-8 4V4a2 2 0 0 1 2-2z"/></svg><span class="@max-[120px]/rail:hidden">Saved</span><small class="ms-auto rounded-full px-2 py-[3px] text-[11px] font-semibold text-tsl29-mut bg-tsl29-chip @max-[220px]/rail:hidden">47</small></a>
        <a href="#" class="flex items-center gap-[11px] min-h-11 px-3 rounded-[11px] text-sm font-medium whitespace-nowrap text-tsl29-mut no-underline transition-colors duration-[180ms] hover:text-tsl29-ink hover:bg-tsl29-hover focus-visible:outline-2 focus-visible:outline-tsl29-accent focus-visible:outline-offset-2 @max-[120px]/rail:justify-center @max-[120px]/rail:px-0 @max-[120px]/rail:w-11 @max-[120px]/rail:mx-auto"><svg viewBox="0 0 24 24" aria-hidden="true" class="flex-none w-[19px] h-[19px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/></svg><span class="@max-[120px]/rail:hidden">History</span><small class="ms-auto rounded-full px-2 py-[3px] text-[11px] font-semibold text-tsl29-mut bg-tsl29-chip @max-[220px]/rail:hidden">210</small></a>
        <a href="#" class="flex items-center gap-[11px] min-h-11 px-3 rounded-[11px] text-sm font-medium whitespace-nowrap text-tsl29-mut no-underline transition-colors duration-[180ms] hover:text-tsl29-ink hover:bg-tsl29-hover focus-visible:outline-2 focus-visible:outline-tsl29-accent focus-visible:outline-offset-2 @max-[120px]/rail:justify-center @max-[120px]/rail:px-0 @max-[120px]/rail:w-11 @max-[120px]/rail:mx-auto"><svg viewBox="0 0 24 24" aria-hidden="true" class="flex-none w-[19px] h-[19px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><circle cx="12" cy="12" r="3"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3M4.9 4.9l2.1 2.1m10 10 2.1 2.1m0-14.2-2.1 2.1m-10 10-2.1 2.1"/></svg><span class="@max-[120px]/rail:hidden">Settings</span></a>
      </nav>
    </aside>
    <span aria-hidden="true" class="absolute inset-y-0 right-0 w-3.5 pointer-coarse:w-[22px] flex flex-col items-center justify-center gap-[3px] cursor-col-resize opacity-50 hover:opacity-100">
      <i class="w-[3px] h-[3px] rounded-full bg-tsl29-mut"></i><i class="w-[3px] h-[3px] rounded-full bg-tsl29-mut"></i><i class="w-[3px] h-[3px] rounded-full bg-tsl29-mut"></i>
    </span>
  </div>
  <main class="flex-1 min-w-0 p-8 overflow-y-auto [scrollbar-gutter:stable]">
    <h1 class="text-[22px] font-semibold leading-tight mb-2.5">Reading now</h1>
    <p class="max-w-[50ch] text-sm leading-[1.65] text-tsl29-mut text-pretty">Drag the dotted edge. Full &rarr; labels-only &rarr; icon rail: three densities from container queries &mdash; the sidebar reads its OWN width, never the viewport's.</p>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl29-bg: #101613;
  --color-tsl29-bg: oklch(0.13 0.012 155);
  --color-tsl29-panel: #161f1b;
  --color-tsl29-panel: oklch(0.17 0.016 155);
  --color-tsl29-ink: #e8f0ec;
  --color-tsl29-ink: oklch(0.94 0.005 155);
  --color-tsl29-mut: #929d97;
  --color-tsl29-mut: oklch(0.64 0.013 155);
  --color-tsl29-line: #343f39;
  --color-tsl29-line: oklch(0.28 0.017 155);
  --color-tsl29-accent: #5fdcae;
  --color-tsl29-accent: oklch(0.78 0.15 160);
  --color-tsl29-chip: rgb(232 240 236 / 0.08);
  --color-tsl29-chip: color-mix(in oklab, oklch(0.94 0.005 155) 8%, transparent);
  --color-tsl29-hover: rgb(232 240 236 / 0.06);
  --color-tsl29-hover: color-mix(in oklab, oklch(0.94 0.005 155) 6%, transparent);
  --color-tsl29-tint: rgb(95 220 174 / 0.14);
  --color-tsl29-tint: color-mix(in oklab, oklch(0.78 0.15 160) 14%, transparent);
  --font-tsl29-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tsl-29 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
```
