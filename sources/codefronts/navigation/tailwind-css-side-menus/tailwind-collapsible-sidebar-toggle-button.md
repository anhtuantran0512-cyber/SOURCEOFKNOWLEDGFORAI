---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-collapsible-sidebar-toggle-button/"
title: "Tailwind Collapsible Sidebar with Toggle Button (No JS)"
section: "navigation"
category: "tailwind-css-side-menus"
category_name: "Tailwind CSS Side Menus"
description: "A sidebar that animates between a 240px full layout and a 64px icon rail at the press of a pivot button, with labels, badges and the user card collapsing in…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Collapsible Sidebar with Toggle Button (No JS)
Source: https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-collapsible-sidebar-toggle-button/

A sidebar that animates between a 240px full layout and a 64px icon rail at the press of a pivot button, with labels, badges and the user card collapsing in sync via max-w-0 opacity-0. The toggle button flips its arrow and its accessible name (“Collapse sidebar” ↔ “Expand sidebar”), and collapsed labels stay in the accessibility tree. Zero JavaScript.
## HTML
```html
<section class="tsm-15 group flex w-full min-h-svh bg-tsm15-bg font-tsm15-sans text-tsm15-ink" aria-label="Collapsible sidebar with toggle button demo">
  <input type="checkbox" id="tsm-15-toggle" class="peer sr-only">
  <nav aria-label="Main" class="relative flex w-60 shrink-0 flex-col overflow-hidden border-r border-tsm15-acc/12 bg-tsm15-nav transition-[width] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-checked:w-16 motion-reduce:transition-none">
    <div class="mb-3 flex items-center gap-2 border-b border-tsm15-acc/12 px-3.5 py-4 group-has-checked:flex-col group-has-checked:px-0">
      <span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-[9px] bg-linear-135 from-tsm15-acc to-tsm15-acc2 text-base font-extrabold text-white">R</span>
      <span class="max-w-40 flex-1 text-[15px] font-extrabold overflow-hidden whitespace-nowrap transition-[max-width,opacity,margin] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-checked:max-w-0 group-has-checked:opacity-0 motion-reduce:transition-none">Recto</span>
      <label for="tsm-15-toggle" data-tsm15-collapse class="grid size-11 shrink-0 cursor-pointer place-items-center rounded-full text-tsm15-mut transition-colors hover:bg-tsm15-acc hover:text-white group-has-[input:focus-visible]:outline-2 group-has-[input:focus-visible]:outline-tsm15-acc2">
        <span class="sr-only group-has-checked:hidden">Collapse sidebar</span><span class="sr-only hidden group-has-checked:inline">Expand sidebar</span>
        <svg class="size-4 transition-transform duration-350 group-has-checked:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 6-6 6 6 6"/></svg>
      </label>
    </div>
    <ul class="grid flex-1 content-start gap-1 px-2.5 group-has-checked:px-[7px]">
      <li><a href="#" class="group/l flex min-h-11 items-center overflow-hidden rounded-[10px] px-1.5 text-[13px] font-semibold text-tsm15-mut transition-colors hover:bg-tsm15-acc/8 hover:text-tsm15-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm15-acc2 aria-[current=page]:bg-tsm15-acc/10 aria-[current=page]:text-tsm15-acc2" aria-current="page"><span class="grid size-9 shrink-0 place-items-center rounded-lg transition-colors group-hover/l:bg-tsm15-acc/15 group-aria-[current=page]/l:bg-tsm15-acc/18"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg></span><span class="ml-1.5 max-w-40 overflow-hidden whitespace-nowrap transition-[max-width,opacity,margin] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-checked:max-w-0 group-has-checked:opacity-0 motion-reduce:transition-none group-has-checked:ml-0">Dashboard</span></a></li>
      <li><a href="#" class="group/l flex min-h-11 items-center overflow-hidden rounded-[10px] px-1.5 text-[13px] font-semibold text-tsm15-mut transition-colors hover:bg-tsm15-acc/8 hover:text-tsm15-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm15-acc2 aria-[current=page]:bg-tsm15-acc/10 aria-[current=page]:text-tsm15-acc2"><span class="grid size-9 shrink-0 place-items-center rounded-lg transition-colors group-hover/l:bg-tsm15-acc/15 group-aria-[current=page]/l:bg-tsm15-acc/18"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 5-6"/></svg></span><span class="ml-1.5 max-w-40 overflow-hidden whitespace-nowrap transition-[max-width,opacity,margin] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-checked:max-w-0 group-has-checked:opacity-0 motion-reduce:transition-none group-has-checked:ml-0">Analytics</span><span class="ml-auto rounded-full bg-tsm15-acc/20 px-2 py-0.5 text-[10px] font-bold text-tsm15-acc2 transition-opacity group-has-checked:opacity-0">9</span></a></li>
      <li><a href="#" class="group/l flex min-h-11 items-center overflow-hidden rounded-[10px] px-1.5 text-[13px] font-semibold text-tsm15-mut transition-colors hover:bg-tsm15-acc/8 hover:text-tsm15-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm15-acc2 aria-[current=page]:bg-tsm15-acc/10 aria-[current=page]:text-tsm15-acc2"><span class="grid size-9 shrink-0 place-items-center rounded-lg transition-colors group-hover/l:bg-tsm15-acc/15 group-aria-[current=page]/l:bg-tsm15-acc/18"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m12 3 8 4.5v9L12 21l-8-4.5v-9z"/><path d="m4 7.5 8 4.5 8-4.5"/><path d="M12 12v9"/></svg></span><span class="ml-1.5 max-w-40 overflow-hidden whitespace-nowrap transition-[max-width,opacity,margin] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-checked:max-w-0 group-has-checked:opacity-0 motion-reduce:transition-none group-has-checked:ml-0">Products</span></a></li>
      <li><a href="#" class="group/l flex min-h-11 items-center overflow-hidden rounded-[10px] px-1.5 text-[13px] font-semibold text-tsm15-mut transition-colors hover:bg-tsm15-acc/8 hover:text-tsm15-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm15-acc2 aria-[current=page]:bg-tsm15-acc/10 aria-[current=page]:text-tsm15-acc2"><span class="grid size-9 shrink-0 place-items-center rounded-lg transition-colors group-hover/l:bg-tsm15-acc/15 group-aria-[current=page]/l:bg-tsm15-acc/18"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 4h2l2.4 11h11L21 8H6.2"/><circle cx="9" cy="19.5" r="1.5"/><circle cx="17" cy="19.5" r="1.5"/></svg></span><span class="ml-1.5 max-w-40 overflow-hidden whitespace-nowrap transition-[max-width,opacity,margin] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-checked:max-w-0 group-has-checked:opacity-0 motion-reduce:transition-none group-has-checked:ml-0">Orders</span><span class="ml-auto rounded-full bg-tsm15-acc/20 px-2 py-0.5 text-[10px] font-bold text-tsm15-acc2 transition-opacity group-has-checked:opacity-0">3</span></a></li>
      <li><a href="#" class="group/l flex min-h-11 items-center overflow-hidden rounded-[10px] px-1.5 text-[13px] font-semibold text-tsm15-mut transition-colors hover:bg-tsm15-acc/8 hover:text-tsm15-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm15-acc2 aria-[current=page]:bg-tsm15-acc/10 aria-[current=page]:text-tsm15-acc2"><span class="grid size-9 shrink-0 place-items-center rounded-lg transition-colors group-hover/l:bg-tsm15-acc/15 group-aria-[current=page]/l:bg-tsm15-acc/18"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7"/><path d="M18 14.5a6.5 6.5 0 0 1 3.5 5.5"/></svg></span><span class="ml-1.5 max-w-40 overflow-hidden whitespace-nowrap transition-[max-width,opacity,margin] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-checked:max-w-0 group-has-checked:opacity-0 motion-reduce:transition-none group-has-checked:ml-0">Customers</span></a></li>
      <li><a href="#" class="group/l flex min-h-11 items-center overflow-hidden rounded-[10px] px-1.5 text-[13px] font-semibold text-tsm15-mut transition-colors hover:bg-tsm15-acc/8 hover:text-tsm15-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm15-acc2 aria-[current=page]:bg-tsm15-acc/10 aria-[current=page]:text-tsm15-acc2"><span class="grid size-9 shrink-0 place-items-center rounded-lg transition-colors group-hover/l:bg-tsm15-acc/15 group-aria-[current=page]/l:bg-tsm15-acc/18"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6h9"/><path d="M19 6h1"/><circle cx="16" cy="6" r="2.5"/><path d="M4 12h2"/><path d="M12 12h8"/><circle cx="9" cy="12" r="2.5"/><path d="M4 18h11"/><circle cx="18" cy="18" r="2.5"/></svg></span><span class="ml-1.5 max-w-40 overflow-hidden whitespace-nowrap transition-[max-width,opacity,margin] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-checked:max-w-0 group-has-checked:opacity-0 motion-reduce:transition-none group-has-checked:ml-0">Settings</span></a></li>
    </ul>
    <div class="flex items-center overflow-hidden border-t border-tsm15-acc/12 px-3 py-4 group-has-checked:justify-center group-has-checked:px-0">
      <span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full bg-linear-135 from-tsm15-acc to-violet-500 text-xs font-bold text-white">WP</span>
      <span class="ml-2.5 max-w-40 overflow-hidden whitespace-nowrap transition-[max-width,opacity,margin] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-checked:max-w-0 group-has-checked:opacity-0 motion-reduce:transition-none group-has-checked:ml-0"><span class="block text-xs font-bold">W. Park</span><span class="block text-[10px] text-tsm15-mut">Admin</span></span>
    </div>
  </nav>
  <div class="min-w-0 flex-1 p-6">
    <div class="mx-auto max-w-3xl">
      <h1 class="text-xl font-extrabold">Dashboard</h1>
      <p class="mt-1.5 mb-6 max-w-prose text-[13px] leading-relaxed text-tsm15-mut text-pretty">Press the arrow beside the logo to collapse the sidebar to icons and back. One hidden checkbox, one width transition.</p>
      <div class="grid grid-cols-2 gap-2.5 md:grid-cols-4">
          <div class="rounded-xl border border-tsm15-acc/12 bg-tsm15-surface p-4"><p class="text-[22px] font-extrabold tabular-nums text-tsm15-acc2">$82k</p><p class="mt-1 text-[11px] text-tsm15-mut">Revenue</p></div>
          <div class="rounded-xl border border-tsm15-acc/12 bg-tsm15-surface p-4"><p class="text-[22px] font-extrabold tabular-nums text-tsm15-acc2">1,247</p><p class="mt-1 text-[11px] text-tsm15-mut">Orders</p></div>
          <div class="rounded-xl border border-tsm15-acc/12 bg-tsm15-surface p-4"><p class="text-[22px] font-extrabold tabular-nums text-tsm15-acc2">98%</p><p class="mt-1 text-[11px] text-tsm15-mut">Uptime</p></div>
          <div class="rounded-xl border border-tsm15-acc/12 bg-tsm15-surface p-4"><p class="text-[22px] font-extrabold tabular-nums text-tsm15-acc2">4.9 / 5</p><p class="mt-1 text-[11px] text-tsm15-mut">Rating</p></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsm15-bg: #09090b;
  --color-tsm15-bg: oklch(0.141 0.004 285.8);
  --color-tsm15-surface: #141418;
  --color-tsm15-surface: oklch(0.193 0.008 285.6);
  --color-tsm15-nav: #0f0f12;
  --color-tsm15-nav: oklch(0.17 0.006 285.7);
  --color-tsm15-acc: #e11d48;
  --color-tsm15-acc: oklch(0.586 0.222 17.6);
  --color-tsm15-acc2: #fb7185;
  --color-tsm15-acc2: oklch(0.719 0.169 13.4);
  --color-tsm15-ink: #f1f5f9;
  --color-tsm15-ink: oklch(0.968 0.007 247.9);
  --color-tsm15-mut: #a1a1aa;
  --color-tsm15-mut: oklch(0.712 0.013 286.1);
  --font-tsm15-sans: 'Sora', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tsm-15 {
  width: 100%;
  min-height: 100svh;
}
```
