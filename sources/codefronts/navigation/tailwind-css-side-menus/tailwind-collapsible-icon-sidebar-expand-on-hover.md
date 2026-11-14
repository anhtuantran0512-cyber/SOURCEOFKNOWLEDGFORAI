---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-collapsible-icon-sidebar-expand-on-hover/"
title: "Tailwind Collapsible Icon Sidebar That Expands on Hover"
section: "navigation"
category: "tailwind-css-side-menus"
category_name: "Tailwind CSS Side Menus"
description: "A 60px icon rail that widens to 232px on hover or keyboard focus, fading in labels and badges after the width has started moving."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Collapsible Icon Sidebar That Expands on Hover
Source: https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-collapsible-icon-sidebar-expand-on-hover/

A 60px icon rail that widens to 232px on hover or keyboard focus, fading in labels and badges after the width has started moving. The port fixes the original's biggest flaw: the rail now expands over the page as a floating layer instead of shoving the content sideways on every mouse pass. Pure Tailwind.
## HTML
```html
<section class="tsm-04 relative flex w-full min-h-svh bg-tsm04-bg font-tsm04-sans text-tsm04-ink" aria-label="Collapsible icon sidebar expanding on hover demo">
  <div aria-hidden="true" class="w-[60px] shrink-0"></div>
  <nav data-tsm04-rail aria-label="Main" class="group/rail absolute inset-y-0 left-0 z-20 flex w-[60px] flex-col overflow-hidden border-r border-tsm04-acc/15 bg-tsm04-rail py-4 transition-[width,box-shadow] delay-150 duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] hover:w-[232px] hover:shadow-[12px_0_40px_oklch(0_0_0/0.55)] hover:delay-0 focus-within:w-[232px] focus-within:shadow-[12px_0_40px_oklch(0_0_0/0.55)] motion-reduce:transition-none">
    <div class="mb-6 flex items-center whitespace-nowrap">
      <span class="grid w-[60px] shrink-0 place-items-center"><span aria-hidden="true" class="grid size-9 place-items-center rounded-[9px] bg-tsm04-acc text-base font-extrabold text-black transition-[border-radius] duration-300 group-hover/rail:rounded-full">Z</span></span>
      <span class="flex-1 text-[13px] font-semibold opacity-0 transition-opacity duration-200 group-hover/rail:opacity-100 group-hover/rail:delay-75 group-focus-within/rail:opacity-100">Zenith</span>
    </div>
    <ul class="flex-1">
      <li><a href="#" class="group/l relative flex h-12 w-full items-center overflow-hidden whitespace-nowrap text-tsm04-mut transition-colors hover:bg-tsm04-acc/8 hover:text-tsm04-ink focus-visible:bg-tsm04-acc/8 focus-visible:text-tsm04-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm04-acc aria-[current=page]:bg-tsm04-acc/10 aria-[current=page]:text-tsm04-ink aria-[current=page]:after:absolute aria-[current=page]:after:inset-y-3 aria-[current=page]:after:left-0 aria-[current=page]:after:w-[3px] aria-[current=page]:after:rounded-r-full aria-[current=page]:after:bg-tsm04-acc" aria-current="page"><span class="grid h-12 w-[60px] shrink-0 place-items-center transition-colors group-hover/l:text-tsm04-acc group-aria-[current=page]/l:text-tsm04-acc2"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg></span><span class="flex-1 text-[13px] font-semibold opacity-0 transition-opacity duration-200 group-hover/rail:opacity-100 group-hover/rail:delay-75 group-focus-within/rail:opacity-100">Dashboard</span></a></li>
      <li><a href="#" class="group/l relative flex h-12 w-full items-center overflow-hidden whitespace-nowrap text-tsm04-mut transition-colors hover:bg-tsm04-acc/8 hover:text-tsm04-ink focus-visible:bg-tsm04-acc/8 focus-visible:text-tsm04-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm04-acc aria-[current=page]:bg-tsm04-acc/10 aria-[current=page]:text-tsm04-ink aria-[current=page]:after:absolute aria-[current=page]:after:inset-y-3 aria-[current=page]:after:left-0 aria-[current=page]:after:w-[3px] aria-[current=page]:after:rounded-r-full aria-[current=page]:after:bg-tsm04-acc"><span class="grid h-12 w-[60px] shrink-0 place-items-center transition-colors group-hover/l:text-tsm04-acc group-aria-[current=page]/l:text-tsm04-acc2"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 5-6"/></svg></span><span class="flex-1 text-[13px] font-semibold opacity-0 transition-opacity duration-200 group-hover/rail:opacity-100 group-hover/rail:delay-75 group-focus-within/rail:opacity-100">Analytics</span><span class="mr-3 rounded-full bg-tsm04-acc/20 px-1.5 text-[10px] font-bold text-tsm04-acc2 opacity-0 transition-opacity group-hover/rail:opacity-100 group-focus-within/rail:opacity-100">5</span></a></li>
      <li><a href="#" class="group/l relative flex h-12 w-full items-center overflow-hidden whitespace-nowrap text-tsm04-mut transition-colors hover:bg-tsm04-acc/8 hover:text-tsm04-ink focus-visible:bg-tsm04-acc/8 focus-visible:text-tsm04-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm04-acc aria-[current=page]:bg-tsm04-acc/10 aria-[current=page]:text-tsm04-ink aria-[current=page]:after:absolute aria-[current=page]:after:inset-y-3 aria-[current=page]:after:left-0 aria-[current=page]:after:w-[3px] aria-[current=page]:after:rounded-r-full aria-[current=page]:after:bg-tsm04-acc"><span class="grid h-12 w-[60px] shrink-0 place-items-center transition-colors group-hover/l:text-tsm04-acc group-aria-[current=page]/l:text-tsm04-acc2"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg></span><span class="flex-1 text-[13px] font-semibold opacity-0 transition-opacity duration-200 group-hover/rail:opacity-100 group-hover/rail:delay-75 group-focus-within/rail:opacity-100">Projects</span></a></li>
      <li><a href="#" class="group/l relative flex h-12 w-full items-center overflow-hidden whitespace-nowrap text-tsm04-mut transition-colors hover:bg-tsm04-acc/8 hover:text-tsm04-ink focus-visible:bg-tsm04-acc/8 focus-visible:text-tsm04-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm04-acc aria-[current=page]:bg-tsm04-acc/10 aria-[current=page]:text-tsm04-ink aria-[current=page]:after:absolute aria-[current=page]:after:inset-y-3 aria-[current=page]:after:left-0 aria-[current=page]:after:w-[3px] aria-[current=page]:after:rounded-r-full aria-[current=page]:after:bg-tsm04-acc"><span class="grid h-12 w-[60px] shrink-0 place-items-center transition-colors group-hover/l:text-tsm04-acc group-aria-[current=page]/l:text-tsm04-acc2"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg></span><span class="flex-1 text-[13px] font-semibold opacity-0 transition-opacity duration-200 group-hover/rail:opacity-100 group-hover/rail:delay-75 group-focus-within/rail:opacity-100">Messages</span><span class="mr-3 rounded-full bg-tsm04-acc/20 px-1.5 text-[10px] font-bold text-tsm04-acc2 opacity-0 transition-opacity group-hover/rail:opacity-100 group-focus-within/rail:opacity-100">9</span></a></li>
      <li aria-hidden="true" class="mx-auto my-2 h-px w-4/5 bg-tsm04-acc/15"></li>
      <li><a href="#" class="group/l relative flex h-12 w-full items-center overflow-hidden whitespace-nowrap text-tsm04-mut transition-colors hover:bg-tsm04-acc/8 hover:text-tsm04-ink focus-visible:bg-tsm04-acc/8 focus-visible:text-tsm04-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm04-acc aria-[current=page]:bg-tsm04-acc/10 aria-[current=page]:text-tsm04-ink aria-[current=page]:after:absolute aria-[current=page]:after:inset-y-3 aria-[current=page]:after:left-0 aria-[current=page]:after:w-[3px] aria-[current=page]:after:rounded-r-full aria-[current=page]:after:bg-tsm04-acc"><span class="grid h-12 w-[60px] shrink-0 place-items-center transition-colors group-hover/l:text-tsm04-acc group-aria-[current=page]/l:text-tsm04-acc2"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .8-1 1.5v.7"/><path d="M12 17h.01"/></svg></span><span class="flex-1 text-[13px] font-semibold opacity-0 transition-opacity duration-200 group-hover/rail:opacity-100 group-hover/rail:delay-75 group-focus-within/rail:opacity-100">Help</span></a></li>
      <li><a href="#" class="group/l relative flex h-12 w-full items-center overflow-hidden whitespace-nowrap text-tsm04-mut transition-colors hover:bg-tsm04-acc/8 hover:text-tsm04-ink focus-visible:bg-tsm04-acc/8 focus-visible:text-tsm04-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm04-acc aria-[current=page]:bg-tsm04-acc/10 aria-[current=page]:text-tsm04-ink aria-[current=page]:after:absolute aria-[current=page]:after:inset-y-3 aria-[current=page]:after:left-0 aria-[current=page]:after:w-[3px] aria-[current=page]:after:rounded-r-full aria-[current=page]:after:bg-tsm04-acc"><span class="grid h-12 w-[60px] shrink-0 place-items-center transition-colors group-hover/l:text-tsm04-acc group-aria-[current=page]/l:text-tsm04-acc2"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6h9"/><path d="M19 6h1"/><circle cx="16" cy="6" r="2.5"/><path d="M4 12h2"/><path d="M12 12h8"/><circle cx="9" cy="12" r="2.5"/><path d="M4 18h11"/><circle cx="18" cy="18" r="2.5"/></svg></span><span class="flex-1 text-[13px] font-semibold opacity-0 transition-opacity duration-200 group-hover/rail:opacity-100 group-hover/rail:delay-75 group-focus-within/rail:opacity-100">Settings</span></a></li>
    </ul>
    <div class="flex items-center overflow-hidden border-t border-tsm04-acc/15 pt-3 whitespace-nowrap">
      <span class="grid w-[60px] shrink-0 place-items-center"><span aria-hidden="true" class="grid size-[30px] place-items-center rounded-full bg-linear-135 from-amber-500 to-red-500 text-[11px] font-bold text-black">MK</span></span>
      <span class="flex-1 text-[13px] font-semibold opacity-0 transition-opacity duration-200 group-hover/rail:opacity-100 group-hover/rail:delay-75 group-focus-within/rail:opacity-100"><span class="block text-xs">M. Kowalski</span><span class="block text-[10px] font-normal text-tsm04-mut">Admin</span></span>
    </div>
  </nav>
  <div class="min-w-0 flex-1 px-6 py-7">
    <div class="mx-auto max-w-3xl">
      <h1 class="text-xl font-bold">Dashboard</h1>
      <p class="mt-2 mb-6 max-w-prose text-[13px] leading-relaxed text-tsm04-mut text-pretty">Hover the icon rail — or Tab into it — to expand. It floats over this page, so nothing here shifts.</p>
      <div class="grid grid-cols-2 gap-2.5 md:grid-cols-4">
      <div class="rounded-xl border border-tsm04-acc/15 bg-tsm04-surface p-4"><p class="text-xl font-bold tabular-nums text-tsm04-acc2">41</p><p class="mt-1 text-[11px] text-tsm04-mut">Active projects</p></div>
      <div class="rounded-xl border border-tsm04-acc/15 bg-tsm04-surface p-4"><p class="text-xl font-bold tabular-nums text-tsm04-acc2">98%</p><p class="mt-1 text-[11px] text-tsm04-mut">Health score</p></div>
      <div class="rounded-xl border border-tsm04-acc/15 bg-tsm04-surface p-4"><p class="text-xl font-bold tabular-nums text-tsm04-acc2">$74k</p><p class="mt-1 text-[11px] text-tsm04-mut">Monthly revenue</p></div>
      <div class="rounded-xl border border-tsm04-acc/15 bg-tsm04-surface p-4"><p class="text-xl font-bold tabular-nums text-tsm04-acc2">1.2k</p><p class="mt-1 text-[11px] text-tsm04-mut">Team members</p></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsm04-bg: #09090b;
  --color-tsm04-bg: oklch(0.141 0.004 285.8);
  --color-tsm04-surface: #18181b;
  --color-tsm04-surface: oklch(0.21 0.006 285.9);
  --color-tsm04-rail: #0f0f12;
  --color-tsm04-rail: oklch(0.17 0.006 285.7);
  --color-tsm04-acc: #f59e0b;
  --color-tsm04-acc: oklch(0.769 0.165 70.1);
  --color-tsm04-acc2: #fbbf24;
  --color-tsm04-acc2: oklch(0.837 0.164 84.4);
  --color-tsm04-ink: #fafafa;
  --color-tsm04-ink: oklch(0.985 0 0);
  --color-tsm04-mut: #a1a1aa;
  --color-tsm04-mut: oklch(0.712 0.013 286.1);
  --font-tsm04-sans: 'Geist', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tsm-04 {
  width: 100%;
  min-height: 100svh;
}
```
